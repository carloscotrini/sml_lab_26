# Creative Storyteller Review: Section-by-Section Comedy & Engagement Proposals

**Reviewer:** Creative Storyteller (comedy writer / science communicator persona)
**Date:** April 2026
**Mission:** Make every section of Regression Autopsy so memorable that students leave the lecture hall quoting it.

---

## Guiding Principles

The notes already have genuine hits: the Pete Davidson collider example, the SheKnows article reveal, drunk darts, seat number significance, and the 69-vs-70 kid. The pattern behind these wins is always the same: (1) present something students already believe, (2) let them commit to it emotionally, (3) pull the rug out mathematically. Every proposal below follows that template.

I also propose a **running gag** that threads through the entire lecture series: **"The Exam Score Cinematic Universe" (ESCU)**. Each section opens with a fake movie-trailer-style voiceover recap of the previous section's disaster, delivered in the style of a Netflix "Previously on..." cold open. This gives the lecture series the feeling of a serialized show -- students will want to attend the next "episode." The professor can literally say, in a movie trailer voice: *"Last time on Regression Autopsy... your coefficient was a liar. This week... your uncertainty is about to betray you."*

---

## Section 1: Introduction

### The Opening Hook
Project the real BBC headline from August 2020: **"A-level results: Ofqual's exam algorithm -- how did it work?"** (BBC News). Then show a second headline from two days later: **"A-level results: 'Unfair' algorithm to be scrapped"** (The Guardian). Let students absorb the timeline: an algorithm decided half a million students' futures on a Tuesday, and was scrapped by Thursday.

Then say: "That algorithm was a regression model. It included school-level variables, prior performance, and teacher predictions. It looked fine on paper. Its R-squared was good. Its diagnostics passed. And it systematically downgraded students from disadvantaged schools, ruined university admissions for thousands of teenagers, and was abandoned within 72 hours."

Pause. "This course is about why."

### The Punchline Moment
After introducing the five variables (Y, X1, X2, X3, U), pause on U (self-discipline) and say: "Here is the thing about U. Everyone in this room has one. You filled out an Instagram story slider about yourself once, maybe for fun, maybe ironically. That number -- your self-reported discipline score -- is sitting on Instagram's servers right now, and it is the single most important variable in every regression we will run this semester. You cannot access it. I cannot access it. The university cannot access it. But it is driving every result we will see for the next eight weeks. The most important variable in your data is the one you do not have. Welcome to statistics."

### The Callback
The A-level algorithm should become the recurring "ghost" of the course. Whenever a new failure mode is introduced, flash the BBC headline briefly on the slide. By Section 7 (Real World), reveal which specific failure modes were present in the Ofqual model. This gives students a cumulative "aha" as they realize each section explains one more piece of why the A-level disaster happened.

### The Meme-able Takeaway
**"The most important variable in your regression is the one you forgot to collect."**

---

## Section 2: The Data Generating Process

### The Opening Hook
Open with a live audience poll (raise hands or use a quick phone poll): "How many hours did you study for the last exam?" Record the rough distribution on the board. Then: "How many of you would describe yourselves as disciplined?" Record that. Then: "Interesting. The people who raised their hands for 'disciplined' are overwhelmingly the same people who said they studied the most. I did not need a regression to see that. But here is the problem: I can see both of those variables. In most real datasets, you only get one."

Then say: "For the next eight weeks, you get to be God. We are building a fake university from scratch -- every student's secret discipline score, every lucky break on the exam, every late-night cramming session. In the real world, God has the DGP and you do not. But in this classroom, you get to see every hidden variable, every causal arrow, every coefficient. Enjoy it. It is the last time in your career you will ever have this much information."

### The Punchline Moment
After walking through all six structural equations, return to the audience poll data and say: "By the way, when I asked who is disciplined, about 70% of you raised your hands. The real distribution is not that. Self-reported discipline is biased upward -- everyone thinks they are above average. This is exactly why U is unobserved: self-report is unreliable, and the reliable version lives on a server you cannot access. The DGP is not just a set of equations. It is a statement about what you can and cannot know."

