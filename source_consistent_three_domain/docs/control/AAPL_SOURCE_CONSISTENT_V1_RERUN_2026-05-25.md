# AAPL Source-Consistent V1 Rerun 2026-05-25

## 1. Conclusion

- Source-consistent AAPL V1 rerun was performed.
- Input was the fixed raw OHLC snapshot.
- No external data was fetched in this rerun.
- No notebooks were executed.
- This is a structural concentration test, not prediction, trading, or causality.

## 2. Input

| Field | Value |
| --- | --- |
| input file path | `data/aapl_fixed_ohlc_2024-05-25_2026-05-25.csv` |
| SHA256 | `e368084c40010af1cd33d9c492256faaf0bda5f19c44790092b16d824d7e0577` |
| actual first date | `2024-05-28` |
| actual last date | `2026-05-22` |
| row count in raw snapshot | `499` |
| valid evaluation rows | `479` |
| source intake note path | `docs/source_intake/AAPL_FIXED_SOURCE_SNAPSHOT_INTAKE_2026-05-25.md` |
| policy path | `docs/source_intake/AAPL_FIXED_SOURCE_SNAPSHOT_POLICY_2026-05-25.md` |

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
| `479` | `24` | `0.05010438413361169` | `5` | `4` | `0.8` | `15.966666666666667` | `0.04021460650369431` | `0.001975258814809518` |

## 5. Temporal Shift Controls

Temporal shift uses the existing V1 circular-shift convention:

```python
np.roll(collapse_labels, shift)
```

This preserves event count and evaluates shifted labels against the fixed high-Ω mask.

| shift | n_rows | total event count | baseline | n_high | n_event_high | P(collapse given high Ω) | ratio |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `30` | `479` | `24` | `0.05010438413361169` | `5` | `1` | `0.2` | `3.9916666666666667` |
| `60` | `479` | `24` | `0.05010438413361169` | `5` | `0` | `0.0` | `0.0` |
| `120` | `479` | `24` | `0.05010438413361169` | `5` | `0` | `0.0` | `0.0` |

## 6. Shuffled-Label Controls

| runs | mean P(collapse given high Ω) | median P(collapse given high Ω) | min P(collapse given high Ω) | max P(collapse given high Ω) | mean ratio | median ratio | min ratio | max ratio | mean n_event_high | min n_event_high | max n_event_high |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `100` | `0.04800000000000001` | `0.0` | `0.0` | `0.6` | `0.9579999999999999` | `0.0` | `0.0` | `11.975` | `0.24` | `0` | `3` |

The shuffled-label control permutes only the binary collapse labels. Ω, high-Ω membership, thresholds, row eligibility, and event count remain fixed. The fixed high-Ω tail is sparse in this two-year snapshot (`n_high = 5`), so individual overlaps can move ratios sharply.

## 7. Comparison With Previous Fallback AAPL Result

- The previous fallback result remains internal-only.
- This rerun supersedes the fallback AAPL result for source-consistent AAPL evidence.
- Do not mix fallback and fixed-snapshot results.

## 8. Claim Boundary

- This is not a prediction model.
- This is not a trading strategy.
- This is not causal evidence.
- No optimization or tuning was performed.
- Definitions were fixed ex ante for this rerun.
- The event definition is independent of Ω.

## 9. Output Files

- `scripts/aapl_source_consistent_v1_rerun.py`
- `results/aapl_source_consistent_v1_original_2026-05-25.csv`
- `results/aapl_source_consistent_v1_temporal_shifts_2026-05-25.csv`
- `results/aapl_source_consistent_v1_shuffled_runs_2026-05-25.csv`
- `results/aapl_source_consistent_v1_summary_2026-05-25.json`
- `docs/control/AAPL_SOURCE_CONSISTENT_V1_RERUN_2026-05-25.md`
