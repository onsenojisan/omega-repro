# Minimal Ω Structural Concentration Template

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/onsenojisan/omega-repro/blob/main/templates/omega_minimal_template/omega_minimal_template.ipynb)

This is a historical V1 executable comparison illustrating `P(event | high Ω)` versus baseline `P(event)`. It is not a validation tool for Ω. Meaningful future use requires an independently defined event label, frozen definitions, and anti-circularity checks.

It is a structural concentration comparison, not a prediction model. Ω is computed only from the selected value column:

- `I = rolling standard deviation(value, window=20)`
- `G = absolute first difference(value)`
- `Ω = I * G`

The event or collapse column must be defined independently from Ω. Do not tune the threshold, window, or event definition after seeing the result.

Null results are valid. A ratio near 1 means the event did not concentrate in high-Ω states under this simple historical V1 comparison. A high ratio alone is not evidence.

## Colab-Ready Usage

1. Open `omega_minimal_template.ipynb` in Google Colab.
2. Run the cells.
3. Upload your CSV when prompted, or upload `example_data.csv` to test immediately.
4. Select:
   - value column
   - optional time/order column
   - binary event column
5. Copy the final result block into your notes or report.

## Files

- `omega_minimal_template.ipynb` - minimal Colab notebook
- `example_data.csv` - tiny example dataset
- `example_result.md` - smoke-test output format for the bundled sample CSV; not empirical evidence
- `README.md` - this guide

`example_data.csv` is the repository copy of the Zenodo sample file `omega_minimal_sample.csv`.
