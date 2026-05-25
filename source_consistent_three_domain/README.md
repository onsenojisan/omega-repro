# Source-Consistent Three-Domain Ω Reruns

This folder contains a public subset for the source-consistent AAPL, BTC, and Earthquake Japan reruns.
It includes fixed source artifacts, source intake notes, standalone scripts, result files, and concise review notes.

This is a structural concentration test. It is not a prediction model, trading strategy, causal claim, forecasting claim, or earthquake early-warning method.
Events are defined independently from Ω. Ω is used as a conditioning state, not as the event definition.

## Domains

| Domain | Main Ratio | Notes |
| --- | ---: | --- |
| AAPL | `15.966666666666667` | Fixed Yahoo Finance/yfinance OHLC snapshot; sparse high-Ω tail. |
| BTC | `17.256944444444443` | Fixed Yahoo Finance/yfinance OHLC snapshot; sparse high-Ω tail; fixed snapshot omits `2026-05-24`. |
| Earthquake Japan | `6.004434589800443` | Fixed USGS catalog and fixed future 3-hour event labels; not forecasting or early warning. |

Full internal validation material remains separate. This subset is intended to expose only the public-facing source-consistent artifacts needed to inspect or rerun the three fixed-source checks.

## Minimal Rerun Commands

```bash
python scripts/aapl_source_consistent_v1_rerun.py
python scripts/btc_source_consistent_v1_rerun.py
python scripts/earthquake_future_event_window_labels.py
python scripts/earthquake_source_consistent_v1_rerun.py
```

If regenerating Earthquake results from the raw USGS catalog, construct the future 3-hour event labels before running the Earthquake source-consistent V1 rerun.

## Caveats

- AAPL and BTC have sparse high-Ω tails.
- The BTC fixed snapshot omits `2026-05-24`.
- The Earthquake Japan result is not a forecasting claim and is not an early-warning method.
