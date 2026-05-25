# Earthquake Fixed Source Catalog Intake 2026-05-25

## 1. Conclusion

- Fixed raw USGS earthquake catalog was created for source-consistent Earthquake rerun preparation.
- This is source intake only.
- No Ω calculation, event-window construction, control rerun, shuffled-label test, or temporal-shift test was performed.
- Existing Earthquake results remain internal-only / caveated.

## 2. Definition Anchor

- Existing Earthquake V1 definitions are taken from the reviewed Earthquake control hierarchy.
- Source: USGS FDSN event CSV API.
- Region: Japan-region bounding box.
- Latitude range: 30 to 46.
- Longitude range: 130 to 150.
- Date range: 2020-01-01 to 2025-01-01.
- Minimum magnitude: 3.0.
- Sequence ordering: ascending by event time.
- Timestamp basis: source-provided UTC event time.
- Magnitude field: mag.
- Future event definition later: future 3-hour window contains mag >= 5.5.
- High-Ω threshold later: q(0.99).
- Event definition remains independent of Ω.

## 3. Query

| item | value |
| --- | --- |
| endpoint | `https://earthquake.usgs.gov/fdsnws/event/1/query.csv` |
| serialized query URL | `https://earthquake.usgs.gov/fdsnws/event/1/query.csv?format=csv&starttime=2020-01-01&endtime=2025-01-01&minlatitude=30&maxlatitude=46&minlongitude=130&maxlongitude=150&minmagnitude=3.0&orderby=time-asc` |
| retrieval date/time | `2026-05-25T09:30:40Z` |
| format | `csv` |
| starttime | `2020-01-01` |
| endtime | `2025-01-01` |
| minlatitude | `30` |
| maxlatitude | `46` |
| minlongitude | `130` |
| maxlongitude | `150` |
| minmagnitude | `3.0` |
| orderby | `time-asc` |
| source response | HTTP `200`, `text/csv; charset=utf-8` |

## 4. Raw Catalog File

| item | value |
| --- | --- |
| file path | `data/earthquake_japan_usgs_fixed_catalog_2020-01-01_2025-01-01.csv` |
| row count | `4081` |
| columns | `time`, `latitude`, `longitude`, `depth`, `mag`, `magType`, `nst`, `gap`, `dmin`, `rms`, `net`, `id`, `updated`, `place`, `type`, `horizontalError`, `depthError`, `magError`, `magNst`, `status`, `locationSource`, `magSource` |
| actual first time | `2020-01-01T01:08:54.688Z` |
| actual last time | `2024-12-31T16:28:31.896Z` |
| SHA256 hash | `b04406376de91adf6c4ce802d228d3311275b5055b7146471446918b1931f1c5` |

## 5. Data Quality Checks

| check | result | notes |
| --- | --- | --- |
| required columns | pass | `time`, `latitude`, `longitude`, `depth`, `mag`, `id`, `place`, and `type` are present. |
| missing time | pass | `0` |
| missing mag | pass | `0` |
| missing id | pass | `0` |
| duplicate id | pass | `0` |
| duplicate full rows | pass | `0` |
| time parse success | pass | `0` parse errors |
| time ordering | pass | ascending by `time` |
| UTC / timezone notation | pass | all `4081` time strings end with `Z` |
| latitude bounds | pass | `0` rows outside 30 to 46 |
| longitude bounds | pass | `0` rows outside 130 to 150 |
| minimum magnitude check | pass | `0` rows below `3.0` |
| event types found | pass | `earthquake: 4081` |
| non-earthquake type count | pass | `0` |
| min / max magnitude | recorded | min `3.1`, max `7.5` |
| min / max latitude | recorded | min `30.0026`, max `45.9804` |
| min / max longitude | recorded | min `130.0628`, max `149.9906` |

## 6. Rerun Authorization Status

- Catalog intake is complete.
- Rerun is not performed in this step.
- Future 3-hour event-window construction is not performed in this step.
- Rerun may proceed only after this intake is reviewed.
- Expected output schema remains V1.

## 7. Claim Boundary

- This raw catalog does not itself validate Ω.
- This is not a prediction model.
- This is not a forecasting claim.
- This is not causal evidence.
- This is not an earthquake early-warning method.
- This is preparation for a structural concentration test under fixed definitions.
