# Chicago Traffic Activity Fixed Scope v1.0

Status: Internal / pre-execution fixed scope
Purpose: Fixed execution scope for the Chicago traffic crash activity Omega test
Scope: Chicago, Illinois daily traffic crash count
Publication status: Not a result report

Related files:
- maintenance/CHICAGO_TRAFFIC_ACTIVITY_DOMAIN_SELECTION_V1.md
- maintenance/INTERNAL_OMEGA_EMPIRICAL_DESIGN_MAP_V1.md
- maintenance/INTERNAL_EMPIRICAL_SEQUENCES_STATUS_REVIEW_V2.md

---

## 1. Purpose

This document fixes the execution scope for the Chicago traffic crash activity Omega structural concentration test.

This is not a result document.

This document is created before the fixed execution, Omega computation, event evaluation, or result interpretation.

The purpose is to prevent post-hoc region selection, data-source selection, sample-period selection, observable selection, threshold selection, timing selection, or event-definition tuning.

---

## 2. Test status

Current status:
pre-computation
pre-result
internal only

No empirical claim is made here.

---

## 3. Domain and region

Domain:
traffic

Region:
Chicago, Illinois

Region role:
traffic-region internal empirical sequence

Boundary:
This Chicago sequence is separate from any prior traffic result. It is not a replacement, reinterpretation, public update, or extension of any prior traffic result.

---

## 4. Data source

Data source:
City of Chicago Data Portal, Traffic Crashes - Crashes

Provider / attribution:
City of Chicago

Dataset identifier:
85ca-t3if

Dataset page:
https://data.cityofchicago.org/Transportation/Traffic-Crashes-Crashes/85ca-t3if

Socrata API endpoint:
https://data.cityofchicago.org/resource/85ca-t3if.json

Metadata endpoint:
https://data.cityofchicago.org/api/views/85ca-t3if

Fixed date field:

- display name: CRASH_DATE
- API field name: crash_date
- observed data type in metadata: calendar_date
- field role: date and time of crash as entered by the reporting officer

Fixed query family:

- select date_trunc_ymd(crash_date) as crash_day, count(*) as crash_count
- where crash_date >= '2018-01-01T00:00:00'
- where crash_date < '2025-01-01T00:00:00'
- group by date_trunc_ymd(crash_date)
- order by crash_day

Response format:
JSON

If the API is unavailable, the schema changes, the crash_date field is missing or ambiguous, or the fixed query cannot be reproduced, stop and report the sequence as blocked rather than changing the source, region, sample period, observable, threshold, or timing rule.

---

## 5. Sample period

Sample period:
2018-01-01 through 2024-12-31, inclusive

Date rule:
Use the date component of the official crash_date field returned by the City of Chicago Data Portal API.

Do not change the sample period after inspecting Omega results.

---

## 6. Observable variable

Primary observable:
daily traffic crash count

Definition:
daily_crash_count = number of crash records whose official crash_date falls on the UTC-free calendar date in the fixed Chicago dataset query

One observable only:
Do not combine crash counts with injury counts, speed limit, weather condition, lighting condition, crash type, location, severity, police beat, vehicle counts, or any other field in the default test.

Missing or incomplete days:
Construct a complete calendar-day series for the fixed sample period. If a returned day is missing from the grouped API response, treat its daily crash count as 0 only if the API response itself is valid and the missing day is within the fixed query period. If date parsing fails, duplicate grouped dates appear, or the API returns dates outside the fixed sample period, stop and report the sequence as blocked.

---

## 7. Daily aggregation rule

Aggregation unit:
one calendar day derived from crash_date

For each day in the sample period:
daily_crash_count = count of crash records with crash_date on that day

Zero-count days:
Keep zero-count days as observed daily counts if they occur in the complete fixed date range.

---

## 8. Omega definition

Default Omega definition:
I = rolling sample standard deviation(daily_crash_count, window = 30 days)
G = absolute first difference(daily_crash_count)
Omega = I x G

Equivalent notation:
I_t = rolling_std(daily_crash_count, 30)
G_t = |daily_crash_count_t - daily_crash_count_{t-1}|
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
event_t = daily_crash_count_t > q(0.95)

Quantile rule:
q(0.95) is computed from raw daily_crash_count on valid analysis rows.

Event independence:
The event is defined from raw daily crash count only.

It is not defined from Omega, I, G, the high-Omega threshold, the Omega quantile, or any post-hoc condition selected after inspecting Omega results.

Do not modify the event threshold after seeing results.

---

## 11. Event timing rule

Timing:
contemporaneous

Comparison:
event_t is compared with high_Omega_t

This timing rule is fixed before execution.

This is not a prediction, forecast, causality, intervention, traffic-safety recommendation, policy, public-warning, operational guidance, or risk-score design.

No lead, lag, or window length is part of the default test.

---

## 12. Minimum output required after execution

The result must report:

- domain
- region
- data source
- sample period
- date field
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
- n_source_records
- result_class

Sparse cases must explicitly report n_high and n_event_high.

---

## 13. Exclusion / sparse rules

Delay, block, or classify as sparse if:

- the API response cannot be reproduced
- the schema no longer contains crash_date
- the crash_date field becomes ambiguous
- the grouped date series contains duplicate dates
- the grouped date series contains dates outside the fixed sample period
- no valid analysis rows remain after the rolling window
- n_high is too small for stable interpretation
- n_event_high is zero

Do not change the domain, region, data source, sample period, observable, I, G, Omega, high-Omega threshold, event threshold, or timing rule to avoid a sparse, null, negative, inverse, weak, or inconvenient result.

---

## 14. Claim boundary

This test evaluates structural concentration only.

It asks whether an independently defined high daily crash-count event occurs more frequently under high-Omega conditions than at baseline.

It does not claim prediction, causality, intervention, traffic-safety recommendation, policy relevance, public warning, operational guidance, risk scoring, or full validation of the theory.

The result applies only to this fixed Chicago daily traffic crash count operationalization.

End of document.