### The Callback
Reference the Instagram slider every time U appears in later sections. "Remember, this number is sitting on a server in Menlo Park, California, and it is about to ruin your regression."

### The Meme-able Takeaway
**"In real life, God has the DGP and you do not. For the next eight weeks, you get to be God. Enjoy it -- it is the last time."**

---

## Section 3: Omitted Variable Bias

### The Opening Hook
Project the real published study: **"Countries that consume more chocolate per capita win more Nobel Prizes"** (Messerli, 2012, New England Journal of Medicine -- yes, this was published in the NEJM). Show the actual scatterplot. It is beautiful. The correlation is striking. Then ask: "So... should Switzerland invest in chocolate to win more Nobels?"

Let the room laugh. Then: "The omitted variable here is national wealth. Rich countries can afford both chocolate and research universities. But the New England Journal of Medicine published this. With a straight face. And a scatterplot."

Then pivot: "You have just witnessed omitted variable bias in the wild. The formula we are about to learn explains EXACTLY how much the chocolate coefficient is inflated, and why."

### The Punchline Moment
After proving the OVB formula and doing the numerical example, return to the chocolate-Nobel study. "The OVB formula says: Bias = (effect of wealth on Nobel Prizes) times (correlation between wealth and chocolate consumption). Both are positive. So the bias is positive. The chocolate coefficient is inflated by exactly the amount that wealth's ghost is haunting the regression. The formula does not just tell you something is wrong -- it tells you the exact magnitude and direction of the lie."

### The Callback
"Another ghost in the regression" should become a recurring phrase. Every time OVB appears in a later section, say "the ghost is back." In Section 7 (Real World), say: "In the tutoring example, the ghost is not just present -- it flipped the sign. The ghost is running the show."

### The Meme-able Takeaway
**"Leave out a variable that matters and is correlated with what you included, and its ghost haunts your estimate."** (This line is already in the notes -- promote it to a slide header.)

---

## Section 4: Heteroscedasticity

### The Opening Hook
Show a screenshot from Glassdoor or levels.fyi of software engineer salaries. Junior engineers: CHF 85K to CHF 95K. Staff engineers: CHF 150K to CHF 600K. "At the bottom, everyone makes roughly the same. At the top, the spread is enormous. Your confidence interval for a junior engineer's salary is tight. Your confidence interval for a senior's salary is so wide you could drive a truck through it. This is heteroscedasticity: the variance of the outcome depends on where you are on the predictor."

Then: "And here is the problem. Standard OLS looks at the tight cluster at the bottom AND the wide spread at the top and says, 'I am going to pretend the spread is the same everywhere.' It averages the noise. Which means it is overconfident about the seniors and underconfident about the juniors. Your confidence interval is lying, and the lie has a direction."

### The Punchline Moment
After presenting the coverage simulation (82% actual coverage vs. 95% nominal), say: "Let me rephrase that. If you use standard confidence intervals on this data, you will say 'I am 95% sure the answer is in this range' -- and you will be wrong nearly one time in five. Not one time in twenty. One time in five. That is not a rounding error. That is a lie you tell your boss, your client, or your reviewer, backed by the full authority of a formula you did not check."

### The Callback
"After three beers" (from Drunk Darts) should become shorthand for heteroscedasticity. In later sections, whenever standard errors are mentioned, a quick "are we sober or are we at three beers?" checks whether heteroscedasticity is a concern.

### The Meme-able Takeaway
**"Your confidence interval is not lying about where the truth is. It is lying about how sure you are."**

---

## Section 5: Significance vs. Effect Size

### The Opening Hook
Project the real CNN headline: **"Coffee drinkers live longer, study finds"** (CNN, 2017). Then show: **"People who eat more chocolate are thinner, study says"** (NBC). Then: **"Owning a cat may reduce heart attack risk by 40%"** (various). Let students nod along.

Then say: "Every single one of these studies had p-values below 0.05. Every single one had enormous sample sizes -- hundreds of thousands of people. Every single one found effects so small that they would make zero difference to any individual person's life. But the p-value said 'significant,' so here it is on CNN."

