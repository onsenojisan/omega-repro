# Public-Facing Artifact Plan v1.0

Status: Internal planning document
Purpose: Define possible future public-facing empirical artifacts, ordering, scope, exclusions, and prerequisites
Scope: Planning only for future public-facing handling of completed internal empirical sequences
Publication status: Internal only / not a public-facing claim

Related files:
- AGENTS.md
- maintenance/EMPIRICAL_MAINTENANCE_INDEX_V5.md
- maintenance/INTERNAL_EMPIRICAL_SEQUENCES_STATUS_REVIEW_V3.md
- maintenance/PUBLIC_FACING_INTEGRATION_ELIGIBILITY_REVIEW_V1.md

---

## 1. Purpose and scope

This document defines a conservative plan for possible future public-facing artifacts related to completed internal Omega empirical sequences.

This is a planning document only.

It does not create or edit any public-facing artifact.

It does not create or run a new empirical test.

It does not modify result values, completed result memos, empirical definitions, thresholds, event definitions, sample periods, timing rules, or claim boundaries.

It does not update README, GitHub Pages, Zenodo/public summaries, canonical documents, public PDFs, note posts, Substack posts, omega-library, or any public-facing surface.

The default recommendation remains:
no immediate public integration.

---

## 2. Current status summary

The current internal empirical sequence set is indexed in maintenance/EMPIRICAL_MAINTENANCE_INDEX_V5.md.

Completed internal sequences:

| sequence | status | public-facing status |
|---|---|---|
| GitHub activity | closed for current internal comparison | internal only |
| Wikipedia activity | closed for current internal comparison | internal only |
| Global earthquake activity | closed for current internal comparison | internal only |
| London weather activity | closed for current internal comparison | internal only |
| Chicago traffic activity | closed for current internal comparison | internal only |

The public-facing integration eligibility review concludes:

```text
no integration yet
```

This plan accepts that conclusion.

---

## 3. Relationship to PUBLIC_FACING_INTEGRATION_ELIGIBILITY_REVIEW_V1

maintenance/PUBLIC_FACING_INTEGRATION_ELIGIBILITY_REVIEW_V1.md controls this plan.

That review states:

- positive concentration alone is not public eligibility
- completed internal sequences should remain internal for now
- public-facing integration requires a separate artifact plan
- public language must remain limited to structural concentration only
- high-risk domains require strong exclusions against forecasting, policy, traffic-safety, risk-score, software-quality, public-attention, and full-theory validation claims

This plan is the artifact-planning step requested by that review.

It does not override the eligibility review.

It does not authorize public integration.

---

## 4. Possible future public-facing artifact types

| artifact type | possible role | current recommendation | notes |
|---|---|---|---|
| appendix-only internal result digest | low-prominence technical digest of fixed internal sequence statuses and minimal outputs | first candidate, but not now | should remain technical, include sparse/null rules, and avoid narrative claims |
| Zenodo supplement candidate | reproducibility-oriented supplement containing fixed-scope references and minimal result tables | possible later | only after artifact scope, wording, and result inclusion rules are fixed |
| note/Substack explanatory candidate | explanatory article about how internal empirical maintenance works | not recommended now | high narrative overstatement risk |
| Cross-Domain Summary update candidate | future conservative summary of internal topology coverage | possible only after separate cross-domain public review | must avoid universal validation language |
| README/GitHub Pages update candidate | public navigation update or minimal pointer | last candidate, not recommended now | highest risk of turning internal maintenance into public claim surface |

---

## 5. Recommended order of artifacts

Recommended order if public-facing work proceeds later:

1. Internal appendix-only result digest draft
2. Public-facing wording and exclusion review for the digest
3. Zenodo supplement scope review
4. Zenodo supplement candidate draft, if approved
5. Cross-Domain Summary eligibility review
6. Cross-Domain Summary candidate draft, if approved
7. note/Substack explanatory candidate, only after the above are stable
8. README/GitHub Pages update candidate, only if a stable public artifact already exists and a minimal navigation pointer is justified

Do not skip directly to README, GitHub Pages, note/Substack, or Cross-Domain Summary.

Do not create any artifact in this list from this plan alone.

---

## 6. What should remain internal for now

The following should remain internal for now:

- all completed result memos
- all detailed sequence summaries
- all sequence completion notes
- all exact result values unless a later artifact plan explicitly approves inclusion
- the sparse GitHub internal pipeline result, which must remain visible if GitHub is summarized
- domain-specific limitation language
- live API revision caveats
- sequence-level risk assessments
- public-facing eligibility judgments

Internal-only status applies to:

