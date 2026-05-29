# Exploratory Omega Sensitivity / Design-Space Scan

This document describes a separate exploratory scan for checking whether the event concentration comparison remains stable across nearby Omega definitions, rolling windows, high-Omega thresholds, and lead settings.

It is not part of the fixed minimal protocol. It does not replace the Minimal Standard Form, select a new official Omega definition, optimize thresholds, or turn a tuned result into confirmatory evidence.

## Why It Is Separate

The fixed minimal protocol keeps definitions fixed before looking at results. This scan intentionally varies nearby specifications, so it must be treated as exploratory design-space inspection only.

The scan asks:

`P(event | high score) > baseline P(event)`

across a predefined grid. The main output is robustness across that grid, not the single best ratio.

## Input CSV

The script expects a CSV with at least:

- `time`
- `value`
- `event`

`value` must be numeric. `event` must be binary or convertible to `0/1`. The event column is treated as independently defined by the user; the script does not redefine event from value.

Rows are sorted by the `time` column before rolling-window, first-difference, and lead calculations.

## Scan Space

The predefined scan uses:

- rolling windows: `5, 10, 20, 30, 60`
- high-score quantiles: `0.90, 0.95, 0.975, 0.99`
- lead settings: `0, 1, 3, 5` rows
- score types: `omega_product`, `I_only`, `G_only`, `omega_product_z`

Definitions:

- `I = rolling standard deviation(value, window)`
- `G = absolute first difference(value)`
- `omega_product = I * G`
- `I_only = I`
- `G_only = G`
- `omega_product_z = z(I) * z(G)`, when stable and well-defined
- high score means `score >= quantile(score, q)`

For `lead > 0`, row `t` is evaluated against `event` at `t + lead`. These lead results are exploratory and must not be described as predictive evidence.

## How To Run

From the repository root:

```powershell
python scripts\omega_sensitivity_scan.py templates\omega_minimal_template\example_data.csv
```

Optional arguments:

```powershell
python scripts\omega_sensitivity_scan.py path\to\data.csv --output-dir outputs --domain "my-domain"
```

The default output files are:

- `outputs/sensitivity_scan_results.csv`
- `outputs/sensitivity_scan_summary.md`

## CSV Output

Each scanned specification is retained, including weak, sparse, and invalid rows. The CSV columns are:

- `domain_or_file`
- `score_type`
- `rolling_window`
- `high_quantile`
- `lead`
- `n_rows_valid`
- `n_events`
- `baseline_p_event`
- `n_high`
- `n_event_high`
- `p_event_given_high`
- `ratio`
- `above_baseline`
- `reliability_flag`

Reliability flags:

- `ok`: `n_high >= 10` and `n_event_high >= 3`
- `sparse_high`: `n_high < 10`
- `sparse_event_high`: `n_event_high < 3`
- `no_events`: `n_events == 0`
- `invalid`: cannot compute

## Markdown Summary

The summary reports:

- total scanned specifications
- percentage where `P(event | high score) > baseline P(event)`
- median ratio by score type, rolling window, high quantile, and lead
- best ratio, clearly labelled exploratory
- stable regions and failure regions, if any
- omega product comparison against `I_only` and `G_only`
- warnings about sparse counts, narrow parameter dependence, and lead interpretation

## Interpretation Rules

Do not use this scan as post-hoc confirmation. The best single result is not the main result. Stability across nearby specifications matters more than the maximum ratio.

If `omega_product` is not better than `I_only` or `G_only`, state that clearly. If results depend on one narrow parameter choice, state that clearly. If event counts are sparse, state that clearly. If contemporaneous `lead=0` is stable but forward leads are unstable, state that clearly.
