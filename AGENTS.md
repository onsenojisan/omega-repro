# Agent Instructions

> Maintenance note: This file contains repository operation guidance for AI/code agents. It is public for transparency, but it is not the ordinary reader path. Ordinary readers should start with `README.md` or the Ω Library execution hub.

## 1. Repository Purpose

This repository supports reproducible Omega structural concentration tests.

It is not a prediction, trading, optimization, or causal-inference framework. Do not reframe the repository, outputs, notebooks, reports, or documentation in those terms.

## 2. Reproducibility-First Policy

- Preserve fixed ex-ante definitions.
- Preserve event definitions that are independent from Omega measurements.
- Report only:
  - `P(event | high Omega)`
  - baseline `P(event)`
  - ratio
  - relevant counts
- Do not add post-hoc tuning.
- Do not optimize parameters to improve results.
- Treat null results as valid outcomes.

## 3. Structural Stability Policy

- Preserve role separation between canonical, executable, interpretive, and reference artifacts.
- Avoid excessive cross-linking.
- Avoid topology expansion without structural necessity.
- Leave intentional isolated or weakly linked reference artifacts isolated when structurally appropriate.
- Do not add links merely to silence validator warnings.

## 4. Change Discipline

- Do not change Omega definitions, thresholds, event definitions, domain specifications, or output semantics without explicit approval.
- Do not silently modify notebooks or reported metrics.
- Do not introduce new empirical domains unless explicitly requested.
- Do not convert the repository into a prediction, optimization, intervention, or trading framework.
- Prefer review documents before edits.
- Prefer the smallest safe change.

## 5. Public-Facing Stability

- Keep README entry paths stable.
- Preserve Colab reproducibility paths.
- Preserve Zenodo reference consistency.
- Preserve report-template accessibility.
- Prefer minimal and stable public navigation.

## 6. Agent Workflow

- First inspect git status and recent commits.
- Classify findings as:
  - required fix
  - optional improvement
  - no action
- Explain any public-facing impact before modification.
- Avoid unnecessary refactors.
- Never commit or push unless explicitly instructed.

## 7. Prohibited Actions

- Threshold optimization.
- Post-hoc fitting.
- Prediction framing.
- Causal claims.
- Trading-strategy framing.
- Automatic domain expansion.
- Silent output changes.
- Large structural rewrites without approval.
