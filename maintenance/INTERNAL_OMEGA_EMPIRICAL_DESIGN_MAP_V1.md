# Internal Ω Empirical Design Map v1.0

Status: Internal / maintainer-facing working document  
Purpose: Empirical design support  
Scope: Future Ω empirical tests  
Publication status: Not intended as a theory or outreach document

---

## 1. Purpose

This document defines the internal design map for choosing, structuring, and screening future Ω empirical tests.

Its purpose is not to expand the theory.

Its purpose is to make empirical work faster, more stable, and less dependent on repeated theoretical judgment.

This document should be used before starting a new empirical test to decide:

- whether the domain is suitable for an Ω test,
- what observable variables can be used,
- how Ω should be operationalized,
- how the event / collapse outcome should be defined independently from Ω,
- whether the test should proceed, be delayed, or be excluded.

This document is an empirical execution aid.

It is not a replacement for:

- Ω Minimal Standard Form v1.0,
- existing reproducibility protocols,
- domain-specific empirical reports,
- PureCore,
- VOT,
- the Structural Overview,
- Civilizational Ω.

---

## 2. Core Empirical Question

The minimal empirical question is:

> Do independently defined collapse-like events concentrate in high-Ω states compared with the baseline event rate?

The standard comparison is:

```text
P(event | high Ω)
vs
baseline P(event)
```

For compatibility with the existing Ω Minimal Standard Form, this is equivalent to:

```text
P(collapse | high Ω)
vs
P(collapse)
```

Optional derived output:

```text
ratio = P(event | high Ω) / baseline P(event)
```

or, equivalently:

```text
ratio = P(collapse | high Ω) / P(collapse)
```

No other result is required for the minimal empirical claim.

---

## 3. Terminology Note

In this document, "event" means the independently defined collapse-like binary outcome used in the minimal validation standard.

For compatibility with existing Ω documents:

```text
event ≡ collapse-like event
P(event | high Ω) ≡ P(collapse | high Ω)
baseline P(event) ≡ P(collapse)
```

The word "event" is used when discussing broad empirical design across domains.

The word "collapse" is used when aligning with the formal minimal standard.

Both refer to the same required structure:

```text
one independently defined binary outcome
```

The event / collapse definition must be fixed before evaluation and must not be derived from Ω, I, G, or the high-Ω threshold.

---

## 4. Fixed Minimal Claim

The empirical claim is limited to structural concentration.

Accepted claim:

```text
Collapse-like events concentrate in high-Ω states.
```

Equivalent formal statement:

```text
P(collapse | high Ω) > P(collapse)
```

Not accepted as minimal claims:

```text
Ω predicts collapse.
Ω causes collapse.
Ω optimizes intervention.
Ω is a trading signal.
Ω is a complete model of the domain.
Ω validates the entire Pleasure Order framework.
```

The empirical test only evaluates whether independently defined events are more frequent under pre-defined high-Ω conditions than under the baseline.

---

## 5. Fixed Validation Rules

All empirical tests should preserve the following rules.

### 5.1 High-Ω condition

For new minimal tests, the default high-Ω execution standard is:

```text
high Ω = Ω > q(0.99)
```

Rules:

```text
q is computed within each dataset
q is fixed ex ante
q = 0.99 is the default minimal-test threshold
```

Other thresholds may be used only as exploratory or sensitivity checks.

They are not part of the default minimal test.

They must be reported separately.

They must not replace the q = 0.99 result after observing outcomes.

The high-Ω threshold must not be changed after seeing the result.

---

### 5.2 Independent event / collapse definition

The event / collapse definition must be independent from Ω.

The event must not be defined using:

- Ω itself,
- I,
- G,
- the high-Ω threshold,
- the same composite score used to define Ω,
- any post-hoc condition selected after inspecting Ω results.

Acceptable event examples:

```text
extreme price range
future earthquake above magnitude threshold
extreme precipitation
extreme daily count
activity burst or collapse defined directly from observed counts
```

Unacceptable event examples:

```text
event = Ω is high
event = I × G exceeds threshold
event = same variable and same threshold as Ω
event = manually selected cases after seeing Ω peaks
```

---

### 5.3 No tuning

The test must not tune:

- Ω definition,
- event threshold,
- time window,
- lead/lag window,
- domain subset,
- region subset,
- sample period,

in order to improve the ratio.

If multiple versions are explored, they must be treated as exploratory and separated from the default fixed test.

