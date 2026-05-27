"""Run the fixed global earthquake activity Omega test.

This script follows maintenance/EARTHQUAKE_ACTIVITY_FIXED_SCOPE_V1.md.
It fetches fixed historical USGS FDSN Event API CSV data at runtime, prints
the minimal result block to stdout, and does not create result files.
"""

from __future__ import annotations

import csv
import io
import math
import statistics
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import date, datetime, timedelta, timezone


DOMAIN = "Global earthquake activity"
DATA_SOURCE = "USGS FDSN Event API"
ENDPOINT = "https://earthquake.usgs.gov/fdsnws/event/1/query"
QUERY_START_DATE = date(2000, 1, 1)
QUERY_END_DATE = date(2025, 12, 31)
ANALYSIS_START_DATE = date(2000, 1, 1)
ANALYSIS_END_DATE = date(2025, 12, 30)
MIN_OBSERVABLE_MAGNITUDE = 5.5
EVENT_MAGNITUDE_THRESHOLD = 6.5
ROLLING_WINDOW = 30
HIGH_OMEGA_Q = 0.99
NULL_TOLERANCE = 1e-12
USER_AGENT = "omega-repro-earthquake-activity-test/1.0"


@dataclass(frozen=True)
class EarthquakeEvent:
    event_id: str
    day: date
    magnitude: float


@dataclass(frozen=True)
class DailyRow:
    day: date
    activity_count: int
    event_next_day: bool
    intensity: float | None
    gradient: int | None
    omega: float | None


def query_url(start_day: date, end_day: date) -> str:
    params = {
        "format": "csv",
        "starttime": f"{start_day.isoformat()}T00:00:00",
        "endtime": f"{end_day.isoformat()}T23:59:59",
        "minmagnitude": f"{MIN_OBSERVABLE_MAGNITUDE:.1f}",
        "eventtype": "earthquake",
        "orderby": "time-asc",
    }
    return f"{ENDPOINT}?{urllib.parse.urlencode(params)}"


def iter_year_chunks(start_day: date, end_day: date) -> list[tuple[date, date]]:
    chunks: list[tuple[date, date]] = []
    current = start_day
    while current <= end_day:
        chunk_end = min(date(current.year, 12, 31), end_day)
        chunks.append((current, chunk_end))
        current = chunk_end + timedelta(days=1)
    return chunks


def parse_usgs_time(value: str) -> date:
    if not value:
        raise SystemExit("USGS CSV row has empty time")
    normalized = value.replace("Z", "+00:00")
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError as exc:
        raise SystemExit(f"invalid USGS event time: {value!r}") from exc
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc).date()


def fetch_events() -> list[EarthquakeEvent]:
    events: list[EarthquakeEvent] = []
    seen_ids: set[str] = set()

    for start_day, end_day in iter_year_chunks(QUERY_START_DATE, QUERY_END_DATE):
        request = urllib.request.Request(
            query_url(start_day, end_day),
            headers={"User-Agent": USER_AGENT},
        )
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                raw_payload = response.read().decode("utf-8")
        except urllib.error.URLError as exc:
            raise SystemExit(f"failed to fetch USGS FDSN Event API data: {exc}") from exc

        reader = csv.DictReader(io.StringIO(raw_payload))
        required_columns = {"time", "mag", "id"}
        if reader.fieldnames is None or not required_columns.issubset(reader.fieldnames):
            raise SystemExit(
                "invalid USGS CSV response: missing one of required columns "
                f"{sorted(required_columns)}"
            )

        for row in reader:
            event_id = (row.get("id") or "").strip()
            if not event_id:
                raise SystemExit("USGS CSV row has empty event id")
            if event_id in seen_ids:
                raise SystemExit(f"duplicate USGS event id in fixed query: {event_id}")
            seen_ids.add(event_id)

            magnitude_text = (row.get("mag") or "").strip()
            try:
                magnitude = float(magnitude_text)
            except ValueError as exc:
                raise SystemExit(f"invalid USGS event magnitude: {magnitude_text!r}") from exc
            if magnitude < MIN_OBSERVABLE_MAGNITUDE:
                raise SystemExit(
                    "USGS response included an event below the fixed minmagnitude "
                    f"filter: {magnitude}"
                )

            events.append(
                EarthquakeEvent(
                    event_id=event_id,
                    day=parse_usgs_time(row["time"]),
                    magnitude=magnitude,
                )
            )

    if not events:
        raise SystemExit("USGS FDSN Event API returned no fixed-query events")

    events.sort(key=lambda event: (event.day, event.event_id))
    return events


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


