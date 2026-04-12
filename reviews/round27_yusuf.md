# Round 27 Review — Yusuf (time-poor MechE, 3rd year)

**Context:** I have 30 min/day. I commute between a logistics shift and ETH. I don't have time for cute. I skimmed this in 40 min, then went deep on the sections I thought would show up on the exam.

Verdict up front: **value/minute = 7/10**. Better than most ETH scripts I've read. But ~20 pages could go, and a few sections bury the punchline so deep I had to re-read twice. That's expensive when you only have 30 min.

---

## 1. Sections that are too long for their value

### Section 2 (Data Generating Process) — cut ~35%
Lines 256–411. The DGP gets walked through THREE times:
- The definition block (eq 2.1–2.6).
- The paragraph-by-paragraph walkthrough ("$U \sim \mathcal{N}(0,1)$: Self-discipline…" etc., lines 300–320).
- The "Numbers Behind the Story" Key Insight box (lines 324–340).

I read the equations, got it. Then you explain $U$ in prose. Then you explain $U$ AGAIN in the Key Insight ("$\beta_U = 2$: each standard deviation..."). Three identical re-explanations of the same seven parameters is brutal when I'm on a train. **Kill the Key Insight box, or kill the prose walkthrough. Not both.**

Also: the "Negative study hours" remark (line 306), the "Logarithm convention" remark (294), and the "Causal ordering" remark (342) are three remark-boxes back-to-back-to-back. The negative-study-hours one is pure throat-clearing — I'd never notice or care, and if I ran a simulation I'd figure it out in 10 seconds.

### Section 3 (OVB) — cut ~25%
Great section overall but has 3 visualizations for the same idea:
- The "Ghost in the Regression" vizspec
- The "Before and After: The OVB Reveal" Key Insight (two "slides")
- The "Sign the Bias / Dog owners" Try-It-Yourself box

Slide 1 vs Slide 2 in the Before/After box is redundant with the vizspec above it. The CNN coffee Toy Story is great signal. The dog-owner box is fine. But we don't need four separate retellings of "omitted variable makes coefficient too big."

### Section 5 (Significance) — cut ~30%
The Seat Number toy story is gold. But then:
- "Stand Up If Significant" classroom exercise (801–808) — I'm reading alone on a train. This is for the lecturer, not me. Cut from notes, keep for lecture.
- "Replication Crisis" remark with power-posing story (895–899) — entertaining but adds no exam content beyond what's in the multiple-testing proposition.
- "Keyboard That Saves 0.1 Seconds" numerical example (901–917) — this is literally the seat number example with different numbers. Redundant.

### Section 9 (Real World / Lalonde) — cut ~20%
The Cinelli-Hazlett robustness value is explained in a definition, then in a numerical example, then referenced again in the BS Detector. Fine. But the COVID smoking remark (1481–1483) is a third separate collider example after the Hot Guys Are Jerks toy story AND the movie-star-spouses toy story in Section 8. By Section 9 I already get it — colliders are everywhere. I don't need another one.

---

## 2. Padding vs signal — specific hit list

**Padding (cut ruthlessly):**

1. **"Meet the Students" (Anna and Ben), lines 242–250.** They appear here, then get re-invoked in Section 3 ("Think about what this means for Anna and Ben..."), Section 8 ("Return to Anna and Ben..."), Section 10 ("Anna-and-Ben pairs exist..."). Every invocation says the same thing: "different $U$, same $X$." The idea lands on first telling. Every subsequent Anna/Ben sentence is a narrative callback that adds zero exam value.

2. **"Coefficient tracker" headers** at the start of Sections 4, 5, 6, 7, 8, 9, 10, 11, 12. Nine tracker headers cumulatively repeating the same list of pathologies. By Section 7 I've memorized them. The tracker in Section 12 (the actual summary table) is the only one I need.

3. **"Running gags to watch for" paragraph (line 129).** Meta-commentary about the notes themselves. Cut.

4. **The Pete Davidson paragraph (1166).** Entertaining. Exam-relevant content = 0. The Brunel "hot guys" toy story already delivered the collider point.

5. **The LTCM opener in Section 7 (line 1021).** One-sentence version would work: "Overfitting cost LTCM \$4.6B." The full paragraph is padding before you get to bias-variance.

6. **"How to Read These Notes" section (116–130).** I know how to read notes. Delete.

7. **Remark: Classic RDD Applications (1581).** Angrist-Lavy and Carpenter-Dobkin trivia. Skip for exam.

**Signal (earns its place):**

- The OVB numerical example (five students, sleep/study). Crisp, verifies the formula, I could reproduce on an exam.
- The IV numerical example (roommates, lines 1334–1381). First correct coefficient moment lands because the setup is concrete.
- The polynomial table in Section 7 (training vs test $R^2$). One table does more work than two pages of prose would.
- FWL three-step procedure (Section 11) — the best explanation of "controlling for" I've seen. Every sentence earns its space.
- The Statistical BS Detector (Appendix B). Genuinely useful; I'll photograph it.