---

### 5.4 Minimum output

Each completed test should report at least:

```text
domain
data source
sample period
observable variable
I definition
G definition
Ω definition
high-Ω threshold
event / collapse definition
event timing rule
P(event | high Ω) / P(collapse | high Ω)
baseline P(event) / P(collapse)
ratio
n_total
n_high
n_event_total / n_collapse_total
n_event_high / n_collapse_high
```

Sparse-event cases should explicitly report event counts.

At minimum:

```text
n_high
n_event_high / n_collapse_high
```

---

### 5.5 Legacy threshold note

Some earlier or reproduction-specific results, especially in power-market tests, may have used domain-specific high-Ω thresholds or broader high-Ω regimes.

For new tests under this design map:

```text
q = 0.99 is the default execution standard.
```

Legacy results may be retained as historical, exploratory, or reproduction-specific records.

They should not redefine the current execution standard.

If a legacy result uses a threshold other than q = 0.99, it should be labeled as:

```text
legacy threshold
domain-specific threshold
exploratory threshold
or reproduction-specific threshold
```

It should not be mixed with new q = 0.99 minimal tests without explicit notation.

---

## 6. Theory Documents and Their Internal Roles

This section fixes how existing theory documents should be used during empirical work.

### 6.1 PureCore

Role:

```text
Internal structural core.
```

Use:

- defines layered internal structure,
- defines BYXCZ,
- defines forward flow,
- defines reverse flow,
- defines coherence and coherence flux,
- provides the cognitive/internal architecture of the theory.

Do not use PureCore as the direct empirical template for non-cognitive domains.

PureCore should not be expanded every time a new empirical test is added.

Empirical expansion should proceed through the Ω execution layer, not by modifying PureCore.

---

### 6.2 VOT

Role:

```text
Cross-domain directionality bridge.
```

Use:

- defines Ω as directionality potential,
- defines V = dΩ/dt,
- supports cross-domain projection,
- justifies why different domains can be tested using a common Ω-style structure.

VOT is the main theoretical bridge for empirical expansion.

When a new domain is considered, first ask whether it can be mapped to VOT-level directionality without requiring additional theory.

If the answer is no, the domain should be delayed.

---

### 6.3 Structural Overview

Role:

```text
Canonical whole-theory map.
```

Use:

- keeps the entire structure coherent,
- separates Natural-Ω and Civilizational-Ω,
- prevents empirical work from drifting into disconnected terminology,
- clarifies where empirical tests sit inside the broader framework.

The Structural Overview is a reference map, not an execution protocol.

It should not be modified in response to individual empirical results unless there is a genuine structural revision.

---

### 6.4 Civilizational Ω

Role:

```text
Future macro-scale extension.
```

Current empirical status:

```text
Excluded from near-term minimal Ω empirical expansion.
```

Civilizational Ω is theoretically part of the full framework.

However, it is excluded from near-term minimal empirical expansion because its operationalization requires:

- composite variables,
- long historical horizons,
- difficult independent event definitions,
- higher interpretive burden,
- larger risk of subjective proxy selection.

This is an empirical-priority decision.

It is not a theoretical rejection.

Civilizational Ω may become suitable for empirical testing only if the following are available:

```text
clear observable variables
stable public dataset
pre-defined independent event
sufficient sample size
minimal interpretation burden
reproducible code
```

Until then, Civilizational Ω should remain a macro-scale theoretical extension rather than a current reproducibility target.

---

### 6.5 Empirical Protocols

Role:

```text
Execution layer.
```

Use:

- define actual tests,
- specify variables,
- fix thresholds,
- provide reproducible code,
- report minimal outputs,
- separate fixed tests from exploratory checks.

The empirical protocol layer has priority over theoretical elaboration when running tests.

When an empirical test conflicts with a theoretical desire, preserve the empirical protocol and delay the theoretical extension.

---

## 7. Domain Screening Criteria

Before starting a new Ω test, evaluate the domain using the following criteria.

A domain is suitable if it has:

1. A time-indexed or ordered dataset.
2. A measurable observable variable.
3. A plausible dispersion or instability component.
4. A plausible directional change component.
5. An independently definable event / collapse outcome.
6. Enough observations for high-Ω conditioning.
7. A reproducible public or shareable data source.
8. Low risk of post-hoc definition.
9. Minimal interpretation burden.
10. No need to expand the theory before execution.