Then reveal: "This is exactly the seat number problem. With enough data, ANYTHING is significant. Your seat number in this room, right now, would predict your exam score at p < 0.002 if I had ten years of data. Not because seats matter, but because with 50,000 observations, even random noise looks 'significant.'"

### The Punchline Moment
Do the live version. Before class, run the seat-number regression on real exam data from a past year (anonymized). Project it live. Show the coefficient: 0.003 points per seat number. Show the p-value: 0.002. Then say: "According to this model, the student in seat 200 has a 0.6-point advantage over the student in seat 1. That is less than one point on a hundred-point exam. And the model says this is 'highly significant.' The model is not lying -- the effect IS statistically distinguishable from zero. But would you switch seats over 0.6 points? Would you write a CNN headline about it?"

Pause. "This is why we need effect sizes, not just p-values."

### The Callback
From this point forward, any time a p-value appears, the professor should ask: "Is this a seat number, or is this real?" This becomes a mental shortcut students can use forever.

### The Meme-able Takeaway
**"Statistical significance tells you the effect is not zero. It does not tell you the effect matters."** (Already in the notes -- make it the slide title in 48-point font.)

---

## Section 6: Specification Error

### The Opening Hook
Show a real fitness tracker chart -- the kind that shows "projected weight loss if you keep this up" in a straight line trending downward forever. "According to my Apple Watch, if I keep running 5K three times a week, I will weigh negative 12 kilograms by 2029." Let the absurdity land.

Then: "This is linear extrapolation. The model found a real trend in the data range where you have observations. Then it extended that trend into territory where it has never been, and predicted something physically impossible. This is not a bug in the fitness tracker. This is what EVERY linear model does when you extrapolate past your data. And it happens in contexts with much higher stakes than my jogging habit."

### The Punchline Moment
Walk through the studying example: a student who studied 30 hours gets a predicted score of 100.5. Then: "The model is telling you this student scored above the maximum possible score. The exam only goes to 100. The linear model says, with full statistical confidence, that this person broke mathematics." Pause. "And at 50 hours? The prediction is 132.5. The model is not just wrong -- it has left the building. It is in another dimension. This is what happens when you assume the relationship is linear and it is not."

### The Callback
"Your model just predicted a score of 132" becomes shorthand for extrapolation failure. Use it in Section 7 (overfitting) when the degree-15 polynomial goes off the rails: "The polynomial did not predict 132. It predicted negative 13. Which is honestly worse."

### The Meme-able Takeaway
**"A model that predicts a score of 132 on a 100-point exam is not being confident. It is being delusional."**

---

## Section 7: Overfitting

### The Opening Hook
Show the actual AI-generated art progression meme: early AI art (blurry, wrong) vs. current AI art (photorealistic). Then show an AI-generated image that is photorealistic but has seven fingers. "This image has a training R-squared of 0.97. It looks incredible. But it has seven fingers because the model memorized the noise in its training data. It learned that 'hands have approximately this many appendages' without learning the actual rule."

Then: "This is overfitting. A model that memorizes its training data can produce outputs that look spectacular -- right up until the moment it encounters something slightly different from what it trained on. Then you get seven fingers. Or, in regression terms, a test R-squared that is literally negative."

### The Punchline Moment
Show the polynomial degree table. Build suspense: degree 1 (training 0.71, test 0.69 -- "respectable"), degree 3 (0.82, 0.78 -- "looking good"), degree 7 (0.91, 0.63 -- "wait, training went up but test went DOWN"). Then degree 15: training 0.97, test negative. "Negative R-squared means the model predicts WORSE than just guessing the average. You built a model with 16 free parameters, it memorized every wiggle in your training data, and it now makes predictions that are literally worse than knowing nothing. You went to all that effort to be worse than ignorance."

Then show the Model C prediction: "In one training set, the degree-4 polynomial predicted a score of negative 13. Negative thirteen points on an exam. At least the linear model's 132 was optimistic. This model is telling you the student owes points."

### The Callback
"Seven fingers" becomes the recurring image for overfitting. In Section 9 (Real World): "The Lalonde observational estimate is the seven-fingered hand of causal inference -- it looks like a hand, it is shaped like a hand, but something is deeply, obviously wrong."

