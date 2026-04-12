# Student Review: Regression Autopsy Lecture Notes

**Reviewer:** Lena M., 2nd-year Mechanical Engineering  
**Date:** April 2026  
**Overall impression:** These are some of the best-structured statistics notes I have encountered. The recurring exam-score dataset is genuinely helpful. But there are places where I got completely stuck, and a few where the notes assume I already know things I do not. Below is everything, section by section.

---

## 1. Introduction (Section 1)

**Rating: 8/10**

The setup is clear and I appreciate that every variable is explained in plain language. The Instagram slider story for the unobserved confounder U is vivid -- it made the idea of "unobserved" feel real instead of abstract.

### Where I got stuck
- The phrase "In the language of causal inference, Y is the dependent variable" confused me. Is "dependent variable" specific to causal inference, or is it the standard regression term? I have seen "dependent variable" in basic linear algebra / regression contexts with no causal meaning. This sentence made me think causal inference has its own vocabulary for something I already knew, and I spent time wondering what the distinction was.
- The description of X3 as a "post-treatment variable" is introduced very early but not formally defined until much later (Section 3/6). The first time I read "Including it as a control will backfire spectacularly," I had no framework for understanding WHY. I just had to trust you. That made me anxious.

### Logic gaps
- None serious. This is a setup section and it does its job.

### Stories
- The Instagram slider story works perfectly. It is concrete, it is something I can picture, and it directly maps onto the math (U ~ N(0,1)). No filler here.

### Missing prerequisites
- The notes assume I know what "causal inference" means as a field. I have heard the term but never taken a course on it. A single sentence like "Causal inference is the branch of statistics concerned with determining whether X actually causes Y, not just whether they are correlated" would help enormously.

---

## 2. The Data Generating Process (Section 2)

**Rating: 7/10**

### Where I got stuck
- **The DGP equations themselves (Definition 2.1).** I stared at these for a long time. The individual walk-throughs in plain language below are excellent, but on first reading I hit the wall of six simultaneous equations and panicked. Suggestion: put the plain-language explanations BEFORE or ALONGSIDE the equations, not after.
- **The epsilon equation** $\varepsilon \sim N(0, 0.5 \cdot |X_1|)$. This is the variance being $0.5 |X_1|$, right? But normally when we write $N(0, \sigma)$ the second argument is the standard deviation, not the variance. The heteroscedasticity definition later (Section 4) says $\text{Var}(\varepsilon_i | X_i) = h \cdot |X_1|$, which means $0.5 |X_1|$ IS the variance, so the standard deviation is $\sqrt{0.5 |X_1|}$. But the DGP notation $N(0, 0.5 \cdot |X_1|)$ is ambiguous -- is the second argument the variance or the standard deviation? This genuinely confused me. In Section 4, the notes compute $\sqrt{0.5 \cdot 1} \approx 0.71$ for the standard deviation, which confirms the second argument is the variance. But the standard convention for $N(\mu, \sigma)$ uses standard deviation. I re-read this five times. Please clarify explicitly: "where the second parameter denotes the variance, not the standard deviation."
- **plim (Remark on probability limit).** The explanation "what the estimator settles down to with unlimited data" is helpful, but I have never seen plim in any of my math or mechanics courses. I do not know what "convergence in probability" means formally. The notes say "think of it as..." which is a nice shortcut, but for the exam, do I need to know the formal definition? If so, it is missing.

### Logic gaps
- **The log in the outcome equation.** The notes say $Y = 50 + 8\log(X_1) + ...$. Is this the natural logarithm or log base 10? This matters numerically. Later the notes compute $8\log(2) \approx 5.5$, which only works for the natural log ($\ln 2 \approx 0.693$, and $8 \times 0.693 = 5.54$). Please write $\ln$ explicitly, or state the convention once.
- The "Key Insight" box on page parameters says $\beta_1 = 8$ means "each unit increase in log(hours studied) adds 8 points." Then it says "going from 1 to 2.7 hours (one log-unit)." But $e^1 \approx 2.718$, so going from 1 hour to $e$ hours is one log-unit. This is correct but only if the student knows that "one log-unit" means "multiply by e." In mechanical engineering we almost never think in natural-log units. A brief note like "because ln(e) - ln(1) = 1" would prevent confusion.

