# Earthquake Source-Consistent V1 Rerun 2026-05-25

## 1. Conclusion

- Source-consistent Earthquake V1 rerun was performed.
- Input was the fixed raw USGS catalog and fixed future 3-hour event labels.
- No external data was fetched in this rerun.
- No notebooks were executed.
- This is a structural concentration test, not prediction / forecasting / early warning / causality.

## 2. Input

| item | value |
| --- | --- |
| raw catalog file path | `data/earthquake_japan_usgs_fixed_catalog_2020-01-01_2025-01-01.csv` |
| raw catalog SHA256 | `b04406376de91adf6c4ce802d228d3311275b5055b7146471446918b1931f1c5` |
| label file path | `data/earthquake_japan_future_3h_event_labels_2020-01-01_2025-01-01.csv` |
| label file SHA256 | `39278964dbfd5535a37b4ec5e4856a240f64686b8caa099cf52d1741738f350f` |
| raw rows | `4081` |
| valid evaluation rows | `4062` |
| actual first time | `2020-01-01T01:08:54.688Z` |
| actual last time | `2024-12-31T16:28:31.896Z` |
| source intake note path | `docs/source_intake/EARTHQUAKE_FIXED_SOURCE_CATALOG_INTAKE_2026-05-25.md` |
| event-window construction note path | `docs/control/EARTHQUAKE_EVENT_WINDOW_LABEL_CONSTRUCTION_2026-05-25.md` |
| source policy path | `docs/source_intake/EARTHQUAKE_FIXED_SOURCE_CATALOG_POLICY_2026-05-25.md` |

## 3. Fixed Definitions

- I = rolling std of magnitude, window 20.
- G = absolute magnitude change.
- Ω = I × G.
- event label = future 3-hour window contains later mag >= 5.5.
- high Ω = Ω > q(0.99).
- event definition independent of Ω.

## 4. Original Result

| n_rows | total event count | baseline P(collapse) | n_high | n_event_high | P(collapse given high Ω) | ratio | q_omega_0.99 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `4062` | `99` | `0.024372230428360415` | `41` | `6` | `0.14634146341463414` | `6.004434589800443` | `0.8501531315554205` |

## 5. Temporal Shift Controls

| shift | n_rows | total event count | baseline | n_high | n_event_high | P(collapse given high Ω) | ratio |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `+30` | `4062` | `99` | `0.024372230428360415` | `41` | `0` | `0.0` | `0.0` |
| `+60` | `4062` | `99` | `0.024372230428360415` | `41` | `0` | `0.0` | `0.0` |
| `+120` | `4062` | `99` | `0.024372230428360415` | `41` | `0` | `0.0` | `0.0` |

## 6. Shuffled-Label Controls

| runs | mean P(collapse given high Ω) | median P(collapse given high Ω) | min P(collapse given high Ω) | max P(collapse given high Ω) | mean ratio | median ratio | min ratio | max ratio | mean n_event_high | min n_event_high | max n_event_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `100` | `0.02024390243902439` | `0.024390243902439025` | `0.0` | `0.07317073170731707` | `0.8306134515890613` | `1.000739098300074` | `0.0` | `3.0022172949002215` | `0.83` | `0` | `3` |

## 7. Comparison With Previous Earthquake Result

- The previous Earthquake result remains internal-only / caveated until this source-consistent chain is reviewed.
- This rerun supersedes the previous Earthquake result only for source-consistent Earthquake evidence because numeric consistency is confirmed.
- Do not mix previous review-only result and fixed-source rerun result without caveat.

## 8. Claim Boundary

- Not a prediction model.
- Not a forecasting claim.
- Not an earthquake early-warning method.
- In statistical seismology, this earthquake result should be interpreted as a minimal concentration screening result, not as evidence that Ω adds information beyond ETAS / Hawkes-process conditional intensity models.
- Not causal evidence.
- No optimization / tuning.
- Fixed ex-ante definitions.
- Independent event definition.

## 9. Output Files

- `results/earthquake_source_consistent_v1_original_2026-05-25.csv`
- `results/earthquake_source_consistent_v1_temporal_shifts_2026-05-25.csv`
- `results/earthquake_source_consistent_v1_shuffled_runs_2026-05-25.csv`
- `results/earthquake_source_consistent_v1_summary_2026-05-25.json`