- GitHub activity sequence
- Wikipedia activity sequence
- global earthquake activity sequence
- London weather activity sequence
- Chicago traffic activity sequence

---

## 7. Minimum conditions before any public artifact is created

Before any public artifact is created, the maintainer should fix:

1. artifact type
2. destination surface
3. intended reader
4. exact allowed wording
5. exact prohibited wording
6. whether result values are included, summarized, or omitted
7. whether all sequences are included or only a conservative subset
8. whether sparse, null, weak, negative, inverse, and positive results are all represented correctly
9. how data-source reproducibility caveats are stated
10. how live API revision risk is stated
11. how internal maintenance documents are linked, if at all
12. whether a technical appendix is required before narrative explanation
13. whether a Zenodo supplement is required before any public navigation update
14. whether the artifact can be reviewed without changing result memos

If any condition is unresolved, do not create the public artifact.

---

## 8. Required claim boundary language

Any future public-facing artifact must preserve language equivalent to:

```text
This material reports fixed internal structural concentration checks.
It asks whether independently defined events occur more frequently under high-Omega conditions than at baseline.
It does not claim prediction, causality, intervention, policy relevance, risk scoring, public warning, software-quality assessment, public-attention forecasting, traffic-safety guidance, or full validation of the theory.
```

If a shorter version is required, it must still include:

```text
structural concentration only
no prediction
no causality
no intervention or policy claim
no risk-score or public-warning claim
no full-theory validation
```

---

## 9. Prohibited public framings

Do not frame any public artifact as:

- prediction
- causality
- intervention
- policy guidance
- trading signal
- risk score
- software-quality assessment
- maintainer behavior assessment
- public-attention forecasting
- social behavior diagnosis
- information-quality assessment
- earthquake forecasting
- hazard assessment
- public warning
- weather forecasting
- climate interpretation
- traffic-safety recommendation
- operational guidance
- full-theory validation
- universal cross-domain proof

Do not use platform analytics as validation evidence.

Do not use positive concentration alone as public eligibility.

Do not hide sparse, null, weak, negative, or inverse results if the relevant sequence is summarized.

---

## 10. Sequence-by-sequence artifact suitability

| sequence | appendix-only digest | Zenodo supplement | note/Substack explanation | Cross-Domain Summary | README/GitHub Pages |
|---|---|---|---|---|---|
| GitHub activity | possible later; must include sparse internal pipeline result | possible later if reproducibility boundaries are clear | not recommended now; software-quality misread risk | possible only as one limited information-system example | not recommended now |
| Wikipedia activity | possible later; public-attention exclusions required | possible later if API reproducibility caveats are included | not recommended now; public-attention narrative risk | possible only as one limited information-system example | not recommended now |
| Global earthquake activity | possible only with strong anti-forecasting language | possible later as reproducibility supplement candidate | not recommended now; hazard and warning risk | high-risk inclusion; requires separate review | not recommended now |
| London weather activity | possible later; weather and climate exclusions required | possible later with live API caveats | not recommended now; weather narrative risk | possible only with explicit non-forecasting language | not recommended now |
| Chicago traffic activity | possible later; traffic-safety and policy exclusions required | possible later with City of Chicago data caveats | not recommended now; traffic-safety and policy risk | high-risk inclusion; requires separate review | not recommended now |

Overall suitability:

- appendix-only digest is the safest first possible public-facing form
- Zenodo supplement is the safest possible reproducibility-oriented form
- note/Substack and README/GitHub Pages are not immediate candidates
- Cross-Domain Summary requires a separate review before any update

---

## 11. Recommended next action

Recommended next action:
do not create any public-facing artifact yet.

If the maintainer wants to proceed, create an internal appendix-only result digest draft first.

That draft should:

- be internal until reviewed
- include only fixed sequence statuses and minimal values
- preserve sparse/null/negative/weak/positive result rules
- include mandatory claim boundary language
- avoid public narrative framing
- not update README, GitHub Pages, Zenodo, note, Substack, public PDFs, or omega-library

---

## 12. Stop conditions

Stop public-facing artifact work if any of the following occur:

- public wording implies prediction
- public wording implies causality
- public wording implies intervention or policy guidance
- public wording implies trading relevance
- public wording implies traffic-safety guidance
- public wording implies risk scoring
- public wording implies software-quality assessment
- public wording implies public-attention forecasting
- public wording implies full-theory validation
- result values are changed
- completed result memos would need edits
- sparse or limitation cases would be omitted
- artifact scope depends on platform analytics
- artifact scope depends on positive results only
- destination surface is README or GitHub Pages before a stable public artifact exists
- Zenodo/public summary text would be changed before wording review
- Cross-Domain Summary would be updated before a separate cross-domain review

End of document.
