# Minimal Template Smoke-Test Result

This file records the expected output format for running `omega_minimal_template.ipynb` with `example_data.csv`.

This is a template smoke test only. It is not empirical evidence, not a public domain result, and not part of the public result registry.

Users should replace `example_data.csv` with their own data containing a numeric value column and an independently defined binary event column. Null, weak, sparse, or near-baseline outputs are valid results under the protocol.

## Fixed Inputs

- CSV: `example_data.csv`
- value column: `value`
- time/order column: `time`
- event column: `event`
- rolling window: `20`
- high Omega: top `1%`

## Expected Copy/Paste Block

```text
Domain: omega_minimal_template/example_data.csv
P(event | high Omega): 1
Baseline P(event): 0.363636
Ratio: 2.75
n_rows: 11
n_high: 1
n_event_high: 1
```

## Verification Notes

These values are computed from the fixed notebook logic: `I = rolling standard deviation(value, window=20)`, `G = absolute first difference(value)`, `Omega = I * G`, and high Omega as rows with `Omega >= q(0.99)` among valid rows.

The sample has a sparse high-Omega tail (`n_high = 1`), which is acceptable for a smoke test but should not be read as empirical evidence.

## Claim Boundary

This smoke test demonstrates notebook mechanics only. It does not claim prediction, causality, optimization, trading value, intervention value, forecasting, or early-warning capability.
