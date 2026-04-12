# The Anna and Ben Mystery

*A narrative arc for `dgp-intro.html`*

---

## Prologue (before Stage 1)

Meet Anna. Meet Ben.

They sit in the same lecture hall. They take the same notes. This semester, both tell you — honestly — that they studied **2 hours a day** and attended **10 out of 12 lectures**.

Then the exam happens.

Anna scores **72**. Ben scores **58**.

*Same hours. Same attendance. Fourteen-point gap.*

You're going to spend the next ten minutes figuring out why. Not by guessing. By **building**, piece by piece, the hidden machine that produces exam scores in this world. By the end, you'll know Anna and Ben better than their own instructors do.

Ready? Let's start with one variable.

---

## Stage 1 — A world without surprises

### Opening hook

Imagine, for a moment, a universe that's almost embarrassingly fair. Every hour you study adds exactly the same number of points. No luck. No mood. No bad coffee. If you could peer into the grade-generating machine of this universe, it would look like a single clean line.

### Body

Drag the slider. Watch what happens to Anna's exam score as her study hours change.

> **[beat — the reader pulls the slider]**

There's no mystery here. Two hours gives you one score. Four hours gives you another. The relationship is *exact*. A function, in the strict mathematical sense — one input, one output, no wiggle room.

This is what a regression model *wishes* the world looked like: a tidy rule, a straight arrow from cause to effect.

> **[beat — Anna and Ben appear, both at 2 hours, both landing on the same point on the line]**

Notice something strange? On this line, Anna and Ben are in the *exact same spot*. Same hours in, same score out. Our mystery has no oxygen in this universe. To solve it, we need to break the line.

### Transition out

But you already know real life isn't like this. You've had the bad exam after the good preparation. You've had the lucky guess on a question you didn't study. **What happens when we let a little chaos in?**

---

## Stage 2 — Letting the world breathe

### Opening hook

Every real measurement is the signal plus something *else*. A sneeze. A typo. A question that happened to favor one student's intuition. Statisticians have a name for this else: **noise**. And the moment we add it, our tidy line starts to shimmer.

### Body

Press **Run Semester** to simulate one class taking the exam.

> **[beat — a single dot lands near, but not on, the line]**

That's Anna. Two hours studied. But her score isn't exactly where the line said it should be. It's close. It *wobbles*.

Press it again. And again.

