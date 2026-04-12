# Plan: Simpson's Paradox Example, Collider References, and Interactive Web App

Branch: `interactive-regression-app`

## Scope

Three related deliverables:
1. **Content addition** — Simpson's paradox example in the OVB section (quick win)
2. **Content addition** — Article references for collider bias (quick win)
3. **Main project** — Interactive regression web app (Setosa/Distill-style)

---

## Part 1: Simpson's Paradox DGP for OVB Section

### Goal
Show students a concrete scenario where including the confounder **flips the sign** of the coefficient — the most dramatic form of OVB. This makes the abstract formula $\E[\hat\beta_1^{\text{short}}] = \beta_1 + \beta_2 \delta_1$ viscerally real.

### Proposed example: "The Nursing Paradox"

**Story.** A hospital's records show that patients who receive more nursing hours per day take *longer* to recover. The administration considers reducing nursing time to "accelerate recovery." Before they act, a statistician intervenes.

**DGP:**
- $U$ = severity of admission (1 = mild, 10 = severe)
- $X$ = nursing hours per day; sicker patients get more nursing: $X = 2 + 0.8\,U + \eta$, $\eta \sim \mathcal{N}(0, 0.3)$
- $Y$ = recovery time in days; more nursing *helps* (negative true effect), but sicker patients take longer: $Y = 5 - 0.5\,X + 2\,U + \varepsilon$, $\varepsilon \sim \mathcal{N}(0, 0.5)$

**True causal effect:** $\beta_X = -0.5$ (each extra nursing hour saves half a day)

**Short regression (Y on X alone):**
$\plim\,\hat\beta^{\text{short}} = \beta_X + \beta_U \cdot \delta_1 = -0.5 + 2 \cdot \frac{\Cov(X,U)}{\Var(X)} \approx -0.5 + 2(0.97) \approx +1.45$

**Sign flipped!** The naive regression says nursing *hurts*; the true effect says it *helps*.

### Concrete 10-patient numerical example
Include a table where the reader can hand-verify:
- Aggregate slope: positive (nursing → slower recovery)
- Within-severity-group slope: negative (nursing → faster recovery)
- The OVB formula predicts the gap exactly

### Where it goes
Add as a new `numermark` box in Section 3 after the existing studying/sleeping numerical example, titled **"The Nursing Paradox: When the Sign Flips."**

### Additional note
Briefly mention Simpson's paradox and UC Berkeley admissions 1973 as the canonical real-world case, with a one-line citation.

---

## Part 2: Collider Bias Article References

### Goal
Add hyperlinks to the real articles students can click through, so the collider bias lecture becomes actionable outside class.

### Articles to cite in Section 8 (Causation)

1. **SheKnows — "Really hot guys are also really not nice, says science"** — the lecture opener. Real headline that unknowingly commits collider bias.
2. **YourTango — "25 Smokin' HOT Celebrities With Just Average-Looking Spouses"** — catalogue of Pete Davidson-style examples.
3. **Jordan Ellenberg (Slate, 2014) — "The Summer's Most Unread Book Is…"** — his Great Square dating metaphor.
4. **Griffith et al. (2020, Nature Communications) — UK Biobank collider bias paper** — COVID smoking paradox.
5. **Ellenberg's *How Not to Be Wrong*** — book reference for the Great Square of Men.

### Implementation
Add a new box after the collider discussion:
```
\begin{keyinsight}[title={Real Articles Committing Collider Bias}]
For further reading, these real articles unknowingly demonstrate the paradox...
\end{keyinsight}
```
Include `\href` links to each.

---

## Part 3: Interactive Regression Web App

### Inspiration (from research)

- **Setosa.io** — minimal aesthetic, draggable points, linked panels updating in real time. Uses D3/SVG for 2D, Three.js for 3D. Katex isn't used there but Distill uses it extensively.
- **Distill.pub** — inline interactive figures, narrative text interspersed with widgets, side-by-side comparisons. Uses custom D3 builds, Katex for formulas.
- **3blue1brown manim-style animations** — smooth transitions, color-coded variables.

### Design principles

1. **Minimal aesthetic** — white/off-white background, one accent color per variable (reuse lecture-notes palette: blue=OLS, gold=truth, red=bias, green=repair).
2. **Linked views** — changing any control updates every panel simultaneously. No "submit" buttons for exploration.
3. **Narrative scaffolding** — prose on the left, viz on the right (Distill style), or top-bottom stacked for mobile.
4. **Katex formulas** — the DGP is a formula, not a picture of a formula.
5. **One idea per screen** — resist the urge to cram. Let each pathology get its own canvas.

### Technical stack

| Layer | Choice | Why |
|-------|--------|-----|
| Hosting | GitHub Pages | Already configured on the repo; free; fits static-site model |
| Framework | None (vanilla JS + HTML) | Keeps load fast, no build step; Setosa's approach |
| Visualization | D3.js v7 | Industry standard, handles SVG binding to data elegantly |
| Math rendering | Katex | Much faster than MathJax, easier to style |
| Simulation | Custom JS (seedable PRNG: we already have `site/js/company_sim.js`) | Reuse existing DGP simulator |
| Styling | Plain CSS with CSS variables | No Tailwind/etc. overhead |

