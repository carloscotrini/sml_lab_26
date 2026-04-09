---
title: "Regression Autopsy: Eight Ways Your Model Is Lying to You"
subtitle: "Complete Build Specification — For Implementation by Claude Code"
author: "Confidential Build Document"
date: "Version 1.0 | March 2026"
---

# REGRESSION AUTOPSY

## Eight Ways Your Model Is Lying to You

**Complete Build Specification**

**For Implementation by Claude Code**

---

**CONFIDENTIAL BUILD DOCUMENT**

Version 1.0 | March 2026

---

# 1. Course Overview & Core Promise

> *Regression is the most dangerous tool in data science. Not because it doesn't work — because it almost works. It gives you a number, a confidence interval, a p-value, and a clean summary table. Everything looks authoritative. And in most observational analyses, the number is wrong. This series of notebooks will show you exactly how, exactly why, and exactly what to do about it.*

**Course Title:** Regression Autopsy: Eight Ways Your Model Is Lying to You

**Format:** Eight core interactive Colab notebooks + one optional deep dive

**Core Promise:** By the end of this course, you will never blindly trust a regression again — and you'll know exactly when you should trust one.

**Emotional Arc:** Trust → Betrayal → Understanding → Mastery → Redemption

The student begins by trusting regression blindly (Notebook 1), gets burned six different ways (Notebooks 1–6), learns to diagnose and mitigate each problem, confronts the limits of mitigation with real data (Notebook 7), and discovers that regression can be trustworthy when paired with a research design that earns that trust (Notebook 8).

**Opening Framing (displayed in Notebook 1, Cell 0):** "You'll work with one company's data across eight notebooks. Each notebook will ask you to make a judgment. Each time, you'll be wrong — but in a precisely predictable way. By the end, you'll understand not just how to run a regression, but when to trust one."

# 2. Target Audience

**Primary:** Anyone who runs regressions without formal econometrics training — data analysts at startups, product managers interpreting A/B tests, policy researchers, journalists, engineers.

**Secondary:** Instructors who want a ready-made module for statistics, econometrics, or data science courses.

## Language Principles

- Lead with the consequence, not the mechanism. "Your number is too big, here's why" before the formula.
- Theorem names appear in footnotes or collapsible cells, never in the main narrative flow.
- Every concept has a one-sentence version before the formal version.
- The insight is complete without the math. The math is there for those who want it.

# 3. Pedagogical Framework

## 3.1 The Six-Beat Structure

Every notebook follows the same six-beat arc. This consistency builds familiarity — by Notebook 3, the student knows the rhythm and can focus on the content rather than the structure.

| Beat | Name      | Purpose                                                        | Student Experience                   |
|------|-----------|----------------------------------------------------------------|---------------------------------------|
| 1    | Trap      | Student commits to a wrong answer via interactive widget       | Confidence: "I know this"             |
| 2    | Reveal    | One visualization exposes the problem                          | Shock: "Wait, what?"                  |
| 3    | Formalize | Theorem stated in LaTeX, confirmed by Monte Carlo simulation   | Understanding: "Oh, that's why"       |
| 4    | Destroy   | Interactive sliders let the student control violation severity | Exploration: "What happens if..."     |
| 5    | Repair    | Toggle activates the fix, side by side with the broken version | Relief: "There's a solution"          |
| 6    | Limit     | Second slider finds the boundary where the repair fails        | Wisdom: "But it's not a silver bullet"|

## 3.2 The Trap Widget System

The trap is the most critical element. Its purpose is to make the student commit to an answer before being corrected. This commitment is what makes the correction memorable.

**Design Requirements for Traps**

- Use ipywidgets radio buttons or checkboxes, not free text, so responses are machine-readable.
- Include a Submit button. The next cell's output is gated until submission.
- Traps must be hard enough to catch experienced practitioners, not just beginners. For example: ask the direction of bias, not just whether bias exists.
- Record the student's response in a JSON file for the final dashboard in Notebook 8.
- Gate system is pure Python (ipywidgets), no JavaScript injection. Must work in Colab, Jupyter, JupyterLab, and VS Code.

## 3.3 Recurring Dataset

All eight notebooks use the same housing dataset and the same variables. The student builds a relationship with this data across notebooks. When a coefficient changes from one notebook to the next, they remember the old value. The recurring dataset creates emotional continuity that isolated examples cannot.

## 3.4 Discussion Prompts

After each Destroy beat, a markdown cell poses a discussion question designed to provoke argument between two students or serve as a reflective prompt for solo learners. These have no single correct answer — they surface the judgment that statistics requires beyond mechanics.

## 3.5 Lingering Questions & Transition Cards

Each notebook ends with a lingering question that the next notebook answers, plus a styled HTML card with a one-click Colab link to the next notebook. This is the Netflix-style "next episode" prompt delivered at the moment of maximum engagement.

# 4. Visual Design System

## 4.1 Color Palette

Consistent across all eight notebooks. No exceptions. No notebook-specific color schemes.

| Color | Hex     | Meaning                | Usage                                                   |
|-------|---------|------------------------|---------------------------------------------------------|
| Blue  | #2E5EA8 | OLS estimator          | OLS distribution, regression line, OLS confidence intervals |
| Gold  | #D4A017 | Truth                  | True parameter value (vertical line), true DGP          |
| Red   | #C0392B | Bias / Violation / Error | Biased distributions, violated assumptions, missed CIs |
| Green | #27AE60 | Repair working         | Corrected estimator, restored coverage                  |
| Gray  | #7F8C8D | Alternative estimators | Non-OLS estimators in Gauss-Markov comparisons          |

## 4.2 Accessibility: Secondary Visual Channels

Every color choice must be paired with a secondary channel so the visualization works in grayscale and for colorblind users.