### Stories
- The causal graph (TikZ diagram) is outstanding. Having the parameter values on the arrows is exactly what I need. I kept referring back to this diagram throughout the entire document.

### Missing prerequisites
- Familiarity with matrix notation for regression ($\mathbf{X}^\top \mathbf{X}$, etc.) is assumed. I have seen this in linear algebra, but many MechE students might not connect "design matrix" to what they learned. One sentence linking it to the Ax = b systems we solve in structural mechanics would help.

---

## 3. Omitted Variable Bias (Section 3)

**Rating: 9/10**

This is the best section in the notes. The proof is short, every step is justified, and the numerical example is perfect.

### Where I got stuck
- **The auxiliary slope $\delta_1$.** The definition is clear ($\text{Cov}(X_1, X_2)/\text{Var}(X_1)$), and the notes correctly say it is "the slope from regressing $X_2$ on $X_1$." But I initially read $\delta_1$ as "the correlation between $X_1$ and $X_2$" because the formula looks similar. It is NOT the correlation -- it is the regression slope, which has different units. I figured this out from the numerical example (where $\delta_1 = -0.8$ hours-of-sleep per hour-of-studying), but a brief note on units would have saved me the confusion.
- **Collider bias proof (Proposition 3.5).** The formula $\text{Cov}(X, U | C) = \text{Cov}(X, U) - \text{Cov}(X,C) \text{Var}(C)^{-1} \text{Cov}(C,U)$ appears without derivation. Where does this come from? Is it a standard result from multivariate normal theory? I have never seen conditional covariance computed this way. The proof uses it as if it is obvious, but for me it was the hardest line in the entire document. I would appreciate either a derivation or a reference to where I can find one.

### Logic gaps
- **The proof uses plim but the theorem states E[...].** The theorem says $E[\hat\beta_1^{short}] = \beta_1 + \beta_2 \delta_1$, but the proof computes plim. These are different things (expectation vs. probability limit). The result is the same for this linear case, but the mismatch between the theorem statement and the proof bothered me. Which one is it, exactly?
- **The "When OVB Cannot Be Signed" subsection** is only three sentences. It introduces the idea that with multiple omitted variables the bias direction is indeterminate, but gives no formula and no example. Either expand it or cut it -- as-is, it just made me nervous without teaching me anything.

### Stories
- **The Sunscreen Murder Mystery** is perfect. Ice cream, drownings, hot weather -- I immediately understood the structure of OVB. This is the gold standard for how a toy story should work.
- The sleeping/studying numerical example is also perfect. I verified every number on paper.

### Missing prerequisites
- The proof uses properties of covariance (linearity, $\text{Cov}(X, \varepsilon) = 0$ from the conditional mean assumption). I happen to know these, but many MechE students might not. A one-line reminder that $\text{Cov}(aX + bY, Z) = a\text{Cov}(X,Z) + b\text{Cov}(Y,Z)$ would help.

---

## 4. Heteroscedasticity (Section 4)

**Rating: 7/10**

### Where I got stuck
- **The sandwich formula (Theorem 4.2).** I understand the structure: bread-meat-bread. But the notes do not show how to go from "OLS is unbiased" to the variance formula. The proof in the Repair Box (derivation of the sandwich estimator) fills this gap later, but by the time I reached Theorem 4.2, I was stuck. Consider moving the derivation up, or at least forward-referencing it.
- **The Breusch-Pagan test.** The statement "Under $H_0$, $nR^2 \sim \chi^2_p$ asymptotically" is presented as a fact. I have never seen the chi-squared distribution in any of my courses. The notes explain $R^2$ (good) and test statistics in general (good), but the leap to "this particular statistic follows a chi-squared distribution" is not justified at all. I understand this is an asymptotic result and proving it might be out of scope, but I do not even know what a chi-squared distribution LOOKS like. A sentence like "The chi-squared distribution with p degrees of freedom is the distribution of the sum of p squared standard normals" would give me something to hold onto.
- **The remark about $\Omega$ being diagonal** is very helpful. I was indeed confused about whether heteroscedasticity means correlated errors. This remark cleared it up. Thank you.

