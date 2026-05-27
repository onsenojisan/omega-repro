# GitHub Activity Ω Test Fixed Scope v1.0

Status: Internal / pre-data fixed scope  
Purpose: Fixed execution scope for first GitHub activity Ω test  
Scope: First internal GitHub repository activity test  
Publication status: Not a result report

Related design note:

```text
maintenance/GITHUB_ACTIVITY_OMEGA_TEST_DESIGN_V1.md
```

---

## 1. Purpose

This document fixes the execution scope for the first internal GitHub activity Ω structural concentration test.

This is not a result document.

This document is created before data collection, Ω computation, event evaluation, or result interpretation.

The purpose is to prevent post-hoc repository selection, sample-period selection, observable selection, or event-definition tuning.

---

## 2. Test status

Current status:

```text
pre-data
pre-computation
pre-result
internal only
```

This document fixes the initial test scope only.

No empirical claim is made here.

---

## 3. Target repository

Repository analyzed:

```text
onsenojisan/omega-repro
```

Repository type:

```text
project-maintenance / reproducibility repository
```

Reason for selection:

```text
The repository is public, accessible, directly related to Ω reproducibility work, and suitable for an internal first-run test of the GitHub activity design.
```

Limitation:

```text
Because this is the author's own repository, the result should be treated as an internal pipeline test, not as strong external evidence.
```

Public-facing use:

```text
Do not use this result as a public cross-domain claim unless later confirmed with external repositories under the same fixed specification.
```

---

## 4. Sample period

Default sample period:

```text
from first available commit date
through 2026-05-26 UTC, inclusive
```

Cutoff rationale:

```text
The cutoff date is fixed before data collection to avoid including a partial current day or adjusting the period after seeing results.
```

Time zone rule:

```text
Use UTC dates for daily aggregation.
```

Do not change the sample period after inspecting the data or results.

If the repository has too few observations, report the test as delayed or sparse.

Do not replace the repository after seeing unfavorable results.

---

## 5. Observable variable

Primary observable:

```text
daily commit count
```

Definition:

```text
activity_count = number of commits per UTC day
```

Commit timestamp rule:

```text
Use commit author date if available.
If author date is not available or is unreliable in the extraction method, use commit committer date and report that choice.
```

One observable only:

```text
The first internal test uses daily commit count only.
```

Do not combine commits, issues, pull requests, stars, releases, or comments in the default test.

Combined activity may be explored later, but it must be labeled separately as exploratory.

---

## 6. Daily aggregation rule

Aggregation unit:

```text
one UTC calendar day
```

For each day in the sample period:

```text
activity_count = number of commits assigned to that UTC date
```

Zero-activity days:

```text
Include zero-activity days between the first available commit date and the fixed cutoff date.
```

Reason:

```text
Excluding zero-activity days would distort the daily activity time series and inflate event rates.
```

---

## 7. Ω definition

Default Ω definition:

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

Rolling window:

```text
30 days
```

Window status:

```text
fixed before evaluation
```

Do not tune the rolling window after seeing the result.

---

## 8. High-Ω condition

Default high-Ω condition:

```text
high Ω = Ω > q(0.99)
```

Quantile rule:

```text
q is computed within the valid analysis rows after Ω is computed.
```

Rows with insufficient rolling-window history should be excluded from the valid analysis rows.

The high-Ω threshold must not be changed after seeing the result.

---

## 9. Event definition

Default event:

```text
event = activity_count > q(0.95)
```

Interpretation:

```text
A GitHub activity burst occurs when the daily commit count exceeds the 95th percentile of daily commit counts in the valid analysis period.
```

Event independence:

```text
The event is defined from raw daily commit count only.
It is not defined from Ω, I, G, high_Ω, or the Ω threshold.
```

Do not modify the event threshold after seeing results.

---

## 10. Event timing rule

Default timing:

```text
contemporaneous
```

Comparison:

```text
event_t is compared with high_Ω_t
```

This is not a forecast.

No lead or lag window is part of the default test.

Forward-window versions may be explored later, but must be reported separately.

---

## 11. Minimum output required after execution

When the test is eventually executed, the result must report:

```text
domain
repository analyzed
sample period
time zone
observable variable
aggregation rule
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
n_valid
n_high
n_event_total
n_event_high
```

Sparse cases must explicitly report:

```text
n_high
n_event_high
```

---

## 12. Exclusion / sparse rules

Delay or classify as sparse if:

```text
n_valid is too small
n_high is too small
n_event_high is too small
the repository has long inactivity periods that make interpretation unstable
the commit history cannot be reproduced consistently
the extracted timestamps are ambiguous
```

Do not change the repository, period, observable, event threshold, Ω window, or timing rule to avoid a sparse or null result.

---

## 13. Claim boundary

Use this boundary if the result is later summarized:

```text
This test evaluates structural concentration only.

It asks whether independently defined GitHub commit-activity burst events occur more frequently under high-Ω conditions than at baseline.

It does not claim prediction, causality, optimization, intervention, or full validation of the theory.

Because the first repository is the author's own repository, the result should be treated as an internal pipeline test unless reproduced on external repositories under the same fixed specification.
```

---

## 14. Next step after this memo

After this fixed-scope memo is committed, the next step may be to create an execution script or notebook that:

```text
extracts commit history
aggregates daily commit counts
includes zero-activity days
computes I, G, Ω
computes high_Ω using q = 0.99
computes event using q = 0.95
outputs the minimum result table
```

That future execution must not change the fixed scope defined here.

End of document.
