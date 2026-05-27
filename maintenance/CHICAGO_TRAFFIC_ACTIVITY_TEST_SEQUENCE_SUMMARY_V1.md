# Chicago Traffic Activity Test Sequence Summary v1.0

Status: Internal sequence summary
Purpose: Summarize the Chicago traffic crash activity Omega test sequence
Scope: Chicago, Illinois daily traffic crash count
Publication status: Internal only / not a public-facing claim

Related files:
- maintenance/CHICAGO_TRAFFIC_ACTIVITY_DOMAIN_SELECTION_V1.md
- maintenance/CHICAGO_TRAFFIC_ACTIVITY_FIXED_SCOPE_V1.md
- scripts/chicago_traffic_activity_test.py
- maintenance/CHICAGO_TRAFFIC_ACTIVITY_RESULT_V1.md

---

## 1. Sequence status

The Chicago traffic activity sequence currently contains one fixed-scope test:

1. Chicago, Illinois daily traffic crash count test

This summary does not replace the result memo.

---

## 2. Sequence order

The sequence preserved the required order:

1. source and schema verification
2. domain selection/design note
3. fixed-scope memo
4. execution script
5. script execution
6. result memo
7. sequence summary

No result-driven method changes were made.

---

## 3. Test summary

Domain:
traffic

Region:
Chicago, Illinois

Data source:
City of Chicago Data Portal, Traffic Crashes - Crashes

Dataset id:
85ca-t3if

Date field:
CRASH_DATE / crash_date

Observable:
daily traffic crash count

Omega:
rolling 30-day crash-count dispersion multiplied by absolute daily crash-count change

High-Omega condition:
Omega > q(0.99)

Independent event:
daily_crash_count > q(0.95)

Timing:
contemporaneous

Result class:
positive concentration

Recorded values:

- P(event | high Omega): 0.538461538462
- baseline P(event): 0.0498417721519
- ratio: 10.8034188034
- n_total: 2557
- n_valid: 2528
- n_high: 26
- n_event_total: 126
- n_event_high: 14
- n_source_records: 768801

---

## 4. Relationship to completed sequences

This Chicago traffic activity sequence is separate from the closed GitHub activity sequence.

This Chicago traffic activity sequence is separate from the closed Wikipedia activity sequence.

This Chicago traffic activity sequence is separate from the closed global earthquake activity sequence.

This Chicago traffic activity sequence is separate from the closed London weather activity sequence.

This Chicago traffic activity sequence is separate from any prior traffic result.

It is not a replacement, reinterpretation, public update, or extension of any prior traffic result.

---

## 5. Interpretation boundary

This sequence evaluates structural concentration only.

It asks whether an independently defined high daily crash-count event occurs more frequently under high-Omega conditions than at baseline.

It does not claim prediction, causality, intervention, traffic-safety recommendation, policy relevance, public warning, operational guidance, risk scoring, or full validation of the theory.

It should not be integrated into public-facing materials without a separate public-facing review.

End of document.
