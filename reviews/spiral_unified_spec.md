# Unified Implementation Spec — `dgp-intro.html`

**Target:** `/site/playground/dgp-intro.html`
**Shared modules:** `site/playground/shared/{dgp.js, regression.js, plot.js, table.js, style.css}`
**Stack:** ES modules, D3 v7, KaTeX. No framework.
**Budget:** ~500–1500 lines HTML/JS. One page. Scrollytelling layout.

---

## Top-level decisions (resolving disagreements)

1. **Stage count: 8.** The pedagogist's 9-stage arc is collapsed by merging his Stage 3 ("ghost appears") and Stage 4 ("naming U") into a single Stage 1 that introduces U upfront as a named hidden variable — this follows the narrator's and animator's lead. Rationale: mech-eng students don't need a "mystery" pre-reveal; naming U as *self-discipline* immediately gives them a concrete hook, and the pedagogist's mystery beat is preserved inside Stage 6's "reveal" payoff.
2. **The "optional" stages (animator's Stage 8 free-play dashboard and the pedagogist's per-stage sandbox) are cut from the guided arc and folded into a single terminal "playground open" state.** Reason: scope. We keep it as the natural ending of Stage 8, not a separate stage.
3. **DGP ordering is the narrator's + animator's, NOT the pedagogist's.** We build *causes first* (U → X₁ → X₂ → Y) rather than the pedagogist's *effect first* (Y = line, then add noise, then reveal U). Rationale: starting from U is more faithful to the data-generating process and avoids the "noise without a reason" stage that adds a step without new insight.
4. **Visual language:** animator's locked palette — violet = truth, green = estimate, amber = Anna, teal = Ben, grey = noise.
5. **Voice:** narrator's second-person prose verbatim. Pedagogist's "Anna always above Ben" drama is preserved at Stage 6.
6. **Anna & Ben coordinates:** narrator's values — `X₁ = 2 hours, X₂ = 10 lectures, Anna Y = 72, Ben Y = 58`. (Pedagogist's 4/12/82/68 is dropped for consistency with the prose, which would be harder to rewrite.)
7. **Anna & Ben rendering:** animator's 24px SVG avatars with single-line faces, halos encoding U. (Pedagogist's "two coloured dots" is the fallback at small sizes.)
8. **Layout:** **scrollytelling** with a sticky viz pane on the right and scrolling text on the left. The formula tracker + U widget live in a persistent top bar that spans both. Each stage is a `<section>` whose scroll-into-view fires its transition.

---

## Stage 1 — Meet Anna and Ben

**Pedagogical goal:** Establish U as a real but unobservable trait. The student learns that two students can be identical on paper and still different in ways no dataset captures.

**Animation storyboard.**
- `t=0` — warm off-white canvas empty.
- `t=0.4s` — Anna's 60px avatar fades in left (amber accent, slight-smile face + glasses glyph); bobs once (sine, 3s period).
- `t=0.8s` — Ben's avatar fades in right (teal accent, neutral mouth + hoodie arc); bobs out of phase.
- `t=1.4s` — serif names drift up from below each avatar.
- `t=2.0s` — a faint vertical axis labelled "self-discipline U" draws itself down the middle (opacity 0 → 0.3, 600ms).
- `t=3.0s` — Anna glides up the axis to U = +0.85σ (halo brightens to 4px amber glow); Ben glides down to U = −0.85σ (halo dims to 1px teal). `easeCubicInOut`, 1200ms.
- `t=4.5s` — a translucent violet N(0,1) ridge fades in behind the axis; Anna and Ben are visibly samples from it.
- `t=6.0s` — a grey gaussian-blur **veil** slides down from the top and covers both avatars to ~70% opacity. Halos fight through but lose clarity.

