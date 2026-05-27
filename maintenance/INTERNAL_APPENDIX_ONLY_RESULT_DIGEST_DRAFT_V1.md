# Internal Appendix-Only Result Digest Draft v1.0

Status: Internal digest draft
Purpose: Summarize completed internal empirical sequences as possible future appendix-only material
Scope: GitHub activity, Wikipedia activity, global earthquake activity, London weather activity, and Chicago traffic activity sequences
Publication status: Internal only / not a public-facing artifact

Related files:
- AGENTS.md
- maintenance/EMPIRICAL_MAINTENANCE_INDEX_V5.md
- maintenance/INTERNAL_EMPIRICAL_SEQUENCES_STATUS_REVIEW_V3.md
- maintenance/PUBLIC_FACING_INTEGRATION_ELIGIBILITY_REVIEW_V1.md
- maintenance/PUBLIC_FACING_ARTIFACT_PLAN_V1.md

---

## 1. Purpose and scope

This document is an internal appendix-only result digest draft.

It summarizes completed internal empirical sequences as possible future appendix-only material.

It is not a public artifact.

It does not create or run a new empirical test.

It does not modify result values, completed result memos, empirical definitions, thresholds, event definitions, sample periods, timing rules, or claim boundaries.

It does not update README, GitHub Pages, Zenodo/public summaries, canonical documents, public PDFs, note posts, Substack posts, omega-library, or any public-facing surface.

The default recommendation remains:
no immediate public integration.

---

## 2. Inclusion rule

Include only completed internal sequences indexed by maintenance/EMPIRICAL_MAINTENANCE_INDEX_V5.md and reviewed in maintenance/INTERNAL_EMPIRICAL_SEQUENCES_STATUS_REVIEW_V3.md.

Use only values already recorded in existing result memos, sequence summaries, or maintenance index files.

If a value is not clearly recorded in those sources, write:

```text
not summarized here
```

Positive concentration alone is not public eligibility.

Platform analytics are not validation evidence.

All language in this digest is limited to structural concentration only.

---

## 3. Result digest table

