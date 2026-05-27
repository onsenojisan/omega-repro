# London Weather Activity Test Sequence Summary v1.0

Status: Internal sequence summary
Purpose: Summarize the London weather activity Omega test sequence
Scope: London, United Kingdom daily precipitation
Publication status: Internal only / not a public-facing claim

Related files:
- maintenance/LONDON_WEATHER_ACTIVITY_DOMAIN_SELECTION_V1.md
- maintenance/LONDON_WEATHER_ACTIVITY_FIXED_SCOPE_V1.md
- scripts/london_weather_activity_test.py
- maintenance/LONDON_WEATHER_ACTIVITY_RESULT_V1.md

---

## 1. Sequence status

The London weather activity sequence currently contains one fixed-scope test:

1. London, United Kingdom daily precipitation test

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
weather

Location:
London, United Kingdom

Data source:
Open-Meteo Archive API

Observable:
daily precipitation

Omega:
rolling 30-day precipitation dispersion multiplied by absolute daily precipitation change

High-Omega condition:
Omega > q(0.99)

Independent event:
daily_precipitation_mm > q(0.95)

Timing:
contemporaneous

Result class:
positive concentration

Recorded values:

- P(event | high Omega): 0.513513513514
- baseline P(event): 0.0496688741722
- ratio: 10.3387387387
- n_total: 3653
- n_valid: 3624
- n_high: 37
- n_event_total: 180
- n_event_high: 19

---

## 4. Relationship to completed sequences

This London weather activity sequence is separate from the closed GitHub activity sequence.

This London weather activity sequence is separate from the closed Wikipedia activity sequence.

This London weather activity sequence is separate from the closed global earthquake activity sequence.

This London weather activity sequence is separate from any existing Tokyo weather result.

It is not a Tokyo replacement, reinterpretation, public update, or extension.

---

## 5. Interpretation boundary

This sequence evaluates structural concentration only.

It does not claim prediction, causality, weather forecasting, climate interpretation, public warning, intervention, policy relevance, risk scoring, or full validation of the theory.

It should not be integrated into public-facing materials without a separate public-facing review.

End of document.