**Narrative text (left column, scrolls past).**
> Meet Anna. Meet Ben.
>
> They sit in the same lecture hall. They take the same notes. This semester, both tell you — honestly — that they studied **2 hours a day** and attended **10 out of 12 lectures**.
>
> Then the exam happens. Anna scores **72**. Ben scores **58**.
>
> *Same hours. Same attendance. Fourteen-point gap.*
>
> You're going to spend the next ten minutes figuring out why — by building, piece by piece, the hidden machine that produces exam scores in this world.
>
> First, something you won't see in any spreadsheet. Call it **U** — self-discipline, grit, focus, whatever you like. Anna has a lot of it. Ben has less. It's real, and it's about to start pulling strings.
>
> *U is who they really are — and we will never see it directly.*

**Interactive handles.** One slider: **"Draw new people"** — re-samples 8 anonymous 16px avatars along the U axis (staggered 80ms delays). Anna and Ben stay pinned.

**Transition to Stage 2.** The veil stays. The vertical U axis **rotates 90° counterclockwise** (1000ms) and flattens into the horizontal X₁ axis of Stage 2. Anna and Ben slide along with it to their Stage-2 positions. This rotation is the visual thesis: U was vertical and hidden; its consequences will be horizontal and visible.

---

## Stage 2 — What U does to study hours

**Pedagogical goal:** Hidden causes produce visible behaviour. `X₁ = 2 + 0.5·U + η₁`. Students feel how much of the X₁ spread comes from U vs. from noise.

**Animation storyboard.**
- U axis shrinks to an **inset widget** top-left (veiled, bobbing — persistent from now on).
- `t=0.5s` — `X₁ = 2 + 0.5·U + η₁` types in at top-right via KaTeX, term by term (400ms each). `2` lands black; `0.5·U` glows violet briefly; `η₁` shimmers grey.
- `t=2.5s` — a **violet arrow** shoots from the U widget horizontally into the main canvas. Both avatars slide right: Anna to `X₁ ≈ 2.43`, Ben to `X₁ ≈ 1.57`. `easeCubicOut`, 900ms. Arrow fades at 1200ms.
- `t=4.0s` — grey jitter activates: each avatar trembles with `η₁ ~ N(0, 0.3)` re-sampled every 600ms, spring-damped. Runs 3s.
- `t=7.0s` — jitter freezes; faint dotted verticals mark each avatar's final X₁.

**Narrative text.**
> Every real measurement is the signal plus something else. A sneeze. A typo. A question that happened to favor one student's intuition.
>
> But before the noise arrives, notice something else: **U has already moved them.** Anna's discipline didn't just sit in her head — it pushed her to study more hours. Ben's lower U pushed him to study fewer. The *same* hidden trait leaked into what we thought was an independent input.
>
> That violet arrow is the cause. The grey shimmer is the chance. Both land in the same number — hours studied — and from the outside, we can't tell them apart.

**Interactive handles.**
- Button **"Resample η"** — re-runs jitter (1.5s).
- Toggle **"Show U's push"** — OFF collapses both avatars to x = 2 with jitter only; flipping ON leaps them apart with 900ms elastic ease. (Aha beat: *"That gap? That's U."*)

**Transition to Stage 3.** The X₁ axis slides down to become the bottom axis of a 2D scatter. A Y-axis grows upward labelled "X₂ lectures attended." Avatars keep their X₁, now rise to their X₂.

---

## Stage 3 — Two windows onto U

**Pedagogical goal:** Multiple observables are partial shadows of the same U. `X₂ = 10 + 0.3·U + η₂`. Correlation between X₁ and X₂ is U's fingerprint.

**Animation storyboard.**
- `t=0.8s` — `X₂ = 10 + 0.3·U + η₂` types in below the first equation.
- `t=1.5s` — violet arrow from U widget **forks**: horizontal to X₁, vertical to X₂. Anna rises to X₂ ≈ 10.25, Ben drops to X₂ ≈ 9.75.
- `t=3.0s` — grey jitter on both axes for both avatars.
- `t=4.5s` — **fountain spawn**: 200 anonymous grey dots (r=2, opacity 0.5) arc in from the origin with staggered 15ms delays, settling into a diagonally elongated cloud (canvas rendering).
- `t=7.5s` — a thin violet population-regression line of X₂ on X₁ fades in at 30% opacity through the cloud.

