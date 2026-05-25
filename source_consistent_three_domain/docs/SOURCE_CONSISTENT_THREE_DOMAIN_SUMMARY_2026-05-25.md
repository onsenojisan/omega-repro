# Source-Consistent Three-Domain Ω Summary 2026-05-25

## 1. Conclusion

Three source-consistent fixed-source reruns have been completed: AAPL, BTC, and Earthquake Japan.
Each result uses a fixed source artifact, source intake record, standalone rerun script, result files, and review note.
This document summarizes source-consistent evidence only.
This is not a prediction model, trading strategy, causal claim, forecasting claim, or earthquake early-warning method.

## 2. What This Tests

The test asks whether independently defined collapse-like events concentrate in high-Ω states.
Ω is a conditioning state, not the event definition.
Events are defined independently from Ω.
The reported comparison is P(collapse | high Ω) versus baseline P(collapse).

## 3. Source-Consistent Results

| Domain | Fixed Source Artifact | Event Definition | P(collapse \| high Ω) | Baseline | Ratio | n_high | Event Count | Main Caveat |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| AAPL | fixed Yahoo Finance/yfinance OHLC snapshot | intraday range `(High - Low) / Close > q(0.95)` | `0.8` | `0.05010438413361169` | `15.966666666666667` | `5` | `24` | sparse high-Ω tail |
| BTC | fixed Yahoo Finance/yfinance OHLC snapshot | intraday range `(High - Low) / Close > q(0.95)` | `0.875` | `0.05070422535211268` | `17.256944444444443` | `8` | `36` | sparse high-Ω tail; fixed snapshot omits `2026-05-24` |
| Earthquake Japan | fixed USGS catalog + fixed future 3h labels | later event within 3h with `mag >= 5.5` | `0.14634146341463414` | `0.024372230428360415` | `6.004434589800443` | `41` | `99` | not forecasting or early warning |

## 4. Control Summary

| Domain | Temporal Shift Result | Shuffled-Label Result | Interpretation |
| --- | --- | --- | --- |
| AAPL | +30 ratio `3.9916666666666667`, +60 `0.0`, +120 `0.0` | mean ratio `0.9579999999999999`, max `11.975` | original concentration remains above shuffled mean; sparse denominator caveat |
| BTC | +30 ratio `0.0`, +60 `2.579365079365079`, +120 `0.0` | mean ratio `1.0354166666666667`, max `9.86111111111111` | original concentration remains above shuffled mean; sparse denominator caveat |
| Earthquake Japan | +30 / +60 / +120 ratios all `0.0` | mean ratio `0.8306134515890613`, max `3.0022172949002215` | timing shifts remove reviewed concentration |

## 5. Source Artifacts

AAPL:

- `data/aapl_fixed_ohlc_2024-05-25_2026-05-25.csv`
- `docs/source_intake/AAPL_FIXED_SOURCE_SNAPSHOT_INTAKE_2026-05-25.md`
- `scripts/aapl_source_consistent_v1_rerun.py`
- `docs/control/AAPL_SOURCE_CONSISTENT_V1_RERUN_2026-05-25.md`

BTC:

- `data/btc_fixed_ohlc_2024-05-25_2026-05-25.csv`
- `docs/source_intake/BTC_FIXED_SOURCE_SNAPSHOT_INTAKE_2026-05-25.md`
- `scripts/btc_source_consistent_v1_rerun.py`
- `docs/control/BTC_SOURCE_CONSISTENT_V1_RERUN_2026-05-25.md`

Earthquake:

- `data/earthquake_japan_usgs_fixed_catalog_2020-01-01_2025-01-01.csv`
- `data/earthquake_japan_future_3h_event_labels_2020-01-01_2025-01-01.csv`
- `docs/source_intake/EARTHQUAKE_FIXED_SOURCE_CATALOG_INTAKE_2026-05-25.md`
- `scripts/earthquake_source_consistent_v1_rerun.py`
- `docs/control/EARTHQUAKE_SOURCE_CONSISTENT_V1_RERUN_2026-05-25.md`

## 6. Claim Boundary

This is a structural concentration summary.
It is not a prediction model.
It is not a trading strategy.
It is not causal evidence.
It is not an earthquake forecasting or early-warning method.
The results do not imply endorsement of the broader theory.
Null results in future domains would remain valid under the protocol.

## 7. Status

This is a public-facing draft extracted from completed source-consistent internal validation chains.
It should not replace CONTROL_SUMMARY.md.
CONTROL_SUMMARY.md remains the internal validation summary.
This draft should be reviewed before use in Zenodo, GitHub Pages, note, Substack, or other public-facing surfaces.
