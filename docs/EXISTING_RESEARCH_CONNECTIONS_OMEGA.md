# Structural Concentration and Existing Research Terminology

This document is a terminology bridge and positioning guide, not a literature review or unification claim.

This note describes how the minimal Ω structural concentration framework can be named alongside existing research language. It is not a theory paper and does not claim that Ω subsumes, explains, or replaces existing research fields.

Ω evaluates whether pre-defined structural concentration measures change around independently defined collapse or event states. It evaluates structural concentration, not timing prediction. It does not establish causality, and null results are valid outcomes.

All definitions should be fixed ex-ante. Collapse or event definitions must be independent from Ω measurements so that the protocol does not define the target state using the same quantity it later evaluates.

| Existing research language | Typical focus | Ω minimal protocol focus | Relationship / distinction |
| --- | --- | --- | --- |
| Forecasting / prediction | Estimating future values, events, or event timing | Comparing pre-defined structural concentration measures across independently defined states | Ω is not a timing-prediction protocol and should not be presented as a forecast model. |
| Anomaly detection | Identifying observations that depart from expected patterns | Testing whether concentration differs in event-adjacent or state-conditioned windows | Ω can be used near anomaly workflows, but it does not define anomalies by itself. |
| Extreme value theory | Modeling tail behavior and rare extremes | Evaluating whether structural concentration is elevated or altered around independently defined extremes | Ω does not replace tail modeling; it reports a separate structural comparison. |
| Volatility clustering | Persistence or grouping of high-variance periods | Measuring concentration structure under fixed window and event definitions | Ω may be compared with volatility patterns, but concentration is not the same as volatility. |
| Regime transitions | Changes between market, system, or process states | Comparing concentration across pre-labeled regimes or transition windows | Ω requires regime labels or rules to be specified outside the Ω measure. |
| Critical transitions | System shifts associated with loss of resilience or threshold effects | Checking whether structural concentration changes before or during independently defined transition states | Ω does not prove a critical mechanism or universal transition law. |
| Early warning signals | Indicators that may precede a transition or failure | Describing ex-ante concentration behavior before independently defined events | Ω may be reported alongside warning indicators, but it is not itself a universal warning signal. |
| Stress regimes | Periods of elevated strain, instability, or disruption | Evaluating concentration under pre-defined stress and non-stress states | Ω depends on external stress definitions and does not validate the stress label causally. |
| Conditional probability / state conditioning | Estimating probabilities or distributions conditional on state variables | Conditioning Ω summaries on pre-defined states, windows, or event classes | Ω can be reported within state-conditioned analysis, but it is a measurement protocol rather than a probability model. |
| Reproducibility / minimal protocols | Fixed definitions, auditable inputs, and repeatable procedures | Using a minimal CSV format, explicit definitions, and transparent null-result reporting | Ω is designed to support reproducible comparison, not to replace richer domain-specific methods. |

## Use With

- Minimal CSV Template: https://zenodo.org/records/20309117
- Reproducibility Package: https://zenodo.org/records/19159664
- Canonical Structural Overview: https://zenodo.org/records/18296691

## Suggested Use

Use this note as a lightweight connection layer when introducing Ω to readers who already know related terminology. It should help prevent overclaiming by making the protocol boundaries explicit: fixed definitions, independent event labels, no causal claim, no replacement of existing methods, and valid null results.

The purpose is only to reduce interpretation friction across existing research communities.