def build_rows(events: list[EarthquakeEvent]) -> list[DailyRow]:
    count_by_day = {day: 0 for day in date_range(ANALYSIS_START_DATE, ANALYSIS_END_DATE)}
    event_by_day = {day: False for day in date_range(ANALYSIS_START_DATE, QUERY_END_DATE)}

    for event in events:
        if ANALYSIS_START_DATE <= event.day <= ANALYSIS_END_DATE:
            count_by_day[event.day] += 1
        if ANALYSIS_START_DATE <= event.day <= QUERY_END_DATE and event.magnitude >= EVENT_MAGNITUDE_THRESHOLD:
            event_by_day[event.day] = True

    activity_counts = [count_by_day[day] for day in date_range(ANALYSIS_START_DATE, ANALYSIS_END_DATE)]

    rows: list[DailyRow] = []
    for index, day in enumerate(date_range(ANALYSIS_START_DATE, ANALYSIS_END_DATE)):
        activity_count = activity_counts[index]
        intensity = rolling_sample_std(activity_counts, index, ROLLING_WINDOW)
        gradient = None if index == 0 else abs(activity_count - activity_counts[index - 1])
        omega = None if intensity is None or gradient is None else intensity * gradient
        rows.append(
            DailyRow(
                day=day,
                activity_count=activity_count,
                event_next_day=event_by_day[day + timedelta(days=1)],
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
    p_event_high: float,
    baseline: float,
    ratio: float,
    n_total: int,
    n_valid: int,
    n_high: int,
    n_event_total: int,
    n_event_high: int,
    n_catalog_events: int,
    result_class: str,
) -> None:
    lines = [
        ("domain", DOMAIN),
        ("data source", DATA_SOURCE),
        ("endpoint", ENDPOINT),
        ("fixed query", "format=csv; eventtype=earthquake; minmagnitude=5.5; orderby=time-asc"),
        (
            "source query period",
            f"{QUERY_START_DATE.isoformat()} through {QUERY_END_DATE.isoformat()} UTC, inclusive",
        ),
        (
            "sample period",
            f"{ANALYSIS_START_DATE.isoformat()} through {ANALYSIS_END_DATE.isoformat()} UTC, inclusive",
        ),
        ("time zone rule", "UTC dates derived from the USGS event time field"),
        ("observable variable", "activity_count = daily count of earthquakes with preferred magnitude >= 5.5"),
        ("aggregation rule", "one UTC calendar day, including zero-count days"),
        ("I definition", "rolling sample standard deviation(activity_count, window = 30 days)"),
        ("G definition", "absolute first difference(activity_count)"),
        ("Omega definition", "Omega = I x G"),
        ("high-Omega threshold", f"Omega > q(0.99), q_0.99 = {format_float(q_omega)}"),
        ("event definition", "next UTC day contains at least one earthquake with preferred magnitude >= 6.5"),
        ("event timing rule", "one-day forward association: event_t is evaluated on day t+1"),
        ("P(event | high Omega)", format_float(p_event_high)),
        ("baseline P(event)", format_float(baseline)),
        ("ratio", format_float(ratio)),
        ("n_total", str(n_total)),
        ("n_valid", str(n_valid)),
        ("n_high", str(n_high)),
        ("n_event_total", str(n_event_total)),
        ("n_event_high", str(n_event_high)),
        ("n_catalog_events", str(n_catalog_events)),
        ("result_class", result_class),
    ]
    for key, value in lines:
        print(f"{key}: {value}")


def main() -> None:
    events = fetch_events()
    rows = build_rows(events)
    valid_rows = [row for row in rows if row.omega is not None]
    if not valid_rows:
        raise SystemExit("no valid analysis rows after applying the fixed 30-day rolling window")

    q_omega = linear_quantile([row.omega for row in valid_rows if row.omega is not None], HIGH_OMEGA_Q)
    high_omega = [row.omega is not None and row.omega > q_omega for row in valid_rows]
    event_rows = [row.event_next_day for row in valid_rows]

    n_total = len(rows)
    n_valid = len(valid_rows)
    n_high = sum(high_omega)
    n_event_total = sum(event_rows)
    n_event_high = sum(event and high for event, high in zip(event_rows, high_omega))

    baseline = n_event_total / n_valid if n_valid else math.nan
    p_event_high = n_event_high / n_high if n_high else math.nan
    ratio = p_event_high / baseline if n_high and baseline else math.nan
    result_class = classify_result(n_high, n_event_high, p_event_high, baseline)

    print_result_block(
        q_omega=q_omega,
        p_event_high=p_event_high,
        baseline=baseline,
        ratio=ratio,
        n_total=n_total,
        n_valid=n_valid,
        n_high=n_high,
        n_event_total=n_event_total,
        n_event_high=n_event_high,
        n_catalog_events=len(events),
        result_class=result_class,
    )


if __name__ == "__main__":
    main()
