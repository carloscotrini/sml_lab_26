# Visual Improvement Proposals for "Regression Autopsy"

**Reviewer:** Creative Visualizer (Data Visualization Expert)
**Date:** April 2026
**Scope:** Diagram replacements, infographic summaries, before/after slides, recurring visual, animation storyboards

---

## 1. Diagram Replacements

For each major concept, here is a visual that conveys the core intuition without equations. Each description is detailed enough for an illustrator or TikZ author to produce.

### 1.1 Omitted Variable Bias -- "The Ghost in the Machine"

**Layout:** A scatterplot of Hours Studied (x-axis) vs. Exam Score (y-axis) with two regression lines. The short-regression line (red, steeper) and the full-regression line (gold, correct slope). Between them, a semi-transparent "ghost" figure labeled U (Self-Discipline) floats behind the data cloud. From the ghost, two translucent arrows emerge: one pushes data points rightward (toward more studying) and one pushes them upward (toward higher scores). The ghost's hand literally tilts the red regression line upward from its correct gold position. A callout reads: "The ghost pushes both X and Y in the same direction, making OLS think X did all the work."

**Color scheme:** Ghost in biasred at 30% opacity. Gold line uses truthgold. Red line uses biasred. Data points in olsblue.

**Why it works:** Students can immediately see that the unobserved variable acts as an invisible hand on the regression line. The ghost metaphor matches the existing "Ghost in the Regression" visualization spec title.

---

### 1.2 Heteroscedasticity -- "The Trumpet Plot"

**Layout:** A horizontal trumpet shape. The left (narrow) end represents low study hours; the right (wide) end represents high study hours. Inside the trumpet, data points are scattered: tightly clustered on the left, spreading wildly on the right. A single regression line runs through the center. Two confidence bands are overlaid: a classical band (constant width, blue dashed) and a robust band (widening with the trumpet, green solid). At the narrow end, both bands are similar. At the wide end, the classical band is far too narrow -- mark this region with a red highlight and the label "False Confidence Zone."

Along the bottom, five small dartboard icons illustrate the progression: at X=1, darts cluster tightly around the bullseye; at X=3, moderate scatter; at X=5, darts hit the wall, the floor, and one arrow points to a bartender icon off-board. This directly echoes the "Drunk Darts" story.

**Why it works:** The trumpet shape is a single glanceable image that encodes both the data pattern and the inferential danger. The dartboards along the bottom tie it to the existing narrative.

---

### 1.3 Collider Bias -- "The Fame Filter"

**Layout:** Two panels side by side.

**Left panel ("Full Population"):** A 2D grid with Talent on the x-axis and Luck on the y-axis. Four quadrants are populated with stick figures. Bottom-left (low talent, low luck) figures are gray. The other three quadrants have colored figures. No visible correlation -- figures are evenly distributed. A large "r = 0" label sits in the corner.

**Right panel ("Famous Only"):** The same grid, but the bottom-left quadrant is now crossed out with a large X and labeled "Filtered Out." The remaining three quadrants show only the colored figures. A negative-slope dashed line appears through the remaining points. Label reads "r = -0.33" in red. A speech bubble from an observer says: "Talented famous people are never lucky! The universe must be fair." A footnote reads: "No. You just removed the people who are neither."

Between the two panels, a large funnel icon labeled "Condition on Fame" shows the filtering step.

**Why it works:** The side-by-side comparison makes the manufactured correlation visually undeniable. The crossed-out quadrant is the single visual element that explains everything.

---

### 1.4 Bias-Variance Tradeoff -- "Three Dart Players, One Board"

The notes already describe this metaphor. The proposal is to make it a real, detailed illustration rather than a text description.

**Layout:** Three dartboards arranged horizontally.

**Board 1 ("The Robot"):** All five darts clustered tightly in the upper-left quadrant, far from the bullseye. Label: "High Bias, Low Variance." Subtitle: "Consistently wrong."

**Board 2 ("The Drunk Expert"):** Five darts scattered across the entire board, but their centroid (marked with a small gold X) sits on the bullseye. Label: "Low Bias, High Variance." Subtitle: "Right on average, useless in practice."

**Board 3 ("The Wobble"):** One dart precisely on the bullseye, but the bullseye itself has a wavy halo around it, indicating the board is vibrating. Label: "Irreducible Noise." Subtitle: "Even perfect aim can't beat a shaking wall."

