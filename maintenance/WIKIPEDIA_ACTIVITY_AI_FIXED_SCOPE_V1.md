# Wikipedia Activity AI Fixed Scope v1.0

Status: Internal / pre-data fixed scope  
Purpose: Fixed execution scope for second Wikipedia activity Ω test  
Scope: English Wikipedia pageviews for Artificial intelligence  
Publication status: Not a result report

Related files:
- maintenance/NEXT_EMPIRICAL_DOMAIN_SELECTION_V1.md
- maintenance/WIKIPEDIA_ACTIVITY_PYTHON_FIXED_SCOPE_V1.md
- maintenance/WIKIPEDIA_ACTIVITY_PYTHON_RESULT_V1.md
- maintenance/WIKIPEDIA_ACTIVITY_TEST_SEQUENCE_SUMMARY_V1.md
- maintenance/EMPIRICAL_MAINTENANCE_INDEX_V1.md

---

## 1. Purpose

This document fixes the execution scope for the second Wikipedia activity Ω structural concentration test.

This is not a result document.

This document is created before API access, data collection, Ω computation, event evaluation, or result interpretation.

The purpose is to prevent post-hoc page selection, sample-period selection, observable selection, or event-definition tuning.

---

## 2. Test status

Current status:
pre-data
pre-computation
pre-result
internal only

This document fixes the second Wikipedia test scope only.

No empirical claim is made here.

---

## 3. Domain

Domain:
Wikipedia activity

Domain type:
public knowledge-system activity count time series

Reason for selection:
Wikipedia activity was selected as the next empirical domain after the completed GitHub activity sequence.

The first Wikipedia activity test used the English Wikipedia page Python (programming language) and produced a positive concentration result under the fixed specification.

Artificial intelligence is selected as the second Wikipedia activity page to test whether the same fixed design can be applied to a broader public-interest knowledge page.

This test is not a correction or optimization of the Python page result.

---

## 4. Target page

Project:
English Wikipedia

Page:
Artificial intelligence

Canonical page title for API use:
Artificial_intelligence

Reason for page selection:
The page is a stable, high-interest public knowledge page.

It differs from Python (programming language) by representing a broader scientific, technological, and public-interest topic rather than a specific programming-language page.

The page is selected before data collection.

Do not replace the page after inspecting the data or result.

---

## 5. Data source

Preferred data source:
Wikimedia Pageviews API

Data type:
daily pageviews for a fixed Wikipedia article

Project:
en.wikipedia.org

Access:
all-access

Agent:
user

Granularity:
daily

Article:
Artificial_intelligence

This fixed-scope memo does not access the API.

API access, if implemented later, must follow this scope exactly.

If the API is unavailable or the page history cannot be reproduced, report the test as delayed rather than changing the page or data source after inspection.

---

## 6. Sample period

Default sample period:
from first available daily pageview date in the selected data source
through 2026-05-26 UTC, inclusive

Cutoff rationale:
The cutoff date matches the cutoff used in the GitHub activity sequence and the first Wikipedia activity test.

Time zone rule:
Use the date convention returned by the Wikimedia daily pageviews data.

Do not change the sample period after inspecting the data or results.

If the data source starts later than expected, use the first available date from the fixed data source and report it clearly.

---

## 7. Observable variable

Primary observable:
daily pageview count

Definition:
activity_count = number of daily user pageviews for Artificial_intelligence

One observable only:
The second Wikipedia activity test uses daily pageview count only.

Do not combine pageviews, edits, revisions, links, article length, references, redirects, or other Wikipedia metrics in the default test.

Edit or revision activity may be explored later, but it must be labeled separately as exploratory or as a separate fixed-scope test.

---

## 8. Daily aggregation rule

Aggregation unit:
one calendar day as reported by the Wikimedia Pageviews API

For each day in the sample period:
activity_count = daily pageview count for the selected page

Missing days:
If missing days appear in the API response, handle them explicitly.

Preferred rule:
treat missing dates as missing data, not zero, unless the API documentation or response clearly indicates that the true count is zero.

Do not remove low-activity days merely to improve the result.

---

## 9. Ω definition

Default Ω definition:
I = rolling standard deviation(activity_count, window = 30 days)
G = absolute first difference(activity_count)
Ω = I × G

Equivalent notation:
I_t = rolling_std(activity_count, 30)
G_t = |activity_count_t - activity_count_t-1|
Ω_t = I_t × G_t

Rolling window:
30 days

Window status:
fixed before evaluation

Do not tune the rolling window after seeing the result.

---

## 10. High-Ω condition

Default high-Ω condition:
high Ω = Ω > q(0.99)

Quantile rule:
q is computed within the valid analysis rows after Ω is computed.

Rows with insufficient rolling-window history should be excluded from the valid analysis rows.

The high-Ω threshold must not be changed after seeing the result.

---

## 11. Event definition

Default event:
event = activity_count > q(0.95)

Interpretation:
A Wikipedia activity burst occurs when the daily pageview count exceeds the 95th percentile of daily pageview counts in the valid analysis period.

Event independence:
The event is defined from raw daily pageview count only.
It is not defined from Ω, I, G, high_Ω, or the Ω threshold.

Do not modify the event threshold after seeing results.

---

## 12. Event timing rule

Default timing:
contemporaneous

Comparison:
event_t is compared with high_Ω_t

This is not a forecast.

No lead or lag window is part of the default test.

Forward-window versions may be explored later, but must be reported separately.

---

## 13. Minimum output required after execution

When the test is eventually executed, the result must report:

domain
project
page
canonical page title
data source
sample period
time zone or API date convention
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
missing_days
result_class

Sparse cases must explicitly report:

n_high
n_event_high

---

## 14. Exclusion / sparse rules

Delay or classify as sparse if:

n_valid is too small
n_high is too small
n_event_high is too small
the API response cannot be reproduced
the selected page redirects ambiguously
the selected page identity is unstable
the daily pageview data contain unexplained gaps
the observable requires subjective interpretation

Do not change the page, period, observable, event threshold, Ω window, high-Ω threshold, or timing rule to avoid a sparse, null, or inverse result.

---

## 15. Relationship to prior tests

The completed GitHub activity sequence ended with:

internal pipeline test:
onsenojisan/omega-repro
result_class: sparse

external repository test 1:
pandas-dev/pandas
result_class: positive concentration

external repository test 2:
numpy/numpy
result_class: positive concentration

The first Wikipedia activity test used:

page:
Python (programming language)

result_class:
positive concentration

The Artificial intelligence test is the second Wikipedia activity test under the same design family.

It is not a tuning response to the Python page result.

---

## 16. Claim boundary

Use this boundary if the result is later summarized:

This test evaluates structural concentration only.

It asks whether independently defined Wikipedia pageview burst events occur more frequently under high-Ω conditions than at baseline.

It does not claim prediction, causality, public attention forecasting, social behavior diagnosis, information quality assessment, article quality assessment, or full validation of the theory.

The tested page is a single Wikipedia article. The result should not be presented as evidence for all Wikipedia activity unless additional pages are tested under fixed specifications.

---

## 17. Next step after this memo

After this fixed-scope memo is committed, the next step may be to create an execution script that:

fetches daily pageview data from the fixed data source
uses Artificial_intelligence as the fixed page title
uses the fixed sample period and cutoff
computes I, G, Ω
computes high_Ω using q = 0.99
computes event using q = 0.95
outputs the minimum result block

That future execution must not change the fixed scope defined here.

End of document.
