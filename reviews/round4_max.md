# Follow-Up Review: Regression Autopsy (Revised Lecture Notes)
**Reviewer:** Max, 3rd-year Mechanical Engineering, ETH Zurich
**Date:** April 2026
**Round:** 2 (follow-up after revisions)
**Previous overall rating:** 6/10

---

## 1. What Improved

**The DGP section is genuinely better.** My biggest complaint last time was that Section 2 hit me with six equations and then expected me to care. The new version adds the "What Is a Data Generating Process?" and "What Is OLS?" subsections before the equations, and that framing makes a real difference. The sentence "Think of it as a recipe: if you follow these steps, you get a dataset" is exactly the kind of sentence that keeps me from checking out. The new "Why These Relationships?" subsection that walks through each arrow in the causal graph is also good -- last time the graph just appeared with no context. Now there is an explicit bullet for each arrow ("Self-discipline -> studying: Obvious -- disciplined students put in more hours"). That is what I asked for. Rating goes up.

**The new Toy Stories land.** The CNN Coffee Miracle in the OVB section is better than the old Sunscreen Murder Mystery (which was already good). Coffee is something I actually drink, and the line "The coffee coefficient absorbed the ghost of kale salads and morning jogs" made me laugh. The "Hot Guys Are Jerks" cold open in Section 8 and the Pete Davidson example are excellent -- I would genuinely tell my friends about these. The COVID Smoking Paradox remark at the end of Section 9 is a real-world collider bias example with actual stakes. That is exactly the kind of thing I asked for in my "real failures with consequences" wishlist item.

**The "Predict Before You Peek" boxes.** These are new and they work. Asking me to write down a prediction before revealing the answer is a small thing but it forces engagement. The one in the heteroscedasticity section ("what fraction of nominal 95% CIs actually contain the true coefficient?") and the one in the specification error section ("what score does the linear model predict for 30 hours?") both made me pause and think. More of these.

**The Cold Open.** Starting the entire document with the seat number teaser and then calling back to it in the conclusion is a good structural move. It gives the whole thing a narrative arc instead of just being a sequence of sections.

**The visualization specifications.** These are new and they sound fantastic -- assuming they actually exist in the interactive notebooks. "Draw 100 new samples and watch confidence intervals cascade" is the kind of thing I would engage with for 20 minutes. The IV strength simulator with the F-statistic turning red sounds genuinely fun.

**Confidence intervals are now properly introduced.** Last time, the heteroscedasticity section jumped straight into the sandwich formula without explaining what a confidence interval even is. Now there is a full subsection with a definition, a careful explanation of what 95% does and does not mean, and the concept of coverage. This is good pedagogy.

**The roommate IV example is fleshed out.** Last time I said IV was "an entire lecture crammed into two pages." It is still dense, but the numerical example with five students, explicit OLS vs IV calculations, and the line "OLS nearly triples the true effect" makes the stakes concrete. I can follow the arithmetic and verify it myself. The remark about policy consequences ("a university would impose unreasonable requirements") gives it real-world weight.

---

## 2. What Is Still Boring

**The proofs have not moved.** I said last time: put the proofs in an appendix. They are all still inline. The bias-variance proof, the sandwich formula derivation, the FWL proof with the partitioned normal equations, the collider bias proof -- they are all still sitting right in the middle of the narrative. I still skip every single one. I appreciate that some students want them, but they break the flow for me. The OVB proof is the shortest and most tolerable. The FWL proof is the worst offender.

**Section 12 (Diagnostics) is still a reference table, not a section.** I said last time I would print it and bring it to the exam. That has not changed. It is useful but not engaging. In a lecture, this is a bathroom break.

**Section 13 (Theorem Map) is still for the professor.** I do not think in terms of "generalisation relationships." The new paragraph at the bottom that connects the theorems to the exam score DGP is an improvement, but the table itself still feels like an internal curriculum document. If you reframed it as "here is the order you should study these topics in, and here is what breaks if you skip one," I might care.

**The Cinelli-Hazlett framework in Section 9 is still too abstract.** It got slightly more context (the tutoring connection), but the formula $\text{RV}_{q,\alpha}$ is still opaque. I read it twice again and I still could not explain it to my study group. This section needs a worked numerical example with actual numbers, like every other section has.

**Cross-validation still has no numerical example.** I flagged this last time. Every other concept gets a table with five students and arithmetic I can verify. Cross-validation gets three paragraphs of text and a definition. I know what cross-validation is in theory. I do not know how to do it on paper from this description.

---

## 3. New Problems

