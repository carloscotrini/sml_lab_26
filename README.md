# Regression Autopsy: Eight Ways Your Model Is Lying to You

Regression is the most dangerous tool in data science. Not because it doesn't work — because it almost works. It gives you a number, a confidence interval, a p-value, and a clean summary table. Everything looks authoritative. And in most observational analyses, the number is wrong. This series of notebooks will show you exactly how, exactly why, and exactly what to do about it.

## Notebooks

| # | Notebook | Core Concept | One-Line Description |
|---|----------|--------------|----------------------|
| 1 | [Why Your Coefficient Is Wrong](notebooks/01_coefficient.ipynb) | Omitted variable bias | How leaving out a single variable can silently shift your estimate in one direction. |
| 2 | [Why Your Uncertainty Is Wrong](notebooks/02_uncertainty.ipynb) | Heteroscedasticity and standard errors | Why your confidence intervals are too narrow and your p-values are too small. |
| 3 | [Why Your Significance Is Wrong](notebooks/03_significance.ipynb) | Statistical vs. effect size and power | The difference between a statistically significant result and one that matters. |
| 1.5 | [(Optional) What "Controlling For" Actually Means](notebooks/01b_controlling_for.ipynb) | Frisch-Waugh-Lovell theorem | The mechanical truth behind "holding constant" and partial regression. |
| 4 | [Why Your Model Is Wrong](notebooks/04_specification.ipynb) | Specification error and extrapolation | What happens when the real relationship is nothing like the one you assumed. |
| 5 | [Why Your R² Is Lying](notebooks/05_overfitting.ipynb) | Overfitting and bias-variance tradeoff | Why a high R² can mean your model is memorizing noise. |
| 6 | [Why Your Causal Claim Is Wrong](notebooks/06_causation.ipynb) | Endogeneity and instrumental variables | The gap between prediction and causation, and one way to close it. |
| 7 | [The Real World](notebooks/07_real_world.ipynb) | Confronting real data with all pathologies | A single messy dataset where every problem from the course shows up at once. |
| 8 | [The Redemption](notebooks/08_redemption.ipynb) | Regression discontinuity design | When regression actually can identify causal effects — and why the design matters. |

## Getting Started

Click any notebook badge to open directly in Google Colab. No installation needed. Each notebook is self-contained.

| Notebook | Colab Link |
|----------|------------|
| NB1 — Why Your Coefficient Is Wrong | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/[REPO]/blob/main/notebooks/01_coefficient.ipynb) |
| NB2 — Why Your Uncertainty Is Wrong | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/[REPO]/blob/main/notebooks/02_uncertainty.ipynb) |
| NB3 — Why Your Significance Is Wrong | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/[REPO]/blob/main/notebooks/03_significance.ipynb) |
| NB1.5 — What "Controlling For" Actually Means (Optional) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/[REPO]/blob/main/notebooks/01b_controlling_for.ipynb) |
| NB4 — Why Your Model Is Wrong | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/[REPO]/blob/main/notebooks/04_specification.ipynb) |
| NB5 — Why Your R² Is Lying | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/[REPO]/blob/main/notebooks/05_overfitting.ipynb) |
| NB6 — Why Your Causal Claim Is Wrong | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/[REPO]/blob/main/notebooks/06_causation.ipynb) |
| NB7 — The Real World | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/[REPO]/blob/main/notebooks/07_real_world.ipynb) |
| NB8 — The Redemption | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/[REPO]/blob/main/notebooks/08_redemption.ipynb) |

## Prerequisites

Basic familiarity with Python and statistics. No econometrics background needed.

## Contributing

### How to add new disaster sidebars

Each disaster sidebar is a collapsed cell within a notebook, structured with three tabs:

1. **The Story** — A real-world narrative that motivates the pathology.
2. **The Math** — A concise formal treatment of why the problem arises.
3. **The Simulation** — A runnable mini-simulation triggered by a single button.

Sidebars use 60% saturation of the main palette colors to visually distinguish them from the primary notebook content while remaining consistent with the overall design.

When adding a new sidebar:

- Follow the three-tab structure (The Story, The Math, The Simulation) exactly.
- Use 60% saturation of the notebook's main palette colors for sidebar styling.
- Ensure the simulation runs end-to-end from a single button click with no external dependencies.
- Place the sidebar in the relevant notebook, immediately after the section it illustrates.
- Keep the cell collapsed by default so it does not interrupt the main narrative flow.

## License

License TBD
