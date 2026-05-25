# AAPL Fixed Source Snapshot Intake 2026-05-25

## 1. Conclusion

- Fixed raw OHLC snapshot was created for source-consistent AAPL rerun preparation.
- This is source intake only.
- No Ω calculation, control rerun, shuffled-label test, or temporal-shift test was performed.
- Existing fallback AAPL results remain internal-only.

## 2. Definition Anchor

- Definition source-of-truth: Zenodo 19492994
- Ticker: AAPL
- Source: Yahoo Finance via yfinance
- auto_adjust=False
- Use High, Low, Close
- Use Close, not Adj Close
- Event definition later: (High - Low) / Close > q(0.95)
- High-Ω threshold later: q(0.99)
- Event definition remains independent of Ω

## 3. Snapshot File

| Field | Value |
| --- | --- |
| file path | `data/aapl_fixed_ohlc_2024-05-25_2026-05-25.csv` |
| retrieval date/time | `2026-05-25T04:38:19Z` |
| yfinance version | `1.4.0` |
| pandas version | `3.0.3` |
| requested start date | `2024-05-25` |
| requested end date | `2026-05-25` |
| query end date | `2026-05-26` |
| actual first date | `2024-05-28` |
| actual last date | `2026-05-22` |
| row count | `499` |
| columns | `Date`, `Open`, `High`, `Low`, `Close`, `Adj Close`, `Volume` |
| SHA256 hash | `e368084c40010af1cd33d9c492256faaf0bda5f19c44790092b16d824d7e0577` |

## 4. Data Quality Checks

| Check | Result | Notes |
| --- | --- | --- |
| missing High / Low / Close | pass | `High=0`, `Low=0`, `Close=0` |
| duplicated Date | pass | `0` duplicated dates |
| Date ordering | pass | Dates are ordered oldest to newest. |
| numeric High / Low / Close | pass | High, Low, and Close parsed as numeric values. |
| High >= Low | pass | `0` violations |
| Close / Adj Close both present | pass | Both columns are present. |
| Close used as analysis basis | recorded | Future rerun should use `Close`. |
| Adj Close not substituted | recorded | `Adj Close` is retained for provenance only. |
| Close outside High / Low range | pass | `0` rows |
| non-trading days / weekend / holiday handling | recorded | Requested start date `2024-05-25` fell before the first returned trading day `2024-05-28`; requested end date `2026-05-25` used exclusive query end `2026-05-26`, with last returned trading day `2026-05-22`. |

## 5. Rerun Authorization Status

- Snapshot intake is complete.
- Rerun is not performed in this step.
- Rerun may proceed only after this intake is reviewed.
- Expected output schema remains V1.

## 6. Claim Boundary

- This snapshot does not itself validate Ω.
- This is not a prediction model.
- This is not a trading strategy.
- This is not causal evidence.
- This is preparation for a structural concentration test under fixed definitions.
