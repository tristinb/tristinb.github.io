---
title: LLMs represent a win for utility theory
description: AI's success shows we don't need to encode heuristics and biases into agent based models
date: 2025-06-05
tags: [complexity, LLMs]
draft: False
---

Our political-economic system emerges from complex interactions among humans and firms. Since the 1970s, economists have mostly agreed that we cannot understand the system as a whole without some model of the individuals within that system. Both neoclassical and behavioral economists model these individuals as if they maximize a utility function. [Complexity economists](https://yalebooks.yale.edu/book/9780300283327/making-sense-of-chaos/) and [psychologists](https://global.oup.com/academic/product/simple-heuristics-that-make-us-smart-9780195143812) argue that instead we should model humans as following simple rules, or heuristics. They note that any realistic utility function would be extremely complex, context dependent and different across individuals, making the whole concept impractical. But the success of LLMs, like ChatGPT, shows that systems can, in fact, learn complicated, context-dependent utility functions that are tailorable to individual preferences, thereby supporting the utility function view. The rest of this post shows how utility maximization drives the LLMs we use today.

LLMs go through various training phases, the final of which, post-training, allows us to ask the model simple questions and receive natural-sounding responses. One post-training step, reinforcement learning from human feedback (RLHF), or with AI feedback (RLAIF), seeks to encode human stylistic and content preferences into the LLM.[^RLHF_BOOK] RLHF works by feeding a prompt to a language model and then having it output several different completions to the prompt. A labeler then notes which completion it prefers. With this labeled dataset, another LLM then learns to predict the labelers' preferences over the completions. Using reinforcement learning with the reward model, the base LLM learns to fine tune its responses.[^DPO]

Economists follow a similar formula when they try to estimate utility functions. They observe consumers choosing between various affordable items and then note which was purchased, or preferred. From data on many such transactions economists then fit a model, much smaller than an LLM, to estimate a utility function. Although focusing on surveys rather than behavior, Daniel Kahneman and Amos Tversky's experiments asked subjects questions such as whether they would prefer a coin flip that paid $120 for heads and nothing for tails versus a guaranteed $50. From these surveys they estimated utility functions that showed humans take larger risks to avoid losses than they would to make a similar-sized gain. This research won the Nobel prize.

Note the similarity between RLHF and Kahneman and Tversky's experiments: both methods first ask a human responder to label which of two outcomes they prefer, then estimate a utility function from this data. [Ethayarajh et al](https://arxiv.org/abs/2402.01306) dig into this connection, arguing that the best performing models implicitly use utility functions similar to those proposed by Kahneman and Tversky. They propose reward models directly based on Kahneman and Tversky-inspired utility functions.

Reward models show we can learn utility functions, but what about the problem of them changing across contexts and people? LLM-based reward models easily deal with even slight contextual shifts. During pretraining, the model learns that wine relates more closely with vineyard-related vocabulary than beer does. RLHF reinforces these relationships, as the model learns how the context of a prompt impacts the completions that labelers prefer.

Incorporating diverse human preferences presents a larger challenge. Training on just one reward model assumes we all have the same preferences. But even data labelers have different preferences, with different groups producing reward models with different predictions. Taking advantage of this variation in reward models, researchers recently released an [open source dataset](https://arxiv.org/abs/2409.20296) to build and evaluate new methods to build personalized LLMs. Companies like Netflix, Meta, and Amazon profited massively from personalized content. Doing the same with LLMs will likely drive similarly massive profits. Therefore, this problem is unlikely to persist.

RLHF's success shows that we can use data to estimate flexible utility functions that account for diverse contexts and preferences. Therefore, economists and others modeling complex systems can avoid encoding long lists of heuristics into their agents' behavior. Instead, they can supply data from which agents learn utility functions. Simulations of these more realistic agents interacting will teach us new lessons about how these complex adaptive systems evolve.

## Footnotes

[^RLHF]: See Nathan Lambert's recent [RLHF book](https://rlhfbook.com/) for a more detailed introduction.

[^DPO]: Direct policy optimization, part of the broader family of direct alignment algorithms, doesn't explicitly train a reward model or use reinforcement learning to update the LLM. But these are still done implicitly. The models still optimize the Bradley-Terry preference model.