A domain should be delayed or excluded if:

1. The event cannot be defined independently from Ω.
2. The data are too sparse.
3. The observable variable is subjective or unstable.
4. The result requires complex interpretation before the minimal test is clear.
5. The test depends on private or non-reproducible data.
6. The theory must be expanded before the empirical design can be specified.
7. The result would be difficult to report without causal, predictive, or policy claims.

---

## 8. Standard Operational Structure

The default empirical structure is:

```text
I = structural dispersion or instability
G = directional change or movement
Ω = I × G
event / collapse = independently defined binary outcome
high Ω = Ω > q(0.99)
evaluation = P(event | high Ω) vs baseline P(event)
```

Equivalent formal output:

```text
P(collapse | high Ω)
P(collapse)
ratio = P(collapse | high Ω) / P(collapse)
```

This default should be used unless the domain clearly requires a different Ω form.

A different Ω form is allowed only if:

```text
it is specified before evaluation
it does not use the event definition
it is not chosen to improve the result
it is reported separately if exploratory
```

---

## 9. Domain Design Table

| Domain | Observable | I | G | Ω | Event / collapse | Default q | Status |
|---|---|---|---|---|---|---:|---|
| Finance | price / return | rolling volatility | absolute return or range movement | I × G | extreme price movement | 0.99 | suitable |
| Crypto | price / return | rolling volatility | absolute return or range movement | I × G | extreme price movement | 0.99 | suitable |
| Earthquakes | magnitude / event sequence | rolling magnitude dispersion | magnitude change | I × G | future event above magnitude threshold | 0.99 | suitable |
| Weather | precipitation / temperature | rolling dispersion | daily change | I × G | extreme precipitation or weather event | 0.99 | suitable |
| Traffic | daily count | rolling count dispersion | daily count change | I × G | extreme accident count | 0.99 | suitable |
| Power markets | price / load / regional spread | cross-sectional or temporal dispersion | deviation or price movement | defined equivalent | extreme price spike | 0.99 | suitable but may be sparse |
| Ecology | chlorophyll-a / population / biomass | rolling dispersion | temporal change | I × G | bloom, crash, or extreme shift | 0.99 | promising |
| Information systems | edits / commits / pageviews / activity counts | rolling dispersion | activity change | I × G | burst or collapse in activity | 0.99 | promising |
| Public health | case counts / hospitalization counts | rolling dispersion | count change | I × G | extreme surge | 0.99 | delay; requires careful framing |
| Civilization | composite institutional / information / technology variables | unresolved | unresolved | composite Ω_civ | regime collapse | unresolved | excluded from near-term expansion |

---

## 10. Priority Classification

### 10.1 Priority A: direct empirical expansion

Use these when the goal is to add reproducible tests quickly.

```text
finance
crypto
weather
traffic
earthquakes
power markets
```

These domains already fit the minimal Ω structure or have close precedents.

They are appropriate for strengthening reproducibility, adding regions, adding assets, or testing additional periods.

---

### 10.2 Priority B: promising but requires careful design

Use these when the goal is to expand topology without overcomplicating the theory.

```text
ecology
information systems
GitHub activity
Wikipedia activity
web traffic
search activity
```

These domains are useful because they test whether Ω works outside physical or market systems.

However, the event definition must be especially clear.

Priority B domains should not proceed until the event / collapse definition is fixed before evaluation.

---

### 10.3 Priority C: delay or exclude

Do not prioritize these unless a clean dataset and event definition are already available.

```text
civilizational collapse
AI-human co-directionality
large-scale historical transitions
political regime change
cultural transformation
public health
```

Reason:

These domains are theoretically important but empirically heavy.

They risk shifting the project from minimal reproducible concentration tests into broad interpretive modeling.

---

## 11. Event Definition Rules by Domain Type

### 11.1 Continuous time-series domains

Examples:

```text
finance
crypto
weather
traffic
ecology
information activity
```

Preferred event definition:

```text
event = observed value exceeds a pre-defined quantile or fixed threshold
```

Examples:

```text
daily range > q(0.95)
precipitation > q(0.95)
daily count > q(0.95)
activity change > q(0.95)
```

The event threshold must be fixed before evaluation.

The event threshold must not be identical to the high-Ω threshold unless independently justified.

---

### 11.2 Event-sequence domains

Examples:

```text
earthquakes
incidents
failures
outages
```

Preferred event definition:

```text
event = future occurrence of an independently defined event within a fixed window
```

Examples:

```text
M >= 5.5 within next 3 hours
outage within next 6 hours
incident count exceeds threshold within next day
```

The future window must be fixed before evaluation.

The future window must not be changed after seeing high-Ω results.

---

### 11.3 Cross-sectional domains

Examples:

```text
power markets
regional systems
multi-zone networks
```

Preferred Ω structure:

```text
I = cross-sectional dispersion
G = directional deviation from system baseline
Ω = I × G or defined equivalent
```

Preferred event definition:

```text
event = independently defined extreme system outcome
```

Example:

```text
regional price spike
extreme price ratio
system stress event
```

Cross-sectional tests may require domain-specific Ω construction.

If so, the construction must be fixed before evaluation and reported separately from standard I × G time-series tests.

---

## 12. Result Classification

Each test result should be classified internally as one of the following.

### 12.1 Positive concentration

```text
P(event | high Ω) > baseline P(event)
```

Equivalent:

```text
P(collapse | high Ω) > P(collapse)
```

Interpretation:

Independently defined events occur more frequently under high-Ω conditions than at baseline.

This supports the minimal structural concentration claim for that domain and operationalization.

---

### 12.2 Null

```text
P(event | high Ω) ≈ baseline P(event)
```

Equivalent:

```text
P(collapse | high Ω) ≈ P(collapse)
```

Interpretation:

The test does not show meaningful concentration under the fixed operationalization.

This is still a valid result.

It should not trigger post-hoc changes to Ω, event definitions, thresholds, windows, or sample periods.

---

### 12.3 Negative or inverse

```text
P(event | high Ω) < baseline P(event)
```

Equivalent:

```text
P(collapse | high Ω) < P(collapse)
```

Interpretation:

Events are less frequent under high-Ω conditions than at baseline.

This is still a valid result.

It should be reported as evidence against the tested operationalization, not corrected after the fact.

---

### 12.4 Sparse

```text
n_high or n_event_high is too small for stable interpretation
```

Equivalent:

```text
n_high or n_collapse_high is too small for stable interpretation
```

Interpretation:

The result may be directionally informative but should not be overemphasized.

Sparse results may be kept for internal comparison, but they should be clearly marked.

Sparse results should always report:

```text
n_total
n_high
n_event_total / n_collapse_total
n_event_high / n_collapse_high
```

---

### 12.5 Rule for all result classes

A null, negative, inverse, or sparse result must not trigger post-hoc changes to:

- Ω definition,
- I definition,
- G definition,
- event / collapse definition,
- threshold,
- sample period,
- lead/lag window,
- domain subset,
- reporting language.

Exploratory follow-up tests are allowed only if clearly separated from the fixed minimal test.

---

## 13. Exclusion Rules

A candidate test should be rejected or postponed if any of the following apply.

### 13.1 Event circularity

Reject if:

```text
event is mathematically derived from Ω
```

or:

```text
event is selected because it overlaps with high Ω
```

or:

```text
event uses Ω, I, G, or the high-Ω threshold
```

---

### 13.2 Too few high-Ω cases

Postpone or report as sparse if:

```text
n_high is too small for meaningful interpretation
```

Sparse results may still be reported, but they should not be overemphasized.

---

### 13.3 Too much theory required

Reject or postpone if:

```text
the empirical test requires new theory before variables can be defined
```

The current empirical layer should not depend on new metaphysical, cognitive, or civilizational claims.

---

### 13.4 Non-reproducible data

Reject for public empirical use if:

```text
the dataset cannot be shared, accessed, or reproduced
```

Private exploratory checks may be kept separate.

---

### 13.5 Ambiguous observable

Reject or postpone if:

```text
the main variable cannot be measured consistently
```

Examples:

```text
social mood
civilizational meaning
institutional health
collective anxiety
```

These may be theoretically relevant but are not suitable for minimal Ω tests unless converted into stable observable proxies.

---

### 13.6 Policy-heavy interpretation

Delay if the result would be difficult to report without implying:

```text
prediction
causality
intervention
policy recommendation
risk scoring
individual or group diagnosis
```

This does not make the domain invalid.

It means the domain is not suitable for near-term minimal Ω empirical expansion.

---

## 14. Internal Decision Procedure

Before starting a new test, answer the following questions.

