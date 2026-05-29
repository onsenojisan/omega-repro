"""Exploratory Omega sensitivity / design-space scan.

This script is separate from the fixed minimal protocol. It scans predefined
nearby score, window, threshold, and lead settings and reports stability of
P(event | high score) > baseline P(event). It does not choose or optimize a new
official Omega definition.
"""

from __future__ import annotations

import argparse
import math
from pathlib import Path
from typing import Iterable

import numpy as np
import pandas as pd


ROLLING_WINDOWS = (5, 10, 20, 30, 60)
HIGH_QUANTILES = (0.90, 0.95, 0.975, 0.99)
LEADS = (0, 1, 3, 5)
SCORE_TYPES = ("omega_product", "I_only", "G_only", "omega_product_z")

RESULT_COLUMNS = [
    "domain_or_file",
    "score_type",
    "rolling_window",
    "high_quantile",
    "lead",
    "n_rows_valid",
    "n_events",
    "baseline_p_event",
    "n_high",
    "n_event_high",
    "p_event_given_high",
    "ratio",
    "above_baseline",
    "reliability_flag",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Run an exploratory Omega sensitivity / design-space scan on a CSV "
            "with time,value,event columns."
        )
    )
    parser.add_argument("csv_path", help="Input CSV with at least time,value,event columns.")
    parser.add_argument(
        "--output-dir",
        default="outputs",
        help="Directory for sensitivity_scan_results.csv and sensitivity_scan_summary.md.",
    )
    parser.add_argument(
        "--domain",
        default=None,
        help="Optional label for the domain_or_file output column. Defaults to the CSV filename.",
    )
    parser.add_argument("--value-col", default="value", help="Numeric value column name.")
    parser.add_argument(
        "--event-col",
        default="event",
        help="Independent binary event column name; values must convert to 0/1.",
    )
    parser.add_argument(
        "--time-col",
        default="time",
        help="Time or row-order column used to sort rows before rolling and lead calculations.",
    )
    return parser.parse_args()


def require_columns(df: pd.DataFrame, columns: Iterable[str]) -> None:
    missing = [column for column in columns if column not in df.columns]
    if missing:
        raise ValueError(f"missing required column(s): {', '.join(missing)}")


def coerce_binary_event(series: pd.Series) -> pd.Series:
    truthy = {"1", "1.0", "true", "t", "yes", "y"}
    falsey = {"0", "0.0", "false", "f", "no", "n"}
    converted: list[float] = []
    invalid: set[str] = set()

    for value in series:
        if pd.isna(value):
            converted.append(np.nan)
            continue
        if isinstance(value, (bool, np.bool_)):
            converted.append(float(int(value)))
            continue
        if isinstance(value, str):
            normalized = value.strip().lower()
            if normalized in truthy:
                converted.append(1.0)
                continue
            if normalized in falsey:
                converted.append(0.0)
                continue
            try:
                numeric = float(normalized)
            except ValueError:
                invalid.add(value)
                converted.append(np.nan)
                continue
        else:
            numeric = float(value)

        if math.isclose(numeric, 0.0):
            converted.append(0.0)
        elif math.isclose(numeric, 1.0):
            converted.append(1.0)
        else:
            invalid.add(str(value))
            converted.append(np.nan)

    if invalid:
        shown = ", ".join(sorted(invalid)[:10])
        raise ValueError(f"event column must be binary or convertible to 0/1; invalid values: {shown}")

    return pd.Series(converted, index=series.index, dtype="float64")


def read_input(csv_path: Path, time_col: str, value_col: str, event_col: str) -> pd.DataFrame:
    df = pd.read_csv(csv_path)
    require_columns(df, [time_col, value_col, event_col])
    df = df.sort_values(time_col).reset_index(drop=True)

    value = pd.to_numeric(df[value_col], errors="coerce")
    bad_values = df.loc[value.isna() & df[value_col].notna(), value_col]
    if not bad_values.empty:
        shown = ", ".join(str(item) for item in sorted(set(bad_values.astype(str)))[:10])
        raise ValueError(f"value column must be numeric; invalid values: {shown}")

    event = coerce_binary_event(df[event_col])
    return pd.DataFrame({"value": value, "event": event})


def zscore(series: pd.Series) -> pd.Series | None:
    valid = series.dropna()
    if len(valid) < 2:
        return None
    std = float(valid.std())
    if not math.isfinite(std) or math.isclose(std, 0.0):
        return None
    mean = float(valid.mean())
    return (series - mean) / std