| sequence name | test / unit | domain / topology | data source | sample period | observable | I definition | G definition | Omega definition | high-Omega threshold | independent event definition | P(event \| high Omega) | baseline P(event) | ratio | n_total | n_high | n_event_high | result class | appendix suitability | public-risk note | required exclusion language |
|---|---|---|---|---|---|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---|---|---|---|
| GitHub activity sequence | onsenojisan/omega-repro | GitHub repository activity / information-system repository activity | not summarized here | 2026-03-24 through 2026-05-26 UTC, inclusive | activity_count = number of commits per UTC day | rolling standard deviation(activity_count, window = 30 days) | absolute first difference(activity_count) | Omega = I x G | Omega > q(0.99), q_0.99 = 2.40858460444 | activity_count > q(0.95), q_0.95 = 3 | 0 | 0 | nan | 64 | 1 | 0 | sparse | appendix-only candidate only if sparse pipeline result remains visible | high software-quality and maintainer-behavior misread risk | no prediction; no causality; no intervention; no software-quality assessment; no maintainer behavior assessment; no full-theory validation |
| GitHub activity sequence | pandas-dev/pandas | GitHub repository activity / information-system repository activity | not summarized here | 2009-07-31 through 2026-05-26 UTC, inclusive | activity_count = number of commits per UTC day | rolling standard deviation(activity_count, window = 30 days) | absolute first difference(activity_count) | Omega = I x G | Omega > q(0.99), q_0.99 = 152.39969333 | activity_count > q(0.95), q_0.95 = 18 | 0.516129032258 | 0.0454619787408 | 11.3529821304 | 6144 | 62 | 32 | positive concentration | appendix-only candidate only with external-repository limits stated | high software-quality and maintainer-behavior misread risk | no prediction; no causality; no intervention; no software-quality assessment; no maintainer behavior assessment; no full-theory validation |
| GitHub activity sequence | numpy/numpy | GitHub repository activity / information-system repository activity | not summarized here | 2001-12-18 through 2026-05-26 UTC, inclusive | activity_count = number of commits per UTC day | rolling standard deviation(activity_count, window = 30 days) | absolute first difference(activity_count) | Omega = I x G | Omega > q(0.99), q_0.99 = 139.359972741 | activity_count > q(0.95), q_0.95 = 15 | 0.505617977528 | 0.0468697313701 | 10.7877293671 | 8926 | 89 | 45 | positive concentration | appendix-only candidate only with external-repository limits stated | high software-quality and maintainer-behavior misread risk | no prediction; no causality; no intervention; no software-quality assessment; no maintainer behavior assessment; no full-theory validation |
| Wikipedia activity sequence | Python (programming language) | Wikipedia activity / information-system public page activity | Wikimedia Pageviews API | 2015-07-01 through 2026-05-26 UTC, inclusive | activity_count = daily pageview count | rolling standard deviation(activity_count, window = 30 days) | absolute first difference(activity_count) | Omega = I x G | Omega > q(0.99), q_0.99 = 9111909.79039 | activity_count > q(0.95), q_0.95 = 10394.8 | 0.25 | 0.0500758725341 | 4.99242424242 | 3983 | 40 | 10 | positive concentration | appendix-only candidate only with public-attention exclusions | high public-attention and social-behavior misread risk | no prediction; no causality; no public-attention forecasting; no social behavior diagnosis; no information-quality assessment; no full-theory validation |
| Wikipedia activity sequence | Artificial intelligence | Wikipedia activity / information-system public page activity | Wikimedia Pageviews API | 2015-07-01 through 2026-05-26 UTC, inclusive | activity_count = daily pageview count | rolling standard deviation(activity_count, window = 30 days) | absolute first difference(activity_count) | Omega = I x G | Omega > q(0.99), q_0.99 = 13777877.6356 | activity_count > q(0.95), q_0.95 = 19418.95 | 0.4 | 0.0500758725341 | 7.98787878788 | 3983 | 40 | 16 | positive concentration | appendix-only candidate only with public-attention exclusions | high public-attention and social-behavior misread risk | no prediction; no causality; no public-attention forecasting; no social behavior diagnosis; no information-quality assessment; no full-theory validation |
| Global earthquake activity sequence | global USGS earthquake activity | global earthquake activity / natural event-sequence activity | USGS FDSN Event API | 2000-01-01 through 2025-12-30 UTC, inclusive | activity_count = daily count of earthquakes with preferred magnitude >= 5.5 | rolling sample standard deviation(activity_count, window = 30 days) | absolute first difference(activity_count) | Omega = I x G | Omega > q(0.99), q_0.99 = 18.6192361281 | next UTC day contains at least one earthquake with preferred magnitude >= 6.5 | 0.221052631579 | 0.106897644449 | 2.06789057624 | 9496 | 95 | 21 | positive concentration | appendix-only candidate only with strong anti-forecasting limits | very high earthquake forecasting, hazard, warning, and risk misread risk | no prediction; no causality; no earthquake forecasting; no hazard assessment; no public warning; no intervention; no policy; no risk scoring; no full-theory validation |
| London weather activity sequence | London daily precipitation | weather / physical environmental time series | Open-Meteo Archive API | 2015-01-01 through 2024-12-31 UTC, inclusive | daily_precipitation_mm = precipitation_sum in millimeters | rolling sample standard deviation(daily_precipitation_mm, window = 30 days) | absolute first difference(daily_precipitation_mm) | Omega = I x G | Omega > q(0.99), q_0.99 = 101.745635181 | daily_precipitation_mm > q(0.95), q_0.95 = 9.5 | 0.513513513514 | 0.0496688741722 | 10.3387387387 | 3653 | 37 | 19 | positive concentration | appendix-only candidate only with weather/climate exclusions | high weather forecasting, climate, warning, policy, and risk misread risk | no prediction; no causality; no weather forecasting; no climate interpretation; no public warning; no intervention; no policy; no risk scoring; no full-theory validation |
| Chicago traffic activity sequence | Chicago daily traffic crash count | traffic / civic-transport count time series | City of Chicago Data Portal, Traffic Crashes - Crashes | 2018-01-01 through 2024-12-31, inclusive | daily_crash_count = count of crash records per calendar day | rolling sample standard deviation(daily_crash_count, window = 30 days) | absolute first difference(daily_crash_count) | Omega = I x G | Omega > q(0.99), q_0.99 = 8541.60699871 | daily_crash_count > q(0.95), q_0.95 = 388 | 0.538461538462 | 0.0498417721519 | 10.8034188034 | 2557 | 26 | 14 | positive concentration | appendix-only candidate only with traffic-safety and policy exclusions | very high traffic-safety, intervention, policy, public-warning, operational, and risk-score misread risk | no prediction; no causality; no intervention; no policy; no traffic-safety recommendation; no public warning; no operational guidance; no risk scoring; no full-theory validation |

