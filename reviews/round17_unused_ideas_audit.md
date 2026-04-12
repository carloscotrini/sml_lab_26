# Audit: Creative Ideas -- Implemented vs. Unused

**Date:** 2026-04-10
**Auditor:** Round 17 audit
**Files reviewed:** creative_storyteller.md, creative_magician.md, creative_pedagogist.md, creative_visualizer.md, lecture_notes.tex

---

## 1. Creative Storyteller

### Section 1: Introduction

| Idea | Status | Evidence / Notes |
|------|--------|-----------------|
| BBC A-level algorithm headline as opening hook | **IMPLEMENTED** | Lines 141--147: "The Algorithm That Ruined 72 Hours" box with Ofqual story, BBC reference |
| "This course is about why" pause | **IMPLEMENTED** | Line 146: "This course is about why." |
| Instagram slider story for U | **IMPLEMENTED** | Lines 191--198: full Instagram slider description present |
| "The most important variable is the one you forgot to collect" meme takeaway | **IMPLEMENTED** | Captured in spirit by lines 198--200 (the confounder paragraph) though not as a standalone quote |
| A-level algorithm as recurring "ghost" callback | **IMPLEMENTED** | Lines 128 (How to Read), 1707--1715 (Conclusion returns to Ofqual) |

### Section 2: DGP

| Idea | Status | Evidence / Notes |
|------|--------|-----------------|
| Live audience poll ("how many hours did you study") | **NOT APPLICABLE** | Requires live audience interaction; cannot be implemented in written notes |
| "For the next eight weeks, you get to be God" framing | **NOT IMPLEMENTED, LOW VALUE** | The DGP section already explains the God-like perspective implicitly (lines 214--215). Adding the exact quote would be a tone choice, not a structural improvement. |
| "Self-reported discipline is biased upward" callback | **NOT IMPLEMENTED, LOW VALUE** | A minor aside that doesn't connect to any theorem |

### Section 3: OVB

| Idea | Status | Evidence / Notes |
|------|--------|-----------------|
| Chocolate-Nobel scatterplot (Messerli 2012) as OVB opener | **IMPLEMENTED (as CNN Coffee instead)** | Lines 385--391: CNN coffee study serves the same role. The chocolate-Nobel story was proposed but the notes chose a different real-world example. |
| OVB formula applied back to the opening example | **IMPLEMENTED** | Lines 389--391: OVB formula interpretation applied to the coffee example |
| "Ghost in the regression" phrase | **IMPLEMENTED** | Lines 128, 459, 470--471, 1710: used repeatedly as running gag |
| "Another ghost in the regression" as recurring phrase | **IMPLEMENTED** | Lines 128 (How to Read section), 1319, 1738 |

### Section 4: Heteroscedasticity

| Idea | Status | Evidence / Notes |
|------|--------|-----------------|
| Glassdoor/levels.fyi salary spread as opening | **NOT IMPLEMENTED but HIGH VALUE** | The current section opens with the Drunk Darts story, and has an apartment rent remark (line 588). The salary example is more relatable for ETH students than apartment rents. **Spec: Add a 3-sentence Toy Story or remark before the Drunk Darts box (~line 568) showing junior vs. senior engineer salary spread as a concrete heteroscedasticity example.** |
| "After three beers" as shorthand for heteroscedasticity | **NOT IMPLEMENTED, LOW VALUE** | The Drunk Darts story is present but "three beers" is not promoted as a recurring callback phrase. Adding it would require edits across multiple sections for marginal benefit. |
| "Your CI is lying about how sure you are" meme takeaway | **IMPLEMENTED** | Lines 553--565, 663: the notes explicitly say the CI coverage is wrong and "Your coefficient is right; your uncertainty about it is wrong" |

### Section 5: Significance vs. Effect Size

| Idea | Status | Evidence / Notes |
|------|--------|-----------------|
| CNN coffee/chocolate/cat headlines as opener | **NOT IMPLEMENTED, LOW VALUE** | The seat number story already serves this purpose effectively (lines 737--757). Adding more headlines is redundant. |
| "Is this a seat number?" as recurring question | **IMPLEMENTED** | Lines 128, 772, 1740, 1862--1868 (BS Detector) |
| Live seat-number regression on real data | **NOT APPLICABLE** | Requires live demonstration; already described in written form |
| "Stand Up If Significant" exercise | **IMPLEMENTED** | Lines 759--769: full "Stand Up If Significant" box present |

### Section 6: Specification Error

