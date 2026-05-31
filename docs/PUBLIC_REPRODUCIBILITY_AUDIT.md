# Public Reproducibility Audit

This document is an inspection and reproducibility audit for existing public registry rows. It is not a new analysis, does not add an empirical domain, does not add registry rows, and does not change any reported metric, threshold, window, lead, event definition, or output artifact.

## Claim Boundary

This repository evaluates structural concentration only:

`P(event | high Omega)` versus baseline `P(event)`

Event definitions must be independent from Omega. This audit does not support prediction, causality, optimization, trading strategy, intervention, forecasting, or earthquake early-warning claims.

## Public Registry Row Audit

| domain | registry row present | fixed source artifact repository-local | exact working directory | exact rerun command | script path | fixed input artifact path | output artifact path | dependencies | caveats | reproducibility status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AAPL source-consistent rerun | yes | yes | `source_consistent_three_domain` | `python scripts/aapl_source_consistent_v1_rerun.py` | `source_consistent_three_domain/scripts/aapl_source_consistent_v1_rerun.py` | `source_consistent_three_domain/data/aapl_fixed_ohlc_2024-05-25_2026-05-25.csv` | `source_consistent_three_domain/results/aapl_source_consistent_v1_summary_2026-05-25.json` | Python with `numpy` and `pandas` | Sparse high-Omega tail; rerun writes the existing result CSV and JSON outputs. | Fully rerunnable from repository-local fixed source artifacts, assuming dependencies are installed. |
| BTC source-consistent rerun | yes | yes | `source_consistent_three_domain` | `python scripts/btc_source_consistent_v1_rerun.py` | `source_consistent_three_domain/scripts/btc_source_consistent_v1_rerun.py` | `source_consistent_three_domain/data/btc_fixed_ohlc_2024-05-25_2026-05-25.csv` | `source_consistent_three_domain/results/btc_source_consistent_v1_summary_2026-05-25.json` | Python with `numpy` and `pandas` | Sparse high-Omega tail; fixed snapshot omits `2026-05-24`; rerun writes the existing result CSV and JSON outputs. | Fully rerunnable from repository-local fixed source artifacts, assuming dependencies are installed. |
| Earthquake Japan source-consistent rerun | yes | yes | `source_consistent_three_domain` | `python scripts/earthquake_future_event_window_labels.py` then `python scripts/earthquake_source_consistent_v1_rerun.py` | `source_consistent_three_domain/scripts/earthquake_future_event_window_labels.py`; `source_consistent_three_domain/scripts/earthquake_source_consistent_v1_rerun.py` | `source_consistent_three_domain/data/earthquake_japan_usgs_fixed_catalog_2020-01-01_2025-01-01.csv`; `source_consistent_three_domain/data/earthquake_japan_future_3h_event_labels_2020-01-01_2025-01-01.csv` | `source_consistent_three_domain/results/earthquake_source_consistent_v1_summary_2026-05-25.json` | Python with `numpy` and `pandas` | Has a label-construction step plus a rerun step; rerun writes the existing result CSV and JSON outputs; not forecasting, warning, hazard prediction, or early-warning evidence. | Fully rerunnable from repository-local fixed source artifacts, assuming dependencies are installed. |

## Dependency Note

Local reruns require Python with `numpy` and `pandas`. The source-consistent scripts read fixed repository-local input artifacts, verify expected hashes where applicable, and write result artifacts under `source_consistent_three_domain/results/`.

## Caveats

- AAPL has a sparse high-Omega tail.
- BTC has a sparse high-Omega tail.
- The BTC fixed snapshot omits `2026-05-24`.
- Earthquake Japan has a label-construction step plus a rerun step.
- Earthquake Japan is not forecasting, warning, hazard prediction, or early-warning evidence.

## Inspected But Not Public Registry Rows

- PJM is referenced as an external reference example, but complete fixed registry metrics are not stored as repository-local result artifacts.
- The minimal CSV template has a workflow and sample CSV, but no explicit completed result block is stored in the repository.

## Interpretation

Sparse, weak, null, or source-limited results should be reported and flagged, not hidden. A sparse or weak outcome is still a valid reproducibility outcome under the fixed minimal protocol.