| Element         | Color | Line Style  | Marker   |
|-----------------|-------|-------------|----------|
| OLS             | Blue  | Solid       | Circle   |
| Truth           | Gold  | Thick solid | Diamond  |
| Violation / Bias| Red   | Dotted      | Triangle |
| Repair          | Green | Dash-dot    | Square   |
| Alternatives    | Gray  | Dashed      | None     |

## 4.3 Interactive Elements

- Sliders: horizontal, at the top of the cell. Left end = assumption holds (green label). Right end = assumption maximally violated (red label). Default position always left. A thin colored bar fading green-to-red beneath the slider.
- Dynamic titles: a sentence above each plot that updates with slider position. Format: "OLS is unbiased (bias = 0.00)" or "OLS is biased (bias = 2.47, predicted: 2.51)".
- Two-column layout: visualization on the left, live-updating summary panel on the right showing current parameter values, theoretical prediction, simulated result, and discrepancy.
- Slider positions: discrete, snapped values. No continuous sliding. Prevents interpolation artifacts. Slider for ρ has 21 positions: -0.95, -0.85, ..., 0.85, 0.95.

## 4.4 Sidebar Visual Treatment

Sidebar plots use the same hues as the main flow but at 60% saturation. This visually signals supplementary status. Sidebars are collapsed by default using Colab's `#@title` feature with a provocative label.

# 5. Technical Infrastructure

## 5.1 Shared Module: company_sim.py

Embedded in each notebook's collapsed setup cell. No cross-notebook imports. No network dependencies. The notebook must work offline.

**CompanySimulator Class (~80 lines)**

- Constructor takes pathology strength parameters with realistic defaults.
- `generate(n=500, seed=42)` → pandas DataFrame with columns: `sale_price`, `living_area`, `bedrooms`, `zestimate`.
- `truth()` → DataFrame adding `desirability_U` column + dictionary of true parameters.
- `dgp_summary()` → LaTeX string of the full specification.
- Pathology methods: `set_heteroscedasticity(strength)`, `set_endogeneity(strength)`, `set_nonlinearity(curvature)`.
- Data generation order: U first, then X₁ and X₂ from U, then Y from X₁, X₂, U, ε, then X₃ from Y. X₃ is post-treatment — never in the true DGP for Y.

**MonteCarloEngine Class (~40 lines)**

- `run(estimator_fn, param_grid, n_reps=5000)` → precomputes draws across parameter grid, returns numpy array.
- Stores results in dictionary keyed by parameter grid values.
- Slider callbacks index into the array. Response time < 50ms.
- `quick_run(estimator_fn, dgp_fn, n_reps=1000)` → single-configuration simulation for sidebar mini-sims. No caching.
- Precomputation runs during setup with progress bar. Estimated time: 20–30 seconds on free Colab.

**DiagnosticSuite Class (~30 lines)**

- Single function call producing four-panel residual diagnostic: residuals vs. fitted, QQ plot, scale-location, leverage.
- Plus VIF table, Breusch-Pagan test, Durbin-Watson statistic, Jarque-Bera test.
- Consistent visual format across all notebooks. Builds familiarity by Notebook 7.

**AutopsyReport Widget Factory (~30 lines)**

- Notebooks 3–6: lightweight two-question version ("What is the biggest threat?" and "How would you check?").
- Notebook 7–8: full sensitivity analysis version with four fields + contour plot.
- Third field added from Notebook 3 onward: "Which real-world disaster is most analogous?" with dropdown of previously encountered sidebars.
- Responses stored to JSON for the final dashboard in Notebook 8.

## 5.2 Gate System (~20 lines)

Module-level dictionary `_trap_responses = {}`. Trap widget's submit callback writes to this dictionary and saves as JSON to `/content/trap_log.json`. Reveal cells check for the key. If missing, display warning. Pure Python. No JavaScript. Platform-independent.

## 5.3 Dependencies

All pre-installed on Colab. No pip installs required: numpy, pandas, matplotlib, statsmodels, ipywidgets, IPython.display. For Notebook 7: the Lalonde dataset is base64-encoded in the setup cell. Zero external data dependencies.

## 5.4 Precomputation Strategy

Every slider snaps to discrete values. Each position has exactly 5,000 precomputed Monte Carlo draws stored in a dictionary. Slider movement triggers a dictionary lookup, not a computation. Response time under 50 milliseconds. Precomputation runs in setup cell with progress bar. Front-load engagement: the scenario and trap question appear before precomputation, so the student reads and answers while the engine runs in a subsequent cell.

# 6. The Data Generating Process (DGP)

A single coherent DGP underlies all eight notebooks. Every pathology is present simultaneously in one business story. Each notebook isolates and examines one pathology.

## 6.1 The Business Story

HomeValuer Realty maintains a pricing dataset of residential home sales. The outcome Y is the sale price in thousands of dollars. Predictors are the home's living area X₁ (in thousands of square feet), the number of bedrooms X₂, and the Zillow Zestimate X₃ recorded at listing time. A hidden variable U represents neighborhood desirability, which the student never observes directly.

The running decision-maker is a home flipper. She is deciding whether to fund an $80k renovation that would add 500 square feet to a property. She wants to know: if she makes the house bigger, how much more will it sell for? That is the question driving every regression in the course.

## 6.2 Variable Intuition

The formal DGP in §6.3 names four observed variables (Y, X₁, X₂, X₃) and one hidden variable (U). Before the equations, this section builds intuition for what each variable represents and what role it plays in the analysis. A reader who internalizes these roles will find every pathology in the course easier to understand, because each pathology is fundamentally about one of these roles being misunderstood.

**Y — sale price**

The outcome. The thing the analyst wants to explain or predict. Sale price is what the homeowner cares about, what the flipper's profit depends on, and what the bank's mortgage decision rests on. Throughout the course, every regression has Y on the left-hand side. Typical value: $450k for a 3-bedroom suburban home. When you read "the coefficient is wrong" or "your estimate of β is biased," the β is always a number that translates a unit change in some predictor into a dollar change in Y.

