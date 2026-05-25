"""Run the Earthquake Japan source-consistent V1 control.

Inputs are fixed local artifacts only:
- raw USGS catalog CSV
- fixed future 3-hour event-label CSV

This script performs Omega calculation and V1 controls. It does not fetch
external data, execute notebooks, or reconstruct future event-window labels.
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np
import pandas as pd


RAW_CATALOG_PATH = Path("data/earthquake_japan_usgs_fixed_catalog_2020-01-01_2025-01-01.csv")
LABEL_PATH = Path("data/earthquake_japan_future_3h_event_labels_2020-01-01_2025-01-01.csv")
RESULT_DIR = Path("results")

EXPECTED_RAW_SHA256 = "b04406376de91adf6c4ce802d228d3311275b5055b7146471446918b1931f1c5"
EXPECTED_LABEL_SHA256 = "39278964dbfd5535a37b4ec5e4856a240f64686b8caa099cf52d1741738f350f"

ORIGINAL_CSV = RESULT_DIR / "earthquake_source_consistent_v1_original_2026-05-25.csv"
TEMPORAL_CSV = RESULT_DIR / "earthquake_source_consistent_v1_temporal_shifts_2026-05-25.csv"
SHUFFLED_CSV = RESULT_DIR / "earthquake_source_consistent_v1_shuffled_runs_2026-05-25.csv"
SUMMARY_JSON = RESULT_DIR / "earthquake_source_consistent_v1_summary_2026-05-25.json"

ROLLING_WINDOW = 20
HIGH_OMEGA_Q = 0.99
TEMPORAL_SHIFTS = [30, 60, 120]
SHUFFLE_RUNS = 100
SHUFFLE_SEED_START = 20260523


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def require_hash(path: Path, expected: str) -> str:
    actual = sha256_file(path)
    if actual != expected:
        raise SystemExit(f"SHA256 mismatch for {path}: expected {expected}, got {actual}")
    return actual


def summarize_labels(
    condition: str,
    labels: np.ndarray,
    high_omega: np.ndarray,
    q_omega: float,
    shift: int | None = None,
    seed: int | None = None,
    run: int | None = None,
) -> dict[str, float | int | str | None]:
    n_rows = int(labels.size)
    total_event_count = int(labels.sum())
    baseline = float(labels.mean())
    n_high = int(high_omega.sum())
    n_event_high = int(labels[high_omega].sum())
    p_event_high = float(labels[high_omega].mean()) if n_high else math.nan
    ratio = float(p_event_high / baseline) if baseline else math.nan
    return {
        "domain": "Earthquake Japan",
        "condition": condition,
        "shift": shift,
        "run": run,
        "seed": seed,
        "n_rows": n_rows,
        "total_event_count": total_event_count,
        "baseline": baseline,
        "q_omega_0.99": q_omega,
        "n_high": n_high,
        "n_event_high": n_event_high,
        "p_collapse_given_high_omega": p_event_high,
        "ratio": ratio,
    }


def assert_close(name: str, actual: float, expected: float, tol: float = 1e-12) -> None:
    if not math.isclose(actual, expected, rel_tol=tol, abs_tol=tol):
        raise SystemExit(f"{name} mismatch: expected {expected}, got {actual}")


def main() -> None:
    raw_sha = require_hash(RAW_CATALOG_PATH, EXPECTED_RAW_SHA256)
    label_sha = require_hash(LABEL_PATH, EXPECTED_LABEL_SHA256)

    raw = pd.read_csv(RAW_CATALOG_PATH)
    labels = pd.read_csv(LABEL_PATH)
    if len(raw) != len(labels):
        raise SystemExit(f"Row count mismatch: raw={len(raw)}, labels={len(labels)}")
    if not raw["time"].equals(labels["time"]) or not raw["id"].equals(labels["id"]):
        raise SystemExit("Raw catalog and label file do not align on time/id")

    parsed_time = pd.to_datetime(raw["time"], utc=True)
    if not parsed_time.is_monotonic_increasing:
        raise SystemExit("Raw catalog is not sorted ascending by time")

    mag = raw["mag"].astype(float)
    delta_mag = mag.diff()
    intensity = mag.rolling(window=ROLLING_WINDOW).std()
    gradient = delta_mag.abs()
    omega = intensity * gradient

    event_labels_full = labels["future_3h_mag_ge_5_5_event"].astype(int)
    if not set(event_labels_full.unique()).issubset({0, 1}):
        raise SystemExit("Event label column contains values outside {0, 1}")

    valid = delta_mag.notna() & intensity.notna() & omega.notna()
    valid_labels = event_labels_full.loc[valid].to_numpy(dtype=int)
    valid_omega = omega.loc[valid]
    q_omega = float(valid_omega.quantile(HIGH_OMEGA_Q))
    high_omega = (valid_omega > q_omega).to_numpy(dtype=bool)

    original = summarize_labels("original", valid_labels, high_omega, q_omega)

    if int(original["n_rows"]) != 4062:
        raise SystemExit(f"n_rows mismatch: expected 4062, got {original['n_rows']}")
    if int(original["total_event_count"]) != 99:
        raise SystemExit(
            f"total_event_count mismatch: expected 99, got {original['total_event_count']}"
        )
    assert_close("baseline", float(original["baseline"]), 0.024372230428360413)
    if int(original["n_high"]) != 41:
        raise SystemExit(f"n_high mismatch: expected 41, got {original['n_high']}")
    if int(original["n_event_high"]) != 6:
        raise SystemExit(
            f"n_event_high mismatch: expected 6, got {original['n_event_high']}"
        )
    assert_close(
        "P(collapse | high Omega)",
        float(original["p_collapse_given_high_omega"]),
        0.14634146341463414,
    )
    assert_close("ratio", float(original["ratio"]), 6.004434589800443)

    temporal_rows = []
    for shift in TEMPORAL_SHIFTS:
        shifted_labels = np.roll(valid_labels, shift)
        row = summarize_labels(
            f"circular_shift_+{shift}",
            shifted_labels,
            high_omega,
            q_omega,
            shift=shift,
        )
        if int(row["total_event_count"]) != int(original["total_event_count"]):
            raise SystemExit(f"Shift +{shift} did not preserve event count")
        temporal_rows.append(row)

    shuffled_rows = []
    for run in range(SHUFFLE_RUNS):
        seed = SHUFFLE_SEED_START + run
        shuffled_labels = np.random.default_rng(seed).permutation(valid_labels)
        row = summarize_labels(
            "shuffled_labels",
            shuffled_labels,
            high_omega,
            q_omega,
            seed=seed,
            run=run + 1,
        )
        if int(row["total_event_count"]) != int(original["total_event_count"]):
            raise SystemExit(f"Shuffle run {run + 1} did not preserve event count")
        shuffled_rows.append(row)

    shuffled_frame = pd.DataFrame(shuffled_rows)
    shuffled_summary = {
        "runs": SHUFFLE_RUNS,
        "mean_p_collapse_given_high_omega": float(
            shuffled_frame["p_collapse_given_high_omega"].mean()
        ),
        "median_p_collapse_given_high_omega": float(
            shuffled_frame["p_collapse_given_high_omega"].median()
        ),
        "min_p_collapse_given_high_omega": float(
            shuffled_frame["p_collapse_given_high_omega"].min()
        ),
        "max_p_collapse_given_high_omega": float(
            shuffled_frame["p_collapse_given_high_omega"].max()
        ),
        "mean_ratio": float(shuffled_frame["ratio"].mean()),
        "median_ratio": float(shuffled_frame["ratio"].median()),
        "min_ratio": float(shuffled_frame["ratio"].min()),
        "max_ratio": float(shuffled_frame["ratio"].max()),
        "mean_n_event_high": float(shuffled_frame["n_event_high"].mean()),
        "min_n_event_high": int(shuffled_frame["n_event_high"].min()),
        "max_n_event_high": int(shuffled_frame["n_event_high"].max()),
    }

    RESULT_DIR.mkdir(parents=True, exist_ok=True)
    pd.DataFrame([original]).to_csv(ORIGINAL_CSV, index=False)
    pd.DataFrame(temporal_rows).to_csv(TEMPORAL_CSV, index=False)
    shuffled_frame.to_csv(SHUFFLED_CSV, index=False)

    summary = {
        "input": {
            "raw_catalog_path": str(RAW_CATALOG_PATH),
            "raw_catalog_sha256": raw_sha,
            "label_path": str(LABEL_PATH),
            "label_sha256": label_sha,
            "raw_rows": int(len(raw)),
            "valid_evaluation_rows": int(original["n_rows"]),
            "actual_first_time": str(raw.loc[0, "time"]),
            "actual_last_time": str(raw.loc[len(raw) - 1, "time"]),
        },
        "definitions": {
            "I": "rolling standard deviation of magnitude, window 20",
            "G": "absolute magnitude change",
            "Omega": "I * G",
            "event_label": "fixed future 3-hour window contains later mag >= 5.5",
            "high_omega": "Omega > q(0.99)",
            "event_definition_independent_of_omega": True,
            "temporal_shift": "circular row shifts",
            "shuffle_runs": SHUFFLE_RUNS,
            "shuffle_seed_start": SHUFFLE_SEED_START,
        },
        "original": original,
        "temporal_shifts": temporal_rows,
        "shuffled_label_controls": shuffled_summary,
        "outputs": {
            "original_csv": str(ORIGINAL_CSV),
            "temporal_shifts_csv": str(TEMPORAL_CSV),
            "shuffled_runs_csv": str(SHUFFLED_CSV),
            "summary_json": str(SUMMARY_JSON),
        },
    }
    SUMMARY_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