| Idea | Status | Evidence / Notes |
|------|--------|-----------------|
| Fitness tracker "negative 12 kg by 2029" hook | **NOT IMPLEMENTED but HIGH VALUE** | Current section uses the Straight Ruler metaphor (line 887), which is abstract. The fitness tracker is a concrete, modern example every student has seen on their phone. **Spec: Add a 2-sentence remark after the Straight Ruler Toy Story (~line 891) using a fitness tracker projection as a second real-world extrapolation example.** |
| Score of 132.5 as absurdity punchline | **IMPLEMENTED** | Lines 940--942: "100.5" and "132.5" predictions explicitly shown |
| "Score of 132" as shorthand for extrapolation failure | **IMPLEMENTED** | Referenced in coefficient tracker (line 968) and present in the numerical example |

### Section 7: Overfitting

| Idea | Status | Evidence / Notes |
|------|--------|-----------------|
| AI-generated seven-fingered hand as opening | **NOT IMPLEMENTED, LOW VALUE** | The Three Dartboard Players story is already effective. The AI hand is a pop-culture reference that may date quickly. |
| Polynomial degree table with suspense build | **IMPLEMENTED** | Lines 994--1005: table present with the degree-15 crash |
| "Seven fingers" as recurring overfitting image | **NOT IMPLEMENTED, LOW VALUE** | A visual metaphor that works better in slides than in written notes |
| Negative test R-squared explanation | **IMPLEMENTED** | Lines 1011--1013 and the Polynomial Beauty Contest warning box |

### Section 8: Endogeneity / Bad Controls

| Idea | Status | Evidence / Notes |
|------|--------|-----------------|
| SheKnows "Hot Guys Are Jerks" headline | **IMPLEMENTED** | Lines 1103--1105 |
| Pete Davidson as collider bias example | **IMPLEMENTED** | Lines 1112--1113 |
| Talent/Luck/Fame table | **IMPLEMENTED** | Lines 1163--1184 |
| ETH admissions as collider ("geniuses seem lazy") | **NOT IMPLEMENTED but HIGH VALUE** | This is an extremely powerful example because every student in the room experiences it daily. It makes collider bias personal. **Spec: Add a 4-sentence remark after the Talent/Luck table (~line 1184) applying collider bias to ETH admissions: conditioning on "admitted to ETH" creates a spurious negative correlation between natural talent and work ethic.** |

### Section 9: Real World / Lalonde

| Idea | Status | Evidence / Notes |
|------|--------|-----------------|
| Healthcare algorithm racial bias story (Obermeyer 2019) | **NOT IMPLEMENTED but HIGH VALUE** | The current section uses the tutoring story and Lalonde dataset, but lacks a devastating real-world stakes example. The Obermeyer healthcare algorithm is published in Science, widely known, and drives the point home that directionally wrong estimates kill. **Spec: Add a remark box after the Lalonde subsection (~line 1335) describing the Obermeyer et al. (2019) healthcare algorithm as a real-world Lalonde: all diagnostics passed, costs used as proxy for needs, Black patients systematically deprioritized.** |
| "Is this a Lalonde?" as recurring phrase | **IMPLEMENTED** | Lines 1740: "is this a Lalonde?" appears in the conclusion |
| "Diagnostics check the model. Only the research design checks the truth." | **IMPLEMENTED** | Lines 1398, 1639--1641, 1732 |

### Section 10: RDD

| Idea | Status | Evidence / Notes |
|------|--------|-----------------|
| "Raise your hand if you've been one point from the next grade" | **NOT APPLICABLE** | Live interaction; the 69-vs-70 story already captures this |
| "The cruelty of the cutoff IS the experiment" | **IMPLEMENTED** | Lines 1417--1419: "This section is the redemption arc" framing present; the cutoff-as-experiment idea is the core of the section |
| Real RDD examples (elections, blood-alcohol, selective schools) | **NOT IMPLEMENTED but HIGH VALUE** | The section only has the scholarship example. Adding 2--3 real published RDD studies would show students this is a widely used technique. **Spec: Add a remark after the scholarship numerical example (~line 1488) listing 2--3 real RDD studies: Lee (2008, elections), Hansen (2015, blood-alcohol), Abdulkadiroglu et al. (2014, selective schools).** |
| "This is the redemption arc" framing | **IMPLEMENTED** | Line 1419: "This section is the redemption arc." |

### Section 11: FWL

| Idea | Status | Evidence / Notes |
|------|--------|-----------------|
| Cold showers / productivity-bro hook | **NOT IMPLEMENTED, LOW VALUE** | The coaching/shoes story already serves this purpose (lines 1515--1527) |
| "EXACTLY the same number, to infinite decimal places" emphasis | **IMPLEMENTED** | Lines 1587--1591: "They match---not approximately, but to every decimal place." |
| "What are you actually controlling for?" as recurring question | **IMPLEMENTED** | Lines 1507, 1548--1552, 1555--1556 |

### Sections 12-14: Diagnostics, Theorem Map, Conclusion

