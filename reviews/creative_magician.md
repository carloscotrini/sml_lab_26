# The Dramatic Arc: Redesigning "Regression Autopsy" as a Stage Performance

**Author:** The Stage Magician  
**Date:** April 2026

---

## Preamble: The Philosophy

The greatest magic trick ever performed is not a disappearing elephant. It is the moment an audience realizes they have been fooled -- and *loves it*. That moment requires three things: the audience must feel confident, they must be wrong, and the reveal must feel inevitable in hindsight.

This lecture already has several of those moments. The seat number table. The collider bias opener. The tutoring sign-flip. But right now they are scattered across a 90-minute runtime with no overarching rhythm. The energy map below turns a collection of good tricks into a *show*.

---

## 1. The Energy Map (90-Minute Lecture)

The fundamental rhythm of a 90-minute performance is five peaks separated by valleys of focused quiet. Peaks are for surprise, laughter, and physical participation. Valleys are for derivations, reflection, and the slow build of tension before the next peak. The audience should never go more than 12 minutes without a jolt.

```
Energy
  ^
  |
H |   *P1*                *P2*          *P3*              *P4*        *P5*
  |  /    \              /    \        /    \            /    \      /    \
  | /      \    ___     /      \      /      \     ____/      \    /      \
M |/        \  /   \   /        \    /        \   /            \  /        |
  |          \/     \ /          \  /          \/               \/         |
L |                  V            V                                        |
  +-------------------------------------------------------------------------> Time
  0    10    20    30    40    50    60    70    80    90 (min)
```

### Minute-by-Minute Breakdown

**0:00 -- 0:30 | COLD OPEN (silence, then shock)**
Walk to the front. Say nothing. Project a single slide: a regression table showing that a tutoring program *decreases* student grades by 3 points, p < 0.01. Let the audience read it. Then, quietly: "This regression is a lie. Every diagnostic passed. The standard errors are correct. The model fits well. And the answer has the wrong sign. By the end of this lecture, you will know exactly how this happened -- and you will never trust a regression output the same way again." Pause. Let it land.

**0:30 -- 7:00 | THE SETUP: Meet the Dataset (Low-Medium Energy)**
Introduce the exam score DGP. But do NOT show equations. Show the causal graph first. Arrows. Stories. "Self-discipline is the thing you cannot see. It lives on Instagram's servers, not in the registrar's database. And it is about to ruin everything." Quiet, narrative, world-building. The audience should feel like they are entering a story, not a textbook.

