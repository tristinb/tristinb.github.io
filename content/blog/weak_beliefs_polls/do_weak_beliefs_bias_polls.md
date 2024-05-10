---
title: Strength of Beliefs and Polls
description: What happens when people respond to surveys randomly?
date: 2023-11-19
draft: True
tags: [polls, beliefs]
---

[The previous post](/blog/polls/) explored how selection bias leads to problems in surveys and opinion polls. It assumed respondents had stable, or fixed, beliefs over whatever issue the pollster asked them. But what would happen to a survey's results if respondents had weaker beliefs, leading them to answer with whatever felt right in the moment? For example, consider a poll that resulted in 50 percent of the population favoring A to B. Does this represent half the population holding firm preferences for A and the other half with strong preferences for B? Or does this represent the full population being indifferent between A or B and basically choosing an option randomly? Would different compositions of the population add further bias or variance to a poll? Or does the composition not matter? The simulations below show that the strength of a belief, weak or strong, does not cause any additional problems to a poll.

Before delving into the consequences of weak or firm beliefs on polling results, it may help to clarify the definition of belief. David McRaney's *How Minds Change* looks at how conversations can change people's minds on prominent issues such as gay marriage and abortion. At the beginning of these discussions, interviewers often ask something along the lines of "on a scale of 1 to 100, how supportive are you of X"? Respondents rarely responded with a 1 or 100, instead even those with strong opinions tended to reply with something like "5" or "95" rather than 0 or 100. McRaney finds that although small, the area between 1 and 5 or between 95 and 100 creates some space for persuasion. What this means is that beliefs aren't all or nothing propositions; we don't often 100 percent believe or disbelieve something.

Because beliefs aren't typically fixed dichotomies, researchers define a belief as a probability distribution over all possible outcomes.[^bias_surveys] For example, if someone asks about the shape of the earth, we could exhaust all possible outcomes with {"flat", "spherical", "turtles", "something else"}. Each of us may then put a probability on each response. We could do the same with purely factual questions by asking, for example, what is capital of Brazil: {"Rio de Janeiro", "Sao Paulo", "Brasilia", "Another City"}. Some of us may have strong beliefs and put a probability of 1 on one of those outcomes, but someone with weaker beliefs may put 20 percent chance Rio and 80 percent chance Brasilia. If you asked this person 100 times what the capital of Brazil is, you would expect them to say Brasilia 80 times out of those 100 and Rio the other 20. Although this seems erratic, it is what we would expect by defining beliefs as a probability distribution.

This way of defining beliefs resolves a puzzle that public opinion researchers have noticed since at least the 1960s: people often change their opinion on issues sporadically. If you ask someone the same question at two different periods, especially on abstract questions such as the role of government in the economy, many give different responses in each period. This occurs despite little aggregate changes, as people shifting their opinion in one direction may be cancelled out by people shifting the other way.[^kinder_kalmoe] From this finding, much public opinion research, stemming prominently from Zaller's *Nature and Origin of Mass Opinion*, argues people's responses can be described as samples from a distribution over answers that they deem plausible.

But what would happen to a public opinion poll, or survey, if at least some people responded as if they were drawing their answer out of a hat? Would this randomness add any additional bias or noise compared to the case when respondents had much stronger beliefs?

The simulations below answers this question with three scenarios: 1) the population is split into two groups with fixed beliefs. That is, if you poll somebody they will always respond with the same answer 2) The population is split into two groups with strong beliefs. If you poll somebody they will usually respond with the same answer 3) The population is divided into three, two with strong beliefs and the other with weak beliefs, where the group with weak belief is responding as if they are flipping a marginally biased coin and answering accordingly.

To make this a bit more concrete, let's imagine in each scenario we are interested in preferences of TikTok vs YouTube. Given a probability over either TikTok and YouTube, we can adjust the composition of each group in each scenario to result in the survey showing 55 percent of the "population" favoring TikTok. In each scenario we will have 1,002 respondents per poll.

A summary of these scenarios, along with the respondents in each group's probability of choosing either TikTok or YouTube are in the tables below.

### Scenario 1: Always TikTok, Always YouTube
|       |    **Prob. TikTok**   |    **Prob. YouTube**     | **Number Respondents** |
|:-----|:-----------:|:-----------:|:---------------:|
| **Always TikTok** |     1     |     0     |       551       |
| **Always YouTube** |     0     |    1     |       451       |

