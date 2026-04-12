# Animation Storyboard: DGP Intro Playground

**File target:** `/site/playground/dgp-intro.html`
**Director's vibe:** Pixar short meets Explorable Explanation. The math is Woody; the motion is the charm that makes you love Woody. Every parameter, every noise draw, every arrow should feel *alive* — never static, never instantaneous, never cut.

**Core visual language (locked in before Stage 1):**
- **Palette.** Background: warm off-white `#fbf8f3`. Primary ink: `#2a2a2a`. Anna's accent: `#d4722c` (warm amber, "disciplined sunrise"). Ben's accent: `#3c8dbc` (cool teal, "undisciplined tide"). Noise/error: `#9aa0a6` (slate grey). True structural signal: `#7b2cbf` (deep violet — the "truth" color, reserved for the generating process). Estimated/learned quantities: `#2d8659` (confident green).
- **Typography.** Headlines `Fraunces` (serif, literary). Body `Inter`. Math via KaTeX. Formulas always appear with a 400ms fade-in + 4px upward drift (`translateY(4px) → 0`), never pop.
- **Easing defaults.** `d3.easeCubicInOut` for parameter changes. `d3.easeElasticOut.amplitude(1).period(0.4)` for "something new arrives." `d3.easeQuadOut` for fades.
- **Anna & Ben.** Not dots. **Tiny SVG avatars** — 24px circles with a single-line face (Anna: slight upturn smile, small glasses glyph; Ben: neutral line mouth, hoodie hood arc). They live at the top of the stage as **persistent mascots** from Stage 1 onward, with a thin horizontal "stage" line beneath them. When a variable gets defined, their avatar slides to the relevant coordinate — so the student tracks *the same two humans* across every chart. Hover = name tooltip. Their `U` values are **encoded as a subtle halo** (0.85 → bright 4px amber glow; 0.15 → dim 1px teal glow).
- **The TRUE regression surface.** Drawn ONCE at the reveal moment in Stage 6, then persists as a translucent violet ribbon across all subsequent stages (like a ghost that haunts the playground). It never gets redrawn — it just gets *uncovered* by progressively lifting veils.
- **Stage transitions.** Never hard cuts. The outgoing stage's key visual *morphs* into the incoming stage's opening shot via `d3.interpolateObject` on shared attributes (position, opacity, color). Typical transition duration: 900ms. The scroll position is locked during transitions.

---

## Stage 1 — "Meet Anna and Ben" (the hidden variable U)

**Pedagogical beat:** There is something unobservable that matters. We're going to personify it before we hide it.

**Opening shot.**
```
┌─────────────────────────────────────────────────┐
│                                                 │
│         Anna                  Ben               │
│          ◉                     ◉                │
│        (amber)              (teal)              │
│                                                 │
│   "self-discipline"   "self-discipline"         │
│         U = ?               U = ?               │
│                                                 │
└─────────────────────────────────────────────────┘
```
Two avatars centered, big (60px), floating with a slow 3s sine-wave bob (`translateY(0 → -3px → 0)`, staggered by 1.5s so they bob out of phase — feels *alive*, not mechanical).

**Motion choreography.**
- `t=0.0s` — empty canvas, warm background only.
- `t=0.4s` — Anna's avatar fades in at left, bobs once.
- `t=0.8s` — Ben's avatar fades in at right, bobs once.
- `t=1.4s` — names drift up from below each avatar (serif, 18px).
- `t=2.0s` — a faint vertical axis draws itself down the middle, labeled "self-discipline U" at the top, "−2" at bottom, "+2" at top. Axis opacity ramps 0 → 0.3 over 600ms.
- `t=3.0s` — Anna's avatar *glides* up the axis to y-position = 0.85σ (with her amber halo brightening as she rises); Ben glides down to y = −0.85σ (his teal halo dims). Ease: `easeCubicInOut`, 1200ms.
- `t=4.5s` — a gaussian bell curve (density of N(0,1)) fades in *behind* the axis as a translucent violet ridge, with Anna and Ben sitting on its flank at their z-scores. This is the first appearance of the "truth color."
- `t=5.5s` — caption types in below: *"U is who they really are — and we will never see it directly."*
- `t=6.0s` — a **veil** drops: a grey-fog gradient (`<filter>` with `feGaussianBlur stdDeviation=8`) slides down from above and covers both avatars to ~70% opacity. The halos are still faintly visible through it. Caption updates: *"From now on, U is hidden. But watch what it does."*

