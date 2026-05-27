# Empirical Maintenance Index v1.0

Status: Internal maintenance index  
Purpose: Navigation index for empirical design, execution, result, and closure documents  
Scope: omega-repro maintenance documents and empirical execution support  
Publication status: Internal only / not a result report

---

## 1. Purpose

This document indexes internal empirical maintenance files in the omega-repro repository.

Its purpose is navigation and maintenance.

It does not introduce new empirical definitions.

It does not modify any result.

It does not create a public claim.

It should be used to locate the correct document before changing, extending, or reviewing empirical work.

---

## 2. Maintenance rule

Before starting a new empirical test, use the following order:

1. design note
2. fixed-scope memo
3. execution script
4. result memo
5. sequence summary, if multiple related tests exist
6. completion note, if the sequence should be closed

Do not skip the fixed-scope memo.

Do not execute first and define later.

Do not change thresholds, event definitions, repositories, sample periods, or observables after seeing results.

---

## 3. Core empirical design documents

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

## 4. GitHub activity test sequence

### Sequence status

Status:
closed for current internal comparison

Completion boundary:
maintenance/GITHUB_ACTIVITY_SEQUENCE_COMPLETION_NOTE_V1.md

Summary:
The current GitHub activity sequence consists of:

1. internal pipeline test on onsenojisan/omega-repro
2. external pandas-dev/pandas test
3. external numpy/numpy test
4. sequence summary
5. completion note

Do not automatically add more repositories to this sequence.

Additional repositories should be treated as a separate extension or new sequence version.

---

## 5. GitHub activity design file

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

## 6. Internal GitHub activity pipeline test

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

## 7. External pandas GitHub activity test

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

## 8. External NumPy GitHub activity test

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

## 9. GitHub activity sequence summary and closure

### Sequence summary

File:
maintenance/GITHUB_ACTIVITY_TEST_SEQUENCE_SUMMARY_V1.md

Role:
Summarizes the internal pipeline test and two external repository tests.

Status:
completed

Use:
Read when reviewing the current GitHub activity sequence as a whole.

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

## 10. Result interpretation rules

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

## 11. Public-facing boundary

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

## 12. Recommended next workflow

When beginning a new empirical domain:

1. read maintenance/INTERNAL_OMEGA_EMPIRICAL_DESIGN_MAP_V1.md
2. create a domain design note
3. create a fixed-scope memo
4. create an execution script
5. run the script without changing definitions
6. create a result memo
7. create a sequence summary if multiple related tests exist
8. create a completion note if the sequence should be closed
9. update this index only after the sequence structure is stable

---

## 13. Current status summary

Current completed empirical maintenance sequence:

GitHub activity:
- internal pipeline test: sparse
- pandas-dev/pandas: positive concentration
- numpy/numpy: positive concentration
- sequence summary: completed
- completion note: completed

Current instruction:
Do not expand GitHub activity automatically.

Recommended next action:
Use this index to choose whether the next work should be a new domain, a separate GitHub activity extension, or a broader internal comparison.

End of document.
