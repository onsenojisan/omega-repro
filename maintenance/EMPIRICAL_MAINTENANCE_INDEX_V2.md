# Empirical Maintenance Index v2.0

Status: Internal maintenance index
Purpose: Navigation index for empirical design, execution, result, summary, and closure documents
Scope: omega-repro maintenance documents after GitHub activity and Wikipedia activity sequences
Publication status: Internal only / not a result report

---

## 1. Purpose

This document indexes internal empirical maintenance files in the omega-repro repository.

This is v2 of the empirical maintenance index.

It reflects the completed GitHub activity sequence and the completed Wikipedia activity sequence.

Its purpose is navigation and maintenance.

It does not introduce new empirical definitions.

It does not modify any result.

It does not create a public claim.

It should be used to locate the correct document before changing, extending, or reviewing empirical work.

---

## 2. Relationship to v1

Previous index:

maintenance/EMPIRICAL_MAINTENANCE_INDEX_V1.md

Role of v1:
Index created after the GitHub activity sequence was completed.

Role of v2:
Index created after both GitHub activity and Wikipedia activity sequences were completed.

Do not delete or modify v1.

Use this v2 index as the current internal navigation reference.

---

## 3. Maintenance rule

Before starting a new empirical test, use the following order:

1. domain selection memo, if choosing between candidate domains
2. design note
3. fixed-scope memo
4. execution script
5. result memo
6. sequence summary, if multiple related tests exist
7. completion note, if the sequence should be closed
8. maintenance index update, after the structure is stable

Do not skip the fixed-scope memo.

Do not execute first and define later.

Do not change thresholds, event definitions, repositories, pages, sample periods, or observables after seeing results.

---

## 4. Core empirical design documents

### Internal Ω empirical design map

File:
maintenance/INTERNAL_OMEGA_EMPIRICAL_DESIGN_MAP_V1.md

Role:
General internal guide for choosing and screening future Ω empirical tests.

Use:
Read before starting a new empirical domain or deciding whether a domain should proceed, be delayed, or be excluded.

Do not use:
Do not treat this as a result report.

---

## 5. Domain selection documents

### Next empirical domain selection

File:
maintenance/NEXT_EMPIRICAL_DOMAIN_SELECTION_V1.md

Role:
Selected Wikipedia activity as the next empirical domain after the completed GitHub activity sequence.

Status:
completed

Use:
Read when reviewing why Wikipedia activity followed GitHub activity.

Do not use:
Do not treat this as a result report or as a fixed-scope memo.

---

## 6. GitHub activity sequence

### Sequence status

Status:
closed for current internal comparison

Completion boundary:
maintenance/GITHUB_ACTIVITY_SEQUENCE_COMPLETION_NOTE_V1.md

Summary:
The completed GitHub activity sequence consists of:

1. internal pipeline test on onsenojisan/omega-repro
2. external pandas-dev/pandas test
3. external numpy/numpy test
4. sequence summary
5. completion note

Do not automatically add more repositories to this sequence.

Additional GitHub repositories should be treated as a separate extension or new sequence version.

---

## 7. GitHub activity design file

File:
maintenance/GITHUB_ACTIVITY_OMEGA_TEST_DESIGN_V1.md

Role:
Pre-evaluation design for GitHub repository activity Ω tests.

Defines:
- domain
- observable family
- Ω construction
- high-Ω threshold
- event definition
- timing rule
- reporting requirements
- exclusion rules
- claim boundary

Use:
Read before creating any GitHub activity fixed-scope memo.

Do not use:
Do not change this file in response to later results.

---

## 8. Internal GitHub activity pipeline test

### Fixed scope

File:
maintenance/GITHUB_ACTIVITY_OMEGA_TEST_FIXED_SCOPE_V1.md

Role:
Fixed scope for the internal pipeline test on onsenojisan/omega-repro.

Status:
completed

### Execution script

File:
scripts/github_activity_omega_test.py

Role:
Execution script for the internal pipeline test.

Status:
completed

### Result memo

File:
maintenance/GITHUB_ACTIVITY_OMEGA_TEST_RESULT_V1.md

Role:
Internal result memo for the onsenojisan/omega-repro pipeline test.

Result class:
sparse

Status:
completed

