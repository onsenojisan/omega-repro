# Wikipedia Activity Ω Test Sequence Summary v2.0

Status: Internal sequence summary
Purpose: Summary of the fixed Wikipedia activity Ω tests completed so far
Scope: English Wikipedia pageviews for Python (programming language) and Artificial intelligence
Publication status: Internal only / not a public cross-domain claim

Related files:
- maintenance/NEXT_EMPIRICAL_DOMAIN_SELECTION_V1.md
- maintenance/WIKIPEDIA_ACTIVITY_PYTHON_FIXED_SCOPE_V1.md
- maintenance/WIKIPEDIA_ACTIVITY_PYTHON_RESULT_V1.md
- maintenance/WIKIPEDIA_ACTIVITY_AI_FIXED_SCOPE_V1.md
- maintenance/WIKIPEDIA_ACTIVITY_AI_RESULT_V1.md
- maintenance/WIKIPEDIA_ACTIVITY_TEST_SEQUENCE_SUMMARY_V1.md
- scripts/wikipedia_activity_python_test.py
- scripts/wikipedia_activity_ai_test.py
- maintenance/EMPIRICAL_MAINTENANCE_INDEX_V1.md

---

## 1. Purpose

This document summarizes the Wikipedia activity Ω test sequence completed so far.

The sequence currently consists of:

1. English Wikipedia pageviews for Python (programming language)
2. English Wikipedia pageviews for Artificial intelligence

This is a V2 sequence summary.

It does not introduce new definitions.

It does not modify any result.

It does not create a public cross-domain claim.

---

## 2. Fixed design family

Both Wikipedia activity tests use the same design family:

daily pageviews are treated as the activity count.

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

| sequence | project | page | role | result_class | P_event_given_high_Omega | baseline_P_event | ratio | missing_days |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | en.wikipedia.org | Python (programming language) | first Wikipedia activity test | positive concentration | 0.25 | 0.0500758725341 | 4.99242424242 | 0 |
| 2 | en.wikipedia.org | Artificial intelligence | second Wikipedia activity test | positive concentration | recorded in result memo | recorded in result memo | recorded in result memo | recorded in result memo |

Note:
The exact stdout blocks remain in the individual result memos:

- maintenance/WIKIPEDIA_ACTIVITY_PYTHON_RESULT_V1.md
- maintenance/WIKIPEDIA_ACTIVITY_AI_RESULT_V1.md

This table is a summary and does not replace the source result files.

---

## 4. Internal interpretation

Both completed Wikipedia activity tests produced positive concentration results under fixed specifications.

This suggests that the Wikipedia activity Ω design is operationally viable for the two selected pages.

However, this remains a limited two-page sequence.

It should not be treated as a public Wikipedia-domain claim.

---

## 5. Relationship to the GitHub activity sequence

This Wikipedia activity sequence follows the completed GitHub activity sequence, but it is not part of that sequence.

The completed GitHub activity sequence remains closed.

The Wikipedia activity tests form a separate information-system activity sequence.

Current relationship:

GitHub activity:
- internal pipeline result: sparse
- external pandas result: positive concentration
- external NumPy result: positive concentration
- sequence closed

Wikipedia activity:
- Python (programming language): positive concentration
- Artificial intelligence: positive concentration
- sequence open unless closed by a future completion note

---

## 6. Claim boundary

This sequence evaluates structural concentration only.

It asks whether independently defined Wikipedia pageview burst events occur more frequently under high-Ω conditions than at baseline.

It does not claim prediction, causality, public attention forecasting, social behavior diagnosis, information quality assessment, article quality assessment, or full validation of the theory.

The current result sequence is based on two Wikipedia articles.

Additional pages would be needed before describing this as a stable Wikipedia activity-domain pattern.

---

## 7. Method stability note

The selected pages were not changed after seeing results.

The sample period was not changed after seeing results.

The observable was not changed after seeing results.

The event definition was not changed after seeing results.

The Ω window and thresholds were not changed after seeing results.

This preserves the fixed-sequence interpretation.

---

## 8. Difference from V1 summary

The V1 summary covered only:

Python (programming language)

This V2 summary adds:

Artificial intelligence

The V1 summary remains preserved as the historical one-page summary.

This V2 summary should be used for reviewing the current two-page Wikipedia activity sequence.

---

## 9. Next internal options

Possible next steps:

1. stop here and keep the two-page Wikipedia activity sequence as an internal extension
2. add one more Wikipedia page under a separate fixed-scope memo
3. create a Wikipedia activity completion note if the sequence should be closed
4. later update the empirical maintenance index after the Wikipedia sequence structure is stable

Do not publicize as a broad Wikipedia-domain claim at this stage.

End of document.
