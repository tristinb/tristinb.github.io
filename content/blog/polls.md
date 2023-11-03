---
title: How Wrong are Polls?
description: Should we trust them? How wrong are they?
date: 2023-11-02
draft: false
---

With tiny response rates and a recent history of "missing" critical election results, the conventional wisdom is that polls can no longer be trusted. But can they? How should we interpret polls results in light of these failures?

## Background: Polling Fundamentals

Polls are often reported as being plus or minus three percent of the true value, with a 95 percent confidence interval. In English, this means that if we see a poll result that says 52 percent of the respondents prefer Brittany to Bill then we can be 95 percent confident that the true proportion of the population as a whole that prefers Brittany is somewhere between 49 and 55 percent.[^1] We can interpret "95 percent confident" as thinking that if we ran our poll a million times, only 5 percent of them, or 50 thousand, would be either less than 49 or greater than 55 percent.

You can run the following bit of python code to see this for yourself. The code assumes you ask 1000 people if they prefer candidate a or b. If they prefer candidate a, record a 1. Otherwise, record a 0. We assume the true proportion of the population that prefers candidate a is 54 percent.

```python
import numpy as np
population_pct=.54 # True value of the population
n = 1000 # poll 1000 people
test_draws = np.random.binomial(n, pop_pct, size=1_000_000)/n # sample from a binomial distribution
prop_outside_3_pct = np.sum(np.abs(test_draws-population_pct)>.03)/len(test_draws) # how many are outside 3%?
print(f'Proportion outside 3 percent: {prop_outside_3_pct: .2f}')
```
```text
Proportion outside 3 percent:  0.057
```

If you run the code you will see it is quite close to five percent. Notice, however, that it will not be exactly 5 percent. The standard error of the estimate (i.e. the proportion), depends on both the number of people you poll (n) and the true proportion of the population that supports candidate a.[^2] A sample size of 1000, however, generally gets pretty close to 3 percent when the true proportion of the population that supports a candidate is around 50 percent, and is easy to remember.

## Problem: We Can't Sample At Random

Although the above works great in theory, it relies on a key assumption that is often violated in practice: we draw our samples at random from the population. The problem is if certain segments of the population are systematically less likely to respond to a poll than others. 

If we knew, and could measure, the characteristic of this segment of the population that is unlikely to respond to a survey, then we can adjust our sample to account for it. However, imagine a case such as "people who are low trust are less likely to respond to a poll, and more likely to vote for candidate B". Things like low trust are difficult to measure directly and adjust for.

### Causes of Bias

Can we see this with an example? Now how many fall outside of 3 percent?

### Can 

Response bias: who responds to polls?

Historically, polls represented their results as being plus or minus three percent from the true value. Somewhat like the magical two percent inflation target, this was seen as sufficiently close to the true value to be seen as reasonably. 

The error rate comes from statistics, with the assumption that you are taking a perfectly random sample of the population. With 1000 people sampled at random, you have about a 95 percent chance of the true value coming within +/- 3 percent of the estimated value.

Election polling is systematically biased; averages don't work to cancel out errors

Things you cannot control for for a survey sample to be unbiased: did you just hear about x? People who watch the news more may be more likely to respond a certain way. Or a particular YouTube channel.
    - Do we want to capture this bias?

### Where is opinion likely to move?

We have messengers, and receivers. Receivers have opinion on a range of things, from individuals, to policies. Here demand effects may matter.

What are we likely to track?

How much bias can we expect in other areas? Can think of the costs/benefits of actually voting

Here we can run a simple simulation


[^1]: This is often phrased, the other way, something like "if we ran the poll an infinite number of times, 95 percent of them would come within 3 percent of the true value", implying we should trust that our poll is in the 95 percent of these cases. However, the true value being within plus or minus three percent of the sample value or the sample value being within plus or minus three percent of the true value are equivalent. You can see this with algebra: $$true \leq sample + .03 \iff sample \geq true - .03$$ $$true \geq sample - .03 \iff sample \leq true + .03 $$ The equations on the left hand side say that the true value will be within 3 percentage points of the sample value. The right hand side says the sample value will be within +/- 3 percent of the true value. These two statements are equivalent.

[^2]: We could calculate the value of N we would need for +/- 3 percent to cover 95 percent when the true value of the population is 0.54 as $$.03=1.96\sqrt{\frac{.54(1-.54)}{n}}$$ $$\sqrt{n} = \frac{1.96}{.03}\sqrt{0.2484}$$ $$ n = 1060.28 $$. If we set our sample size in the example above to 1061 we will see the number get closer to 0.05.