**Narrative text.**
> A detective never trusts a single witness. Neither should a model.
>
> We're going to add a second variable — **X₂**, lectures attended. Same story: U pushes it, noise jitters it. But watch what happens when we put both axes in the same picture.
>
> A hundred anonymous students rain in. The cloud tilts. Why? Because U is still pulling the strings — on both axes at once. Students with high U study more *and* attend more. Students with low U do neither. The tilt you see is U's fingerprint on the data.

**Interactive handles.**
- Slider **"Strength of U's fingerprint"** (0 → 2, scales the 0.5 and 0.3 coefficients together). At 0 the cloud is a circular blob; at 2 it's nearly a line. Caption at 0: *"No U, no correlation. U is the whole story."*
- Button **"Replay the fountain"** — re-samples the 200 points.

**Transition to Stage 4.** The (X₁, X₂) cloud dims to 15% opacity. A new Y-axis grows on the right. Canvas splits via CSS grid animation (`1fr 0fr → 1fr 1fr`, 1200ms).

---

## Stage 4 — The outcome (the full DGP arrives)

**Pedagogical goal:** Y depends on observables, on U directly, and on heteroscedastic noise. `Y = 50 + 8·log(X₁) + 3·X₂ + 2·U + ε`, with `ε ~ N(0, 0.5·X₁)`. Log curvature and heteroscedasticity land together, but both are secondary to the main beat: **the full generative truth is revealed.**

**Animation storyboard.**
- `t=0` — split screen: left (X₁, X₂) cloud dimmed, right empty (X₁, Y) panel.
- `t=0` — Y equation types in at top, term by term, 500ms each. Colour-codes in place: `50` black, `8·log(X₁)` green, `3·X₂` green, `2·U` violet, `ε` grey.
- `t=3.0s` — **firefly migration**: each of the 200 left-pane points sends a 1px 30% opacity arc to its computed Y on the right pane, staggered 10ms, each 400ms long.
- `t=7.5s` — trails fade (1000ms), leaving the new (X₁, Y) cloud. Anna and Ben land last with a small elastic bounce.
- `t=9.0s` — the **true regression curve** (expected Y given X₁, integrating over X₂ and U) draws left-to-right in violet with a traveling sparkler head, 1500ms.
- `t=11.0s` — heteroscedastic **violet ribbon** breathes around the curve (width ∝ `0.5·X₁`, 4s opacity oscillation 0.15 ↔ 0.25).

**Narrative text.**
> Now the exam happens. And the machine that produces scores looks like this:
>
> `Y = 50 + 8·log(X₁) + 3·X₂ + 2·U + ε`
>
> Every term earns its place. The `log` says the first hour of study is worth much more than the tenth — diminishing returns, baked right in. The `3·X₂` rewards showing up. The `2·U` is the direct fingerprint of discipline on the exam itself. And `ε` is what's left — the sneezes, the lucky guesses, the pen that ran out.
>
> Look closely at that noise. The cloud doesn't have uniform width. Students who studied little scatter tightly. Students who studied a lot scatter wildly. This is called **heteroscedasticity** — different scatter in different regions — and it will matter when we start trusting our predictions.

**Interactive handles.**
- Slider **"noise scale"** — multiplies the 0.5 coefficient in ε's std (0 → 2). Points re-jitter live.
- Toggle **"Include 2·U term"** — OFF collapses Anna and Ben toward the curve (preview of what controlling for U would buy).
- Scrubber **"time"** — replays the firefly migration at any speed.

**Transition to Stage 5.** Left pane fades entirely. Right pane expands to full width (CSS grid 1fr 0fr). Violet truth curve stays; Anna and Ben stay highlighted.

---

## Stage 5 — The estimator arrives

**Pedagogical goal:** OLS fits what it can see. Students feel least-squares as physical spring equilibrium, then see the gap between estimate (green) and truth (violet).

