# GitHub Activity Ω Test Design v1.0

Status: Internal / pre-evaluation design  
Purpose: Candidate empirical test design  
Scope: GitHub repository activity as an information-system domain  
Publication status: Not a result report

---

## 1. Purpose

This document defines a pre-evaluation design for testing whether independently defined GitHub activity events concentrate in high-Ω states.

This is not a result document.

This document fixes the candidate domain, observable variables, Ω construction, event definition, threshold rule, and reporting requirements before any empirical result is computed.

The purpose is to prevent post-hoc tuning.

---

## 2. Minimal empirical question

The empirical question is:

```text
Do independently defined GitHub activity events concentrate in high-Ω states compared with the baseline event rate?
```

The standard comparison is:

```text
P(event | high Ω)
vs
baseline P(event)
```

Optional derived output:

```text
ratio = P(event | high Ω) / baseline P(event)
```

No prediction, causality, optimization, intervention, or full validation of The Pleasure Order is claimed.

---

## 3. Domain

Domain:

```text
GitHub repository activity
```

Domain type:

```text
information system / activity-count time series
```

Rationale:

GitHub repositories generate ordered public activity records such as commits, issues, pull requests, comments, releases, and stars.

These can be aggregated into time-indexed activity counts.

The domain is suitable as a candidate Ω test because it has:

```text
time-indexed observations
publicly reproducible data
count-based observable variables
clear burst-style event definitions
low interpretation burden
```

---

## 4. Candidate observable variable

Preferred observable:

```text
daily activity count
```

Recommended initial definition:

```text
activity_count = daily number of commits
```

Alternative observables, if commits are unavailable or unsuitable:

```text
daily issue count
daily pull request count
daily combined activity count
daily commit + issue + pull request count
```

The first internal test should use one observable only.

The observable must be selected before evaluation.

---

## 5. Ω definition

Default structure:

```text
I = rolling standard deviation(activity_count, window = 30 days)
G = absolute first difference(activity_count)
Ω = I × G
```

Equivalent notation:

```text
I_t = rolling_std(activity_count, 30)
G_t = |activity_count_t - activity_count_{t-1}|
Ω_t = I_t × G_t
```

The 30-day window is chosen before evaluation.

Do not tune the rolling window after seeing the result.

If a 20-day window is tested for compatibility with the generic minimal CSV template, it must be labeled as a sensitivity check, not the default result.

---

## 6. High-Ω condition

Default high-Ω condition:

```text
high Ω = Ω > q(0.99)
```

Rules:

```text
q is computed within the dataset
q = 0.99 is fixed before evaluation
the threshold must not be changed after seeing the result
```

Other thresholds may be used only as exploratory or sensitivity checks.

They must not replace the default q = 0.99 result.

---

## 7. Event definition

Preferred event:

```text
event = activity_count > q(0.95)
```

Interpretation:

```text
An activity burst occurs when daily activity count exceeds the 95th percentile of daily activity counts within the dataset.
```

The event definition is independent from Ω because it is based only on the raw activity count, not on Ω, I, G, or the high-Ω threshold.

Unacceptable event definitions:

```text
event = Ω is high
event = I × G exceeds a threshold
event = manually selected activity spikes after observing Ω
event = event threshold changed after seeing high-Ω rows
```

---

## 8. Event timing rule

Default timing rule:

```text
contemporaneous
```

That is:

```text
event_t is compared with high_Ω_t
```

This test is not a forecast.

Forward-window versions may be explored later, but they must be labeled separately.

---

## 9. Data source requirement

The dataset must be reproducible from a public GitHub repository.

Minimum required fields after preprocessing:

```text
date
activity_count
event
I
G
Ω
high_Ω
```

The source repository, API/query method, date range, and aggregation rule must be recorded.

The sample period must be fixed before evaluation.

---

## 10. Minimum reporting output

A completed internal result must report:

```text
domain
data source
repository analyzed
sample period
observable variable
I definition
G definition
Ω definition
high-Ω threshold
event definition
event timing rule
P(event | high Ω)
baseline P(event)
ratio
n_total
n_high
n_event_total
n_event_high
```

Sparse-event cases must explicitly report:

```text
n_high
n_event_high
```

---

## 11. Result classification

Classify the result as one of:

```text
positive concentration
null
negative / inverse
sparse
```

Positive concentration:

```text
P(event | high Ω) > baseline P(event)
```

Null:

```text
P(event | high Ω) ≈ baseline P(event)
```

Negative / inverse:

```text
P(event | high Ω) < baseline P(event)
```

Sparse:

```text
n_high or n_event_high is too small for stable interpretation
```

Do not change Ω, event definitions, thresholds, windows, repository selection, or sample period after seeing the result.

---

## 12. Exclusion / delay rules

Delay or reject the test if:

```text
the repository has too few observations
activity is too sparse
n_high is too small
event_count is too small
the data cannot be reproduced
the observable requires subjective interpretation
the event definition overlaps with Ω
```

Private exploratory checks may be kept separate, but they must not be presented as fixed minimal results.

---

## 13. Claim boundary

Use the following statement when summarizing any result:

```text
This test evaluates structural concentration only.

It asks whether independently defined GitHub activity events occur more frequently under high-Ω conditions than at baseline.

It does not claim prediction, causality, optimization, intervention, or full validation of the theory.
```

---

## 14. Internal status

This design is suitable for internal empirical expansion because it tests an information-system topology while preserving the minimal Ω structure.

It should proceed only after the dataset, repository, sample period, observable, and event definition are fixed.

End of document.
