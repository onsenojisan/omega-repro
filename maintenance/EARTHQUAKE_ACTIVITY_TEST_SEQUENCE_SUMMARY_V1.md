# Earthquake Activity Test Sequence Summary v1.0

Status: Internal sequence summary
Purpose: Summarize the first earthquake activity Omega test sequence
Scope: Global earthquake activity
Publication status: Internal only / not a public cross-domain claim

Related files:
- maintenance/EARTHQUAKE_ACTIVITY_DOMAIN_SELECTION_V1.md
- maintenance/EARTHQUAKE_ACTIVITY_FIXED_SCOPE_V1.md
- scripts/earthquake_activity_global_m55_test.py
- maintenance/EARTHQUAKE_ACTIVITY_RESULT_V1.md

---

## 1. Sequence status

The earthquake activity sequence currently contains one fixed-scope test:

1. global USGS earthquake activity daily magnitude-count test

This summary does not replace the result memo.

---

## 2. Sequence order

The sequence preserved the required order:

1. domain selection/design note
2. fixed-scope memo
3. execution script
4. script execution
5. result memo
6. sequence summary

No result-driven method changes were made.

---

## 3. Test summary

Domain:
global earthquake activity

Data source:
USGS FDSN Event API

Observable:
daily count of global earthquakes with preferred magnitude >= 5.5

Omega:
rolling 30-day count dispersion multiplied by absolute daily count change

High-Omega condition:
Omega > q(0.99)

Independent event:
next UTC day contains at least one earthquake with preferred magnitude >= 6.5

Timing:
one-day forward association

Result class:
positive concentration

Recorded values:

- P(event | high Omega): 0.221052631579
- baseline P(event): 0.106897644449
- ratio: 2.06789057624
- n_total: 9496
- n_valid: 9467
- n_high: 95
- n_event_total: 1012
- n_event_high: 21

---

## 4. Relationship to completed sequences

This earthquake activity sequence is separate from the closed GitHub activity sequence.

This earthquake activity sequence is separate from the closed Wikipedia activity sequence.

This global earthquake activity sequence is separate from any prior Japan earthquake result.

It is not a Japan-region extension, reinterpretation, or replacement.

It should not be used to reopen either completed information-system activity sequence.

---

## 5. Interpretation boundary

This sequence evaluates structural concentration only.

It does not claim prediction, causality, earthquake forecasting, hazard assessment, emergency planning, intervention, policy relevance, risk scoring, or full validation of the theory.

It should not be integrated into public-facing materials without a separate public-facing review.

End of document.
