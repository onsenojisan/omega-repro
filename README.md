# Ω Reproduction (PJM)

Reproduce structural collapse in minutes.

---

## What happens

Collapse-related events (6 steps ahead) concentrate in extreme Ω states.

---

## Quick Start

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

## Notes

This is a specific implementation.

Guide (fixed cross-domain interface):  
https://zenodo.org/records/19199493  

Reproducibility package:  
https://zenodo.org/records/19159664

After running (30 sec):

Report your result:
https://github.com/onsenojisan/omega-repro/issues/new?template=report.md

Report (minimal):
domain / data / collapse definition / P(collapse | high Ω) / baseline
