"""Run the AAPL source-consistent V1 structural concentration control.

This script reads only the fixed local raw OHLC snapshot. It does not fetch
external data and does not execute notebooks.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd


INPUT_FILE = Path("data/aapl_fixed_ohlc_2024-05-25_2026-05-25.csv")
EXPECTED_SHA256 = "e368084c40010af1cd33d9c492256faaf0bda5f19c44790092b16d824d7e0577"

RESULTS_DIR = Path("results")
ORIGINAL_OUT = RESULTS_DIR / "aapl_source_consistent_v1_original_2026-05-25.csv"
TEMPORAL_OUT = RESULTS_DIR / "aapl_source_consistent_v1_temporal_shifts_2026-05-25.csv"
SHUFFLED_OUT = RESULTS_DIR / "aapl_source_consistent_v1_shuffled_runs_2026-05-25.csv"
SUMMARY_OUT = RESULTS_DIR / "aapl_source_consistent_v1_summary_2026-05-25.json"

ROLLING_WINDOW = 20
EVENT_Q = 0.95
OMEGA_Q = 0.99
TEMPORAL_SHIFTS = [30, 60, 120]
SHUFFLE_RUNS = 100
SHUFFLE_SEED_BASE = 20260525


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


def main() -> None:
    input_sha256 = require_fixed_input()
    eligible, metadata = load_eligible_rows()

    labels = eligible["collapse"].to_numpy(dtype=bool)
    high_omega = eligible["high_omega"].to_numpy(dtype=bool)

    original = evaluate(labels, high_omega)
    original_row = {
        "condition": "original",
        **original,
        "q_event_0.95": metadata["q_event_0.95"],
        "q_omega_0.99": metadata["q_omega_0.99"],
    }

    temporal_rows = []
    for shift in TEMPORAL_SHIFTS:
        shifted = np.roll(labels, shift)
        temporal_rows.append(
            {
                "condition": f"temporal_shift_+{shift}",
                "shift": shift,
                **evaluate(shifted, high_omega),
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
        },
        "definitions": {
            "return": "Close.pct_change()",
            "I": f"rolling standard deviation of return, window={ROLLING_WINDOW}",
            "G": "absolute return",
            "Omega": "I * G",
            "collapse_event": "(High - Low) / Close > q(0.95)",
            "high_omega": "Omega > q(0.99)",
            "event_independent_of_omega": True,
            "temporal_shift": "np.roll(collapse_labels, shift)",
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
