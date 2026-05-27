# Chicago Traffic Activity Omega Test Result v1.0

Status: Internal result
Purpose: Chicago daily traffic crash count Omega result
Scope: Chicago, Illinois traffic crash activity
Publication status: Internal only / not a public-facing claim

Related files:
- maintenance/CHICAGO_TRAFFIC_ACTIVITY_DOMAIN_SELECTION_V1.md
- maintenance/CHICAGO_TRAFFIC_ACTIVITY_FIXED_SCOPE_V1.md
- scripts/chicago_traffic_activity_test.py

---

## 1. Status

This is the result memo for the fixed Chicago traffic crash activity Omega test.

The result was generated after the domain selection/design note, fixed-scope memo, and execution script were created.

No definitions, thresholds, sample periods, windows, event rules, timing rules, data source, or date field were changed after seeing the result.

This Chicago traffic sequence is separate from any prior traffic result. It is not a replacement, reinterpretation, public update, or extension of any prior traffic result.

---

## 2. Fixed scope

Use the fixed scope exactly as defined in:

maintenance/CHICAGO_TRAFFIC_ACTIVITY_FIXED_SCOPE_V1.md

Summary:

- domain: traffic
- region: Chicago, Illinois
- data source: City of Chicago Data Portal, Traffic Crashes - Crashes
- dataset id: 85ca-t3if
- endpoint: https://data.cityofchicago.org/resource/85ca-t3if.json
- metadata endpoint: https://data.cityofchicago.org/api/views/85ca-t3if
- date field: CRASH_DATE / crash_date
- fixed query: grouped daily counts from crash_date for 2018-01-01 through 2024-12-31
- sample period: 2018-01-01 through 2024-12-31, inclusive
- observable variable: daily_crash_count = count of crash records per calendar day
- I definition: rolling sample standard deviation(daily_crash_count, window = 30 days)
- G definition: absolute first difference(daily_crash_count)
- Omega definition: Omega = I x G
- high-Omega threshold: Omega > q(0.99)
- event definition: daily_crash_count > q(0.95)
- event timing rule: contemporaneous

---

## 3. Exact script output

```text
domain: Traffic
region: Chicago, Illinois
data source: City of Chicago Data Portal, Traffic Crashes - Crashes
dataset id: 85ca-t3if
endpoint: https://data.cityofchicago.org/resource/85ca-t3if.json
metadata endpoint: https://data.cityofchicago.org/api/views/85ca-t3if
fixed query: select date_trunc_ymd(crash_date) as crash_day,count(*) as crash_count; where crash_date >= 2018-01-01T00:00:00 and crash_date < 2025-01-01T00:00:00; group by date_trunc_ymd(crash_date); order by crash_day
sample period: 2018-01-01 through 2024-12-31, inclusive
date field: CRASH_DATE / crash_date
source min crash_date: 2018-01-01T00:00:00.000
source max crash_date: 2024-12-31T23:47:00.000
observable variable: daily_crash_count = count of crash records per calendar day
aggregation rule: one calendar day derived from crash_date, including zero-count days if present
I definition: rolling sample standard deviation(daily_crash_count, window = 30 days)
G definition: absolute first difference(daily_crash_count)
Omega definition: Omega = I x G
high-Omega threshold: Omega > q(0.99), q_0.99 = 8541.60699871
event definition: daily_crash_count > q(0.95), q_0.95 = 388
event timing rule: contemporaneous: event_t is compared with high_Omega_t
P(event | high Omega): 0.538461538462
baseline P(event): 0.0498417721519
ratio: 10.8034188034
n_total: 2557
n_valid: 2528
n_high: 26
n_event_total: 126
n_event_high: 14
n_source_records: 768801
result_class: positive concentration
```

---

## 4. Required result values

domain:
traffic

region:
Chicago, Illinois

data source:
City of Chicago Data Portal, Traffic Crashes - Crashes

dataset id:
85ca-t3if

sample period:
2018-01-01 through 2024-12-31, inclusive

date field:
CRASH_DATE / crash_date

source min crash_date:
2018-01-01T00:00:00.000

source max crash_date:
2024-12-31T23:47:00.000

observable:
daily_crash_count = count of crash records per calendar day

I:
rolling sample standard deviation(daily_crash_count, window = 30 days)

G:
absolute first difference(daily_crash_count)

Omega:
Omega = I x G

high-Omega threshold:
Omega > q(0.99), q_0.99 = 8541.60699871

event definition:
daily_crash_count > q(0.95), q_0.95 = 388

timing rule:
contemporaneous; event_t is compared with high_Omega_t

P(event | high Omega):
0.538461538462

baseline P(event):
0.0498417721519

ratio:
10.8034188034

n_total:
2557

n_valid:
2528

n_high:
26

n_event_total:
126

n_event_high:
14

n_source_records:
768801

result class:
positive concentration

---

## 5. Result classification

result_class: positive concentration

The event rate under high-Omega rows is greater than the baseline event rate under the fixed specification.

This classification does not license changing the method, broadening the claim, or treating the result as a prediction, traffic-safety recommendation, warning, policy, intervention, operational, or risk result.

---

## 6. Claim boundary

This test evaluates structural concentration only.

It asks whether an independently defined high daily crash-count event occurs more frequently under high-Omega conditions than at baseline.

It does not claim prediction, causality, intervention, traffic-safety recommendation, policy relevance, public warning, operational guidance, risk scoring, or full validation of the theory.

The result applies only to this fixed Chicago daily traffic crash count operationalization.

---

## 7. Limitations

This is one traffic-region test.

The source is a public City of Chicago Data Portal API, so future reruns may reflect official data revisions returned by the portal.

The observable uses daily crash record counts only.

The event uses a fixed raw daily count q(0.95) rule only.

The result does not evaluate crash severity, injury outcomes, location, road design, weather, enforcement, responsibility, policy, interventions, traffic safety, public warnings, operational recommendations, or risk scoring.

The contemporaneous timing rule is a fixed association rule, not a forecast, warning, causal model, or intervention design.

---

## 8. Reproducibility notes

Execution script:
scripts/chicago_traffic_activity_test.py

Runtime:
Python standard library only.

Command used:

```powershell
C:\Users\garte\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe scripts\chicago_traffic_activity_test.py
```

The first attempt with `python` did not execute because `python` was not on PATH.

The first bundled-Python attempt inside the sandbox was blocked from network access before metadata retrieval.

The completed run used the same fixed script and required network permission to fetch the City of Chicago Data Portal metadata and grouped daily crash counts.

End of document.