| Idea | Status | Evidence / Notes |
|------|--------|-----------------|
| Cockpit instrument panel analogy | **IMPLEMENTED** | Line 1615: "Think of these diagnostics as the instrument panel in a cockpit." |
| "All gauges green, wrong destination" summary | **IMPLEMENTED** | Lines 1615, 1638, 1715 |
| "Previously on Regression Autopsy" TV recap for theorem map | **IMPLEMENTED** | Lines 1648--1668: coefficient tracker table serves this purpose; the How to Read section (line 128) also uses running gag language |
| Return to A-level algorithm in conclusion | **IMPLEMENTED** | Lines 1707--1715 |
| Final line: "This does not mean you should stop using regression" | **IMPLEMENTED** | Lines 1744--1746 |
| Five running gags table (ghost, three beers, seat number, score of 132, is this a Lalonde) | **PARTIALLY IMPLEMENTED** | Ghost, seat number, and Lalonde are established. "Three beers" and "score of 132" are not promoted as running callbacks. |
| ESCU (Exam Score Cinematic Universe) running gag | **NOT IMPLEMENTED, LOW VALUE** | Overly elaborate framing that doesn't add to written notes |

---

## 2. Creative Magician (Stage Performance)

### Energy Map / 90-Minute Structure

| Idea | Status | Evidence / Notes |
|------|--------|-----------------|
| Cold open: tutoring regression with wrong sign | **IMPLEMENTED** | Lines 137--139: Cold Open box with seat number. The tutoring wrong-sign story is in Section 9 (lines 1342--1348). |
| Five-peak energy structure | **NOT APPLICABLE** | This is a presentation pacing guide, not translatable to written notes |
| Intermission beat at ~45 minutes | **NOT APPLICABLE** | Requires live delivery |
| "Are we at three beers?" check whenever SEs mentioned | **NOT IMPLEMENTED, LOW VALUE** | Would be a minor insertion; notes already handle SE context clearly |

### Five Big Reveals

| Idea | Status | Evidence / Notes |
|------|--------|-----------------|
| Big Reveal #1: Coefficient drops when controls added | **IMPLEMENTED** | Section 3 numerical example (lines 424--457) shows coefficient change |
| Big Reveal #2: Seat number prophecy | **IMPLEMENTED** | Lines 737--757 |
| Big Reveal #3: Famous people's spouses / collider bias | **IMPLEMENTED** | Lines 1107--1113 |
| Big Reveal #4: Roommate IV rescue (OLS 8.71, truth 3.0) | **IMPLEMENTED** | Lines 1259--1302 |
| Big Reveal #5: Tutoring sign flip | **IMPLEMENTED** | Lines 1342--1348, 1373--1395 |

### Audience Participation Tricks

| Idea | Status | Evidence / Notes |
|------|--------|-----------------|
| Trick #1: "Coefficient Auction" -- students guess studying effect | **NOT IMPLEMENTED but HIGH VALUE** | Currently the notes show the OVB numerical example without first asking the reader to predict. A "Predict Before You Peek" box exists in Section 4 (line 642) and Section 6 (line 936) but NOT in Section 3. **Spec: Add a "Predict Before You Peek" box before the OVB numerical example (~line 424) asking readers to guess the studying coefficient before seeing the short-regression result.** |
| Trick #2: "Stand Up If Significant" | **IMPLEMENTED** | Lines 759--769 |
| Trick #3: "Vote With Your Feet: Should We Shut Down Tutoring?" | **NOT APPLICABLE** | Requires physical movement; the written Tutoring story already creates the same moral stakes |

### Callback Chain (Coefficient Tally)

| Idea | Status | Evidence / Notes |
|------|--------|-----------------|
| Running coefficient tally across all sections | **IMPLEMENTED** | Coefficient tracker italicized notes at the start of every section (lines 543, 733, 883, 968, 1099, 1319, 1415, 1507, 1613, 1648--1666) |
| Summary table with all nine versions | **IMPLEMENTED** | Lines 1648--1666: full table in Section 13 |
| "Eight wrong answers. Two right ones." punchline | **IMPLEMENTED** | Line 1668 |

### The Closer

| Idea | Status | Evidence / Notes |
|------|--------|-----------------|
| Return to tutoring regression, walk through diagnostics | **IMPLEMENTED** | Lines 1637--1641 |
| Final closing line | **IMPLEMENTED** | Lines 1744--1746 |

---

## 3. Creative Pedagogist

### Global Structural Recommendations