```text
1. What is the domain?
2. What is the observable variable?
3. What is I?
4. What is G?
5. What is Ω?
6. What is the independent event / collapse outcome?
7. Is the event definition independent from Ω, I, G, and the high-Ω threshold?
8. What is the high-Ω threshold?
9. Is q = 0.99 used for the default minimal test?
10. What is the baseline event / collapse rate?
11. Is the dataset reproducible?
12. Is the sample size sufficient?
13. Is n_high sufficient?
14. Is n_event_high / n_collapse_high reported?
15. Is the result interpretable without adding new theory?
```

If any answer is unclear, the test should not move to public reporting.

---

## 15. Internal Go / Delay / Reject Rule

### 15.1 Go

Proceed if:

```text
observable is clear
I is clear
G is clear
Ω is fixed before evaluation
event / collapse is independent
q = 0.99 is used for the default minimal test
data are reproducible
sample size is acceptable
minimal output can be produced
```

---

### 15.2 Delay

Delay if:

```text
domain is promising
but event definition is not yet stable
or data source is not yet fixed
or sample size may be insufficient
or result interpretation would require too much theory
```

---

### 15.3 Reject

Reject if:

```text
event is circular
data are not reproducible
variables are subjective
test requires new theory
result cannot be interpreted minimally
```

---

## 16. Relationship to Existing Results

Existing results should be treated as demonstrations of the minimal comparison:

```text
P(event | high Ω)
vs
baseline P(event)
```

Equivalent:

```text
P(collapse | high Ω)
vs
P(collapse)
```

They should not be treated as proof of the full theory.

Each domain result supports only the following limited statement:

```text
In this domain, under this fixed operationalization,
independently defined events concentrate more strongly in high-Ω states than at baseline.
```

This statement should remain separate from broader theoretical interpretation.

Legacy or exploratory results may remain useful, but they must not override the current minimal standard.

---

## 17. Preferred Next Empirical Directions

The preferred next directions are:

```text
1. Strengthen existing domain summaries.
2. Add one or two topology-expanding domains.
3. Prefer domains with simple public datasets.
4. Avoid civilization-scale tests for now.
5. Avoid theory-heavy domains until the empirical layer is more stable.
```

Recommended near-term candidates:

```text
ecology
GitHub activity
Wikipedia activity
additional weather locations
additional traffic regions
additional finance assets
additional power-market regions
```

The best next test is not necessarily the most theoretically interesting one.

The best next test is the one with:

```text
clear data
clear event / collapse definition
clear Ω
q = 0.99 default threshold
low circularity risk
easy reproducibility
minimal interpretation burden
```

---

## 18. Stability Principle

When empirical and theoretical priorities conflict, empirical stability has priority.

That means:

```text
do not expand the theory to fit a dataset
do not adjust Ω to improve a result
do not redefine events after seeing high-Ω states
do not change thresholds after seeing outcomes
do not add interpretive claims before the minimal comparison is stable
```

The theory can remain broad.

The empirical test must remain narrow.

---

## 19. Minimal Completion Standard for a New Test

A new test is complete when it has:

```text
1. fixed domain
2. fixed dataset
3. fixed observable
4. fixed I
5. fixed G
6. fixed Ω
7. fixed high-Ω threshold q = 0.99
8. fixed independent event / collapse definition
9. reproducible code
10. minimal result table
11. event-count reporting
12. short interpretation
13. explicit claim boundary
```

If these thirteen items are present, the test is complete enough for internal comparison.

---

## 20. Claim Boundary Template

Use the following boundary statement when summarizing any result.

```text
This test evaluates structural concentration only.

It asks whether independently defined events occur more frequently under high-Ω conditions than at baseline.

It does not claim prediction, causality, optimization, intervention, or full validation of the theory.
```

Alternative version using the formal minimal terminology:

```text
This test evaluates structural concentration only.

It asks whether independently defined collapse outcomes occur more frequently under high-Ω conditions than at baseline.

It does not claim prediction, causality, optimization, intervention, or full validation of the theory.
```

---

## 21. Final Internal Rule

The purpose of empirical expansion is not to prove everything.

The purpose is to test whether the same minimal structural concentration pattern appears across domains under fixed, reproducible, non-circular definitions.

If a domain cannot be reduced to this structure, it should be delayed or excluded.

If a domain can be reduced to this structure, it may be tested.

If the result is null, negative, inverse, or sparse, the result is still valid.

The empirical layer should remain narrower than the theory.

---

End of document.
