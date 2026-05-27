# London Weather Activity Omega Test Result v1.0

Status: Internal result
Purpose: London daily precipitation weather activity Omega result
Scope: London, United Kingdom daily precipitation
Publication status: Internal only / not a public-facing claim

Related files:
- maintenance/LONDON_WEATHER_ACTIVITY_DOMAIN_SELECTION_V1.md
- maintenance/LONDON_WEATHER_ACTIVITY_FIXED_SCOPE_V1.md
- scripts/london_weather_activity_test.py

---

## 1. Status

This is the result memo for the fixed London weather activity Omega test.

The result was generated after the domain selection/design note, fixed-scope memo, and execution script were created.

No definitions, thresholds, sample periods, windows, event rules, or timing rules were changed after seeing the result.

This London sequence is separate from any existing Tokyo weather result. It is not a replacement, reinterpretation, public update, or extension of a Tokyo result.

---

## 2. Fixed scope

Use the fixed scope exactly as defined in:

maintenance/LONDON_WEATHER_ACTIVITY_FIXED_SCOPE_V1.md

Summary:

- domain: weather
- location: London, United Kingdom
- coordinates: latitude = 51.5072, longitude = -0.1276
- data source: Open-Meteo Archive API
- endpoint: https://archive-api.open-meteo.com/v1/archive
- fixed query: latitude=51.5072; longitude=-0.1276; daily=precipitation_sum; timezone=UTC
- sample period: 2015-01-01 through 2024-12-31 UTC, inclusive
- observable variable: daily_precipitation_mm = precipitation_sum in millimeters
- I definition: rolling sample standard deviation(daily_precipitation_mm, window = 30 days)
- G definition: absolute first difference(daily_precipitation_mm)
- Omega definition: Omega = I x G
- high-Omega threshold: Omega > q(0.99)
- event definition: daily_precipitation_mm > q(0.95)
- event timing rule: contemporaneous

---

## 3. Exact script output

```text
domain: Weather
location: London, United Kingdom
coordinates: latitude=51.5072, longitude=-0.1276
data source: Open-Meteo Archive API
endpoint: https://archive-api.open-meteo.com/v1/archive
fixed query: latitude=51.5072; longitude=-0.1276; daily=precipitation_sum; timezone=UTC
sample period: 2015-01-01 through 2024-12-31 UTC, inclusive
time zone rule: UTC daily dates returned by the Open-Meteo Archive API
observable variable: daily_precipitation_mm = precipitation_sum in millimeters
aggregation rule: one UTC calendar day as returned by Open-Meteo Archive API
I definition: rolling sample standard deviation(daily_precipitation_mm, window = 30 days)
G definition: absolute first difference(daily_precipitation_mm)
Omega definition: Omega = I x G
high-Omega threshold: Omega > q(0.99), q_0.99 = 101.745635181
event definition: daily_precipitation_mm > q(0.95), q_0.95 = 9.5
event timing rule: contemporaneous: event_t is compared with high_Omega_t
P(event | high Omega): 0.513513513514
baseline P(event): 0.0496688741722
ratio: 10.3387387387
n_total: 3653
n_valid: 3624
n_high: 37
n_event_total: 180
n_event_high: 19
result_class: positive concentration
```

---

## 4. Required result values

domain:
weather

location:
London, United Kingdom

data source:
Open-Meteo Archive API

sample period:
2015-01-01 through 2024-12-31 UTC, inclusive

observable:
daily_precipitation_mm = precipitation_sum in millimeters

I:
rolling sample standard deviation(daily_precipitation_mm, window = 30 days)

G:
absolute first difference(daily_precipitation_mm)

Omega:
Omega = I x G

high-Omega threshold:
Omega > q(0.99), q_0.99 = 101.745635181

event definition:
daily_precipitation_mm > q(0.95), q_0.95 = 9.5

timing rule:
contemporaneous; event_t is compared with high_Omega_t

P(event | high Omega):
0.513513513514

baseline P(event):
0.0496688741722

ratio:
10.3387387387

n_total:
3653

n_valid:
3624

n_high:
37

n_event_total:
180

n_event_high:
19

result class:
positive concentration

---

## 5. Result classification

result_class: positive concentration

The event rate under high-Omega rows is greater than the baseline event rate under the fixed specification.

This classification does not license changing the method, broadening the claim, or treating the result as a forecast, warning, policy, or risk result.

---

## 6. Claim boundary

This test evaluates structural concentration only.

It asks whether an independently defined high-precipitation event occurs more frequently under high-Omega conditions than at baseline.

It does not claim prediction, causality, weather forecasting, climate interpretation, public warning, intervention, policy relevance, risk scoring, or full validation of the theory.

The result applies only to this fixed London daily precipitation operationalization.

---

## 7. Limitations

This is one weather-location test.

The source is a public archive API, so future reruns may reflect any official data revisions returned by Open-Meteo.

The observable uses daily precipitation only.

The event uses a fixed raw daily precipitation q(0.95) rule only.

The result does not evaluate flooding, impacts, climate change, forecast skill, warnings, policy, infrastructure risk, or public safety.

The contemporaneous timing rule is a fixed association rule, not a forecast or warning rule.

---

## 8. Reproducibility notes

Execution script:
scripts/london_weather_activity_test.py

Runtime:
Python standard library only.

Command used:

```powershell
C:\Users\garte\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe scripts\london_weather_activity_test.py
```

The first attempt with `python` did not execute because `python` was not on PATH.

The first bundled-Python attempt inside the sandbox was blocked from network access before data retrieval.

The completed run used the same fixed script and required network permission to fetch the Open-Meteo Archive API data.

End of document.
