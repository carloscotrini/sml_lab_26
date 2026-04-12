# Engagement Review -- Sofia (3rd-year Mechanical Engineering)

**Overall vibe:** These notes are genuinely better than 90% of the stats material I have read at ETH. The "Toy Story" boxes are doing heavy lifting. But there are stretches where I would absolutely zone out and start scrolling Instagram. Below is my honest, section-by-section breakdown.

---

## 1. What Would I Tell My Friends at Dinner?

### Things I would DEFINITELY bring up

- **"Ice cream causes drowning."** (Section 3, Sunscreen Murder Mystery.) I literally texted my flatmate about this while reading. It is the perfect cocktail-party fact. Everyone thinks they are too smart to fall for a spurious correlation, and then you hit them with the formula that shows exactly how much bias you get. Chef's kiss.

- **"Seat number predicts your grade -- with p < 0.002."** (Section 5, The Seat Number story.) This one made me actually laugh. I would 100% bring this up the next time someone waves a p-value at me. The idea that you can make ANYTHING significant if you just collect enough data is the kind of thing that makes you feel like you unlocked a cheat code for understanding the news.

- **"Famous people's spouses seem boring, and it is a MATH thing."** (Section 6, collider bias / movie star spouse story.) OK this is the one. This is the one I would not shut up about. It is basically the statistical version of "why does every hot person date someone mid?" I would tell this at dinner, at brunch, at the gym. You could literally build an entire TikTok around this.

- **"A tutoring program that WORKS looks like it HURTS in the data."** (Section 7, Lalonde / tutoring analog.) This is genuinely unsettling. The fact that every diagnostic passes and the answer still has the wrong sign? That is a horror movie for anyone who trusts data. I would bring this up whenever someone says "the data speaks for itself."

### Things I would NOT mention (because I forgot them 30 seconds after reading)

- The entire Breusch-Pagan test derivation (Section 4.4). I know it is important. I do not care. My eyes slid off it like water off a raincoat.
- The formal proof of the sandwich variance formula. I read it, I followed the algebra, I retained nothing.
- The Theorem Map (Section 10). It reads like a course admin document, not something that makes me think.

---

## 2. Where Do the Notes Come ALIVE?

These are the specific moments where I stopped multitasking and actually paid attention:

1. **The Instagram slider for self-discipline** (Section 1.1). Brilliant framing. Every ETH student has done an Instagram story poll. Making the hidden confounder something that lives on Instagram's servers -- not in the university system -- makes it immediately real. I can picture it.

2. **"Drunk Darts"** (Section 4). The image of darts hitting the bartender after three beers is vivid and funny. It makes heteroscedasticity feel like something that happens to you on a Friday night, not a property of a covariance matrix.

3. **The kid who scored 69 vs. the kid who scored 70** (Section 8, RDD). Everyone has been that kid. Everyone has been one point away from something that mattered. This framing makes the entire RDD concept feel personal and high-stakes.

4. **The keyboard that saves 0.1 seconds** (Section 5). This is a perfect "so what?" killer. You watch the t-statistic climb from "not significant" to "HIGHLY SIGNIFICANT" while the actual effect stays at one-tenth of a second. It makes the whole concept click.

5. **The coaching vs. new shoes story** (Section 9, FWL). Extremely relatable. Anyone who has ever tried to get fit has wondered "is it the trainer or is it the protein powder?" Making FWL about isolating the real cause of improvement is genius.

---

## 3. Where Do the Notes DIE?

### Section 2: The Data Generating Process (lines 177-336)

**Problem:** This section is necessary but it reads like a technical manual. After the engaging intro, you hit a wall of structural equations. The "plain language" walkthroughs help, but there are too many of them back-to-back. By the time I reached the pathologies list, I was skimming.

**What would fix it:** Lead with a single provocative claim. Something like: "We are about to build a fake university where we know everything -- every student's secret discipline score, every lucky break on the exam. In the real world, God has the DGP and you do not. For the next 40 pages, you get to be God." That framing makes the DGP feel like a superpower, not a chore.