---

## 4. Sequence-specific notes

### GitHub activity sequence

The GitHub activity sequence contains one sparse internal pipeline result and two positive external repository results.

The sparse internal pipeline result must remain visible if this sequence is ever summarized.

The sequence should not be presented as evidence about software quality, maintainers, all open-source projects, or software systems generally.

### Wikipedia activity sequence

The Wikipedia activity sequence contains two positive pageview activity results.

The sequence should not be presented as evidence about public attention, social behavior, information quality, article quality, or knowledge systems generally.

### Global earthquake activity sequence

The global earthquake activity sequence contains one positive concentration result under a fixed next-day event rule.

The sequence should not be presented as earthquake forecasting, hazard assessment, public warning capability, emergency planning evidence, or risk scoring.

### London weather activity sequence

The London weather activity sequence contains one positive concentration result for daily precipitation.

The sequence should not be presented as weather forecasting, climate interpretation, public warning capability, flooding evidence, infrastructure risk evidence, or policy evidence.

### Chicago traffic activity sequence

The Chicago traffic activity sequence contains one positive concentration result for daily traffic crash counts.

The sequence should not be presented as traffic-safety guidance, intervention evidence, policy evidence, operational guidance, public warning capability, or risk scoring.

---

## 5. Public-risk notes

The highest-risk sequences for public misunderstanding are:

- global earthquake activity
- Chicago traffic activity
- London weather activity

Reason:
These domains naturally invite forecasting, warning, policy, safety, or risk interpretations.

The information-system sequences also carry high public risk:

- GitHub activity may be misread as software-quality or maintainer behavior evidence.
- Wikipedia activity may be misread as public-attention or social behavior evidence.

This digest is therefore not suitable for public use without a separate public-facing wording and exclusion review.

---

## 6. What must not be claimed

Do not claim:

- prediction
- causality
- optimization
- intervention value
- policy relevance
- trading value
- risk scoring
- software quality assessment
- maintainer behavior assessment
- public attention forecasting
- social behavior diagnosis
- information quality assessment
- article quality assessment
- earthquake forecasting
- hazard assessment
- public warning capability
- weather forecasting
- climate interpretation
- traffic-safety recommendation
- operational guidance
- public safety guidance
- full theory validation
- universal cross-domain generality

Do not use platform analytics as validation evidence.

Do not use positive concentration alone as public eligibility.

Do not hide sparse, weak, null, negative, inverse, or inconvenient results.

---

## 7. Appendix-only suitability judgment

Overall suitability:
possible appendix-only candidate later, not now.

Reason:

- the completed sequence set is internally indexed and fixed
- all listed values are already recorded in result memos, summaries, or index files
- claim boundaries are already explicit
- public-facing risk remains high
- no public-facing wording review has approved this digest
- positive concentration alone is not enough for public integration

Current judgment by sequence:

| sequence | appendix-only suitability |
|---|---|
| GitHub activity | possible later only if sparse pipeline result remains visible |
| Wikipedia activity | possible later only with public-attention exclusions |
| Global earthquake activity | possible later only with strong anti-forecasting and anti-warning exclusions |
| London weather activity | possible later only with weather, climate, warning, policy, and risk exclusions |
| Chicago traffic activity | possible later only with traffic-safety, policy, intervention, warning, operational, and risk-score exclusions |

---

## 8. Required review before any public use

Before any public use, create a separate review that fixes:

1. destination surface
2. exact allowed wording
3. exact prohibited wording
4. whether result values are included, summarized, or omitted
5. whether all sequences are included or only a conservative subset
6. how sparse and limitation cases are displayed
7. how live API revision caveats are stated
8. how public-risk language is attached to each domain
9. whether appendix-only placement is actually appropriate
10. whether any Zenodo supplement or Cross-Domain Summary plan supersedes this digest

No public artifact should be created from this draft alone.

---

## 9. Current recommendation

Keep this digest internal.

Do not use it to update README, GitHub Pages, Zenodo/public summaries, public PDFs, note posts, Substack posts, omega-library, or Cross-Domain Summary materials.

Do not run another empirical sequence from this digest.

Do not treat this digest as external reproduction.

Recommended next step:
public-facing wording and exclusion review for the digest, if the maintainer wants to continue toward appendix-only material.

End of document.
