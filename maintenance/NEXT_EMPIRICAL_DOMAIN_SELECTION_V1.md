# Next Empirical Domain Selection v1.0

Status: Internal domain-selection memo  
Purpose: Select the next empirical domain after the completed GitHub activity sequence  
Scope: Future Ω empirical work  
Publication status: Internal only / not a result report

Related files:
- maintenance/EMPIRICAL_MAINTENANCE_INDEX_V1.md
- maintenance/INTERNAL_OMEGA_EMPIRICAL_DESIGN_MAP_V1.md
- maintenance/GITHUB_ACTIVITY_TEST_SEQUENCE_SUMMARY_V1.md
- maintenance/GITHUB_ACTIVITY_SEQUENCE_COMPLETION_NOTE_V1.md

---

## 1. Purpose

This document selects the next empirical domain to consider after the completed GitHub activity Ω sequence.

This is not a fixed-scope memo.

This is not a result document.

This document does not start a new empirical test.

Its purpose is to choose the next domain direction before any data collection, Ω computation, or result evaluation.

---

## 2. Current empirical status

The GitHub activity sequence is closed for current internal comparison.

Completed GitHub activity sequence:

1. internal pipeline test on onsenojisan/omega-repro
2. external repository test on pandas-dev/pandas
3. external repository test on numpy/numpy
4. sequence summary
5. completion note
6. empirical maintenance index update

Current instruction from the maintenance index:

Do not expand GitHub activity automatically.

Additional GitHub repositories should be treated as a separate extension or new sequence version.

Therefore, the next work should not be another GitHub repository by default.

---

## 3. Candidate domains considered

Candidate domains from the internal empirical design map include:

- ecology
- Wikipedia activity
- web traffic
- search activity
- additional weather locations
- additional traffic regions
- additional finance assets
- additional power-market regions

The goal here is not to choose the most theoretically interesting domain.

The goal is to choose the next domain that is:

- publicly reproducible
- structurally close enough to the minimal Ω design
- different enough from the completed GitHub activity sequence
- low in interpretation burden
- suitable for pre-definition before evaluation
- unlikely to require new theory

---

## 4. Recommended next domain

Recommended next domain:

Wikipedia activity

Recommended initial observable family:

daily Wikipedia page activity or edit activity counts

Preferred initial form:

daily activity count time series

Candidate observable options:

- daily pageviews for a fixed Wikipedia page
- daily edit count for a fixed Wikipedia page
- daily revision count for a fixed Wikipedia page

Preferred first candidate:

daily pageviews for a fixed Wikipedia page, if public API access and reproducible extraction are straightforward.

Fallback candidate:

daily revision or edit counts for a fixed Wikipedia page, if pageview access is less stable.

---

## 5. Reason for selecting Wikipedia activity

Wikipedia activity is a better next step than adding another GitHub repository because it moves from software-development activity to public knowledge-system activity.

It remains an information-system domain, but it is not simply another open-source repository.

It has several advantages:

- public data sources are likely available
- activity can be represented as daily counts
- burst events can be defined independently from Ω
- zero-activity or low-activity days can be retained
- the minimal comparison can remain unchanged
- the interpretation burden is lower than ecology, public health, or civilizational data
- the domain can be tested without expanding the theory

This makes it a suitable next candidate after GitHub activity.

---

## 6. Provisional Ω mapping

This is not yet a fixed scope.

The provisional structure is:

I = rolling standard deviation(activity_count, window = 30 days)  
G = absolute first difference(activity_count)  
Ω = I × G

High-Ω condition:

high Ω = Ω > q(0.99)

Candidate event definition:

event = activity_count > q(0.95)

Timing rule:

contemporaneous

Evaluation:

P(event | high Ω)  
vs  
baseline P(event)

These definitions should not be treated as final until a separate fixed-scope memo is created.

---

## 7. Candidate page-selection rule

A later fixed-scope memo should choose one page or one clearly defined set of pages before data collection.

The page should not be selected after inspecting Ω results.

Preferred page-selection criteria:

- public interest
- long history
- sufficient daily activity
- stable page identity
- reproducible API access
- low interpretive burden

The page should not be selected because it is expected to produce a favorable Ω result.

---

## 8. Why not choose ecology next

Ecology remains promising, but it is heavier than Wikipedia activity.

Reasons to delay ecology:

- data-source selection may require more judgment
- observable definitions can vary by dataset
- biological interpretation may add burden
- event definitions such as bloom, crash, or extreme shift require more care
- public reproducibility may be dataset-dependent

Ecology should remain a later candidate after the information-system extension is stabilized.

---

## 9. Why not choose more GitHub repositories next

The current GitHub activity sequence is already closed.

Adding more GitHub repositories immediately would risk turning a completed sequence into an uncontrolled expansion.

If another GitHub repository is added later, it should be treated as a separate extension or new sequence version.

It should not be added to the already completed sequence.

---

## 10. Next required step

The next step, if this selection is accepted, is to create a fixed-scope memo for the first Wikipedia activity Ω test.

That future fixed-scope memo should specify:

- exact data source
- exact page or page-selection rule
- sample period
- time zone
- observable variable
- aggregation rule
- I definition
- G definition
- Ω definition
- high-Ω threshold
- event definition
- event timing rule
- exclusion rules
- claim boundary

No data collection should occur before that fixed-scope memo is created and committed.

---

## 11. Claim boundary

This domain selection does not claim that Wikipedia activity follows Ω concentration.

It only selects Wikipedia activity as the next candidate domain for a future fixed-scope test.

Any future result must be reported as structural concentration only.

It must not claim prediction, causality, public attention forecasting, social behavior diagnosis, information quality assessment, or validation of the full theory.

---

## 12. Final selection

Selected next empirical domain:

Wikipedia activity

Selected status:

candidate for next fixed-scope memo

Do not execute yet.

End of document.
