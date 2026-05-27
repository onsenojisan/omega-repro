# Wikipedia Activity AI Ω Test Result v1.0

Status: Internal result
Purpose: Second Wikipedia activity Ω result
Scope: English Wikipedia pageviews for Artificial intelligence
Publication status: Internal only / not a public cross-domain claim

Related files:
- maintenance/WIKIPEDIA_ACTIVITY_AI_FIXED_SCOPE_V1.md
- scripts/wikipedia_activity_ai_test.py
- maintenance/WIKIPEDIA_ACTIVITY_PYTHON_RESULT_V1.md
- maintenance/WIKIPEDIA_ACTIVITY_TEST_SEQUENCE_SUMMARY_V1.md
- maintenance/EMPIRICAL_MAINTENANCE_INDEX_V1.md

---

## 1. Status

This is the second Wikipedia activity result produced from the fixed Wikipedia activity Ω test sequence.

The result was generated after the AI fixed-scope memo and AI execution script were committed.

No definitions were changed after seeing the result.

---

## 2. Fixed scope

Use the fixed scope exactly as defined in:

maintenance/WIKIPEDIA_ACTIVITY_AI_FIXED_SCOPE_V1.md

Summary:

- domain: Wikipedia activity
- project: en.wikipedia.org
- page: Artificial intelligence
- canonical page title: Artificial_intelligence
- data source: Wikimedia Pageviews API
- sample period: from first available daily pageview date in the selected data source through 2026-05-26 UTC, inclusive
- time zone or API date convention: Wikimedia daily pageviews date convention
- observable variable: activity_count = daily pageview count
- aggregation rule: one calendar day as reported by the Wikimedia Pageviews API
- I definition: rolling standard deviation(activity_count, window = 30 days)
- G definition: absolute first difference(activity_count)
- Ω definition: Ω = I × G
- high-Ω threshold: Ω > q(0.99)
- event definition: event = activity_count > q(0.95)
- event timing rule: contemporaneous

---

## 3. Exact script output

```text
domain: Wikipedia activity
project: en.wikipedia.org
page: Artificial intelligence
canonical page title: Artificial_intelligence
data source: Wikimedia Pageviews API
sample period: 2015-07-01 through 2026-05-26 UTC, inclusive
time zone or API date convention: Wikimedia daily pageviews date convention
observable variable: activity_count = daily pageview count
aggregation rule: one calendar day as reported by the Wikimedia Pageviews API
I definition: rolling standard deviation(activity_count, window = 30 days)
G definition: absolute first difference(activity_count)
兌 definition: 兌 = I 亊 G
high-兌 threshold: 兌 > q(0.99), q_0.99 = 13777877.6356
event definition: activity_count > q(0.95), q_0.95 = 19418.95
event timing rule: contemporaneous: event_t is compared with high_兌_t
P(event | high 兌): 0.4
baseline P(event): 0.0500758725341
ratio: 7.98787878788
n_total: 3983
n_valid: 3954
n_high: 40
n_event_total: 198
n_event_high: 16
missing_days: 0
result_class: positive concentration
```

---

## 4. Result classification

result_class: positive concentration

---

## 5. Relationship to prior Wikipedia activity test

The first Wikipedia activity test used:

page:
Python (programming language)

result_class:
positive concentration

This Artificial intelligence result is the second fixed-scope Wikipedia activity test.

It is not a tuning response to the Python page result.

Do not use the result to modify the Wikipedia activity method.

---

## 6. Relationship to GitHub activity sequence

This Wikipedia activity sequence follows the completed GitHub activity sequence, but it is separate from it.

The completed GitHub activity sequence was:

- onsenojisan/omega-repro: internal pipeline test, result_class sparse
- pandas-dev/pandas: external repository test, result_class positive concentration
- numpy/numpy: external repository test, result_class positive concentration

The Wikipedia tests form a separate information-system activity sequence.

---

## 7. Internal interpretation boundary

This test evaluates structural concentration only.

It asks whether independently defined Wikipedia pageview burst events occur more frequently under high-Ω conditions than at baseline.

It does not claim prediction, causality, public attention forecasting, social behavior diagnosis, information quality assessment, article quality assessment, or full validation of the theory.

The tested page is a single Wikipedia article. The result should not be presented as evidence for all Wikipedia activity unless additional pages are tested under fixed specifications.

---

## 8. Notes

If the result is sparse, null, negative / inverse, or weak, record it as such.

Do not modify the design, script, threshold, page, observable, rolling window, event definition, or sample period to improve the result.

End of document.