---

## 3. Sections that earn every word

- **Section 11 (FWL).** Tight. Motivation → theorem → numerical verification → what goes wrong. No padding.
- **Section 10 (RDD).** Short, punchy, the scholarship example is enough.
- **Appendix B (BS Detector).** Five questions, one page. Perfect density.
- **Appendix C (Practice Problems).** Exactly what I want: problems + answers, no fluff.

---

## 4. First + last paragraph test

| Section | Passes? | What's missing |
|---|---|---|
| 1 Intro | NO | First = Ofqual. Last = "driving question." Neither tells me the course is about 8 failure modes of OLS. |
| 2 DGP | NO | First paragraph defines "DGP." Last = pathologies list. Middle is where the actual DGP lives. Can't skip. |
| 3 OVB | YES | First sets up TA problem; last key insight gives signed bias. Good. |
| 4 Hetero | YES | CI definition up front, Drunk Darts → sandwich. Works. |
| 5 Significance | YES | Seat number opener + "with enough data, every effect is significant" closer. Good. |
| 6 Specification | PARTIAL | Opens with ruler/road; closes with log repair. Misses: the key result is $\beta^* = \arg\min E[(Y-X\beta)^2]$. Not in first or last para. |
| 7 Overfitting | YES | LTCM opener, bias-variance closer. Good. |
| 8 Causation | NO | Sprawls. First = Hot Guys study. Last = weak instruments. Too much between — endogeneity, colliders, IV, F-stat. Three sections' worth. |
| 9 Real World | YES | Lalonde intro, fragility conclusion. Works. |
| 10 RDD | YES | Short enough that the whole thing reads as one unit. |
| 11 FWL | YES | Motivation up top, bad-controls implication at bottom. Perfect. |

**Biggest failure: Section 8.** It's really 3 topics (endogeneity/colliders/IV) in one. I'd split into 8a "Bad Controls" and 8b "Instrumental Variables." As-is, if I only read first and last paragraphs I'd completely miss the IV framework.

---

## 5. Time to mastery

To ace the exam:
- First pass (skim stories + key insights + theorem statements): **3 hrs**
- Second pass (work numerical examples with pen/paper): **4 hrs**
- Practice problems + Appendix A proofs: **3 hrs**
- Memorize BS Detector + diagnostic table: **1 hr**
- Catch-up re-reads on weak spots (probably Section 8 IV and Section 9 Cinelli-Hazlett): **2 hrs**

**Total: ~13 hours.** That's 2 weekends plus weekday reading. Doable.

For context, a typical ETH script of this length takes me 20+ hours because I'm constantly googling notation and hunting for definitions. These notes have prerequisites up front, recurring example, consistent notation — that saves me real time. **This is the sharpest time advantage of these notes.**

---

## 6. Rating

**Value per minute of reading: 7/10.**

- +2 for recurring DGP (no re-setup cost each section).
- +1 for BS Detector and practice problems with answers.
- +1 for numerical examples that actually verify theorems.
- −1 for redundancy (Anna/Ben, coefficient trackers, multiple collider examples).
- −1 for Section 8 sprawl.
- −1 for too many pedagogical boxes (Toy Story + Key Insight + Numerical Example + Viz + Try-It-Yourself + Warning + Repair — the DGP section has five box types on one page; I lose track of which box matters).

A 9/10 version of these notes exists. It's this minus 15–20 pages.

---

## 7. Top 3 cuts

**Cut 1: All 9 "Coefficient tracker" headers (Sections 4–12).**
Keep only the full tracker table in Section 12/13. The per-section trackers repeat the same cumulative list and add zero information after Section 5. Estimated savings: 1 page total, but huge cognitive relief.

**Cut 2: The triple-walkthrough of the DGP in Section 2.**
Keep the equation block (def 2.1). Keep ONE of {paragraph walkthrough, Key Insight "Numbers Behind the Story"}. Not both. Saves ~1.5 pages and removes the déjà-vu feeling that kills motivation at 10pm.

**Cut 3: Section 5's "Keyboard That Saves 0.1 Seconds" numerical example + the "Stand Up If Significant" classroom exercise + the Replication Crisis remark.**
The seat number toy story and the $t \to \infty$ argument already deliver the point. These three additions are three paraphrases of "big $n$ makes trivial effects significant." Saves ~1.5 pages. Section 5 becomes one of the tightest in the notes.

---

## Closing note

These notes are good. I would not cut the story-driven structure — the Ofqual opener and the CNN coffee example are why I'll remember OVB in 5 years. But the notes *trust the stories too little*. Every punchline gets re-told in a Key Insight box, then re-hammered in a Warning box, then referenced back via Anna/Ben. One telling is enough. Let the story breathe, then move on.

If Carlos cuts 15 pages this becomes a 9/10. As-is, 7/10 is honest.
