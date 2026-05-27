# GitHub Activity External NumPy Ω Test Result v1.0

Status: Internal result  
Purpose: Second external-repository GitHub activity Ω result  
Scope: numpy/numpy daily commit activity  
Publication status: Internal only / not a public cross-domain claim

Related files:
- maintenance/GITHUB_ACTIVITY_OMEGA_TEST_DESIGN_V1.md
- maintenance/GITHUB_ACTIVITY_EXTERNAL_NUMPY_FIXED_SCOPE_V1.md
- scripts/github_activity_external_numpy_test.py
- maintenance/GITHUB_ACTIVITY_EXTERNAL_PANDAS_RESULT_V1.md

---

## 1. Status

This is the second external-repository result produced from the fixed GitHub activity Ω test sequence.

The result was generated after the design note, NumPy fixed-scope memo, and NumPy execution script were committed.

No definitions were changed after seeing the result.

---

## 2. Fixed scope

Fixed scope source:

```text
maintenance/GITHUB_ACTIVITY_EXTERNAL_NUMPY_FIXED_SCOPE_V1.md
```

Summary:

- repository analyzed: numpy/numpy
- sample period: 2001-12-18 through 2026-05-26 UTC, inclusive
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
repository analyzed: numpy/numpy
sample period: 2001-12-18 through 2026-05-26 UTC, inclusive
time zone: UTC
timestamp rule used: commit author date (%aI)
observable variable: activity_count = number of commits per UTC day
aggregation rule: one UTC calendar day, including zero-activity days in the fixed sample period
I definition: rolling standard deviation(activity_count, window = 30 days)
G definition: absolute first difference(activity_count)
Ω definition: Ω = I × G
high-Ω threshold: Ω > q(0.99), q_0.99 = 139.359972741
event definition: activity_count > q(0.95), q_0.95 = 15
event timing rule: contemporaneous: event_t is compared with high_Ω_t
P(event | high Ω): 0.505617977528
baseline P(event): 0.0468697313701
ratio: 10.7877293671
n_total: 8926
n_valid: 8897
n_high: 89
n_event_total: 417
n_event_high: 45
result_class: positive concentration
```

---

## 4. Result classification

```text
positive concentration
```

---

## 5. Relationship to previous GitHub activity tests

- onsenojisan/omega-repro: internal pipeline test, result_class sparse
- pandas-dev/pandas: first external repository test, result_class positive concentration
- numpy/numpy: second external repository test, result_class positive concentration

Do not use the NumPy result to modify the method.

---

## 6. Internal interpretation boundary

This test evaluates structural concentration only.

It asks whether independently defined GitHub commit-activity burst events occur more frequently under high-Ω conditions than at baseline.

It does not claim prediction, causality, optimization, intervention, software quality assessment, maintainer behavior assessment, or full validation of the theory.

The tested repository is an external open-source repository, but the result remains a single-repository GitHub activity test unless reproduced across additional repositories under fixed specifications.

---

## 7. Notes

The result is positive concentration.

Do not modify the design, script, threshold, repository, observable, rolling window, event definition, or sample period to improve the result.

End of document.