**X₁ — living area (thousands of square feet)**

The treatment. The variable whose causal effect on Y the analyst actually wants to know. "If I add 500 sqft to this house, how much will the sale price go up?" That is the question driving the entire course. Notice the phrasing: it is a counterfactual about what would happen *if* you intervened on X₁. Regression does not naturally answer counterfactual questions — it tells you how Y and X₁ co-vary in your data, which is not the same thing. The eight-notebook arc is really about the gap between "co-varies with" and "causes."

**X₂ — number of bedrooms**

A control variable. Bedrooms are not what the flipper is deciding about (the decision is "should I add square footage?"), but bedrooms differ across houses and they affect price independently of square footage. Including X₂ in the regression makes the comparison fairer: it isolates the effect of square footage among houses with the same number of bedrooms. Controls are how analysts try to approximate "all else equal." But — as Notebook 1.5 will show — "controlling for" something is more subtle than it sounds.

**X₃ — Zillow Zestimate at listing time**

The trap. X₃ looks like a useful predictor. It is a number, it is correlated with sale price, and it would obviously improve R². But the Zestimate is computed by an algorithm that uses recent comparable sales — meaning, it is downstream of the very prices the analyst is trying to model. Including X₃ in the regression does not help the analyst learn anything about what causes price; it just lets the model "cheat" by partially seeing the answer. A naive analyst would happily include it. Notebook 6 will show what goes wrong.

**U — neighborhood desirability**

The unobservable. U represents everything about the neighborhood that buyers value but no spreadsheet captures: the feel of the streets, the quality of the schools, the friendliness of the neighbors, the way the light hits the trees in the afternoon. Some of it is captured by proxies (school ratings, crime statistics) but most of it is not. Crucially, U influences *both* the kind of houses that get built (bigger lots and bigger floor plans in nicer neighborhoods) and the prices buyers will pay. This dual influence is what makes U a confounder. Notebook 1 is entirely about what U does to your coefficient estimates when you cannot measure it.

**ε — irreducible noise**

The leftover. Even if you knew everything — every variable, every coefficient, every causal path — two identical houses on the same street would still sell for different prices. One buyer is in a hurry. Another low-balls and gets lucky. The seller's agent is having a bad week. ε is the bucket that holds all of this. Throughout the course, ε is treated as random: zero on average, with a variance that may or may not depend on other variables (Notebook 2 cares about exactly this). When ε behaves nicely, regression works. When ε is heteroscedastic, correlated, or non-normal, things break in specific ways.

**Why these particular roles matter**

Each of the eight notebooks corresponds to a way that one of these roles gets violated or misunderstood:

- Notebook 1 (Coefficient): the role of U is ignored — analyst forgets that an unmeasured confounder can shift β.
- Notebook 2 (Uncertainty): the role of ε is misunderstood — analyst assumes constant variance when it actually scales with X₁.
- Notebook 3 (Significance): the role of Y is conflated with statistical significance — analyst forgets that "p<0.05" says nothing about the size of the effect on Y.
- Notebook 4 (Specification): the role of X₁ is misshaped — analyst fits a line through what is actually a log curve.
- Notebook 5 (R²): the role of the controls is abused — analyst adds polynomial features until X₁'s coefficient memorizes noise.
- Notebook 6 (Causal Claim): the role of X₃ is misclassified — analyst treats a downstream variable as a useful control.
- Notebook 7 (Real World): every role is wrong at once.
- Notebook 8 (Redemption): a research design (RDD) makes the role of X₁ knowably causal.

If you find yourself confused about a notebook, come back to this section and ask: which variable's role is being violated here?

## 6.3 Formal Specification

> **Y = 50 + 8 · log(X₁) + 3 · X₂ + 2 · U + ε**

Where:

- U ~ N(0, 1) — unobserved neighborhood desirability
- X₁ = 2.0 + 0.5 · U + η₁ — living area (thousands of sqft) driven by desirability (creates endogeneity: bigger houses are built in nicer neighborhoods)
- X₂ = 3 + 0.5 · U + η₂ — bedroom count driven by desirability
- X₃ = 0.9 · Y + η₃ — Zestimate computed from comparable recent sales (post-treatment / bad control)
- ε ~ N(0, 0.5 · X₁) — heteroscedastic errors (luxury homes have wilder prices than starter homes)
- η₁, η₂, η₃ ~ N(0, σ²) — independent noise terms

Note: X₁ is in thousands of square feet, so a 2,500 sqft house has X₁ = 2.5 and log(X₁) ≈ 0.92. Y is in thousands of dollars.

## 6.4 Pathologies Present

| Pathology                      | Source in DGP                                                             | Notebook |
|--------------------------------|---------------------------------------------------------------------------|----------|
| Omitted variable bias          | U drives both X₁ and Y; omitting U biases β₁ upward                       | 1        |
| Heteroscedasticity             | ε variance scales with X₁; luxury homes have unpredictable prices         | 2        |
| Inflated significance          | Large n (50,000 home sales) makes trivial effects significant             | 3        |
| Misspecification               | True relationship is log(X₁), not linear X₁                                | 4        |
| Overfitting                    | Adding polynomial terms improves training fit, destroys test fit          | 5        |
| Endogeneity / Reverse causality | X₃ is caused by Y; including it as control creates collider bias         | 6        |
| All simultaneously             | Lalonde real data replaces simulated data                                  | 7        |
| None (by design)               | RDD with valid design eliminates confounding                               | 8        |

## 6.5 Data Generation Order

Critical: generate in causal order to avoid simultaneity. Step 1: Generate U, η₁, η₂, ε. Step 2: Compute X₁ = 2.0 + 0.5·U + η₁ and X₂ = 3 + 0.5·U + η₂. Step 3: Compute Y = 50 + 8·log(X₁) + 3·X₂ + 2·U + ε. Step 4: Compute X₃ = 0.9·Y + η₃. Step 5: Drop U from the observed dataset. The student sees only `sale_price`, `living_area`, `bedrooms`, `zestimate`.

