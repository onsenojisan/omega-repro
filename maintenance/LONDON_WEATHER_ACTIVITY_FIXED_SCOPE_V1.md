# London Weather Activity Fixed Scope v1.0

Status: Internal / pre-data fixed scope
Purpose: Fixed execution scope for the London weather activity Omega test
Scope: London, United Kingdom daily precipitation
Publication status: Not a result report

Related files:
- maintenance/LONDON_WEATHER_ACTIVITY_DOMAIN_SELECTION_V1.md
- maintenance/INTERNAL_OMEGA_EMPIRICAL_DESIGN_MAP_V1.md
- maintenance/INTERNAL_EMPIRICAL_SEQUENCES_STATUS_REVIEW_V1.md

---

## 1. Purpose

This document fixes the execution scope for the London weather activity Omega structural concentration test.

This is not a result document.

This document is created before API access, data collection, Omega computation, event evaluation, or result interpretation.

The purpose is to prevent post-hoc location selection, data-source selection, sample-period selection, observable selection, threshold selection, timing selection, or event-definition tuning.

---

## 2. Test status

Current status:
pre-data
pre-computation
pre-result
internal only

No empirical claim is made here.

---

## 3. Domain and location

Domain:
weather

Location:
London, United Kingdom

Coordinates:

- latitude = 51.5072
- longitude = -0.1276

Location role:
additional weather location for internal comparison

Boundary:
This London sequence is separate from any existing Tokyo weather result. It is not a replacement, reinterpretation, public update, or extension of a Tokyo result.

---

## 4. Data source

Data source:
Open-Meteo Archive API

Endpoint:
https://archive-api.open-meteo.com/v1/archive

Fixed query parameters:

- latitude = 51.5072
- longitude = -0.1276
- start_date = 2015-01-01
- end_date = 2024-12-31
- daily = precipitation_sum
- timezone = UTC

Response format:
JSON

If the API is unavailable or the fixed query cannot be reproduced, stop and report the sequence as blocked rather than changing the source, location, sample period, observable, threshold, or timing rule.

---

## 5. Sample period

Sample period:
2015-01-01 through 2024-12-31, inclusive

Time zone rule:
Use UTC daily dates returned by the Open-Meteo Archive API.

Do not change the sample period after inspecting data or results.

---

## 6. Observable variable

Primary observable:
daily precipitation

Definition:
daily_precipitation_mm = Open-Meteo daily precipitation_sum for London, United Kingdom, in millimeters

One observable only:
Do not combine precipitation with temperature, wind, pressure, humidity, snowfall, weather code, or other fields in the default test.

Missing values:
If any daily precipitation value is missing, null, non-numeric, or the date series is incomplete, stop and report the sequence as blocked rather than imputing values after inspection.

---

## 7. Daily aggregation rule

Aggregation unit:
one UTC calendar day as returned by Open-Meteo Archive API

For each day in the sample period:
daily_precipitation_mm = precipitation_sum for that UTC date

Zero-precipitation days:
Keep zero-precipitation days as observed values.

---

## 8. Omega definition

Default Omega definition:
I = rolling sample standard deviation(daily_precipitation_mm, window = 30 days)
G = absolute first difference(daily_precipitation_mm)
Omega = I x G

Equivalent notation:
I_t = rolling_std(daily_precipitation_mm, 30)
G_t = |daily_precipitation_mm_t - daily_precipitation_mm_{t-1}|
Omega_t = I_t x G_t

Rolling window:
30 days

Window status:
fixed before evaluation

Do not tune the rolling window after seeing the result.

---

## 9. High-Omega condition

Default high-Omega condition:
high Omega = Omega > q(0.99)

Quantile rule:
q is computed within valid analysis rows after Omega is computed.

Rows with insufficient rolling-window history are excluded from valid analysis rows.

The high-Omega threshold must not be changed after seeing the result.

---

## 10. Independent event definition

Event:
event_t = daily_precipitation_mm_t > q(0.95)

Quantile rule:
q(0.95) is computed from raw daily_precipitation_mm on valid analysis rows.

Event independence:
The event is defined from raw daily precipitation only.

It is not defined from Omega, I, G, the high-Omega threshold, the Omega quantile, or any post-hoc condition selected after inspecting Omega results.

Do not modify the event threshold after seeing results.

---

## 11. Event timing rule

Timing:
contemporaneous

Comparison:
event_t is compared with high_Omega_t

This timing rule is fixed before execution.

This is not a prediction, forecast, causality, intervention, policy, public-warning, or risk-score design.

No lead, lag, or window length is part of the default test.

---

## 12. Minimum output required after execution

The result must report:

- domain
- location
- coordinates
- data source
- sample period
- time zone rule
- observable variable
- aggregation rule
- I definition
- G definition
- Omega definition
- high-Omega threshold
- event definition
- event timing rule
- P(event | high Omega)
- baseline P(event)
- ratio
- n_total
- n_valid
- n_high
- n_event_total
- n_event_high
- result_class

Sparse cases must explicitly report n_high and n_event_high.

---

## 13. Exclusion / sparse rules

Delay, block, or classify as sparse if:

- the API response cannot be reproduced
- the returned date series is incomplete
- any daily precipitation value is missing, null, or non-numeric
- no valid analysis rows remain after the rolling window
- n_high is too small for stable interpretation
- n_event_high is zero

Do not change the domain, location, data source, sample period, observable, I, G, Omega, high-Omega threshold, event threshold, or timing rule to avoid a sparse, null, negative, inverse, weak, or inconvenient result.

---

## 14. Claim boundary

This test evaluates structural concentration only.

It asks whether an independently defined high-precipitation event occurs more frequently under high-Omega conditions than at baseline.

It does not claim prediction, causality, weather forecasting, climate interpretation, public warning, intervention, policy relevance, risk scoring, or full validation of the theory.

The result applies only to this fixed London daily precipitation operationalization.

End of document.
