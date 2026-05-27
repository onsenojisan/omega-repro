# Earthquake Activity Fixed Scope v1.0

Status: Internal / pre-data fixed scope
Purpose: Fixed execution scope for first earthquake activity Omega test
Scope: Global USGS earthquake activity, daily magnitude-count sequence
Publication status: Not a result report

Related files:
- maintenance/EARTHQUAKE_ACTIVITY_DOMAIN_SELECTION_V1.md
- maintenance/INTERNAL_OMEGA_EMPIRICAL_DESIGN_MAP_V1.md

---

## 1. Purpose

This document fixes the execution scope for the first earthquake activity Omega structural concentration test.

This is not a result document.

This document is created before API access, data collection, Omega computation, event evaluation, or result interpretation.

The purpose is to prevent post-hoc domain selection, sample-period selection, observable selection, threshold selection, timing selection, or event-definition tuning.

---

## 2. Test status

Current status:
pre-data
pre-computation
pre-result
internal only

No empirical claim is made here.

---

## 3. Domain

Domain:
global earthquake activity

Domain type:
event-sequence / natural hazard activity record

Reason for selection:
Earthquakes are listed as a suitable event-sequence domain in the internal empirical design map.

The domain is separate from the closed GitHub activity and Wikipedia activity sequences.

The domain is also separate from any prior Japan earthquake result.

This test is global and uses the fixed USGS catalog query; it is not a Japan-region extension, reinterpretation, or replacement.

This test uses a fixed public scientific catalog and does not require new theory.

---

## 4. Data source

Data source:
USGS FDSN Event API

Endpoint:
https://earthquake.usgs.gov/fdsnws/event/1/query

Response format:
CSV

Fixed query filters:

- eventtype = earthquake
- minmagnitude = 5.5
- starttime = 2000-01-01T00:00:00 UTC
- endtime = 2025-12-31T23:59:59 UTC
- orderby = time-asc

Chunking rule:
The execution script may request the same fixed query in calendar-year chunks to avoid API result-limit failures.

Chunking must not change the fixed date range, event type, magnitude filter, or ordering.

If the API is unavailable or the fixed query cannot be reproduced, stop and report the sequence as blocked rather than changing the source or scope.

---

## 5. Sample period

Analysis-day sample period:
2000-01-01 through 2025-12-30 UTC, inclusive

Outcome lookahead coverage:
The source query includes 2025-12-31 UTC only so that the next-day event can be evaluated for 2025-12-30.

Time zone rule:
Use UTC dates derived from the USGS event time field.

Do not change the sample period after inspecting data or results.

---

## 6. Observable variable

Primary observable:
daily count of global earthquakes with preferred magnitude >= 5.5

Definition:
activity_count_t = number of USGS earthquake events on UTC day t with preferred magnitude >= 5.5

Zero-activity days:
Include calendar days with zero matching events.

One observable only:
Do not combine counts, maximum magnitude, depth, location, felt reports, significance, ShakeMap, PAGER, or other fields in the default test.

---

## 7. Daily aggregation rule

Aggregation unit:
one UTC calendar day

For each day in the analysis-day sample period:
activity_count_t = count of fixed-query events assigned to that UTC date

Duplicate event identifiers:
If duplicate event ids appear in the fixed query, the execution script must stop rather than silently choosing one record.

Missing dates:
Calendar dates with no matching events are retained as zero-count days.

---

## 8. Omega definition

Default Omega definition:
I = rolling sample standard deviation(activity_count, window = 30 days)
G = absolute first difference(activity_count)
Omega = I x G

Equivalent notation:
I_t = rolling_std(activity_count, 30)
G_t = |activity_count_t - activity_count_{t-1}|
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
event_t = the next UTC day, t+1, contains at least one USGS earthquake event with preferred magnitude >= 6.5

Magnitude threshold:
6.5

The event threshold is fixed before data access or result inspection.

Event independence:
The event is defined from the fixed catalog event magnitude and next-day date only.

It is not defined from Omega, I, G, the high-Omega threshold, the Omega quantile, or any post-hoc condition selected after inspecting Omega results.

Do not modify the event magnitude threshold after seeing results.

---

## 11. Event timing rule

Timing:
one-day forward association

Comparison:
event_t is compared with high_Omega_t, where event_t means whether day t+1 contains at least one magnitude >= 6.5 earthquake.

This timing rule is fixed before execution.

This is not a forecast, warning, causality, intervention, policy, emergency-planning, or risk-score design.

No other lead, lag, or window length is part of the default test.

---

## 12. Minimum output required after execution

The result must report:

- domain
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

Delay or classify as sparse if:

- the API response cannot be reproduced
- duplicate event identifiers appear
- no valid analysis rows remain after the rolling window
- n_high is too small for stable interpretation
- n_event_high is zero
- the event definition cannot be evaluated for the fixed sample

Do not change the domain, sample period, observable, I, G, Omega, high-Omega threshold, event threshold, or timing rule to avoid a sparse, null, negative, inverse, or weak result.

---

## 14. Claim boundary

This test evaluates structural concentration only.

It asks whether an independently defined next-day large-earthquake event occurs more frequently under high-Omega conditions than at baseline.

It does not claim prediction, causality, earthquake forecasting, hazard assessment, emergency planning, intervention, policy relevance, risk scoring, or full validation of the theory.

The result applies only to this fixed global USGS earthquake activity operationalization.

End of document.
