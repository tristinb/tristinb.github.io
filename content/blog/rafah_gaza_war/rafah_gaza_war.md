---
title: Can Biden Make Bibi Balk?
description: Applying game theory to Biden's attempt to halt Netanyahu's invasion Rafah
date: 2024-05-09
draft: False
tags: [international relations, game theory]
---

In the ongoing Israel-Gaza war, Biden recently told the press that he would cut off certain types of military aid to Israel if Netanyahu invaded Rafah. Netanyahu and his most hawkish advisors responded that Israel will do what it deems necessary to defend itself. This post applies a simple model to the current situation to better understand Biden's options and the dynamics in the dispute between Biden and Netanyahu.

## Model

We can model Israel's decision to invade Rafah as a Bayesian game. A key feature of Bayesian games is that a player can be a certain "type". For example, they can be sane or crazy, red or green, strong or weak, any number between 0 and 100 etc. In the model, players don't know the others' types, but they do know the probability distribution over the type. In this setup, we have two players: Biden (B) and Netanyahu (N). Biden's type is either strong or weak. Biden knows his type, but Netanyahu only knows the probability that Biden is either strong or weak.

Netanyahu can choose to either `Attack` or `Refrain`. If he chooses `Refrain`, the game ends, leaving Biden a payoff for convincing Netanyahu to refrain, $RB$, and Netanyahu a payoff for refraining, $RN$.

If Netanyahu chooses to attack, he will get a payoff of $K$. But if Biden chooses to Sanction Netanyahu, or to cut off military aid, that $K$ will come at a cost. Since that cost can be seen as coming from the US government, we assume it is the same regardless of Biden's type. If Biden chooses `Backdown` Israel won't pay a cost from the US reaction, so Netanyahu gets all of $K$ and Biden gets a payoff of $Bd$. 

The game is shown in the figure below. The left side of the tree represents the world where Biden is strong; the right side represents where Biden is weak. The dashed line means that Netanyahu, N, does not know whether he is in the world of Strong or Weak Biden.

{% image "./game_tree.png", "Game Tree" %}

You can see that the game has many undefined variables, or parameters. If they take on certain values, we can find a unique solution to the game. Here are the parameters we need to define:

<table>
<thead>
<th>Parameter</th><th>Description</th>
</thead>
<tr><td>$\theta$</td><td>Probability Biden's type is Strong</td></tr>
<tr><td>$RB$</td><td>B's payoff for N refraining </td></tr>
<tr><td>$RN$</td><td>N's payoff for refraining </td></tr>
<tr><td>$K$</td><td>N's payoff for attacking</td></tr>
<tr><td>cost</td><td>Cost from B's retaliation</td></tr>
<tr><td>$S_s$</td><td>Payoff to strong type for sanctioning</td></tr>
<tr><td>$S_w$</td><td>Payoff to weak type for sanctioning</td></tr>
<tr><td>$Bd$</td><td>Payoff for backing down</td></tr>
</table>

To find the subgame perfect Bayesian Nash equilibrium, we can start from the bottom of the tree and work our way up. First, let's start on the left, where Biden is the strong type. Since Strong Biden loves to fight, it is safe to assume his payoff for `Sanction` is larger than that for `Backdown`. Concretely, since ${S_s}$ is greater than $Bd$ strong Biden chooses `Sanction`. Furthermore, strong Biden seeks to impose a large cost on Israel for attacking, let's assume that $RN$ is greater than $K-{cost}$. In this case, Netanyahu gets a higher payoff, and therefore chooses, `Refrain`. Putting this together, under Strong Biden we get `Refrain` as an equilibrium as long as Biden's payoff for `Sanction` is greater than the payoff for `Backdown` and $K-{cost}$ is less than the payoff for `Refrain`. If either of these fail to hold, and we will revisit the second assumption later, we will get an equilibrium where Netanyahu attacks.

We can repeat this on the right hand side of the tree. Here, Weak Biden does not like conflict. Therefore, if Netanyahu attacks, Biden gets a higher payoff for `Backdown` than for `Sanction`. In the model this is expressed as $Bd$ being greater than ${S_w}$. Since Weak Biden will back down, Netanyahu will attacks and can expect a payoff of $K$. This is a reasonable assumption since if $K$ wasn't credibly better than refraining, Netanyahu wouldn't have threatened to attack in the first place. Putting this together, under Weak Biden we get an equilibrium where Netanyahu chooses `Attack` and Biden chooses `Backdown`. This is different than the equilibrium under Strong Biden. The table below shows the payoffs and Netanyahu's decisions under Biden's two types.