def compute_scores(value: pd.Series, rolling_window: int) -> dict[str, pd.Series | None]:
    intensity = value.rolling(rolling_window).std()
    gradient = value.diff().abs()
    omega_product = intensity * gradient

    z_intensity = zscore(intensity)
    z_gradient = zscore(gradient)
    omega_product_z = None
    if z_intensity is not None and z_gradient is not None:
        omega_product_z = z_intensity * z_gradient

    return {
        "omega_product": omega_product,
        "I_only": intensity,
        "G_only": gradient,
        "omega_product_z": omega_product_z,
    }


def reliability_flag(
    invalid: bool,
    n_events: int,
    n_high: int,
    n_event_high: int,
) -> str:
    if invalid:
        return "invalid"
    if n_events == 0:
        return "no_events"
    if n_high < 10:
        return "sparse_high"
    if n_event_high < 3:
        return "sparse_event_high"
    return "ok"


def scan_one(
    domain_or_file: str,
    score_type: str,
    rolling_window: int,
    high_quantile: float,
    lead: int,
    score: pd.Series | None,
    event: pd.Series,
) -> dict[str, object]:
    base = {
        "domain_or_file": domain_or_file,
        "score_type": score_type,
        "rolling_window": rolling_window,
        "high_quantile": high_quantile,
        "lead": lead,
        "n_rows_valid": 0,
        "n_events": 0,
        "baseline_p_event": np.nan,
        "n_high": 0,
        "n_event_high": 0,
        "p_event_given_high": np.nan,
        "ratio": np.nan,
        "above_baseline": np.nan,
        "reliability_flag": "invalid",
    }

    if score is None:
        return base

    event_lead = event.shift(-lead) if lead else event
    valid = pd.DataFrame({"score": score, "event": event_lead}).dropna(subset=["score", "event"])
    if valid.empty:
        return base

    threshold = float(valid["score"].quantile(high_quantile))
    if not math.isfinite(threshold):
        return base

    high = valid["score"] >= threshold
    n_rows_valid = int(len(valid))
    n_events = int(valid["event"].sum())
    baseline_p_event = float(valid["event"].mean())
    n_high = int(high.sum())
    n_event_high = int(valid.loc[high, "event"].sum())
    p_event_given_high = float(valid.loc[high, "event"].mean()) if n_high else np.nan
    ratio = (
        float(p_event_given_high / baseline_p_event)
        if n_high and baseline_p_event > 0 and math.isfinite(p_event_given_high)
        else np.nan
    )
    above_baseline = (
        bool(p_event_given_high > baseline_p_event)
        if math.isfinite(p_event_given_high) and math.isfinite(baseline_p_event)
        else np.nan
    )

    return {
        **base,
        "n_rows_valid": n_rows_valid,
        "n_events": n_events,
        "baseline_p_event": baseline_p_event,
        "n_high": n_high,
        "n_event_high": n_event_high,
        "p_event_given_high": p_event_given_high,
        "ratio": ratio,
        "above_baseline": above_baseline,
        "reliability_flag": reliability_flag(False, n_events, n_high, n_event_high),
    }


def run_scan(df: pd.DataFrame, domain_or_file: str) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for rolling_window in ROLLING_WINDOWS:
        scores = compute_scores(df["value"], rolling_window)
        for score_type in SCORE_TYPES:
            for high_quantile in HIGH_QUANTILES:
                for lead in LEADS:
                    rows.append(
                        scan_one(
                            domain_or_file=domain_or_file,
                            score_type=score_type,
                            rolling_window=rolling_window,
                            high_quantile=high_quantile,
                            lead=lead,
                            score=scores[score_type],
                            event=df["event"],
                        )
                    )
    return pd.DataFrame(rows, columns=RESULT_COLUMNS)


def format_number(value: object, digits: int = 4) -> str:
    if value is None:
        return "NA"
    try:
        numeric = float(value)
    except (TypeError, ValueError):
        return str(value)
    if not math.isfinite(numeric):
        return "NA"
    return f"{numeric:.{digits}g}"