**Animation storyboard.**
- `t=0` — green candidate line drops from above with wrong slope, wiggling. Labeled "β₀ + β₁·X₁".
- `t=1.5s` — **residual sticks** (vertical grey segments) draw from each point to the green line, 200ms each.
- `t=3.0s` — sticks act as **springs**: pull the green line through 2s `easeCubicInOut` toward OLS optimum. Sticks shorten as it moves.
- `t=5.5s` — line settles at β̂ₒₗₛ; sticks shrink to minimal SSR config and fade to 10% opacity.
- `t=6.5s` — green line locks colour; violet truth curve re-brightens to 0.7 opacity underneath. Gap visible at low and high X₁ (log misspecification).

**Narrative text.**
> Here is the magic trick at the heart of regression. We can't see U. We can't see ε. All we get is the cloud.
>
> Our job is to draw the line that sits as close as possible to every dot at once — the line that minimises the total squared distance from the dots to itself. **Ordinary Least Squares.** OLS. The workhorse of every statistics course ever taught.
>
> Watch it find its equilibrium. The little grey sticks are like springs pulling on the line; it settles where the total tension is smallest.
>
> But our line is straight, and the truth isn't. Look at the gap at the extremes. Going from 1 hour to 2 is life-changing. Going from 9 to 10 is just an extra hour of panic. Can we fix this?

**Interactive handles.**
- **Draggable line endpoints.** Grab either end, see SSR rise in a live readout; release, line springs back to OLS (elastic).
- Button **"Resample the data"** — new 200 points, OLS refit with 800ms transition (sampling variability visible).
- Toggle **"Use log(X₁) as feature"** — green line morphs to a curve (1200ms `d3.interpolate` on y-values), nests into violet truth — but a residual vertical gap remains. Caption: *"Even with the right functional form, we miss U. The curve's shape is right. Its height is wrong."*

**Transition to Stage 6.** Left margin grows a thin "bias" strip that will activate in Stage 6. The green (log) curve stays fit; residuals dim to background.

---

## Stage 6 — The ghost in the residuals (the climax)

**Pedagogical goal:** Residuals aren't white noise — they are U in disguise. Confounding is visible in the diagnostic. This is the emotional peak of the playground.

**Animation storyboard. (Spend 30% of polish budget here.)**
- `t=0` — every residual stick **re-illuminates**, this time coloured by that point's hidden U: high-U → amber, low-U → teal. Left-to-right staggered **bloom wave**, 1200ms.
- `t=1.5s` — the **veil over the U inset widget** (top-left, from Stage 1) lifts and slides off. 200 small avatars appear at their U positions, each matching a residual stick's colour. Unmistakable visual rhyme.
- `t=3.0s` — **sticks fly out** into a small companion chart below (mini-axis: x = U, y = residual). Clear positive correlation.
- `t=5.0s` — violet trend line draws through the companion chart. Slope ≈ 2. Annotation: *"slope ≈ 2 — the 2·U coefficient we couldn't see."*
- `t=6.5s` — the violet truth ribbon in the main chart tilts to show: had we observed U, we could have shifted the green curve up for Anna and down for Ben to match truth exactly.

**Narrative text.**
> Here's something strange. Every semester we run, Anna sits above the line. Every semester, Ben sits below. If the residuals were really just noise, they'd flip sign half the time.
>
> They don't. Something is **systematically** lifting Anna and sinking Ben — and it's the thing we named at the very start. U.
>
> Flip the switch. Watch what colour the residuals actually are.
>
> *The noise wasn't noise. It was someone we weren't looking at.*
>
> This is what a **confounder** does. It shapes the inputs. It shapes the outputs. And when we leave it out of our model, our model happily blames the inputs for what the confounder did. Anna's "extra" points don't belong to her hours — they belong to U, which also made her hours higher. OLS cannot tell the two apart.

