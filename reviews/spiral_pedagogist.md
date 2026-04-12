# Spiral Pedagogist: Brainstorm for `dgp-intro.html`

**Audience:** 4th-semester ETH mech-eng students, no statistics background.
**Framing:** Bruner's spiral — revisit the same object (a scatter of exam scores) repeatedly, each loop adding one layer of reality. Anna and Ben are the two fixed points the student sees through every lens; everything else (noise, curvature, hidden U, heteroscedasticity, colliders) is introduced around them.

## Core design commitments

- **Anna and Ben are the compass.** They are drawn as two specific dots on every screen, always at `X₁=4, X₂=12`, with scores 82 and 68. Every new layer must answer: "What does this stage say about the gap between Anna and Ben?"
- **The scatter plot persists.** We never wipe the canvas. Points fade, morph, gain halos, get ghosts — but the axes (hours studied → exam score) are the visual anchor. Bruner's spiral literally: same picture, deeper reading.
- **Every stage ends with a "click to advance" only after a micro-prediction.** The student is asked to guess before the next layer lands. No passive scrolling.
- **The formula box at the top builds incrementally.** Start with `Y = 8·X₁`. By stage 8 it is the full DGP, but every new term lights up as it appears, and earlier terms dim — so students see the formula grow, not appear.

---

## Stage 1 — The honest world

**What's new:** The simplest universe. `Y = 50 + 8·X₁`. Deterministic. One predictor. No log, no noise, no U.

**What stays the same:** Nothing yet — this is the baseline.

**Animation concept:** A blank scatter plot. A slider labelled "hours studied" appears at the bottom. The student drags it from 0 to 8; a single dot traces a perfect straight line. Then 30 students rain down from the top as small dots, each landing exactly on the line. Anna (highlighted blue) and Ben (highlighted orange) land at `(4, 82)` and `(4, 82)` — **on top of each other**. A speech bubble from Anna: "Wait, why is Ben on my head?" A speech bubble from Ben: "Because in this world, same hours = same score."

**Insight to leave with:** "If hours studied were the whole story, anyone who studied 4 hours would score 82. Full stop. The model is a line, the students are beads on the line."

**Transition:** The lecturer's voice-over text appears: *"But you know this isn't true. You have friends who studied the same as you and got different scores. What would it take for Ben to fall off Anna's head?"* → Button: **"Add the first wrinkle."**

---

## Stage 2 — The first crack: idiosyncratic noise (ε, homoscedastic)

**What's new:** `Y = 50 + 8·X₁ + ε`, with ε ~ N(0, σ²) constant. "Bad luck on exam day" — misread a question, slept poorly, pen ran out.

**What stays the same:** The line. The slope. Anna and Ben still study 4 hours.

**Animation concept:** Each dot from Stage 1 gets a small vertical "jitter spring" attached to the line. A button **"Roll the dice"** jitters every dot by a fresh ε draw. Anna and Ben now separate slightly — maybe Anna at 84, Ben at 80. The line is still drawn through the cloud. A slider for σ lets students crank noise up and down: at σ=0 they snap back to the line; at σ=10 the cloud is wide. Crucially, **Anna and Ben swap positions** on some dice rolls (sometimes Ben is higher). This is the definition of noise: no pattern.

**Insight to leave with:** "Noise is symmetric and memoryless. If we re-ran the exam tomorrow, Anna and Ben would bounce around randomly — sometimes Anna higher, sometimes Ben. A straight line through the cloud still recovers the truth."

**Transition:** *"In real life, if we ran the exam 10 times, would Ben sometimes beat Anna? Think about your own friends. Probably not — the same person tends to do better each time. There's something else going on."* → **"Reveal the something else."**

---

## Stage 3 — The ghost appears (U, but still invisible)

**What's new:** The hidden variable U enters, but **the student cannot see it yet.** `Y = 50 + 8·X₁ + 2·U + ε`. Anna's U is +1.7, Ben's is −1.7.

**What stays the same:** Same axes, same slider, same ε. Anna and Ben still study 4 hours.

**Animation concept:** This is the dramatic moment. When the student clicks "Roll the dice" now, Anna **consistently** lands above Ben. Every roll. The student can hit the button 20 times; Anna is always higher. A counter ticks: "Anna above Ben: 17/20. 18/20. 19/20." A subtle question appears: *"Noise should be 50/50. Why is Anna winning every round?"*

Then a translucent grey silhouette — a literal ghost emoji or figure — fades in behind Anna, labeled with a "?". Same behind Ben but smaller / dimmer. **Ghosts are visible to us, the audience, but the regression line running across the plot does not bend to account for them.** The line is fit through the cloud as before, and a warning lights up: *"The fitted slope is 9.3, but the true slope is 8. Why?"*

**Insight to leave with:** "Something is pushing Anna up and Ben down every single time. It's not random. The model can't see it — but it's smearing into our slope estimate."

**Transition:** *"Let's pull the curtain back. What is the ghost?"* → **"Reveal U."**

---

## Stage 4 — Naming the ghost: the Instagram slider

**What's new:** U is named. Self-discipline. A second hidden slider appears, labeled "Instagram time (inverse) / self-discipline." The student can now drag U for Anna and Ben individually.

