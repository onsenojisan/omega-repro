# Earthquake Activity Omega Test Result v1.0

Status: Internal result
Purpose: First earthquake activity Omega result
Scope: Global USGS earthquake activity, daily magnitude-count sequence
Publication status: Internal only / not a public cross-domain claim

Related files:
- maintenance/EARTHQUAKE_ACTIVITY_DOMAIN_SELECTION_V1.md
- maintenance/EARTHQUAKE_ACTIVITY_FIXED_SCOPE_V1.md
- scripts/earthquake_activity_global_m55_test.py

---

## 1. Status

This is the first global earthquake activity result produced from the fixed global earthquake activity Omega test sequence.

It is separate from any prior Japan earthquake result and does not reinterpret, replace, or extend any Japan-specific earthquake result.

The result was generated after the domain selection/design note, fixed-scope memo, and execution script were created.

No definitions, thresholds, sample periods, windows, event rules, or timing rules were changed after seeing the result.

---

## 2. Fixed scope

Use the fixed scope exactly as defined in:

maintenance/EARTHQUAKE_ACTIVITY_FIXED_SCOPE_V1.md

Summary:

- domain: global earthquake activity
- data source: USGS FDSN Event API
- endpoint: https://earthquake.usgs.gov/fdsnws/event/1/query
- fixed query: format=csv; eventtype=earthquake; minmagnitude=5.5; orderby=time-asc
- source query period: 2000-01-01 through 2025-12-31 UTC, inclusive
- sample period: 2000-01-01 through 2025-12-30 UTC, inclusive
- time zone rule: UTC dates derived from the USGS event time field
- observable variable: activity_count = daily count of earthquakes with preferred magnitude >= 5.5
- aggregation rule: one UTC calendar day, including zero-count days
- I definition: rolling sample standard deviation(activity_count, window = 30 days)
- G definition: absolute first difference(activity_count)
- Omega definition: Omega = I x G
- high-Omega threshold: Omega > q(0.99)
- event definition: next UTC day contains at least one earthquake with preferred magnitude >= 6.5
- event timing rule: one-day forward association: event_t is evaluated on day t+1

---

## 3. Exact script output

```text
domain: Global earthquake activity
data source: USGS FDSN Event API
endpoint: https://earthquake.usgs.gov/fdsnws/event/1/query
fixed query: format=csv; eventtype=earthquake; minmagnitude=5.5; orderby=time-asc
source query period: 2000-01-01 through 2025-12-31 UTC, inclusive
sample period: 2000-01-01 through 2025-12-30 UTC, inclusive
time zone rule: UTC dates derived from the USGS event time field
observable variable: activity_count = daily count of earthquakes with preferred magnitude >= 5.5
aggregation rule: one UTC calendar day, including zero-count days
I definition: rolling sample standard deviation(activity_count, window = 30 days)
G definition: absolute first difference(activity_count)
Omega definition: Omega = I x G
high-Omega threshold: Omega > q(0.99), q_0.99 = 18.6192361281
event definition: next UTC day contains at least one earthquake with preferred magnitude >= 6.5
event timing rule: one-day forward association: event_t is evaluated on day t+1
P(event | high Omega): 0.221052631579
baseline P(event): 0.106897644449
ratio: 2.06789057624
n_total: 9496
n_valid: 9467
n_high: 95
n_event_total: 1012
n_event_high: 21
n_catalog_events: 12847
result_class: positive concentration
```

---

## 4. Required result values

domain:
global earthquake activity

data source:
USGS FDSN Event API

sample period:
2000-01-01 through 2025-12-30 UTC, inclusive

observable:
activity_count = daily count of earthquakes with preferred magnitude >= 5.5

I:
rolling sample standard deviation(activity_count, window = 30 days)

G:
absolute first difference(activity_count)

Omega:
Omega = I x G

high-Omega threshold:
Omega > q(0.99), q_0.99 = 18.6192361281

independent event definition:
the next UTC day contains at least one earthquake with preferred magnitude >= 6.5

timing rule:
one-day forward association; event_t is evaluated on day t+1

P(event | high Omega):
0.221052631579

baseline P(event):
0.106897644449

ratio:
2.06789057624

n_total:
9496

n_valid:
9467

n_high:
95

n_event_total:
1012

n_event_high:
21

result class:
positive concentration

---

## 5. Result classification

result_class: positive concentration

The event rate under high-Omega rows is greater than the baseline event rate under the fixed specification.

This classification does not license changing the method, broadening the claim, or treating the result as an earthquake forecast.

---

## 6. Claim boundary

This test evaluates structural concentration only.

It asks whether an independently defined next-day large-earthquake event occurs more frequently under high-Omega conditions than at baseline.

It does not claim prediction, causality, earthquake forecasting, hazard assessment, emergency planning, intervention, policy relevance, risk scoring, or full validation of the theory.

The result applies only to this fixed global USGS earthquake activity operationalization.

It should not be merged with or used to reinterpret any Japan-specific earthquake result.

---

## 7. Limitations

This is one global earthquake activity test.

The source is a live USGS catalog interface, so future reruns may reflect any official catalog revisions returned by the API.

The observable uses daily global counts of magnitude >= 5.5 events only.

The event uses a fixed next-day magnitude >= 6.5 occurrence rule only.

The result does not evaluate location, depth, rupture mechanics, regional hazard, aftershock structure, seismic triggering, or earthquake impacts.

The one-day forward timing rule is a fixed association rule, not a forecast or warning rule.

---

## 8. Reproducibility notes

Execution script:
scripts/earthquake_activity_global_m55_test.py

Runtime:
Python standard library only.

Command used:

```powershell
C:\Users\garte\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe scripts\earthquake_activity_global_m55_test.py
```

The first attempt with `python` did not execute because `python` was not on PATH.

The first bundled-Python attempt inside the sandbox was blocked from network access before data retrieval.

The completed run used the same fixed script and required network permission to fetch the USGS FDSN Event API data.

End of document.
