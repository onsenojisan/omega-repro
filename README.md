# Open Structural Concentration Testbench

> **Restart status:** The current VOT / The Pleasure Order restart status is summarized in [`RESTART_STATUS.md`](https://github.com/onsenojisan/vot-the-pleasure-order/blob/main/RESTART_STATUS.md). Earlier Omega empirical and reproducibility materials should be read as historical, methodological, or exploratory unless explicitly reauthorized. This repository is not the current project center and should not be read as current validation of Omega.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/onsenojisan/omega-repro/blob/main/templates/omega_minimal_template/omega_minimal_template.ipynb)

This repository preserves the historical V1 CSV-based reproducibility testbench for structural concentration comparisons. It checks whether an independently defined binary event is more frequent in high-Ω rows than in the full baseline, using fixed definitions chosen before looking at results. It is not prediction, classification, trading, optimization, causal inference, or current validation of Ω.

Boundary note: The earlier Ω-centered empirical layer should not be treated as current validation. Existing V1 materials remain historical, fixed, and Ω-centered. High ratio alone is not evidence. Future empirical claims require independent event labels, frozen definitions, anti-circularity review, sufficient support counts, and validation design before evaluation.

Execution hub:  
https://onsenojisan.github.io/omega-library/

## Minimal comparison

The core comparison is:

`P(event | high Ω)` versus `baseline P(event)`

The binary event definition must be independent from Ω. Event thresholds, high-Ω thresholds, and inclusion rules should be fixed ex ante. Null results are valid reproducibility outcomes. High ratio alone should not be treated as evidence.

## Fastest runnable entry

1. Open the Colab notebook: [omega_minimal_template.ipynb](templates/omega_minimal_template/omega_minimal_template.ipynb)
2. Run it with the included example CSV.
3. Read the output comparison: `P(event | high Ω)`, `baseline P(event)`, ratio, and row counts when available.

No local setup is required for the Colab path.

## Try the testbench on your own data

Use the [minimal template](templates/omega_minimal_template/) as a historical V1 executable comparison with a CSV containing a numeric value column and an independently defined binary event column. The included example uses: time, value, event. Replace the sample file with your own data, keep definitions fixed, and report either concentration or a null result. This template is not a validation tool for Ω.

Links: [notebook](templates/omega_minimal_template/omega_minimal_template.ipynb) / [example_data.csv](templates/omega_minimal_template/example_data.csv)

## Reference example: PJM electricity prices

The included reference example applies the same workflow to PJM electricity price data.

Reproducibility package:  
https://zenodo.org/records/19159664

Example event definition:

`ratio_95 = p95 / p_RTO`

`event = 1 if ratio_95 >= q(0.998)`

This PJM example is a reference case for the testbench, not the scope limit of the repository.

## Core definition

`Ω = I × G`

This repository provides a reproducible implementation of the historical V1 structural concentration check around Ω. It does not claim to forecast events, assign class labels, recommend trades, optimize decisions, establish causality, or validate Ω.

## Reference materials

Guide (fixed cross-domain interface):  
https://zenodo.org/records/20107274

Existing research terminology guide:  
[docs/EXISTING_RESEARCH_CONNECTIONS_OMEGA.md](docs/EXISTING_RESEARCH_CONNECTIONS_OMEGA.md)

Public result registry: [results/public_result_registry.md](results/public_result_registry.md)

## Report a result

Report your result:  
https://github.com/onsenojisan/omega-repro/issues/new?template=report.md

Report format:

`Domain / P(event | high Ω) / baseline P(event) / ratio / n_rows if available / n_high if available / n_event_high if available`