**Reject:** React/Vue/Svelte — adds 50KB+ framework, not needed.
**Reject:** Chart.js / Plotly — too opinionated, can't customise enough. D3 gives total control.

### User flow

1. **Landing page** — 8 cards (one per pathology) + 1 card for the "interactive DGP playground"
2. **DGP playground page** (the main new build) — see below
3. **Pathology-specific pages** — one per section, reusing shared components. Already scaffolded by the prior visualization agents; this project extends them.

### The DGP Playground — feature spec

Single page, four linked panels:

```
┌──────────────────────────┬──────────────────────────┐
│ 1. DGP Formula (Katex)    │ 3. Scatter plot         │
│   Editable parameters      │   Data points, fit line  │
│   Checkboxes: include X₂? │   Updated live           │
│   Include U?               │                          │
├──────────────────────────┼──────────────────────────┤
│ 2. Controls                │ 4. Regression output     │
│   n slider                 │   β̂, SE, t, p-values    │
│   Seed input               │   Table updates live     │
│   Regenerate button        │   Narrative: "Notice..."  │
└──────────────────────────┴──────────────────────────┘
```

### Topic integration ("What if I include U?")

Under the main panels, a row of buttons — one per pathology:
- **OVB** → click: fit model with/without U, show before/after coefficients.
- **Heteroscedasticity** → click: overlay robust vs classical CIs.
- **Collider** → click: add X₃ as control, watch β̂ worsen.
- **Specification** → click: swap linear for log model, compare fit.
- **Overfitting** → click: slide polynomial degree, watch train/test R² cross.
- **Causation / IV** → click: reveal the roommate instrument, compare OLS vs IV.
- **Significance** → click: inflate n, watch p-value plummet while coefficient stays flat.
- **RDD** → click: rearrange to scholarship-cutoff scenario.

Each button reveals a narrative paragraph below the panels explaining what just happened — Katex formulas inline.

### Simpson's paradox specific feature

When the OVB button is clicked, show an animated "coefficient gauge":
- At start: β̂ = +1.45 (naive, wrong sign)
- User drags a slider: "How much of U is controlled for (0 → 100%)"
- As slider moves: coefficient smoothly transitions from +1.45 to -0.5
- At 100%: the gauge flips colour from red to green; narrative: "Simpson's paradox resolved."

### Implementation phases

**Phase 1 — Foundation (week 1)**
- [ ] Choose final folder structure (extend existing `site/` or new `app/`?)
- [ ] Set up minimal HTML shell with Katex + D3 from CDN
- [ ] Port existing `company_sim.js` to this page; verify reproducibility
- [ ] Build the four-panel layout (static, non-interactive first)
- [ ] Wire the DGP formula to Katex rendering
- [ ] Verify GitHub Pages deployment works for the new page

**Phase 2 — Core interactivity (week 2)**
- [ ] Control panel: n slider, seed input, regenerate button
- [ ] Live data regeneration on any parameter change
- [ ] Scatter plot with fitted line
- [ ] Regression output table with coefficients/SE/t/p
- [ ] Checkbox toggles: include each variable in the fit

**Phase 3 — Topic buttons (week 3)**
- [ ] 8 pathology buttons with state management
- [ ] OVB view: side-by-side with/without U
- [ ] Simpson's paradox animated gauge
- [ ] Heteroscedasticity: robust vs classical CI overlay
- [ ] Collider: X₃ toggle with warning highlight
- [ ] Specification: linear vs log toggle
- [ ] Overfitting: polynomial degree slider + train/test R² plot
- [ ] IV: instrument reveal animation
- [ ] Significance: n-slider with p-value thermometer
- [ ] RDD: cutoff scatter

**Phase 4 — Polish (week 4)**
- [ ] Smooth transitions between states (D3 animations)
- [ ] Responsive layout (mobile: panels stack; desktop: 2×2 grid)
- [ ] Narrative prose for each topic — connect back to lecture notes
- [ ] Link from each interactive back to the relevant lecture note section (PDF anchor)
- [ ] Final design pass: typography, spacing, colour consistency
- [ ] Accessibility: keyboard navigation, ARIA labels, colour-blind safe palette

### Out of scope (for now)

- 3D visualisations (Three.js) — could add later for e.g. the FWL theorem in 3D
- User accounts / saved states — static site, no backend
- Social sharing of custom DGP configurations — nice-to-have, later

---

## Suggested execution order

1. **Today**: Implement Simpson's paradox numerical example + collider article references (~1–2 hours). Test compile, commit.
2. **Week 1**: Web app Phase 1 — scaffolding and layout.
3. **Week 2**: Web app Phase 2 — core interactivity.
4. **Weeks 3–4**: Topic buttons and polish.
5. **Deploy and iterate** based on student feedback.

---

## Open questions for you

1. **Folder structure**: extend the existing `site/` directory (which has the 8 pathology pages already built by prior agents) or create a new top-level `app/`?
2. **Scenario for the web app**: keep the studying/exam theme from the lecture notes, OR use the Nursing Paradox to showcase sign flipping as the main demo?
3. **Scope discipline**: if time is tight, is the DGP playground alone enough, or do we need all 8 topic buttons working on day one?