### The Meme-able Takeaway
**"A model with a 0.97 training R-squared and a negative test R-squared did not learn. It memorized. There is a difference."**

---

## Section 8: Endogeneity and Bad Controls (Causation)

### The Opening Hook
This section already has the crown jewel: the SheKnows article and Pete Davidson. But here is how to build on it.

Open by projecting the real SheKnows article: **"Really Hot Guys Are Also Really Not Nice, Says Science."** Do a quick show of hands: "Who agrees from personal experience?" (Laughs, many hands.) Then: "You are all falling for Berkson's paradox, and I can prove it with one table."

Do the Talent/Luck/Fame table. Then: "Here is the Pete Davidson version. Why did Twitter lose its mind every time Pete Davidson dated a supermodel? Because among famous comedians, being very funny compensates for not being conventionally attractive. So when you see someone who is famous AND funny, you expect them to not also be gorgeous. Pete Davidson is famous, funny, and dates supermodels, which violates your subconscious collider-bias expectations. Twitter was not observing reality. Twitter was observing a selection effect."

### The Punchline Moment
After the collider bias proof, return to the students' own lives: "Here is one that applies to everyone in this room. You are at ETH. Getting into ETH requires either being very hardworking or very naturally talented (or both). Among ETH students, you will observe a negative correlation between natural talent and work ethic -- the geniuses seem lazy, and the hardest workers seem average. This is NOT because talent makes you lazy. It is because you are conditioning on 'admitted to ETH,' which is a collider. In the general population, there is no such correlation. You manufactured it by being here."

Watch the room go silent. Then: "Every time you think 'that person is so smart but never studies,' you are committing collider bias. In real time. In this room."

### The Callback
"The ETH admissions collider" becomes a recurring reference. In Section 11 (FWL): "When you 'control for' ETH admission in your mental model of your classmates, you are doing exactly what FWL describes -- and in this case, it is giving you a biased picture of reality."

### The Meme-able Takeaway
**"Among famous comedians, being funny means you do not also need to be hot. That is not wisdom. That is collider bias."**

---

## Section 9: The Real World (Lalonde)

### The Opening Hook
Open with a true story: "In 2019, a study published in Science found that a major healthcare algorithm used across the United States was systematically deprioritizing Black patients for extra care. The algorithm used healthcare COSTS as a proxy for healthcare NEEDS. But because Black patients had historically spent less on healthcare -- due to reduced access, not reduced need -- the algorithm concluded they were healthier. It was a perfectly functioning regression model. It passed every diagnostic. And it was denying care to the people who needed it most."

Source: Obermeyer et al., "Dissecting racial bias in an algorithm used to manage the health of populations," Science, 2019. This is real, published, and devastating.

Then: "This is the Lalonde problem at scale. Every diagnostic passed. The model was internally consistent. And the conclusion was not just wrong -- it was the OPPOSITE of the truth."

### The Punchline Moment
After presenting the tutoring analogy, make the connection explicit: "The healthcare algorithm looked at the data and said: 'Black patients cost less, therefore they need less care.' The tutoring regression looked at the data and said: 'Students who go to tutoring score lower, therefore tutoring hurts.' Both models told the truth about the data. Both models lied about the world. The data said one thing. Reality said the opposite. And no diagnostic -- not VIF, not Breusch-Pagan, not robust standard errors -- could detect the lie. Because the lie was not in the model. The lie was in the assumption that the data represented reality."

### The Callback
"All diagnostics green, answer has the wrong sign" -- this should be referred to as "a Lalonde" for the rest of the course. In the Conclusion, the professor can say: "The A-level algorithm was a Lalonde. The healthcare algorithm was a Lalonde. Whenever someone tells you 'the model is fine, the R-squared is high, the residuals look clean,' your first question should be: 'Is this a Lalonde?'"

### The Meme-able Takeaway
**"A well-fitting model with clean diagnostics can give you an answer that is not just wrong, but directionally wrong. Diagnostics check the model. Only the research design checks the truth."**

---

## Section 10: Regression Discontinuity Design

