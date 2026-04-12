# Lecture Review: Regression Autopsy
**Reviewer:** Max, 3rd-year Mechanical Engineering, ETH Zurich
**Date:** April 2026
**Honesty level:** Brutal

---

## Overall First Impression

The title "Regression Autopsy: Eight Ways Your Model Is Lying to You" is genuinely good. It sounds like a YouTube video I might actually click on. But then you open the notes and it is 40+ pages of LaTeX with theorems, proofs, and matrix algebra. The title promises a crime show; the content delivers a textbook. That gap is the core problem.

---

## Section-by-Section Review

### Section 1: Introduction (Rating: 6/10)

The exam score setup is relatable -- I have taken exams, I have wondered if studying actually helps. Good start. The variable descriptions are clear, and I appreciate that each one gets a plain-language explanation.

**Where I zoned out:** The bullet point about U (self-discipline) goes on forever. The Instagram slider thing is a nice touch, but then it dives into "Because U affects both the treatment X1 and the outcome Y, it is a confounder." You just lost every non-stats person in the room. The word "confounder" appears with zero buildup. You defined it in the same sentence you used it, which is fine in a textbook, but in a lecture I would already be checking my phone.

**Where I was confused:** The variable X3 (self-assessed performance) -- you say "Including it as a control will backfire spectacularly (see Section 6)." OK but why even mention it here? You are front-loading a concept (collider bias) that I have zero context for. It feels like foreshadowing in a movie, except I did not sign up to watch all eight sequels.

### Section 2: The Data Generating Process (Rating: 4/10)

This is where you lost me.

**Where I zoned out:** The moment I saw six simultaneous structural equations (2.1 through 2.6), my brain shut off. I know you walk through each one afterwards, and the paragraph-by-paragraph explanations are actually decent. But the wall of equations hits first, and my instinct is "I will never need to memorize this." The Key Insight box titled "The Numbers Behind the Story" is a full page of parameter descriptions. I would skim this in 3 seconds and move on.

**Specific quote that lost me:**
> "$\varepsilon \sim \mathcal{N}(0, 0.5 \cdot |X_1|)$: the randomness in exam scores depends on how much you studied."

The plain English after the equation is good. The equation itself is a wall. In a lecture, I would see the equation on the slide and tune out before the explanation arrives.

**Where I was confused:** The causal graph (the TikZ diagram). I have never seen a "causal graph" before. Dashed nodes, solid arrows, labels like "gamma_1 = 0.5" -- I do not know what I am looking at. You never actually explain what a causal graph IS before showing one. You just drop it in a Remark and assume I know how to read it.

**What would help:** Start with the graph FIRST, explain what arrows mean in one sentence ("arrow from A to B means A causes B"), THEN show the equations as the math version of the picture.

### Section 3: Omitted Variable Bias (Rating: 7/10)

This is where the notes start getting good.

**Where I was engaged:** The Sunscreen Murder Mystery. "It seems like ice cream causes drownings." I actually laughed. This is the kind of example that sticks. I would remember this in the exam. More of this, please.

The studying/sleeping numerical example is excellent. Five students, a table, concrete numbers, and the OVB formula verified with actual arithmetic. I can follow this. I can reproduce this on paper. This is what I need for the exam.

**Where I zoned out:** The proof of Theorem 3.1. I see "plim" and "Cov(X1, beta_0 + beta_1 X_1 + ...)" and my eyes glaze over. I understand that the proof exists and that it is short, but I do not care WHY the formula works -- I care THAT it works and HOW to use it. In a lecture, this proof is a guaranteed phone break.

**Where I was confused:** The subsection "When OVB Cannot Be Signed" is two sentences long and extremely vague: "the sign of the total bias is indeterminate without knowledge of all omitted variables." OK, so what do I DO with that information? This feels like a throwaway paragraph that raises anxiety without resolving it.

The Collider Trap subsection within the OVB section is confusing because it introduces a massive new concept (colliders, paths, conditioning) inside what I thought was the omitted variable bias section. It deserves its own section. When I hit "Definition (Path and Collider)" I thought I had accidentally skipped ahead.

**The proof of Proposition 3.4 (Collider Bias):** This one actually has a punchline -- "Conditioning on the collider manufactured a negative association between X and U from nothing." That is a great line. But the matrix algebra before it is dense. Could you put the punchline FIRST?

### Section 4: Heteroscedasticity (Rating: 5/10)

**Where I was engaged:** The Drunk Darts story is perfect. "After three beers, darts are hitting the wall, the floor, and occasionally the bartender." I am paying attention now. The apartment rent remark is also good -- CHF 800-1000 for a studio vs CHF 3000-8000 for a big flat. That is real life. I have looked at apartments. I get it.