**7:00 -- 12:00 | PEAK 1: "Raise Your Hand If..." (High Energy)**
*[See Audience Participation Trick #1 below.]* The OVB reveal. The audience votes on what they think the studying coefficient is. Most guess too high. You show the OVB formula -- the number drops. The room reacts.

**12:00 -- 22:00 | THE FIRST VALLEY: The Math of OVB (Low Energy, Focused)**
This is the proof. The derivation. The numerical example with five students. The room is quiet. Pens are moving. This is the "pledge" -- the setup where the magician shows you something ordinary (a coin, a deck of cards) and you inspect it carefully. Let the audience sit with the math. Do not rush it. The quiet makes the next peak hit harder.

**22:00 -- 28:00 | PEAK 2: "The SheKnows Article" -- Collider Bias (High Energy)**
Project the actual SheKnows headline: "Why Hot Guys Are Jerks." Read it out loud. Ask the audience: "Is this true? Raise your hand if you have noticed this pattern in real life." Hands go up. Laughter. Then: "You are all experiencing collider bias. Here is why." Walk through the Talent/Luck/Fame table. The room goes from laughing to quiet to "wait, WHAT." This is a classic misdirection-to-reveal. They came in believing a folk observation; they leave understanding it is a mathematical artifact.

**28:00 -- 38:00 | THE SECOND VALLEY: Heteroscedasticity and Standard Errors (Medium-Low)**
Drunk Darts story (brief -- three sentences, not a paragraph). Then the sandwich formula. Then the key punchline: "OLS is not biased. It is overconfident. It is giving you the right answer while lying about how sure it is." Let this section breathe. The apartment rent example is a nice touch -- keep it. Cut the "Everyday Wisdom" box; it dilutes the energy.

**38:00 -- 45:00 | PEAK 3: The Seat Number Trick (High Energy)**
*[See Big Reveal #2 below and Audience Participation Trick #2.]* This is the centerpiece of the show. Set up the regression table. Let the audience see p = 0.002. Watch their faces. Then the reveal. This one gets audible reactions every time.

**45:00 -- 47:00 | INTERMISSION BEAT (Low Energy)**
Two minutes of quiet. Summarize where we are. "So far, your coefficient is wrong, your standard error is wrong, and your p-value is meaningless. And we are only halfway through." A beat. Let the weight of that land.

**47:00 -- 57:00 | SPECIFICATION AND OVERFITTING (Medium Energy)**
The straight ruler on a winding road. The extrapolation to 132.5 points (get a laugh). The degree-15 polynomial table (gasp -- negative test R-squared). This section is a steady build. Not a single peak, but a rising slope.

**57:00 -- 65:00 | PEAK 4: The Instrumental Variable Magic Trick (High Energy)**
*[See Big Reveal #4 below.]* OLS says 8.71. The truth is 3. The audience has been watching OLS fail for 57 minutes. Now you pull out the instrument -- the roommate -- and the number lands on 3.0. Exactly. The relief in the room is palpable. This is the first time something *works*. After an hour of autopsy, the patient finally has a pulse.

**65:00 -- 75:00 | THE THIRD VALLEY: RDD (Medium Energy, Hope)**
The kid who scored 69 vs. 70. This section should feel like the third act of a heist movie -- the plan is coming together. The scholarship cutoff. The clean identification. The audience should feel the shift: we are no longer diagnosing failure. We are building something that works.

**75:00 -- 82:00 | PEAK 5: The Callback (High Energy)**
*[See The Callback Chain below.]* Return to the tutoring regression from the cold open. Walk through it step by step. Show why every diagnostic passed. Show the sensitivity analysis. Show how fragile the result is. Then show the experimental estimate: +8 points. The sign flips. The audience gasps. You have completed the trick you promised in the first 30 seconds.

**82:00 -- 88:00 | FWL as Epilogue (Medium Energy)**
"One more thing." The coaching vs. shoes story. FWL as the explanation of what "controlling for" actually means. This is the denouement -- the audience is winding down, but this final insight clicks everything into place.

**88:00 -- 90:00 | THE CLOSER**
*[See Section 5 below.]*

---

## 2. The Five Big Reveals

### Big Reveal #1: "Your Coefficient Is Inflated" (OVB, minute ~10)

**Setup:** "We have 500 students. We regress exam scores on hours studied. The coefficient says each hour of studying adds 10.5 points. Sounds right -- studying helps, and more is better."

**Misdirection:** Show a clean scatterplot. The slope looks reasonable. The R-squared is decent. The p-value is tiny. Ask the audience: "How many points do you think one extra hour of studying *really* adds?" Take guesses. Most will say 8-12. Write the guesses on the board.

**Reveal:** "The true answer is 8 points per log-unit -- which means about 5.5 points for doubling your study time from 1 to 2 hours, and only 0.9 points for going from 9 to 10 hours. The 10.5 you saw? Two and a half of those points belong to self-discipline, not studying. OLS stole them from a variable you never measured."

**Explanation:** The OVB formula. E[beta_hat_short] = beta_1 + beta_2 * delta_1. The bias is positive because discipline drives both studying and scores. Five-student numerical example. Verify on paper.

---

### Big Reveal #2: "The Seat Number Prophecy" (Significance, minute ~40)

**Setup:** "I ran a regression of exam scores on seat number. Seat number. The number on the chair you happened to sit in. There is zero -- absolutely zero -- reason why this should predict your grade."

**Misdirection:** Project the regression table. Coefficient: 0.003. SE: 0.001. p-value: 0.002. Ask: "Is this significant?" The audience will say yes. Some will say "obviously yes, look at the p-value." Write "SIGNIFICANT" on the board in big letters.

**Reveal:** "Zero point zero zero three. Three thousandths of a point. The total difference between seat 1 and seat 200 is 0.6 points on a 100-point exam. You could not measure this with a magnifying glass. But the p-value says it is 'highly significant.' Because with 50,000 observations, the standard error shrank to one thousandth -- and three thousandths divided by one thousandth is three, which is enough to cross the threshold." Erase "SIGNIFICANT" from the board. Write "DETECTABLE" instead. "Statistical significance tells you the effect is not exactly zero. It tells you nothing about whether the effect matters."

**Explanation:** t = beta_hat / SE. SE = O(1/sqrt(n)). As n grows, |t| grows for any fixed nonzero beta. The keyboard example seals it: the same 0.1-second effect goes from "not significant" to "HIGHLY SIGNIFICANT" just by collecting more emails.

---

### Big Reveal #3: "Famous People's Spouses Seem Boring -- And It Is Math" (Collider Bias, minute ~25)

**Setup:** "Among famous people, have you noticed that their partners often seem... average? Not ugly, not dumb, just... unremarkable. The internet has a whole genre of 'how did THEY land THEM?' content."

**Misdirection:** Project the SheKnows headline or equivalent cultural reference. Show a few examples. The audience nods. "So is it true? Does being famous make you choose worse partners? Or does having a famous partner somehow diminish you?" The audience is now reasoning about psychology, culture, power dynamics. They are confident in their sociological explanations.

**Reveal:** "It is none of those things. It is arithmetic." Show the Talent/Luck/Fame table. Four types. Remove the nobodies. Suddenly, among the famous, talent and luck are negatively correlated. "You manufactured a tradeoff that does not exist in the general population. The moment you filtered on fame -- the collider -- you opened a spurious path. Every hot-take artist on Twitter explaining why Pete Davidson dates supermodels is accidentally doing incorrect causal inference."

**Explanation:** Proposition on collider bias. Cov(X, U | C) != 0 even though Cov(X, U) = 0. The conditional covariance formula. The sign is negative -- conditioning on the collider creates an *inverse* relationship from nothing.

---

### Big Reveal #4: "The Roommate Rescue" (IV, minute ~60)

**Setup:** "For the last hour, we have watched OLS fail. Wrong coefficient, wrong standard errors, wrong significance, wrong functional form, wrong causal claims. Is there anything that actually works? Can we ever get the right answer from observational data?"

**Misdirection:** "What if I told you: OLS says studying adds 8.71 points per hour. The truth is 3. And no matter how much data you collect -- ten million students, every university on Earth -- OLS will never get closer to 3. The bias is baked in. It does not shrink with the sample size. Are you depressed yet?"

**Reveal:** "Now. Your roommate was randomly assigned. Your roommate's study habits influence how much *you* study. But your roommate does not take the exam for you. Watch this." Compute the IV estimate: Cov(Z,Y)/Cov(Z,X) = 6.0/2.0 = 3.0. Exactly the true effect. "By using only the *clean* variation in studying -- the part driven by your roommate, not your own discipline -- we stripped out the contamination. The answer is 3. On the nose."

**Explanation:** IV consistency theorem. The formula. Why exclusion matters. Why relevance matters. The first-stage F-statistic as a quality check.

---

### Big Reveal #5: "The Tutoring Program That 'Hurts'" (Real World, minute ~78)

**Setup:** This is the payoff of the cold open. "Remember the first slide? Tutoring decreases grades by 3 points. p < 0.01. Every diagnostic passed."

**Misdirection:** Walk through the diagnostics one by one. VIF: low. Breusch-Pagan: non-significant. Robust SEs: barely change. Q-Q plot: normal. "By every standard diagnostic in your toolkit, this regression is clean. The model is internally consistent. The residuals look fine." Pause. "Would you shut down the tutoring program?"

**Reveal:** "The students who signed up for tutoring are the ones who were already struggling. Low discipline, missed lectures, fewer study hours. They would have scored poorly *regardless*. Tutoring helps -- the experimental estimate is +8 points. But OLS confused 'who selects into tutoring' with 'what tutoring does.' The sign is not just wrong. It is backwards. And nothing in the regression output told you."

**Explanation:** Self-selection as omitted variable bias. The Lalonde dataset as the real-world version. The robustness value: how fragile was the -3 estimate? Extremely. A confounder with even modest partial R-squared could flip it. "Diagnostics check the model. Only the research design checks the answer."

---

## 3. Audience Participation Tricks

### Trick #1: "The Coefficient Auction" (minute ~8)

**Format:** Live polling or hand-raising.

**Execution:** Before showing any regression output, ask: "How many points does one extra hour of studying add to your exam score? Shout out a number." Collect 5-6 guesses. Write them on the board. Most will cluster around 5-10.

Then show the naive OLS estimate: ~10.5 (or whatever the DGP produces without controls). "Looks like the optimists were right!"

Then add controls. The coefficient drops. Then reveal the OVB formula. Then reveal the true effect via the log model.

Come back to the board: "Who was closest?" The person who guessed lowest wins. "In regression, the gut feeling is almost always too high -- because the gut includes confounders."

**Why it works:** The audience is now personally invested in the coefficient. When it changes across specifications, they feel it. They wrote their guess on the board; their identity is tied to it.

---

### Trick #2: "Stand Up If You Think It Is Significant" (minute ~40)

**Format:** Physical movement.

**Execution:** Project the seat number regression table. "Stand up if you think this result is statistically significant." Most of the room stands. "Stay standing if you think this result is *practically important*." Watch the room sit down in waves as they read the coefficient (0.003 points per seat). By the end, almost no one is standing.

"Look around. Almost everyone in this room stood up for 'significant.' Almost no one stayed up for 'important.' That gap -- between standing and sitting -- is the entire point of this section."

**Why it works:** The physical act of standing and then sitting creates a body-memory of the distinction between significance and importance. They *felt* the difference in their legs.

---

### Trick #3: "Vote With Your Feet: Should We Shut Down Tutoring?" (minute ~76)

**Format:** Move to one side of the room.

**Execution:** Show the tutoring regression (coefficient: -3, p < 0.01). "Left side of the room: you think we should keep the tutoring program. Right side: the data says shut it down. Go." The room splits. Probably 60/40 toward shutting it down -- the regression is "significant," after all.

Then reveal the experimental estimate (+8 points). Then reveal the selection bias. Then ask the "shut it down" side: "What convinced you? The p-value? The coefficient? The diagnostics?" Watch them articulate exactly the reasoning traps the lecture has been dismantling.

"You just made a policy decision that would have hurt struggling students -- based on a regression that passed every diagnostic. This is why research design matters more than statistical technique."

**Why it works:** This creates genuine moral stakes. The audience is not solving a math problem -- they are making a decision about real people. The wrongness of "shut it down" is not just intellectually incorrect; it *feels* wrong once you know the truth. That feeling cements the lesson.

---

## 4. The Callback Chain: "The Coefficient on Study Hours"

### The Recurring Element

One number. One coefficient. The effect of studying on exam scores. It appears in every single section, and it is *wrong in a different way every time*.

This is the vanishing card. The audience watches it transform across the show, and each transformation reveals a new failure mode.

### The Chain

| Moment | Section | What the Coefficient Says | What Is Wrong |
|--------|---------|--------------------------|---------------|
| 1 | Cold open | Tutoring: -3 points | Wrong sign (selection bias) |
| 2 | OVB | Studying: ~10.5 points | Inflated (self-discipline confounding) |
| 3 | Heteroscedasticity | Studying: 10.5 +/- 1.2 | Interval too narrow (wrong SEs) |
| 4 | Significance | Seat number: 0.003*** | Meaningless but "significant" |
| 5 | Specification | Studying: 1.6 per hour (linear) | Wrong shape (log truth, linear fit) |
| 6 | Overfitting | Studying: degree-15 poly, R^2=0.97 | Memorizing noise |
| 7 | Collider bias | Studying (controlling for confidence): near 0 | Destroyed by bad control |
| 8 | IV | Studying: 3.0 (via roommate) | Finally correct |
| 9 | RDD | Scholarship effect: 5.0 | Correct by design |

### How to Use It

Keep a running tally on the board (or a persistent slide in the corner of the presentation). Every time the coefficient changes, update the tally. By the end, the board has nine numbers -- a visual history of everything that went wrong and the two moments something finally went right.

When you reach the IV section and the number finally lands on 3.0, point to the board: "Eight wrong answers. Two right ones. And the two right ones did not come from better statistics -- they came from better *design*."

This single thread ties the entire lecture into a narrative. Without it, the sections feel like independent modules. With it, they feel like chapters in a detective story.

---

## 5. The Closer (Minutes 88:00 -- 90:00)

*[Dim the slides to a single dark background. Step to center stage. No notes.]*

"Let me tell you what I hope you take away from today.

At the beginning of this lecture, I showed you a regression that said tutoring hurts students. The p-value was tiny. The diagnostics were clean. The model was internally consistent. And the answer was not just wrong -- it was backwards.

I then spent ninety minutes showing you eight different ways a regression can lie to you. Your coefficient can be inflated by a variable you never measured. Your confidence interval can promise precision you do not have. Your p-value can scream 'significant' about something that does not matter. Your model can memorize noise and call it understanding. Your controls can destroy the very thing you are trying to estimate.

And yet.

*[Pause. Three seconds.]*

The roommate instrument gave us 3.0. Exactly. The scholarship cutoff gave us 5.0. Exactly. Not because we ran a fancier model. Not because we found better data. Because someone thought carefully about *where the variation comes from*.

That is the lesson. Regression is not broken. It is a power tool. And like every power tool, it will take your hand off if you do not respect what it can and cannot do.

*[Point to the board with the nine coefficients.]*

You have seen nine versions of the same number today. Eight of them were wrong. Two were right. The difference was never the math. The difference was the thinking that came *before* the math."

*[Final slide appears: the closing line from the notes.]*

"This does not mean you should stop using regression. It means you are finally ready to start."

*[Hold for two beats. Then: lights up, applause.]*

---

## Summary of the Redesign

The core architectural change is this: the lecture currently reads as a sequence of independent failure modes, each with its own story and proof. The redesign turns it into a single continuous narrative -- a detective story where the same coefficient keeps getting distorted by different villains, and the audience watches the investigation unfold in real time.

The five peaks are spaced at roughly minutes 10, 25, 40, 60, and 78 -- never more than 18 minutes apart, never less than 12. Between them, the valleys provide the mathematical substance that makes the peaks meaningful. The physical participation tricks (standing, voting, shouting guesses) anchor the abstract concepts in body memory. The callback chain (the coefficient tally on the board) gives the audience a visual throughline that makes every section feel like part of the same story.

The cold open and the closer form a frame: the tutoring regression appears at minute 0 and returns at minute 78, and the mystery is solved. Everything between those two moments is the investigation. The audience leaves not just knowing the math, but having *experienced* it as a narrative -- setup, misdirection, reveal.

That is how you turn a lecture into a show.