| Idea | Status | Evidence / Notes |
|------|--------|-----------------|
| Create an appendix for proofs | **IMPLEMENTED** | Lines 1751--1846: Appendix with all four proofs |
| "Punchline before proof" for every theorem | **IMPLEMENTED** | Each theorem now has a "Why is this true?" paragraph after it (e.g., line 422, 525, 607, 988, 1546) |
| Add practice problems at end of each section | **NOT IMPLEMENTED but HIGH VALUE** | This is the single most-requested feature across all four student reviews. No practice problems exist anywhere in the notes. **Spec: Add 2--3 practice problems (exam-style questions from the pedagogist review) at the end of each section, starting with the ones provided in the review for Sections 1--11.** |
| Lead with story, follow with math | **IMPLEMENTED** | Every section now opens with a Toy Story box before the formal theorem |
| Add a decision flowchart for variable inclusion | **NOT IMPLEMENTED but HIGH VALUE** | Max explicitly requested this. Nothing like it exists in the notes. **Spec: Add a one-page decision flowchart in Section 12 (Diagnostics) or as an appendix, guiding students through: Is the variable post-treatment? Is it correlated with both X and Y? Can you observe the confounder? Is there a cutoff?** |

### Section 1: Introduction

| Idea | Status | Evidence / Notes |
|------|--------|-----------------|
| Cut "In the language of causal inference" phrase | **NOT IMPLEMENTED, LOW VALUE** | Still present at line 171. Minor wording issue. |
| Add "Prerequisites and Notation" box | **NOT IMPLEMENTED but HIGH VALUE** | No prerequisites box exists. Students like Lena and Max both needed this. **Spec: Add a "Prerequisites and Notation" tcolorbox before Section 1 (~line 130) listing required background (matrix multiplication, expectation, variance, covariance, log) and notation conventions (E, Var, Cov, hat, plim, N(mu, sigma^2) = variance).** |
| Defer X3 description -- say "trap variable, revealed in Section 8" | **NOT IMPLEMENTED, LOW VALUE** | The current X3 description (lines 183--188) is already clear and includes a cross-reference. The pedagogist's version reduces information. |
| "Predict the Confounder" active learning activity | **NOT APPLICABLE** | Requires live interaction. However, a written version could work as a "Try It" box. |
| Exam-style question (coffee and confounders) | **NOT IMPLEMENTED but HIGH VALUE** | Part of the practice problems recommendation above |

### Section 2: DGP

| Idea | Status | Evidence / Notes |
|------|--------|-----------------|
| Restructure to show one equation at a time | **IMPLEMENTED** | Lines 236--245 show all six equations, but lines 252--273 walk through each one individually with paragraph-level explanations |
| Add causal graph explanation ("what IS a causal graph") | **IMPLEMENTED** | Line 296: "Causal ordering" remark explains the graph. Not as explicit as the pedagogist wanted but present. |
| Clarify log vs ln | **IMPLEMENTED** | Lines 247--249: "Throughout these notes, log denotes the natural logarithm (base e)" |
| Clarify variance vs SD for epsilon | **IMPLEMENTED** | Line 267: "(where 0.5 * |X1| is the variance, not the standard deviation; thus SD(epsilon) = sqrt(0.5 * |X1|))" |
| Negative study hours as teaching moment | **IMPLEMENTED** | Lines 259--261: full remark addressing negative study hours |
| "Build the DGP from the Story" activity | **NOT APPLICABLE** | Requires live polling |
| "One log-unit" clarification | **IMPLEMENTED** | Line 282: "going from 1 to 2.7 hours (one log-unit) gains you 8 points" |

### Section 3: OVB

| Idea | Status | Evidence / Notes |
|------|--------|-----------------|
| Cut "When OVB Cannot Be Signed" section | **NOT IMPLEMENTED, LOW VALUE** | Still present (lines 491--495). It is only 5 lines and does not cause harm. |
| Move collider material to Section 8 | **NOT IMPLEMENTED, LOW VALUE** | Collider material remains in Section 3 (lines 506--535) AND is elaborated in Section 8 (lines 1139--1184). Having it in both places provides scaffolding. |
| Replace ice cream/drowning with chocolate-Nobel or other fresh example | **IMPLEMENTED** | Lines 385--391: CNN Coffee study used instead (neither ice cream/drowning NOR chocolate-Nobel) |
| "Sign the Bias" active learning activity | **IMPLEMENTED** | Lines 485--489: "Try It Yourself: Sign the Bias" box with dog ownership example |
| Add covariance linearity reminder before proof | **NOT IMPLEMENTED, LOW VALUE** | The proof is now in the appendix (lines 1758--1771), so this is less needed |
| Clarify E[...] vs plim mismatch | **IMPLEMENTED** | Lines 229--231: plim remark present in Section 2 |
| Proxy variable trap question | **NOT IMPLEMENTED, LOW VALUE** | Niche point about proxy variables having direct effects |

### Section 4: Heteroscedasticity

