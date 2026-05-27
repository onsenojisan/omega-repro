"""Run the fixed Wikipedia Python pageview activity Ω test.

This script follows maintenance/WIKIPEDIA_ACTIVITY_PYTHON_FIXED_SCOPE_V1.md.
It fetches daily Wikimedia Pageviews API counts at runtime, prints the minimal
result block to stdout, and does not create result files.
"""

from __future__ import annotations

import json
import math
import statistics
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import date, datetime, timedelta


DOMAIN = "Wikipedia activity"
PROJECT = "en.wikipedia.org"
PAGE = "Python (programming language)"
ARTICLE = "Python_(programming_language)"
DATA_SOURCE = "Wikimedia Pageviews API"
ACCESS = "all-access"
AGENT = "user"
GRANULARITY = "daily"
SAMPLE_END_DATE = date(2026, 5, 26)
ROLLING_WINDOW = 30
HIGH_OMEGA_Q = 0.99
EVENT_Q = 0.95
NULL_TOLERANCE = 1e-12
USER_AGENT = "omega-repro-wikipedia-activity-test/1.0"


@dataclass(frozen=True)
class PageviewRow:
    day: date
    activity_count: int
    intensity: float | None
    gradient: int | None
    omega: float | None


def pageviews_url(start: date, end: date) -> str:
    encoded_article = urllib.parse.quote(ARTICLE, safe="")
    start_stamp = start.strftime("%Y%m%d")
    end_stamp = end.strftime("%Y%m%d")
    return (
        "https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/"
        f"{PROJECT}/{ACCESS}/{AGENT}/{encoded_article}/{GRANULARITY}/"
        f"{start_stamp}/{end_stamp}"
    )


def fetch_pageviews() -> list[tuple[date, int]]:
    # Wikimedia daily pageviews data begin in July 2015; this is the earliest
    # fixed-source start request, not an analysis-period tuning choice.
    request_start = date(2015, 7, 1)
    request = urllib.request.Request(
        pageviews_url(request_start, SAMPLE_END_DATE),
        headers={"User-Agent": USER_AGENT},
    )
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            raw_payload = response.read().decode("utf-8")
    except urllib.error.URLError as exc:
        raise SystemExit(f"failed to fetch Wikimedia Pageviews API data: {exc}") from exc

    try:
        payload = json.loads(raw_payload)
    except json.JSONDecodeError as exc:
        raise SystemExit(f"invalid JSON response from Wikimedia Pageviews API: {exc}") from exc

    items = payload.get("items")
    if not isinstance(items, list):
        raise SystemExit("invalid Wikimedia Pageviews API response: missing items list")

    rows: list[tuple[date, int]] = []
    for item in items:
        if not isinstance(item, dict):
            raise SystemExit("invalid Wikimedia Pageviews API response: item is not an object")
        timestamp = item.get("timestamp")
        views = item.get("views")
        if not isinstance(timestamp, str) or len(timestamp) < 8:
            raise SystemExit(f"invalid item timestamp in Wikimedia response: {timestamp!r}")
        if not isinstance(views, int):
            raise SystemExit(f"invalid item views in Wikimedia response: {views!r}")
        try:
            day = datetime.strptime(timestamp[:8], "%Y%m%d").date()
        except ValueError as exc:
            raise SystemExit(f"invalid item timestamp in Wikimedia response: {timestamp!r}") from exc
        if day <= SAMPLE_END_DATE:
            rows.append((day, views))

    if not rows:
        raise SystemExit("Wikimedia Pageviews API returned no daily pageview rows")

    rows.sort(key=lambda row: row[0])
    return rows


def date_range(start: date, end: date) -> list[date]:
    if start > end:
        raise SystemExit(
            f"first available pageview date {start.isoformat()} is after fixed cutoff "
            f"{end.isoformat()}"
        )
    days = (end - start).days + 1
    return [start + timedelta(days=offset) for offset in range(days)]


def detect_missing_days(pageviews: list[tuple[date, int]]) -> tuple[list[tuple[date, int]], int]:
    counts_by_day = {day: views for day, views in pageviews}
    if len(counts_by_day) != len(pageviews):
        raise SystemExit("duplicate dates returned by Wikimedia Pageviews API")

    first_day = min(counts_by_day)
    all_days = date_range(first_day, SAMPLE_END_DATE)
    missing_days = [day for day in all_days if day not in counts_by_day]

    observed_rows = [(day, counts_by_day[day]) for day in all_days if day in counts_by_day]
    return observed_rows, len(missing_days)


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


def build_rows(pageviews: list[tuple[date, int]]) -> tuple[list[PageviewRow], date]:
    first_pageview_date = min(day for day, _views in pageviews)
    activity_counts = [views for _day, views in pageviews]

    rows: list[PageviewRow] = []
    for index, (day, activity_count) in enumerate(pageviews):
        intensity = rolling_sample_std(activity_counts, index, ROLLING_WINDOW)
        gradient = None if index == 0 else abs(activity_count - activity_counts[index - 1])
        omega = None if intensity is None or gradient is None else intensity * gradient
        rows.append(
            PageviewRow(
                day=day,
                activity_count=activity_count,
                intensity=intensity,
                gradient=gradient,
                omega=omega,
            )
        )
    return rows, first_pageview_date


def classify_result(n_high: int, n_event_high: int, p_event_high: float, baseline: float) -> str:
    if n_high == 0 or n_event_high == 0:
        return "sparse"
    if math.isclose(p_event_high, baseline, rel_tol=NULL_TOLERANCE, abs_tol=NULL_TOLERANCE):
        return "null"
    if p_event_high > baseline:
        return "positive concentration"
    return "negative / inverse"


def format_float(value: float) -> str:
    if math.isnan(value):
        return "nan"
    return f"{value:.12g}"


def print_result_block(
    *,
    first_pageview_date: date,
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
    missing_days: int,
    result_class: str,
) -> None:
    lines = [
        ("domain", DOMAIN),
        ("project", PROJECT),
        ("page", PAGE),
        ("canonical page title", ARTICLE),
        ("data source", DATA_SOURCE),
        (
            "sample period",
            f"{first_pageview_date.isoformat()} through {SAMPLE_END_DATE.isoformat()} UTC, inclusive",
        ),
        ("time zone or API date convention", "Wikimedia daily pageviews date convention"),
        ("observable variable", "activity_count = daily pageview count"),
        (
            "aggregation rule",
            "one calendar day as reported by the Wikimedia Pageviews API",
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
        ("missing_days", str(missing_days)),
        ("result_class", result_class),
    ]
    for key, value in lines:
        print(f"{key}: {value}")


def main() -> None:
    raw_pageviews = fetch_pageviews()
    observed_pageviews, missing_days = detect_missing_days(raw_pageviews)
    rows, first_pageview_date = build_rows(observed_pageviews)

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
        first_pageview_date=first_pageview_date,
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
        missing_days=missing_days,
        result_class=result_class,
    )


if __name__ == "__main__":
    main()
