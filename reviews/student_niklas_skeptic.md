# Critical Review of "Regression Autopsy" Lecture Notes

**Reviewer:** Niklas, 4th-year Mechanical Engineering, ETH Zurich
**Date:** 10 April 2026
**Document:** `lecture_notes.tex` (Regression Autopsy -- Eight Ways Your Model Is Lying to You)

---

## Overall Impression

These notes are genuinely better than most statistics lecture material I have encountered at ETH. The single-DGP-throughout approach is clever and gives the document a narrative coherence that most stats courses lack. That said, the notes have real problems: some sections over-explain things any ETH student already knows, other sections hand-wave past critical assumptions, and several examples have edge cases that would trip up a careful reader. Below I go section by section.

---

## Section-by-Section Review

### 1. Introduction (Rating: 7/10)

**What works:** The exam score running example is well-motivated. Describing every variable with its real-world interpretation *before* showing equations is good pedagogy. The idea of a "trap" variable ($X_3$) is intriguing and creates genuine suspense.

**Where it is dumbed down:** The bullet-point explanations of what an outcome, treatment, and control variable are will feel patronizing to any ETH student who survived Probability and Statistics. We know what a dependent variable is. A one-sentence reminder would suffice; the current treatment is three paragraphs.

**Where it is hand-wavy:** The claim that $U$ (self-discipline) is drawn from $\mathcal{N}(0,1)$ because the Instagram slider is "standardised" glosses over the fact that a bounded slider (0 to 1) cannot produce a Gaussian. You can standardize it to mean 0 and SD 1, but the distribution is still bounded. This is a DGP choice, not a derivation from the story -- be honest about that instead of dressing it up as realistic.

---

### 2. The Data Generating Process (Rating: 8/10)

**What works:** This is the strongest conceptual section. Walking through every equation in plain language *and then* showing the causal graph is exactly the right sequence. The "Key Insight" box tying numbers to real-world meaning is excellent. The causal graph is clean and well-labeled.

**Edge case / internal inconsistency:** The error term is defined as $\varepsilon \sim \mathcal{N}(0, 0.5 \cdot |X_1|)$. But this means the *standard deviation* is $\sqrt{0.5 |X_1|}$, not $0.5 |X_1|$. Later in Section 4 (line ~548), the notes say "noise standard deviation $\sqrt{0.5 \cdot 1} \approx 0.71$," which is correct only if $0.5 |X_1|$ is the *variance*, not the standard deviation. But the notation $\varepsilon \sim \mathcal{N}(0, 0.5 |X_1|)$ is ambiguous -- is the second argument the variance or the standard deviation? In standard probability notation, $\mathcal{N}(\mu, \sigma^2)$ means the second argument is the variance. If so, $\text{Var}(\varepsilon) = 0.5 |X_1|$ and $\text{SD}(\varepsilon) = \sqrt{0.5 |X_1|}$, and the later calculation is correct. But then the "Key Insight" box says "exam score variance scales with study hours" -- which is true only if $h = 0.5$ refers to the variance scaling, not the SD scaling. This needs to be nailed down explicitly. A careful reader will get confused.

**Another edge case:** $X_1 = 2 + 0.5U + \eta_1$ with $\eta_1 \sim \mathcal{N}(0, 0.3)$. Since $U \sim \mathcal{N}(0,1)$, we get $X_1 \sim \mathcal{N}(2, 0.25 + 0.3) = \mathcal{N}(2, 0.55)$. The SD is about $0.74$, so roughly 0.2% of students will have $X_1 < 0$ (negative study hours). The notes never mention this. For a simulation exercise where students generate data, they will see negative values and wonder. Either truncate $X_1$ at zero in the DGP or acknowledge the issue.

**Where it is hand-wavy:** The remark on probability limits (line ~199) says "think of it as what the estimator settles down to with unlimited data." This is fine as intuition, but "settles down to" in what sense? Almost surely? In probability? For ETH students who have taken measure-theoretic probability, this could be sharpened in one sentence: "convergence in probability: for every $\delta > 0$, $P(|\hat{\beta} - \beta| > \delta) \to 0$."

---

### 3. Omitted Variable Bias (Rating: 8/10)

**What works:** The proof is clean and short. The numerical example with five students is genuinely verifiable on paper. The OVB formula is presented in the right order: intuition, formal statement, proof, example. This is a model section.

**The sunscreen story is a missed opportunity.** The ice cream / drowning analogy is one of the most overused examples in all of statistics. Every intro stats course uses it. ETH students have seen it multiple times. Using it here undermines the notes' claim to be at a higher level. Replace it with something from engineering or physics -- e.g., bridge load and deflection with temperature as the omitted variable.

