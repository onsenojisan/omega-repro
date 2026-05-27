# Empirical Maintenance Index v3.0

Status: Internal maintenance index
Purpose: Navigation index for empirical design, execution, result, summary, and closure documents
Scope: omega-repro maintenance documents after GitHub activity, Wikipedia activity, and earthquake activity sequences
Publication status: Internal only / not a result report

---

## 1. Purpose

This document indexes internal empirical maintenance files in the omega-repro repository.

This is v3 of the empirical maintenance index.

It reflects the completed GitHub activity sequence, the completed Wikipedia activity sequence, and the completed first earthquake activity sequence.

Its purpose is navigation and maintenance.

It does not introduce new empirical definitions.

It does not modify any result.

It does not create a public claim.

Use this v3 index as the current internal navigation reference after the earthquake activity sequence.

---

## 2. Relationship to previous indexes

Previous indexes:

- maintenance/EMPIRICAL_MAINTENANCE_INDEX_V1.md
- maintenance/EMPIRICAL_MAINTENANCE_INDEX_V2.md

Role of v1:
Index created after the GitHub activity sequence was completed.

Role of v2:
Index created after both GitHub activity and Wikipedia activity sequences were completed.

Role of v3:
Index created after the first earthquake activity sequence was completed.

Do not delete or modify v1 or v2.

---

## 3. Maintenance rule

Before starting a new empirical test, use the following order:

1. domain selection memo, if choosing between candidate domains
2. design note
3. fixed-scope memo
4. execution script
5. result memo
6. sequence summary, if multiple related tests exist or a sequence boundary is useful
7. completion note, if the sequence should be closed
8. maintenance index update, after the structure is stable

Do not skip the fixed-scope memo.

Do not execute first and define later.

Do not change thresholds, event definitions, repositories, pages, sample periods, observables, or timing rules after seeing results.

---

## 4. Core empirical design documents

### Internal Omega empirical design map

File:
maintenance/INTERNAL_OMEGA_EMPIRICAL_DESIGN_MAP_V1.md

Role:
General internal guide for choosing and screening future Omega empirical tests.

Use:
Read before starting a new empirical domain or deciding whether a domain should proceed, be delayed, or be excluded.

Do not use:
Do not treat this as a result report.

---

## 5. GitHub activity sequence

Sequence status:
closed for current internal comparison

Completion boundary:
maintenance/GITHUB_ACTIVITY_SEQUENCE_COMPLETION_NOTE_V1.md

Summary:
maintenance/GITHUB_ACTIVITY_TEST_SEQUENCE_SUMMARY_V1.md

Completed tests:

1. maintenance/GITHUB_ACTIVITY_OMEGA_TEST_RESULT_V1.md
2. maintenance/GITHUB_ACTIVITY_EXTERNAL_PANDAS_RESULT_V1.md
3. maintenance/GITHUB_ACTIVITY_EXTERNAL_NUMPY_RESULT_V1.md

Rule:
Do not automatically add more repositories to the current sequence.

---

## 6. Wikipedia activity sequence

Sequence status:
closed for current internal comparison

Completion boundary:
maintenance/WIKIPEDIA_ACTIVITY_SEQUENCE_COMPLETION_NOTE_V1.md

Current summary:
maintenance/WIKIPEDIA_ACTIVITY_TEST_SEQUENCE_SUMMARY_V2.md

Completed tests:

1. maintenance/WIKIPEDIA_ACTIVITY_PYTHON_RESULT_V1.md
2. maintenance/WIKIPEDIA_ACTIVITY_AI_RESULT_V1.md

Rule:
Do not automatically add more Wikipedia pages to the current sequence.

---

## 7. Earthquake activity sequence

Sequence status:
closed for current internal comparison

Completion boundary:
maintenance/EARTHQUAKE_ACTIVITY_SEQUENCE_COMPLETION_NOTE_V1.md

Sequence summary:
maintenance/EARTHQUAKE_ACTIVITY_TEST_SEQUENCE_SUMMARY_V1.md

### Domain selection/design

File:
maintenance/EARTHQUAKE_ACTIVITY_DOMAIN_SELECTION_V1.md

Role:
Selects global earthquake activity as the next internal empirical domain after the closed GitHub and Wikipedia activity sequences.

Boundary:
Separate from any prior Japan earthquake result; not a Japan-region extension, reinterpretation, or replacement.

Status:
completed

Do not use:
Do not treat this as a result report.

### Fixed scope

File:
maintenance/EARTHQUAKE_ACTIVITY_FIXED_SCOPE_V1.md

Role:
Fixed pre-execution scope for the first earthquake activity Omega test.

Status:
completed

### Execution script

File:
scripts/earthquake_activity_global_m55_test.py

Role:
Execution script for the fixed global earthquake activity test.

Status:
completed

### Result memo

File:
maintenance/EARTHQUAKE_ACTIVITY_RESULT_V1.md

Role:
Internal result memo for the first global earthquake activity Omega test.

Result class:
positive concentration

Recorded summary values:

- P(event | high Omega): 0.221052631579
- baseline P(event): 0.106897644449
- ratio: 2.06789057624
- n_total: 9496
- n_valid: 9467
- n_high: 95
- n_event_total: 1012
- n_event_high: 21

Status:
completed

Interpretation:
Single fixed global earthquake activity result under fixed specification. Not an earthquake forecasting, hazard, risk, or public claim.

Boundary:
Separate from any prior Japan earthquake result.

---

## 8. Cross-sequence interpretation

Current completed empirical maintenance sequences:

GitHub activity:

- internal pipeline test: sparse
- pandas-dev/pandas: positive concentration
- numpy/numpy: positive concentration
- sequence closed

Wikipedia activity:

- Python (programming language): positive concentration
- Artificial intelligence: positive concentration
- sequence closed

Earthquake activity:

- global USGS earthquake activity: positive concentration
- sequence closed

Interpretation:
These are internal empirical extensions.

They should not be merged into a public cross-domain claim without a separate internal review and public-facing review.

They do not claim prediction, causality, forecasting, intervention, policy relevance, risk scoring, hazard assessment, public attention forecasting, social behavior diagnosis, information quality assessment, or full validation of the theory.

---

## 9. Result interpretation rules

Completed results must remain fixed.

Do not change a result memo because the result is:

- sparse
- null
- negative / inverse
- weak
- positive

Do not change the method after seeing a favorable result.

Do not remove sparse results.

Do not promote a sequence to public claim without a separate public-facing review.

---

## 10. Public-facing boundary

The maintenance files are internal.

They may inform future public materials, but they are not public-facing claims by themselves.

Do not automatically add internal maintenance results to:

- README
- GitHub Pages
- Zenodo public summaries
- canonical docs
- public PDFs
- public cross-domain summary documents
- note posts
- Substack posts

A separate public-facing review should be created before any public integration.

---

## 11. Recommended next workflow

When beginning another empirical domain or extension:

1. read maintenance/INTERNAL_OMEGA_EMPIRICAL_DESIGN_MAP_V1.md
2. create or review a domain selection memo if choosing between domains
3. create a domain design note
4. create a fixed-scope memo
5. create an execution script
6. run the script without changing definitions
7. create a result memo
8. create a sequence summary if useful
9. create a completion note if the sequence should be closed
10. update this index only after the sequence structure is stable

End of document.
