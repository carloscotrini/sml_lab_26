# Pedagogical Redesign Proposals for "Regression Autopsy" Lecture Notes

**Reviewer:** Creative Pedagogist (Learning Science & Active Learning Specialist)
**Date:** April 2026
**Sources consulted:** All four student reviews (Lena, Max, Niklas, Sofia) and the full lecture notes.

---

## Overarching Diagnosis

The notes have an unusually strong foundation: a single recurring dataset, short proofs, vivid toy stories, and verifiable numerical examples. This is already better than 90% of STEM lecture material. The problems are structural, not content-level:

1. **The notes lead with formalism and follow with intuition.** Research on cognitive load (Sweller, 1988; Mayer's modality principle) shows this is backwards. Students who hit a wall of equations before they have a mental model to hang them on experience extraneous cognitive load -- they are spending effort parsing syntax rather than building understanding.

2. **Passive consumption dominates.** Every section is read-only. There are no prediction moments, no commit-then-reveal sequences, no peer discussion prompts. The worked examples are excellent but they are done FOR the student, never BY the student. Bjork's "desirable difficulties" framework says retrieval practice and generation effects produce stronger learning than passive review.

3. **Forward references create anxiety.** Lena flagged this explicitly: terms like "post-treatment variable" and "collider bias" appear sections before they are defined. This violates the prerequisite ordering principle. Students either zone out or become anxious.

4. **No mechanism for self-assessment.** Without practice problems or self-check questions, students cannot calibrate what they know. Lena's request for practice problems and Max's "what do I need for the exam" refrain both point to this gap.

Below, I propose specific changes section by section, organized under five headings: cognitive load management, active learning insertions, scaffolding fixes, desirable difficulty opportunities, and assessment alignment.

---

## Section 1: Introduction

### Cognitive Load Management

| Action | Content | Rationale |
|--------|---------|-----------|
| **KEEP** | The exam-score dataset with all five variables; the Instagram slider story | This is the narrative spine. Every student praised it. |
| **CUT** | The phrase "In the language of causal inference, Y is the dependent variable" | It confuses rather than clarifies. "Dependent variable" is standard regression vocabulary, not specific to causal inference. Lena flagged this directly. |
| **MOVE to a "Prerequisites" box** | The definition of causal inference as a field | Add one sentence at the top: "Causal inference is the branch of statistics that asks whether X actually causes Y, not merely whether they are correlated." This costs 15 words and prevents the anxiety Lena described. |
| **SHORTEN** | The U (self-discipline) bullet point | Max said it "goes on forever." Keep the Instagram slider hook and the key sentence about U driving both X1 and Y. Move the detailed mechanism ("through paying attention in class, doing practice problems...") to the DGP section where it belongs. |
| **DEFER** | The X3 (self-assessed performance) description | Do NOT describe collider bias here. Instead, write: "X3 is a trap variable. We will reveal why in Section 8. For now, just note that it is measured AFTER the exam." This reduces forward-reference anxiety while preserving suspense. |

### Active Learning Insertion

**Activity: "Predict the Confounder" (2 minutes)**
Before revealing U, display only X1 (hours studied), X2 (lectures attended), and Y (exam score). Ask students: "What hidden variable could be driving both study hours and exam scores, making it look like studying helps more than it actually does? Write one candidate on a piece of paper." Give 60 seconds. Then reveal the Instagram slider story. This is a "generate before you receive" moment -- students who commit to a guess process the reveal more deeply (generation effect, Slamecka & Graf 1978).

### Scaffolding Fix

Add a one-page "Prerequisites and Notation" box before Section 1 begins:
- List required background: matrix multiplication, inverses, expectation, variance, covariance, normal distribution, natural logarithm
- Define notation: E, Var, Cov, hat notation, plim (informal)
- State convention: N(mu, sigma^2) means the second argument is the VARIANCE throughout these notes

This addresses Lena's request for a notation table and Max's implicit need to know what is exam-relevant.

### Desirable Difficulty

None in this section -- it is a setup section and should feel welcoming, not challenging.

### Exam-Style Question

> "A researcher finds that students who drink more coffee score higher on exams. She concludes that coffee improves exam performance. Name one plausible unobserved confounder, state the direction of the bias it would create, and explain whether the true effect of coffee is likely larger or smaller than the OLS estimate."

This tests the ability to reason about confounding without any formulas -- pure conceptual understanding.

---

## Section 2: The Data Generating Process

### Cognitive Load Management

| Action | Content | Rationale |
|--------|---------|-----------|
| **RESTRUCTURE** | The six structural equations (Definition 2.1) | Currently: wall of six equations, THEN plain-language walkthroughs. Restructure to: causal graph FIRST (the TikZ diagram, which both Lena and Max praised), then each equation introduced ONE AT A TIME with its plain-language explanation immediately alongside. Never show all six at once before explaining them. |
| **KEEP** | The causal graph, all plain-language paragraphs, the "Numbers Behind the Story" box | These are the strongest elements. |
| **CUT** | The "Pathologies Embedded in the DGP" list (Section 2.4) | This is a table of contents for the rest of the course disguised as content. It front-loads six concepts students have not encountered yet. Replace with a single sentence: "This DGP contains multiple hidden problems. Each of the following sections will isolate and dissect one." |
| **CLARIFY** | The epsilon notation | Add explicitly after Eq. 2.4: "Convention: throughout these notes, N(0, v) means the second parameter is the VARIANCE, so the standard deviation is sqrt(v). Here, Var(epsilon) = 0.5|X1| and SD(epsilon) = sqrt(0.5|X1|)." This resolves the ambiguity that confused both Lena and Niklas. |
| **CLARIFY** | log vs. ln | Add once: "Throughout these notes, log denotes the natural logarithm (base e). We write log rather than ln for notational compactness." |

### Active Learning Insertion

**Activity: "Build the DGP from the Story" (3 minutes)**
Show students the causal graph with arrows but WITHOUT the equations on them. Give them this prompt: "The first hour of studying helps a lot, but the tenth hour barely helps. Which mathematical function has this property? (a) linear, (b) quadratic, (c) logarithmic, (d) exponential." Live poll or hand-raise. Then reveal: "It is (c), logarithmic -- and that is why the DGP uses 8 log(X1)."

Follow up: "Self-discipline drives both studying and scores. If discipline goes up by 1 SD, do you think study hours go up by a lot or a little?" (Hand-raise: a lot vs. a little.) Reveal: gamma_1 = 0.5 hours per SD. "Surprisingly modest -- but even this small link is enough to create serious bias."

### Scaffolding Fix

- Add one sentence before the causal graph: "A causal graph shows which variables cause which. An arrow from A to B means A directly causes B. A dashed node means the variable is unobserved by the analyst."
- Max specifically requested this: "You never actually explain what a causal graph IS before showing one."
- Add the "one log-unit" clarification Lena requested: "Going from 1 to e (approx 2.72) hours is one log-unit, because ln(e) - ln(1) = 1."

### Desirable Difficulty

**The Negative Study Hours Trap:** Niklas caught that the DGP can generate X1 < 0. Rather than silently fixing this, USE it as a teaching moment. After presenting the DGP, add: "Quick check: can this DGP produce a student with negative study hours? If so, what does that tell you about the limitations of assuming normality for a naturally non-negative variable?" This is a legitimate modeling concern that teaches students to interrogate assumptions.

### Exam-Style Question

> "Suppose you change the DGP so that self-discipline U has NO effect on lectures attended (gamma_2 = 0). Which arrow disappears from the causal graph? Does omitting lectures from the regression still bias the coefficient on study hours? Explain using the OVB formula."

This tests whether students understand the mechanics of confounding, not just the formula.

---

## Section 3: Omitted Variable Bias

### Cognitive Load Management

| Action | Content | Rationale |
|--------|---------|-----------|
| **KEEP** | The OVB theorem, proof, numerical example, visualization spec, collider bias subsection | This is the highest-rated section across all four reviewers. Do not touch the core. |
| **CUT** | "When OVB Cannot Be Signed" (Section 3.3) | All four reviewers flagged this: it is three sentences, raises anxiety, and teaches nothing actionable. Either expand it with a numerical example or remove it entirely. Recommendation: remove it. It can go in an appendix for advanced readers. |
| **MOVE the Collider Trap subsection** | To Section 8 (Endogeneity and Bad Controls) | Max said it "deserves its own section." He is right. Encountering collider bias inside the OVB section is cognitively jarring -- students think they are still learning about omitting variables, and suddenly the concept of "controlling for too much" appears. The collider material belongs with the bad controls discussion. Keep a one-sentence forward reference: "Not all omissions are bad -- sometimes ADDING a variable creates bias. We will see this in Section 8." |
| **REPLACE** | The ice cream/drowning story | Niklas and Sofia both flagged this as overused. Replace with an engineering-adjacent example: "Countries that eat more chocolate per capita win more Nobel Prizes (real published correlation, Messerli 2012). Does chocolate make you smarter? No -- wealthy countries can afford both chocolate and research universities. Wealth is the omitted variable." This is memorable, real, and not the example every other stats course uses. |

### Active Learning Insertion

**Activity: "Sign the Bias" (3 minutes)**
After presenting the OVB formula but BEFORE the numerical example, give students three scenarios. For each, they must determine the sign of the bias:

1. "You regress income on years of education, omitting IQ. Assume: IQ positively affects income, IQ is positively correlated with education. Is the bias on education positive or negative?" (Positive -- OLS overestimates the return to education.)
2. "You regress marathon time on weekly training miles, omitting age. Assume: older runners are slower (positive effect on time), older runners train more miles (positive correlation). Is the bias on training positive or negative?" (Positive -- OLS underestimates the benefit of training, because the coefficient on time is positive.)
3. "You regress exam score on hours studied, omitting hours slept. Assume: sleep helps scores (positive), studying more costs sleep (negative correlation). Sign the bias." (Negative -- OLS underestimates the studying effect.)

Scenario 3 is the numerical example that follows. Students who committed to a sign will engage more deeply when verifying with numbers.

### Scaffolding Fix

- Add a one-line reminder of covariance linearity before the proof: "Recall: Cov(aX + bY, Z) = a Cov(X,Z) + b Cov(Y,Z). We use this in the next three lines."
- Clarify the delta_1 units in the numerical example: "delta_1 = -0.8 hours of sleep per hour of studying. This is not a correlation (which is unitless); it is a regression slope (which has units)."
- Address the E[...] vs. plim mismatch Lena flagged: add a one-sentence remark after the proof: "The theorem is stated in terms of E[...] and the proof uses plim. For the linear model with non-stochastic regressors, these coincide. For stochastic regressors (our case), the plim version is the precise statement."

### Desirable Difficulty

**The Proxy Trap:** After presenting the proxy variable approach, pose this: "Your proxy for self-discipline is 'number of library visits per week.' This correlates with discipline at q = 0.6. But library visits also directly affect exam scores (you study more effectively in the library). Is this proxy safe to use? What could go wrong?" The answer: if the proxy has a direct effect on Y not mediated through X1, including it changes the interpretation of the coefficient. This is a genuine statistical subtlety that forces students to think about causal structure, not just formulas.

### Exam-Style Question

> "A researcher regresses country GDP on foreign aid received, omitting institutional quality. She finds that aid has a negative effect on GDP. Using the OVB formula, determine the sign of the bias under these assumptions: (i) better institutions increase GDP, (ii) countries with worse institutions receive more aid. Could the true effect of aid be positive? Show your reasoning."

---

## Section 4: Heteroscedasticity

### Cognitive Load Management

| Action | Content | Rationale |
|--------|---------|-----------|
| **KEEP** | Drunk Darts story, apartment rent remark, CI definition, sandwich formula STATEMENT, Breusch-Pagan logic, numerical example, robust SE repair box | Core content that works. |
| **CUT** | The "Everyday Wisdom" insight box (lottery tickets, putting yourself out there) | Lena explicitly said "felt like filler. It does not map cleanly onto the math. I skipped it on re-reading." Sofia was the only one who liked it, and even she would not bring it up at dinner. |
| **MOVE to appendix** | The sandwich estimator PROOF (lines 669-683) | Max: "Pure algebra. Correct, clear, and absolutely dead on arrival for engagement." Niklas can look it up. Add a "skip to the punchline" summary before the proof: "Punchline: each observation gets to vouch for its own noise level, instead of forcing everyone to share the same estimate. The proof (below / in Appendix B) is short matrix algebra." |
| **SHORTEN** | The confidence interval explanation (lines 511-529) | Niklas: "Every ETH student in their 4th year has heard the '95% does not mean 95% probability' speech at least three times." Cut the paragraph of explanation. Keep the definition and one sentence of clarification. |
| **CLARIFY** | The 82% coverage claim | Niklas demanded a source. Add: "This 82% is from a Monte Carlo simulation of the specific DGP in Section 2 with n=500; coverage depends on the DGP structure." |
| **ADD** | A one-sentence definition of the chi-squared distribution | Before the Breusch-Pagan test: "The chi-squared distribution with p degrees of freedom is the distribution of the sum of p independent squared standard normal variables. It is always non-negative, right-skewed, and becomes approximately normal for large p." This costs two sentences and resolves Lena's biggest gap in this section. |

### Active Learning Insertion

**Activity: "Spot the Funnel" (2 minutes)**
Before revealing the heteroscedasticity definition, display a scatterplot of exam scores vs. hours studied (generated from the DGP, with the funnel shape visible). Ask: "Look at this scatterplot. Something is different about the spread of scores at the left side vs. the right side. What do you notice? Turn to your neighbor and describe the pattern in one sentence."

After 60 seconds, cold-call two pairs. Then reveal: "The spread fans out. This is called heteroscedasticity, and it means your confidence intervals are lying."

This is a "notice before you name" activity -- students who discover the pattern themselves encode the concept more deeply than those who are handed the Greek word first.

### Scaffolding Fix

- Define "consistency" before using it: "An estimator is consistent if it converges to the true parameter value as n grows to infinity. We will see this formally in Section 8 (IV), but for now: consistent = 'gets it right with enough data.'"
- Remove the forward reference to t-statistics in the Breusch-Pagan "Contrast" paragraph. Move it to Section 5, where t-statistics are actually introduced, as a backward reference instead.

### Desirable Difficulty

**The Small-Sample Trap:** After presenting robust SEs, pose this: "You have data on 15 students. You detect heteroscedasticity with Breusch-Pagan. Should you use robust standard errors? Why or why not?" Most students will say yes (because the section just taught them to). The correct answer is: probably not -- with n=15, the sandwich estimator is noisier than the classical one. This forces students to internalize the warning box rather than skimming it.

### Exam-Style Question

> "You regress apartment rent on apartment size for 200 Zurich listings. The Breusch-Pagan test gives nR^2 = 14.3 with 1 degree of freedom (critical value at 5%: 3.84). (a) Do you reject homoscedasticity? (b) Your OLS coefficient on size is 15.2 CHF/m^2 with classical SE = 2.1. A colleague says 'the coefficient is wrong because of heteroscedasticity.' Is she correct? What exactly is wrong?"

This tests the crucial distinction: heteroscedasticity biases SEs, not coefficients. The most common student error is thinking the coefficient itself is biased.

---

## Section 5: Significance vs. Effect Size

### Cognitive Load Management

| Action | Content | Rationale |
|--------|---------|-----------|
| **KEEP everything** | Seat number story, keyboard example, t-statistic derivation, multiple testing proof, Bonferroni correction | This is the highest-rated section (8-9 from every reviewer). It exemplifies the ideal structure: story first, math minimal, examples doing the heavy lifting. |
| **CUT** | Nothing | This section is the template for how every other section should be restructured. |
| **ADD** | The Bonferroni proof (one line) | Lena asked for it: "P(at least one false positive) <= sum P(false positive_j) = m * alpha/m = alpha." This is literally one line and makes the section self-contained. |
| **ADD** | One paragraph on the replication crisis | Sofia requested this and she is right: "This is why psychology had a replication crisis. Researchers found 'significant' effects of power posing and social priming in huge samples -- effects so small they evaporated on replication. The p-value said 'real.' The effect size said 'who cares.'" This is one paragraph and it makes the section feel urgent rather than academic. |

### Active Learning Insertion

**Activity: "The Significance Lottery" (3 minutes)**
Before the seat number reveal, run this live: "I am going to test whether your student ID number predicts your exam grade. Raise your hand if you think this will be statistically significant." (Most hands stay down.) "Now suppose I do this for 50,000 students over 10 years." (Some hands go up.) "The result: p = 0.002. Your student ID 'significantly predicts' your grade."

Pause. Let the discomfort sit. Then ask: "What went wrong? Turn to your neighbor -- 30 seconds." This is the "commit before the reveal" pattern. Students who publicly predicted "not significant" will feel the sting of the counterexample more acutely.

### Scaffolding Fix

- The power formula can stay but add a worked micro-example immediately after it: "With beta = 0.1, sigma = 2, n = 50: Power = Phi(0.1/(2/sqrt(50)) - 1.96) = Phi(0.354 - 1.96) = Phi(-1.61) = 0.054. You have a 5.4% chance of detecting this tiny effect. You would need n > 3000 to reach 80% power." This makes the formula tangible.

### Desirable Difficulty

**The Power Paradox:** "A pharmaceutical company tests a new drug on 500,000 patients and finds a statistically significant improvement (p < 0.001). The drug reduces headache duration by 0.3 seconds. A competing drug, tested on 200 patients, fails to reach significance (p = 0.12) but shows a reduction of 45 minutes. Which drug would you prescribe? Why?" This forces students to pit significance against effect size in a context with real stakes.

### Exam-Style Question

> "You test 100 dietary supplements for their effect on exam performance. None of them actually works (all true effects are zero). You use alpha = 0.05 for each test. (a) How many 'significant' results do you expect? (b) A newspaper reports: 'Study finds 5 supplements boost exam scores.' Is this evidence that any supplement works? (c) What significance threshold would you need to use so that the expected number of false positives is less than 1?"

---

## Section 6: Specification Error

### Cognitive Load Management

| Action | Content | Rationale |
|--------|---------|-----------|
| **KEEP** | Straight Ruler story, extrapolation danger section, diminishing returns table, repair box | Solid content. |
| **ADD** | The explicit formula for beta* | Lena: "Is beta* = E[XX']^{-1} E[XY]? The theorem just says 'best linear approximation' without giving me the formula." Add it. One line. |
| **ADD** | Explanation of how the linear fit was obtained | Niklas: "No one actually computed this." Show the OLS computation or state the distributional assumption. |
| **ADD** | A brief note on practical specification testing | Lena: "How would I KNOW the true form is logarithmic in practice?" Add 2-3 sentences: "In practice, you do not know the true functional form. Residual plots (Section 12) can reveal systematic curvature. Cross-validation (Section 7) can compare competing specifications. Domain knowledge -- knowing that most learning processes exhibit diminishing returns -- is your strongest guide." |

### Active Learning Insertion

**Activity: "Extrapolation Roulette" (3 minutes)**
Give students the linear model: Y-hat = 52.5 + 1.6 * X1. Ask them to predict the score for a student who studied 50 hours. They compute: 132.5. "Raise your hand if you believe a student can score 132.5 on a 100-point exam." (Laughter, no hands.) "Congratulations, you just discovered specification error. The model is lying because it assumed a straight line where reality curves."

Now ask: "What would be a more reasonable prediction for 50 hours? Write a number." Collect a few answers. Then reveal the log model prediction: 81.3. This is the "predict-then-compare" structure.

### Scaffolding Fix

- Define argmin in a margin note: "argmin_beta f(beta) means 'the value of beta that makes f smallest.'"
- Clarify the "marginal gain" column header in the table: rename it to "Gain from doubling hours" to avoid confusion with the economic meaning of "marginal."

### Desirable Difficulty

**The Overprediction Audit:** "Your university uses the linear model Y-hat = 52.5 + 1.6X1 to predict exam scores for advising purposes. A student who studied 20 hours is predicted to score 84.5. The true score (from the log model) is about 74. How much damage does this overprediction do? What decision might a student make based on the inflated prediction?" (They might study less, thinking they are safe.) This forces students to think about the real-world consequences of specification error.

### Exam-Style Question

> "The true relationship between experience (years) and salary (CHF) is Y = 40000 + 15000 * log(X). A linear model fit on workers with 1-10 years of experience gives Y-hat = 42000 + 3200X. (a) What does each model predict for a worker with 20 years of experience? (b) Which prediction is more plausible? (c) Explain, in terms of the bias-variance tradeoff, why the linear model performs reasonably within [1,10] but fails outside it."

---

## Section 7: Overfitting and Bias-Variance

### Cognitive Load Management

| Action | Content | Rationale |
|--------|---------|-----------|
| **KEEP** | Three Dartboard Players story, bias-variance theorem statement, polynomial table, three-models numerical example | All praised across reviews. |
| **MOVE to appendix** | The bias-variance PROOF | Max will never read it. Lena can follow it but does not need it in the main text. Keep a one-line summary: "The proof (Appendix C) uses the identity E[(X-c)^2] = (EX - c)^2 + Var(X), applied to the prediction error." This hint is enough for students who want to reconstruct it. |
| **CLARIFY** | The independence assumption in the proof | Niklas flagged this as the biggest buried assumption. Add prominently: "CRITICAL: this decomposition applies to the expected error on a NEW test point, not to the training data. The noise epsilon at the test point is independent of the model f-hat, which was trained on separate data. This is why we need held-out test sets." |
| **CLARIFY** | Negative test R^2 | Lena: "How can R^2 be negative?" Add: "Test R^2 is computed as 1 - SS_res/SS_tot using the test data. Unlike training R^2, it can be negative: this happens when the model predicts worse than simply guessing the test-set mean." |
| **EXPAND** | Cross-validation | Add a small numerical example: "Take the 5 students from the OVB example. In 5-fold CV, each student is held out once. For Student A, train on B-E, predict A's score, compute the error. Repeat for each student. Average the 5 squared errors." This fills the gap Max and Lena both identified. |

### Active Learning Insertion

**Activity: "Bet on the Polynomial" (3 minutes)**
Display the polynomial-degree table but with the test R^2 column hidden. Show only training R^2: 0.71, 0.82, 0.91, 0.97. Ask: "Which polynomial degree will perform best on NEW data? Vote: degree 1, 3, 7, or 15." Most students will guess degree 15 (highest training R^2) or degree 3 (hedging). Reveal the test R^2 column. The degree-15 crash is a visceral lesson.

This is a "trap" activity designed to exploit the intuition that "higher R^2 = better model." Students who get burned remember.

### Scaffolding Fix

- State the table metadata Lena requested: "Table computed from the exam score DGP with n=200 training points and n=200 test points, averaged over 50 random draws."
- Add the identity hint Lena suggested: "This step uses the standard identity E[(X-c)^2] = (EX - c)^2 + Var(X) for any constant c. You can verify this by expanding both sides."

### Desirable Difficulty

**The Cross-Validation Trap:** "You try 500 different model specifications (polynomials, interactions, transformations) and pick the one with the best 5-fold CV score. Your selected model has CV R^2 = 0.89. Is this an honest estimate of future performance? Why or why not?" (No -- searching over 500 specs inflates the best CV score. This is the "researcher degrees of freedom" problem.) The warning box mentions this but does not make students confront it actively.

### Exam-Style Question

> "Model A has Bias^2 = 16 and Variance = 4. Model B has Bias^2 = 1 and Variance = 25. Irreducible noise is 5 for both. (a) Compute the total MSE for each model. (b) Which model would you prefer? (c) You collect 10x more training data. Which component (bias or variance) does this primarily reduce? Which model benefits more from extra data?"

---

## Section 8: Endogeneity and Bad Controls

### Cognitive Load Management

| Action | Content | Rationale |
|--------|---------|-----------|
| **KEEP** | Movie star spouse story, endogeneity definition, IV definition, IV consistency theorem, roommate numerical example, talent/luck/fame table | All praised. |
| **MOVE here** | The collider bias material from Section 3 | This is its natural home. Rename the section: "Why Your Causal Claim Is Wrong: Bad Controls, Colliders, and Instruments." Group all causal-graph reasoning in one place. |
| **ADD** | A transition between the simplified IV DGP and the main DGP | Niklas: "The switch to a simplified DGP is fine but should be flagged more explicitly." Add: "For clarity, we use a simplified DGP (linear, no log, no X2) to isolate the IV mechanics. The coefficient 3 is not the same as the 8 from the main DGP." |
| **ADD** | One sentence acknowledging exclusion is untestable | Niklas: "Exclusion is ALWAYS an assumption that cannot be tested from data." Add: "The exclusion restriction cannot be verified from data alone. It is a substantive claim about the world -- 'my roommate's habits affect my score ONLY through my own studying' -- and must be defended on domain-knowledge grounds." |
| **ADD** | One sentence on the F > 10 source | "This rule of thumb originates from Stock and Yogo (2005). It is a practical heuristic, not a theorem." |

### Active Learning Insertion

**Activity: "Name That Instrument" (3 minutes)**
After presenting the IV definition but BEFORE the roommate example, give students three candidate instruments for study hours and ask them to evaluate relevance and exclusion for each:

1. "Your roommate's study hours." (Valid -- random assignment makes it independent of U, peer effects create relevance.)
2. "The distance from your dorm to the library." (Plausible relevance, but exclusion is questionable -- living far from the library might also affect lecture attendance or sleep.)
3. "Your grade in last semester's math course." (INVALID -- past grades reflect ability/discipline, which is the confounder U itself.)

Students discuss in pairs for 90 seconds, then vote. This teaches the hardest part of IV: recognizing that finding a valid instrument requires causal reasoning, not just correlation.

### Scaffolding Fix

- Add the definition of potential outcomes BEFORE they appear in the RDD section. Place a brief definition here: "The potential outcomes framework imagines two versions of each student: Y_1 (the score they WOULD get with treatment) and Y_0 (the score they WOULD get without). The causal effect for student i is Y_1i - Y_0i. We can never observe both for the same student -- this is called the fundamental problem of causal inference."
- Show the intermediate algebra in the IV consistency proof that Lena requested: "Y = X*beta + epsilon, so Cov(Z,Y) = Cov(Z, X*beta + epsilon) = beta*Cov(Z,X) + Cov(Z,epsilon) = beta*Cov(Z,X) + 0."

### Desirable Difficulty

**The Exclusion Violation:** "Your roommate is not just influencing your study hours -- she is also explaining concepts to you directly, which improves your score through a channel other than your own study time. Does the IV estimate still recover the causal effect of YOUR study hours? What happens to the IV estimate?" (It is biased -- the exclusion restriction is violated. The IV estimate now captures a mix of your studying effect and the direct knowledge transfer.) This forces students to think critically about the most fragile assumption in IV.

### Exam-Style Question

> "A researcher wants the causal effect of class size on test scores. She uses rainfall on the first day of school as an instrument (more rain -> fewer students show up -> smaller de facto class size). (a) Is rainfall plausibly relevant? (b) Can you think of a way rainfall might violate the exclusion restriction? (c) The first-stage F-statistic is 4.2. Should you trust the IV estimate? Why or why not?"

---

## Section 9: The Real World (Lalonde / Sensitivity Analysis)

### Cognitive Load Management

| Action | Content | Rationale |
|--------|---------|-----------|
| **KEEP** | Tutoring story, the core lesson that diagnostics can all pass while the estimate is directionally wrong | This is the most important conceptual point in the entire course. |
| **EXPAND** | The sensitivity analysis section with a numerical example | Every reviewer flagged this as the biggest gap. Add a toy computation of the robustness value using simple numbers. |
| **ADD** | Definition of partial R^2 | "The partial R^2 of X with respect to Y, after controlling for W, is the R^2 from regressing the residuals of Y on W against the residuals of X on W. It measures how much additional variation X explains beyond what W already explains." |
| **ADD** | A simple numerical Lalonde-style table | Show 5 treated and 5 control observations with visible covariate imbalance, the OLS estimate, and the experimental estimate. Make it verifiable on paper. This restores the notes' own pattern. |
| **CUT** | The formal RV formula (line 1254) | In its current form it is opaque. Replace with a verbal description and the numerical example. |

### Active Learning Insertion

**Activity: "The Diagnostic False Alarm" (4 minutes)**
Present students with a regression output: coefficient = -3.0, SE = 1.2, p = 0.01, R^2 = 0.45, Breusch-Pagan p = 0.62, VIF = 1.3. All diagnostics green. Ask: "Based on this output, would you conclude that tutoring reduces exam scores? Vote yes or no."

After the vote (most will say yes -- the evidence looks strong), reveal the selection bias story. Then ask: "What information would you need, beyond what is in this regression output, to trust this result?" (Answer: knowledge of the treatment assignment mechanism -- who selected into tutoring and why.)

This is the most important "trap" in the entire course. Students who vote yes and get burned will remember the lesson.

### Scaffolding Fix

- Define "RCT" explicitly: "A randomized controlled trial (RCT) randomly assigns participants to treatment and control groups. Because assignment is random, there are no systematic differences between groups on any variable -- observed or unobserved. This is why experimental estimates are considered the gold standard."

### Desirable Difficulty

Already built into the activity above. The entire section IS a desirable difficulty -- it undermines the comforting belief that "if the diagnostics pass, the answer is right."

### Exam-Style Question

> "You estimate the effect of a job training program on wages using observational data. OLS gives a coefficient of -2500 CHF (training appears to reduce wages). All diagnostics pass. (a) Give a plausible explanation for this negative coefficient that does not involve training being harmful. (b) An RCT finds the true effect is +1800 CHF. Explain the discrepancy. (c) Without an RCT, how could you assess whether your observational estimate is trustworthy?"

---

## Section 10: Regression Discontinuity Design

### Cognitive Load Management

| Action | Content | Rationale |
|--------|---------|-----------|
| **KEEP** | The 69-vs-70 story, the scholarship numerical example, the bandwidth discussion framework | All work well. |
| **CUT** | The five surnames in the bandwidth methods reference (Imbens-Kalyanaraman, Calonico-Cattaneo-Titiunik) | Max: "You just threw five surnames at me and expected me to feel informed." Replace with: "Optimal bandwidth methods exist that balance bias and variance automatically. The details are beyond our scope, but the key insight is: narrower windows reduce bias (more comparable students) at the cost of higher variance (fewer students)." |
| **ADD** | A proof sketch for the RDD identification theorem | Lena requested this. Three lines: "Everyone just below c is untreated, so lim_{r up c} E[Y|R=r] = E[Y0|R=c]. Everyone just above c is treated, so lim_{r down c} E[Y|R=r] = E[Y1|R=c]. The jump is therefore E[Y1 - Y0 | R=c]." |
| **ADD** | Mention of manipulation as a threat | Niklas: "The most important threat to RDD is manipulation." Add: "The key assumption can fail if individuals can precisely manipulate their running variable to land just above the cutoff. If students can retake the exam or appeal their grade, the students just above 70 may be systematically different from those just below. A standard check: plot the density of the running variable near the cutoff. A suspicious spike just above the threshold suggests manipulation." |

### Active Learning Insertion

**Activity: "Find the RDD in the Wild" (3 minutes)**
After presenting the scholarship example, ask students: "Can you think of a real-world situation where a sharp cutoff determines who gets a treatment? Discuss with your neighbor for 60 seconds, then share." Examples students might generate: drinking age and accidents, speed camera thresholds and fines, GPA cutoffs for dean's list, BMI cutoffs for medical interventions. Each one is a potential RDD. This teaches students to see RDDs in everyday life.

### Scaffolding Fix

- Define potential outcomes HERE if not already done in Section 8: "Y1 is the outcome a student WOULD have if they received the scholarship. Y0 is the outcome they WOULD have without it. We observe Y1 for students above the cutoff and Y0 for students below."
- Add noise to the numerical example: Niklas noted it is unrealistically clean. Add small epsilon values so the RDD estimate is close to but not exactly 5.0, which also motivates bandwidth choice.

### Desirable Difficulty

**The Fake Discontinuity:** Show students a scatterplot with a clear jump at the cutoff. Then reveal: "This jump was created by a change in the grading rubric at the cutoff, not by the scholarship. Students above 50 had their scores inflated by the new rubric. The 'treatment effect' is an artifact." Ask: "How would you distinguish a real treatment effect from a measurement artifact at the cutoff?" This teaches the importance of understanding what generates the discontinuity.

### Exam-Style Question

> "A city imposes a speed limit of 30 km/h on streets shorter than 200 meters. A researcher uses an RDD at the 200m cutoff to estimate the effect of the speed limit on accidents. (a) What is the running variable? (b) Who is 'treated' and who is 'control'? (c) Give one reason the continuity assumption might fail. (d) If the city council can reclassify streets near 200m to change their speed limit, is the RDD still valid?"

---

## Section 11: Frisch-Waugh-Lovell

### Cognitive Load Management

| Action | Content | Rationale |
|--------|---------|-----------|
| **KEEP** | Coaching/shoes story, the three-step algorithm, the numerical example | Lena rated this 9/10 and called it "the most illuminating section." |
| **MOVE to appendix** | The block matrix proof (lines 1395-1411) | Max: "This is the densest piece of linear algebra in the entire document. I would not attempt to read this even the night before the exam." Keep a one-line summary: "The proof (Appendix D) uses the block structure of the normal equations. The key step: premultiplying both sides by M2 = I - X2(X2'X2)^{-1}X2' annihilates all X2 terms." |
| **ADD** | One intermediate step in the numerical example | Lena: "I had to redo them on paper to verify." Show one intermediate computation explicitly: "Person A's predicted mood from sleep alone: Y_pred = intercept + 1.45 * 2 = 3 + 1.45*2... Residual: 3 - 4.2 = -1.2." |
| **ADD** | A one-sentence reminder of projection matrices | "M2 is the matrix that, when multiplied by any vector v, returns the residuals from regressing v on X2. It 'projects away' the X2 component. If this is unfamiliar: think of it as the operator that answers 'what is left of v after removing everything X2 can explain?'" |

### Active Learning Insertion

**Activity: "Do the FWL by Hand" (5 minutes)**
Give students the data table from the numerical example (Exercise, Sleep, Mood for 5 people). Ask them to:
1. Regress Y on X2 and compute residuals (give them the slope: 1.45)
2. Regress X1 on X2 and compute residuals (give them the slope: 0.45)
3. Regress residual Y on residual X1

This is the only section where the activity is computation rather than prediction. The FWL theorem is best understood by DOING it. Five data points, three regressions, all arithmetic doable on a phone calculator. The payoff: when they get 4.684 and see it matches the full regression, the theorem is no longer abstract.

### Scaffolding Fix

- Note the idempotent/symmetric properties of M2 that Niklas flagged: "M2 is idempotent (M2^2 = M2: projecting twice is the same as projecting once) and symmetric (M2' = M2). These properties simplify the algebra in the proof."

### Desirable Difficulty

**The Bad Control FWL:** After the main example, pose: "Now suppose you 'control for' post-exam confidence (X3 = 0.9Y + noise). Apply FWL: what happens when you residualize Y against X3? You are removing from the exam score everything that confidence can explain. But confidence is 90% of the exam score itself! You are stripping out most of the genuine signal. What do you expect to happen to the coefficient on study hours?" (It collapses toward zero.) This makes the bad-controls warning from Section 8 concrete through the FWL lens.

### Exam-Style Question

> "You regress salary (Y) on years of experience (X1) and education level (X2). The coefficient on experience is 3200 CHF/year. Your colleague says: 'This means that if two people have the same education, one extra year of experience is worth 3200 CHF.' Using FWL, explain precisely what 'the same education' means here. Is your colleague's interpretation correct?"

---

## Sections 12-13: Diagnostics and Theorem Map

### Cognitive Load Management

| Action | Content | Rationale |
|--------|---------|-----------|
| **KEEP** | The diagnostics table, the cockpit analogy, the theorem map structure | Useful reference material. |
| **ADD** | Definitions of VIF and Cook's distance | Niklas and Lena both flagged these as named but undefined. VIF: "VIF_j = 1/(1-R^2_j), where R^2_j is the R-squared from regressing X_j on all other predictors. VIF > 10 means X_j is nearly a linear combination of the others." Cook's distance: "Cook's d_i measures how much all fitted values change when observation i is removed. d > 1 flags a point that single-handedly shifts the regression." |
| **REFRAME** | The Theorem Map | Sofia: "Frame it as a 'Previously on Regression Autopsy' TV-recap." This is a good idea. Rewrite the intro: "Think of each section as an episode. In Episode 1, you discovered your coefficient was lying (OVB). In Episode 2, you found your uncertainty was lying (heteroscedasticity). In Episode 3, your significance was lying (effect size). Each episode peeled back one more layer of deception. Here is how they connect..." |

### Active Learning Insertion

**Activity: "Diagnose This Regression" (4 minutes)**
Display a complete regression output with four diagnostic plots (residuals vs. fitted, QQ plot, scale-location, residuals vs. leverage). One plot shows a clear funnel pattern (heteroscedasticity). Ask: "Which diagnostic flag is raised? What repair would you apply? What does this NOT tell you about?" (It does not tell you about omitted variables or causal validity.)

This is a capstone activity that integrates knowledge from multiple sections.

### Exam-Style Question

> "You run a regression and all diagnostics pass: residuals are homoscedastic, normally distributed, and no influential outliers. A colleague says: 'Great, the model is correct.' Give two specific reasons why all diagnostics passing does NOT guarantee the model is correct."

---

## Global Structural Recommendations

### 1. Create an Appendix for Proofs

Move the following proofs to an appendix, replacing each with a 1-2 sentence "punchline" summary in the main text:
- Sandwich estimator derivation (Section 4)
- Bias-variance proof (Section 7)
- FWL proof (Section 11)
- Collider bias conditional covariance proof (Section 3)

This addresses Max's core complaint ("proofs should be in an appendix") without sacrificing rigor for students like Lena who want them. Label the appendix clearly: "Appendix: Complete Proofs (for exam preparation and the curious)."

### 2. Add "Punchline Before Proof" Throughout

For every theorem, add a bold one-sentence summary BEFORE the formal statement. Sofia called these "skip to the punchline" signposts. Examples:
- OVB: "Punchline: leaving out a variable that matters makes the coefficient on the included variable absorb the omitted variable's effect."
- Sandwich: "Punchline: let each observation report its own noise level instead of forcing a one-size-fits-all variance."
- Bias-variance: "Punchline: a model that memorizes noise perfectly will predict new data terribly."

### 3. Add Practice Problems

Every section should end with 2-3 practice problems (not worked examples -- problems for the student to solve). This is the single most-requested feature across all four reviews. Examples are embedded in the exam-style questions above.

### 4. Lead with Story, Follow with Math

Several sections currently lead with equations and follow with stories. Invert this for: Section 2 (DGP), Section 4 (heteroscedasticity definition before Drunk Darts), Section 6 (Theorem 6.1 before Straight Ruler). The pattern should always be: story/hook -> intuition -> formal statement -> proof (appendix) -> numerical example -> visualization.

### 5. Add a Decision Flowchart

Max requested this explicitly: "I want a flowchart." Create a one-page visual:
- "Is the variable caused by the treatment or outcome?" -> Yes: DO NOT control for it (Section 8). No: continue.
- "Is it correlated with both treatment and outcome?" -> Yes: control for it (Section 3). No: including it is harmless but adds noise.
- "Can you observe the confounder?" -> No: consider IV (Section 8) or sensitivity analysis (Section 9).
- "Is there a sharp cutoff?" -> Yes: consider RDD (Section 10).

This gives students a practical decision tool -- the kind of thing they can use at 2am when staring at data.

---

## Summary of Highest-Priority Changes

1. **Restructure Section 2** to show one equation at a time with its explanation, not all six first
2. **Move proofs to an appendix** with punchline summaries in the main text
3. **Add the "Prerequisites and Notation" box** before Section 1
4. **Clarify the variance/SD convention** for epsilon in the DGP (affects every subsequent section)
5. **Move collider material** from Section 3 to Section 8
6. **Add one active learning activity per section** (specific designs above)
7. **Expand Section 9** with a worked sensitivity analysis example and actual Lalonde numbers
8. **Add practice problems** at the end of each section
9. **Define all terms before use**: potential outcomes, partial R^2, chi-squared, VIF, Cook's distance, consistency
10. **Replace the ice cream/drowning example** with something ETH students have not seen five times