> **[beat — repeated runs; Anna's dot lands in different places each time]**

Same Anna. Same study hours. *Different score every time.* Because the world threw in a little ε — a little epsilon, a little randomness — between the rule and the result.

This is the first honest thing we can say about the world: **Y is not a function of X. Y is a function of X, plus something we can't see.**

### Transition out

One student wobbling around a line is a curiosity. But what if we ran the semester with a *hundred* students? Would the line still be visible — or would the noise swallow it whole?

---

## Stage 3 — A hundred students, one truth

### Opening hook

Here is the magic trick at the heart of regression. Take a cloud of dots that looks, at first glance, like a mess. Squint. Somewhere inside that mess is a line that nobody drew — but everybody is wobbling around. Your job, as a statistician, is to find it.

### Body

Press **Run Semester (n=100)**. Watch a hundred students land at once.

> **[beat — the cloud appears]**

Messy, right? Some students studied 1 hour and scored well. Some studied 4 hours and bombed. If you showed this to a friend with no training, they might say: "There's no pattern here."

There is. Watch.

> **[beat — the OLS line is drawn through the cloud, slowly]**

That line isn't a guess. It's the line that sits as close as possible to all the dots at once — the line that minimizes the total squared distance from every dot to itself. **Ordinary Least Squares.** OLS. The workhorse of every statistics course ever taught.

> **[beat — Anna and Ben highlighted in the cloud]**

There's Anna, sitting comfortably above the line. There's Ben, stuck below. The *line* tells you what the average student with their hours would score. The *distance* from the line tells you how much each person defied the average.

But why does Anna *consistently* sit above? Hold that thought.

### Transition out

Look closely at the cloud. The line we drew is straight. But the dots... aren't they curving a little? Like the line is too steep on the right, and too shallow on the left? **Maybe the world isn't linear after all.**

---

## Stage 4 — When straight lines lie

### Opening hook

Going from 1 hour of study to 2 is life-changing. Going from 9 hours to 10 is... fine. An extra hour of panic. You already know this in your bones. The question is: how does a statistician *write it down*?

### Body

Toggle between **Linear** and **Log**.

> **[beat — the straight line bends into a curve]**

That curve is `log(X₁)`. It rises fast when hours are small, then flattens. It says: the first hour of studying is worth a *lot*. The tenth hour is worth a little. **Diminishing returns**, baked right into the equation.

> **[beat — residuals shown as vertical bars under each line]**

See how the log curve hugs the dots more tightly? The little vertical bars — the residuals — get shorter. The model is no longer fighting the data. It's *listening* to it.

> **[beat — Anna and Ben at 2 hours each, sitting on the log curve]**

Here's our pair. Both at 2 hours, both sitting on the curve — and yet Anna is still floating above, Ben still sinking below. The shape of the curve has changed. The mystery has not.

### Transition out

We've explained the *shape* of the relationship. We have not explained **Anna**. Something about her — something we haven't measured yet — lifts her score above the curve every single semester. What if study hours weren't the only thing that mattered?

---

## Stage 5 — A second witness

### Opening hook

A detective never trusts a single witness. Neither should a model. If you want to predict an exam score, study hours is a start — but what about actually *showing up*?

### Body

We're going to add a second variable: **X₂**, lectures attended out of 12. Flip the switch.

> **[beat — the 2D cloud tilts into a 3D scatter; a plane replaces the curve]**

The line has become a **plane**. Two inputs, one output. For every pair — hours studied *and* lectures attended — the plane tells you the predicted score.

> **[beat — Anna and Ben pinned on the plane, both at (2 hours, 10 lectures)]**

And here is where it gets uncomfortable. Anna and Ben have the *same* coordinates on the plane. Same hours. Same lectures. The plane says they should score the same.

*They don't.*

We added a witness. The witness agrees with the first one. And yet Anna is still floating, Ben still sinking. Two variables aren't enough. **Something is missing from our model.**

### Transition out

What if the thing that separates Anna from Ben isn't something we can measure at all? What if it's been sitting in the data the whole time — invisible, unnamed, quietly pulling the strings?

---

## Stage 6 — The ghost in the machine

### Opening hook

Meet **U**. You can't see U. You can't measure U. U doesn't appear in any spreadsheet, any survey, any gradebook. But U is the reason Anna is Anna and Ben is Ben.

### Body

Let's call U **self-discipline**. Call it grit. Call it whatever you like — the thing that makes one person review their notes the night before and another person open Netflix. It's real. It's powerful. And we have **no column for it**.

> **[beat — U revealed as a hidden dial; Anna's dial at 0.85, Ben's at 0.15]**

Anna's U is high. Ben's U is low. And now look what U *does* in the machine.

> **[beat — arrows animate from U into X₁, X₂, AND Y]**

U doesn't just affect the exam score directly. U affects how many hours Anna *chooses* to study. U affects how many lectures she *bothers* to attend. U is upstream of everything.

This is called a **confounder** — a hidden variable that shapes both the inputs and the output. And confounders are how perfectly good regressions tell perfectly wrong stories. Your model will look at Anna's hours and credit them for her score. But some of that credit belongs to U — the thing that made her study those hours *and* made her ace the exam for reasons beyond them.

> **[beat — Anna and Ben shown side by side; their "identical" inputs revealed to have slightly different U-tinted origins]**

Anna and Ben reported the same hours. But for Anna, those 2 hours were focused, engaged, disciplined. For Ben, they were 2 hours with a phone in his hand. The *number* is the same. The *thing it represents* is not.

### Transition out

U explains the gap. But it also warns us: our model's view of the world is incomplete in ways we can't fix by adding more columns. And there's one more surprise waiting in the noise itself — **what if the chaos isn't the same size for everyone?**

---

## Stage 7 — Noise that grows

### Opening hook

We said ε was random. We did not say it was *equal*. Look closely at the students who studied very little and the students who studied a lot. Does the spread look... different?

### Body

Run the semester. Then sort the students left to right by hours studied.

> **[beat — a fan-shaped cloud appears, narrow on the left, wide on the right]**

See it? On the left, where hours are low, the dots hug the curve tightly. On the right, where hours are high, the dots *spray*. Some high-hour students crush the exam. Some high-hour students bomb it anyway. The variance of ε grows with X₁.

This has a name that sounds scarier than it is: **heteroscedasticity**. Hetero — different. Scedastic — scatter. Different scatter in different regions. It means our comfortable assumption — that noise is one uniform fog over everything — is wrong.

> **[beat — confidence band widens as X₁ increases]**

Why does this matter? Because when you predict Anna's score — Anna who studies a lot — your uncertainty is *larger* than when you predict a student who barely studied. The line is the same. The *trust* in the line is not.

### Transition out

So far, every variable we've added has helped. More information, better model — right? Prepare yourself. The next variable is going to **destroy** everything we've built, and it's going to look *helpful* while it does it.

---

## Stage 8 — The trap

### Opening hook

Imagine a magic new feature. You walk up to each student after the exam and ask: *"How do you think you did?"* Their answer — call it X₃ — correlates beautifully with their actual score. Should you put it in your model?

*Your instincts are about to betray you.*

### Body

Add X₃ to the regression.

> **[beat — R² jumps to something suspiciously close to 1]**

Look at that. Near-perfect prediction. The model is *triumphant*. You could publish this. You could sell this.

You would be lying.

> **[beat — the causal diagram redraws: arrow from Y → X₃, not X₃ → Y]**

X₃ isn't a *cause* of the exam score. X₃ is a **consequence** of it. Students who did well *feel* like they did well. Students who bombed *feel* like they bombed. You're not predicting the score — you're predicting the score using a very slightly noisier version of the score itself.

This is a **post-treatment variable**. It's measured *after* the thing you're trying to explain. And when you include it, it steals the credit from every honest predictor. Study hours? No longer matters. Lectures? Irrelevant. The model puts all its weight on X₃, because X₃ is basically Y in a costume.

> **[beat — Anna and Ben compared one final time]**

Here's the cruelest part. If a professor used this model to *advise future students*, they might say: "Your hours don't matter. What matters is feeling confident about the exam." That advice is worse than useless. It's backwards. **You don't score well because you feel confident. You feel confident because you scored well.**

### Closing

Let's return to where we started.

Anna: 2 hours, 10 lectures, score 72.
Ben: 2 hours, 10 lectures, score 58.

You now know why.

Anna's U was high. That same discipline made her 2 hours *denser* than Ben's 2 hours, made her lectures more attentive, and gave her a direct boost on exam day beyond anything we could measure. The 14-point gap wasn't mysterious. It was U, doing what U always does — shaping inputs, shaping outputs, staying invisible.

A regression model built on (X₁, X₂) alone would have shrugged at this gap and called it noise. A regression model built on (X₁, X₂, X₃) would have "explained" the gap by cheating. Neither model would tell you the truth: **that the most important variable in this story was the one we never got to measure**.

That's the job, from here on out. Not just to fit lines. To know which lines are honest.

Welcome to the rest of the course.
