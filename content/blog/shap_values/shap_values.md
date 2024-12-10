---
title: Shapley Values for Interpretable ML
date: 2024-12-09
draft: False
tags: [machine learning, game theory]
---

With machine learning (ML) impacting more and more of our daily lives interpretable ML is becoming more critical. Shapley values offer a method to explain why models make their predictions. But although Shapley values may shed some light onto an ML model's behavior, these values themselves lack an intuitive interpretation. This post goes over the game theory foundation of Shapley values, then shows how ML approaches are built on this foundation. It then shows why Shapley values tell us much less about our data and models than we may have hoped.

## Shapley values

Shapley values applied have their origin in cooperative game theory. Two driving questions of cooperative game theory are 1) what coalitions will form and 2) how will the coalitions divide their winnings. 

We can show this through a simple example of voting in a 100 member legislature that needs a simple majority to pass a rule. Suppose this legislature has four voting parties that always vote in unison. Party A has 40 members, B has 30 members, C and D each have 15 members. If parties come together to get a majority, they win $100 to split; those outside the coalition win $0. If A is in a winning coalition, how much of the $100 should they get? Party A's Shapley value would be a fair cut of the $100.

With a little bit of abstraction, let *i* represent any of the parties A, B, C, D. The intuition for calculating the Shapley value for party *i* goes as follows. First, the calculation only considers the grand coalition, or the coalition involving all 4 players. Then, we consider all possible orderings, or permutations, of this coalition. Each of these orderings has a point where party *i* enters the coalition -- 1st, 2nd, 3rd, or 4th in our example. With each of these orderings, we take difference in the coalition's value right before *i* entered and right after *i* entered. This difference tells us how much value *i* brought to that particular ordering. If we do this across all possible orderings and then take the average of these values, we will have player *i*'s Shapley value.

As an example, the table below shows how we can calculate the Shapley value for party A. Recall A has 40 votes, B has 30, while C and D each have 15 votes.

**Different Coalition Orderings for Party A**
| Position in the ordering | Example Coalitions | Value Before A | Value with A | Marginal Contribution |
|---------------:|----------------------------:|-----------------:|--------------:|---------------------:|
| 1 | {A,B,C,D} | 0 | 0 | 0 |
| 2 | {B,A,C,D}, {C,A,B,D} | 0 | 100 | 100 |
| 3 | {B,C,A,D}, {C,B,A,D} | 0 | 100 | 100 |
| 4 | {B,C,D,A}, {C,B,D,A} | 100 | 100 | 0 |

This table only shows some of the possible orderings. In total number of permutations here is 4!=24, with 6 possibilities for every position that A can enter. In 12 of these A's marginal contribution is 100; in 12 it is 0. Therefore, A's average marginal contribution across all coalitions, or its Shapley value is 50.

If we run Shapley values for other players we will notice that they are 16.67. This may seem odd: B has 30 votes, C and D each have 15. B could argue that they brought twice as much to the table as either C or D so they should be entitled to twice the reward. But without A, B would still need both C and D to get to 51 votes. In other words, despite having twice the number of votes C has, B can never add value where C can't. In the terms of game theory, B and C here are *interchangable* as they were both equally important to any coalition. 

These values don't directly line up to the number of votes each party provides. Party A's Shapley value is 50, although they bring 40 votes. As the table above showed, across all possible coalitions, Party A increased the grand coalition's payoff by 50, on average -- this is the amount of value, not votes, that party A brings. Similarly, Party B and C have a different number of votes, but the same Shapley value. This is, again, because both parties contributed the same amount on average to the full coalition's payoff. We know that parties B and C have a different number of votes, but we can't infer that from the Shapley values alone.

Similarly, If we remove A from the grand coalition, the payoff isn't 100 minus player A's Shapley value of 50. Instead, since the number of votes without A is 60, the coalition will still get 100. All the Shapley values really tell us here is that Party A is the most important member, while the other three are equally important.

## Shapley values in machine learning

Machine learning models take in a set of inputs (features), calculate a bunch of interactions between them and then output a prediction. Because of these interactions' complexity, these models are often called black-boxes. To understand why these black-boxes made their predictions, practitioners commonly use Shapley values.