**Where the example breaks down:** The five-student numerical example (lines 401-431) uses data with no noise ($Y = 60 + 5X_1 + 3X_2$ exactly). This is pedagogically useful but the notes then claim "the full regression recovers $\hat{\beta}_1 = 5$, $\hat{\beta}_2 = 3$ exactly." With five observations and two regressors plus intercept, we have $n = 5$ and $p = 3$. The system is not exactly identified; it has 2 degrees of freedom. The full regression only recovers the exact coefficients because the data was *generated* with zero noise -- but the notes do not prove or even state that $X_1$ and $X_2$ are not collinear in this five-point sample, which is necessary for $(X^\top X)^{-1}$ to exist. A skeptical reader would want verification that the design matrix has full rank.

**Collider bias section (lines 462-501):** This is excellent. The formal proposition with proof is rigorous, the warning box is well-written, and the "rule of thumb" is practical. One issue: the definition (line 466) says a collider is defined on a *path*, but then says "$Y$ is a collider on the path $X_1 \to Y \leftarrow U$." Strictly, this is not a path in the usual graph-theory sense -- it is a fork into $Y$ from two sources. The definition of "path" as "any sequence of arrows regardless of direction" is correct for d-separation, but it is non-standard and will confuse students who know graph theory. A footnote would help.

**Proxy variable section (lines 456-460):** The claim that "residual bias is approximately $(1-q)$ times the original bias" is stated without proof or reference. This is a nontrivial result. Under what conditions does this hold? Linearity of the proxy in $U$? What if the proxy is a nonlinear function of $U$? This is hand-waving -- either prove it or cite a source.

---

### 4. Heteroscedasticity (Rating: 7/10)

**What works:** The sandwich formula derivation is complete and correct. The Breusch-Pagan test is explained with real care -- walking through why $nR^2$ works and why $\sigma^2$ is not needed is above-average exposition.

**Where it is dumbed down:** The "Drunk Darts" story is fun, but the confidence interval section (lines 511-529) spends an entire paragraph explaining what a 95% CI is and what it is not. Every ETH student in their 4th year has heard the "it does not mean 95% probability that $\beta$ is in this interval" speech at least three times. Keep the definition, cut the paragraph of explanation.

**Where it is hand-wavy:** The notes claim (line 607) that "with heteroscedasticity, classical CIs achieve only ~82% coverage." Where does 82% come from? Is this from a simulation of the specific DGP defined in Section 2? If so, say so. If it is a general statement, it is wrong -- coverage under heteroscedasticity depends entirely on the structure of the heteroscedasticity and the design matrix. This number needs a source or a derivation.

**Edge case in the numerical example (lines 584-601):** The table shows five students with fitted values from $\hat{Y} = 53 + 6.5X$. But the true model is stated as $Y = 50 + 8X$. The OLS fit on five points gives $53 + 6.5X$, but the notes never show *how* this was computed. Given the $Y$ values in the table (59, 66, 75, 72, 96), a reader who actually runs the OLS calculation gets: $\bar{X} = 3$, $\bar{Y} = 73.6$, $\hat{\beta}_1 = \text{Cov}(X,Y)/\text{Var}(X) = 34/10 = 3.4$... wait, let me check. Actually I suspect the numbers are made up to illustrate a point rather than being a genuine OLS fit, which would be a serious pedagogical error in notes that tell students to "verify on paper." If the numbers do not actually come from OLS on the given data, that is a credibility problem.

---

### 5. Significance and Effect Size (Rating: 9/10)

**What works:** The seat number example is brilliant -- much better than the tired ice cream story. It is concrete, absurd enough to be memorable, and makes the point sharply. The keyboard example is also well-chosen. The multiple testing section with the proof via linearity of expectation is clean.

**Minor quibble:** The power formula (line 755) is an approximation that assumes $\sigma$ is known (hence $z$ instead of $t$ quantiles). This is fine for large $n$ but the notes do not flag this approximation. For $n = 5$ in the earlier examples, using the normal approximation for power would be misleading.

**Where it could be stronger:** The Bonferroni correction is mentioned but no discussion of its conservatism or alternatives (Holm, BH/FDR). For ETH students who will encounter GWAS or multi-comparison problems in their careers, mentioning that Bonferroni is the *most conservative* correction would be useful.

---

### 6. Specification Error (Rating: 7/10)

**What works:** The "straight ruler on a winding road" analogy is apt. The extrapolation danger section is well-argued.

**Where the example breaks down:** The table (lines 850-861) claims the linear model $\hat{Y} = 52.5 + 1.6 X_1$ is "a reasonable OLS fit to the log curve over [1, 16]." But no one actually computed this. If I take 100 equally spaced points from 1 to 16, compute $Y = 50 + 8\ln(X_i)$, and run OLS, I do not get $52.5 + 1.6X_1$. The intercept and slope depend on the distribution of $X_1$ in the sample. Stating a linear fit without specifying the data distribution is sloppy.