### Scenario 2: Strong TikTok, Strong YouTube
|       |    **Prob. TikTok**   |    **Prob. YouTube**     | **Number Respondents** |
|:-----|:-----------:|:-----------:|:---------------:|
| **Strong TikTok** |     0.95     |     0.05     |       556       |
| **Strong YouTube** |     0.05     |     0.95     |       446       |

### Scenario 3: Strong TikTok, Strong YouTube, Weak TikTok
|       |    **Prob. TikTok**   |    **Prob. YouTube**     | **Number Respondents** |
|:-----|:-----------:|:-----------:|:---------------:|
| **Strong TikTok** |     0.95     |     0.05     |       334       |
| **Strong YouTube** |     0.05     |     0.95     |       334       |
| **Weak TikTok** |     0.65     |     0.35     |       334       |

The following code simulates surveys of the populations in each of the three scenarios. The figure below provides the results of the simulations from this code.

<div id="code">

```python
import numpy as np
from scipy import stats

strong_tt_prob = .95
strong_yt_prob = .95
weak_prob = .65
num_trials = 10_000
n = 1002

# Scenario 1
scen_1_dist = stats.binom(p=.55,n=n).rvs(num_trials)/n

# Scenario 2
## Sample from each group based on its population
scen_2_group_samps = stats.multinomial(n=n, p=[.556, 1-.556]).rvs(num_trials)
scen_2_p = [strong_tt_prob, 1-strong_yt_prob]
## Now "poll" thse who you sampled above based on their probabilities
scen_2_dist = stats.binom(p=scen_2_p,n=scen_2_group_samps).rvs().sum(axis=1)/n

# Scenario 3
## Sample from each group based on its population
scen_3_group_samps = stats.multinomial(n=n, p=[.33,.33,.33]).rvs(num_trials)
scen_3_p = [strong_tt_prob, 1-strong_yt_prob, weak_prob]
scen_3_dist = stats.binom(p=scen_3_p,n=group_samps).rvs().sum(axis=1)/n
```

</div>

<button id="toggle-button" onclick="toggleContent()">Show Code</button>


{% image "./weak_beliefs_polls.png", "Samples drawn from the above distribution"%}

The figure above shows the simulations are basically identical for every scenario. The mean in each is 55 percent preferring TikTok, as expected. In other words, the composition added no bias to the average response. Furthermore, in all three scenarios we see nearly the exact same spread around the mean. Therefore, the composition had no impact on the poll's variance.

Taken together, the strength of respondents' beliefs have no noticeable impact on the bias or variance of a poll. Since the composition of the population had no impact on the outcomes, we are unlikely to be able to determine the strength of beliefs from a handful of polls. As the three scenarios above show, there are many different ways for a poll to result in 55 percent of the population claiming that they prefer TikTok to YouTube.

However, a poll is just a snapshot; the public's underlying beliefs change over time. We may suspect that those with weaker beliefs are more apt to shift their support for one outcome or another than those with stronger beliefs. In scenario 3 above, imagine that YouTube launched a dreamy new feature that diminished the uncertain group's preference for TikTok from 65 percent to 45 percent. This shifts our poll above to show around 48 percent preferring TikTok and 52 percent favoring YouTube. This marks a substantial change driven by the one segment with weak beliefs. In other words, breaking news or other events may appear to impact aggregate survey results simply by shifting the underlying probability distribution of an already uncertain group of respondents.[^swing_voters] Given this group has weaker beliefs, it is not unreasonable to expect further news to lead to shifts back in the other direction.

## Footnotes

[^bias_surveys]: Bullock, John G., and Gabriel Lenz. "Partisan bias in surveys." Annual Review of Political Science 22 (2019): 325-342.

[^kinder_kalmoe]: Kinder, Donald R., and Nathan P. Kalmoe. Neither liberal nor conservative: Ideological innocence in the American public. University of Chicago Press, 2017.

[^swing_voters]: Poll aggregates may also change because news events cause partisans -- or those with stronger beliefs -- to become more eager to answer public opinion polls, see: Gelman, Andrew, Sharad Goel, Douglas Rivers, and David Rothschild. "The mythical swing voter." Quarterly Journal of Political Science 11, no. 1 (2016): 103-130.
