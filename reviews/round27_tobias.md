# Round 27 Review — Tobias (3rd-year MechE, ADHD, zig-zag reader)

Okay so. I read these notes the way I read everything: I opened the PDF, scrolled the whole thing end-to-end in like 90 seconds, let my eyes snag on the colored boxes and bold words, THEN I went back. Here's what happened from that mode.

---

## 1. Zig-zag reading — does it hold together when I jump in?

**Mostly yes. Genuinely impressed.** The coefficient-tracker italic paragraph at the top of every section from Sec 4 onward is gold for a zig-zag reader. When I land cold in Section 7 (Overfitting), the first thing my eye grabs is:

> *Coefficient tracker: 10.5 (biased), wrong CI, significant-but-trivial, wrong shape. Now we try to fix the shape...*

That single line tells me where I am in the story without reading the previous 40 pages. This is the #1 thing keeping me oriented. **Do not remove it. Ever.**

### Sections where jumping in leaves me lost:

- **Section 2 (The DGP), subsection "The Exam Score DGP" (around line 282).** I landed on the big `align` block with $U, X_1, X_2, \varepsilon, Y, X_3$ and six equations. No coefficient tracker here (because the gag hasn't started). No toy story. No colored box telling me "this is the recipe that the rest of the notes will keep referencing." It's just a wall of math at the top of a subsection. When I jump here cold, I have no idea why I should care about these specific numbers (2, 0.5, 0.3, 10, 50, 8, 3, 2). A single colored box saying "These six equations are the machine that produces every student in this course — come back to them when a later section breaks" would rescue this.

- **Section 11 (FWL), "Numerical Example" (line 1647).** Totally new variables appear (exercise, sleep, mood — A/B/C/D/E people). This broke my brain for a second. We've spent 10 sections with Anna, Ben, hours-studied, self-discipline. Now suddenly person "D" does 5 hours of exercise and 8 hours of sleep? I had to scroll up twice to confirm I was still in the same document. The toy story right above (running coach + new shoes) is ALSO a new scenario. So in one section, you throw three universes at me: exam scores (still the frame), running coach, and exercise/sleep/mood. Jumping into the middle of Section 11, I genuinely wondered if I'd clicked into the wrong PDF.

- **Section 12 (Diagnostic Toolkit Summary).** I landed on the big diagnostics table (VIF, Breusch-Pagan, Durbin-Watson, Jarque-Bera) and it felt like a different textbook. No story, no Anna/Ben, no ghost. The coefficient tracker at the top helps, but then the vibe instantly goes clinical. I skimmed past it in 8 seconds.

- **Appendix A (Proofs).** Obviously. But this is fine — proofs are proofs. No complaint.

---

## 2. Running gag consistency

### "Is this a seat number?" — **Great until it isn't.**

Traced every occurrence. It appears:
- Intro para (line 129): teased
- **Section 5** (Significance): born, main event (lines 777, 799, 803, 811, 830, 898) — perfect
- Section 6 header tracker (line 930): callback ✓
- Section 7 tracker (line 1019): callback ✓ ("significant-but-trivial")
- Sections 8, 9 trackers: mentioned ✓
- Section 10 tracker: mentioned ✓
- Section 12 tracker: ✓
- Section 13 table: ✓
- Conclusion (line 1829): ✓ (one of the three closing questions)
- BS Detector (line 1951): ✓

**Where it disappears:** Section 11 (FWL) tracker does NOT include "seat number." The tracker there just lists "inflated, misshapen, memorised, destroyed, sign-flipped" — it skips the significance betrayal. As a zig-zag reader who anchors on recurring phrases, I noticed instantly. Fix: add "seat-numbered" or "trivially-significant" back into the Section 11 tracker.

Also: the gag is purely mentioned in trackers from Sec 6 onward. It never gets *re-activated* — nobody says "wait, is coefficient X a seat number?" in any of the worked examples in Sections 7–11. That's fine, but consider one more live use in Section 9 (Real World) where there's a massive $n$ and an OVB problem — perfect place to ask "is Ofqual's seat number?"

### Anna & Ben — **Introduced strong, then ghosted.**

They show up on:
- Line 246–250 (introduced, great)
- Line 522 (Section 3, OVB) ✓
- Line 1216 (Section 8, bad controls) ✓
- Line 1534 (Section 10, RDD) ✓ (briefly, "Anna-and-Ben pairs")

**That's it. Four appearances in ~2000 lines.** They completely vanish in:
- Section 4 (Heteroscedasticity) — no Anna/Ben, even though the "Drunk Darts" toy story and "Five Students" numerical example would be a natural place to say "Anna's variance looks like X, Ben's like Y."
- Section 5 (Significance) — huge missed opportunity. The seat number gag is all about $n=50{,}000$ students. Could easily say "Anna sat in seat 147, Ben in seat 12 — did that cause the 14-point gap? Of course not."
- Section 6 (Specification) — absent. The diminishing-returns log curve cries out for "Anna on the flat part, Ben on the steep part."
- Section 7 (Overfitting) — absent. The degree-15 polynomial memorising noise and then failing on new data is SO natural for "what does the overfit model predict for a new Anna vs. a new Ben?"
- Section 9 (Real World / tutoring) — absent.
- Section 11 (FWL) — absent. And this is the section that invents whole new characters (A/B/C/D/E). Why not make the numerical example *Anna and Ben and three friends*?
- Sections 12, 13, Conclusion — absent.
- BS Detector cheat sheet — absent.

This is my **biggest pain point**. The intro promises: *"Every pathology in these notes is, at its core, about what happens to Anna and Ben."* Then for 6 out of 10 pathology sections, Anna and Ben are not there. As a zig-zag reader who clings to named characters, this feels like a broken promise. I read the intro, got attached, and then the people I was attached to vanished. It bothers me more than it should.

### "Ghost" metaphor — **Consistent and strong.**

This one works great. "Ghost of self-discipline," "ghost of kale salads and morning jogs," "ghost is running the show" — this runs all the way through, shows up in the BS Detector as "Where's the ghost?", and lands in the conclusion. No complaints. More of this, please.

### "Coefficient tracker" — **Gold standard.** Already covered.

---

## 3. Visual hierarchy — how are the boxes doing?

Box counts I tallied:

| Box type | Count | Status |
|---|---|---|
| `toystory` (gold) | ~10 | Just right |
| `keyinsight` (blue) | ~13 | Overused |
| `numermark` (light blue) | ~11 | Just right |
| `vizspec` (green) | ~9 | Just right, one per section |
| `repairbox` (green) | ~7 | Good |
| `warningbox` (red) | ~9 | Good |
| raw `tcolorbox` custom | ~9 | **Problem — see below** |

### Issues I noticed:

- **`keyinsight` is overused.** In Section 8 alone there are 3 keyinsight boxes (lines 1156, 1201, 1247) plus a warningbox and a toystory. Blue box everywhere = blue box nowhere. When every "important thing" gets a Key Insight label, none of them feels important. My eye stops treating the blue box as a privileged signal.

- **Custom raw `tcolorbox` invocations are inconsistent.** The "Cold Open," "The Algorithm That Ruined 72 Hours," "Try It Yourself" (twice), "Predict Before You Peek," "Stand Up If Significant," and the four yellow boxes at the end of the BS Detector are all hand-rolled `tcolorbox` with their own titles. As a zig-zag reader: what is a "Cold Open"? What is "Try It Yourself"? Is "Predict Before You Peek" the same class as "Stand Up If Significant"? I can't tell from colors alone, because they use different colors (red, gold, gold, gold, gold). Some are identical color-wise to `toystory` boxes but have totally different functions. Define a new environment or two (`coldopen`, `tryityourself`) so these become recognizable patterns, not one-off ornaments.

- **Section headers don't have a visual cue for which sections are "failure mode" vs. "theory" vs. "redemption."** Sec 10 is called "The Redemption" — love that — but the section heading is the same blue as every other section. A small icon or color tag per section ("💀 failure," "✨ redemption," "🔧 toolkit") would help me know where I am when I jump. (No emoji in the actual document if you hate them — a colored bullet or label works fine.)

### Box type that's underused:

- **`repairbox` (green).** Only ~7 in a document about diagnosing and fixing problems. Every failure-mode section *should* end with a Repair box saying "here's what to do instead." Section 5 (Significance) has a repairbox — great. Section 6 (Specification) has one. But Sections 7 (Overfitting) and 8 (Bad Controls) end without a clear green repair. The structure I want as a zig-zag reader is: Toy Story → math → Numerical Example → Warning → **Repair** → Viz. Make that 6-box rhythm explicit.

---

## 4. Missing signposts

Places where I lost the thread:

- **Between Section 2 and Section 3.** Sec 2 ends with "Pathologies Embedded in the DGP" (line 387). Then Sec 3 starts ("Why Your Coefficient Is Wrong: Omitted Variable Bias") with... a setup subsection and immediately a coffee example. I lost the link from "the DGP we just built" to "and here's the first way it breaks OLS." A one-sentence bridge like "We now take the DGP from Section 2 and watch OLS fail on it in eight different ways. First up: omitted variables." would anchor me.

- **Section 11 placement is weird.** The document goes Sec 10 (RDD, "redemption") → Sec 11 (FWL). After the redemption I expected either a summary or the end. Instead I got another theorem chapter. The coefficient tracker at the top of Sec 11 doesn't explain *why* FWL comes now and not earlier. Is it a toolkit chapter? A capstone? I couldn't tell while skimming. Add a line: "You've now seen all eight failure modes. Before the summary, we stop to nail down what 'controlling for' actually means — a piece of machinery that should have appeared in Section 3, but makes more sense after you've seen it fail."

- **Section 12 → 13 transition.** Sec 12 ends with a warningbox about diagnostics being insufficient. Sec 13 ("Theorem Map") opens cold with a table. No bridge. I had no idea Sec 13 was going to be a table. A one-liner: "Here is every result we proved, in one place."

- **BS Detector appendix (Sec 15).** This is LOVELY and I would print it and tape it to my wall. But it's buried after the proofs appendix. As a zig-zag reader, I would put this RIGHT after the Conclusion, before proofs. The cheat sheet is what I'll actually use.

---

## 5. Box fatigue

Density hotspots (places where three+ boxes cluster with no prose breathing room):

- **Section 8 (Causation), lines 1156–1247.** In ~90 lines I counted: keyinsight, toystory, keyinsight, warningbox, numermark, vizspec, keyinsight. Seven boxes, rapid-fire. My eye bounces between them and I stop reading the connective prose entirely. After three boxes in a row, I start skipping boxes because I've been overstimulated. Thin this out — merge the two keyinsights around the "control for everything" discussion (1201 and 1247) into one, or convert one into plain prose.

- **Section 5 (Significance), lines 776–828.** Toystory → Try-It-Yourself → Keyinsight → Keyinsight. Two keyinsights back-to-back at 810 and 828. When I zig-zag I can't tell these apart — both are blue, both say Key Insight, both are short. Either merge them or retitle one.

- **BS Detector cheat sheet (line 1940 onward).** Four yellow boxes in a row with near-identical styling. That's actually fine *for a cheat sheet* (I want them uniform), but note the tension: the same visual pattern that's noise in a chapter is a feature in a reference sheet. Keep it.

No complaints about Sections 2, 4, 6, 7, 10, 11 — box density there feels right.

---

## 6. Rating: **8 / 10**

If I jump around, does this hold my attention? Yes, most of the time. The coefficient tracker, the ghost metaphor, the cold open, and the Toy Story boxes are genuinely excellent zig-zag infrastructure. I would recommend these notes to another ADHD student unprompted. Last round's notes I'd have given a 6.

What holds it back from a 9 or 10:
1. Anna & Ben absent from 6 of 10 failure-mode sections (biggest issue — broken promise from intro)
2. `keyinsight` overused, and the custom `tcolorbox` one-offs break the visual grammar
3. Section 11 placement/framing is disorienting on zig-zag
4. No Repair box at the end of every failure section (the rhythm is almost-but-not-quite consistent)

---

## 7. Top 3 fixes for zig-zag readers

### Fix 1: **Bring Anna & Ben into every failure-mode section.**
One sentence per section is enough. Pattern: "[Current pathology] hits Anna and Ben like this: [one-line consequence]." Target sections: 4 (Het), 5 (Significance), 6 (Specification), 7 (Overfitting), 9 (Real World), 11 (FWL numerical example — just rename persons A–E to Anna, Ben, Clara, Daniel, Eva). This converts them from "intro characters I forgot about" to "the anchor that survives every zig-zag jump."

### Fix 2: **Define explicit named environments for the one-off boxes AND put a small icon/label strip at the top of each section indicating its role.**
Right now Cold Open, Algorithm That Ruined 72 Hours, Try It Yourself, Predict Before You Peek, and Stand Up If Significant are all raw `tcolorbox`. Promote them to named environments (`\begin{coldopen}`, `\begin{tryit}`, `\begin{predict}`) so a zig-zag reader learns "oh, gold box with play-icon = hands-on exercise." Also add a tiny label at each section heading: "Failure Mode 3 of 8" or "Toolkit" or "Redemption." When I jump to a page, one glance at the header tells me what kind of section I'm in.

### Fix 3: **Standardize every failure-mode section to the same 6-box rhythm and flag it at the top of the notes.**
The rhythm: Coefficient Tracker → Toy Story → Math → Numerical Example → Warning → **Repair** → Visualization. Currently some sections have all six, some skip the Repair (Sections 7, 8). Fill the gaps. Then in "How to Read These Notes" show the rhythm as a visual template so I know what to expect and can predict what's coming next. This kills the #1 zig-zag failure — not knowing what's next — at the structural level, once and for all.

---

*— Tobias*
