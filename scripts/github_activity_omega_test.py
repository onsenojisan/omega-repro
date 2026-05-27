"""Run the first internal GitHub activity Ω structural concentration test.

This script follows maintenance/GITHUB_ACTIVITY_OMEGA_TEST_FIXED_SCOPE_V1.md.
It reads local git history, prints the minimal result block to stdout, and
does not create result files.
"""

from __future__ import annotations

import math
import statistics
import subprocess
from collections import Counter
from dataclasses import dataclass
from datetime import date, datetime, timedelta, timezone
from pathlib import Path


TARGET_REPOSITORY = "onsenojisan/omega-repro"
SAMPLE_END_DATE = date(2026, 5, 26)
ROLLING_WINDOW = 30
HIGH_OMEGA_Q = 0.99
EVENT_Q = 0.95


@dataclass(frozen=True)
class AnalysisRow:
    day: date
    activity_count: int
    intensity: float | None
    gradient: int | None
    omega: float | None


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def run_git(args: list[str]) -> str:
    try:
        completed = subprocess.run(
            ["git", *args],
            cwd=repo_root(),
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
    except FileNotFoundError as exc:
        raise SystemExit("git executable not found; local repository history is unavailable") from exc
    except subprocess.CalledProcessError as exc:
        detail = (exc.stderr or exc.stdout or "").strip()
        raise SystemExit(f"git command failed: git {' '.join(args)}\n{detail}") from exc
    return completed.stdout


def require_git_history() -> None:
    inside = run_git(["rev-parse", "--is-inside-work-tree"]).strip()
    if inside != "true":
        raise SystemExit("not inside a git work tree; local repository history is unavailable")

    commit_count = run_git(["rev-list", "--count", "HEAD"]).strip()
    if not commit_count.isdigit() or int(commit_count) == 0:
        raise SystemExit("no commits found in local git history")

    remote_url = run_git(["remote", "get-url", "origin"]).strip()
    normalized = remote_url.removesuffix(".git")
    if TARGET_REPOSITORY not in normalized:
        raise SystemExit(
            f"unexpected origin remote for fixed-scope test: {remote_url!r}; "
            f"expected repository containing {TARGET_REPOSITORY!r}"
        )


def parse_git_iso_datetime(value: str) -> datetime:
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise ValueError(f"git timestamp has no timezone: {value!r}")
    return parsed.astimezone(timezone.utc)


def load_commit_dates() -> tuple[list[date], str]:
    author_output = run_git(["log", "--format=%aI"])
    author_values = [line.strip() for line in author_output.splitlines() if line.strip()]
    if author_values:
        try:
            return [parse_git_iso_datetime(value).date() for value in author_values], (
                "commit author date (%aI)"
            )
        except ValueError as exc:
            raise SystemExit(f"unable to parse git author dates: {exc}") from exc

    committer_output = run_git(["log", "--format=%cI"])
    committer_values = [line.strip() for line in committer_output.splitlines() if line.strip()]
    if not committer_values:
        raise SystemExit("git log returned no commit timestamps")
    try:
        return [parse_git_iso_datetime(value).date() for value in committer_values], (
            "commit committer date (%cI); author date unavailable"
        )
    except ValueError as exc:
        raise SystemExit(f"unable to parse git committer dates: {exc}") from exc


def date_range(start: date, end: date) -> list[date]:
    if start > end:
        raise SystemExit(
            f"first available commit date {start.isoformat()} is after fixed cutoff "
            f"{end.isoformat()}"
        )
    days = (end - start).days + 1
    return [start + timedelta(days=offset) for offset in range(days)]


def rolling_sample_std(values: list[int], index: int, window: int) -> float | None:
    if index + 1 < window:
        return None
    return float(statistics.stdev(values[index + 1 - window : index + 1]))


def linear_quantile(values: list[float | int], q: float) -> float:
    if not values:
        raise SystemExit("cannot compute quantile on an empty valid analysis period")
    if not 0 <= q <= 1:
        raise ValueError(f"quantile must be between 0 and 1: {q}")

    ordered = sorted(float(value) for value in values)
    if len(ordered) == 1:
        return ordered[0]

    position = (len(ordered) - 1) * q
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return ordered[int(position)]

    fraction = position - lower
    return ordered[lower] + (ordered[upper] - ordered[lower]) * fraction


def build_rows(commit_dates: list[date]) -> tuple[list[AnalysisRow], date]:
    first_commit_date = min(commit_dates)
    all_days = date_range(first_commit_date, SAMPLE_END_DATE)

    counts_by_day = Counter(day for day in commit_dates if first_commit_date <= day <= SAMPLE_END_DATE)
    activity_counts = [counts_by_day[day] for day in all_days]

    rows: list[AnalysisRow] = []
    for index, day in enumerate(all_days):
        activity_count = activity_counts[index]
        intensity = rolling_sample_std(activity_counts, index, ROLLING_WINDOW)
        gradient = None if index == 0 else abs(activity_count - activity_counts[index - 1])
        omega = None if intensity is None or gradient is None else intensity * gradient
        rows.append(
            AnalysisRow(
                day=day,
                activity_count=activity_count,
                intensity=intensity,
                gradient=gradient,
                omega=omega,
            )
        )
    return rows, first_commit_date


def classify_result(n_high: int, n_event_high: int, p_event_high: float, baseline: float) -> str:
    if n_high == 0 or n_event_high == 0:
        return "sparse"
    if p_event_high > baseline:
        return "positive concentration"
    if p_event_high < baseline:
        return "negative / inverse"
    return "null"


def format_float(value: float) -> str:
    if math.isnan(value):
        return "nan"
    return f"{value:.12g}"


def print_result_block(
    *,
    first_commit_date: date,
    timestamp_rule_used: str,
    q_omega: float,
    q_event: float,
    p_event_high: float,
    baseline: float,
    ratio: float,
    n_total: int,
    n_valid: int,
    n_high: int,
    n_event_total: int,
    n_event_high: int,
    result_class: str,
) -> None:
    lines = [
        ("domain", "GitHub repository activity"),
        ("repository analyzed", TARGET_REPOSITORY),
        (
            "sample period",
            f"{first_commit_date.isoformat()} through {SAMPLE_END_DATE.isoformat()} UTC, inclusive",
        ),
        ("time zone", "UTC"),
        ("timestamp rule used", timestamp_rule_used),
        ("observable variable", "activity_count = number of commits per UTC day"),
        (
            "aggregation rule",
            "one UTC calendar day, including zero-activity days in the fixed sample period",
        ),
        ("I definition", "rolling standard deviation(activity_count, window = 30 days)"),
        ("G definition", "absolute first difference(activity_count)"),
        ("Ω definition", "Ω = I × G"),
        ("high-Ω threshold", f"Ω > q(0.99), q_0.99 = {format_float(q_omega)}"),
        ("event definition", f"activity_count > q(0.95), q_0.95 = {format_float(q_event)}"),
        ("event timing rule", "contemporaneous: event_t is compared with high_Ω_t"),
        ("P(event | high Ω)", format_float(p_event_high)),
        ("baseline P(event)", format_float(baseline)),
        ("ratio", format_float(ratio)),
        ("n_total", str(n_total)),
        ("n_valid", str(n_valid)),
        ("n_high", str(n_high)),
        ("n_event_total", str(n_event_total)),
        ("n_event_high", str(n_event_high)),
        ("result_class", result_class),
    ]
    for key, value in lines:
        print(f"{key}: {value}")


def main() -> None:
    require_git_history()
    commit_dates, timestamp_rule_used = load_commit_dates()
    rows, first_commit_date = build_rows(commit_dates)

    valid_rows = [row for row in rows if row.omega is not None]
    if not valid_rows:
        raise SystemExit("no valid analysis rows after applying the fixed 30-day rolling window")

    q_omega = linear_quantile([row.omega for row in valid_rows if row.omega is not None], HIGH_OMEGA_Q)
    q_event = linear_quantile([row.activity_count for row in valid_rows], EVENT_Q)

    high_omega = [row.omega is not None and row.omega > q_omega for row in valid_rows]
    events = [row.activity_count > q_event for row in valid_rows]

    n_total = len(rows)
    n_valid = len(valid_rows)
    n_high = sum(high_omega)
    n_event_total = sum(events)
    n_event_high = sum(event and high for event, high in zip(events, high_omega))

    baseline = n_event_total / n_valid if n_valid else math.nan
    p_event_high = n_event_high / n_high if n_high else math.nan
    ratio = p_event_high / baseline if n_high and baseline else math.nan
    result_class = classify_result(n_high, n_event_high, p_event_high, baseline)

    print_result_block(
        first_commit_date=first_commit_date,
        timestamp_rule_used=timestamp_rule_used,
        q_omega=q_omega,
        q_event=q_event,
        p_event_high=p_event_high,
        baseline=baseline,
        ratio=ratio,
        n_total=n_total,
        n_valid=n_valid,
        n_high=n_high,
        n_event_total=n_event_total,
        n_event_high=n_event_high,
        result_class=result_class,
    )


if __name__ == "__main__":
    main()
