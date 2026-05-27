# Chicago Traffic Activity Domain Selection v1.0

Status: Internal domain-selection and design note
Purpose: Select Chicago traffic crash daily counts as the next internal traffic-region empirical sequence
Scope: Chicago, Illinois traffic crash activity
Publication status: Internal only / not a public-facing claim

Related files:
- AGENTS.md
- maintenance/EMPIRICAL_MAINTENANCE_INDEX_V4.md
- maintenance/INTERNAL_OMEGA_EMPIRICAL_DESIGN_MAP_V1.md
- maintenance/INTERNAL_EMPIRICAL_SEQUENCES_STATUS_REVIEW_V2.md

---

## 1. Purpose

This note selects one internal traffic-region empirical sequence before fixed execution.

It is not a result document.

It does not create a public-facing claim.

It does not modify any completed result memo.

It does not authorize prediction, causality, intervention, policy, traffic-safety recommendation, risk-score, public-warning, or public-facing integration language.

---

## 2. Selection basis

The internal empirical sequences status review v2 recommends traffic region as the preferred next candidate if a clean public source and fixed event definition are available.

The internal empirical design map lists traffic as a suitable domain with:

- daily count observable
- rolling count dispersion as I
- daily count change as G
- Omega = I x G
- extreme accident count as event / collapse
- default high-Omega threshold q = 0.99

Chicago, Illinois daily traffic crash count is selected as one traffic-region sequence.

This is a new internal traffic-region sequence.

It is separate from the completed GitHub activity, Wikipedia activity, global earthquake activity, and London weather activity sequences.

It is also separate from any prior traffic result. It is not a replacement, reinterpretation, public update, or extension of any prior traffic result.

---

## 3. Source verification

Preferred data source:
official City of Chicago public crash dataset

Selected data source:
City of Chicago Data Portal, Traffic Crashes - Crashes

Dataset identifier:
85ca-t3if

Dataset API endpoint:
https://data.cityofchicago.org/resource/85ca-t3if.json

Dataset metadata endpoint:
https://data.cityofchicago.org/api/views/85ca-t3if

Attribution observed from metadata:
City of Chicago

Schema field selected for crash date:

- display name: CRASH_DATE
- API field name: crash_date
- observed data type in metadata: calendar_date
- field role: date and time of crash as entered by the reporting officer

The selected source is public, reproducible through the Socrata API, and provides a clear crash date/time field for daily count construction.

---

## 4. Selected domain

Domain:
traffic

Region:
Chicago, Illinois

Observable:
daily traffic crash count

Sample period:
2018-01-01 through 2024-12-31, inclusive

Reason for selection:
Chicago daily crash counts provide ordered daily observations, an official public source, a clear date/time field, and a low-interpretation binary event definition based on an extreme daily count rule.

---

## 5. Fixed design direction

The Chicago traffic activity test should use:

I:
rolling sample standard deviation of daily crash count over a 30-day window

G:
absolute daily crash-count change

Omega:
I x G

High-Omega condition:
Omega > q(0.99), computed on valid analysis rows

Independent event:
daily crash count > q(0.95), computed from raw daily crash count on valid analysis rows

Timing rule:
contemporaneous; event_t is compared with high_Omega_t

The event is defined from raw daily crash count only.

It is not defined from Omega, I, G, the high-Omega threshold, or any post-hoc condition selected after inspecting results.

---

## 6. Screening against the design map

The selected Chicago traffic sequence satisfies the design-map screening criteria:

- time-indexed dataset: yes
- measurable observable: yes, daily traffic crash count
- dispersion component: yes, rolling daily count dispersion
- directional change component: yes, absolute daily crash-count change
- independently definable event outcome: yes, raw daily count above a fixed quantile rule
- enough observations for q = 0.99 conditioning: expected from the fixed seven-year daily sample
- reproducible public source: yes, official City of Chicago Data Portal API
- low post-hoc definition risk: yes, definitions are fixed before execution
- minimal interpretation burden: yes, only structural concentration is reported
- no theory expansion required: yes

---

## 7. Claim boundary

This selection note does not claim that Chicago traffic crash activity follows an Omega pattern.

It only selects Chicago daily traffic crash count as one internal fixed-scope traffic-region sequence.

Do not use this selection note to support prediction, causality, intervention, policy, traffic-safety recommendation, risk scoring, public warning, operational guidance, or public-facing validation claims.

End of document.