## 6.6 Collider Bias Note

X₃ (Zestimate) is NOT in the true DGP for Y. It is caused by Y — the Zestimate algorithm uses comparable recent sale prices, so it is downstream of the very thing we are trying to model. Including X₃ as a control is a collider conditioning error. In Notebook 1's repair cell, toggling X₃ into the model should make the coefficient worse, not better. This is the only place in the course where a DAG is shown (three nodes: Living Area → Sale Price → Zestimate, with Neighborhood Desirability → Sale Price, and Neighborhood Desirability → Living Area).

# 7. Theorem Map

Each notebook is anchored by one core theorem. The theorems form a logical chain where each generalizes the previous one. The student who reads the formal statements in sequence sees a connected structure, not isolated results.

| NB  | Theorem                  | Formal Statement                                                                                     | Dependencies |
|-----|--------------------------|------------------------------------------------------------------------------------------------------|--------------|
| 1   | Omitted Variable Bias    | E[β̂₁] = β₁ + β₂δ₁ where δ₁ = Cov(X₁, X₂)/Var(X₁)                                                    | None         |
| 2   | Variance Decomposition   | Homoscedastic: Var(β̂) = σ²(X'X)⁻¹. Heteroscedastic: (X'X)⁻¹X'ΩX(X'X)⁻¹                             | NB 1         |
| 3   | t-Statistic Anatomy      | t = β̂/SE(β̂). Power = P(|t|>c | β≠0). Increases with n and effect size.                             | NB 2         |
| 4   | Specification Error      | If Y=f(X)+ε and we fit Y=Xβ+ε, OLS converges to linear projection, not f'(x).                       | NB 1–3       |
| 5   | Bias-Variance Tradeoff   | E[(ŷ-y)²] = Bias² + Variance + σ². Adding parameters reduces bias, increases variance.               | NB 4         |
| 6   | IV Consistency           | If E[εX]≠0 but E[εZ]=0, E[ZX]≠0: β̂_IV = (Z'X)⁻¹Z'Y is consistent.                                   | NB 1         |
| 7   | Sensitivity Analysis     | Robustness value RV = minimum partial R² to nullify conclusion. Cinelli-Hazlett.                     | All          |
| 8   | RDD Identification       | At cutoff c, if E[Y₀\|X=c] continuous, gap = E[Y₁-Y₀\|X=c].                                         | NB 4, 5      |
| 1.5 | Frisch-Waugh-Lovell      | β̂₁ from Y~X₁+X₂ = β̂ from M₂Y ~ M₂X₁ where M₂ = I-X₂(X₂'X₂)⁻¹X₂'                                   | NB 1         |

Meta-lesson: each theorem generalizes the previous. OVB is a special case of endogeneity. Classical variance is a special case of the sandwich estimator. The linear model is a special case of all models. Relaxing the assumptions that justified the previous notebook's conclusion generates the next notebook's theorem.

# 8. Notebook Specifications

Each notebook is specified with its full cell structure, trap design, interactive elements, and connections to other notebooks.

## 8.1 Notebook 1: Why Your Coefficient Is Wrong

**Core concept:** Omitted variable bias

**Core message (plain language):** "If something you didn't measure is correlated with both your input and your output, your coefficient is wrong. Not noisy. Not uncertain. Wrong. Systematically shifted in one direction."

**Estimated time:** 45 minutes

**File:** `01_coefficient.ipynb`

### Cell-by-Cell Specification

**Cell 0 — Setup (collapsed, `#@title`):** Contains CompanySimulator, MonteCarloEngine, AutopsyReport, gate system, all imports. ~200 lines. Runs precomputation: 5,000 Monte Carlo draws at each of 21 ρ values (-0.95 to 0.95). Progress bar. ~20 seconds on free Colab.

**Cell 1 — The Hook (markdown):** Provocative opening paragraph ("Regression is the most dangerous tool..."). Course framing. Then scenario: "You're an analyst at HomeValuer Realty. A home flipper wants to know whether square footage drives sale price. She's deciding whether to fund an $80k renovation that would add 500 sqft to a property. You have 500 sales records from across the region."

**Cell 2 — The Trap:** Runs simple regression: `sale_price` on `living_area` only. Displays statsmodels summary. Widget asks: "Based on this regression, what do you conclude?"

Options:

- A: "Living area strongly increases sale price (coefficient ≈ 4.7, p < 0.001). Recommend funding the addition."
- B: "There's a positive relationship but I'm not confident it's causal."
- C: "The coefficient is biased upward — the true effect is smaller."
- D: "The coefficient is biased but I can't determine the direction."

Correct answer: C. Option A is the naive answer. Option D is the sophisticated-but-wrong answer (the direction IS determinable). Submit button gates Cell 3.

**Cell 3 — The Reveal:** Displays recorded answer. Scatterplot of `sale_price` vs. `living_area`, points colored by hidden U (neighborhood desirability). Colorbar: blue = undesirable, gold = desirable. Pattern visible: desirable neighborhoods cluster upper-right. Formal OVB formula in LaTeX: E[β̂₁] = β₁ + β₂δ₁ = 2.3 + 2.0 × 1.2 = 4.7. Tailored response based on which option the student chose.

**Cell 4 — Monte Carlo Confirmation:** 5,000 replications with confound present. Animated histogram building particle by particle (200 frames, 25 particles/frame, 8 seconds). Distribution centers on 4.7. Gold vertical line at true value 2.3. Red annotation: "Bias = 2.4". Text confirms: "OVB formula predicts 4.7. Simulation mean is 4.698. Theory confirmed." Skip Animation button available.

**Cell 5 — The Destruction Playground:** Slider: "Correlation between neighborhood desirability and living area (ρ)" from -0.95 to 0.95 in steps of 0.1. Default: 0.0 (no confounding). Left panel: histogram of 5,000 β̂₁ estimates from precomputed grid. At ρ=0 centered on truth (2.3). Slides as ρ changes. Right panel: live summary with ρ, theoretical bias, simulated mean, true β₁. Dynamic title updates. Near-perfect match between predicted and simulated bias at every position.

**Cell 6 — Discussion Prompt (markdown):** "Your colleague says: 'I controlled for every variable in the dataset so there can't be omitted variable bias.' What's wrong with this reasoning?"

**Cell 7 — The Repair:** Same layout as Cell 5. Toggle button: "Include neighborhood desirability (U) as control: ON/OFF". When ON, histogram snaps to center on 2.3 regardless of ρ. Second toggle: "Include Zillow Zestimate (X₃) as control". When ON instead of U, coefficient gets worse. Dynamic title turns red with warning. DAG rendered with matplotlib: three nodes (Living Area → Sale Price → Zestimate) + (Desirability → Sale Price). Red X when bad control active. One-sentence disclaimer: "This is a causal diagram. We won't use these formally, but this picture explains why controlling for the Zestimate backfires."

**Cell 8 — The Limit of Repair:** Slider: "Proxy quality: 0% to 100%". At 100% the proxy perfectly measures U; bias eliminated. At 50%, noisy proxy gives partial debiasing. At 0%, full bias returns. Smooth curve showing residual bias as function of proxy quality. Live readout: "With X% proxy quality, residual bias = [value]. You've eliminated Y% of the confound."

**Cell 9 — Disaster Sidebar (collapsed):** Title: "Real-World Disaster: The hormone therapy that killed". Tabbed widget with three tabs: The Story (HRT narrative, 3 paragraphs), The Math (OVB formula: 0.5 + (-3.0)(0.6) = -1.3; sign wrong), The Simulation (1,000 datasets, distribution centered on -1.3 with gold line at truth +0.5).

**Cell 10 — Mini Autopsy:** Two text input fields: "What is the biggest threat to this estimate?" and "How would you check if that threat is real?" Responses stored to JSON.

**Cell 11 — The Bridge (markdown + HTML):** Lingering question: "Your coefficient is now correct. But can you trust the standard errors?" Netflix-style card linking to Notebook 2.

## 8.2 Notebook 2: Why Your Uncertainty Is Wrong

**Core concept:** Heteroscedasticity and standard errors

**Core message:** "Your coefficient might be right but your margin of error is wrong. You think you're 95% sure. You're actually 82% sure."

**Estimated time:** 30 minutes

**File:** `02_uncertainty.ipynb`

**Trap:** Student includes correct controls from NB1. Coefficient is correct. CI shown as [6.2, 9.8]. Trap asks: "Are you confident the true effect is in this range?"

**Reveal:** 1,000 Monte Carlo confidence intervals stacked vertically. True value as vertical line. ~18% miss (red). Too many red bars. "Your 95% CI only covers the truth 82% of the time."

**Destroy:** Slider controls heteroscedasticity strength. Coverage counter updates live.

**Repair:** Toggle: classical SEs vs. robust (White/Huber-White) SEs. Coverage snaps to 95% with robust SEs.

**Limit:** Sample size slider. At n=20, robust SEs have worse coverage than classical (sandwich estimator biased in small samples). Student finds the crossover point.

**Disaster sidebar:** Google Flu Trends. Autocorrelation inflated confidence. Effective sample size formula: n(1-ρ)/(1+ρ). With ρ=0.8 and n=100, effective n≈11.

**Bridge:** "Your standard errors are correct now. But what does 'significant' actually mean?"

## 8.3 Notebook 3: Why Your Significance Is Wrong

**Core concept:** Statistical significance vs. effect size and power

**Core message:** "With enough data, everything is statistically significant. Your shoe size predicts your income. The question is never 'is this significant?' — it's 'is this big enough to matter?'"

**Estimated time:** 30 minutes

**File:** `03_significance.ipynb`

**Trap:** 50,000 home sales. Everything significant at p<0.001. Checkboxes ask: "Which variables have a meaningful effect on sale price?" Student selects based on p-values.

**Reveal:** The Zillow Zestimate has p<0.001 but coefficient = $3 per Zestimate-point (economically meaningless — a $100k Zestimate difference predicts only a $300 difference in price). Another variable — number of bedrooms — has coefficient = $47,200 per extra bedroom but p=0.12.

**Destroy:** Sample size slider. As n increases, p-values for trivial effects cross 0.05. Coefficient stays flat while p-value plummets. Three-panel display: coefficient, SE, t-stat vs. n.

**Repair:** Introduce effect size measures and confidence intervals. Live power analysis: slider controls true effect size, shows sample size needed to detect it.

**Limit:** With small n, genuinely large effects can be insignificant. Second slider shows the Type II error rate.

**Disaster sidebar:** Genome-wide association studies. 1M tests at α=0.05 → 50,000 false positives. Bonferroni correction. Mini-sim: 1M t-tests on pure noise.

**Bridge:** "You know what's significant and what matters. But is your model even the right shape?"

## 8.4 Notebook 4: Why Your Model Is Wrong

**Core concept:** Specification error and extrapolation

**Core message:** "Your model is an approximation. Inside the range of your data, it might be fine. Outside that range, it's fiction with a confidence interval."

**Estimated time:** 30 minutes

**File:** `04_specification.ipynb`

**Trap:** Linear model of `sale_price` on `living_area`. R²=0.71. Ask: "How much would a 10,000 sqft mansion sell for?" Student enters prediction.

**Reveal:** True relationship is logarithmic — diminishing dollars per square foot as houses get bigger. Linear extrapolation overshoots by 3x at 10,000 sqft. Plot shows divergence beyond data range.

**Destroy:** Draggable vertical bar representing prediction point. Inside data range: overlap. Outside: wild divergence. Confidence band widens but doesn't contain truth.

**Repair:** Fit log-transformed model. Intuition: each additional square foot adds less value than the last, because buyers pay a premium for the first 1,500 sqft of a house far more than for square feet 8,000 through 10,000. Extrapolation improves dramatically.

**Limit:** Even log model fails at extreme extrapolation. Every functional form is a local approximation.

**Disaster sidebar:** Challenger O-ring disaster. Selection on Y (only analyzed failure flights). Include all flights and the temperature trend is obvious.

**Bridge:** "Your model is now correctly specified. But how do you know it's not just memorizing the data?"

## 8.5 Notebook 5: Why Your R² Is Lying

**Core concept:** Overfitting and the bias-variance tradeoff

**Core message:** "A model that fits your existing data perfectly will predict new data terribly. This is not a paradox — it's memorization vs. learning."

**Estimated time:** 30 minutes

**File:** `05_overfitting.ipynb`

**Trap:** Add polynomial terms. R² climbs: 0.71 → 0.82 → 0.91 → 0.97. Leaderboard format asks: "Which model wins?" Student picks highest R².

**Reveal:** Train/test split. R²=0.97 model has negative R² on test set. Predicts worse than the mean.

**Destroy:** Slider: polynomial degree 1–15. Two lines: training R² (always rising) and test R² (rises then crashes). Crossover visible.

**Repair:** Cross-validation and adjusted R². Toggle: switch from polynomial family to log-linear family. Test R² jumps above any polynomial. Right model family > right complexity.

**Limit:** Slider controls number of model specifications searched. Best CV R² inflates with search breadth. Even CV can overfit.

**Disaster sidebar:** Long-Term Capital Management. $4.6B loss. Overfit to historical market patterns. Mini-sim: degree 1–45 polynomial, training MSE →0, test MSE explodes.

**Bridge:** "Your model fits well and predicts well. But does increasing X cause Y to increase?"

## 8.6 Notebook 6: Why Your Causal Claim Is Wrong

**Core concept:** Endogeneity, reverse causality, and instrumental variables

**Core message:** "If your input and your output cause each other, regression can't tell you which direction the effect runs."

**Estimated time:** 30 minutes

**File:** `06_causation.ipynb`

**Trap:** Student has fixed coefficient, SEs, significance, functional form, model selection. Everything looks solid. Ask: "Does funding the $80k 500-sqft addition cause sale price to increase by [coefficient × 0.5]?"

**Reveal:** Cross-sectional animation across the dataset reveals that the Zestimate moves in lockstep with sale price because the Zestimate is computed from comparable recent sales. The "predictor" is downstream of the outcome. OLS captures mutual dependence, not causal effect.

**Destroy:** Simulate an A/B test (random assignment of addition vs. no addition across comparable houses). Experimental estimate is smaller than observational. Slider controls endogeneity strength. Gap widens.

**Repair:** Introduce instrumental variables. Natural experiment: the 30-year mortgage rate at the month of sale varies exogenously (it is set by macro conditions, not by any single house) and shifts buyer purchasing power, which shifts the kind of house buyers can afford. IV estimate recovers truth. Brief primer: relevance, exclusion, Wald estimator (3 cells max). Foreshadowed in NB1 footnote.

**Limit:** Slider controls instrument strength. Weak instrument: IV estimate oscillates wildly with enormous CIs. Student finds stability threshold.

**Disaster sidebar:** Police and crime. Positive OLS correlation. Resolved by electoral cycle instrument. Mini-sim: feedback loop DGP, OLS vs. IV estimates.

**Bridge:** "You've learned six ways your regression can fail. Now let's see what happens when they all attack at once."

## 8.7 Notebook 7: The Real World

**Core concept:** Confronting the limits of regression with real data

**Core message:** "You can do everything right and still get the wrong answer. Because the problem isn't in your model. It's in your data."

**Estimated time:** 60 minutes

**File:** `07_real_world.ipynb`

### Three-Act Structure

**Act 1 — False Confidence:** Load the Lalonde observational data (base64-encoded in setup cell). Run OLS of earnings on treatment + controls. Coefficient is negative — training appears to reduce earnings. Student runs full diagnostic suite. Everything looks acceptable. Robust SEs barely change things. VIFs under 3. The model passes every test. Trap: "Does the job training program work? Yes / No / Can't tell."

**Act 2 — The Confrontation:** Reveal the experimental estimate. Positive and large (~$1,800). Side by side with the negative observational estimate. They don't even have the same sign. Visualization: density plots of pre-treatment characteristics for experimental vs. observational samples. Barely overlap. Slider: reweight using subgroup analysis within bins of prior earnings. Estimate crawls toward experimental benchmark but never reaches it. Readout: "Gap remaining: $___"

**Act 3 — Wisdom:** Sensitivity analysis contour plot (Cinelli-Hazlett). X-axis: partial R² of confounder with treatment. Y-axis: partial R² with outcome. Shaded region: combinations that explain away the result. Observed covariates plotted as labeled dots. Interactive: student drags a hypothetical confounder point, bias-adjusted estimate updates in real time. Full autopsy report with four fields. Final cell: side-by-side NB1 and NB7 autopsy reports.

**Disaster sidebar:** Hormone replacement therapy (expanded from NB1 sidebar). Observational studies vs. Women's Health Initiative RCT.

**Bridge:** "Is regression hopeless? No. You just need the right design."

## 8.8 Notebook 8: The Redemption

**Core concept:** Regression discontinuity design — regression works when the design earns trust

**Core message:** "Regression works brilliantly when the world gives you a natural experiment. Your job is to find those moments — or create them."

**Estimated time:** 45 minutes

**File:** `08_redemption.ipynb`

**Setup:** Scholarship cutoff example. Test scores just above and below a threshold. Students barely above got scholarships; those barely below didn't. Near the cutoff, the two groups are nearly identical in every way.

**Visualization:** Scatterplot with vertical line at cutoff. Regression lines on each side. Gap at boundary = causal effect. Visible. Credible.

**Destroy:** Bandwidth slider. Narrow: noisy but unbiased. Wide: smooth but biased. Student watches lines wobble (too narrow) or curve toward each other (too wide). Sweet spot visible.

**Repair:** The RDD itself is the repair. The regression is trustworthy because the design is trustworthy.

**Final autopsy report:** Everything is green. Threats minimal. Robustness value high. Side-by-side comparison: NB1 report (red, fragile) vs. NB8 report (green, credible). Same tool. Same estimator. Same code. Different credibility.

**Disaster sidebar:** Maimonides' Rule study (Angrist & Lavy). Israeli class size discontinuity at 40 students.

> *"You've now seen every way a regression can fail. Most practitioners never learn this. They run regressions that look convincing and draw conclusions that feel solid, without knowing what could go wrong. You're different now. You know the failure modes. You know the diagnostics. You know the repairs and their limits. You know how to write an honest autopsy report. This doesn't mean you should stop using regression. It means you're finally ready to start."*

## 8.9 Notebook 1.5 (Optional): What "Controlling For" Actually Means

**Core concept:** The Frisch-Waugh-Lovell theorem

**Core message:** "Multiple regression doesn't 'hold variables constant.' It strips out what the controls explain about both sides, then measures what's left."

**Estimated time:** 20 minutes

**File:** `01b_controlling_for.ipynb`

**Trap:** Show multiple regression output. Ask which interpretation is correct: A) holding bedrooms constant, B) after residualizing both sides on bedrooms, C) both mean the same thing, D) neither. Most pick A or C. Correct: B.

