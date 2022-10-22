# Explaining the Shelley Incentivized Testnet incentive model
### **Learn about Cardano’s incentive model, rewards, and our plan for the Incentivized Testnet** 
![](img/2019-12-05-explaining-the-shelley-incentivized-testnet-incentive-model.002.png) 5 December 2019![](img/2019-12-05-explaining-the-shelley-incentivized-testnet-incentive-model.002.png)[ Kevin Hammond](/en/blog/authors/kevin-hammond/page-1/)![](img/2019-12-05-explaining-the-shelley-incentivized-testnet-incentive-model.003.png) 7 mins read

![Kevin Hammond](img/2019-12-05-explaining-the-shelley-incentivized-testnet-incentive-model.004.png)[](/en/blog/authors/kevin-hammond/page-1/)
### [**Kevin Hammond**](/en/blog/authors/kevin-hammond/page-1/)
Software Engineer

Engineering

- ![](img/2019-12-05-explaining-the-shelley-incentivized-testnet-incentive-model.005.png)[](https://twitter.com/inputoutputhk "Twitter")

![Explaining the Shelley Incentivized Testnet incentive model](img/2019-12-05-explaining-the-shelley-incentivized-testnet-incentive-model.006.jpeg)

We’ve talked a lot about incentives lately. That’s because right now we’re running the [Incentivized Testnet](https://staking.cardano.org/): a Shelley testnet that provides an opportunity for stakeholders to delegate their stake or operate a stake pool to earn real ada rewards. Later this month, anybody that had ada in either a Daedalus or Yoroi mainnet wallet during the balance snapshot (taken on November 29) will be able to participate in the Incentivized Testnet, as either a delegator or stake pool operator, or both. 

One of our key goals for the Incentivized Testnet is to test – in a real-world setting – the assumptions made in the [Ouroboros incentives whitepaper](https://arxiv.org/ftp/arxiv/papers/1807/1807.11218.pdf), which uses game theory to calculate the incentives required to ensure consistent, active, and strong participation within a blockchain network.

The foundation of Cardano is mathematics; its central pillar, however, is a philosophy aimed at creating a fairer, more transparent, and more equitable system, decentralized and globally distributed.
## **Why incentives matter**
Successful systems depend upon the adequate supply of incentives. Think of a company. A company must sufficiently incentivize its employees to work. This doesn’t just mean turning up to work – existing within the system – but performing a specific function to the desired standard. The same is true (and, arguably, is more crucial) for decentralized systems. Cardano is a decentralized network of global participants, each of whom must be adequately incentivized to take part and perform their roles, with the understanding that the network’s interests align with their own.
## **A brief overview of the incentives mechanism**
Cardano’s incentives model begins with an assumption of rationality: that each player will act to maximize their own returns. These returns are the system’s incentives, and can take the form of tangible rewards – such as money – or intangible rewards, such as esteem, reputation, status, identity, or fulfilment.

Selfless acts are rare. As individuals, we pursue strategies that reward us, directly or indirectly. A network of participants each acting out of self-interest, however, can lead to chaos. That’s why successful systems codify – in protocols, rules, or laws – when and how much each participant will be rewarded. One of the core principles of game theory is that an ideal system is one where a selfish participant, acting in their own best interests, is also, by design, acting in the best interests of the system.

This is the function of Ouroboros’ incentives mechanism: a set of instructions that specify how and when rewards are paid out, and in what proportions to reward different levels of stake contribution. It allows a distributed network of participants to coordinate and collaborate in a decentralized system and receive rewards in accordance with their self-interest, while still contributing to the long-term health of the network. 
## **Aims of Cardano’s incentive model**
Equality and fairness are key to the sustainability of any future system, but can only be assured by the system itself, independent of individual goals or self-interest. Individuals must be free to exercise their ingenuity and maximize their outcomes, as long as doing so does not impede the operation of the network or restrict the possibilities of another (for example, by gaining a disproportionate amount of control). If one participant is the winner every time, other participants are disincentivized and, eventually, disenfranchised. The final implementation of Cardano’s incentives mechanism, as outlined in the [incentives whitepaper](https://arxiv.org/ftp/arxiv/papers/1807/1807.11218.pdf), incorporates these factors, ensuring that that the biggest doesn’t always win, and that not only the richest get richer.

This is one of the aims of the game theory underpinning the incentives model – to test the thresholds and parameters for exploitation and the alignment of individual and collective interest – and is similarly one of the aims of the Incentivized Testnet. Over time, we will introduce new factors to the rewards calculation and monitor the impact on participant behavior.
## **Testing the incentive model**
The incentives model we’re introducing to the Incentivized Testnet is not the final model. We plan to use this phase to test the incentives model incrementally, verifying our assumptions and exploring whether the network and participants respond in the way we anticipate. 

We will not only be testing our game theory, however. We’ll also be testing the technology, ensuring that additional factors for reward calculations are only included once a baseline model is proven to be secure and stable.

In the beginning, various factors will not be included in the rewards calculation. These include factors to increase the number of stake pools and to better rank stake pools according to their desirability. Other factors will be included but in a limited capacity, and their function and calculation will evolve over time. This includes stake pool ranking. At first, the ranking will be based on a stake pool’s performance but, as we progress through the Incentivized Testnet, will transition to be based on desirability (a combination of cost, margin, pledged stake, and performance).

We’ll then gradually introduce additional factors into the rewards calculation, beginning with factors to encourage growth in the number of stake pools and to ensure the system promotes the most desirable stake pools. Each of these is important, and introducing them in a staged approach will allow us to ensure they function as intended and that each has the intended effect on the network.
## **Incentivized Testnet rewards**
The rewards for delegating stake or operating a stake pool on the Incentivized Testnet depend upon the percentage of network participation. An approximate 3.8 million ada will be awarded per epoch. If 50 percent of the network participates, then we estimate the annual return for delegation will be approximately 7 to 8 percent but could, if network participation is lower, be as high as 13-15 percent. These figures are subject to treasury taxes and stake pool fees. A rewards calculator is now available on the [Incentivized Testnet website](https://staking.cardano.org/) which, in addition to other variables, allows you to calculate approximate rewards relative to different levels of network participation. Here’s a sneak peek:

**Approximate delegation rewards calculation at 30% participation**

**Approximate delegation rewards calculation at 50% participation**

Meanwhile, for stake pool operators, the rewards for stake pool operation, assuming a pledged amount of 10,000,000 ada, a 10 dollar daily stake pool operating fee, 50 percent network participation in the Incentivized Testnet, and the operator margin set to 10 percent, the total return rate for stake pool delegation will be approximately 12 to 13 percent. We will be updating the calculator over time to include more sophisticated rewards calculation modelling.

**Approximate stake pool operation rewards calculation at 50% participation**
## **More coming soon**
This is a testnet, and as such involves an iterative process to reach our desired end: a complete and fully functioning incentives mechanism – as described in the Ouroboros whitepaper – that rewards network participants accurately and fairly in proportion to their contribution, while preventing any single actor from gaining a disproportionate amount of control over the network. We’ll be actively monitoring participant behavior throughout the testnet, to determine when and what additional factors may be included in the rewards calculation. 

To learn more about the Incentivized Testnet, [visit our website](https://staking.cardano.org/). If you’re interested in running a stake pool, [register your interest](https://forms.gle/JqPjdMkR58tzj4Mn6) and explore our [testnet website](https://testnet.iohkdev.io/en/) for step-by-step instructions. And, as always, follow us on [Twitter](https://twitter.com/inputoutputhk?lang=en) or [sign up to our email list](https://staking.cardano.org/) for the latest progress updates.