<table>
<tr><th>Strong</th><th>Weak</th><th>Payoff Strong</th><th>Payoff Weak</th></tr>
<tr><td>Refrain</td><td>Attack</td><td>$\theta \times {RN}$</td><td>$(1-\theta) \times K$</td></tr>
</table>

For a subgame perfect Bayesian Nash equilibrium to hold, Netanyahu will choose to `Refrain` if the expected payoff for restraining is greater than the expected payoff for attacking. In the model this is expressed as $\theta \times {RN} \geq (1-\theta)K$. Much of this depends on $\theta$, or Netanyahu's beliefs over Biden's type. Focusing on $\theta$, we can simplify this expression to $\theta \leq \frac{K}{({RN}+K)}$. This equation shows that as $K$ -- or the payoff Netanyahu gets from invading increases -- he needs to be even more convinced Biden is the strong type in order to refrain from attacking. Conversely, as $RN$, or the payoff he gets for refraining, increases he needs to be even less convinced Biden is of the strong type in order to refrain.[^foe]

In order to convince Netanyahu to refrain, and avoid an invasion of Rafah, the model suggests three things Biden could do. 

First, Biden could increase $RN$, which is Netenyahu's payoff for refraining. He could do this, for example, by offering more security guarantees or support in the United Nations. [Protection from ICC prosecution](https://www.axios.com/2024/04/29/netanyahu-biden-icc-arrest-warrants-war-crimes) could be another way to get Netanyahu to refrain. 
   
Second, Biden could try to convince Netanyahu that he is the strong type and that he will not back down from his threats. Biden going public with these threats suggests that private pressure have failed since going public will make it harder to choose `Backdown` because his domestic audiences will find him weak. A large literature on [Audience Costs](https://en.wikipedia.org/wiki/Audience_cost) explores these dynamics in detail.

Third, Biden could further escalate his threats. This would decrease the payoff Netanyahu gets by invading in the event that Biden is the strong type. In other words, Netanyahu can be relatively convinced Biden is the weak type, but still choose to refrain since the cost in the event Biden is the strong type are so large.

Finally, we can revisit the assumption that strong Biden can impose sufficiently strong sanctions to make Netanyahu's payoff for refraining greater than attacking. If strong Biden cannot credibly impose high enough costs to Netanyahu in the event that he attacks, for instance because he faces too many domestic constraints, then there is no equilibrium where Netanyahu chooses to refrain.

If you are interested in further exploring the three scenarios by manipulating $K$ and $RN$, you can click the button below.

<button id="toggle-button" onclick="toggleInteraction()">Explore Scenarios</button>

<div id="code">

By changing the values of $K$, the payoff Netanyahu gets from attacking, and $RN$, the value he gets from refraining, you can see what minimum belief Netanyahu must have over Biden being the strong type in order to refrain according to the model. 

<table>
<tr><th>Parameter</th><th>Value</th></tr>
<tr><td>$K$</td><td><input type="number" id="k" min="0" max="10" value="5" step="0.5" style="width: 100%;" onchange="calculateMinProb()"></td></tr>
<tr><td>$RN$</td><td><input type="number" id="rn" min="0" max="10" value="5" step="0.5" style="width: 100%;" onchange="calculateMinProb()"></td></tr>
<tr style="font-weight: bold;"><td>$\theta$</td><td id="theta">0.5</td>
</table>

By increasing $K$, or the value Netanyahu gets from attacking, $\theta$ will rise. This means that Netanyahu can be more certain that Biden is the strong type, yet still choose to attack since he gets such a high payoff for doing so. Conversely, increasing $RN$ will decrease $\theta$. This means that as the payoffs to refraining rise, Netanyahu can be more certain Biden is the weak type, yet still refrain.
</div>

## Footnotes

[^foe]: Formally if you take first derivatives you can see that the expression is increasing in $K$ and decreasing in $RN$. As both of the second derivatives are negative, as $K$ gets larger $\theta$ approaches 1; and as $RN$ gets smaller, $\theta$ approaches 0.

<script>

function toggleInteraction() {
    var code = document.getElementById("code");
    var button = document.getElementById("toggle-button");
    code.classList.toggle('active');

    var isVisible = code.classList.contains('active');
    var buttonText = isVisible ? 'Hide' : 'Explore Scenarios';
    button.textContent = buttonText
}

const calculateMinProb = () => {
    const k = parseFloat(document.getElementById("k").value);
    const rn = parseFloat(document.getElementById("rn").value);
    const theta =  k / (k + rn);
    document.getElementById("theta").textContent = parseFloat(theta.toFixed(4))
}
</script>