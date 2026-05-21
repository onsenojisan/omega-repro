# Ω Reproduction (PJM)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/onsenojisan/omega-repro/blob/main/templates/omega_minimal_template/omega_minimal_template.ipynb)

Run first: no local setup. Opens the minimal Colab template with included example data.

This repository tests whether independently defined binary events structurally concentrate under fixed ex-ante definitions. It is a reproducibility structure, not a prediction model.

---

## Fastest runnable entry

1. Open the Colab notebook: [omega_minimal_template.ipynb](templates/omega_minimal_template/omega_minimal_template.ipynb)
2. Run with the included example data
3. Replace the CSV to try your own data

---

## Reproduce the PJM example

1. Download dataset  
https://zenodo.org/records/19159664  

2. Upload to Colab  

3. Run  
reproduce_omega_pjm.ipynb  

---

## Try Ω on your own data

Use the [minimal template](templates/omega_minimal_template/) to upload a CSV and test whether independently defined binary events concentrate in high-Ω states. This is a structural concentration test, not prediction. Null results are valid.

Links: [notebook](templates/omega_minimal_template/omega_minimal_template.ipynb) / [example_data.csv](templates/omega_minimal_template/example_data.csv)

---

## Event definition

ratio_95 = p95 / p_RTO  

event = 1 if ratio_95 ≥ q(0.998)  

---

## Ω

Ω = I × G  

---

## Ω Reference Guide

This is a specific implementation.

Guide (fixed cross-domain interface):  
https://zenodo.org/records/19199493  

Existing research terminology guide:  
[docs/EXISTING_RESEARCH_CONNECTIONS_OMEGA.md](docs/EXISTING_RESEARCH_CONNECTIONS_OMEGA.md)

Reproducibility package:  
https://zenodo.org/records/19159664

After running (30 sec):

Report your result:
https://github.com/onsenojisan/omega-repro/issues/new?template=report.md

Report (minimal):
domain / data / collapse definition / P(collapse | high Ω) / baseline
