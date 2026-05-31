# Weather Source-Consistent Fixed-Scope Plan

This is a maintenance-facing fixed-scope preparation note for a possible future weather/environmental source-consistent Omega structural concentration test.

This is not a new result. It is not approval to add the domain. It is not a public registry row. It does not authorize data download, execution, analysis, metric changes, registry changes, or public promotion.

The only claim boundary is structural concentration:

`P(event | high Ω)` versus baseline `P(event)`

Event definitions must be independent from Ω. Null, weak, sparse, unstable, or near-baseline outcomes must be accepted and flagged rather than hidden.

## Fixed Candidate Scope

| Field | Fixed plan |
| --- | --- |
| domain | Weather/environmental |
| location | London, United Kingdom |
| coordinates | latitude `51.5072`, longitude `-0.1276` |
| public archive source | Open-Meteo Archive API, `https://archive-api.open-meteo.com/v1/archive` |
| source query | `latitude=51.5072`, `longitude=-0.1276`, `start_date=2015-01-01`, `end_date=2024-12-31`, `daily=precipitation_sum`, `timezone=UTC` |
| fixed time range | `2015-01-01` through `2024-12-31`, inclusive |
| value variable | daily precipitation, `precipitation_sum`, in millimeters |
| row unit | one UTC calendar day |
| zero values | retain observed zero-precipitation days |
| missing values | block the future run and document the issue; do not impute after inspection |

## Fixed Omega And Event Definitions

| Component | Fixed definition |
| --- | --- |
| `I` | rolling sample standard deviation of daily precipitation, window `30` days |
| `G` | absolute first difference of daily precipitation |
| `Omega` | `I * G` |
| high Omega | `Omega > q(0.99)` computed on valid analysis rows |
| event | daily precipitation `> q(0.95)` computed from raw daily precipitation on valid analysis rows |
| event timing | contemporaneous: `event_t` compared with `high_Omega_t` |
| independence rule | event is defined from raw daily precipitation only, not from Omega, `I`, `G`, high-Omega membership, or result inspection |

No threshold, rolling window, event definition, time range, location, source, or timing rule may be changed after seeing data or results.

## Required Future Artifact Paths

These paths are required only if a future task explicitly approves source-consistent weather execution.

| Artifact type | Required path |
| --- | --- |
| fixed source artifact | `source_consistent_three_domain/data/weather_london_open_meteo_precipitation_2015-01-01_2024-12-31.csv` |
| source intake note | `source_consistent_three_domain/docs/source_intake/WEATHER_LONDON_OPEN_METEO_INTAKE.md` |
| rerun script | `source_consistent_three_domain/scripts/weather_london_source_consistent_v1_rerun.py` |
| original result CSV | `source_consistent_three_domain/results/weather_london_source_consistent_v1_original.csv` |
| summary result JSON | `source_consistent_three_domain/results/weather_london_source_consistent_v1_summary.json` |
| control or caveat note | `source_consistent_three_domain/docs/control/WEATHER_LONDON_SOURCE_CONSISTENT_V1_RERUN.md` |

## Required Future Output Fields

Any future result must report:

* domain
* location
* data source
* fixed time range
* value variable
* Omega definition
* event definition
* high-Omega threshold
* `P(event | high Ω)`
* baseline `P(event)`
* ratio, when defined
* `n_rows`
* `n_high`
* `n_event_high`
* reliability or caveat flag
* rerun command
* output artifact path

Sparse, weak, null, unstable, or near-baseline outcomes are valid outcomes and must remain visible in any future note or registry review.

## Required Future Rerun Command

If a future task explicitly approves execution, the planned rerun command should be:

```powershell
cd source_consistent_three_domain
python scripts/weather_london_source_consistent_v1_rerun.py
```

This command is a planned interface only. This file does not create the script and does not run the analysis.

## Claim Boundary

This plan preserves structural concentration only:

`P(event | high Ω)` versus baseline `P(event)`

This plan does not claim prediction, forecasting, climate-warning capability, causality, optimization, trading value, intervention value, early-warning capability, operational guidance, risk scoring, or proof of a universal physical law.

Any future public-registry consideration must satisfy `source_consistent_three_domain/docs/FUTURE_SOURCE_CONSISTENT_DOMAIN_CHECKLIST.md` before a row is proposed.