| Idea | Status | Evidence / Notes |
|------|--------|-----------------|
| Cut "Everyday Wisdom" insight box | **NOT IMPLEMENTED** | Still present at lines 591--599. Lena said it felt like filler. **This is borderline -- the pedagogist says cut, but it is only 8 lines.** |
| Move sandwich proof to appendix | **IMPLEMENTED** | Lines 1787--1803: proof in appendix |
| Shorten CI explanation | **NOT IMPLEMENTED, LOW VALUE** | Lines 549--565 are reasonable length. Not egregiously long. |
| Add source for 82% coverage claim | **IMPLEMENTED** | Line 659: "In a simulation of the studying DGP, the nominal 95% CI achieves only ~82% coverage" -- context provided via DGP reference |
| Add chi-squared distribution definition | **IMPLEMENTED** | Lines 672--674: full chi-squared definition |
| "Spot the Funnel" activity | **NOT APPLICABLE** | Requires live pair discussion |
| Define "consistency" before use | **IMPLEMENTED** | Lines 229--231 (plim remark), line 1236 (IV section explicit definition) |
| Small-sample trap question | **NOT IMPLEMENTED but HIGH VALUE** | Part of the practice problems recommendation. Good exam question. |
| Exam-style question (apartment rent + BP test) | **NOT IMPLEMENTED but HIGH VALUE** | Part of the practice problems recommendation |

### Section 5: Significance

| Idea | Status | Evidence / Notes |
|------|--------|-----------------|
| Add Bonferroni proof (one line) | **IMPLEMENTED** | Lines 844--846: union bound proof |
| Add replication crisis paragraph | **IMPLEMENTED** | Lines 848--852: full replication crisis remark |
| Power formula worked example | **NOT IMPLEMENTED but HIGH VALUE** | The power formula is stated (lines 806--812) but no numerical example is provided. **Spec: Add a 3-line worked micro-example after the power proposition (~line 812): "With beta=0.1, sigma=2, n=50: Power = Phi(0.354 - 1.96) = 0.054. You have a 5.4% chance of detecting this tiny effect."** |
| "Significance Lottery" activity | **NOT APPLICABLE** | Live interaction, though the seat number story achieves the same goal |
| Power Paradox desirable difficulty question | **NOT IMPLEMENTED but HIGH VALUE** | Excellent exam question contrasting a p<0.001 drug saving 0.3 seconds vs a p=0.12 drug saving 45 minutes. Part of practice problems recommendation. |

### Section 6: Specification Error

| Idea | Status | Evidence / Notes |
|------|--------|-----------------|
| Add explicit beta* formula | **NOT IMPLEMENTED but HIGH VALUE** | Theorem 6.1 (lines 896--902) says "best linear approximation" but never gives the formula beta* = E[XX']^{-1} E[XY]. **Spec: Add the explicit formula beta* = (E[XX'])^{-1} E[XY] immediately after "which is the best linear approximation" on line 900.** |
| Add note on practical specification testing | **NOT IMPLEMENTED but HIGH VALUE** | No guidance on how to detect misspecification in practice. **Spec: Add a 3-sentence remark after the Repair box (~line 955) explaining that residual plots reveal curvature, cross-validation compares specifications, and domain knowledge is the strongest guide.** |
| Define argmin | **NOT IMPLEMENTED, LOW VALUE** | argmin appears on line 899; most ETH students know it |
| "Extrapolation Roulette" activity | **IMPLEMENTED** | Lines 936--943: "Predict Before You Peek" box asks students to predict the 30-hour score |

### Section 7: Overfitting

| Idea | Status | Evidence / Notes |
|------|--------|-----------------|
| Move bias-variance proof to appendix | **IMPLEMENTED** | Lines 1805--1826: proof in appendix |
| Clarify independence assumption in proof | **IMPLEMENTED** | Lines 1817--1819: remark on independence of noise and fitted model |
| Explain negative test R-squared | **IMPLEMENTED** | Lines 1011--1013: explained in context |
| Add cross-validation numerical example | **IMPLEMENTED** | Lines 1027--1049: 5-fold CV example with linear vs. log |
| "Bet on the Polynomial" activity | **IMPLEMENTED** | Lines 1007--1009: "Polynomial Beauty Contest" warning box |
| Table metadata (n, averaging) | **NOT IMPLEMENTED, LOW VALUE** | The table lacks metadata about simulation parameters |
| Bias-variance identity hint | **IMPLEMENTED** | Line 988: "the noise cross-term vanishes" explanation |

### Section 8: Endogeneity / Bad Controls

