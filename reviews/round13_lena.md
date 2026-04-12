# Round 13 Follow-Up Review

**Reviewer:** Lena M., 2nd-year Mechanical Engineering
**Date:** April 2026

---

## Original Concerns: Status Check

1. **Variance vs. SD ambiguity in epsilon** -- FIXED. The DGP paragraph now explicitly states "where 0.5 |X1| is the *variance*, not the standard deviation." Exactly what I asked for.
2. **Chi-squared distribution undefined** -- FIXED. Remark before the Breusch-Pagan test defines it as the sum of squared standard normals. Clear and sufficient.
3. **plim / probability limit** -- FIXED (was partially addressed before, now the remark is clean). Consistency is also properly defined in the IV section.
4. **Potential outcomes undefined** -- FIXED. A dedicated remark before the RDD section defines Y0, Y1, and the fundamental problem of causal inference. This was my single biggest complaint, and it is resolved.
5. **Partial R-squared undefined** -- FIXED. A remark now defines it via the FWL-style residual-on-residual regression. The sensitivity analysis section finally makes sense to me.
6. **VIF and Cook's distance undefined** -- FIXED. The diagnostics table now includes formulas for VIF and Cook's distance. Durbin-Watson and Jarque-Bera are still name-only, but those matter less.
7. **Conditional covariance formula (collider proof)** -- STILL UNJUSTIFIED. The formula appears in the appendix proof without derivation or reference. This remains the hardest single line in the document for me.
8. **log vs. ln convention** -- NOT FIXED. The notes still write log(X1) everywhere without stating whether this is natural log. The numerical check (8 log(2) = 5.5) only works for ln. Please write ln or add one sentence stating the convention.
9. **Bonferroni union bound argument** -- NOT ADDED. The correction is stated but the one-line proof via Boole's inequality is still missing.
10. **OLS unbiasedness under heteroscedasticity** -- The theorem states it but still does not explain *why* (because E[epsilon | X] = 0 is unaffected by the variance structure). One sentence would close this.

## New Issues

None significant. The added material (replication crisis remark, coefficient tracker, Ofqual cold open) is well-integrated and does not introduce new undefined terms.

## Updated Rating: 8.5/10

Up from 7.5. The four gaps I flagged as exam-killers have mostly been closed. I could now handle hard questions on potential outcomes, sensitivity analysis, and heteroscedasticity testing.

## Top 3 Remaining Concerns

1. **Conditional covariance formula** in the collider bias proof -- still no derivation or reference.
2. **log vs. ln** -- still ambiguous throughout. Trivial to fix, still not fixed.
3. **Bonferroni one-line proof** -- still missing the union bound argument that would make the correction feel earned rather than handed down.