### Section 4.4: The Breusch-Pagan Test (lines 624-655)

**Problem:** The test itself is fine, but the explanation of "why nR^2" and the contrast with the t-statistic feel like they belong in an appendix. I understand that the professor wants completeness, but this is where I would open a new browser tab.

**What would fix it:** Cut the "why nR^2" paragraph to two sentences. Add a one-liner like: "If you regress your prediction errors on your predictors and get a decent R-squared, your errors are not random -- they are following a pattern. That pattern is heteroscedasticity."

### Section 4.5: Proof of the Sandwich Estimator (lines 669-683)

**Problem:** Pure algebra. Correct, clear, and absolutely dead on arrival for engagement. Nobody is going to tell their friends about a matrix derivation.

**What would fix it:** Keep it for the hardcore readers but put a visible "skip to the punchline" note. The punchline is: "Each observation gets to vouch for its own noise level, instead of forcing everyone to share the same estimate."

### Section 10: Theorem Map (lines 1505-1536)

**Problem:** This reads like a table of contents with extra steps. It is useful for revision but has zero narrative energy.

**What would fix it:** Frame it as a "Previously on Regression Autopsy" TV-recap. "In Episode 1, you learned your coefficient was a liar. In Episode 2, you discovered your confidence interval was gaslighting you. In Episode 3..." This makes the connections feel like a story arc, not a syllabus.

---

## 4. Real-World Hooks That Are MISSING

| Section | What is missing | Specific suggestion |
|---------|----------------|---------------------|
| **1. Intro** | No pop-culture hook at the top. The exam-score framing is fine but safe. | Open with: "In 2020, an algorithm decided A-level grades for half a million UK students. It was a regression model. It was catastrophically wrong. This course is about why." The UK A-level grading scandal is perfect -- it is real, recent-ish, and enraging. |
| **2. DGP** | The Instagram slider is great but it is the only cultural reference. | Add a reference to "that one friend who posts their Notion study schedule on their story but somehow still fails." Everyone knows that person. It makes the gap between self-reported discipline (U) and actual discipline visceral. |
| **3. OVB** | The ice cream/drowning example is classic but overused. Every stats course uses it. | Swap in or add: "People who own horses live longer. Does buying a horse make you immortal? No -- wealthy people buy horses AND have better healthcare." Or: "Countries that eat more chocolate win more Nobel Prizes." Both are real published correlations. |
| **4. Heteroscedasticity** | The apartment rent example is good but very Zurich-specific. | Add: "Startup salaries. Junior devs all make roughly 80-90K. Senior engineers? Anywhere from 120K to 900K depending on equity, company stage, and negotiation skill. The spread fans out with seniority -- that is heteroscedasticity in your LinkedIn feed." |
| **5. Significance** | The seat number story is perfect. But there is no mention of the replication crisis, which is THE real-world consequence. | Add one paragraph: "This is why psychology had a replication crisis. Researchers ran studies on hundreds of thousands of participants and found 'significant' effects of power posing, ego depletion, and social priming -- effects so small they evaporated the moment someone tried to replicate them. The p-value said 'real.' The effect size said 'who cares.'" |
| **6. Causation / Colliders** | The movie-star spouse example is amazing. But you could go harder. | Add the Pete Davidson example. "Why did everyone on Twitter ask 'how does Pete Davidson date all these women?' He is famous (collider). Among famous comedians, being very funny means you do not also need to be conventionally attractive. Pete is funny AND famous, so people expect him to also be a model. That expectation is collider bias." This would go VIRAL in a lecture hall. |
| **7. Real World** | The Lalonde dataset is important but feels academic. | Tie it to something students care about: "Imagine ETH publishes a study showing that students who use the free tutoring center have LOWER grades. Should they shut it down? This is exactly the Lalonde problem, and the answer is no -- the students who seek tutoring are the ones who are already struggling." (You already have this! But bury the Lalonde name and lead with the ETH framing.) |
| **8. RDD** | The scholarship cutoff is clean but feels like a textbook. | Add: "This is how researchers figured out that winning the lottery does not make you happier long-term, that being elected mayor does not make you richer, and that barely getting into a selective school does not improve your career. Every 'just barely' comparison is an RDD waiting to happen." Give students a mental model for spotting RDDs in the wild. |
| **9. FWL** | The coaching/shoes story is good but could be stickier. | Alternative or addition: "Your friend claims cold showers made her more productive. But she also started meditating and quit social media at the same time. FWL is how you figure out which change actually did the work." Cold showers are a meme in the productivity-bro space; students will laugh. |