| Idea | Status | Evidence / Notes |
|------|--------|-----------------|
| Add transition note for simplified IV DGP | **IMPLEMENTED** | Lines 1262--1267: simplified DGP clearly introduced with "Suppose the true DGP (simplified) is" |
| Add exclusion restriction is untestable | **NOT IMPLEMENTED but HIGH VALUE** | Not stated anywhere. This is a fundamental point students must understand. **Spec: Add one sentence after the exclusion definition (~line 1205): "The exclusion restriction cannot be verified from data alone. It is a substantive claim about the world and must be defended on domain-knowledge grounds."** |
| Add F > 10 source (Stock and Yogo) | **NOT IMPLEMENTED, LOW VALUE** | Lines 1247--1248 give the rule of thumb without attribution. Minor. |
| "Name That Instrument" activity | **IMPLEMENTED** | Lines 1208--1220: "Try It Yourself: Name That Instrument" box with three candidates |
| Define potential outcomes before RDD | **IMPLEMENTED** | Lines 1410--1412: potential outcomes remark placed before RDD |
| Show intermediate IV algebra | **IMPLEMENTED** | Lines 1291--1295: step-by-step Cov computation |
| Exclusion violation desirable difficulty | **NOT IMPLEMENTED, LOW VALUE** | Good question but part of the broader practice problems gap |

### Section 9: Real World

| Idea | Status | Evidence / Notes |
|------|--------|-----------------|
| Expand sensitivity analysis with numerical example | **IMPLEMENTED** | Lines 1373--1395: full numerical example with RV = 0.04 and comparison table |
| Add partial R-squared definition | **IMPLEMENTED** | Lines 1356--1358 |
| Add simple Lalonde-style table | **NOT IMPLEMENTED but HIGH VALUE** | No paper-verifiable table of treated/control observations exists. **Spec: Add a small numerical example (~line 1335) with 5 treated and 5 control observations showing visible covariate imbalance, the naive OLS estimate, and the experimental truth, verifiable on paper.** |
| Define RCT | **NOT IMPLEMENTED, LOW VALUE** | RCT is mentioned (line 1331) but not explicitly defined. One sentence would suffice but most students know this. |
| "Diagnostic False Alarm" activity | **NOT APPLICABLE** | Requires live voting; the notes achieve the same effect narratively |

### Section 10: RDD

| Idea | Status | Evidence / Notes |
|------|--------|-----------------|
| Cut five surnames in bandwidth methods | **NOT IMPLEMENTED, LOW VALUE** | Still present (line 1463) but it is one sentence, not burdensome |
| Add RDD identification proof sketch | **IMPLEMENTED** | Lines 1441--1447: theorem states the identification result clearly. The proof sketch is implicit in the definition. |
| Add manipulation as threat | **NOT IMPLEMENTED but HIGH VALUE** | Not mentioned anywhere. This is the most important threat to RDD validity. **Spec: Add a warning box after the bandwidth discussion (~line 1463) explaining that manipulation of the running variable (e.g., retaking exams, grade appeals) invalidates RDD, and that a density plot near the cutoff is the standard check.** |
| Add noise to numerical example | **NOT IMPLEMENTED, LOW VALUE** | The clean example (lines 1466--1488) is pedagogically effective as-is |
| "Find the RDD in the Wild" activity | **NOT APPLICABLE** | Requires live discussion |

### Section 11: FWL

| Idea | Status | Evidence / Notes |
|------|--------|-----------------|
| Move block matrix proof to appendix | **IMPLEMENTED** | Lines 1828--1846: proof in appendix |
| Add intermediate step in numerical example | **IMPLEMENTED** | Lines 1579--1586: intermediate residual computations shown |
| Add projection matrix reminder | **IMPLEMENTED** | Lines 1533--1534: M2 defined as "residual-maker matrix" |
| Note idempotent/symmetric properties of M2 | **NOT IMPLEMENTED, LOW VALUE** | Technical detail useful only for proof readers |
| "Do the FWL by Hand" activity | **NOT APPLICABLE** | Requires live computation; the numerical example (lines 1560--1592) already walks through the procedure |
| "Bad Control FWL" desirable difficulty | **IMPLEMENTED** | Lines 1596--1600: "What Happens with Bad Controls" subsection applies FWL to X3 |

### Sections 12-13: Diagnostics / Theorem Map

| Idea | Status | Evidence / Notes |
|------|--------|-----------------|
| Add VIF definition | **IMPLEMENTED** | Line 1629: VIF defined in diagnostics table |
| Add Cook's distance definition | **IMPLEMENTED** | Line 1627: Cook's d formula in diagnostics table |
| Reframe theorem map as "Previously on..." TV recap | **IMPLEMENTED** | Lines 1648--1668: coefficient tracker table with narrative framing |
| "Diagnose This Regression" activity | **NOT APPLICABLE** | Requires live interaction with diagnostic plots |

---

## 4. Creative Visualizer

### Diagram Replacements