### Logic gaps
- The claim "OLS remains unbiased" under heteroscedasticity is stated without proof. I believe it (unbiasedness comes from $E[\varepsilon | X] = 0$, which has nothing to do with the variance structure), but the notes should say this explicitly rather than leaving me to figure out why.
- The warning that robust SEs perform poorly for $n < 50$ is useful but has no justification. Why does the sandwich estimator break down? The notes say "each individual $\hat\varepsilon_i^2$ is a noisy estimate of $\sigma_i^2$" -- OK, but why does averaging not fix this? Is it because the $(X^\top X)^{-1}$ amplifies the noise? I would like one more sentence.

### Stories
- **Drunk Darts** is good but slightly too long. The core analogy (more beers = more spread) is clear in the first three sentences. The rest is elaboration I did not need. The apartment rent remark, by contrast, is concise and perfectly placed.
- **The "Everyday Wisdom" insight box** (lottery tickets, putting yourself out there) felt like filler. It does not map cleanly onto the math. I skipped it on re-reading.

### Missing prerequisites
- Chi-squared distribution (see above).
- The concept of "consistency" of an estimator is used but only formally defined later (in the IV section). On first read through Section 4, I did not know precisely what "consistent under heteroscedasticity of unknown form" meant.

---

## 5. Significance vs. Effect Size (Section 5)

**Rating: 9/10**

### Where I got stuck
- The power formula: $\text{Power} \approx \Phi(|\beta_j|/(\sigma/\sqrt{n}) - z_{\alpha/2})$. I can parse this, but I had to think carefully about what $\Phi$ is (CDF of the standard normal -- stated, thankfully). The intuition "power increases with effect size and sample size" is clear. The formula itself I would need to practice with numbers to feel comfortable.