def markdown_table(headers: list[str], rows: list[list[object]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(str(item) for item in row) + " |")
    return "\n".join(lines)


def median_ratio_table(results: pd.DataFrame, group_col: str) -> str:
    ratio_rows = results[np.isfinite(results["ratio"])]
    if ratio_rows.empty:
        return "No finite ratios available."
    grouped = ratio_rows.groupby(group_col, dropna=False)["ratio"].median().reset_index()
    rows = [[item[group_col], format_number(item["ratio"])] for _, item in grouped.iterrows()]
    return markdown_table([group_col, "median_ratio"], rows)


def above_rate_by(results: pd.DataFrame, group_col: str) -> pd.DataFrame:
    computable = results[results["above_baseline"].isin([True, False])].copy()
    if computable.empty:
        return pd.DataFrame(columns=[group_col, "n", "above_rate"])
    computable["above_int"] = computable["above_baseline"].astype(int)
    return (
        computable.groupby(group_col, dropna=False)
        .agg(n=("above_int", "size"), above_rate=("above_int", "mean"))
        .reset_index()
    )


def region_lines(results: pd.DataFrame, threshold: float, direction: str) -> list[str]:
    lines: list[str] = []
    for group_col in ["score_type", "rolling_window", "high_quantile", "lead"]:
        rates = above_rate_by(results, group_col)
        if rates.empty:
            continue
        if direction == "stable":
            selected = rates[rates["above_rate"] >= threshold]
            label = "above-baseline rate"
        else:
            selected = rates[rates["above_rate"] <= threshold]
            label = "above-baseline rate"
        for _, row in selected.iterrows():
            lines.append(
                f"- `{group_col}={row[group_col]}`: {format_number(row['above_rate'] * 100)}% "
                f"{label} across {int(row['n'])} computable specs"
            )
    return lines


def score_type_comparison(results: pd.DataFrame) -> str:
    rates = above_rate_by(results, "score_type")
    ratio_rows = results[np.isfinite(results["ratio"])]
    medians = ratio_rows.groupby("score_type")["ratio"].median().to_dict()
    rows = []
    for score_type in SCORE_TYPES:
        rate_match = rates[rates["score_type"] == score_type]
        above_rate = float(rate_match["above_rate"].iloc[0]) if not rate_match.empty else np.nan
        n = int(rate_match["n"].iloc[0]) if not rate_match.empty else 0
        rows.append([score_type, format_number(medians.get(score_type, np.nan)), format_number(above_rate * 100), n])

    omega = medians.get("omega_product", np.nan)
    i_only = medians.get("I_only", np.nan)
    g_only = medians.get("G_only", np.nan)
    if all(math.isfinite(value) for value in [omega, i_only, g_only]):
        if omega > i_only and omega > g_only:
            statement = "omega_product has a higher median ratio than both I_only and G_only in this exploratory scan."
        else:
            statement = "omega_product is not better than both I_only and G_only by median ratio in this exploratory scan."
    else:
        statement = "omega_product cannot be fully compared with I_only and G_only because at least one median ratio is unavailable."

    return markdown_table(["score_type", "median_ratio", "above_rate_percent", "n_computable"], rows) + "\n\n" + statement


def lead_statement(results: pd.DataFrame) -> str:
    rates = above_rate_by(results, "lead")
    if rates.empty or 0 not in set(rates["lead"]):
        return "Lead stability could not be assessed because no computable lead results were available."
    lead0 = float(rates.loc[rates["lead"] == 0, "above_rate"].iloc[0])
    forward = rates[rates["lead"] > 0]
    if not forward.empty and lead0 >= 0.75 and (forward["above_rate"] < 0.75).all():
        return "Contemporaneous lead=0 is comparatively stable, while forward lead settings are unstable in this scan."
    if not forward.empty and lead0 < 0.75 and (forward["above_rate"] >= 0.75).any():
        return "Forward lead settings show stronger above-baseline rates than lead=0; these lead results are exploratory and not predictive evidence."
    return "Lead results should be read as exploratory stability checks, not predictive evidence."


def narrow_dependence_statement(results: pd.DataFrame) -> str:
    computable = results[results["above_baseline"].isin([True, False])]
    if computable.empty:
        return "No computable results were available to assess parameter dependence."
    overall = float(computable["above_baseline"].astype(int).mean())
    stable = region_lines(results, 0.75, "stable")
    if overall < 0.5 and stable:
        return "Results depend on limited parameter slices rather than broad stability across the scan."
    if overall >= 0.5 and not stable:
        return "Above-baseline results are present, but no single parameter slice reaches the simple stable-region threshold."
    return "Parameter dependence should be assessed from the grouped medians and above-baseline rates rather than the single maximum ratio."


def write_summary(results: pd.DataFrame, output_path: Path) -> None:
    total = len(results)
    computable = results[results["above_baseline"].isin([True, False])]
    n_computable = len(computable)
    above_count = int(computable["above_baseline"].sum()) if n_computable else 0
    above_percent = (above_count / n_computable * 100) if n_computable else np.nan
    sparse_count = int((results["reliability_flag"] != "ok").sum())

    best = results[np.isfinite(results["ratio"])].sort_values("ratio", ascending=False).head(1)
    if best.empty:
        best_text = "No finite exploratory best ratio is available."
    else:
        row = best.iloc[0]
        best_text = (
            "Exploratory best ratio only: "
            f"ratio={format_number(row['ratio'])}, score_type={row['score_type']}, "
            f"rolling_window={row['rolling_window']}, high_quantile={row['high_quantile']}, "
            f"lead={row['lead']}, reliability_flag={row['reliability_flag']}. "
            "This is not confirmatory evidence and is not the main result."
        )

    flag_counts = results["reliability_flag"].value_counts().reindex(
        ["ok", "sparse_high", "sparse_event_high", "no_events", "invalid"], fill_value=0
    )
    sparse_high = int(flag_counts["sparse_high"])
    sparse_event_high = int(flag_counts["sparse_event_high"])
    no_events = int(flag_counts["no_events"])
    if sparse_high or sparse_event_high or no_events:
        sparse_note = (
            "Event or high-score counts are sparse in this scan: "
            f"sparse_high={sparse_high}, sparse_event_high={sparse_event_high}, no_events={no_events}."
        )
    else:
        sparse_note = "No sparse event-count flags were produced in this scan."
    flag_table = markdown_table(
        ["reliability_flag", "count"],
        [[flag, int(count)] for flag, count in flag_counts.items()],
    )

    stable = region_lines(results, 0.75, "stable")
    failure = region_lines(results, 0.25, "failure")

    lines = [
        "# Exploratory Omega Sensitivity / Design-Space Scan Summary",
        "",
        "This scan is exploratory only. It does not change the fixed minimal protocol, does not select a new official Omega definition, and must not be used as post-hoc confirmation.",
        "",
        "The main result is stability across the predefined design space, not the single best ratio.",
        "",
        "## Overall",
        "",
        f"- Total scanned specifications: {total}",
        f"- Computable specifications: {n_computable}",
        f"- Above-baseline specifications: {above_count}",
        f"- Percentage where `P(event | high score) > baseline P(event)`: {format_number(above_percent)}%",
        f"- Non-ok reliability flags: {sparse_count}",
        "",
        "## Reliability Flags",
        "",
        flag_table,
        "",
        "Sparse or unreliable results are retained in the CSV and flagged rather than removed.",
        "",
        sparse_note,
        "",
        "## Median Ratio By Score Type",
        "",
        median_ratio_table(results, "score_type"),
        "",
        "## Median Ratio By Rolling Window",
        "",
        median_ratio_table(results, "rolling_window"),
        "",
        "## Median Ratio By High Quantile",
        "",
        median_ratio_table(results, "high_quantile"),
        "",
        "## Median Ratio By Lead",
        "",
        median_ratio_table(results, "lead"),
        "",
        "## Exploratory Best Ratio",
        "",
        best_text,
        "",
        "## Stable Regions",
        "",
        "\n".join(stable) if stable else "No simple parameter slice reached 75% above-baseline among computable specifications.",
        "",
        "## Failure Regions",
        "",
        "\n".join(failure) if failure else "No simple parameter slice was at or below 25% above-baseline among computable specifications.",
        "",
        "## Omega Product Compared With Controls",
        "",
        score_type_comparison(results),
        "",
        "## Lead Interpretation",
        "",
        lead_statement(results),
        "",
        "## Parameter Dependence",
        "",
        narrow_dependence_statement(results),
        "",
        "## Interpretation Warning",
        "",
        "The best single result is not the main result. Stability across nearby specifications matters more than the maximum ratio. If event counts are sparse or results depend on one narrow parameter choice, treat the scan as weak exploratory evidence only. Lead > 0 rows compare row t with event at t + lead and are exploratory timing checks, not predictive evidence.",
        "",
    ]
    output_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    args = parse_args()
    csv_path = Path(args.csv_path)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    domain_or_file = args.domain or csv_path.name
    df = read_input(csv_path, args.time_col, args.value_col, args.event_col)
    results = run_scan(df, domain_or_file)

    results_path = output_dir / "sensitivity_scan_results.csv"
    summary_path = output_dir / "sensitivity_scan_summary.md"
    results.to_csv(results_path, index=False)
    write_summary(results, summary_path)

    print(f"Wrote {results_path}")
    print(f"Wrote {summary_path}")


if __name__ == "__main__":
    main()