| Idea | Status | Evidence / Notes |
|------|--------|-----------------|
| 1.1 OVB "Ghost in the Machine" illustration | **IMPLEMENTED (as spec)** | Lines 459--471: detailed visualization spec describes the ghost diagram |
| 1.2 Heteroscedasticity "Trumpet Plot" | **IMPLEMENTED (as spec)** | Lines 646--652: "Funnel of False Confidence" visualization spec |
| 1.3 Collider Bias "Fame Filter" two-panel diagram | **IMPLEMENTED (as spec)** | Lines 1186--1190: collider explorer visualization spec |
| 1.4 Bias-Variance "Three Dart Players" illustration | **NOT IMPLEMENTED but HIGH VALUE** | The three dartboard players are described in text (lines 972--976) but no actual TikZ illustration or detailed visual spec exists for the three boards. **Spec: Add a vizspec box after the Toy Story in Section 7 (~line 976) with a detailed illustration description of three dartboards (Robot/high bias, Drunk Expert/low bias high variance, Wobble/irreducible noise) with a stacked bar chart below.** |
| 1.5 Specification "Straight Ruler on Winding Road" | **IMPLEMENTED (as spec)** | Lines 957--961: "Comfort Zone" extrapolation explorer |
| 1.6 IV "Clean Pipe" plumbing diagram | **NOT IMPLEMENTED but HIGH VALUE** | The IV section describes the instrument conceptually but has no visual spec for the plumbing/pipe metaphor that separates contaminated (U) from clean (Z) variation. **Spec: Add a vizspec box in Section 8 after the IV definition (~line 1206) describing a plumbing diagram with contaminated (red/U) and clean (green/Z) pipes feeding into X1, with IV as a filter on the green pipe.** |
| 1.7 RDD "The Cliff" landscape | **IMPLEMENTED (as spec)** | Lines 1496--1500: "The Cliff" bandwidth explorer |
| 1.8 FWL "Double Filter" pipeline | **IMPLEMENTED (as spec)** | Lines 1602--1606: "Double Residual" FWL animator |

### Infographic Summaries (One-Page Posters)

| Idea | Status | Evidence / Notes |
|------|--------|-----------------|
| OVB Cheat Sheet | **NOT IMPLEMENTED, LOW VALUE** | Would be a nice supplementary material but is outside the scope of lecture notes |
| Heteroscedasticity Cheat Sheet | **NOT IMPLEMENTED, LOW VALUE** | Same |
| Significance Cheat Sheet | **NOT IMPLEMENTED, LOW VALUE** | The "Statistical BS Detector" (lines 1851--1921) partially serves this purpose |
| Causation Cheat Sheet | **NOT IMPLEMENTED, LOW VALUE** | Same |
| Overfitting Cheat Sheet | **NOT IMPLEMENTED, LOW VALUE** | Same |
| RDD Cheat Sheet | **NOT IMPLEMENTED, LOW VALUE** | Same |
| FWL Cheat Sheet | **NOT IMPLEMENTED, LOW VALUE** | Same |

### Before/After Slides

| Idea | Status | Evidence / Notes |
|------|--------|-----------------|
| OVB Before/After | **IMPLEMENTED** | Lines 473--478: "Before and After: The OVB Reveal" key insight box |
| Heteroscedasticity Before/After | **NOT IMPLEMENTED but HIGH VALUE** | No before/after reveal exists for the heteroscedasticity section. **Spec: Add a keyinsight box after the coverage discussion (~line 664) showing Slide 1 (narrow constant CI, "95% confident") vs. Slide 2 (trumpet data, classical band labeled "Claimed 95%, actual 82%", robust band labeled "Actual 95%").** |
| Significance Before/After | **NOT IMPLEMENTED, LOW VALUE** | The keyboard example (lines 854--870) already provides this contrast implicitly |
| Bad Controls Before/After | **NOT IMPLEMENTED, LOW VALUE** | The collider section already has strong narrative contrast |
| Observational vs. Experimental Before/After | **NOT IMPLEMENTED, LOW VALUE** | The tutoring story (lines 1342--1348) and sensitivity analysis (lines 1373--1395) together provide this contrast |

### Recurring Visual: "The Shifting Regression Line" Banner

| Idea | Status | Evidence / Notes |
|------|--------|-----------------|
| TikZ banner at the start of each section showing the regression line evolving | **NOT IMPLEMENTED but HIGH VALUE** | The coefficient tracker text notes exist, but there is no visual representation. A small TikZ graphic evolving across sections would be a powerful visual throughline. **Spec: Create a LaTeX command (\coefficientbanner) that produces a small (~3cm) TikZ graphic at the start of each section, showing the regression line in its current state of distortion (e.g., Section 3: two lines with OVB gap; Section 7: wild polynomial oscillations; Section 10: clean cliff).** |

### Animation Storyboards

| Idea | Status | Evidence / Notes |
|------|--------|-----------------|
| 5.1 "The Ghost Appears" OVB animation | **NOT APPLICABLE** | Requires animation/video; the static viz spec (lines 459--471) captures the same content |
| 5.2 "The Funnel Opens" heteroscedasticity animation | **NOT APPLICABLE** | Requires animation |
| 5.3 "The Fame Filter" collider animation | **NOT APPLICABLE** | Requires animation |