Making the leap frm game theory to machine learning will be easier if we clarify a few definitions. 
  
 1) **The Coalition**: For ML, the coalition is defined as a single observation of input features. You can think of this as a row in a data frame.
 2) **The Payoff**: The coalition's payoff is defined as the difference between the model's prediction for the observed row (i.e. the coalition) and the average model prediction across all observations.
 3) **The Shapley value**: for each feature in each row is an estimate of how important that feature was for the deviation from the average prediction. A positive value means the feature pushed the prediction up, while a negative means it pushed it down.

To clarify the above definitions, if the a model's average prediction is 0.55 and the model's prediction for a particular row is .65, then the payoff for that row is 0.1. A Shapley value is then given to each feature in the row such that the sum of the values is to 0.1.

But now we have the problem of actually estimating this value from data. In our example above, when we calculated the Shapley value for party A, we had to consider all possible coalitions. In that example, the coalitions either offered all of their votes or zero votes, and we knew what would happen without them. 

We generally don't know how to set the other values, and zero often makes little sense. To overcome this, algorithms create synthetic -- fake -- observations. Assume we are calculating the Shapley value for Party A from the example above. But assume we have only data for each coalition over time, where the number of votes changes by year. A dataset could  look like the following:

**Party Votes by Year**
| Year | A | B | C | D | majority |
|-----:|--:|--:|--:|---:|----:|
| 1 | 40 | 30 | 15 | 15 | 1 |
| 2 | 25 | 25 | 25 | 25 | 1 |

We are going to try to estimate A's Shapley value in the first row. Suppose we are measuring the marginal effect of A entering the coalition after B. First, we take a random row from the the rest of the dataset. Let's assume that sample is row 2. We then need to create two synthetic rows of data and compare their differences in model output. 

The first synthetic row includes B and A from row 1 with C and D's values from row 2. The second synthetic row uses B's value from row 1 with the rest of the values from row 2. The table below shows these two examples.

**Synthetic Data**
| Coalition | A | B | C | D | majority |
|-----:|--:|--:|--:|---:|----:|
| A After B | 40 | 30 | 25 | 25 | 1 |
| B Only | 25 | 30 | 25 | 25 | 1 |

We would then pass each of these rows through our model and calculate the difference between them to get the marginal impact of A. We then repeat this many times to get an estimate for A and then do this again for all the Shapley values. 

But these synthetic values are often quite different than the data used to train the model. Notice that the sum of the votes in both rows exceeds 100. A model trained on real data would never see this in a 100 member legislature. However, ML models will likely extrapolate anyway and come up with some prediction, despite it not being based in reality. This prediction is then sensitive to how the model extrapolates. Taking advantage of synthetic examples being quite different than the observed data [Slack et al (2019)](https://arxiv.org/abs/1911.02508) built a model that heavily incorporated race and gender to make predictions, but by exploiting synthetic examples were able to output Shapley values for these features that suggested the model didn't find them to be important.

Therefore, since it isn't clear how to turn "off" a feature -- as we could do in our game theory example above -- most methods sample from the other rows of data. But these synthetic rows are often very different from the underlying data, making it difficult to accurately calculating the marginal impact of a feature.

## Can we take action based on Shapley Values?

Ultimately, Shapley values are typically used for predictive models, which seek to exploit correlations. Because of the model assumptions and the way the data is typically collected, they don't tell us anything about what would happen if we actually intervened and changed a variable. This isn't really the goal of the method. However, explaining a model typically asks what would happen if we changed a feature to a particular value.[^citations] But Shapley values don't tell us anything about this.

Going back to the very first example, we know that if we removed A from the coalition, we would lose 40 votes. But the Shapley value of 50 doesn't suggest that. Furthermore, if we removed B or C we would lose 30 and 15 votes, respectively, but both of these parties have the same Shapley value. In other words, Shapley values don't provide much guidance on what would happen if we intervened in a system. This fundamental problem exists on top of the computational associated with actually calculating them.

## Footnotes
[^approximation]: This assumes you can calculate the Shapley value exactly. Since this calculation is NP-Hard, these are typically approximated.
[^citations]: There is a huge amount of literature on this. The most accessible starting point is probably ([Pearl and Mackenzie 2018](https://www.amazon.com/Book-Why-Science-Cause-Effect/dp/046509760X))