### Logic gaps
- The multiple testing proof is clean and uses only linearity of expectation. No gaps. This is a model proof for students at my level.
- However, the Bonferroni correction is stated without explaining WHY testing at $\alpha/m$ controls the family-wise error rate. This is a one-line argument (union bound / Boole's inequality: $P(\text{at least one false positive}) \leq \sum P(\text{false positive}_j) = m \cdot \alpha/m = \alpha$), and including it would make the section self-contained.

### Stories
- **The Seat Number story** is perfect. I laughed and then understood. This is exactly the kind of story that works: absurd enough to be memorable, directly mapping onto the math ($t = \hat\beta / \text{SE}$, large $n$ shrinks SE).
- **The Keyboard example** is also perfect. The table with three sample sizes makes the point visually immediate.

### Missing prerequisites
- The $t$-distribution is mentioned ("follows a $t$-distribution with $n-p$ degrees of freedom"). I know what this is from my statistics intro, but the explanation of WHY we use $t$ instead of normal (estimating $\sigma$ inflates tails) is helpful and sufficient. Good job here.

---

## 6. Specification Error (Section 6)

**Rating: 8/10**

### Where I got stuck
- **Theorem 6.1 (Linear Projection Under Misspecification).** The statement $\beta^* = \arg\min E[(Y - X\beta)^2]$ is clean, but I want to see the explicit solution. Is $\beta^* = E[XX^\top]^{-1} E[XY]$? The theorem just says "best linear approximation" without giving me the formula I would use. I think the answer is yes (population OLS), but this should be stated.

### Logic gaps
- The numerical example (Diminishing Returns table) is great, but the linear fit $\hat{Y} = 52.5 + 1.6 X_1$ appears out of nowhere. How was it obtained? Was it OLS on the log-generated data? For a section about specification error, I want to see the misspecified OLS computation, not just its output.
- The Repair Box says "fit the correctly specified model by transforming the predictor." But how would I KNOW the true form is logarithmic in practice? The notes never address specification testing or model selection for functional form (beyond cross-validation, which appears later). This felt like a gap.

### Stories
- **The Straight Ruler on a Winding Road** is excellent. Clear, visual, and maps directly onto in-sample fit vs. extrapolation failure.

### Missing prerequisites
- The concept of argmin is used. I know it from optimization courses, but it is worth defining for students who might not.

---

## 7. Overfitting (Section 7)

**Rating: 8/10**

### Where I got stuck
- **The bias-variance proof.** The cross-term vanishing step: "because $\varepsilon$ is independent of $\hat{f}$ (trained on separate data)." Wait -- separate data? This is the first mention that $\hat{f}$ must be trained on data independent of the test point $(x_0, Y)$. In practice, we train on the same dataset we are evaluating on (unless we do train/test split). This assumption is critical and deserves more emphasis. I re-read the proof three times before I understood that the decomposition applies to the EXPECTED error on a NEW point, not the training error.
- **The expansion** $E[(f - \hat{f})^2] = (f - \mu)^2 + E[(\hat{f} - \mu)^2]$. This step uses the bias-variance decomposition of a single random variable, which is just $E[(X - c)^2] = (E[X] - c)^2 + \text{Var}(X)$ for constant $c$. This is true but not obvious to someone seeing it for the first time. A hint like "this is the standard identity $E[(X-c)^2] = (EX - c)^2 + \text{Var}(X)$" would save a lot of confusion.

### Logic gaps
- The table showing Training $R^2$ vs. Test $R^2$ for degrees 1, 3, 7, 15 is powerful but the numbers are presented without showing how they were computed. Are these from the exam score DGP? With what sample size? How was the test set constructed? For a section about overfitting, the methodology behind these numbers matters.
- **Cross-validation.** The definition of k-fold CV is correct but the notes never explain WHY averaging MSE across folds gives an honest estimate of prediction error. The key insight (each fold acts as held-out data the model has never seen) is mentioned in passing but not formalized.

### Stories
- **The Three Dartboard Players** maps perfectly onto bias, variance, and irreducible noise. One of the best stories in the document. I would remember this in an exam.

### Missing prerequisites
- The concept of $R^2 < 0$ (test $R^2$ for the degree-15 polynomial) is mentioned without explanation. How can $R^2$ be negative? I think this happens when the model predicts worse than the sample mean, but this is never stated. A student who only knows $R^2 \in [0,1]$ will be confused.

---

## 8. Causation and Bad Controls (Section 8)

**Rating: 7/10**

### Where I got stuck
- **The IV estimator formula** $\hat\beta_{IV} = (Z^\top X)^{-1} Z^\top Y$. This looks like the OLS formula but with $Z$ replacing $X$ in some places. But $Z^\top X$ is not necessarily square (if there are multiple instruments or controls), so $(Z^\top X)^{-1}$ does not obviously exist. The notes only consider the just-identified case (one instrument for one endogenous variable), but this should be stated explicitly.
- **The IV consistency proof.** The step $\text{plim} = \text{Cov}(Z,Y)/\text{Cov}(Z,X) = \beta$ requires: $\text{Cov}(Z,Y) = \beta \cdot \text{Cov}(Z,X) + \text{Cov}(Z,\varepsilon)$, and $\text{Cov}(Z,\varepsilon) = 0$ by exclusion. This is fine, but the notes skip the intermediate algebra. I had to fill in $Y = X\beta + \varepsilon$, so $\text{Cov}(Z,Y) = \text{Cov}(Z, X\beta + \varepsilon) = \beta \text{Cov}(Z,X) + \text{Cov}(Z,\varepsilon)$ myself. The steps are simple but they should be shown -- this is a theorem proof.

### Logic gaps
- **The Collider Bias proposition (Proposition 8.1)** is essentially the same as Proposition 3.5 from the OVB section, but restated in a different context. The overlap is confusing -- I was not sure if this was a new result or a callback. A sentence like "This is the same mechanism as Proposition 3.5, now applied to the causal inference setting" would help.
- **The F-statistic of the first stage.** The rule of thumb $F > 10$ is stated but not derived or justified. Where does 10 come from? Is it arbitrary? I accept it as a practical guideline, but acknowledging that it is a heuristic (from Stock and Yogo, I think?) would be honest.

### Stories
- **"Why Every Movie Star's Spouse Seems Boring"** is clever and memorable. It maps directly onto collider bias. Good.
- **The Talent/Luck/Fame numerical example** is outstanding. I verified all the numbers. Seeing independence break down by conditioning on Fame was the moment collider bias finally clicked for me.

### Missing prerequisites
- Potential outcomes notation ($Y_0$, $Y_1$) appears in the RDD section (Section 9) without any prior introduction. What are potential outcomes? This is a causal inference concept that I have never seen in any MechE course. The notes should either define it or avoid the notation.

---

## 9. RDD (Section 9)

**Rating: 7/10**

### Where I got stuck
- **"Under continuity of potential outcomes at c."** What does this assumption mean? Intuitively I think it means "students just above and just below the cutoff are similar," but the formal statement uses $E[Y_0 | R = r]$ and $E[Y_1 | R = r]$ being continuous. These $Y_0, Y_1$ are potential outcomes that were never defined. I had to guess what they mean (outcome under no treatment and outcome under treatment). This is the single biggest prerequisite gap in the notes.
- **Bandwidth choice.** The bias-variance tradeoff here (narrow = low bias, high variance; wide = opposite) is stated but not formalized. How exactly does bias grow with bandwidth? Is it linear? Quadratic? The notes mention optimal bandwidth methods by name but do not explain the principle behind them.

### Logic gaps
- **The RDD identification theorem** is stated but not proved. Even a sketch would help -- the key step is that continuity of $E[Y_0 | R = r]$ at $c$ means $\lim_{r \uparrow c} E[Y | R = r] = E[Y_0 | R = c]$, because everyone just below $c$ is untreated. Similarly for $Y_1$ from above. The jump is therefore $E[Y_1 - Y_0 | R = c]$. This is three lines and would make the result feel earned rather than handed down.

### Stories
- **"The Kid Who Scored 69 vs. 70"** is perfect. Immediately intuitive. I could explain RDD to a friend using this story.

### Missing prerequisites
- Potential outcomes framework (see above).
- Local polynomial regression (mentioned implicitly in "fit lines on each side").

---

## 10. The Real World (Section 10)

**Rating: 6/10**

This is the most important section conceptually but the least developed mathematically. I understand why -- the point is that math alone cannot save you -- but I left feeling like I could not DO anything with this knowledge.

### Where I got stuck
- **The Cinelli-Hazlett framework.** The robustness value definition uses "partial $R^2$" without defining it. I know what $R^2$ is, but partial $R^2$? Is it the $R^2$ from a regression of one variable on another after controlling for everything else? The formal formula $\text{RV}_{q,\alpha}$ is opaque -- I have no idea how to compute it from this description alone.
- The tutoring story is compelling, but the notes never show me how to USE sensitivity analysis. A numerical example of computing the robustness value (even a toy one) would make this section actionable.

### Logic gaps
- The Lalonde dataset is described but no data or regression output is shown. I am told "observational estimate is negative, experimental estimate is positive" but cannot verify anything. This is the only section where I have to take the notes' word for it entirely.

### Stories
- **The Tutoring story** is the best analog of the Lalonde problem. It made the abstract point concrete. However, it would be even more powerful if accompanied by a numerical example.

### Missing prerequisites
- Partial $R^2$ (see above).
- The concept of a randomized controlled trial (RCT) is mentioned but not defined. Most MechE students know what an experiment is, but "RCT" as a technical term should be spelled out.

---

## 11. Frisch-Waugh-Lovell (Section 11)

**Rating: 9/10**

This might be the most illuminating section for me personally. I have been told to "control for X" in every stats class but never understood what it MEANS mechanically. Now I do.

### Where I got stuck
- **The residual-maker matrix $M_2$.** I know what projection matrices are from linear algebra. But the notation $M_2 = I - X_2(X_2^\top X_2)^{-1} X_2^\top$ is dense. A one-line reminder: "this is the matrix that, when applied to any vector, returns the residuals from regressing that vector on $X_2$" appeared implicitly in the theorem statement, but putting it right after the definition of $M_2$ would help.
- The proof is complete and I could follow every step. This is one of the cleanest proofs in the notes.

### Logic gaps
- The numerical example computes $\tilde{Y}$ and $\tilde{X}_1$ but does not show the intermediate regressions (the fitted values, the subtraction). I had to redo them on paper to verify. Showing one more intermediate step (e.g., "Person A's predicted mood from sleep alone is $Y_{A,pred} = ... $, so residual is $3 - ... = -1.2$") would make the example fully self-contained.

### Stories
- **The Coaching vs. Shoes story** is the best FWL explanation I have ever seen. The three concrete steps (remove what shoes explain about speed, remove what shoes explain about coaching, compare leftovers) are crystal clear. The follow-up "But wait, how can I subtract out the shoe effect if I haven't measured it yet?" addresses exactly the objection I had while reading.

### Missing prerequisites
- Projection matrices. Covered in my linear algebra course, but many students forget. A brief reminder of orthogonal projection would help.

---

## 12. Diagnostics Toolkit & Theorem Map (Sections 12-13)

**Rating: 7/10**

### Where I got stuck
- Several diagnostics in the table (VIF, Cook's distance, Durbin-Watson, Jarque-Bera) are named but never defined in the notes. The Breusch-Pagan test was properly developed, but the others appear only as rows in a summary table. For an exam, would I need to know what VIF stands for and how to compute it? If so, this is a gap.

### Logic gaps
- The Theorem Map table is a nice high-level summary. The claim "you cannot meaningfully discuss power (NB 3) without first understanding correct standard errors (NB 2)" is a good structural point. No logic gaps here.

### Stories
- The cockpit analogy (diagnostics = instrument panel, all gauges green does not mean the flight plan is correct) is memorable and well-placed.

---

## Global Issues

### Notation consistency
- The notes sometimes use $\hat\beta$ and sometimes $\hat\beta_{OLS}$ for the OLS estimator. This is fine in context but I had to check each time whether they meant "OLS specifically" or "any estimator."
- The use of $\varepsilon$ for both the true error and the DGP noise, vs. $\hat\varepsilon$ for residuals, is standard but could be stated explicitly as a convention early on.

### What I wish existed
1. **A notation table** at the beginning: $E$, Var, Cov, plim, $\bhat$, $\bols$, $\biv$, $M_2$, etc. I kept flipping back to find definitions.
2. **A "prerequisites" box** at the start listing what math I need: linear algebra (matrix multiplication, inverses, projection), probability (expectation, variance, covariance, normal distribution), and basic calculus (logarithms, derivatives). This would let me self-assess before starting.
3. **Practice problems.** I learn by doing. The numerical examples are great but they are worked out for me. I want exercises where I have to compute the OVB formula myself, or verify the sandwich estimator on a small dataset.

### Where the notes are strongest
- The recurring exam-score dataset. Coming back to the same variables in every section creates continuity. When the coefficient on study hours changes due to OVB, I remember what it was before. This is brilliant pedagogy.
- Every proof is short and self-contained. No proof exceeds half a page. This is perfect for my level.
- The numerical examples. I verified every one on paper. They all check out. This builds trust.

### Where the notes are weakest
- Sections 9 (RDD) and 10 (Real World) feel rushed compared to the earlier sections. The density of intuition and worked examples drops noticeably.
- Some concepts are used before they are defined (potential outcomes, partial $R^2$, consistency, chi-squared distribution).
- The notes never address what to do when you SUSPECT misspecification but do not know the true functional form. Section 6 says "use log(X)" but only because we know the DGP. In practice, I would not know the DGP.

---

## Section-by-Section Confidence Ratings (1-10 for exam readiness)

| Section | Topic | Rating | Main Barrier |
|---------|-------|--------|-------------|
| 1 | Introduction | 8 | Fine, minor terminology confusion |
| 2 | DGP | 7 | Epsilon variance vs. SD ambiguity; log vs. ln |
| 3 | OVB | 9 | Conditional covariance formula in collider proof |
| 4 | Heteroscedasticity | 7 | Chi-squared distribution unknown; BP test not fully motivated |
| 5 | Significance | 9 | Power formula needs practice |
| 6 | Specification Error | 8 | Would not know how to detect misspecification in practice |
| 7 | Overfitting | 8 | Bias-variance proof assumption about independent test data |
| 8 | Causation / IV | 7 | IV formula assumptions; potential outcomes undefined |
| 9 | RDD | 7 | Potential outcomes; bandwidth theory missing |
| 10 | Real World | 6 | Partial R-squared undefined; no worked sensitivity example |
| 11 | FWL | 9 | Clean and complete |
| 12-13 | Diagnostics / Map | 7 | Many diagnostics named but undefined |

**Weighted average confidence: approximately 7.5/10.** I could pass an exam on this material, but there are at least four places where a hard question would expose a gap (conditional covariance formula, chi-squared distribution, potential outcomes, sensitivity analysis computation).