Interpretation:
This is an internal pipeline test, not external evidence.

---

## 9. External pandas GitHub activity test

### Fixed scope

File:
maintenance/GITHUB_ACTIVITY_EXTERNAL_PANDAS_FIXED_SCOPE_V1.md

Role:
Fixed scope for the first external repository test on pandas-dev/pandas.

Status:
completed

### Execution script

File:
scripts/github_activity_external_pandas_test.py

Role:
Execution script for the pandas-dev/pandas test.

Status:
completed

### Result memo

File:
maintenance/GITHUB_ACTIVITY_EXTERNAL_PANDAS_RESULT_V1.md

Role:
Internal result memo for the pandas-dev/pandas test.

Result class:
positive concentration

Recorded summary values:
P(event | high Ω): 0.516129032258
ratio: 11.3529821304

Status:
completed

Interpretation:
External repository result under fixed specification. Not a standalone public claim.

---

## 10. External NumPy GitHub activity test

### Fixed scope

File:
maintenance/GITHUB_ACTIVITY_EXTERNAL_NUMPY_FIXED_SCOPE_V1.md

Role:
Fixed scope for the second external repository test on numpy/numpy.

Status:
completed

### Execution script

File:
scripts/github_activity_external_numpy_test.py

Role:
Execution script for the numpy/numpy test.

Status:
completed

### Result memo

File:
maintenance/GITHUB_ACTIVITY_EXTERNAL_NUMPY_RESULT_V1.md

Role:
Internal result memo for the numpy/numpy test.

Result class:
positive concentration

Recorded summary values:
P(event | high Ω): 0.505617977528
baseline P(event): 0.0468697313701
ratio: 10.7877293671

Status:
completed

Interpretation:
External repository result under fixed specification. Not a standalone public claim.

---

## 11. GitHub activity sequence summary and closure

### Sequence summary

File:
maintenance/GITHUB_ACTIVITY_TEST_SEQUENCE_SUMMARY_V1.md

Role:
Summarizes the internal pipeline test and two external repository tests.

Status:
completed

Use:
Read when reviewing the completed GitHub activity sequence as a whole.

Do not use:
Do not treat this as replacing individual result memos.

### Completion note

File:
maintenance/GITHUB_ACTIVITY_SEQUENCE_COMPLETION_NOTE_V1.md

Role:
Closes the current GitHub activity sequence as complete enough for internal comparison.

Status:
completed

Use:
Read before deciding whether to add another GitHub repository.

Rule:
Do not automatically add more repositories to the current sequence.

Any additional repository should start as a separate extension or new sequence version.

---

## 12. Wikipedia activity sequence

### Sequence status

Status:
closed for current internal comparison

Completion boundary:
maintenance/WIKIPEDIA_ACTIVITY_SEQUENCE_COMPLETION_NOTE_V1.md

Summary:
The completed Wikipedia activity sequence consists of:

1. first page test on Python (programming language)
2. second page test on Artificial intelligence
3. V1 sequence summary
4. V2 sequence summary
5. completion note

Do not automatically add more Wikipedia pages to this sequence.

Additional Wikipedia pages should be treated as a separate extension or new sequence version.

---

## 13. Wikipedia activity Python test

### Fixed scope

File:
maintenance/WIKIPEDIA_ACTIVITY_PYTHON_FIXED_SCOPE_V1.md

Role:
Fixed scope for the first Wikipedia activity test on English Wikipedia pageviews for Python (programming language).

Status:
completed

### Execution script

File:
scripts/wikipedia_activity_python_test.py

Role:
Execution script for the Python (programming language) Wikipedia pageview test.

Status:
completed

### Result memo

File:
maintenance/WIKIPEDIA_ACTIVITY_PYTHON_RESULT_V1.md

Role:
Internal result memo for the Python (programming language) Wikipedia activity test.

Result class:
positive concentration

Recorded summary values:
P(event | high Ω): 0.25
baseline P(event): 0.0500758725341
ratio: 4.99242424242
missing_days: 0

Status:
completed

Interpretation:
Single-page Wikipedia result under fixed specification. Not a standalone Wikipedia-domain claim.

---

## 14. Wikipedia activity Artificial intelligence test

### Fixed scope

