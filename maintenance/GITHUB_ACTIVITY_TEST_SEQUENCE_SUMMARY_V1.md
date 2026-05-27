# GitHub Activity Ω Test Sequence Summary v1.0

Status: Internal sequence summary  
Purpose: Summary of fixed GitHub activity Ω tests completed so far  
Scope: Internal pipeline test plus two external open-source repository tests  
Publication status: Internal only / not a public cross-domain claim

Related files:
- maintenance/GITHUB_ACTIVITY_OMEGA_TEST_DESIGN_V1.md
- maintenance/GITHUB_ACTIVITY_OMEGA_TEST_FIXED_SCOPE_V1.md
- maintenance/GITHUB_ACTIVITY_OMEGA_TEST_RESULT_V1.md
- maintenance/GITHUB_ACTIVITY_EXTERNAL_PANDAS_FIXED_SCOPE_V1.md
- maintenance/GITHUB_ACTIVITY_EXTERNAL_PANDAS_RESULT_V1.md
- maintenance/GITHUB_ACTIVITY_EXTERNAL_NUMPY_FIXED_SCOPE_V1.md
- maintenance/GITHUB_ACTIVITY_EXTERNAL_NUMPY_RESULT_V1.md
- scripts/github_activity_omega_test.py
- scripts/github_activity_external_pandas_test.py
- scripts/github_activity_external_numpy_test.py

---

## 1. Purpose

This document summarizes the GitHub activity Ω test sequence completed so far.

The sequence consists of:

1. an internal pipeline test on onsenojisan/omega-repro
2. a first external-repository test on pandas-dev/pandas
3. a second external-repository test on numpy/numpy

This is a sequence summary only.

It does not introduce new definitions.

It does not modify any result.

It does not create a public cross-domain claim.

---

## 2. Fixed design family

All tests use the same design family:

repository activity is aggregated into daily commit counts.

The core structure is:

I = rolling standard deviation(activity_count, window = 30 days)  
G = absolute first difference(activity_count)  
Ω = I × G

High-Ω condition:

high Ω = Ω > q(0.99)

Event definition:

event = activity_count > q(0.95)

Timing rule:

contemporaneous

Evaluation:

P(event | high Ω)  
vs  
baseline P(event)

---

## 3. Sequence results

| sequence | repository | role | result_class | P(event \| high Ω) | baseline P(event) | ratio |
|---|---|---|---|---:|---:|---:|
| 1 | onsenojisan/omega-repro | internal pipeline test | sparse | recorded in result memo | recorded in result memo | recorded in result memo |
| 2 | pandas-dev/pandas | first external repository test | positive concentration | 0.516129032258 | recorded in result memo | 11.3529821304 |
| 3 | numpy/numpy | second external repository test | positive concentration | 0.505617977528 | 0.0468697313701 | 10.7877293671 |

Note:
The exact stdout blocks remain in the individual result memos.

This table is a summary and does not replace the source result files.

---

## 4. Internal interpretation

The internal pipeline test on onsenojisan/omega-repro produced a sparse result.

The two external high-activity repositories tested so far produced positive concentration results under the fixed specification.

This suggests that the GitHub activity Ω design is operationally viable for sufficiently active repositories.

However, this remains a limited GitHub activity sequence.

It should not be treated as a public cross-domain claim or as validation of the full theory.

---

## 5. Claim boundary

This sequence evaluates structural concentration only.

It asks whether independently defined GitHub commit-activity burst events occur more frequently under high-Ω conditions than at baseline.

It does not claim prediction, causality, optimization, intervention, software quality assessment, maintainer behavior assessment, or full validation of the theory.

The external tests are still single-repository tests within the GitHub activity domain.

Additional repositories would be needed before describing this as a stable GitHub activity-domain pattern.

---

## 6. Method stability note

The sparse internal result was retained.

The positive pandas result did not trigger method changes.

The positive NumPy result did not trigger method changes.

No repository, sample period, observable, event threshold, Ω window, high-Ω threshold, or timing rule was changed after seeing results.

This preserves the fixed-sequence interpretation.

---

## 7. Next internal options

Possible next steps:

1. stop the GitHub activity sequence here and treat it as a completed internal extension
2. add one more external repository under the same fixed specification
3. create a small internal comparison table across GitHub activity tests
4. later decide whether this belongs in a broader cross-domain summary

Do not publicize as a strong standalone claim until additional repositories or an external reproduction path is prepared.

End of document.
