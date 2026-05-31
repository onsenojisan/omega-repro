# Public Result Registry

This registry is a public inspection table, not a new analysis. It summarizes fixed-source or otherwise reproducible Omega structural concentration results already present in this repository, without changing fixed Omega definitions, event definitions, thresholds, windows, leads, or existing reported metrics.

Structural concentration means:

`P(event | high Ω)` versus baseline `P(event)`

Event definitions must be independent from Omega. Null, weak, sparse, unstable, or near-baseline results are valid outcomes and should be reported and flagged rather than hidden.

## Registry

| domain | data_source | time_range | omega_definition | event_definition | high_omega_threshold | P_event_given_high_omega | baseline_P_event | ratio | n_rows | n_high | n_event_high | reliability_flag | claim_boundary | rerun_command | artifact_link | notes |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| AAPL | fixed Yahoo Finance/yfinance OHLC snapshot | valid rows 2024-06-26 to 2026-05-22; raw snapshot 2024-05-28 to 2026-05-22 | I=rolling standard deviation of return, window=20; G=absolute return; Omega=I*G | (High - Low) / Close > q(0.95) | Omega > q(0.99); q=0.001975258814809518 | 0.8 | 0.05010438413361169 | 15.966666666666667 | 479 | 5 | 4 | sparse_high | structural concentration only | cd source_consistent_three_domain && python scripts/aapl_source_consistent_v1_rerun.py | source_consistent_three_domain/results/aapl_source_consistent_v1_summary_2026-05-25.json | Source-consistent fixed-source rerun; total_event_count=24; q_event_0.95=0.04021460650369431; high-Omega tail is sparse. |
| BTC | fixed Yahoo Finance/yfinance OHLC snapshot | valid rows 2024-06-14 to 2026-05-25; raw snapshot 2024-05-25 to 2026-05-25 | I=rolling standard deviation of return, window=20; G=absolute return; Omega=I*G | (High - Low) / Close > q(0.95) | Omega > q(0.99); q=0.002550863535200483 | 0.875 | 0.05070422535211268 | 17.256944444444443 | 710 | 8 | 7 | sparse_high | structural concentration only | cd source_consistent_three_domain && python scripts/btc_source_consistent_v1_rerun.py | source_consistent_three_domain/results/btc_source_consistent_v1_summary_2026-05-25.json | Source-consistent fixed-source rerun; total_event_count=36; q_event_0.95=0.07337343979783484; high-Omega tail is sparse; fixed snapshot omits 2026-05-24. |
| Earthquake Japan | fixed USGS catalog + fixed future 3-hour event labels | raw catalog 2020-01-01T01:08:54.688Z to 2024-12-31T16:28:31.896Z | I=rolling standard deviation of magnitude, window=20; G=absolute magnitude change; Omega=I*G | fixed future 3-hour window contains later mag >= 5.5 | Omega > q(0.99); q=0.8501531315554205 | 0.14634146341463414 | 0.024372230428360415 | 6.004434589800443 | 4062 | 41 | 6 | ok | structural concentration only | cd source_consistent_three_domain && python scripts/earthquake_source_consistent_v1_rerun.py | source_consistent_three_domain/results/earthquake_source_consistent_v1_summary_2026-05-25.json | Source-consistent fixed-source rerun; total_event_count=99; not forecasting or early warning; timing-shift controls remove reviewed concentration. |

## How To Read This Registry

- Compare `P_event_given_high_omega` with `baseline_P_event`.
- `ratio` is `P_event_given_high_omega / baseline_P_event` when both values are available.
- `n_high` and `n_event_high` are part of the result: sparse tails remain visible through `reliability_flag`.
- `rerun_command` points to an existing repository script when the fixed source artifact and exact rerun path are present.
- `artifact_link` points to the repository artifact used as the fixed source for the registry row.

## What This Registry Does Not Claim

- no prediction
- no causality
- no optimization
- no trading strategy
- no universal physical-law proof
- no earthquake early-warning claim

## Inspected But Not Registered

- PJM electricity reference example: the README and terminology document reference the Zenodo package and event definition, but this repository does not contain the fixed result metrics needed to populate the registry row without importing external values.
- Minimal CSV template example: the repository contains `templates/omega_minimal_template/example_data.csv` and the Colab workflow, but no explicit completed result block is stored in the repository.
