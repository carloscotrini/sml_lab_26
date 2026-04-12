# Round 2 Follow-Up Review

**Reviewer:** Niklas (4th-year MechE, ETH)
**Date:** 10 April 2026

---

## Original Issues: Status Check

1. **Ambiguous epsilon notation** -- FIXED. Line 263 now explicitly states "0.5|X_1| is the variance, not the standard deviation." Clear and correct.
2. **Negative X_1 unacknowledged** -- FIXED. A dedicated Remark (line 255) acknowledges the ~0.3% negative values and explains the truncation tradeoff. Exactly what I asked for.
3. **Unverifiable heteroscedasticity numerical example** -- FIXED. The old made-up $53 + 6.5X$ fit is gone. The new table (line 620) uses $49.6 + 8.0X$ with an explicit verification line showing $\hat\beta_1 = 80/10 = 8.0$. I checked it; it works.
4. **VIF and Cook's distance undefined** -- FIXED. The diagnostics table (line 1611-1613) now defines both inline. VIF formula and Cook's distance formula are present. Good.
5. **Ice cream/drowning example** -- GONE. Replaced entirely. Thank you.
6. **82% coverage unsourced** -- PARTIALLY FIXED. Line 653 now clarifies it comes from "a simulation of the studying DGP," not a general claim. Acceptable, though showing the simulation setup would be better.
7. **Bias-variance independence assumption buried** -- NOT FIXED. The appendix proof (line 1799) still says "trained on separate data" in a parenthetical. The main text (line 974) is equally brief. This assumption is the entire reason test sets exist; it deserves one explicit sentence.
8. **Proxy variable $(1-q)$ claim unproven** -- NOT FIXED. Still stated without proof or citation (line 496).

## New Additions: Assessment

**A-level/Ofqual box:** Effective framing device. One concern: calling school reputation a "collider" is debatable. School reputation is arguably a mediator or a proxy for resources, not a classic collider in the Pearl sense. The causal structure is more nuanced than stated.

**Coefficient tracker:** Clever narrative device. The numbers are internally consistent across sections and the summary table (line 1635) ties them together well. No arithmetic errors found.

**Cinelli-Hazlett section:** Major improvement over Round 1. The partial $R^2$ remark, the RV definition, and the numerical example with the comparison table (line 1365) make this actionable. Previously my weakest section; now solid.

**CV example:** Clean and correct. The 35% MSE reduction claim checks out: $(43.2 - 27.9)/43.2 \approx 35\%$.

## Updated Rigor Rating: 8.0/10

Up from 7.6. The fixes were targeted and effective.

## Strongest Section

**Section 11 (FWL)** -- unchanged. Still the best-structured section with a verifiable example and complete proof.

## Weakest Section

**Section 7 (Overfitting/Bias-Variance)** -- the buried independence assumption is now the most significant remaining gap. The Lalonde section, previously weakest, has been substantially improved.
