# London Weather Activity Domain Selection v1.0

Status: Internal domain-selection and design note
Purpose: Select London daily precipitation as the next internal weather-location empirical sequence
Scope: London, United Kingdom weather activity
Publication status: Internal only / not a public claim

Related files:
- maintenance/INTERNAL_OMEGA_EMPIRICAL_DESIGN_MAP_V1.md
- maintenance/EMPIRICAL_MAINTENANCE_INDEX_V3.md
- maintenance/INTERNAL_EMPIRICAL_SEQUENCES_STATUS_REVIEW_V1.md

---

## 1. Purpose

This note selects the next internal empirical sequence before execution.

It is not a result document.

It does not create a public-facing claim.

It does not modify any completed result memo.

---

## 2. Selection basis

The latest internal empirical sequences status review recommends an additional weather location as the next empirical direction.

The internal empirical design map lists weather as a suitable domain with:

- precipitation / temperature observable
- rolling dispersion as I
- daily change as G
- Omega = I x G
- extreme precipitation or weather event
- default high-Omega threshold q = 0.99

London, United Kingdom is selected as a fixed additional weather location.

This is a new internal weather-location sequence.

It is separate from the completed GitHub activity, Wikipedia activity, and global earthquake activity sequences.

It is also separate from any existing Tokyo weather result. It is not a replacement, reinterpretation, public update, or extension of a Tokyo result.

---

## 3. Selected domain

Domain:
weather

Location:
London, United Kingdom

Coordinates for execution:
latitude = 51.5072
longitude = -0.1276

Observable:
daily precipitation

Preferred data source:
Open-Meteo Archive API

Sample period:
2015-01-01 through 2024-12-31, inclusive

Reason for selection:
London daily precipitation provides a fixed weather-location test with ordered daily observations, a reproducible public data source, a clear observable, and a low-interpretation binary event definition.

---

## 4. Fixed design direction

The London weather activity test should use:

I:
rolling sample standard deviation of daily precipitation over a 30-day window

G:
absolute daily precipitation change

Omega:
I x G

High-Omega condition:
Omega > q(0.99), computed on valid analysis rows

Independent event:
daily precipitation > q(0.95), computed from raw daily precipitation on valid analysis rows

Timing rule:
contemporaneous; event_t is compared with high_Omega_t

The event is defined from raw daily precipitation only.

It is not defined from Omega, I, G, the high-Omega threshold, or any post-hoc condition selected after inspecting results.

---

## 5. Screening against the design map

The selected London weather sequence satisfies the design-map screening criteria:

- time-indexed dataset: yes
- measurable observable: yes, daily precipitation
- dispersion component: yes, rolling precipitation dispersion
- directional change component: yes, absolute daily precipitation change
- independently definable event outcome: yes, raw daily precipitation above a fixed quantile rule
- enough observations for q = 0.99 conditioning: expected from the fixed 10-year daily sample
- reproducible public source: yes, Open-Meteo Archive API
- low post-hoc definition risk: yes, definitions are fixed before execution
- minimal interpretation burden: yes, only structural concentration is reported
- no theory expansion required: yes

---

## 6. Claim boundary

This selection note does not claim that London precipitation follows an Omega pattern.

It only selects London daily precipitation as one internal fixed-scope weather-location sequence.

Do not use this selection note to support prediction, causality, intervention, policy, risk scoring, public warning, climate interpretation, weather forecasting, or public-facing validation claims.

End of document.