The folk wisdom box ("If you never buy a lottery ticket...") is surprisingly effective. It connects to something I already know intuitively.

**Where I zoned out:** The Sandwich Formula. The moment I see $(X^\top X)^{-1} X^\top \Omega X (X^\top X)^{-1}$, I am gone. I understand the metaphor (bread-meat-bread), but the actual matrix expression is something I would memorize the night before the exam and forget immediately after. The derivation/proof that follows is even worse -- it is a full page of matrix algebra that I will never read voluntarily.

**Where I was confused:** The Breusch-Pagan test subsection is surprisingly well-explained -- I appreciate the step-by-step logic and the "Why nR^2?" paragraph. But the contrast paragraph at the end ("Contrast with the t-statistic") felt like it was written for someone who already knows what a t-statistic is. You have not introduced t-statistics yet (that is Section 5). Why are you comparing to something I have not seen?

**Rating justification:** Good stories, but the ratio of "dense math I will never use" to "things I need to know for the exam" is too high.

### Section 5: Significance vs Effect Size (Rating: 8/10)

This is the best section in the notes.

**Where I was engaged:** The Seat Number story. "Seat number has absolutely zero effect on your exam score... Yet the p-value screams p = 0.002: highly significant!" This blew my mind a little. I have always assumed "significant" means "important." The fact that it does not is genuinely surprising and useful. I would actually tell my friends about this.

The Keyboard example (saving 0.1 seconds per email) is also great -- the table showing the same tiny effect becoming "significant" purely because n grows is very visual and very convincing.

**Where I zoned out:** The power formula. $\text{Power} \approx \Phi(|\beta_j| / (\sigma/\sqrt{n}) - z_{\alpha/2})$. I understand the concept of power from the surrounding text -- "probability of detecting a real effect" -- but the formula is just notation soup to me. I would skip it.

**What made this section work:** The examples do all the heavy lifting. The math is minimal and the stories are memorable. Every section should be like this one.

### Section 6: Specification Error (Rating: 6/10)

**Where I was engaged:** "The Straight Ruler on a Winding Road" is a solid analogy. The extrapolation example where a linear model predicts a score of 132.5 for 50 hours of studying is genuinely funny in an absurd way. "The linear model says you should be 500 feet in the air" -- good visual.

The diminishing returns table (Section 6.2) is clear and I can follow the arithmetic.

**Where I zoned out:** Theorem 5.1 (Linear Projection Under Misspecification). "$\beta^* = \arg\min E[(Y - X\beta)^2]$" -- I vaguely know what argmin means but this felt very abstract. The one-sentence explanation after ("best linear approximation to f(X)") should come BEFORE the theorem, not after.

### Section 7: Overfitting (Rating: 7/10)

**Where I was engaged:** The Three Dartboard Players is a great analogy for bias-variance. High bias = consistently wrong spot, high variance = all over the place, irreducible noise = wobbly wall. I get it. The table with degree vs training/test R^2 is devastating -- degree 15 gets R^2 = 0.97 in training and NEGATIVE in testing. That table alone teaches the entire concept.

The numerical example with three models and three training sets is excellent. Model C predicting -13 for one dataset is hilariously bad.

**Where I zoned out:** The bias-variance proof. I see "Let mu = E[f-hat(x_0)]" and I am out. The proof is short but I do not need it.

**Where I was confused:** Cross-validation is introduced very briefly. Three paragraphs, no numerical example. Every other concept gets a worked example with a table -- why not this one? I have heard of cross-validation but I do not actually know how to DO it from this description alone.

### Section 8: Endogeneity and Bad Controls (Rating: 7/10)

**Where I was engaged:** "Why Every Movie Star's Spouse Seems Boring" -- incredible title, great story. "By restricting your attention to a group defined by the outcome of the very thing you're studying, you manufactured a relationship from thin air." That is a clear, memorable explanation.

The Talent/Luck/Fame table is simple and devastating. Four types, one gets dropped, and suddenly Talent and Luck are negatively correlated. I can explain this to my non-stats friends.

**Where I was confused:** The instrumental variables subsection introduces a LOT of new machinery. Instruments, relevance, exclusion, first-stage F-statistic, weak instruments -- this is an entire lecture's worth of content crammed into two pages. The roommate example is good but I needed more time with it.

The IV formula $\hat{\beta}_{IV} = (Z^\top X)^{-1} Z^\top Y$ is stated without much buildup. You go from "here is the formula" to "here is a consistency proof" very fast.

### Section 9: The Real World (Rating: 6/10)

**Where I was engaged:** The tutoring example is devastating. "OLS says tutoring decreases scores by 3 points. Should you shut down the programme? Of course not." Strong opening.

