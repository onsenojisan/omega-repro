# Future Source-Consistent Domain Checklist

This checklist is a maintenance-facing gate for future explicitly approved source-consistent domain work. It is not a new analysis, not approval to add a domain, and not a public result.

The only claim boundary is structural concentration:

`P(event | high Ω)` versus baseline `P(event)`

Event definitions must be independent from Ω. Null, weak, sparse, or near-baseline outcomes are valid and must be reported and flagged rather than hidden.

## Before Any Rerun

* [ ] Domain addition or review scope was explicitly approved.
* [ ] Fixed source artifact is saved or the external dependency is pinned and documented.
* [ ] Fixed time range is documented.
* [ ] Fixed value variable is documented.
* [ ] Fixed event definition is documented and independent from Ω.
* [ ] Fixed Ω definition is documented.
* [ ] Fixed high-Ω threshold is documented.
* [ ] No threshold optimization was performed.
* [ ] No post-hoc parameter tuning was performed.
* [ ] Source intake note is saved.

## Before Public Registry Consideration

* [ ] Rerun command is documented.
* [ ] Script path is documented.
* [ ] Fixed input artifact path is documented.
* [ ] Output artifact path is documented.
* [ ] `P(event | high Ω)` is reported.
* [ ] Baseline `P(event)` is reported.
* [ ] Ratio is reported when defined.
* [ ] `n_rows` is reported.
* [ ] `n_high` is reported.
* [ ] `n_event_high` is reported.
* [ ] Sparse, weak, null, unstable, or source-limited caveats are visible.
* [ ] Control or caveat note is saved if needed.
* [ ] Claim boundary is structural concentration only.
* [ ] Result is classified as public registry candidate, internal maintenance only, or deferred.

## Not Allowed

* prediction claim
* causality claim
* optimization claim
* trading-strategy claim
* intervention claim
* forecasting claim
* earthquake early-warning claim
* universal physical-law proof
* suppressing null, weak, sparse, or near-baseline results
