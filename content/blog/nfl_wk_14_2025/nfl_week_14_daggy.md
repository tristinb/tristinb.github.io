---
title: Week 14 NFL Predictions, Daggy vs Kalshi
date: 2025-12-09
tags: [statistics, nfl, kalshi]
draft: False
---

Last Thursday, I asked Daggy to run a handful of models on basic NFL data, choose the best one, and predict Week 14 games. For a baseline, I compared the predictions with [Kalshi](https://kalshi.com/), an $11 billion prediction market that allows people in all 50 states to put money on NFL games.

Daggy not only got one more game correct than Kalshi, but also achieved a better Brier score (lower is better). The table below shows the predictions and result for each game. 

| Matchup | Winner | Daggy Prob | Kalshi Prob | Result |
|---------|--------|------------|-------------|---------|
| ARI vs LA | LA | 68.3% | 82% | Both ✓ |
| ATL vs SEA | SEA | 59.4% | 74% | Both ✓ |
| BAL vs PIT | PIT | 46.9% | 29% | Both ✗ |
| BUF vs CIN | BUF | 69.5% | 72% | Both ✓ |
| CLE vs TEN | TEN | 36.6% | 36% | Both ✗ |
| DET vs DAL | DET | 65.3% | 62% | Both ✓ |
| GB vs CHI | GB | 62.5% | 73% | Both ✓ |
| JAX vs IND | JAX | 50.3% | 47% | Daggy ✓ |
| KC vs HOU | HOU | 51.3% | 36% | Daggy ✓ |
| LAC vs PHI | LAC | 48.7% | 45% | Both ✗ |
| LV vs DEN | DEN | 72.5% | 80% | Both ✓ |
| MIN vs WAS | MIN | 40.5% | 48% | Both ✗ |
| NYJ vs MIA | MIA | 46.4% | 57% | Kalshi ✓ |
| TB vs NO | NO | 41.7% | 21% | Both ✗ |
| **TOTAL** | | **Daggy: 8/16** | **Kalshi: 7/16** | |
| **Brier Score** | | **0.22** | **0.24** | |

I was skeptical of these predictions when I posted them to LinkedIn last Thursday. Not only was the data simple, with nothing on injuries or weather conditions, but Claude, which interfaces with Daggy, also asked Daggy to drop data before 2024 despite having data going back to 2000. The best model of the three Daggy trained only had seven features. Overall, the whole modeling process took about ten minutes and Daggy made better week 14 predictions than a prediction market that harnessed the wisdom of the crowds. We will see if this holds in week 15.