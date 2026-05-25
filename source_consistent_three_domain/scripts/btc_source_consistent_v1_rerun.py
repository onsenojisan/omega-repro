"""Run the BTC source-consistent V1 structural concentration control.

This script reads only the fixed local raw OHLC snapshot. It does not fetch
external data and does not execute notebooks.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd


INPUT_FILE = Path("data/btc_fixed_ohlc_2024-05-25_2026-05-25.csv")
EXPECTED_SHA256 = "d856e196192be7a6776d61b3d3008618ae588091578b68407507a5dcdd215adb"

RESULTS_DIR = Path("results")
ORIGINAL_OUT = RESULTS_DIR / "btc_source_consistent_v1_original_2026-05-25.csv"
TEMPORAL_OUT = RESULTS_DIR / "btc_source_consistent_v1_temporal_shifts_2026-05-25.csv"
SHUFFLED_OUT = RESULTS_DIR / "btc_source_consistent_v1_shuffled_runs_2026-05-25.csv"
SUMMARY_OUT = RESULTS_DIR / "btc_source_consistent_v1_summary_2026-05-25.json"

ROLLING_WINDOW = 20
EVENT_Q = 0.95
OMEGA_Q = 0.99
TEMPORAL_SHIFTS = [30, 60, 120]
SHUFFLE_RUNS = 100
SHUFFLE_SEED_BASE = 20260525
MISSING_CALENDAR_DATE = "2026-05-24"


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require_fixed_input() -> str:
    if not INPUT_FILE.exists():
        raise FileNotFoundError(f"fixed snapshot not found: {INPUT_FILE}")
    actual = sha256_file(INPUT_FILE)
    if actual != EXPECTED_SHA256:
        raise RuntimeError(
            f"fixed snapshot SHA256 mismatch: expected {EXPECTED_SHA256}, got {actual}"
        )
    return actual


def calendar_gap_metadata(raw: pd.DataFrame) -> dict[str, object]:
    dates = pd.to_datetime(raw["Date"])
    full = pd.date_range(dates.min(), dates.max(), freq="D")
    missing = full.difference(dates)
    return {
        "inclusive_calendar_days": int(len(full)),
        "calendar_day_gaps": int(len(missing)),
        "missing_calendar_dates": [date.strftime("%Y-%m-%d") for date in missing],
    }


def load_eligible_rows() -> tuple[pd.DataFrame, dict[str, object]]:
    raw = pd.read_csv(INPUT_FILE)
    required = ["Date", "High", "Low", "Close"]
    missing = [col for col in required if col not in raw.columns]
    if missing:
        raise ValueError(f"missing required columns: {missing}")

    work = raw.copy()
    work["Date"] = pd.to_datetime(work["Date"])
    for col in ["High", "Low", "Close"]:
        work[col] = pd.to_numeric(work[col], errors="raise")

    work["return"] = work["Close"].pct_change()
    work["I"] = work["return"].rolling(window=ROLLING_WINDOW).std()
    work["G"] = work["return"].abs()
    work["Omega"] = work["I"] * work["G"]
    work["intraday_range"] = (work["High"] - work["Low"]) / work["Close"]

    eligible = work.dropna(subset=["return", "I", "G", "Omega", "intraday_range"]).copy()
    q_event = float(eligible["intraday_range"].quantile(EVENT_Q))
    q_omega = float(eligible["Omega"].quantile(OMEGA_Q))
    eligible["collapse"] = eligible["intraday_range"] > q_event
    eligible["high_omega"] = eligible["Omega"] > q_omega

    metadata = {
        "raw_rows": int(len(raw)),
        "raw_first_date": str(raw["Date"].iloc[0]),
        "raw_last_date": str(raw["Date"].iloc[-1]),
        "valid_evaluation_rows": int(len(eligible)),
        "valid_first_date": eligible["Date"].dt.strftime("%Y-%m-%d").iloc[0],
        "valid_last_date": eligible["Date"].dt.strftime("%Y-%m-%d").iloc[-1],
        "q_event_0.95": q_event,
        "q_omega_0.99": q_omega,
        **calendar_gap_metadata(raw),
    }
    return eligible, metadata


def evaluate(labels: np.ndarray, high_omega: np.ndarray) -> dict[str, object]:
    n_rows = int(len(labels))
    total_event_count = int(labels.sum())
    baseline = float(total_event_count / n_rows) if n_rows else float("nan")
    n_high = int(high_omega.sum())
    n_event_high = int(labels[high_omega].sum())
    p_high = float(n_event_high / n_high) if n_high else float("nan")
    ratio = float(p_high / baseline) if baseline else float("nan")
    return {
        "n_rows": n_rows,
        "total_event_count": total_event_count,
        "baseline_p_collapse": baseline,
        "n_high": n_high,
        "n_event_high": n_event_high,
        "p_collapse_given_high_omega": p_high,
        "ratio": ratio,
    }


def evaluate_shifted(labels: pd.Series, high_omega: pd.Series, shift: int) -> dict[str, object]:
    shifted = labels.shift(shift)
    valid = shifted.notna()
    result = evaluate(shifted[valid].to_numpy(dtype=bool), high_omega[valid].to_numpy(dtype=bool))
    result["dropped_rows_from_shift"] = int((~valid).sum())
    return result


def main() -> None:
    input_sha256 = require_fixed_input()
    eligible, metadata = load_eligible_rows()

    labels_series = eligible["collapse"].reset_index(drop=True)
    high_omega_series = eligible["high_omega"].reset_index(drop=True)
    labels = labels_series.to_numpy(dtype=bool)
    high_omega = high_omega_series.to_numpy(dtype=bool)

    original = evaluate(labels, high_omega)
    original_row = {
        "condition": "original",
        **original,
        "q_event_0.95": metadata["q_event_0.95"],
        "q_omega_0.99": metadata["q_omega_0.99"],
    }

    temporal_rows = []
    for shift in TEMPORAL_SHIFTS:
        temporal_rows.append(
            {
                "condition": f"temporal_shift_+{shift}",
                "shift": shift,
                **evaluate_shifted(labels_series, high_omega_series, shift),
            }
        )

    shuffled_rows = []
    for run in range(SHUFFLE_RUNS):
        seed = SHUFFLE_SEED_BASE + run
        rng = np.random.default_rng(seed)
        shuffled = rng.permutation(labels)
        shuffled_rows.append(
            {
                "condition": "shuffled_labels",
                "run": run + 1,
                "seed": seed,
                **evaluate(shuffled, high_omega),
            }
        )

    shuffled_df = pd.DataFrame(shuffled_rows)
    shuffled_summary = {
        "runs": SHUFFLE_RUNS,
        "seed_base": SHUFFLE_SEED_BASE,
        "mean_p_collapse_given_high_omega": float(
            shuffled_df["p_collapse_given_high_omega"].mean()
        ),
        "median_p_collapse_given_high_omega": float(
            shuffled_df["p_collapse_given_high_omega"].median()
        ),
        "min_p_collapse_given_high_omega": float(
            shuffled_df["p_collapse_given_high_omega"].min()
        ),
        "max_p_collapse_given_high_omega": float(
            shuffled_df["p_collapse_given_high_omega"].max()
        ),
        "mean_ratio": float(shuffled_df["ratio"].mean()),
        "median_ratio": float(shuffled_df["ratio"].median()),
        "min_ratio": float(shuffled_df["ratio"].min()),
        "max_ratio": float(shuffled_df["ratio"].max()),
        "mean_n_event_high": float(shuffled_df["n_event_high"].mean()),
        "min_n_event_high": int(shuffled_df["n_event_high"].min()),
        "max_n_event_high": int(shuffled_df["n_event_high"].max()),
    }

    summary = {
        "input": {
            "file": str(INPUT_FILE),
            "sha256": input_sha256,
            **metadata,
            "missing_calendar_date_caveat": (
                f"{MISSING_CALENDAR_DATE} is absent from the fixed snapshot and was "
                "not imputed or refetched."
            ),
        },
        "definitions": {
            "return": "Close.pct_change()",
            "I": f"rolling standard deviation of return, window={ROLLING_WINDOW}",
            "G": "absolute return",
            "Omega": "I * G",
            "collapse_event": "(High - Low) / Close > q(0.95)",
            "high_omega": "Omega > q(0.99)",
            "event_independent_of_omega": True,
            "temporal_shift": "labels.shift(+rows), shifted-null rows excluded",
            "shuffled_labels_runs": SHUFFLE_RUNS,
        },
        "original": original_row,
        "temporal_shifts": temporal_rows,
        "shuffled_summary": shuffled_summary,
        "outputs": {
            "original_csv": str(ORIGINAL_OUT),
            "temporal_shifts_csv": str(TEMPORAL_OUT),
            "shuffled_runs_csv": str(SHUFFLED_OUT),
            "summary_json": str(SUMMARY_OUT),
        },
    }

    RESULTS_DIR.mkdir(exist_ok=True)
    pd.DataFrame([original_row]).to_csv(ORIGINAL_OUT, index=False, lineterminator="\n")
    pd.DataFrame(temporal_rows).to_csv(TEMPORAL_OUT, index=False, lineterminator="\n")
    shuffled_df.to_csv(SHUFFLED_OUT, index=False, lineterminator="\n")
    SUMMARY_OUT.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