### The Opening Hook
"Raise your hand if you have ever been one point away from the next grade." (Every hand goes up.) "Raise your hand if it felt deeply unfair." (Every hand stays up.) "Good. You have all experienced a natural experiment."

Then: "Here is the beautiful thing about that unfairness. The student who scored 69 and the student who scored 70 are, for all practical purposes, the same student. Same ability, same preparation, same background. One had a slightly better morning. One guessed right on one multiple-choice question. The difference is pure luck. And because it is pure luck, comparing their outcomes is as good as a randomized experiment. The cruelty of the cutoff IS the experiment."

### The Punchline Moment
After the scholarship numerical example, zoom out: "This is how researchers discovered that barely winning an election does not make politicians richer (Lee, 2008). That barely getting into a selective school does not improve your lifetime earnings (Abdulkadiroglu et al., 2014). That scoring just above the legal blood-alcohol limit leads to much higher recidivism (Hansen, 2015). Every sharp cutoff in the world is an RDD waiting to happen. Your 69-vs-70 grade boundary is one of them."

Then the twist: "RDD is the one section where regression EARNS its trust back. We have spent seven sections breaking regression. This is the section where it redeems itself. Not because the math got better, but because the DESIGN got better. The answer was not in the formula. It was in the structure of the problem."

### The Callback
"This is the redemption arc" -- frame RDD as the hero's return. "Your coefficient has been lying to you for seven sections. RDD is where it finally tells the truth -- not because it wanted to, but because the cutoff FORCED it to."

### The Meme-able Takeaway
**"The cruelty of the cutoff IS the experiment."**

---

## Section 11: Frisch-Waugh-Lovell

### The Opening Hook
"Your friend says cold showers made her more productive. But she also started meditating, quit social media, and began a new job -- all in the same month. Which change actually did the work?"

Show a real tweet or Reddit post from the productivity-bro space claiming that cold showers changed their life. "The internet is full of people who changed five things at once and attributed all the improvement to the one that sounds the coolest. FWL is the mathematical procedure for figuring out which change actually mattered. It is the antidote to every 'this one weird trick' claim you have ever seen."

### The Punchline Moment
After the numerical example matches to every decimal place, say: "Let me say that again. The coefficient you get from the full multiple regression -- with all the variables in at once -- is EXACTLY the same number, to infinite decimal places, as the coefficient you get from this three-step residualization. Not approximately. Not in the limit. EXACTLY. This is not an approximation. It is an identity. It is what 'controlling for' has ALWAYS meant, every time anyone has ever said it, in every paper you have ever read. And most of the people who said it did not know this."

### The Callback
"What are you actually controlling for?" becomes the recurring skeptical question. In the Conclusion: "Every time someone says 'after controlling for income, education, and age...' you now know they are saying 'after residualizing both sides against income, education, and age.' If that makes the claim sound less magical, good. It should."

### The Meme-able Takeaway
**"'Controlling for X' does not mean 'holding X constant.' It means removing X's fingerprints from both sides of the equation."**

---

## Section 12: Diagnostics Toolkit Summary

### The Opening Hook
"Here is your cockpit instrument panel." Project a real airplane cockpit photo with all gauges green. "All gauges green. Engines running. Altitude stable. Everything looks perfect." Beat. "Except the flight plan takes you to Pyongyang instead of Paris. The instruments do not check whether you are going to the right place. They check whether the plane is functioning. This is what diagnostics do for regression."

### The Punchline Moment
"In the tutoring example, VIF was low. Breusch-Pagan was non-significant. Robust standard errors barely changed. Residuals looked beautiful. Every gauge was green. And the estimate had the wrong sign. The plane was flying perfectly -- to the wrong destination."

### The Callback
"All gauges green, wrong destination" becomes the one-line summary of the entire course's message about diagnostics. In the final exam review: "If I could tattoo one sentence on your brain, it would be this: all gauges green does not mean you are going the right way."

### The Meme-able Takeaway
**"All diagnostics green does not mean the answer is right. It means the model is internally consistent. These are not the same thing."**

---

## Section 13: Theorem Map

### The Opening Hook
Do this as a "Previously on Regression Autopsy" TV recap, delivered in an actual dramatic voiceover style (the professor can ham this up):