File:
maintenance/WIKIPEDIA_ACTIVITY_AI_FIXED_SCOPE_V1.md

Role:
Fixed scope for the second Wikipedia activity test on English Wikipedia pageviews for Artificial intelligence.

Status:
completed

### Execution script

File:
scripts/wikipedia_activity_ai_test.py

Role:
Execution script for the Artificial intelligence Wikipedia pageview test.

Status:
completed

### Result memo

File:
maintenance/WIKIPEDIA_ACTIVITY_AI_RESULT_V1.md

Role:
Internal result memo for the Artificial intelligence Wikipedia activity test.

Result class:
positive concentration

Recorded summary values:
Recorded in the result memo.

Status:
completed

Interpretation:
Single-page Wikipedia result under fixed specification. Not a standalone Wikipedia-domain claim.

---

## 15. Wikipedia activity sequence summaries and closure

### V1 sequence summary

File:
maintenance/WIKIPEDIA_ACTIVITY_TEST_SEQUENCE_SUMMARY_V1.md

Role:
Summarizes the first Wikipedia activity test on Python (programming language).

Status:
completed / historical one-page summary

Use:
Read when reviewing the one-page starting point.

Do not use:
Do not treat this as the current full Wikipedia sequence summary.

### V2 sequence summary

File:
maintenance/WIKIPEDIA_ACTIVITY_TEST_SEQUENCE_SUMMARY_V2.md

Role:
Summarizes the current two-page Wikipedia activity sequence.

Status:
completed / current Wikipedia sequence summary

Use:
Read when reviewing the completed Wikipedia activity sequence as a whole.

Do not use:
Do not treat this as replacing individual result memos.

### Completion note

File:
maintenance/WIKIPEDIA_ACTIVITY_SEQUENCE_COMPLETION_NOTE_V1.md

Role:
Closes the current Wikipedia activity sequence as complete enough for internal comparison.

Status:
completed

Use:
Read before deciding whether to add another Wikipedia page.

Rule:
Do not automatically add more pages to the current sequence.

Any additional page should start as a separate extension or new sequence version.

---

## 16. Cross-sequence interpretation

Current completed information-system activity sequences:

GitHub activity:
- internal pipeline test: sparse
- pandas-dev/pandas: positive concentration
- numpy/numpy: positive concentration
- sequence closed

Wikipedia activity:
- Python (programming language): positive concentration
- Artificial intelligence: positive concentration
- sequence closed

Interpretation:
These are internal information-system activity extensions.

They should not be merged into a public cross-domain claim without a separate internal review.

They do not claim prediction, causality, software quality assessment, public attention forecasting, social behavior diagnosis, information quality assessment, or full validation of the theory.

---

## 17. Result interpretation rules

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

## 18. Public-facing boundary

The maintenance files are internal.

They may inform future public materials, but they are not public-facing claims by themselves.

Do not automatically add internal maintenance results to:

- README
- Zenodo public summaries
- cross-domain summary documents
- note posts
- Substack posts
- public PDF summaries

A separate public-facing review should be created before any public integration.

---

## 19. Recommended next workflow

When beginning a new empirical domain:

1. read maintenance/INTERNAL_OMEGA_EMPIRICAL_DESIGN_MAP_V1.md
2. create or review a domain selection memo if choosing between domains
3. create a domain design note
4. create a fixed-scope memo
5. create an execution script
6. run the script without changing definitions
7. create a result memo
8. create a sequence summary if multiple related tests exist
9. create a completion note if the sequence should be closed
10. update this index only after the sequence structure is stable

---

## 20. Current status summary

Current completed empirical maintenance sequences:

GitHub activity:
- internal pipeline test: sparse
- pandas-dev/pandas: positive concentration
- numpy/numpy: positive concentration
- sequence summary: completed
- completion note: completed

Wikipedia activity:
- Python (programming language): positive concentration
- Artificial intelligence: positive concentration
- V2 sequence summary: completed
- completion note: completed

Current instruction:
Do not expand GitHub activity or Wikipedia activity automatically.

Recommended next action:
Use this index to choose whether the next work should be:

- a new empirical domain
- a separate extension of an existing information-system domain
- a broader internal comparison across information-system activity tests
- an internal review before any public-facing integration

End of document.
