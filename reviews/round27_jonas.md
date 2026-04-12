# Round 27 Review — Jonas (MSc, ex-Bosch manufacturing analytics)

I came to ETH to get past the "Excel plus vibes" ceiling I hit at Bosch. I read these notes with one question in my head: *would this have caught the mistakes I've actually watched destroy a regression in production?* Some of it yes. Quite a lot — no. Here is my take, honest.

---

## 1. Industrial relevance — concept-by-concept score

Scale: 1 = "wouldn't have saved us"; 5 = "this is exactly the trap I saw blow up".

| Section | Concept | Score | Comment |
|---|---|---|---|
| 3 | Omitted variable bias (OVB) | **5** | This is *the* pathology in manufacturing analytics. Our "line-speed vs. defect rate" model was a textbook OVB story — humidity and operator shift drove both. I wish I'd had the auxiliary-regression verification trick then. |
| 4 | Heteroscedasticity + sandwich SEs | **4** | Real: warranty-claim variance explodes with vehicle age/mileage. Classical SEs lied to us about a supplier effect. The note that sandwich SEs are unreliable for n < 50 is the kind of caveat you *never* see in tutorials — gold. |
| 5 | Significance vs. effect size | **5** | The seat-number story is essentially what happens every Monday in an SAP/BI shop with 10M rows. Every VP's dashboard has p < 0.001 on nothing. The "stand up if significant" exercise is the single most transferable thing in the notes. |
| 6 | Specification / extrapolation | **4** | The straight-line-on-curved-road framing maps directly to stress vs. fatigue cycles (log/power law) and to predicting warranty claims outside observed mileage. Would have caught our "predicted 107% defect rate" embarrassment in review. |
| 7 | Overfitting / bias-variance / CV | **3** | Conceptually fine, but a polynomial of degree 15 is not how people overfit in industry. In industry you overfit by **feature engineering on the whole dataset before CV**, by **tuning hyperparameters on the test set**, and by **leaky joins**. None of that is here. |
| 8 | Endogeneity / bad controls / IV | **4** | Collider framing is great. IV example (roommate study hours) is cute but not a thing I've seen deployed. In industry the usable instruments are staggered rollouts, policy changes, supplier switches — none mentioned. |
| 9 | Lalonde / sensitivity / Cinelli–Hazlett | **5** | The "all diagnostics green, sign is flipped" warning is the most important paragraph in the notes. This is exactly how our procurement team "proved" an expensive supplier was worse. Robustness value is genuinely useful; I hadn't seen it taught before. |
| 10 | RDD | **3** in industry | Beautiful method, but I've almost never had a usable cutoff at work. In pharma, credit scoring, ed-tech yes; in manufacturing no. Keep it, but do not oversell it as an everyday tool. |
| 11 | Frisch–Waugh–Lovell | **4** | I wish someone had beaten this into me at 22. "Controlling for" gets used as a magic spell in every DS stand-up. The three-step algorithm on a spreadsheet finally made it mechanical. |
| 12 | Diagnostics toolkit | **3** | The warning that all gauges can read green while the plane crashes is the correct framing. But the table itself is a standard list; a junior will still walk away thinking VIF/BP/DW is the checklist. |

**Average industrial relevance: ~4.0.** Higher than most textbook treatments. Significantly better than anything I got in undergrad.

---

## 2. Missing real-world pathologies

This is where my frustration sits. The notes treat the DGP as fixed and the analyst as well-intentioned but naive. The pathologies that eat models in production are almost all *upstream* of the regression:

1. **Data leakage.** Zero coverage. The #1 way industrial regressions lie: a feature is constructed using future information (e.g., "rolling 30-day avg of defects" computed over the whole dataset before splitting). Training R² = 0.98, production = random. Must be in the notes.
2. **Concept drift / non-stationarity.** The DGP is static. In real life the coefficient on "line speed" changes when the supplier changes, when the sensor is recalibrated, when a tariff hits. A model trained on 2022 data scoring 2024 data is the normal case, not the exception. No discussion.
3. **Selection bias in the *sample*, not just the controls.** Maintenance records only exist for machines that failed loudly enough to trigger a ticket. Survivorship in warranty: claims only exist from customers who bothered. The Lalonde section hints at this but stays abstract.
4. **Measurement error and instrument calibration.** Every sensor drifts. Attenuation bias from noisy X is a classical result and entirely absent. This caused a real incident at my previous team: a torque sensor was miscalibrated by 4%, the coefficient shrank toward zero, and engineering concluded torque "didn't matter."
5. **Label noise / operational definitions changing.** "Defect" was redefined in Q3 to include cosmetic blemishes. The coefficient flipped. No section on this.
6. **Clustered / panel data.** The notes explicitly punt on autocorrelation and clustering in one sentence. In industry, observations are *almost always* clustered (by machine, shift, plant, customer) and treating them as iid gives standard errors that are off by 3-10x. This deserves a section, not a footnote.
7. **Simpson's paradox across plants / product lines.** Aggregate and disaggregate coefficients pointing opposite directions is the single most embarrassing meeting moment I have witnessed. The collider section is adjacent but does not nail this.
8. **Model monitoring / calibration drift post-deployment.** Calibration plots, PSI, recalibration. Entirely absent. A junior reading these notes will think the regression is done when the coefficient is estimated. In production, that's when the work begins.

---

## 3. Toy-example credibility