**Visual metaphors.**
- **Bobbing avatars** = aliveness, personhood, not-just-data.
- **Bell curve behind axis** = the population they were sampled from.
- **Grey veil** = the hiddenness of U. This veil is a recurring motif; it reappears (thicker, thinner) in every later stage where U matters.

**Interactive handle.**
A single slider at the bottom: **"Draw new people."** Dragging it re-samples 8 extra anonymous avatars (smaller, 16px, no names, no halos visible through the veil) that slide into random U positions along the axis. This lets the student feel that Anna and Ben are just two draws from a population. Slider uses `d3.drag()`; avatars animate with staggered 80ms delays.

**"Aha" beat.** `t=6.0s`, when the veil drops. Visually: the vivid amber and teal halos *fight through* the grey fog but lose clarity. Emotional read: "Oh — I can feel that U is there, but I can't measure it."

**Transition to Stage 2.** The veil stays. The axis rotates 90° counterclockwise (ease 1000ms) to become horizontal, the bell curve flattens into the new x-axis of Stage 2, and Anna & Ben slide to their X₁ (hours studied) positions — *because* U pushed them there. This rotation is the visual thesis statement of the whole playground: **U was vertical and hidden; its consequences are horizontal and visible.**

---

## Stage 2 — "What U does to study hours" (X₁ = 2 + 0.5U + η₁)

**Pedagogical beat:** Hidden U causes visible behavior.

**Opening shot (post-transition).**
```
┌─────────────────────────────────────────────────┐
│  [veiled U axis, now tiny, top-left corner]     │
│                                                 │
│     Anna ◉─────────────▶                        │
│                   Ben ◉──────▶                  │
│                                                 │
│  ├───┼───┼───┼───┼───┼───┼───┼──▶               │
│  0   1   2   3   4   5   6   7  hours studied   │
└─────────────────────────────────────────────────┘
```
U axis shrinks to a small "inset widget" top-left (still veiled, still bobbing — **persistent reminder**). Main canvas is now the X₁ axis horizontally.

