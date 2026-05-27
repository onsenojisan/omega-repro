# Earthquake Activity Domain Selection v1.0

Status: Internal domain-selection and design note
Purpose: Select a new empirical domain after the closed GitHub and Wikipedia activity sequences
Scope: Global earthquake activity sequence
Publication status: Internal only / not a public claim

Related files:
- maintenance/INTERNAL_OMEGA_EMPIRICAL_DESIGN_MAP_V1.md
- maintenance/EMPIRICAL_MAINTENANCE_INDEX_V2.md

---

## 1. Purpose

This note selects the next internal empirical domain before execution.

It is not a result document.

It does not modify the closed GitHub activity or Wikipedia activity sequences.

It does not create a public-facing claim.

---

## 2. Completed-sequence boundary

The current GitHub activity sequence is closed for current internal comparison.

The current Wikipedia activity sequence is closed for current internal comparison.

The next test should therefore use a new domain rather than adding another GitHub repository or Wikipedia page to the completed sequences.

This global earthquake activity sequence is also separate from any prior Japan earthquake result.

It is not a reinterpretation, correction, replacement, or extension of any Japan-specific earthquake result.

---

## 3. Selected domain

Selected domain:
global earthquake activity

Domain type:
event-sequence / natural hazard activity record

Reason for selection:
The internal empirical design map lists earthquakes as a suitable domain with:

- a magnitude / event sequence observable
- rolling magnitude or activity dispersion as I
- magnitude or activity change as G
- Omega = I x G
- a future event above a fixed magnitude threshold
- default high-Omega threshold q = 0.99

This domain is separate from the completed information-system activity tests.

It is a global USGS catalog activity-count test, not a Japan-region earthquake test.

It uses a public, reproducible scientific data source.

It does not require new theory before execution.

---

## 4. Fixed design direction

The first earthquake activity test should use a simple daily global activity-count operationalization.

Observable:
daily count of global earthquakes with preferred magnitude >= 5.5

I:
rolling sample standard deviation of the daily count over a 30-day window

G:
absolute first difference of the daily count

Omega:
I x G

High-Omega condition:
Omega > q(0.99), computed on valid analysis rows

Independent event:
whether the next UTC day contains at least one earthquake with preferred magnitude >= 6.5

Timing rule:
one-day forward association; high-Omega_t is compared with event_{t+1}

This timing rule is fixed before execution.

It is not a prediction, warning, causality, intervention, policy, trading, or risk-score design.

---

## 5. Data-source suitability

Preferred source:
USGS FDSN Event API

Reason:
The USGS earthquake catalog API supports fixed date windows, CSV output, minimum magnitude filters, event type filters, and UTC time interpretation.

The test should use only fixed historical dates.

If the API is unavailable or the fixed query cannot be reproduced, the sequence should stop rather than replacing the source after inspection.

---

## 6. Screening against the design map

The domain satisfies the design-map screening criteria:

- time-indexed dataset: yes
- measurable observable: yes, daily count of magnitude >= 5.5 events
- dispersion component: yes, rolling count dispersion
- directional change component: yes, absolute daily count change
- independently definable event outcome: yes, next-day magnitude >= 6.5 occurrence
- enough observations for q = 0.99 conditioning: expected from a multi-decade daily sample
- reproducible public source: yes, USGS FDSN Event API
- low post-hoc definition risk: yes, all thresholds and timing are fixed before execution
- minimal interpretation burden: yes, only a concentration comparison is reported
- no theory expansion required: yes

---

## 7. Claim boundary

This domain selection does not claim that earthquakes follow an Omega pattern.

It only selects global earthquake activity as a suitable internal empirical sequence for one fixed-scope test.

Any result must remain limited to the fixed operationalization and must report:

- P(event | high Omega)
- baseline P(event)
- ratio
- event and high-Omega counts
- result class

Do not use this selection note to support prediction, causality, earthquake forecasting, hazard assessment, intervention, policy, emergency planning, risk scoring, or public warning claims.

End of document.