**Reveal:** FWL procedure manually: residualize Y on X₂, residualize X₁ on X₂, regress residuals. Coefficient matches to 14 decimal places. Side-by-side: original scatterplot vs. partial regression plot.

**Interactive:** Checkbox list of control variables. For each combination, full regression and FWL shown side by side. Match always holds. Partial regression plot updates dynamically. Bad control (X₃) distorts the residual cloud visibly.

**Diagnostic tool:** Partial regression plot grid for each predictor. Click on any point to highlight it across all plots. Leverage is coefficient-specific, not model-wide.

# 9. Real-World Disaster Sidebars

Each sidebar has three elements: narrative (3 paragraphs, no jargon), formal diagnosis (OVB formula or equivalent applied to the specific case, 4–6 lines of LaTeX), and mini-simulation (5–10 lines of code, one plot, one button, runs in <2 seconds).

| NB  | Sidebar Title                         | Core Error                      | Formal Diagnosis                                                   |
|-----|---------------------------------------|---------------------------------|---------------------------------------------------------------------|
| 1   | The hormone therapy that killed       | Omitted variable (healthy-user bias) | β_HRT=+0.5, β_U=-3.0, ρ=0.6 → E[β̂]=-1.3 (sign flip)           |
| 2   | Google Flu Trends                     | Autocorrelation → wrong SEs     | Effective n = n(1-ρ)/(1+ρ). ρ=0.8, n=100 → eff. n≈11              |
| 3   | Genome-wide association studies        | Multiple testing                | 1M tests, α=0.05 → 50K false positives. Bonferroni: α/m=5×10⁻⁸     |
| 4   | Challenger disaster                   | Selection on Y / specification error | Regress on failure flights only: no trend. All flights: clear trend. |
| 5   | Long-Term Capital Management          | Overfitting to historical patterns | Degree 45 polynomial: training MSE≈0, test MSE explodes         |
| 6   | Police and crime                      | Reverse causality / endogeneity | OLS: positive. IV (electoral cycle): negative. Different signs.    |
| 7   | Hormone replacement therapy (expanded) | Selection bias + OVB            | Full sensitivity analysis. RV shows fragility.                     |
| 8   | Maimonides' Rule                      | RDD success story               | Class split at 40 students. Effect visible at discontinuity.       |

