---
title: External Validity
description: Understanding when model retraining won't work
date: 2026-01-14
tags: [machine learning, statistics] 
draft: False
---

Machine learning models often degrade soon after they are launched. From widely publicized failures, like [Google Flu Trends](https://en.wikipedia.org/wiki/Google_Flu_Trends) and [Zillow's $6 billion home-flipping foray](https://fortune.com/2022/06/02/zillow-6-billion-home-flipping-business-housing-market-fortune-500/), to less headline worthy cases such as accuracy dropping by [nearly 15 percent](https://proceedings.mlr.press/v97/recht19a/recht19a.pdf) in a replication study of the widely used ImageNet benchmark dataset, ML models often perform worse in the wild than practitioners hope.

Most ML textbooks offer simple advice: gather new data and retrain the model. However, this only works when models degrade because the relationship between the features and the target shift, but the features still contain enough information to predict the target well. For example, a higher resolution camera may change how pixel values relate to the existence of a hot dog in an image, but it doesn't change the underlying relationship between pixels and the image's content. 

Retraining a model with new data will not help if models degrade for other reasons -- reasons long studied in the social sciences, under the name of *external validity*, which explores the extent to which models or theories perform well on new data[^train-test]. Understanding threats to external validity can help us better understand how well our models may perform when deployed and give us a sense of what to do when they degrade.

A machine learning, or statistical, model can be broken up into at least the following parts, all of which may differ between model development and deployment[^egami-et]:
- Y: the target that we want to explain or predict. This could be real-estate prices in Zillow's case, or whether an email is spam.
- X: The measured features of the sample. This can be everything we would use to try to predict house prices in the Zillow example, the words in an email or the pixel values in an image. We typically hope this sample is representative of the population to which we want to deploy our model.
- C: The unmeasured context. These are variables that we don't, or can't, measure when we train our model. This could be something like a geographic region for house prices or a different period of time.
<!-- - T: The treatment. In experiments, or causal models, we often want to measure an intervention's impact. The treatment could be a vaccine, a longer-mortgage, or a school voucher. -->

Starting with the target, during training we may only be able to use proxies for what we hope to capture in the world. For spam classification, we need to come up with a definition of spam that matches what our users conceptualize as spam. For example, how should we label an email that comes from an old acquaintance pitching their startup? Similarly, political opinion polls ask respondents how they would vote if the election were today. Does this match how they actually vote? If our proxy doesn't match the outcome that the model is hoping to explain or predict, the model will not perform well in the world. Collecting more data won't help.

Moving to the sample, [Recht et al.](https://arxiv.org/abs/1902.10811) built new datasets closely matching the procedures to generate two popular ML benchmark datasets: CIFAR-10 and ImageNet. They then used a variety of models trained on the original datasets and found that they all did worse on the new data, with accuracy falling by 3-15 percent on CIFAR-10 and 11-15 percent on ImageNet. These large accuracy drops despite negligible differences in labeling, the authors argue, show that when the sample is even slightly different than the population where we want to deploy our model, we may see substantial degradation. Fortunately, in this case, gathering more data from the population and retraining our model typically improves it.

Finally, we have context validity to understand how well the model will travel to new geographies, or time periods. [Egami and Hartman](https://www.cambridge.org/core/journals/american-political-science-review/article/elements-of-external-validity-framework-design-and-analysis/2D0914404C84B3F169732FF1D5E39420) point out that we can think of context validity as being like sample validity, but for features that either don't change or for which we don't have data within our study. For example, a study that predicts user behavior based on 20-year-olds in Florida does not tell us directly how our model will perform on 30-year-olds in Colorado. The same thing occurs when we look to the future. [New technologies and new trends arise](https://journals.sagepub.com/doi/10.1177/20531680231187271) that didn't exist in our training datasets. For example, the impact of writing assistant tools on student performance was likely much different in 2020, when tools were limited to simple style and grammar suggestions, than after ChatGPT's launch, when students could offload most of the writing process to the chatbot. These technological changes can break relationships that we could have previously used to make predictions. When these relationships are broken, not just tweaked, gathering more data and retraining our model won't improve it. Instead, we need to rethink the model fundamentally.

Understanding different threats to external validity shows that simply gathering data and retraining a model only works in a minority of cases. If the way we define our target doesn't match what a model's end users care about, or if the world changes in ways that break relationships we used for prediction, simply collecting more data won't help.


## Footnotes

[^train-test]: Typically, ML researchers perform a "train/test split" to try to get a sense of how well their model will perform on new data. However, this test data is typically a random subset of the training data, meaning the test comes from the same distribution as the training set.

[^egami-et]: [Egami and Hartman](https://www.cambridge.org/core/journals/american-political-science-review/article/elements-of-external-validity-framework-design-and-analysis/2D0914404C84B3F169732FF1D5E39420) also point out the treatment as another dimension that may not travel well. For example, in an experiment we may be able to ensure the placebo group and the treatment group don't interfere with one another, but this may be more difficult when an intervention is scaled up. 

