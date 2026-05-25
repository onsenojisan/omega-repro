"""Build fixed future 3-hour event-window labels for Earthquake Japan.

This script performs label construction only. It does not calculate Omega,
select high-Omega rows, run controls, shuffle labels, or fetch external data.
"""

from __future__ import annotations

import csv
import hashlib
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path


INPUT_PATH = Path("data/earthquake_japan_usgs_fixed_catalog_2020-01-01_2025-01-01.csv")
OUTPUT_PATH = Path("data/earthquake_japan_future_3h_event_labels_2020-01-01_2025-01-01.csv")
EXPECTED_SHA256 = "b04406376de91adf6c4ce802d228d3311275b5055b7146471446918b1931f1c5"
EVENT_MAG_THRESHOLD = 5.5
FUTURE_WINDOW = timedelta(hours=3)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_usgs_time(value: str) -> datetime:
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise ValueError(f"Timestamp lacks timezone: {value}")
    return parsed.astimezone(timezone.utc)


def format_optional_time(value: datetime | None) -> str:
    if value is None:
        return ""
    return value.isoformat(timespec="milliseconds").replace("+00:00", "Z")


def load_catalog(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    required = {"time", "id", "mag"}
    missing = sorted(required.difference(rows[0].keys() if rows else []))
    if missing:
        raise ValueError(f"Input catalog is missing required columns: {missing}")
    return rows


def main() -> None:
    actual_sha = sha256_file(INPUT_PATH)
    if actual_sha != EXPECTED_SHA256:
        raise SystemExit(
            f"Input SHA256 mismatch: expected {EXPECTED_SHA256}, got {actual_sha}"
        )

    rows = load_catalog(INPUT_PATH)
    times = [parse_usgs_time(row["time"]) for row in rows]
    mags = [float(row["mag"]) for row in rows]
    ids = [row["id"] for row in rows]

    if any(times[index] > times[index + 1] for index in range(len(times) - 1)):
        raise SystemExit("Input catalog is not sorted ascending by time")

    output_rows: list[dict[str, str | int | float]] = []
    qualifying_indices = [index for index, mag in enumerate(mags) if mag >= EVENT_MAG_THRESHOLD]

    for index, current_time in enumerate(times):
        window_end = current_time + FUTURE_WINDOW
        future_indices = [
            future_index
            for future_index in qualifying_indices
            if times[future_index] > current_time and times[future_index] <= window_end
        ]
        event_count = len(future_indices)
        first_index = future_indices[0] if future_indices else None
        max_mag = max((mags[future_index] for future_index in future_indices), default=None)

        output_rows.append(
            {
                "time": rows[index]["time"],
                "id": ids[index],
                "mag": rows[index]["mag"],
                "future_3h_mag_ge_5_5_event": 1 if event_count else 0,
                "future_3h_event_count": event_count,
                "future_3h_max_mag": "" if max_mag is None else max_mag,
                "future_3h_first_event_time": ""
                if first_index is None
                else format_optional_time(times[first_index]),
                "future_3h_first_event_id": "" if first_index is None else ids[first_index],
            }
        )

    fieldnames = [
        "time",
        "id",
        "mag",
        "future_3h_mag_ge_5_5_event",
        "future_3h_event_count",
        "future_3h_max_mag",
        "future_3h_first_event_time",
        "future_3h_first_event_id",
    ]
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_PATH.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(output_rows)

    label_sum = sum(int(row["future_3h_mag_ge_5_5_event"]) for row in output_rows)
    rows_with_count = sum(int(row["future_3h_event_count"]) > 0 for row in output_rows)
    first_labeled = next(
        (row["time"] for row in output_rows if int(row["future_3h_mag_ge_5_5_event"]) == 1),
        "",
    )
    last_labeled = next(
        (
            row["time"]
            for row in reversed(output_rows)
            if int(row["future_3h_mag_ge_5_5_event"]) == 1
        ),
        "",
    )
    summary = {
        "input_path": str(INPUT_PATH),
        "input_sha256": actual_sha,
        "output_path": str(OUTPUT_PATH),
        "output_sha256": sha256_file(OUTPUT_PATH),
        "raw_rows": len(rows),
        "output_rows": len(output_rows),
        "first_time": rows[0]["time"] if rows else "",
        "last_time": rows[-1]["time"] if rows else "",
        "total_event_labels": label_sum,
        "rows_with_future_3h_event_count_gt_0": rows_with_count,
        "max_future_3h_event_count": max(
            int(row["future_3h_event_count"]) for row in output_rows
        )
        if output_rows
        else 0,
        "max_future_3h_max_mag": max(
            (
                float(row["future_3h_max_mag"])
                for row in output_rows
                if row["future_3h_max_mag"] != ""
            ),
            default=None,
        ),
        "first_labeled_event_time": first_labeled,
        "last_labeled_event_time": last_labeled,
    }
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