---

## 5. The "Wow Factor" Test -- Would I Tell My Friends?

| Section | Title | Rating (1-10) | One-line verdict |
|---------|-------|:---:|-----------------|
| 1 | Introduction | 6 | Solid setup, but no single "oh wow" moment. Needs a punchier opening hook. |
| 2 | Data Generating Process | 4 | Necessary but dry. The Instagram slider saves it from a 3. |
| 3 | Omitted Variable Bias | 8 | The Sunscreen Murder Mystery carries this section. The numerical example is satisfying. |
| 4 | Heteroscedasticity | 7 | Drunk Darts is memorable. The Zurich apartment remark is nice. Loses steam in the BP test and sandwich proof. |
| 5 | Significance vs. Effect Size | 9 | The seat number story is a 10. The keyboard example is a 10. The multiple testing section is solid. This is the section I would screenshot and post on my story. |
| 6 | Specification Error | 6 | The Straight Ruler metaphor is decent. The "score over 100" moment is good. But overall this section feels more like problem-solving than storytelling. |
| 7 | Overfitting | 7 | The Three Dartboard Players is a solid metaphor. The degree-15 polynomial table is a great "oh no" moment. |
| 8 | Causation / Bad Controls | 9 | The movie star spouse story alone makes this a 9. The fame/talent/luck table is elegant. The tutoring twist is genuinely upsetting in a good way. |
| 9 | FWL | 7 | The coaching/shoes story is clear and relatable. The numerical example is one of the best in the notes -- you can actually follow every step. |
| 10 | RDD | 8 | The 69-vs-70 kid is universally relatable. The scholarship example is clean. This section feels like hope after all the doom. |
| 11 | Diagnostics Summary | 3 | This is a reference table. Important, not interesting. Nobody tells their friends about diagnostic tables. |
| 12 | Theorem Map | 3 | Same issue. Useful for studying, not for engagement. |
| 13 | Conclusion | 7 | The closing line ("This does not mean you should stop using regression. It means you are finally ready to start.") is genuinely good. I would put that on a sticker. |

**Overall average: 6.5 / 10**

---

## Summary: Three Things That Would Make This a 9/10

1. **Open with a real disaster.** The UK A-level algorithm scandal, the Amazon hiring algorithm that was biased against women, or the healthcare algorithm that deprioritized Black patients. Start with stakes. Make the reader think "oh no, this matters" before they see a single equation.

2. **Add one pop-culture example per section.** You already have the movie star spouse story and drunk darts. Do this for EVERY section. The Pete Davidson collider example alone would make students remember collider bias for the rest of their lives. The replication crisis would make the significance section feel urgent. Each example costs you one paragraph and buys you an entire section's worth of engagement.

3. **Create "skip to the punchline" signposts before every proof.** I am not saying remove the proofs -- they belong in lecture notes. But put a bold one-sentence summary before each proof so that readers like me can grab the intuition and decide whether to dive into the algebra. The students who want the math will still read it. The students who need the story will not lose the thread.

These notes are already in the top tier of anything I have read at ETH. The Toy Story boxes, the numerical examples, and the visualization specs show that someone genuinely thought about how students learn. With the hooks above, this could be the lecture that students talk about at Mensa for the rest of the semester.