**What stays the same:** Formula. Line. Noise. Anna and Ben at 4 hours.

**Animation concept:** Two Instagram-phone icons appear next to Anna and Ben. Dragging Anna's phone toward "scroll all day" drops her U and her exam score slides down to meet Ben's. Dragging Ben's phone toward "phone in a drawer" lifts his U and his score rises to meet Anna's. **The students literally become each other when you swap their U.** A caption: "Anna minus her discipline = Ben."

Then a **"play God" mode**: the student can set U for the whole class via one master slider. Watch the cloud shift up or down as a whole. Watch the fitted regression slope tilt.

**Insight to leave with:** "The ghost has a name: self-discipline. It is a real number attached to every student. We just never measured it. And it moves exam scores by 2 points per unit — invisibly."

**Transition:** *"But here's the twist. Disciplined students don't just score higher — they also study more. U isn't just hiding in ε. It's hiding in X₁ too."* → **"Show the leak."**

---

## Stage 5 — The leak: U flows into X₁

**What's new:** `X₁ = 2 + 0.5·U + η₁`. Self-discipline causes hours studied. This is the confounding structure in full.

**What stays the same:** Y equation, the Instagram slider metaphor, Anna and Ben.

**Animation concept:** Up until now Anna and Ben were both pinned at X₁=4. Now the student drags Anna's Instagram slider up, and **her hours-studied dot slides right as well** — discipline makes her study more. Ben's slider down moves him left. The two dots pull apart horizontally, not just vertically.

Now the master "class U" slider: when discipline rises across the class, the **entire cloud migrates diagonally up-right** (more hours → higher scores). An OLS line is re-fit each frame. The student watches the fitted slope climb from 8 to ~10 as U variance increases. A red overlay draws the true slope (8) vs. the OLS slope (the steeper one); the gap is labeled **"omitted-variable bias."**

An **A/B toggle**: "Condition on U" vs. "Ignore U." Toggle on: two separate parallel lines appear, one for high-U students and one for low-U students, **both with slope 8.** Toggle off: one fat line with slope 10. Same data, two different stories.

**Insight to leave with:** "Hours studied is not exogenous. It is partly discipline in disguise. OLS cannot tell them apart, so it blames hours for what discipline did."

**Transition:** *"We've been assuming the line is straight. But think: is the 10th hour of studying worth as much as the 1st?"* → **"Curve reality."**

---

## Stage 6 — The curved world: the log

**What's new:** `Y = 50 + 8·log(X₁) + ...`. Diminishing returns.

**What stays the same:** U, ε, Anna, Ben, the plot axes.

**Animation concept:** The straight line **bends** smoothly into a log curve, as if a soft gravity pulled its right end down. A side-by-side: on the left, straight-line prediction for Anna and Ben (both predicted at 58.9); on the right, log prediction (both at ~61.1). Neither matches reality, but the log is closer — and more importantly, **the log + U together nail Anna (82) and Ben (68).**

Interaction: a radio toggle for the student's assumed functional form ("linear" / "log" / "square root"). Each choice redraws the fit. Residuals light up in red — large wedges for misfit, tiny flecks for fit. The log option minimises the red.

**Insight to leave with:** "The first hour of study matters more than the tenth. Reality curves. If we insist on a straight line, we systematically miss students at both ends of the X₁ range."

**Transition:** *"Anna doesn't just study more — she also attends more lectures. Let's add the second predictor."* → **"Bring in X₂."**

---

## Stage 7 — The second dimension: X₂ attendance

**What's new:** `X₂ = 10 + 0.3·U + η₂` and the `+3·X₂` term in Y. Now we have two predictors, both partially driven by U.

**What stays the same:** The log on X₁, U, ε, Anna, Ben.

**Animation concept:** The 2D scatter **tilts into 3D** — the plane X₁ × X₂ spreads out, and Y becomes height. A rotating axis shows Anna and Ben now at the same `(X₁=4, X₂=12)` grid cell but at different heights because U differs. The regression **plane** (not line) is fit; students can rotate the plot with a drag.

A smaller **"partial effect"** panel shows: hold X₂ fixed at 12, vary X₁ → see the log curve. Hold X₁ fixed at 4, vary X₂ → see the linear slope 3. This is ceteris paribus, visualised.

Crucially: when the student drags the class-U slider, **both X₁ and X₂ shift together.** Discipline leaks into two predictors simultaneously. The bias now smears across two coefficients. A caption: "U is hiding in two places now."

**Insight to leave with:** "More predictors don't solve the ghost — they give it more places to hide. Every variable correlated with U inherits a piece of its shadow."

**Transition:** *"We've been assuming noise is the same size for every student. Is that really true? Do weak students score as predictably as strong ones?"* → **"Let noise breathe."**

---

## Stage 8 — Heteroscedasticity: the fan

**What's new:** `ε ~ N(0, 0.5·|X₁|)`. Noise scales with hours studied.

**What stays the same:** Everything else.

