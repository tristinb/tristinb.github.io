---
title: How Wrong are Polls?
description: This post asks to what extent we can actually trust polls.
date: 2023-11-01
draft: true
tags:
    - polls
    - woohoo
---

With tiny response rates and a recent history of "missing" critical election results, the conventional wisdom is that polls can no longer be trusted. But can they? How do random polls compare to new innovations, such as longitudinal panels employed by companies such as YouGov?

### What do we mean by "good polls"?

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

```python
import matplotlib.pyplot as plt
from scipy import stats

x = stats.binom(1000, .52).rvs()
```