**Authentic-feeling:**
- The Ofqual cold open. Real, recent, politically charged, and diagnosable with the tools taught. Excellent.
- The LTCM one-paragraph mention in overfitting. Would like more of this.
- The COVID smoking paradox (collider). Correct and famous.
- The keyboard-saving-0.1-seconds table. This is literally every A/B test I have seen a PM get excited about.
- The tutoring self-selection analog of Lalonde. Clean and close to reality.

**Artificial / I'd cut or rework:**
- **The Instagram-slider self-discipline construct.** I get why it's pedagogically cute, but it undermines credibility. No analyst has that data. Replace with something like "years of operator experience, not in the HR extract" — the *structure* of invisibility is the same and it stops feeling like a TikTok.
- **Anna and Ben.** Fine the first time. By the tenth callback it reads like a children's book. I rolled my eyes at "Anna paid attention in every lecture; Ben scrolled his phone."
- **"Hot guys are jerks" and Pete Davidson.** Funny, and collider logic is correct, but it's the exact kind of example that makes senior engineers stop taking the course seriously. Keep one celebrity collider, drop the other.
- **The roommate-as-IV.** Clever pedagogically but not an instrument anyone has ever used. Use Angrist-style quarter-of-birth, or a supplier-rotation natural experiment. The Angrist-Lavy and Carpenter-Dobkin mentions in a remark should be *examples with numbers*, not a one-line citation.
- **The 5-student numerical tables.** Useful for pen-and-paper derivation. But 5 rows is exactly the sample size where everything the notes warn about (robust SEs, CV, BP test) breaks. Either say so explicitly or use n=50 with a downloadable CSV.
- **Drunk darts, winding road.** Charming once, exhausting by section 6.

---

## 4. The Monday-morning test

If I walked back into my old Bosch team tomorrow:

**I would reference:**
- §3 (OVB) — specifically the signable-bias worked example. I'd print the OVB-sign table.
- §5 (Significance vs. effect size) — I would read the seat-number story aloud in the next stakeholder meeting.
- §9 (Lalonde + robustness value) — I'd run a Cinelli-Hazlett RV on our supplier-quality model today. This is the single biggest immediately-usable thing.
- §11 (FWL) — to stop colleagues from saying "controlling for" without knowing what they mean.
- §12 warning box (all diagnostics green, design rotten) — this needs to be on the wall.

**I would skip:**
- §10 (RDD). Beautiful, but unless my team builds a credit-scoring model or something with a sharp rule, we're not running RDD on a production line.
- The bias-variance toy with degree-15 polynomials. I'd teach leakage and CV-on-a-pipeline instead.
- Most of the Anna-and-Ben narrative. My colleagues would mock it.

**I would *supplement* with (material not in the notes):**
- A 30-minute lecture on data leakage with a worked example.
- Clustered standard errors for panel data.
- A monitoring/drift section.

---

## 5. Overall rating for a junior data analyst at a real company

**7 / 10.**

Better than most. The framing ("regression is lying to you, here's how") is exactly the right mindset. The OVB, significance-vs-importance, Lalonde-sensitivity, and FWL sections are industrially first-rate. It loses points because:
- It treats the analyst's problem as "which estimator / test / model?" when the actual problem is usually "the data you have is not the data you think you have."
- Zero coverage of leakage, drift, measurement error, or clustering.
- Too many student/exam toys; an industrial analog for each would cost little and double the stickiness.

I would recommend it — with two supplementary chapters bolted on.

---

## 6. Three industrial failure stories the notes should include

### a) The Boeing 737 MAX MCAS angle-of-attack regression
Not a regression per se but the statistical spirit is identical: a critical system relied on **a single sensor** (no redundancy), and the validation dataset did not span the operational envelope where MCAS would activate most aggressively. This is specification/extrapolation (§6) plus measurement error (missing from notes) plus a safety-critical deployment. Two crashes, 346 deaths. A regression student reading this understands why "within-data-range fit was fine" is never a defense.

### b) Zillow Offers, 2021
Zillow's iBuying algorithm — a regression/ML model predicting home resale values — overestimated prices in a drifting market. Zillow bought thousands of homes above market value, took a $881M write-down, shut the division, laid off 25% of staff. This is **concept drift** (missing from notes) and **feedback loops** (the model's own purchases moved prices). A textbook demonstration that "train R² = 0.95" means nothing when the DGP shifts.

### c) Google Flu Trends
Predicted flu prevalence from search queries. Worked brilliantly on training data, beat CDC in early deployment, then systematically over-predicted flu for years. Causes: search behavior drifted (Google itself changed autocomplete, suggestion algorithms — the model was using its *own influence* as a feature), and the original variable-selection was effectively a multiple-testing crime scene (50M candidate terms, 45 picked). This hits multiple testing (§5), concept drift (missing), and data leakage (missing) simultaneously — an ideal capstone story. It is also famous enough that alumni will remember the lesson.

---

## One-paragraph bottom line

These notes are better than the regression course I took in mechanical engineering and better than 90% of what data-scientist bootcamps teach. The pedagogical architecture (toy → theorem → numerical → viz) is genuinely good. But the notes live in a world where the analyst has the right data, correctly measured, drawn iid from a stationary DGP, and "only" needs to pick the right estimator. At Bosch, that world does not exist. Add leakage, drift, measurement error, and clustering — even just a page each — and you go from 7/10 to 9/10. Until then, this is an excellent foundation that a junior analyst should read *and then immediately be told what it does not cover.*

— Jonas
