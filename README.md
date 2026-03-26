# Ω Reproduction (PJM)

Reproduce structural collapse in minutes.

---

## What this is

This repository reproduces the PJM result in the reproducibility package.

---

## What happens

Collapse-related events concentrate in extreme Ω states.

---

## Quick Start

1. Download dataset  
https://zenodo.org/records/19159664  

2. Upload the dataset (rt_hrl_lmps_2025-03.csv) to Colab  

3. Run  
reproduce_omega_pjm.ipynb  

→ Expected:

- Event rate increases sharply in the highest Ω regime  
- Collapse-related events concentrate in extreme Ω states  
- Low Ω regions show near-zero event rate  

---

## Event definition (this implementation)

event = 1 if (p95 / p_RTO) exceeds the 0.998 quantile of the full sample

---

## Ω (Omega)

Ω = I × G

---

## Apply to your system

Replace:

- I (structural imbalance)  
- G (directional change)  
- collapse variable  

Keep:

- Ω = I × G  

---

## Notes

This repository reproduces a specific implementation.

It is not a fixed cross-domain specification.

For a minimal, fixed interface across domains, see the Guide:
https://zenodo.org/records/19199493  

---

## Reproducibility package

https://zenodo.org/records/19159664
