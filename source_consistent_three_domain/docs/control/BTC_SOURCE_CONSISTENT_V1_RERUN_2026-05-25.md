# BTC Source-Consistent V1 Rerun 2026-05-25

## 1. Conclusion

- Source-consistent BTC V1 rerun was performed.
- Input was the fixed raw OHLC snapshot.
- No external data was fetched in this rerun.
- No notebooks were executed.
- This is a structural concentration test, not prediction, trading, or causality.

## 2. Input

| Field | Value |
| --- | --- |
| input file path | `data/btc_fixed_ohlc_2024-05-25_2026-05-25.csv` |
| SHA256 | `d856e196192be7a6776d61b3d3008618ae588091578b68407507a5dcdd215adb` |
| actual first date | `2024-05-25` |
| actual last date | `2026-05-25` |
| raw snapshot rows | `730` |
| valid evaluation rows | `710` |
| source intake note path | `docs/source_intake/BTC_FIXED_SOURCE_SNAPSHOT_INTAKE_2026-05-25.md` |
| policy path | `docs/source_intake/BTC_FIXED_SOURCE_SNAPSHOT_POLICY_2026-05-25.md` |
| missing calendar date caveat | `2026-05-24` is absent from the fixed snapshot and was not imputed or refetched. |

## 3. Fixed Definitions

| Component | Definition |
| --- | --- |
| `I` | rolling standard deviation of returns, window `20` |
| `G` | absolute return |
| Ω | `I × G` |
| collapse event | `(High - Low) / Close > q(0.95)` |
| high Ω | `Ω > q(0.99)` |
| event independence | event definition is independent of Ω |

## 4. Original Result

| n_rows | total event count | baseline P(collapse) | n_high | n_event_high | P(collapse given high Ω) | ratio | q_event_0.95 | q_omega_0.99 |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `710` | `36` | `0.05070422535211268` | `8` | `7` | `0.875` | `17.256944444444443` | `0.07337343979783484` | `0.002550863535200483` |

## 5. Temporal Shift Controls

Temporal shifts use +row label shifts. Rows with missing shifted labels are excluded rather than imputed or wrapped.

| shift | n_rows | dropped rows | total event count | baseline | n_high | n_event_high | P(collapse given high Ω) | ratio |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `30` | `680` | `30` | `36` | `0.052941176470588235` | `8` | `0` | `0.0` | `0.0` |
| `60` | `650` | `60` | `36` | `0.055384615384615386` | `7` | `1` | `0.14285714285714285` | `2.579365079365079` |
| `120` | `590` | `120` | `30` | `0.05084745762711865` | `6` | `0` | `0.0` | `0.0` |

## 6. Shuffled-Label Controls

| runs | mean P(collapse given high Ω) | median P(collapse given high Ω) | min P(collapse given high Ω) | max P(collapse given high Ω) | mean ratio | median ratio | min ratio | max ratio | mean n_event_high | min n_event_high | max n_event_high |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `100` | `0.0525` | `0.0` | `0.0` | `0.5` | `1.0354166666666667` | `0.0` | `0.0` | `9.86111111111111` | `0.42` | `0` | `4` |

The shuffled-label control permutes only the binary collapse labels. Ω, high-Ω membership, thresholds, row eligibility, and event count remain fixed. The fixed high-Ω tail is sparse (`n_high = 8`), so individual overlaps can move ratios sharply.

## 7. Comparison With Previous BTC Result

- The previous BTC result remains internal-only / caveated.
- This rerun supersedes the previous BTC result only for source-consistent BTC evidence.
- Do not mix live rolling-window BTC result and fixed-snapshot BTC result.

## 8. Claim Boundary

- This is not a prediction model.
- This is not a trading strategy.
- This is not causal evidence.
- No optimization or tuning was performed.
- Definitions were fixed ex ante for this rerun.
- The event definition is independent of Ω.

## 9. Output Files

- `scripts/btc_source_consistent_v1_rerun.py`
- `results/btc_source_consistent_v1_original_2026-05-25.csv`
- `results/btc_source_consistent_v1_temporal_shifts_2026-05-25.csv`
- `results/btc_source_consistent_v1_shuffled_runs_2026-05-25.csv`
- `results/btc_source_consistent_v1_summary_2026-05-25.json`
- `docs/control/BTC_SOURCE_CONSISTENT_V1_RERUN_2026-05-25.md`