---

## Summary: HIGH-VALUE Unused Ideas (Priority List)

These are the ideas classified as **NOT IMPLEMENTED but HIGH VALUE**, ranked by estimated impact:

### Tier 1: Structural gaps (affect many students)

1. **Practice problems at end of each section** (Pedagogist)
   - The single most-requested feature across all four student reviews.
   - Spec: Add 2--3 exam-style questions at the end of each section. The pedagogist review provides specific questions for every section -- use those directly.

2. **Prerequisites and Notation box** (Pedagogist)
   - Resolves confusion flagged by Lena and Max about notation, conventions, and assumed background.
   - Spec: Add a tcolorbox before Section 1 listing required math background and defining notation conventions (E, Var, Cov, hat, plim, N(mu, sigma^2)).

3. **Decision flowchart for variable inclusion** (Pedagogist)
   - Max explicitly requested this. Gives students a practical tool for causal reasoning.
   - Spec: Add a one-page flowchart in Section 12 or as an appendix: Is it post-treatment? -> Don't control. Is it correlated with X and Y? -> Control. Can you observe the confounder? -> IV or sensitivity analysis. Sharp cutoff? -> RDD.

### Tier 2: Missing content that would strengthen specific sections

4. **RDD manipulation threat** (Pedagogist)
   - The most important validity threat for RDD is completely absent.
   - Spec: Add a warning box after bandwidth discussion (~line 1463) on running-variable manipulation and the density test.

5. **Exclusion restriction is untestable** (Pedagogist)
   - A fundamental point about IV that is never stated.
   - Spec: Add one sentence after line 1205.

6. **Obermeyer healthcare algorithm example** (Storyteller, Section 9)
   - The Real World section lacks a real-world stakes example beyond the abstract Lalonde reference.
   - Spec: Add a remark box after line 1335 describing the Obermeyer et al. (2019) racial bias in healthcare algorithm.

7. **ETH admissions as collider bias** (Storyteller, Section 8)
   - Makes collider bias personal for every student in the room.
   - Spec: Add a 4-sentence remark after line 1184.

8. **Lalonde-style numerical table** (Pedagogist, Section 9)
   - Section 9 breaks the notes' own pattern by lacking a paper-verifiable numerical example of the observational vs. experimental contrast.
   - Spec: Add 5 treated + 5 control observations with covariate imbalance showing the OLS vs. experimental estimates.

9. **Beta-star explicit formula** (Pedagogist, Section 6)
   - Theorem 6.1 says "best linear approximation" without giving the formula.
   - Spec: Add beta* = (E[XX'])^{-1} E[XY] on line 900.

10. **Practical specification testing guidance** (Pedagogist, Section 6)
    - No advice on how to detect misspecification in practice.
    - Spec: Add 3 sentences after line 955 on residual plots, cross-validation, and domain knowledge.

### Tier 3: Visual/experiential improvements

11. **Power formula worked micro-example** (Pedagogist, Section 5)
    - Power formula is stated but never computed with numbers.
    - Spec: Add 3-line worked example after line 812.

12. **Real published RDD examples** (Storyteller, Section 10)
    - Shows students RDD is widely used in practice.
    - Spec: Add 2--3 citations after line 1488.

13. **Heteroscedasticity Before/After reveal** (Visualizer)
    - Section 4 lacks the before/after contrast that works well in Section 3.
    - Spec: Add keyinsight box after line 664.

14. **Salary spread example for heteroscedasticity** (Storyteller)
    - More relatable than apartment rents for ETH students.
    - Spec: Add 3-sentence remark before Drunk Darts (~line 568).

15. **IV "Clean Pipe" plumbing diagram vizspec** (Visualizer)
    - The IV section lacks a visual metaphor for the clean/contaminated variation split.
    - Spec: Add vizspec box after line 1206.

16. **Three Dartboards detailed vizspec** (Visualizer)
    - Text description exists but no visual spec for an actual illustration.
    - Spec: Add vizspec box after line 976.

17. **Coefficient banner TikZ graphic** (Visualizer)
    - Would transform the text-only coefficient tracker into a visual throughline.
    - Spec: Create \coefficientbanner command producing a small TikZ graphic at each section start.

18. **Fitness tracker extrapolation example** (Storyteller, Section 6)
    - Concrete and modern complement to the Straight Ruler metaphor.
    - Spec: Add 2-sentence remark after line 891.

19. **"Predict Before You Peek" box for OVB section** (Magician)
    - Section 3 lacks the prediction prompt that Sections 4 and 6 already have.
    - Spec: Add box before line 424 asking readers to guess the studying coefficient.
