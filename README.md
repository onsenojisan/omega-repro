# Ω Reproduction & Results

A minimal, executable interface for testing structural collapse.

This repository is a minimal hub for reproducing and extending the Ω (Omega) framework.

---

## Core Hypothesis

Collapse may not be driven by levels (price, demand, utilization),

but by:

→ structure × direction

---

## Ω (Omega)

Ω integrates:

- structural imbalance (I)
- directional deviation (G)

into a single state variable.

Ω = I × G

---

## What is observed (in this setup)

Using real data (power systems and initial cross-domain tests):

- Most of the time → no events occur  
- When Ω becomes extreme → events appear  

→ Collapse-related events concentrate in extreme Ω states in this setup  

This suggests:

- collapse is not continuous  
- it may emerge as a regime shift  

---

## Quick Start

1. Download the dataset from Zenodo:  
   https://zenodo.org/records/19159664  

2. Upload the dataset (rt_hrl_lmps_2025-03.csv) to Colab  

3. Open and run:  
   reproduce_omega_pjm.ipynb  

→ Expected outcome:

- Event rate increases sharply in the highest Ω decile  
- Event concentration appears in extreme Ω states  
- Low Ω regions show near-zero event rate  

---

## Minimal Interface (for comparability)

To enable cross-domain comparison, a minimal interface is defined:

- Ω = I × G  
- collapse = defined as a single observable variable  

Notes:

- The specific construction of I and G is domain-dependent  
- The definition of collapse is domain-dependent  
- Event thresholds are fixed within each implementation  

This interface is fixed for comparability,  
but does NOT imply theoretical optimality or finality.

---

## Implementation in this repository (PJM case)

This notebook provides one concrete implementation in power systems.

### Ω construction

- I (imbalance) → zonal price dispersion (sigma_zone)  
- G (direction) → deviation of high-end price from system price (spread_95_rto)  

Ω is defined as:

Ω = sigma_zone × spread_95_rto  

---

### Event definition

Events are NOT defined directly from Ω.

Instead:

- A price ratio variable is constructed:  
  ratio_95 = p95 / p_rto  

- Event is defined as an extreme state of this ratio:  

  event = ratio_95 > q(0.998)

---

### Evaluation structure

The notebook evaluates:

→ whether future events concentrate in extreme Ω states

Specifically:

- event_lead6 = event shifted by +6 hours  
- current Ω is used to evaluate future event occurrence  

This tests whether extreme Ω states precede collapse-related events.

---

## What to do

- Reproduce the result using the provided package  
- Apply the same interface to other domains  
- Compare results across implementations  
- Test alternative constructions of Ω  

---

## Try Your Own Data

Replace:

- I (imbalance)  
- G (direction)  
- collapse definition  

Keep:

- Ω = I × G  
- collapse = a single observable variable  

Event definition should be fixed consistently within your implementation.

---

## How to Share Results

Open an Issue and include:

- dataset  
- Ω definition (I, G)  
- event definition  
- collapse definition  
- result summary  

---

## Open Questions (main entry points)

- Does collapse follow a threshold (gate-like) structure?  
- Is the interaction between I and G necessary?  
- Can collapse occur without one of them?  
- Can interventions reduce Ω before collapse?  
- What is the minimal sufficient structure for Ω?  

---

## Reference

Zenodo (reproducibility package):  
https://zenodo.org/records/19159664  

---

## Open

Reproducible and open.  

Independent implementations are strongly encouraged.  

Reproduction results can be shared here:  
https://github.com/onsenojisan/omega-repro