**Interactive handles.**
- **Toggle "Reveal U"** — physical-flip switch, 300ms. ON = Stage 6 state (U coloured, companion chart visible). OFF = Stage 5 state.
- **Bidirectional hover-link** — hover a residual stick → matching avatar's halo triples brightness in the U inset; reverse also works. **This is the central pedagogical interaction of the whole playground.**

**Transition to Stage 7.** Companion chart stays. Main scatter dims. A new right-hand panel slides in introducing X₃.

---

## Stage 7 — The seductive shortcut

**Pedagogical goal:** Adding a highly-correlated variable can destroy your model if that variable is caused by Y. Post-treatment / collider bias, made visceral.

**Animation storyboard.**
- Main (X₁, Y) scatter shrinks to 30% width left; new (X₃, Y) scatter at 70% right.
- `t=0` — `X₃ = 0.9·Y + η₃` types in. The `0.9·Y` term pulses a warning desaturated-red (`#b5654a`) as it lands.
- `t=1.0s` — right pane fills with 200 points in tight diagonal (r² ≈ 0.95).
- `t=2.5s` — green OLS line snaps into near-perfect fit on the right.
- `t=3.5s` — inset coefficient table animates: `β̂_X₃ ≈ 1.1` glows green while `β̂_X₁`, `β̂_X₂` **collapse to grey near zero**.
- `t=5.5s` — violet truth curve in the left pane ghosts to 0.1 opacity — "your model forgot why."
- `t=7.0s` — **counterfactual drag**: an anonymous ghost avatar is dragged along X₁; because X₃ is clamped (post-outcome, it doesn't update with X₁), predicted Y barely moves. Predictive failure visible in real time.

**Narrative text.**
> Imagine a magic new feature. After each exam, you ask every student: *"How do you think you did?"* Call their answer **X₃**. It correlates beautifully with the actual score. Should you put it in your model?
>
> Your instincts are about to betray you.
>
> Look at that R². Near-perfect. You could publish this. You could sell this. You would be lying.
>
> X₃ isn't a *cause* of the exam score. X₃ is a **consequence** of it. Students who did well feel like they did well. You're not predicting the score — you're predicting the score using a slightly noisier copy of the score itself.
>
> When you include X₃, it steals the credit from every honest predictor. Hours studied? "No longer matters." The model puts all its weight on X₃, because X₃ is Y in a costume. If a professor used this model to advise future students — *"don't worry about hours, just feel confident!"* — the advice would be backwards. **You don't score well because you feel confident. You feel confident because you scored well.**

**Interactive handles.**
- Toggle **"Include X₃ in the model"** — flipping on triggers the whole sequence; off reverses.
- **"Intervene on X₁" drag** — the student drags a ghost avatar along X₁; the predicted-Y trace follows with or without X₃.

**Transition to Stage 8.** All panes dim to a title card that reads *"The playground is open."*

---

## Stage 8 — Anna and Ben, revisited (and the sandbox)

**Pedagogical goal:** Consolidation. Return to the opening question — *why 72 vs 58?* — with all the vocabulary. Then hand the student every knob.

**Animation storyboard.**
- `t=0` — all charts from Stages 1–7 tile into a responsive grid (CSS grid auto-flow, 1500ms stagger).
- `t=1.5s` — Anna's and Ben's avatars migrate across the grid and dock in a summary panel showing their full causal trace: U → X₁ (Anna's 2 hours are "denser"), U → X₂, U → Y directly, plus ε.
- `t=3.0s` — a subtle pulsing highlight travels across the sliders once (a "try me" hint), then stops.

**Narrative text.**
> Let's return to where we started.
>
> Anna: 2 hours, 10 lectures, score 72. Ben: 2 hours, 10 lectures, score 58.
>
> You now know why.
>
> Anna's U was high. That same discipline made her 2 hours denser than Ben's 2 hours, made her lectures more attentive, and gave her a direct boost on exam day beyond anything we could measure. The 14-point gap wasn't mysterious. It was U, doing what U always does — shaping inputs, shaping outputs, staying invisible.
>
> A regression on (X₁, X₂) alone would call this gap noise. A regression including X₃ would "explain" it by cheating. Neither tells you the truth: **the most important variable in this story was the one we never got to measure.**
>
> That's the job, from here on out. Not just to fit lines. To know which lines are honest.
>
> Welcome to the rest of the course. Play.

**Interactive handles (all live simultaneously).**
- Every slider/toggle from Stages 1–7.
- **Scenario presets row**: "Ideal researcher" (U observed, log feature, no X₃), "Naive analyst" (linear X₁, no log, X₃ included), "You, yesterday" (random defaults). Each transitions all parameters over 1500ms.
- **Timeline scrubber** replays the full Stage 1 → 7 arc in 60s.

**Transition.** None — this is the end state.

---

## Persistent elements (never redrawn, only re-styled)

- **U inset widget** — top-left, from Stage 1 onward. Veiled in Stages 1–5, unveiled in Stage 6, stays unveiled afterward.
- **Anna and Ben avatars** — all stages. Halo brightness encodes U.
- **Formula tracker** — top bar, KaTeX. Stage 2 adds X₁'s equation, Stage 3 stacks X₂'s, Stage 4 stacks Y's, Stage 7 stacks X₃'s. New lines: 400ms fade + 4px upward drift. Terms colorize in place as their role is revealed (e.g., `2·U` starts black and pulses violet in Stage 6).
- **Violet true curve** — Stages 4–8, opacity-modulated.
- **Green OLS fit** — Stages 5–8, shape-morphs with feature toggles.

## Palette (locked)

| Role | Hex |
|---|---|
| Background | `#fbf8f3` |
| Primary ink | `#2a2a2a` |
| Anna / high-U | `#d4722c` (amber) |
| Ben / low-U | `#3c8dbc` (teal) |
| Noise | `#9aa0a6` (slate grey) |
| TRUE structural signal | `#7b2cbf` (deep violet) |
| Estimated / learned | `#2d8659` (confident green) |
| Warning (post-treatment) | `#b5654a` (desaturated red) |

## Typography

- Headlines: `Fraunces` (serif).
- Body: `Inter`.
- Math: KaTeX.
- All formulas appear with 400ms fade + 4px upward drift.

## Easing defaults

- Parameter changes: `d3.easeCubicInOut`.
- Arrivals: `d3.easeElasticOut.amplitude(1).period(0.4)`.
- Fades: `d3.easeQuadOut`.
- Stage transitions: 900ms; scroll position locked during transition.

---

## Tech implementation checklist

Build in this order:

### 1. Page scaffold (~80 lines)
- `<!doctype html>`, KaTeX + D3 CDN, import map.
- Grid layout: top bar (60px, persistent — formula tracker + U inset widget), main area split into sticky right viz pane (~55% viewport width) and scrolling left text column (~45%).
- Each stage = `<section data-stage="N">` in the left column. IntersectionObserver fires stage entry/exit.
- CSS variables for the palette (`--c-truth`, `--c-est`, `--c-anna`, etc.).
- `prefers-reduced-motion` media query disabling translations (fades only), jitter (instant), sparkler (static).

### 2. Shared state machine (~60 lines)
- Single module `state.js` exporting a reactive store:
  ```js
  { activeStage: 1, params: {sigmaEps, coefU_X1, coefU_X2, showUArrow, useLog, includeX3, noiseScale, ...}, sample: [...] }
  ```
- Subscribers: each stage module registers render + teardown callbacks.
- IntersectionObserver → `setActiveStage(n)` → runs teardown of old stage, entry transition, and entry of new stage.
- Shared RNG (seedable) so "Resample" is reproducible within a session.

### 3. Shared modules to extend / consume
- `shared/dgp.js` — extend to compute `(U, X₁, X₂, Y, X₃, ε)` per the spec's coefficients. Seedable.
- `shared/regression.js` — OLS with selectable feature set (X₁ raw, log X₁, X₂, X₃). Returns coefficients + residuals.
- `shared/plot.js` — axis helpers, canvas point-cloud renderer, SVG overlay layer.
- `shared/table.js` — coefficient table with glow/fade animation hooks.

### 4. Persistent top bar (~100 lines)
- **Formula tracker** — stacked KaTeX lines; each term is a `<span>` with a class controlling colour; state subscribers toggle classes.
- **U inset widget** — small SVG (120×80px). Renders vertical U axis, Anna+Ben avatars at their U positions, 200 anonymous avatars once spawned, veil `<filter>` toggled by stage. Bidirectional hover in Stage 6 emits events to main-pane residual sticks (pub/sub over the state store).

### 5. Anna & Ben avatar component (~60 lines)
- Reusable SVG snippet (24px default, 60px in Stage 1). Props: `{x, y, scale, u, highlighted}`.
- Halo rendered as `<filter id="glow-anna">` / `<filter id="glow-ben">` with std-deviation driven by `|u|`.
- Bobbing animation via `d3.timer` (disabled by reduced-motion).

### 6. Stages as modules (~100–150 lines each, 8 total)
Each file `stages/stage{1..8}.js` exports:
```js
{ id, enter(prevState, done), exit(nextState, done), render(state), teardown() }
```
- `enter` plays the entry animation (choreography above), calls `done()` when ready.
- `render` is idempotent w.r.t. state params (re-renders point positions, fit lines, sticks, etc.).
- `exit` plays the transition morph described in each stage's "Transition to N+1" section.

### 7. Transitions (~80 lines)
- A small `transition.js` utility schedules the coordinated motion across the top bar, main viz pane, and text column.
- Key morphs to implement:
  - **Stage 1 → 2**: U axis rotates 90° CCW; bell curve flattens into horizontal X₁ axis.
  - **Stage 2 → 3**: X₁ axis drops, Y axis grows, avatars climb.
  - **Stage 3 → 4**: CSS grid `1fr 0fr → 1fr 1fr`, firefly migration primed.
  - **Stage 4 → 5**: CSS grid `1fr 1fr → 0fr 1fr`.
  - **Stage 5 → 6**: bias strip grows at left margin.
  - **Stage 6 → 7**: X₃ panel slides in from right.
  - **Stage 7 → 8**: all panes dim to title card, then tile into grid.

### 8. Interactive handles
- Sliders: `<input type="range">` styled, wired to state. Throttle cloud redraws to `d3.timer` 60fps during drag; full recompute on `input:end`.
- Toggles: custom `<button role="switch">` with 300ms flip.
- Draggable OLS endpoints (Stage 5): `d3.drag()` on line handles; live SSR readout; spring-back on end.
- Counterfactual drag (Stage 7): ghost avatar follows cursor along X₁; predicted-Y trace re-computes per toggle state.

### 9. Performance discipline
- 200 points rendered to `<canvas>`; Anna, Ben, axes, lines, sticks on `<svg>` overlay.
- During slider drag: pause ribbon breathing, throttle heteroscedasticity recompute.
- Cache true-curve path string; recompute only on slider release.
- No WebGL needed.

### 10. Accessibility
- Labels on every slider/toggle (not colour alone).
- `aria-live="polite"` on the formula tracker for screen readers.
- Keyboard nav: Tab cycles controls; arrows adjust sliders; Space toggles switches.
- `prefers-reduced-motion` honoured throughout.

### 11. Deploy
- Push to `main`; existing GitHub Pages workflow auto-deploys to `/playground/dgp-intro.html`.
- Smoke test: load page cold, scroll once top-to-bottom, verify no console errors and all 8 stage transitions complete.

---

**Signature moment the implementer must nail:** Stage 6, `t=0.0–1.5s` — the left-to-right bloom wave turning grey residual sticks into amber/teal in sync with the U veil lifting. Spend 30% of polish budget there. This is the emotional payoff the whole arc exists to deliver.
