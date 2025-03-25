---
title: Bayes tells us absence of evidence is evidence of absence
date: 2025-03-24
tags: [bayes, probability, decision science] 
draft: false
---

Journalists from various outlets have spent the last few weeks pouring over more than two thousand newly declassified documents on John F. Kennedy's assassination. So far, no new evidence shows that anybody other than Lee Harvey Oswald was involved. We shouldn't be surprised -- more than 60 years of "no evidence" provides strong evidence for no government conspiracy. Often times, absence of evidence IS evidence of absence. 

We can show this with simple math, particularly with Bayes' rule. Our goal is to estimate probability that the government killed JFK. To be concrete, let's define our evidence as 60 years with no conviction. As background information, we can include everything else regarding our belief of the government's guilt, from how nefarious the government is, to motivations etc. 

From this information, all we need for our calculation is the following:

1) Our prior, or our belief that the government killed Kennedy. This is all of our background information *other* than 60+ years of no convictions. 

2) The likelihood of observing the evidence given the hypothesis is true. That is assuming the government did kill Kennedy, what is the probability we would see 60+ years without a conviction?

3) The likelihood of observing the evidence given the hypothesis is false. That is, assuming the government had nothing to do with the assassination, what is the probability we wouldn't see a government official convicted?[^bayes]

Now let's put these numbers into the table below. For (1) let's assume ignorance regarding the government killing Kennedy -- all our background information washes out -- and put our prior at 50-50. 

For (2) we start by assuming the government killed Kennedy. Given this assumption, what's the probability we would see no conviction after 60 years? Let's suppose the CIA is good at covering things up, but not perfect -- plenty of evidence exists on things like Bay of Pigs, Iran, Guatemala, etc. Furthermore, there have been several government investigations and independent reports. Some politician surely would have benefited from a smoking gun showing the government's involvement and more. In other words, many people have been looking for evidence, if it existed it's likely someone would have found it. Yet it is absent. But let's be conservative and put the probability of a JFK-murdering government *not* having a anyone convicted after 60+ years at 10 percent.

Finally, (3) asks us to consider the probability of no conviction given the government was *not* involved. This answer is straightforward -- if the government wasn't involved, we wouldn't expect to see much. We should provide an outside chance of someone planting evidence for fame and political points, but that is about it if we assume the government's innocent. So let's call this 99 percent.

The table below uses these probabilities to calculate our posterior belief that the government killed JFK.

<table>
<tr><th>Data</td><th>Description</th><th>Value</th></tr>
<tr><td>Prior</td><td>How probable is the hypothesis</td><td><input type="number" id="prior" min="0" max="1" value=".5" step=".05" onchange="calcProb()"></td></tr>
<tr><td>Prob(data | h=True)</td><td>How probable is the data if the hypothesis is true?</td><td><input type="number" id="lk_true" min="0" max="1" value=".1" step=".05" onchange="calcProb()"></td></tr>
<tr><td>Prob(data | h=false)</td><td>How probable is the data if the hypothesis is false?</td><td><input type="number" id="lk_false" min="0" max="1" value=".99" step=".05" onchange="calcProb()"></td></tr>
<tr style="font-weight: bold;"><td>Prob(h | h=true)</td><td>How probable is our hypothesis given the data?</td><td id="posterior"> 0.0917</td></tr>
</table>

The absence of a conviction over 60 years brings our prior belief of the government's guilt down from 50 percent to about 9 percent. You can see most of this shift in the ratio of (2) to (3), or the absence of evidence given the government being guilty compared with the absence of evidence given the government being innocent. The large number of people searching for evidence, yet finding none after 60+ years, leads us to put a low probability p(data | h=true). Conversely, an innocent government is consistent with us not finding much evidence, leading to a high probability on p(data | h=false). Therefore, the absence of evidence provides strong evidence that the government had nothing to do with the assassination, enough to bring our 50 percent belief down to 9 percent.

But absence of evidence may also mean nothing. For example, suppose I am searching for buried treasure in the mountains of Idaho with little more than a Reddit thread to guide me. Here the probability of me not finding the treasure, given my search material is high. By toggling the second row of the table above, you will see that the lack of treasure found on my search doesn't say much about whether the treasure exists.

## Footnotes

[^bayes]: Typically with Bayes rule the third factor is the probability of the evidence. But in this case that would just be the prior (1) times the likelihood (2) plus one minus the prior times (3).

<script>

const calcProb = () => {
    const prior = parseFloat(document.getElementById('prior').value);
    const lk_true = parseFloat(document.getElementById('lk_true').value);
    const lk_false = parseFloat(document.getElementById('lk_false').value);
    
    const num = prior*lk_true
    const denom = prior*lk_true + (1-prior)*lk_false
    if(denom==0){
        document.getElementById('posterior').textContent = 0
    }
    else {
    const prob = num/denom
    document.getElementById('posterior').textContent = parseFloat(prob.toFixed(2))
    
    }
    

}

</script>