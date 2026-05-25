# BTC Fixed Source Snapshot Intake 2026-05-25

## 1. Conclusion

- Fixed raw OHLC snapshot was created for source-consistent BTC rerun preparation.
- This is source intake only.
- No Ω calculation, control rerun, shuffled-label test, or temporal-shift test was performed.
- Existing BTC results remain internal-only / caveated.

## 2. Definition Anchor

- Existing BTC V1 definitions are taken from the reviewed BTC control hierarchy.
- Ticker: BTC-USD
- Source: Yahoo Finance via yfinance
- Use High, Low, Close
- Use Close as analysis basis
- Do not substitute adjusted prices unless explicitly justified.
- Event definition later: (High - Low) / Close > q(0.95)
- High-Ω threshold later: q(0.99)
- Event definition remains independent of Ω.

## 3. Snapshot File

| Field | Value |
| --- | --- |
| file path | `data/btc_fixed_ohlc_2024-05-25_2026-05-25.csv` |
| retrieval date/time | `2026-05-25T05:44:03Z` |
| yfinance version | `1.4.0` |
| pandas version | `3.0.3` |
| requested start date | `2024-05-25` |
| requested end date | `2026-05-25` |
| query end date | `2026-05-26` |
| actual first date | `2024-05-25` |
| actual last date | `2026-05-25` |
| row count | `730` |
| columns | `Date`, `Open`, `High`, `Low`, `Close`, `Adj Close`, `Volume` |
| SHA256 hash | `d856e196192be7a6776d61b3d3008618ae588091578b68407507a5dcdd215adb` |

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
| crypto 24/7 calendar-day handling | caveat | The requested inclusive calendar span has `731` dates, but yfinance returned `730` rows. The missing calendar date is `2026-05-24`. |
| timezone / daily boundary assumptions | caveat | yfinance returned date-only daily candles. The CSV does not store an explicit timezone; daily boundaries are inherited from Yahoo Finance / yfinance output. |

## 5. Rerun Authorization Status

- Snapshot intake is complete with a calendar-day caveat for missing date `2026-05-24`.
- Rerun is not performed in this step.
- Rerun may proceed only after this intake is reviewed.
- Expected output schema remains V1.

## 6. Claim Boundary

- This snapshot does not itself validate Ω.
- This is not a prediction model.
- This is not a trading strategy.
- This is not causal evidence.
- This is preparation for a structural concentration test under fixed definitions.
