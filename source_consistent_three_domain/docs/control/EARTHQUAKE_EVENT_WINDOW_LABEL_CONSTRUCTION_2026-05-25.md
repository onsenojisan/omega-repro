# Earthquake Future 3-Hour Event-Window Label Construction 2026-05-25

## 1. Conclusion

- Future 3-hour event-window labels were constructed from the fixed USGS catalog.
- This is label construction only.
- No Ω calculation, high-Ω selection, control rerun, shuffled-label test, or temporal-shift test was performed.

## 2. Input

| item | value |
| --- | --- |
| input catalog path | `data/earthquake_japan_usgs_fixed_catalog_2020-01-01_2025-01-01.csv` |
| input SHA256 | `b04406376de91adf6c4ce802d228d3311275b5055b7146471446918b1931f1c5` |
| raw row count | `4081` |
| first time | `2020-01-01T01:08:54.688Z` |
| last time | `2024-12-31T16:28:31.896Z` |
| source intake note path | `docs/source_intake/EARTHQUAKE_FIXED_SOURCE_CATALOG_INTAKE_2026-05-25.md` |
| source policy path | `docs/source_intake/EARTHQUAKE_FIXED_SOURCE_CATALOG_POLICY_2026-05-25.md` |

## 3. Event Definition

- For each row, event = 1 if a later event within 3 hours has `mag >= 5.5`.
- Current row is excluded.
- Future window uses `time_j > time_i` and `time_j <= time_i + 3 hours`.
- Event definition is independent of Ω.

## 4. Output

| item | value |
| --- | --- |
| output label file path | `data/earthquake_japan_future_3h_event_labels_2020-01-01_2025-01-01.csv` |
| output row count | `4081` |
| output SHA256 | `39278964dbfd5535a37b4ec5e4856a240f64686b8caa099cf52d1741738f350f` |
| output columns | `time`, `id`, `mag`, `future_3h_mag_ge_5_5_event`, `future_3h_event_count`, `future_3h_max_mag`, `future_3h_first_event_time`, `future_3h_first_event_id` |

## 5. Label Checks

| check | result | status |
| --- | --- | --- |
| total event labels | `99` | pass |
| rows with future_3h_event_count > 0 | `99` | pass |
| max future_3h_event_count | `5` | pass |
| max future_3h_max_mag | `7.5` | pass |
| first labeled event time | `2020-09-12T02:38:00.472Z` | pass |
| last labeled event time | `2024-11-26T12:18:13.433Z` | pass |
| label values 0/1 only | `0`, `1` | pass |
| future event time bounds | `0` violations | pass |
| label/count consistency | `0` violations | pass |
| consistency with prior total events = 99 | `99` | pass |

## 6. Rerun Authorization Status

- Event-window label construction is complete.
- Rerun is not performed in this step.
- Rerun may proceed only after this label construction is reviewed.
- Expected output schema remains V1.

## 7. Claim Boundary

- This label file does not itself validate Ω.
- This is not a prediction model.
- This is not a forecasting claim.
- This is not causal evidence.
- This is not an earthquake early-warning method.
- This is preparation for a structural concentration test under fixed definitions.