## Sidebar Layout

Each sidebar is a single cell containing an `ipywidgets.Tab` with three tabs: "The Story", "The Math", "The Simulation". Collapsed by default using `#@title` with a provocative label. Sidebar plots use 60% saturation of the main color palette. Mini-simulation runs via a single "Run Simulation" button — no sliders, no interactivity. The sidebar is a closed argument: story says X, math says X, simulation confirms X.

# 10. Cross-Notebook Systems

## 10.1 Trap Response Storage

Each notebook stores trap responses to `/content/trap_log.json`. Key format: `"notebook_N_qM"`. Notebook 8's final cell reads this file and compiles a misconception dashboard showing every wrong answer alongside the correction and the theorem that predicted the error.

## 10.2 Progressive Autopsy Reports

Notebooks 3–6: two-question lightweight version. Notebooks 7–8: full four-question version with sensitivity analysis. Starting from Notebook 3, a dropdown field asks: "Which real-world disaster is most analogous to your situation?" populated with all sidebars encountered so far. This builds the pattern-matching instinct of experienced practitioners.

## 10.3 Transition Cards

Each notebook ends with a styled HTML card containing: the lingering question, the next notebook's title, and a one-click "Open in Colab" link. Delivered at the moment of maximum engagement.

## 10.4 Final Dashboard (Notebook 8, last cell)

