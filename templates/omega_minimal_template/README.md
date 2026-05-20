# Minimal Ω Structural Concentration Template

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/onsenojisan/omega-repro/blob/main/templates/omega_minimal_template/omega_minimal_template.ipynb)

This is a tiny Google Colab template for testing whether independently defined binary events concentrate in high-Ω states.

It is a structural concentration test, not a prediction model. Ω is computed only from the selected value column:

- `I = rolling standard deviation(value, window=20)`
- `G = absolute first difference(value)`
- `Ω = I * G`

The event or collapse column must be defined independently from Ω. Do not tune the threshold, window, or event definition after seeing the result.

Null results are valid. A ratio near 1 means the event did not concentrate in high-Ω states under this simple test.

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
- `README.md` - this guide