**Motion choreography.**
- `t=0.0s` — avatars are at x=0 (leftmost), both.
- `t=0.5s` — equation `X₁ = 2 + 0.5·U + η₁` types in at top-right, KaTeX, 400ms per term (each term has its own fade-in). The `2` lands first (constant); then `+ 0.5·U` glows violet briefly (it's from the truth-colored hidden source); then `+ η₁` shimmers grey (noise).
- `t=2.5s` — a **violet arrow** shoots from the inset U widget horizontally into the main canvas, and both avatars *slide right* along the axis: Anna to x = 2 + 0.5·0.85 = 2.425, Ben to x = 2 + 0.5·(−0.85) = 1.575. Motion: `easeCubicOut`, 900ms. The arrow fades out at 1200ms.
- `t=4.0s` — noise term activates: a grey **jitter shake** is applied to each avatar (small `η₁ ~ N(0, 0.3)` perturbations, re-sampled every 600ms, avatar translates with spring-damped `easeElasticOut`). This runs for 3 seconds. The student sees Anna wobble around 2.4 and Ben wobble around 1.6.
- `t=7.0s` — jitter freezes. A faint vertical dotted line at each avatar's current x marks their final X₁.

**Visual metaphors.**
- **Violet arrow** = causal push from U. This arrow convention recurs for every variable U touches.
- **Grey jitter** = noise η. The shake is *visibly distinguishable* from the violet push because it's fast, small, and achromatic.
- **Inset U widget** = "don't forget, the cause is still hiding up there."

**Interactive handle.**
A **"resample η"** button. Each click re-runs the jitter animation for 1.5s. A **toggle** labeled "Show U's push": when off, the violet arrow and U-dependent offset vanish, and Anna/Ben collapse to x=2 with jitter. This lets the student *feel* how much of the spread is U vs η.

**"Aha" beat.** The first click of "Show U's push" OFF → ON. The avatars leap apart (Anna right, Ben left) with a 900ms elastic ease. Caption pulses: *"That gap? That's U."*

**Transition to Stage 3.** The X₁ axis slides down to become the *bottom* axis of a 2D scatter plot; a new Y-axis grows upward from the origin labeled "X₂ lectures attended." The avatars stay pinned at their X₁ values and now slide vertically to their X₂ values.

---

## Stage 3 — "Two windows onto U" (adding X₂ = 10 + 0.3U + η₂)

**Pedagogical beat:** Multiple observables all whisper about the same hidden U.

**Opening shot.**
A 2D scatter canvas. X₁ horizontal, X₂ vertical. Anna and Ben are the only two points. The U inset widget is still top-left.

**Motion choreography.**
- `t=0.0s` — Y-axis finishes drawing.
- `t=0.8s` — second equation `X₂ = 10 + 0.3·U + η₂` types in below the first.
- `t=1.5s` — violet arrow from U widget now forks: one horizontal (to X₁), one vertical (to X₂). Anna slides up to y ≈ 10.25, Ben down to y ≈ 9.75.
- `t=3.0s` — grey jitter on both axes simultaneously for Anna and Ben.
- `t=4.5s` — **200 anonymous draws** stream in as small grey dots (`r=2`, `opacity=0.5`) from a "fountain" at the origin, each arcing via `d3.interpolate` with staggered 15ms delays. They settle into a diagonally-elongated cloud.
- `t=7.5s` — a **thin violet line** (the population regression of X₂ on X₁) fades in through the cloud at 30% opacity. Annotation: *"X₁ and X₂ are correlated — through U."*

**Visual metaphors.**
- **Forking violet arrow** = one cause, two effects.
- **Diagonal cloud** = correlation as visual tilt.
- **Fountain spawn** = sampling, the stochastic engine running.

**Interactive handle.**
- **Slider: "Strength of U's fingerprint"** — scales the 0.5 and 0.3 coefficients together from 0 to 2. At 0, the cloud becomes a circular blob (no correlation); at 2, it becomes a near-line. The cloud re-animates smoothly via D3 data-join with 400ms transitions. Anna and Ben's halos pulse during the drag.
- **Button: "Replay the fountain"** — re-samples all 200 points.

**"Aha" beat.** Dragging the slider from 2 → 0 and watching a tilted correlated cloud *collapse into a round pancake*. Caption that appears only when the slider hits 0: *"No U, no correlation. U is the whole story."*

**Transition to Stage 4.** The cloud dims to 15% opacity. A new vertical axis grows on the RIGHT side of the canvas, labeled "Y — exam score." The canvas splits: left pane keeps the (X₁, X₂) cloud; right pane is a new scatter of (X₁, Y) being born. Transition is a CSS `grid-template-columns` animation from `1fr 0fr` to `1fr 1fr` over 1200ms.

---

## Stage 4 — "The outcome" (Y = 50 + 8 log X₁ + 3 X₂ + 2U + ε)

**Pedagogical beat:** The outcome depends on observables AND on U directly AND with heteroscedastic noise. The full generative truth arrives.

**Opening shot.** Split screen: left (X₁, X₂) cloud dimmed; right empty (X₁, Y) panel waiting.

**Motion choreography.**
- `t=0.0s` — equation `Y = 50 + 8·log(X₁) + 3·X₂ + 2·U + ε` types in at top, term by term, 500ms each. Each term's color-codes as it lands: `50` black (constant), `8·log(X₁)` green (observable structural), `3·X₂` green, `2·U` violet (hidden structural), `ε` grey (noise).
- `t=3.0s` — for each of the 200 cloud points on the left, a **ghost trail** (a 1px line, 30% opacity) arcs from its (X₁, X₂) position on the left pane to its computed Y on the right pane. Trails draw with staggered 10ms delays, each taking 400ms. It looks like a migration of fireflies across the canvas divide.
- `t=7.5s` — trails fade (1000ms), leaving a new cloud on the right: (X₁, Y). Anna and Ben's points land last, with a small bounce (elastic ease, 600ms).
- `t=9.0s` — the **true regression curve** (8·log(X₁) + 3·E[X₂|X₁] + 2·E[U|X₁] as a function of X₁) draws itself in violet from left to right, 1500ms, with a traveling light-dot at the draw head (like a sparkler). This is the **first appearance of TRUTH as a curve**.
- `t=11.0s` — **heteroscedastic noise visualization**: a violet ribbon expands vertically around the true curve, width ∝ `0.5·|X₁|`. The ribbon breathes — a slow 4s opacity oscillation (0.15 ↔ 0.25) conveying "this width is the noise scale."

**Visual metaphors.**
- **Firefly migration** = deterministic map from inputs to outcome.
- **Sparkler draw** = the truth being revealed, not assumed.
- **Breathing ribbon** = heteroscedasticity as a *living* width, not a static band.

**Interactive handle.**
- **Slider: "noise scale"** (multiplier on the 0.5 in ε's std). 0 → ribbon collapses to the line; 2 → ribbon balloons. Points re-jitter on the fly.
- **Toggle: "Include 2·U term"** — when off, the violet curve drops (since E[U] = 0 conditional effects vanish) and Anna/Ben collapse toward the curve. This is a mini-preview of what happens if U were controlled for.
- **Scrubber: "time"** — drag left-right to replay the firefly migration at any speed.

**"Aha" beat.** `t=9.0s`, when the sparkler draws the true curve. The student has seen points first, curve second — this matters. The curve is an *explanation* for the cloud, not a prior assumption.

**Transition to Stage 5.** The left pane (X₁, X₂) cloud fades entirely. Right pane expands to full width (CSS grid 1fr 0fr). The violet true curve stays. Anna and Ben remain as the only highlighted points.

---

## Stage 5 — "The estimator arrives" (OLS fits the visible data)

**Pedagogical beat:** We can only see what we see. OLS draws a green line through the cloud. How close is it to the violet truth?

**Opening shot.** Full-width (X₁, Y) scatter, true violet curve dim (opacity 0.3), 200 grey points, Anna + Ben highlighted.

**Motion choreography.**
- `t=0.0s` — a **green candidate line** drops in from above with high slope, wiggling, labeled "β₀ + β₁·X₁". The student immediately sees it's a wrong fit.
- `t=1.5s` — **residual sticks** (vertical grey segments) appear from each point to the green line. Each stick has length = |residual|, animates in with a 200ms draw.
- `t=3.0s` — residual sticks *pull* on the green line like springs. The line rotates/translates via a 2-second `easeCubicInOut` animation toward the OLS optimum, sticks shortening as it goes. This is the **OLS-as-spring-relaxation metaphor**.
- `t=5.5s` — line settles at β̂ₒₗₛ. Residual sticks shrink to their minimal sum-of-squares configuration and fade to 10% opacity.
- `t=6.5s` — the estimated line's color locks to confident green `#2d8659`. True violet curve brightens back to 0.7 opacity *underneath* it. The student sees both — green straight line, violet curved truth — with a visible gap, especially at low and high X₁ (because truth is log-shaped).

**Visual metaphors.**
- **Springs** = least squares as physical equilibrium.
- **Green vs violet** = estimate vs truth, side by side, persistent.
- **Gap at extremes** = model misspecification, silently displayed.

**Interactive handle.**
- **Draggable line endpoints** — the student can grab either end of the green line and drag it away from OLS. A live readout shows SSR increasing. Release → line springs back to OLS (elastic ease). This viscerally teaches "OLS is the minimum."
- **Button: "Resample the data"** — new 200 points, new OLS refit with 800ms transition. Student sees the green line *wobble* across resamples (sampling variability made visceral).
- **Toggle: "Use log(X₁) as feature"** — when ON, the green line becomes a green curve that aligns almost perfectly with the violet truth (except for the 2·U bias). The gap shrinks dramatically.

**"Aha" beat.** Toggling "Use log(X₁)" ON for the first time. The green line *warps* into a curve via 1200ms `d3.interpolate` on the y-values, and it *nests into* the violet truth. But — and this is key — a residual vertical offset remains at every point. That offset is the hidden 2·U. Caption: *"Even with the right functional form, we miss U. The curve's shape is right. Its height is wrong."*

**Transition to Stage 6.** The left margin of the canvas grows a new vertical strip — the "bias" meter — which will animate in Stage 6.

---

## Stage 6 — "The ghost in the residuals" (U as confounder)

**Pedagogical beat:** The residuals are not white noise — they're secretly painted by U.

**Opening shot.** Scatter with green OLS curve and violet truth. Residual sticks faint in background.

**Motion choreography.**
- `t=0.0s` — every point's **residual stick re-illuminates**, this time colored by the point's (hidden) U value: high-U points get amber sticks, low-U points get teal sticks. Coloring animates in over 1000ms.
- `t=1.5s` — the **veil over the U inset widget** (top-left, from Stage 1) *lifts* — it slides up and off, revealing the 200 small avatars at their U positions, each matching a residual stick's color. The visual rhyme is unmistakable: the colors on the sticks are the colors on the U axis.
- `t=3.0s` — a subtle **sort animation**: the residual sticks reorder themselves along a new mini-axis at the bottom (x = U, y = residual), flying out of the scatter and into a small companion chart below. This chart shows the **residuals vs U** — a clear positive correlation (slope ≈ 2).
- `t=5.0s` — violet trend line draws itself through the residuals-vs-U companion chart. Annotation lands: *"slope ≈ 2 — the 2·U coefficient we couldn't see."*
- `t=6.5s` — the violet truth ribbon in the main chart *tilts* to show confidence: if we had observed U, we could have shifted the green curve up for Anna, down for Ben, and matched the violet truth exactly.

**Visual metaphors.**
- **Color-matching (amber sticks ↔ amber halos)** = the residuals literally *are* U in disguise.
- **Sticks flying out into companion chart** = diagnostic-plot-as-revelation.
- **Veil lifting** = the epistemological payoff.

**Interactive handle.**
- **Toggle: "Reveal U"** — the master switch. OFF = Stage 5 state (U hidden). ON = Stage 6 state (U colors visible, companion chart visible). The toggle is a physical-looking switch with a satisfying 300ms flip animation.
- **Hover a residual stick** — the matching avatar in the U inset widget highlights (halo triples in brightness). Reverse hover also works: hover the avatar, the stick glows. This bidirectional hover-link is the **central pedagogical interaction** of the whole playground.

**"Aha" beat.** The first time the toggle flips ON and the grey residual sticks *bloom* into amber/teal in a 1200ms staggered wave (left-to-right across the X₁ axis). The student audibly goes "oh." Caption that appears on completion: *"The noise wasn't noise. It was someone we weren't looking at."*

**Transition to Stage 7 (optional).** The companion chart stays. The main scatter dims. A new panel slides in from the right introducing X₃.

---

## Stage 7 — "The seductive shortcut" (X₃ = 0.9·Y + η₃, post-treatment)

**Pedagogical beat:** Adding a highly-correlated variable can *destroy* your model if it's caused by Y.

**Opening shot.** Main (X₁, Y) scatter on left (30% width). New (X₃, Y) scatter on right (70% width).

**Motion choreography.**
- `t=0.0s` — equation `X₃ = 0.9·Y + η₃` types in. The `0.9·Y` term pulses a warning color (desaturated red `#b5654a`) when it lands — a subtle semiotic hint.
- `t=1.0s` — right pane populates with 200 points in a *tight diagonal* (r² ≈ 0.95). The cloud is almost a line.
- `t=2.5s` — a green OLS line in the right pane fits almost perfectly.
- `t=3.5s` — a **"regression with X₃ included"** fit runs in a small inset: coefficients table animates in, with `β̂_X₃` ≈ 1.1 glowing green and `β̂_X₁`, `β̂_X₂` *collapsing* toward zero with a sad grey fade.
- `t=5.5s` — the violet TRUE curve in the left pane *ghosts out to near-invisibility* (opacity 0.1), symbolizing: "your model forgot why."
- `t=7.0s` — a **counterfactual arrow** animation: the student is asked to imagine intervening on X₁ (study more hours). An animation shows an anonymous avatar being dragged right along X₁ by the mouse, but because X₃ is "clamped" (it's a post-outcome measurement, it doesn't update), the predicted Y barely moves. The student *sees* the predictive failure in real time.

**Visual metaphors.**
- **Tight diagonal cloud** = deceptive correlation.
- **Collapsing coefficients** = interpretability lost.
- **Ghosted truth curve** = causality forgotten.
- **Clamped X₃ during intervention** = the post-treatment fallacy made mechanical.

**Interactive handle.**
- **Toggle: "Include X₃ in the model"** — flipping it on triggers the whole sequence. Flipping off brings everything back.
- **"Intervene on X₁" drag** — the student drags a ghost avatar along X₁; the predicted Y trace follows with or without X₃ depending on toggle.

**"Aha" beat.** The moment the `β̂_X₁` number fades to grey near zero while the tight diagonal X₃ cloud looks so *seductively clean*. Caption: *"X₃ explains Y beautifully. And tells you nothing useful."*

**Transition to Stage 8.** All panes dim to a title card.

---

## Stage 8 — "The playground is open" (free exploration)

**Pedagogical beat:** Now you have the keys.

**Opening shot.** A dashboard with every slider and toggle from stages 1-7, all available simultaneously.

**Motion choreography.**
- `t=0.0s` — all charts from previous stages tile into a responsive grid (CSS grid auto-flow animation, 1500ms stagger).
- `t=1.5s` — a subtle pulsing highlight travels across the sliders once (a "try me" hint), then stops.

**Interactive handles (all live).**
- Every slider/toggle from Stages 1-7.
- A **"scenario presets"** row: buttons "Ideal researcher" (U observed, log feature, no X₃), "Naive analyst" (linear X₁, no log, X₃ included), "You, yesterday" (random defaults). Each triggers a 1500ms transition of all parameters to the preset.
- A **timeline scrubber** at the bottom replays the full Stage 1 → 7 narrative in 60 seconds.

**"Aha" beat.** None prescribed — the student constructs their own.

---

## Cross-stage design notes

**Persistent elements (never get redrawn, only re-styled):**
- The U inset widget (Stages 1-6).
- Anna and Ben's avatars (all stages).
- The violet true curve (Stages 4-8, opacity-modulated).
- The green OLS fit (Stages 5-8, shape-morphs with feature toggles).

**Recurring motifs:**
- **Violet = truth, green = estimate, grey = noise, amber = Anna/high-U, teal = Ben/low-U.** Rigid palette discipline.
- **Veils** for hiddenness, **sparklers** for revelation, **springs** for optimization, **fireflies** for deterministic mapping, **fountains** for sampling.

**Formula rendering (KaTeX).**
Every formula appears in a fixed top bar that accumulates: Stage 2 adds X₁'s equation, Stage 3 stacks X₂'s below it, Stage 4 stacks Y's, Stage 7 stacks X₃'s. Each new line fades in with 400ms opacity + 4px upward drift. Terms colorize in place as their role is revealed (e.g., `2·U` in Y's equation starts black and pulses violet the first time Stage 6's "Reveal U" is toggled). This gives the formula bar a **growing, living** quality — by Stage 8 it's a full DGP recipe, color-coded.

**Canvas vs SVG.**
- **SVG** for Anna/Ben avatars, formulas, axes, OLS line, true curve, residual sticks, annotations.
- **Canvas** for the 200-point cloud (faster redraws during slider drags).
- **No WebGL needed** — 200 points is well within canvas reach. Reserve WebGL for a future "posterior distribution" stage if ever added.

**Performance discipline.**
- During slider drags, disable the breathing-ribbon oscillation.
- Use `d3.timer` throttling at 60fps for jitter animations.
- Cache the true curve's path string; only recompute on slider release, not during drag.

**Accessibility.**
- Every color-coded term has a text label (amber/teal are not the sole information channel — Anna/Ben have name labels).
- Every animation respects `prefers-reduced-motion: reduce` — fades replace translations, jitter becomes instantaneous, sparklers become static.
- Keyboard nav: Tab cycles through sliders and toggles; arrow keys adjust sliders; Space toggles switches.

**The signature moment of the whole piece.**
If the student remembers only one frame, it should be **Stage 6, t=0.0-1.5s**: the moment the grey residual sticks *bloom into color* in a left-to-right wave, and the veil over U lifts in perfect sync. That's the emotional climax. Everything before it builds to it; everything after it reflects on it. The implementer should spend 30% of their polish budget on those 1.5 seconds.