Below the three boards, a stacked bar chart shows Bias-squared (red), Variance (blue), and Noise (gray) for each player, directly connecting the visual metaphor to the mathematical decomposition.

---

### 1.5 Specification Error -- "The Straight Ruler on a Winding Road"

**Layout:** A bird's-eye view of a winding mountain road (S-shaped curve). A long straight ruler is placed on top, spanning the observed section of the road. Within the ruler's range, the fit looks decent -- the ruler roughly follows the road's average direction. Past the end of the ruler, the road curves sharply downhill to the right, but the ruler's extension (drawn as a red dashed line) flies off a cliff into empty sky. A small car icon sits at the ruler's end, about to drive off the cliff. Caption: "In-sample: reasonable. Out-of-sample: fiction."

Below this illustration, a miniature version shows the same story in scatterplot form: data points follow a log curve, the linear fit is okay within [1, 16], but at X=30 the linear prediction exceeds 100 (marked with a red "IMPOSSIBLE" flag).

---

### 1.6 Instrumental Variables -- "The Clean Pipe"

**Layout:** A plumbing diagram. Two pipes feed into a mixing valve (representing X1, hours studied). One pipe comes from U (self-discipline, colored red, labeled "contaminated") and the other from Z (roommate's study hours, colored green, labeled "clean"). Both pipes merge into X1, which then flows into Y (exam score). The IV estimator is illustrated as a filter that blocks the red pipe and only measures flow from the green pipe into Y.

Labels: "OLS measures total flow (contaminated)" with a red arrow. "IV measures only clean flow" with a green arrow. The ratio Cov(Z,Y)/Cov(Z,X) appears as a flow meter on the green pipe.

---

### 1.7 RDD -- "The Cliff"

**Layout:** A landscape cross-section. On the left, terrain slopes gently upward (representing outcomes below the cutoff). At exactly X=50 (the cutoff), there is a sharp cliff face -- terrain jumps up by exactly tau units. On the right, terrain continues sloping gently upward from the new, higher elevation. Two students stand on either side of the cliff: one at score 49 (just below) looking up at the other at score 51 (just above). They are drawn identically -- same height, same clothes, same backpack -- to emphasize they are effectively the same student. The only difference: one stands on lower ground. A measuring tape spans the cliff face, reading "tau = 5 points."

In the background, students far from the cliff (at scores 20 and 80) look noticeably different from each other, illustrating why we need to zoom in near the cutoff.

---

### 1.8 FWL -- "The Double Filter"

**Layout:** A three-stage pipeline diagram.

**Stage 1:** Two funnels at the top. Funnel A takes in Y (mood scores) and X2 (sleep) and outputs residuals Y-tilde ("mood that sleep can't explain"). Funnel B takes in X1 (exercise) and X2 (sleep) and outputs residuals X1-tilde ("exercise that sleep can't explain").

**Stage 2:** The two streams of residuals flow down into a single regression box.

**Stage 3:** Out comes beta-hat-1 = 4.684, which is shown to be exactly equal to the coefficient from the full multiple regression (displayed in a side panel for comparison).

At each funnel, small "before" and "after" scatterplots show the data and residuals. The visual makes "residualizing both sides" tangible.

---

## 2. Infographic Summaries (One-Page Wall Posters)

Each section gets a single-page visual summary with 3-4 key elements that a student could pin above their desk.

### 2.1 OVB Cheat Sheet

- **Top left:** The ghost diagram (Section 1.1 above), small version.
- **Top right:** The OVB formula in a large colored box: E[beta-hat-short] = beta-1 + beta-2 * delta-1, with each term labeled in plain language underneath: "What you get = What's true + (How much the omitted var matters) x (How correlated it is with your predictor)."
- **Bottom left:** A 2x2 sign table. Rows: beta-2 positive / negative. Columns: delta-1 positive / negative. Cells show: "Bias UP" (with up arrow), "Bias DOWN" (with down arrow), colored red and blue respectively. This is the "direction of bias" quick reference.
- **Bottom right:** The five-student numerical example in miniature, showing the coefficient shifting from 5.0 to 2.6 with a large red arrow.

### 2.2 Heteroscedasticity Cheat Sheet

- **Top:** The trumpet plot (Section 1.2 above), spanning the full width.
- **Middle left:** Classical vs. Robust SE comparison. Two confidence intervals for the same estimate, side by side: the classical one (too narrow, labeled "Lying about your uncertainty") and the robust one (wider, labeled "Honest").
- **Middle right:** The Breusch-Pagan test in three steps, as a flowchart: (1) Run your regression, get residuals. (2) Square them, regress on X. (3) If nR-squared > chi-squared critical value, your errors are heteroscedastic.
- **Bottom:** The repair in one sentence: "Use sandwich standard errors. Each observation vouches for its own noise level."

### 2.3 Significance vs. Effect Size Cheat Sheet

- **Top:** Two "dashboards" side by side. Left dashboard: a gauge labeled "p-value" with the needle deep in the green zone (p = 0.002). Right dashboard: a gauge labeled "Effect Size" with the needle barely above zero (0.003 points). Large label: "These two gauges measure different things."
- **Middle:** The keyboard table (n = 5, 50, 5000) rendered as three magnifying glasses of increasing size, all focused on the same tiny effect (0.1 seconds). The smallest glass says "Not significant." The largest screams "p < 0.001!!!" The effect dot under each glass is the same size.
- **Bottom:** The multiple testing formula (E[false positives] = m * alpha) with an icon grid: 200 small squares representing 200 tests, with 10 randomly highlighted in red ("false positives by pure chance").

### 2.4 Causation / Bad Controls Cheat Sheet

- **Top left:** The Fame Filter two-panel diagram (Section 1.3 above), compact version.
- **Top right:** A decision tree for variable inclusion: "Does the variable cause Y? --> Is it also correlated with X? --> YES: Control for it. // Is the variable CAUSED BY Y or the treatment? --> NEVER control for it. // Is it downstream of a collider? --> NEVER control for it."
- **Bottom:** The IV plumbing diagram (Section 1.6 above) in miniature, with the three-word summary: "Find clean variation."

### 2.5 Overfitting Cheat Sheet

- **Top:** The three dartboards (Section 1.4 above).
- **Middle:** The polynomial degree table (degrees 1, 3, 7, 15) with training R-squared as ascending green bars and test R-squared as bars that rise then crash below zero. The U-shape is visually immediate.
- **Bottom:** A single sentence in large text: "A model that explains 97% of your training data might be explaining mostly noise."

### 2.6 RDD Cheat Sheet

- **Top:** The cliff landscape (Section 1.7 above).
- **Middle:** The bandwidth tradeoff as a slider visualization: narrow (few points, clean estimate, wide error bars) vs. wide (many points, biased estimate, narrow error bars).
- **Bottom:** The key insight: "No confounders needed. The design earns trust."

### 2.7 FWL Cheat Sheet

- **Top:** The double filter pipeline (Section 1.8 above).
- **Middle:** The three-step algorithm in large numbered boxes: (1) Remove X2 from Y. (2) Remove X2 from X1. (3) Regress leftovers on leftovers.
- **Bottom:** The warning: "This also reveals what goes wrong with bad controls. Residualizing on a post-treatment variable destroys your signal."

---

## 3. Before/After Slides

Five pairs of slides. Each "Before" slide shows the naive view; each "After" slide reveals what is actually happening. The contrast IS the lesson.

### Slide Pair 1: OVB

**Before:** A clean scatterplot of study hours vs. exam score with a steep positive regression line. Title: "Studying 1 extra hour raises your score by 10 points!" A green checkmark. A student fist-pumping.

**After:** The same scatterplot, but now the ghost of Self-Discipline is visible behind the data cloud. The regression line has split in two: the red naive line (steep) and the gold true line (less steep). Title: "Actually, self-discipline is doing half the work." Red X replaces the checkmark. The ghost is pulling data points along both axes simultaneously.

### Slide Pair 2: Heteroscedasticity

**Before:** A regression line with a narrow, constant-width confidence band. Title: "We're 95% confident the true slope is between 6.2 and 7.8." A blue shield icon labeled "Reliable."

**After:** The same regression line, but the data points now visibly fan out to the right (the trumpet). The classical confidence band is still shown (narrow, dashed, labeled "Claimed 95%, actual 82%"), and alongside it the robust band (wider, solid, labeled "Actual 95%"). Title: "Your uncertainty estimate is lying." The blue shield is cracked.

### Slide Pair 3: Significance vs. Effect Size

**Before:** A headline: "NEW KEYBOARD LAYOUT SIGNIFICANTLY IMPROVES PRODUCTIVITY (p < 0.001)." A bar chart shows the t-statistic towering above the significance threshold. Confetti animation.

**After:** The same headline, but now a second axis is added showing the actual effect: 0.1 seconds per email. A person typing is shown with a tiny clock showing "0.1 sec." Title: "Statistically significant. Practically meaningless." The confetti has turned to dust.

### Slide Pair 4: Bad Controls / Collider Bias

**Before:** A researcher at a whiteboard says: "I controlled for everything in my dataset: study hours, lectures, AND post-exam confidence. My model must be right!" A checklist with all items ticked. R-squared = 0.94.

**After:** The same whiteboard, but now a causal graph is drawn. An arrow from Y to X3 is highlighted in red. The researcher's checklist now has the confidence variable crossed out in red with the note: "This variable is CAUSED by Y. Including it opened a path that wasn't there before." The coefficient on study hours has collapsed from 10 to 2. Title: "More controls made it worse."

### Slide Pair 5: Observational vs. Experimental

**Before:** A bar chart: "Students who attended tutoring scored 3 points LOWER." An administrator holds a sign: "SHUT DOWN THE TUTORING PROGRAM." OLS output table with negative coefficient.

**After:** Two bar charts side by side. Left: the same observational result (negative). Right: the experimental result (positive, +8 points). Between them, an arrow labeled "Self-Selection" explains the difference: students who sought tutoring were already struggling. Title: "The data looked fine. Every diagnostic passed. The answer was still directionally wrong." The administrator now holds a sign: "I almost made a terrible mistake."

---

## 4. The Recurring Visual: "The Shifting Regression Line"

**Concept:** A single regression line for "hours studied vs. exam score" that appears at the top of every section as a narrow banner. Each section transforms it in a specific way, building a cumulative visual story.

**Section 1 (Intro):** A clean, confident blue line through a scatter of points. Label: "OLS says: 10 points per hour."

**Section 2 (DGP):** The same line, but now a faint gold "truth" line appears below it, less steep. Label: "Truth says: 8 points per log-hour."

**Section 3 (OVB):** The blue line is annotated with a red delta-arrow showing the gap between it and the truth. The ghost icon appears. Label: "The gap is OVB."

**Section 4 (Heteroscedasticity):** The confidence band around the blue line changes from constant-width to a trumpet shape. Label: "The uncertainty was wrong too."

**Section 5 (Significance):** The t-statistic value grows as the sample size increases (shown as the scatter getting denser), but the gap between lines stays the same. Label: "Significant, not important."

**Section 6 (Specification):** The gold truth line is revealed to be a curve (log), not a straight line. The blue line only matches it in a narrow range. Outside that range, they diverge catastrophically. Label: "It was never a line."

**Section 7 (Overfitting):** Multiple polynomial curves (degree 3, 7, 15) are overlaid, each one wilder than the last. The degree-15 curve oscillates violently. Label: "More flexible is not more right."

**Section 8 (Causation):** The blue line splits into two: an OLS line (biased) and an IV line (correct but noisier / wider band). A "clean pipe" icon appears next to the IV line. Label: "IV: noisy but honest."

**Section 9 (Real World):** The blue line flips to a negative slope. All diagnostic checkmarks are green, but the line points the wrong way. Label: "Everything looked fine. Everything was wrong."

**Section 10 (RDD):** A vertical cutoff line appears at X=50. On either side of it, two short local regression segments form a cliff. Label: "Zoom in. Let the design do the work."

**Section 11 (FWL):** The scatter is replaced by residual scatter (Y-tilde vs X1-tilde). The slope of the residual regression is marked as identical to the full-model coefficient. Label: "This is what 'controlling for' actually means."

**Section 12 (Conclusion):** All previous versions of the line are layered transparently, one on top of another, showing the full journey from naive to informed. The final gold truth curve is drawn thick and solid on top. Label: "You are finally ready to start."

This banner should be implemented as a small TikZ graphic (approximately 3cm tall) inserted via a custom LaTeX command at the start of each section, so students see the regression line evolving as they read.

---

## 5. Animation Storyboards

### 5.1 Animation: "The Ghost Appears" (OVB, 30 seconds)

**0-5s:** A scatterplot of study hours vs. exam score populates dot by dot. A regression line fits through the data. A confident label appears: "beta = 10.2."

**5-10s:** The background dims. A translucent figure (the "ghost" of self-discipline) fades in, hovering behind the scatter. Two glowing arrows extend from the ghost: one pulls dots rightward (more studying), one pulls dots upward (higher scores).

**10-18s:** The dots begin to glow in a gradient from blue (low discipline) to red (high discipline). The viewer can now see that high-discipline students cluster in the upper-right and low-discipline in the lower-left. The regression line is visibly steered by this color gradient.

**18-25s:** A second "truth" regression line draws in gold, less steep. The gap between the red line and the gold line is highlighted and labeled "OVB = beta-2 times delta-1." The ghost's hand is shown physically tilting the red line away from the gold line.

**25-30s:** A slider labeled "Correlation between U and X" appears. It slides from 0.5 to 0: the ghost fades, the red line rotates down to meet the gold line. Slides back to 0.5: the ghost reappears, the gap reopens. Final frame: "The bias is proportional to the ghost's influence."

---

### 5.2 Animation: "The Funnel Opens" (Heteroscedasticity, 30 seconds)

**0-5s:** A horizontal axis labeled "Hours Studied" and a vertical axis labeled "Exam Score." Data points appear, left to right, starting at X=1. The first few points cluster tightly around the regression line -- barely any vertical spread.

**5-12s:** As X increases, new points appear with progressively more vertical scatter. The data cloud takes on a trumpet/funnel shape. The regression line draws through the center. A label reads: "The more you study, the more unpredictable your score."

**12-18s:** A classical (constant-width) confidence band appears in blue. A counter runs "Drawing 100 samples..." and 100 thin confidence intervals cascade from top to bottom. Green if they contain the true slope, red if they miss. On the right side of the funnel (high X), a disproportionate number are red.

**18-22s:** A large counter reads: "Classical coverage: 82%." Pause for emphasis. A "promised" label reads "95%." The difference is highlighted.

**22-28s:** The blue band morphs into a green robust band that widens with the funnel. The cascade redraws. Now the coverage counter reads: "Robust coverage: 95%." Green check.

**28-30s:** Final frame: split view. Left: "Classical SE: pretends the trumpet doesn't exist." Right: "Robust SE: respects the trumpet." Trumpet icon as a mnemonic.

---

### 5.3 Animation: "The Fame Filter" (Collider Bias, 30 seconds)

**0-5s:** A 2D grid appears: Talent (x-axis, 0-1) and Luck (y-axis, 0-1). 400 dots populate uniformly across the grid. Each dot is a person. A correlation readout in the corner says "r = 0.00." No pattern visible.

**5-10s:** Each dot gets colored by its "Fame" score (Talent + Luck). A color scale runs from gray (low fame) to gold (high fame). The dots do not move -- the coloring just reveals that fame is spread across the grid with no pattern between Talent and Luck.

**10-16s:** A "Fame Threshold" slider appears and begins to rise. As it climbs, dots below the threshold fade to near-invisibility. At threshold = 1.0 (meaning you need at least Talent + Luck >= 1.0 to be "famous"), the bottom-left triangle of dots has vanished.

**16-22s:** The remaining visible dots now form a band from upper-left (lucky, not talented) to lower-right (talented, not lucky). A regression line draws through them with a clear negative slope. The correlation readout updates: "r = -0.33." A label appears: "Among the famous, talent and luck appear negatively correlated."

**22-27s:** The animation zooms in on a single famous person in the upper-left (high luck, low talent). A speech bubble: "Look at that talented person's boring spouse!" Another famous person in the lower-right (high talent, low luck). Speech bubble: "Look at that lucky person who has no talent!" Both speech bubbles then get crossed out.

**27-30s:** The threshold slider slides back to zero. All dots reappear. The negative slope vanishes. r snaps back to 0.00. Final text: "The correlation was never real. You manufactured it by filtering."

---

## Summary

The proposals above address the core feedback from Max and Sofia: walls of equations kill engagement. Each visualization is designed to convey a concept's intuition in a single glance. The recurring regression-line banner creates continuity across sections. The before/after slides provide the emotional contrast that makes lessons stick. The animations bring the three most commonly misunderstood concepts to life in a format suitable for lecture or online embedding.

All diagrams use the existing color scheme defined in the LaTeX preamble (olsblue, truthgold, biasred, repairgreen) for visual consistency with the notes.
