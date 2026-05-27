# GitHub Activity External Repository Fixed Scope v1.0

Status: Internal / pre-data fixed scope  
Purpose: Fixed execution scope for first external GitHub activity Ω test  
Scope: pandas-dev/pandas daily commit activity  
Publication status: Not a result report

Related files:
- maintenance/GITHUB_ACTIVITY_OMEGA_TEST_DESIGN_V1.md
- maintenance/GITHUB_ACTIVITY_OMEGA_TEST_FIXED_SCOPE_V1.md
- maintenance/GITHUB_ACTIVITY_OMEGA_TEST_RESULT_V1.md
- scripts/github_activity_omega_test.py

---

## 1. Purpose

This document fixes the execution scope for the first external-repository GitHub activity Ω structural concentration test.

This is not a result document.

This document is created before cloning, data collection, Ω computation, event evaluation, or result interpretation.

The purpose is to prevent post-hoc repository selection, sample-period selection, observable selection, or event-definition tuning.

---

## 2. Test status

Current status:

pre-data  
pre-computation  
pre-result  
internal only

This document fixes the external test scope only.

No empirical claim is made here.

---

## 3. Target repository

Repository analyzed:

pandas-dev/pandas

Repository type:

external open-source software repository

Reason for selection:

pandas-dev/pandas is a public, high-activity open-source repository with long-term commit history and sufficient expected daily activity for an external GitHub activity Ω test.

Role in the empirical sequence:

This is the first external-repository follow-up after the internal pipeline test on onsenojisan/omega-repro produced a sparse result.

Interpretation boundary:

The result, whether positive, null, inverse, or sparse, must be treated as a fixed external-repository test under the same design family. It must not be used to redefine the GitHub activity Ω method after the fact.

---

## 4. Sample period

Default sample period:

from first available commit date  
through 2026-05-26 UTC, inclusive

Cutoff rationale:

The cutoff date matches the fixed cutoff used in the first internal GitHub activity pipeline test and is fixed before data collection.

Time zone rule:

Use UTC dates for daily aggregation.

Do not change the sample period after inspecting the data or results.

If the repository history is too large or too difficult to process locally, report the execution as delayed rather than changing the repository or period after inspection.

---

## 5. Observable variable

Primary observable:

daily commit count

Definition:

activity_count = number of commits per UTC day

Commit timestamp rule:

Use commit author date if available.  
If the local git extraction method only reliably exposes committer date, use committer date and report that choice clearly.

One observable only:

The first external test uses daily commit count only.

Do not combine commits, issues, pull requests, stars, releases, comments, or contributors in the default test.

Combined activity may be explored later, but it must be labeled separately as exploratory.

---

## 6. Daily aggregation rule

Aggregation unit:

one UTC calendar day

For each day in the sample period:

activity_count = number of commits assigned to that UTC date

Zero-activity days:

Include zero-activity days between the first available commit date and the fixed cutoff date.

Reason:

Excluding zero-activity days would distort the daily activity time series and inflate event rates.

---

## 7. Ω definition

Default Ω definition:

I = rolling standard deviation(activity_count, window = 30 days)  
G = absolute first difference(activity_count)  
Ω = I × G

Equivalent notation:

I_t = rolling_std(activity_count, 30)  
G_t = |activity_count_t - activity_count_{t-1}|  
Ω_t = I_t × G_t

Rolling window:

30 days

Window status:

fixed before evaluation

Do not tune the rolling window after seeing the result.

---

## 8. High-Ω condition

Default high-Ω condition:

high Ω = Ω > q(0.99)

Quantile rule:

q is computed within the valid analysis rows after Ω is computed.

Rows with insufficient rolling-window history should be excluded from the valid analysis rows.

The high-Ω threshold must not be changed after seeing the result.

---

## 9. Event definition

Default event:

event = activity_count > q(0.95)

Interpretation:

A GitHub activity burst occurs when the daily commit count exceeds the 95th percentile of daily commit counts in the valid analysis period.

Event independence:

The event is defined from raw daily commit count only.  
It is not defined from Ω, I, G, high_Ω, or the Ω threshold.

Do not modify the event threshold after seeing results.

---

## 10. Event timing rule

Default timing:

contemporaneous

Comparison:

event_t is compared with high_Ω_t

This is not a forecast.

No lead or lag window is part of the default test.

Forward-window versions may be explored later, but must be reported separately.

---

## 11. Minimum output required after execution

When the test is eventually executed, the result must report:

domain  
repository analyzed  
sample period  
time zone  
timestamp rule used  
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
result_class

Sparse cases must explicitly report:

n_high  
n_event_high

---

## 12. Exclusion / sparse rules

Delay or classify as sparse if:

n_valid is too small  
n_high is too small  
n_event_high is too small  
the repository has activity structure that makes interpretation unstable  
the commit history cannot be reproduced consistently  
the extracted timestamps are ambiguous  
the repository cannot be cloned or inspected in the local environment

Do not change the repository, period, observable, event threshold, Ω window, or timing rule to avoid a sparse, null, or inverse result.

---

## 13. Relationship to the first internal pipeline test

The first internal GitHub activity test used:

repository:  
onsenojisan/omega-repro

result_class:  
sparse

That result is retained as an internal pipeline test.

This external repository test is not a correction of the sparse result.

It is a separate fixed-scope external test using the same design family.

---

## 14. Claim boundary

Use this boundary if the result is later summarized:

This test evaluates structural concentration only.

It asks whether independently defined GitHub commit-activity burst events occur more frequently under high-Ω conditions than at baseline.

It does not claim prediction, causality, optimization, intervention, software quality assessment, maintainer behavior assessment, or full validation of the theory.

The tested repository is an external open-source repository, but the result remains a single-domain GitHub activity test unless reproduced across additional repositories under fixed specifications.

---

## 15. Next step after this memo

After this fixed-scope memo is committed, the next step may be to create or adapt an execution script that:

clones or reads pandas-dev/pandas  
extracts commit history  
aggregates daily commit counts  
includes zero-activity days  
computes I, G, Ω  
computes high_Ω using q = 0.99  
computes event using q = 0.95  
outputs the minimum result block

That future execution must not change the fixed scope defined here.

End of document.
