"""Run the fixed London daily precipitation weather activity Omega test.

This script follows maintenance/LONDON_WEATHER_ACTIVITY_FIXED_SCOPE_V1.md.
It fetches fixed Open-Meteo Archive API data at runtime, prints the minimal
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


DOMAIN = "Weather"
LOCATION = "London, United Kingdom"
LATITUDE = 51.5072
LONGITUDE = -0.1276
DATA_SOURCE = "Open-Meteo Archive API"
ENDPOINT = "https://archive-api.open-meteo.com/v1/archive"
SAMPLE_START_DATE = date(2015, 1, 1)
SAMPLE_END_DATE = date(2024, 12, 31)
OBSERVABLE = "daily_precipitation_mm"
DAILY_VARIABLE = "precipitation_sum"
TIMEZONE = "UTC"
ROLLING_WINDOW = 30
HIGH_OMEGA_Q = 0.99
EVENT_Q = 0.95
NULL_TOLERANCE = 1e-12
USER_AGENT = "omega-repro-london-weather-activity-test/1.0"


@dataclass(frozen=True)
class WeatherRow:
    day: date
    daily_precipitation_mm: float
    intensity: float | None
    gradient: float | None
    omega: float | None


def archive_url() -> str:
    params = {
        "latitude": f"{LATITUDE:.4f}",
        "longitude": f"{LONGITUDE:.4f}",
        "start_date": SAMPLE_START_DATE.isoformat(),
        "end_date": SAMPLE_END_DATE.isoformat(),
        "daily": DAILY_VARIABLE,
        "timezone": TIMEZONE,
    }
    return f"{ENDPOINT}?{urllib.parse.urlencode(params)}"


def fetch_daily_precipitation() -> list[tuple[date, float]]:
    request = urllib.request.Request(
        archive_url(),
        headers={"User-Agent": USER_AGENT},
    )
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            raw_payload = response.read().decode("utf-8")
    except urllib.error.URLError as exc:
        raise SystemExit(f"failed to fetch Open-Meteo Archive API data: {exc}") from exc

    try:
        payload = json.loads(raw_payload)
    except json.JSONDecodeError as exc:
        raise SystemExit(f"invalid JSON response from Open-Meteo Archive API: {exc}") from exc

    daily = payload.get("daily")
    if not isinstance(daily, dict):
        raise SystemExit("invalid Open-Meteo response: missing daily object")

    raw_dates = daily.get("time")
    raw_precipitation = daily.get(DAILY_VARIABLE)
    if not isinstance(raw_dates, list) or not isinstance(raw_precipitation, list):
        raise SystemExit("invalid Open-Meteo response: missing daily time or precipitation list")
    if len(raw_dates) != len(raw_precipitation):
        raise SystemExit("invalid Open-Meteo response: time and precipitation lengths differ")

    rows: list[tuple[date, float]] = []
    seen_days: set[date] = set()
    for raw_day, raw_value in zip(raw_dates, raw_precipitation):
        if not isinstance(raw_day, str):
            raise SystemExit(f"invalid Open-Meteo date value: {raw_day!r}")
        try:
            day = datetime.strptime(raw_day, "%Y-%m-%d").date()
        except ValueError as exc:
            raise SystemExit(f"invalid Open-Meteo date value: {raw_day!r}") from exc
        if day in seen_days:
            raise SystemExit(f"duplicate Open-Meteo date value: {day.isoformat()}")
        seen_days.add(day)

        if not isinstance(raw_value, (int, float)) or isinstance(raw_value, bool):
            raise SystemExit(f"invalid precipitation value for {day.isoformat()}: {raw_value!r}")
        value = float(raw_value)
        if value < 0:
            raise SystemExit(f"negative precipitation value for {day.isoformat()}: {value}")
        rows.append((day, value))

    expected_days = date_range(SAMPLE_START_DATE, SAMPLE_END_DATE)
    expected_set = set(expected_days)
    returned_set = {day for day, _value in rows}
    if returned_set != expected_set:
        missing = sorted(expected_set - returned_set)
        extra = sorted(returned_set - expected_set)
        raise SystemExit(
            "Open-Meteo returned an unexpected date set; "
            f"missing={len(missing)}, extra={len(extra)}"
        )

    rows.sort(key=lambda row: row[0])
    return rows


def date_range(start_day: date, end_day: date) -> list[date]:
    if start_day > end_day:
        raise SystemExit(f"invalid date range: {start_day} after {end_day}")
    days = (end_day - start_day).days + 1
    return [start_day + timedelta(days=offset) for offset in range(days)]


def rolling_sample_std(values: list[float], index: int, window: int) -> float | None:
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


def build_rows(daily_precipitation: list[tuple[date, float]]) -> list[WeatherRow]:
    values = [value for _day, value in daily_precipitation]
    rows: list[WeatherRow] = []
    for index, (day, daily_precipitation_mm) in enumerate(daily_precipitation):
        intensity = rolling_sample_std(values, index, ROLLING_WINDOW)
        gradient = None if index == 0 else abs(daily_precipitation_mm - values[index - 1])
        omega = None if intensity is None or gradient is None else intensity * gradient
        rows.append(
            WeatherRow(
                day=day,
                daily_precipitation_mm=daily_precipitation_mm,
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
    result_class: str,
) -> None:
    lines = [
        ("domain", DOMAIN),
        ("location", LOCATION),
        ("coordinates", f"latitude={LATITUDE:.4f}, longitude={LONGITUDE:.4f}"),
        ("data source", DATA_SOURCE),
        ("endpoint", ENDPOINT),
        (
            "fixed query",
            "latitude=51.5072; longitude=-0.1276; daily=precipitation_sum; timezone=UTC",
        ),
        (
            "sample period",
            f"{SAMPLE_START_DATE.isoformat()} through {SAMPLE_END_DATE.isoformat()} UTC, inclusive",
        ),
        ("time zone rule", "UTC daily dates returned by the Open-Meteo Archive API"),
        ("observable variable", "daily_precipitation_mm = precipitation_sum in millimeters"),
        ("aggregation rule", "one UTC calendar day as returned by Open-Meteo Archive API"),
        ("I definition", "rolling sample standard deviation(daily_precipitation_mm, window = 30 days)"),
        ("G definition", "absolute first difference(daily_precipitation_mm)"),
        ("Omega definition", "Omega = I x G"),
        ("high-Omega threshold", f"Omega > q(0.99), q_0.99 = {format_float(q_omega)}"),
        (
            "event definition",
            f"daily_precipitation_mm > q(0.95), q_0.95 = {format_float(q_event)}",
        ),
        ("event timing rule", "contemporaneous: event_t is compared with high_Omega_t"),
        ("P(event | high Omega)", format_float(p_event_high)),
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
    daily_precipitation = fetch_daily_precipitation()
    rows = build_rows(daily_precipitation)
    valid_rows = [row for row in rows if row.omega is not None]
    if not valid_rows:
        raise SystemExit("no valid analysis rows after applying the fixed 30-day rolling window")

    q_omega = linear_quantile([row.omega for row in valid_rows if row.omega is not None], HIGH_OMEGA_Q)
    q_event = linear_quantile([row.daily_precipitation_mm for row in valid_rows], EVENT_Q)

    high_omega = [row.omega is not None and row.omega > q_omega for row in valid_rows]
    events = [row.daily_precipitation_mm > q_event for row in valid_rows]

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
        result_class=result_class,
    )


if __name__ == "__main__":
    main()