Side-by-side comparison of the NB1 autopsy report (red, fragile, uncertain) and the NB8 autopsy report (green, credible, trustworthy). Same tool. Same estimator. Same code. Different credibility. Below: table of all trap responses across all notebooks with corrections. Below that: the closing paragraph. "This doesn't mean you should stop using regression. It means you're finally ready to start."

# 11. Repository Structure & Distribution

## 11.1 File Structure

```
regression-autopsy/
├── index.html                   (landing page, GitHub Pages)
├── company_sim.py               (shared module, also embedded in each NB)
├── data/
│   └── lalonde.csv              (also base64 in NB7)
├── notebooks/
│   ├── 01_coefficient.ipynb
│   ├── 01b_controlling_for.ipynb   (optional)
│   ├── 02_uncertainty.ipynb
│   ├── 03_significance.ipynb
│   ├── 04_specification.ipynb
│   ├── 05_overfitting.ipynb
│   ├── 06_causation.ipynb
│   ├── 07_real_world.ipynb
│   └── 08_redemption.ipynb
├── images/
│   └── og_card.png              (social media preview)
└── README.md
```

## 11.2 Landing Page

Static HTML on GitHub Pages. Dark background, white text, course title in large sans-serif, subtitle hook line. Eight full-width cards for core notebooks with titles and one-sentence descriptions. Optional notebooks as indented half-width cards with a subtle border and "Optional Deep Dive" badge. Each card has an "Open in Colab" badge that links directly to the notebook.

