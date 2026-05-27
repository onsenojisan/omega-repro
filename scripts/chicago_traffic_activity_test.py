"""Run the fixed Chicago traffic crash activity Omega test.

This script follows maintenance/CHICAGO_TRAFFIC_ACTIVITY_FIXED_SCOPE_V1.md.
It fetches fixed City of Chicago Data Portal daily crash counts at runtime,
prints the minimal result block to stdout, and does not create result files.
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


DOMAIN = "Traffic"
REGION = "Chicago, Illinois"
DATA_SOURCE = "City of Chicago Data Portal, Traffic Crashes - Crashes"
DATASET_ID = "85ca-t3if"
ENDPOINT = "https://data.cityofchicago.org/resource/85ca-t3if.json"
METADATA_ENDPOINT = "https://data.cityofchicago.org/api/views/85ca-t3if"
SAMPLE_START_DATE = date(2018, 1, 1)
SAMPLE_END_DATE = date(2024, 12, 31)
QUERY_END_EXCLUSIVE = date(2025, 1, 1)
DATE_FIELD = "crash_date"
OBSERVABLE = "daily_crash_count"
ROLLING_WINDOW = 30
HIGH_OMEGA_Q = 0.99
EVENT_Q = 0.95
NULL_TOLERANCE = 1e-12
USER_AGENT = "omega-repro-chicago-traffic-activity-test/1.0"


@dataclass(frozen=True)
class DailyRow:
    day: date
    daily_crash_count: int
    intensity: float | None
    gradient: int | None
    omega: float | None


def metadata_url() -> str:
    return METADATA_ENDPOINT


def daily_counts_url() -> str:
    params = {
        "$select": f"date_trunc_ymd({DATE_FIELD}) as crash_day,count(*) as crash_count",
        "$where": (
            f"{DATE_FIELD} >= '{SAMPLE_START_DATE.isoformat()}T00:00:00' "
            f"and {DATE_FIELD} < '{QUERY_END_EXCLUSIVE.isoformat()}T00:00:00'"
        ),
        "$group": f"date_trunc_ymd({DATE_FIELD})",
        "$order": "crash_day",
        "$limit": "5000",
    }
    return f"{ENDPOINT}?{urllib.parse.urlencode(params)}"


def source_count_url() -> str:
    params = {
        "$select": f"count(*) as n,min({DATE_FIELD}) as min_date,max({DATE_FIELD}) as max_date",
        "$where": (
            f"{DATE_FIELD} >= '{SAMPLE_START_DATE.isoformat()}T00:00:00' "
            f"and {DATE_FIELD} < '{QUERY_END_EXCLUSIVE.isoformat()}T00:00:00'"
        ),
    }
    return f"{ENDPOINT}?{urllib.parse.urlencode(params)}"


def fetch_json(url: str, source_name: str) -> object:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            raw_payload = response.read().decode("utf-8")
    except urllib.error.URLError as exc:
        raise SystemExit(f"failed to fetch {source_name}: {exc}") from exc

    try:
        return json.loads(raw_payload)
    except json.JSONDecodeError as exc:
        raise SystemExit(f"invalid JSON response from {source_name}: {exc}") from exc


def verify_schema() -> None:
    payload = fetch_json(metadata_url(), "City of Chicago dataset metadata")
    if not isinstance(payload, dict):
        raise SystemExit("invalid City of Chicago metadata response: expected object")
    if payload.get("id") != DATASET_ID:
        raise SystemExit(f"unexpected dataset id in metadata: {payload.get('id')!r}")

    columns = payload.get("columns")
    if not isinstance(columns, list):
        raise SystemExit("invalid City of Chicago metadata response: missing columns")

    matches = [
        column
        for column in columns
        if isinstance(column, dict) and column.get("fieldName") == DATE_FIELD
    ]
    if len(matches) != 1:
        raise SystemExit(f"expected exactly one {DATE_FIELD!r} column in metadata, found {len(matches)}")

    column = matches[0]
    if column.get("name") != "CRASH_DATE":
        raise SystemExit(f"unexpected display name for {DATE_FIELD}: {column.get('name')!r}")
    if column.get("dataTypeName") not in {"calendar_date", "floating_timestamp", "fixed_timestamp"}:
        raise SystemExit(
            f"unexpected data type for {DATE_FIELD}: {column.get('dataTypeName')!r}"
        )


def parse_socrata_day(value: str) -> date:
    if not value:
        raise SystemExit("City of Chicago daily count row has empty crash_day")
    for fmt in ("%Y-%m-%dT%H:%M:%S.%f", "%Y-%m-%dT%H:%M:%S"):
        try:
            return datetime.strptime(value, fmt).date()
        except ValueError:
            pass
    raise SystemExit(f"invalid City of Chicago crash_day value: {value!r}")


def parse_source_count_summary() -> tuple[int, str, str]:
    payload = fetch_json(source_count_url(), "City of Chicago source count summary")
    if not isinstance(payload, list) or len(payload) != 1 or not isinstance(payload[0], dict):
        raise SystemExit("invalid City of Chicago source count summary response")
    row = payload[0]
    try:
        n_source_records = int(row["n"])
    except (KeyError, TypeError, ValueError) as exc:
        raise SystemExit("invalid source count summary: missing numeric n") from exc
    min_date = str(row.get("min_date", ""))
    max_date = str(row.get("max_date", ""))
    if not min_date or not max_date:
        raise SystemExit("invalid source count summary: missing min_date or max_date")
    return n_source_records, min_date, max_date


def fetch_daily_counts() -> tuple[list[tuple[date, int]], int, str, str]:
    verify_schema()
    n_source_records, min_date, max_date = parse_source_count_summary()

    payload = fetch_json(daily_counts_url(), "City of Chicago grouped daily crash counts")
    if not isinstance(payload, list):
        raise SystemExit("invalid City of Chicago daily counts response: expected list")

    counts_by_day = {day: 0 for day in date_range(SAMPLE_START_DATE, SAMPLE_END_DATE)}
    seen_days: set[date] = set()
    grouped_record_count = 0

    for raw_row in payload:
        if not isinstance(raw_row, dict):
            raise SystemExit(f"invalid daily count row: {raw_row!r}")
        raw_day = raw_row.get("crash_day")
        raw_count = raw_row.get("crash_count")
        if not isinstance(raw_day, str):
            raise SystemExit(f"invalid crash_day value: {raw_day!r}")

        day = parse_socrata_day(raw_day)
        if day < SAMPLE_START_DATE or day > SAMPLE_END_DATE:
            raise SystemExit(f"daily count response includes date outside fixed sample period: {day}")
        if day in seen_days:
            raise SystemExit(f"duplicate daily count date in response: {day}")
        seen_days.add(day)

        try:
            count = int(raw_count)
        except (TypeError, ValueError) as exc:
            raise SystemExit(f"invalid crash_count for {day}: {raw_count!r}") from exc
        if count < 0:
            raise SystemExit(f"negative crash_count for {day}: {count}")
        counts_by_day[day] = count
        grouped_record_count += count

    if grouped_record_count != n_source_records:
        raise SystemExit(
            "grouped daily crash counts do not sum to source record count: "
            f"grouped={grouped_record_count}, source={n_source_records}"
        )

    rows = [(day, counts_by_day[day]) for day in date_range(SAMPLE_START_DATE, SAMPLE_END_DATE)]
    return rows, n_source_records, min_date, max_date


def date_range(start_day: date, end_day: date) -> list[date]:
    if start_day > end_day:
        raise SystemExit(f"invalid date range: {start_day} after {end_day}")
    days = (end_day - start_day).days + 1
    return [start_day + timedelta(days=offset) for offset in range(days)]


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


def build_rows(daily_counts: list[tuple[date, int]]) -> list[DailyRow]:
    values = [value for _day, value in daily_counts]
    rows: list[DailyRow] = []
    for index, (day, daily_crash_count) in enumerate(daily_counts):
        intensity = rolling_sample_std(values, index, ROLLING_WINDOW)
        gradient = None if index == 0 else abs(daily_crash_count - values[index - 1])
        omega = None if intensity is None or gradient is None else intensity * gradient
        rows.append(
            DailyRow(
                day=day,
                daily_crash_count=daily_crash_count,
                intensity=intensity,
                gradient=gradient,
                omega=omega,
            )
        )
    return rows


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
    n_source_records: int,
    source_min_date: str,
    source_max_date: str,
    result_class: str,
) -> None:
    lines = [
        ("domain", DOMAIN),
        ("region", REGION),
        ("data source", DATA_SOURCE),
        ("dataset id", DATASET_ID),
        ("endpoint", ENDPOINT),
        ("metadata endpoint", METADATA_ENDPOINT),
        (
            "fixed query",
            (
                "select date_trunc_ymd(crash_date) as crash_day,count(*) as crash_count; "
                "where crash_date >= 2018-01-01T00:00:00 and crash_date < 2025-01-01T00:00:00; "
                "group by date_trunc_ymd(crash_date); order by crash_day"
            ),
        ),
        (
            "sample period",
            f"{SAMPLE_START_DATE.isoformat()} through {SAMPLE_END_DATE.isoformat()}, inclusive",
        ),
        ("date field", "CRASH_DATE / crash_date"),
        ("source min crash_date", source_min_date),
        ("source max crash_date", source_max_date),
        ("observable variable", "daily_crash_count = count of crash records per calendar day"),
        ("aggregation rule", "one calendar day derived from crash_date, including zero-count days if present"),
        ("I definition", "rolling sample standard deviation(daily_crash_count, window = 30 days)"),
        ("G definition", "absolute first difference(daily_crash_count)"),
        ("Omega definition", "Omega = I x G"),
        ("high-Omega threshold", f"Omega > q(0.99), q_0.99 = {format_float(q_omega)}"),
        ("event definition", f"daily_crash_count > q(0.95), q_0.95 = {format_float(q_event)}"),
        ("event timing rule", "contemporaneous: event_t is compared with high_Omega_t"),
        ("P(event | high Omega)", format_float(p_event_high)),
        ("baseline P(event)", format_float(baseline)),
        ("ratio", format_float(ratio)),
        ("n_total", str(n_total)),
        ("n_valid", str(n_valid)),
        ("n_high", str(n_high)),
        ("n_event_total", str(n_event_total)),
        ("n_event_high", str(n_event_high)),
        ("n_source_records", str(n_source_records)),
        ("result_class", result_class),
    ]
    for key, value in lines:
        print(f"{key}: {value}")


def main() -> None:
    daily_counts, n_source_records, source_min_date, source_max_date = fetch_daily_counts()
    rows = build_rows(daily_counts)
    valid_rows = [row for row in rows if row.omega is not None]
    if not valid_rows:
        raise SystemExit("no valid analysis rows after applying the fixed 30-day rolling window")

    q_omega = linear_quantile([row.omega for row in valid_rows if row.omega is not None], HIGH_OMEGA_Q)
    q_event = linear_quantile([row.daily_crash_count for row in valid_rows], EVENT_Q)

    high_omega = [row.omega is not None and row.omega > q_omega for row in valid_rows]
    events = [row.daily_crash_count > q_event for row in valid_rows]

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
        n_source_records=n_source_records,
        source_min_date=source_min_date,
        source_max_date=source_max_date,
        result_class=result_class,
    )


if __name__ == "__main__":
    main()
