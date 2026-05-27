# GitHub Activity External pandas Ω Test Result v1.0

Status: Internal result  
Purpose: First external-repository GitHub activity Ω result  
Scope: pandas-dev/pandas daily commit activity  
Publication status: Internal only / not a public cross-domain claim

Related files:
- maintenance/GITHUB_ACTIVITY_OMEGA_TEST_DESIGN_V1.md
- maintenance/GITHUB_ACTIVITY_EXTERNAL_PANDAS_FIXED_SCOPE_V1.md
- scripts/github_activity_external_pandas_test.py

---

## 1. Status

This is the first external-repository result produced from the fixed GitHub activity Ω test.

The result was generated after the design note, external fixed-scope memo, and execution script were committed.

No definitions were changed after seeing the result.

---

## 2. Fixed scope

Fixed scope source:

```text
maintenance/GITHUB_ACTIVITY_EXTERNAL_PANDAS_FIXED_SCOPE_V1.md
```

Summary:

- repository analyzed: pandas-dev/pandas
- sample period: 2009-07-31 through 2026-05-26 UTC, inclusive
- time zone: UTC
- timestamp rule used: commit author date (%aI)
- observable variable: activity_count = number of commits per UTC day
- aggregation rule: one UTC calendar day, including zero-activity days between the first available commit date and the fixed cutoff date
- I definition: rolling standard deviation(activity_count, window = 30 days)
- G definition: absolute first difference(activity_count)
- Ω definition: Ω = I × G
- high-Ω threshold: Ω > q(0.99)
- event definition: event = activity_count > q(0.95)
- event timing rule: contemporaneous; event_t is compared with high_Ω_t

---

## 3. Exact script output

```text
domain: GitHub repository activity
repository analyzed: pandas-dev/pandas
sample period: 2009-07-31 through 2026-05-26 UTC, inclusive
time zone: UTC
timestamp rule used: commit author date (%aI)
observable variable: activity_count = number of commits per UTC day
aggregation rule: one UTC calendar day, including zero-activity days in the fixed sample period
I definition: rolling standard deviation(activity_count, window = 30 days)
G definition: absolute first difference(activity_count)
Ω definition: Ω = I × G
high-Ω threshold: Ω > q(0.99), q_0.99 = 152.39969333
event definition: activity_count > q(0.95), q_0.95 = 18
event timing rule: contemporaneous: event_t is compared with high_Ω_t
P(event | high Ω): 0.516129032258
baseline P(event): 0.0454619787408
ratio: 11.3529821304
n_total: 6144
n_valid: 6115
n_high: 62
n_event_total: 278
n_event_high: 32
result_class: positive concentration
```

---

## 4. Result classification

```text
positive concentration
```

---

## 5. Internal interpretation boundary

This test evaluates structural concentration only.

It asks whether independently defined GitHub commit-activity burst events occur more frequently under high-Ω conditions than at baseline.

It does not claim prediction, causality, optimization, intervention, software quality assessment, maintainer behavior assessment, or full validation of the theory.

The tested repository is an external open-source repository, but the result remains a single-repository GitHub activity test unless reproduced across additional repositories under fixed specifications.

---

## 6. Notes

The result is positive concentration.

Do not modify the design, script, threshold, repository, observable, rolling window, event definition, or sample period to improve the result.

End of document.