"In Episode 1, you learned your coefficient was a liar -- self-discipline's ghost was inflating the studying effect. In Episode 2, you discovered your confidence interval was gaslighting you -- the noise was growing with the predictor. In Episode 3, you watched a seat number achieve p = 0.002 and questioned everything you knew about significance. In Episode 4, your linear model predicted a score of 132 on a 100-point exam and you realized the road was curvier than the ruler. In Episode 5, a degree-15 polynomial got an R-squared of 0.97 in training and negative in testing. In Episode 6, Pete Davidson broke your understanding of collider bias. In Episode 7, every diagnostic passed and the answer pointed the wrong way. In Episode 8, a kid who scored 69 gave you the redemption arc you needed. And in Episode 8.5, you learned that 'controlling for' means something very specific that most researchers cannot explain."

"Today: the recap episode. Let us see how all nine theorems connect."

### The Punchline Moment
Show the theorem map table, but after each row, flash the corresponding "disaster example" from that section. OVB: chocolate and Nobel Prizes. Heteroscedasticity: salary funnels. Significance: seat numbers. Specification: score of 132. Overfitting: seven-fingered AI hand. Collider bias: Pete Davidson. Lalonde: healthcare algorithm. RDD: the 69-vs-70 kid. FWL: cold showers.

"You now have nine different ways to ask 'is this regression lying to me?' and nine different tools to find out. That is what this course gave you."

### The Callback
Every callback from every previous section appears here. This is the payoff for the running gags. The professor can rapid-fire: "Are we at three beers? Is this a seat number? How many fingers does the hand have? Is this a Lalonde? What are you actually controlling for?"

### The Meme-able Takeaway
**"Nine ways your model can lie. Nine tools to catch it. One rule: never trust the output without interrogating the assumptions."**

---

## Section 14: Conclusion

### The Opening Hook
Return to the A-level algorithm from Section 1. Project the same BBC headline. "We started this course with an algorithm that decided half a million students' futures and was scrapped in 72 hours. You now have the vocabulary to say EXACTLY what went wrong."

Then walk through it: "The algorithm had omitted variable bias -- it used school-level averages instead of individual student ability. It had specification error -- it assumed linear relationships between prior results and predicted grades. It had bad controls -- it conditioned on school characteristics that were downstream of socioeconomic status. And no one ran the sensitivity analysis that would have revealed how fragile the estimates were. Every failure mode we studied was present. And no one checked."

### The Punchline Moment
"Here is the final twist. The algorithm was built by professional statisticians. They knew about OVB. They knew about specification error. They presumably knew about collider bias. And they still shipped it. Not because they were incompetent -- because they were under time pressure, working with imperfect data, and trusted the model's diagnostics. All gauges were green. The plane flew to the wrong destination. And half a million students paid the price."

Pause. "This is why you took this course. Not so you can pass an exam. So you can be the person in the room who says: 'Wait. Have we checked whether this is a Lalonde?'"

### The Callback
Every running gag gets its final appearance. The ghosts, the beers, the seat numbers, the seven fingers, the Lalonde, the cold showers -- one final rapid-fire montage of everything the students have learned, delivered as a greatest-hits reel.

### The Meme-able Takeaway
**"This does not mean you should stop using regression. It means you are finally ready to start."** (Already the closing line -- perfect. Do not change it. It is the mic drop.)

---

## Summary: The Five Running Gags

For continuity across all sections, here are the recurring callbacks that thread the entire course together:

| Gag | Introduced In | Used In |
|-----|--------------|---------|
| "The ghost in the regression" | Section 3 (OVB) | Sections 7, 8, 9, 14 |
| "Are we at three beers?" | Section 4 (Heteroscedasticity) | Any section mentioning SEs |
| "Is this a seat number?" | Section 5 (Significance) | Any section showing p-values |
| "Score of 132" / "seven fingers" | Sections 6-7 (Specification/Overfitting) | Any section about extrapolation |
| "Is this a Lalonde?" | Section 9 (Real World) | Sections 12, 13, 14 |

These five phrases give students a portable vocabulary for statistical skepticism that they can use long after the course ends.
