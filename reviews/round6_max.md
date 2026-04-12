# Follow-Up Review: Round 3
**Reviewer:** Max, 3rd-year Mechanical Engineering, ETH Zurich
**Date:** April 2026
**Round:** 3
**Previous ratings:** 6/10 -> 7/10

---

## 1. Did Moving Proofs to the Appendix Help?

Yes. This is the single best change so far. All five major proofs (OVB, Collider Bias, Sandwich Estimator, Bias-Variance, FWL) now live in Appendix A, and the main text has punchline summaries instead -- short "Why is this true?" paragraphs that give the intuition without the matrix algebra. The FWL section, which I previously called the densest piece of linear algebra in the entire document, now reads like a normal section. I no longer hit a wall of partitioned normal equations in the middle of the coaching/shoes story. This change alone is worth a full point. The main text finally flows the way the Toy Stories always wanted it to.

## 2. Does the Cross-Validation Example Work?

Yes. Five folds, two candidate models (linear vs log), concrete MSE numbers per fold, and a clear winner. This is exactly what I asked for twice. I can verify the arithmetic, I can see that the log model wins on every fold, and the connection to the DGP is explicit. The warning box about CV overfitting with 500 model specifications is also a nice touch -- it anticipates the "just CV everything" mindset that I would have walked away with otherwise.

## 3. The Replication Crisis Remark

Good addition. The Open Science Collaboration stat (only 36 out of 100 studies replicated) is concrete and alarming. The final line -- "Is this a seat number?" -- callbacks to the cold open nicely. It gives the significance section real-world stakes without adding bloat.

## 4. Updated Rating: 8/10

Up from 7. The proof relocation and the CV example were my top two priorities in both previous reviews, and both are now addressed well. The notes finally feel like they are written for students first and mathematicians second.

## 5. Top 2 Remaining Issues

**1. The Cinelli-Hazlett robustness value still has no numerical example.** This was my third priority last round and it remains untouched. Every other concept in the notes has a worked example with actual numbers. This one is still a formula and a definition. Give me the tutoring scenario with partial R-squared values I can check.

**2. Length.** The notes are now even longer with the appendix added on top of everything else. For a student opening this cold, the page count is intimidating. A one-page "roadmap" at the start -- telling me which sections to read for which exam topics -- would help me not panic.

---

*"You listened. Twice. The proofs are out of my way, the CV example exists, and I can read front-to-back without reaching for my phone. Two more reviews ago I said this could be an 8 if you moved the proofs. You moved them. It is an 8."*