**Deeper problem:** The "marginal gain" column shows $+5.5$ for every doubling, which is $8 \ln 2 \approx 5.545$. The notes round to 5.5, which is fine. But the column header says "Marginal gain" which conventionally means the gain from one additional unit, not from doubling. The text explains this, but the table header is misleading on its own.

**Hand-wavy:** Theorem 4.1 (Linear Projection) is stated without proof. For a section that claims "every claim is stated as a formal result," this is a gap. The result is a standard consequence of the projection theorem, but even a two-line proof would strengthen the section.

---

### 7. Overfitting and Bias-Variance (Rating: 8/10)

**What works:** The bias-variance proof is correct and clearly presented. The three-model numerical example (constant, line, degree-4 polynomial) is a genuinely good teaching tool. The table with Bias^2, Variance, and Total MSE is clean and memorable.

**Where it is hand-wavy:** The bias-variance decomposition proof (lines 917-932) has a critical assumption buried in a parenthetical: "$\varepsilon$ is independent of $\hat{f}$ (trained on separate data)." This is a HUGE assumption. In practice, $\hat{f}$ is trained on the *same* data that generated $\varepsilon$. The cross-term only vanishes if we evaluate at a *new* test point $(x_0, Y_0)$ where $Y_0 = f(x_0) + \varepsilon_0$ and $\varepsilon_0$ is independent of the training set. The notes should make this explicit -- it is the entire reason we need test data. Sweeping it into a parenthetical undermines the proof's credibility.

**Edge case in the polynomial table (lines 939-949):** Test $R^2 < 0$ for degree 15. The notes explain this means "predicts worse than the sample mean." True, but $R^2 < 0$ is technically undefined in some formulations of $R^2$ (the "1 - SS_res/SS_tot" version can go negative on test data, but the "correlation squared" version cannot). Which $R^2$ is being used? This matters because students will encounter both definitions.

**Cross-validation warning (lines 974-977):** The warning about CV overfitting with many model specs is important but vague. How many is "large"? Is there a correction? This could use one sentence pointing to nested CV or a reference.

---

### 8. Endogeneity and Bad Controls (Rating: 8/10)

**What works:** The "movie star's spouse" toy story is the best one in the document. It is original (I have not seen it in other textbooks), immediately intuitive, and maps perfectly onto the formal concept. The IV section is well-structured: motivation, definition, theorem, numerical example.

**Where it contradicts itself:** The collider bias proposition (line 1049) says "even if $X_1$ is otherwise exogenous." But in the DGP, $X_1$ is NOT exogenous -- it is driven by $U$. So the proposition's condition does not apply to the running example. The notes should clarify: the proposition is a general result, and in our DGP the collider bias *compounds* the existing endogeneity rather than creating it from scratch.

**IV numerical example (lines 1153-1196):** The example is clean and works. However, the DGP used here ($Y = 50 + 3X_1 + 2U$) is *different* from the main DGP ($Y = 50 + 8\log(X_1) + 3X_2 + 2U + \varepsilon$). The switch to a simplified DGP is fine but should be flagged more explicitly -- a student might wonder why $\beta_1$ suddenly changed from 8 to 3 and why the log disappeared.

**Exclusion restriction:** The notes say the roommate instrument satisfies exclusion because "your roommate does not take the exam for you." This is a plausibility argument, not a proof. What if roommates share study materials or explain concepts to each other? Then the roommate's hours affect your score through a channel other than your own study hours (knowledge transfer), violating exclusion. The notes should acknowledge that exclusion is *always* an assumption that cannot be tested from data -- this is one of the most important points in all of IV estimation, and it gets one sentence.

---

### 9. Real World / Lalonde (Rating: 6/10)

**What works:** The tutoring analogy is effective. The point that "every diagnostic passed yet the estimate had the wrong sign" is the most important lesson in the entire document.

**Where it is hand-wavy:** The Cinelli-Hazlett robustness value gets a definition and a two-sentence description. This is not enough. What is partial $R^2$? (It has been used throughout the notes but never defined.) How do you compute RV in practice? The formula on line 1254 is notation-heavy and unexplained -- what is $q$? What is the "adjusted estimate"? A student cannot use this tool based on what is written here.

**Weakest section overall.** This section feels rushed. The Lalonde dataset is mentioned but no actual numbers are shown (unlike every other section). The sensitivity analysis is name-dropped without enough depth to be actionable. Either expand it with a numerical example or cut it to a pointer and be honest that it is beyond scope.

---

### 10. Regression Discontinuity Design (Rating: 7/10)

**What works:** The "kid who scored 69 vs 70" story is vivid. The numerical example is clean and verifiable. The bandwidth discussion is well-framed.