**Animation concept:** The cloud of points, which has been roughly tube-shaped around the fit curve, now **opens like a fan** as X₁ increases. For low X₁ the dots hug the curve tightly; for high X₁ the dots spray widely. A "confidence tube" around the regression curve pulses in sync — narrow on the left, wide on the right.

Interaction: a heteroscedasticity slider (0 to 1) lets the student morph from homoscedastic back to heteroscedastic. At 0 the fan closes into a tube; at 1 it fully spreads. Anna and Ben (at X₁=4) are in the **middle** of the fan — their gap is mostly U, not noise. But pick a high-X₁ student: their gap from the curve could easily be noise.

**Insight to leave with:** "Not all predictions are equally certain. A student who studied 10 hours is less predictable than one who studied 1. The honesty of our prediction depends on where on the X₁ axis we stand."

**Transition:** *"One last variable. What if we measured something AFTER the exam — like how the student felt they did? Would that help predict Y?"* → **"The trap."**

---

## Stage 9 — The collider: X₃ as a post-treatment trap

**What's new:** `X₃ = 0.9·Y + η₃`. Self-assessed performance. The forbidden predictor.

**What stays the same:** All prior variables.

**Animation concept:** A new column "self-assessed performance" appears on the right. Arrows of causation are drawn **on the canvas** for the first time: U → X₁, U → X₂, U → Y, X₁ → Y, X₂ → Y, and crucially **Y → X₃**. The arrow points the wrong way for a predictor.

A big button **"Add X₃ to the regression"** appears. The student clicks it. The R² jumps to 0.98 — students cheer. Then a second panel shows: what is the coefficient on X₁ now? It has **collapsed toward zero.** Hours studied "no longer matters." Caption in red: *"You just told the model that hours studied don't affect the exam. Do you believe that?"*

Then stratify: among students who rated themselves 8, Anna and Ben both rated high and the within-stratum slope on X₁ is flat. Among students who rated themselves 5, same thing. **The collider sliced the data exactly where variation lived.**

A toggle lets the student remove X₃ and watch the X₁ coefficient snap back to something sensible.

**Insight to leave with:** "Adding variables doesn't always help. Some variables are downstream of Y — including them steals the signal you actually wanted. More data can make you more wrong."

**Transition (to the rest of the course):** *"You've now met every piece of the DGP. Self-discipline is a ghost. Hours studied is curved. Attendance is partial. Noise breathes. Self-assessment is a trap. The rest of this course is: given data from this world, what can we still recover?"*

---

## Cross-cutting design notes

**Play mode at the end of each stage.** After the student has seen the scripted story, a "sandbox" button unlocks the current DGP with all sliders free. They can build their own Anna, their own Ben, their own class. This respects Bruner's enactive mode — learning by doing after learning by watching.

**Anna and Ben are never hidden.** In every stage they are two distinctly coloured dots with labels. Even when the class cloud is dense, their dots have an outline / halo that keeps them visible. The spiral in Bruner's sense is: you know these two students already — now here is one more thing about them.

**Visual metaphors that should land:**

- **Ghost** for U in stage 3 (translucent figure behind each dot)
- **Leak / tint** for U flowing into X₁ (a coloured tint on the X₁ axis when the Instagram slider moves)
- **Bending ruler** for the log transition (the line literally warps)
- **Fan** for heteroscedasticity (noise width as visible spread)
- **Wrong-way arrow** for the collider (every other arrow points into Y; X₃'s arrow points out)
- **Curtain** for the "reveal U" moment (stage 4 opens with a drawn curtain swept aside)

**Where sliders dominate vs. pure animation:**

- Stages 1, 2, 6, 8: mostly animation + one slider. The student's job is to watch and predict.
- Stages 4, 5, 7: heavy interaction. U is the thing they need to *feel*, and feeling requires dragging.
- Stage 3: **no interaction yet** — this is the mystery stage. The student should feel confused by Anna always winning. Interaction would let them explain it away; we want them stuck.
- Stage 9: binary toggle (add X₃ or not) + a stratification drawer. The drama is in the flip, not in fine-tuning.

**Micro-predictions between stages.** Before each new stage lands, a one-sentence question: *"If we add noise, will Anna always beat Ben?"* / *"If discipline also causes hours, will the OLS slope get bigger or smaller?"* / *"If we add self-assessment, will R² go up, down, or stay the same?"* Wrong predictions are more memorable than right ones — the feedback is the point.

**The formula tracker.** Top-right corner, a LaTeX-rendered formula that grows from `Y = 8·X₁` in stage 1 to the full DGP in stage 9. New terms flash yellow when they first appear; established terms are grey. This gives the spiral a literal visual trace: students see how much world they've absorbed.

**Rough time budget:** 90 seconds per stage on average, with play mode optional. Total guided pass: ~15 minutes. A student who does every play mode: ~40 minutes. This matches a single pre-lecture homework.

**Accessibility note for mech-eng framing:** Stages 6 (log) and 7 (plane in 3D) will feel familiar — mech engs know curves and planes from thermodynamics and statics. Lean into this. Stages 3–5 (the hidden U) are where the pedagogical work is hardest, because "unmeasured causal drivers" has no mech-eng analogue. This is where we slow down, use the most animation, and let the student sit with mystery longest.