**The notes got longer.** The additional context and framing are good, but the document is now even more massive. The new subsections ("What Is a DGP?", "What Is OLS?", "Why These Relationships?", "Confidence Intervals", the expanded IV section) all individually make sense, but collectively they push this toward textbook length. For a lecture, that is intimidating. A student opening this for the first time sees 60+ pages and might not start at all.

**Some of the new boxes feel like padding.** The "Try It Yourself: Sign the Bias" box with the dog ownership example is fine but predictable -- the hint gives away the entire answer. The "Polynomial Beauty Contest" warning box asks "which model would you deploy?" and then immediately tells me the answer. These feel less like genuine engagement and more like rhetorical questions dressed up as interaction.

**The Pete Davidson paragraph is a bit much.** The movie star spouse story is great. The Pete Davidson addition is funny but risks dating the notes. In three years, students might not know who he is (or might associate him with something completely different). The movie star spouse analogy is timeless; the celebrity gossip is not.

**The remark about negative study hours is unnecessary.** Spending a paragraph explaining why 0.3% of simulated students have negative study hours is the kind of technical disclaimer that only a fellow professor would care about. As a student, I would read "negative study hours" and think "that is obviously a simulation artifact" and move on. The remark slows down the DGP section right when it is building momentum.

---

## 4. Updated Section Ratings

| Section | Topic | Old Rating | New Rating | Change |
|---------|-------|-----------|-----------|--------|
| 1 | Introduction | 6 | 7 | +1 (cold open is strong, variable descriptions unchanged but flow better) |
| 2 | Data Generating Process | 4 | 6 | +2 (the "What Is a DGP?" and "Why These Relationships?" framing helps a lot) |
| 3 | Omitted Variable Bias | 7 | 8 | +1 (CNN Coffee story is great, "Sign the Bias" exercise is decent) |
| 4 | Heteroscedasticity | 5 | 6 | +1 (CI intro and "Predict Before You Peek" help; proof still kills momentum) |
| 5 | Significance vs Effect Size | 8 | 8 | 0 (was already the best section, no major changes needed) |
| 6 | Specification Error | 6 | 7 | +1 ("Predict Before You Peek" for the 30-hour student is good) |
| 7 | Overfitting | 7 | 7 | 0 (no significant changes, still missing a CV numerical example) |
| 8 | Endogeneity & Bad Controls | 7 | 8 | +1 (Pete Davidson is fun if risky, roommate IV example is much better) |
| 9 | The Real World | 6 | 7 | +1 (COVID smoking paradox is a real-world story with stakes) |
| 10 | Regression Discontinuity | 7 | 7 | 0 (unchanged, still solid) |
| 11 | Frisch-Waugh-Lovell | 5 | 6 | +1 (the coaching/shoes story is clearer, "bad controls via FWL" insight is new and good) |
| 12-13 | Diagnostics & Theorem Map | 5 | 5 | 0 (theorem map got a connecting paragraph, but still reads like a curriculum doc) |
| 14 | Conclusion | 6 | 7 | +1 (callbacks to seat number, coffee, hot guys tie the narrative together nicely) |

**Overall: 7/10** (up from 6/10). The notes are meaningfully better. The framing, the stories, and the engagement boxes all push in the right direction. But the core structural problem remains: proofs inline, no appendix separation, and the sheer length is now even more daunting. One more round of editing focused on length and proof placement could push this to an 8.

---

## 5. Top 3 Remaining Priorities

**1. Move proofs to an appendix.** This is my number one recommendation for the second time in a row. The proofs are not bad -- they are just in the wrong place. Every proof interrupts a story that was building momentum. Create an appendix, move all proofs there, and replace each with a one-line reference: "Proof: see Appendix A.3." The students who want rigor will find them. The rest of us will not have our flow broken. This single change would improve the reading experience more than anything else.

**2. Add a cross-validation numerical example.** Every major concept in these notes gets a table with five students and arithmetic you can check by hand. Cross-validation does not. Give me five students, three folds, show me the MSE calculation for each fold, show me the average. Make it as concrete as the OVB example or the FWL example. Right now cross-validation is the only core concept that is taught purely through text, and it shows.

**3. Add a worked numerical example for the Cinelli-Hazlett robustness value.** This is the most abstract concept in the notes and it has no numbers attached to it. Give me the tutoring scenario with actual partial R-squared values. Show me: "the observational estimate is -3, the robustness value is 0.04, meaning a confounder that explains just 4% of the variation in both tutoring and scores would flip the sign." That sentence, backed by arithmetic, would make the concept click. Right now it is a definition followed by hand-waving.

---

*"The notes went from 'I would attend for the Toy Stories' to 'I would attend for the Toy Stories and the interactive visualizations and maybe even some of the theory.' That is real progress. Move the proofs out of my way and I might actually read the whole thing."*