**Where I zoned out:** The Cinelli-Hazlett framework and robustness values. This is too abstract for me. "The minimum strength of association measured in partial R^2 that an unobserved confounder would need..." -- I read this three times and I am still not sure I could explain it to someone.

### Section 10: Regression Discontinuity Design (Rating: 7/10)

**Where I was engaged:** "The Kid Who Scored 69 vs The Kid Who Scored 70." Immediately relatable. Every student knows the pain of being one point below a cutoff. The scholarship numerical example is clean and the arithmetic checks out.

**Where I was confused:** Bandwidth choice. "Optimal bandwidth selection methods (e.g., Imbens-Kalyanaraman or Calonico-Cattaneo-Titiunik)" -- you just threw five surnames at me and expected me to feel informed. I do not.

### Section 11: Frisch-Waugh-Lovell (Rating: 5/10)

**Where I was engaged:** The coaching/shoes story in the Toy Story box. The three steps are clear. "But wait, how can I subtract out the shoe effect if I haven't measured it yet? You HAVE measured it." That anticipated my exact question. Good teaching move.

**Where I zoned out:** The proof with the partitioned normal equations and $M_2 = I - X_2(X_2^\top X_2)^{-1}X_2^\top$. This is the densest piece of linear algebra in the entire document. I would not attempt to read this even the night before the exam.

**Where I was confused:** The "residual-maker matrix" $M_2$. What is a projection matrix? What does "projects orthogonally to the column space" mean? I took linear algebra two years ago and I have forgotten. A one-sentence reminder would help.

### Sections 12-13: Diagnostics and Theorem Map (Rating: 5/10)

The diagnostics table is useful as a reference sheet. I would print this on one page and bring it to the exam (if allowed). But I would not read it in a lecture.

The Theorem Map table is for the professor, not for me. "Generalisation Relationship" is not something I think about. I think about "what do I need to know for the exam."

### Conclusion (Rating: 6/10)

The final line is good: "This does not mean you should stop using regression. It means you are finally ready to start." That is a mic drop. But the eight-item numbered list before it is just a summary I would skim.

---

## What Is Missing (Things That Would Make Me WANT to Attend)

1. **Real failures with consequences.** You hint at this with the Lalonde dataset and the tutoring example, but I want MORE. Tell me about a time a bad regression led to a real-world disaster. A drug that got approved because someone ignored heteroscedasticity. A policy that failed because of omitted variable bias. Make it feel like these mistakes have stakes beyond a homework grade.

2. **A "cheat sheet" decision tree.** I want a flowchart: "Is your variable caused by the outcome? YES -> do not control for it. NO -> Is it correlated with your treatment? YES -> control for it. NO -> do not bother." Something I can actually use when I am staring at data at 2am.

3. **Competitions or challenges.** "Here is a dataset. Find the hidden bias. First team to identify it wins." I would pay attention for that.

4. **Shorter proofs or no proofs.** I know this is controversial, but I do not learn from proofs. I learn from examples. Every proof in these notes could be replaced with "the proof is in the appendix" and I would lose nothing. Put the proofs in an appendix for the students who care.

5. **Memes or visual humor.** The Toy Stories are the best part of the notes. They should be BIGGER, not boxed off to the side. Lead with the story, then do the math. Right now many sections lead with the math and use the story as seasoning.

6. **Code.** Show me a 5-line Python snippet that demonstrates each failure. I can run code. I cannot run a proof.

---

## Summary Ratings

| Section | Topic | Rating (1-10) |
|---------|-------|---------------|
| 1 | Introduction | 6 |
| 2 | Data Generating Process | 4 |
| 3 | Omitted Variable Bias | 7 |
| 4 | Heteroscedasticity | 5 |
| 5 | Significance vs Effect Size | 8 |
| 6 | Specification Error | 6 |
| 7 | Overfitting | 7 |
| 8 | Endogeneity & Bad Controls | 7 |
| 9 | The Real World | 6 |
| 10 | Regression Discontinuity | 7 |
| 11 | Frisch-Waugh-Lovell | 5 |
| 12-13 | Diagnostics & Theorem Map | 5 |
| 14 | Conclusion | 6 |

**Overall: 6/10.** The stories and numerical examples are genuinely good -- some of the best I have seen in a stats course. But they are buried under dense proofs and matrix algebra that I will never read. The notes try to be two things at once: an engaging narrative and a rigorous reference. For me, the narrative wins every time, and the rigor just gets in the way. If you separated the two -- stories and examples up front, proofs in an appendix -- these could be an 8 or 9.

---

*"I would attend the lecture for the Toy Stories. I would skip the proofs. I would study from the numerical examples the night before the exam. That is the honest truth."*