## 11.3 Social Media Card

`og_card.png`: dark background, white text, title "Regression Autopsy", hook line "Eight Ways Your Model Is Lying to You", subtle scatterplot with regression line in background. Used for Twitter/LinkedIn/Slack previews.

## 11.4 Self-Containment Principle

Every notebook is fully self-contained. The CompanySimulator and all utilities are embedded in a collapsed setup cell. No cross-notebook imports. No network dependencies for core functionality. The Lalonde dataset is base64-encoded in NB7. A student on a plane with no internet can run any single notebook.

# 12. Build Order & Phasing

| Phase | Deliverable                              | Purpose             | Validates                                                                 |
|-------|------------------------------------------|---------------------|---------------------------------------------------------------------------|
| 1     | Notebook 1 (complete)                    | Minimum viable course | Six-beat structure, trap system, Monte Carlo engine, sliders, sidebar, autopsy |
| 2     | Notebooks 2 and 7                        | Core trio           | Modularity (NB2) and capstone with real data (NB7). NB7 tests standalone virality. |
| 3     | Notebooks 3, 4, 5, 6                     | Fill the spine      | Faster to build — infrastructure exists from Phase 1                       |
| 4     | NB8, NB1.5, instructor's guide, landing page | Finale and polish | Cross-NB dashboard, accessibility, distribution                            |
| 5     | Open source + blog post                  | Community           | Share NB7 on social media (most self-contained/provocative)                |

Phase 1 produces a complete, shareable artifact. Not a skeleton. A finished notebook a student can open and learn from. That early win sustains momentum through longer phases.

# 13. Testing & Quality Criteria

## 13.1 Per-Notebook Testing Checklist

1. Open in fresh Colab runtime with no prior state
2. Setup cell completes in under 30 seconds with visible progress bar
3. Trap widget renders; all options clickable; submit works
4. Attempting to run reveal cell without submitting triggers gate warning
5. Reveal renders with correct tailored response based on trap answer
6. Monte Carlo animation plays smoothly with no frame drops
7. Interactive sliders respond in under 100ms at all positions
8. Theoretical predictions match simulated results to two decimal places at every slider position
9. Repair toggle produces visible, immediate change in visualization
10. Limit slider finds the boundary where repair fails
11. Sidebar tabs render; simulation button produces correct output
12. Autopsy widget accepts input and stores to JSON
13. Transition card links to next notebook correctly
14. Total runtime first-to-last cell: under 3 minutes including precomputation
15. Total memory usage: under 500MB on free Colab tier
16. All plots readable when converted to grayscale
17. All interactive elements have text alternatives (dynamic titles)

## 13.2 Cross-Notebook Testing

18. Trap log JSON accumulates correctly across notebooks
19. NB8 final dashboard correctly displays all previous trap responses
20. Autopsy report dropdown populates with sidebars from all previously completed notebooks
21. Each notebook runs independently without any other notebook having been opened
22. Transition card Colab links open correctly from within Colab

# 14. Instructor's Guide Outline

## 14.1 Timing

| Notebook | Self-Paced   | Live Classroom | Notes                                              |
|----------|--------------|----------------|----------------------------------------------------|
| 1        | 45 min       | 45 min         | First notebook; structure is new to students      |
| 2–6      | 20–30 min each | 30 min each  | Structure familiar by NB3; faster pacing          |
| 7        | 60 min       | 60 min         | Real data requires more discussion                |
| 8        | 30 min       | 45 min         | Including final reflection and dashboard review   |
| Total    | ~5 hours     | ~6 hours       | One-day workshop or two-week module               |

## 14.2 Suggested Syllabi

**Full sequence (8 notebooks):** Notebooks 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8. Optional 1.5 between 1 and 2.

**Essentials track (4 notebooks):** 1 → 2 → 5 → 7. Covers coefficient bias, uncertainty, overfitting, real-world confrontation.

**Executive briefing (2 notebooks):** 1 → 7. "Your coefficient is wrong" and "you can't always fix it."

## 14.3 Discussion Facilitation

In a classroom, the instructor should pause at each trap and facilitate public commitment before the reveal. Suggested prompts provided for each notebook. The public commitment makes the correction more powerful in group settings.

# 15. Accessibility Requirements

- Every color choice paired with secondary visual channel (line style, marker shape). See Visual Design System §4.2.
- All plots must be readable when converted to grayscale. Test every visualization in grayscale before release.
- Dynamic titles carry all quantitative information textually, so screen readers can parse the key lesson.
- Slider labels communicate meaning ("Strong negative confounding" / "Strong positive confounding"), not just numbers. Numbers appear in the summary panel.
- Sidebar tab structure navigable by keyboard.
- All images have alt text in markdown cells.
- Font sizes minimum 10pt in all plots (12pt preferred).
- Notebook runs on free Colab tier with no paid runtime or GPU required.

---

**END OF SPECIFICATION**

*This document contains everything needed to build the complete Regression Autopsy course.*

*Build Notebook 1 first. Validate the design. Then iterate.*