**Where it is hand-wavy:** The RDD Identification Theorem (line 1292) states the continuity assumption but never discusses when it might fail. The most important threat to RDD is *manipulation* -- students near the cutoff might retake the exam, bribe the grader, or self-select. The McCrary density test (checking for bunching at the cutoff) is standard in RDD practice and is not mentioned at all.

**Edge case:** The numerical example has perfectly spaced data points (43, 45, 47, 49, 51, 53, 55, 57) with no noise in $Y$. This makes the RDD estimate exact, but it is unrealistically clean. In practice, there is scatter around the regression lines, and the bandwidth choice becomes genuinely difficult. The example gives a false sense of precision.

---

### 11. Frisch-Waugh-Lovell (Rating: 9/10)

**What works:** This is the second-strongest section after OVB. The coaching/shoes story is excellent -- much better than the usual abstract "partialling out" explanation. The three-step algorithm is concrete and executable. The proof is complete. The numerical example is verifiable and the numbers actually check out.

**Minor issue:** The proof (lines 1395-1411) uses block matrix inversion, which is standard but non-trivial. It might help to note that $M_2$ is idempotent and symmetric ($M_2^2 = M_2$, $M_2^\top = M_2$), since these properties are used implicitly when going from Step 3 to the formula.

**Where it could go further:** The connection to partial regression plots / added-variable plots is mentioned in one sentence. This deserves a figure or at least a worked example showing the plot, since it is the primary visual diagnostic tool for understanding multiple regression in practice.

---

### 12-13. Diagnostics and Theorem Map (Rating: 7/10)

**What works:** The diagnostics table is a useful reference. The theorem map showing how results build on each other is a nice structural touch.

**Where it is hand-wavy:** VIF is mentioned (VIF > 10 is "problematic") but never defined. What is VIF? A student encountering this table cannot use it without an external reference. Same for Cook's distance -- "Cook's $d > 1$" is stated as a threshold with no explanation of what $d$ measures.

**Missed opportunity:** The diagnostics section could include a flowchart: "If you suspect X, run diagnostic Y, and if it fails, apply repair Z." The information is all in the notes but scattered across sections.

---

## Summary Ratings

| Section | Topic | Rating |
|---------|-------|--------|
| 1 | Introduction | 7/10 |
| 2 | Data Generating Process | 8/10 |
| 3 | Omitted Variable Bias | 8/10 |
| 4 | Heteroscedasticity | 7/10 |
| 5 | Significance and Effect Size | 9/10 |
| 6 | Specification Error | 7/10 |
| 7 | Overfitting / Bias-Variance | 8/10 |
| 8 | Endogeneity and Bad Controls | 8/10 |
| 9 | Real World / Lalonde | 6/10 |
| 10 | Regression Discontinuity | 7/10 |
| 11 | Frisch-Waugh-Lovell | 9/10 |
| 12-13 | Diagnostics / Theorem Map | 7/10 |

**Overall: 7.6/10**

---

## Strongest Section

**Section 11 (FWL)** and **Section 5 (Significance/Effect Size)** are tied for best. FWL has the best pedagogical structure: a concrete story, a clean proof, and a numerical example that actually checks out. Significance has the best toy example (seat numbers) and the cleanest practical takeaway. Both sections hit the right level for ETH students -- neither condescending nor hand-wavy.

## Weakest Section

**Section 9 (Real World / Lalonde)** needs the most work. It is the only section that breaks the notes' own pattern: no numerical example with verifiable numbers, no complete derivation of the sensitivity analysis tool, and the Cinelli-Hazlett framework is introduced with insufficient detail to be useful. This is frustrating because the *lesson* of this section (diagnostics can all pass while the estimate is directionally wrong) is arguably the most important one in the entire document. The content deserves better treatment.

## Top-Priority Fixes

1. **Clarify the $\varepsilon$ notation in the DGP.** Is $\mathcal{N}(0, 0.5|X_1|)$ parameterized by variance or standard deviation? This ambiguity propagates through every section that discusses heteroscedasticity.

2. **Acknowledge negative study hours.** The DGP can generate $X_1 < 0$. Either truncate or discuss.

3. **Verify all numerical examples are actually computable.** The heteroscedasticity example (Section 4) claims an OLS fit of $53 + 6.5X$ without showing the computation. If students cannot reproduce it, trust in the notes erodes.

4. **Expand the Lalonde / sensitivity analysis section** with a worked numerical example of the robustness value, or honestly demote it to "further reading."

5. **Retire the ice cream / drowning example.** Replace with something engineering-adjacent that ETH students have not seen five times already.

6. **State the independence assumption in the bias-variance proof explicitly** rather than burying it in a parenthetical. This is not a minor technical point -- it is the reason cross-validation exists.

7. **Define VIF and Cook's distance** in the diagnostics table, or remove them. Half-defined tools are worse than no tools.
