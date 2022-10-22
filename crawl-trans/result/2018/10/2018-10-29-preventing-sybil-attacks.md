# Preventing Sybil attacks
![](img/2018-10-29-preventing-sybil-attacks.002.png) 29 October 2018![](img/2018-10-29-preventing-sybil-attacks.002.png)[ Lars Brünjes](/en/blog/authors/lars-brunjes/page-1/)![](img/2018-10-29-preventing-sybil-attacks.003.png) 8 mins read

![Lars Brünjes](img/2018-10-29-preventing-sybil-attacks.004.png)[](/en/blog/authors/lars-brunjes/page-1/)
### [**Lars Brünjes**](/en/blog/authors/lars-brunjes/page-1/)
Education Director

Education

- ![](img/2018-10-29-preventing-sybil-attacks.005.png)[](mailto:lars.bruenjes@iohk.io "Email")
- ![](img/2018-10-29-preventing-sybil-attacks.006.png)[](https://www.linkedin.com/in/dr-lars-br%C3%BCnjes-1640993b "LinkedIn")
- ![](img/2018-10-29-preventing-sybil-attacks.007.png)[](https://twitter.com/LarsBrunjes "Twitter")
- ![](img/2018-10-29-preventing-sybil-attacks.008.png)[](https://github.com/brunjlar "GitHub")

![Preventing Sybil attacks](img/2018-10-29-preventing-sybil-attacks.009.jpeg)

Building on last week’s [post by Professor Aggelos Kiayias](/en/blog/stake-pools-in-cardano/ "Stake pools in Cardano, iohk.io"), IOHK’s chief scientist, I want to use this post to discuss another choice we made when [designing Cardano’s reward mechanism](https://arxiv.org/pdf/1807.11218.pdf "Reward Sharing Schemes for Stake Pools, arxiv.org"). The mechanism is designed to give an [incentive to stakeholders](https://www.youtube.com/watch?v=2pdkIXDU1no&list=PLFLTrdAG7xRbAqhF3Tg8BeAea7Ard-ttn "Incentive Paper Lecture Series (Part 1), youtube.com") to ‘do the right thing’ and participate in the protocol in a way that ensures its smooth, efficient and secure operation. As was explained last week, to ensure fairness and decentralization, the rewards mechanism follows three principles:

- Total rewards for a stake pool should be proportional to the size of the pool until the pool reaches saturation.
- Rewards inside a pool should be proportional to a pool member’s stake.
- Pool operators should get higher rewards for their efforts.

One necessary modification deals with pool performance. If a pool operator neglects his ‘duties’ and does not create the blocks he is supposed to create, the pool rewards will decrease accordingly.

Take the example of Alice and Bob who run pools of equal sizes. They are both elected as slot leaders with 100 slots each. Alice dutifully creates all 100 blocks in the 100 slots she leads, whereas Bob misses 20 slots and only creates 80 blocks. In this case, Alice’s pool will get full rewards, whereas Bob’s pool will get less. How much less exactly is controlled by a parameter.
## **The challenge**
In this post, I want to concentrate on another potential challenge to the Cardano principles and explain how we decided to overcome it. The challenge was mentioned at the end of last week’s post: *How do we prevent one person from creating dozens or even hundreds of small pools?*

Note that for very large stakeholders it is perfectly legitimate to split their stake into several pools to get a fair share of the rewards.
#### **An example of a Sybil attack**
Let’s assume that we are aiming for 100 pools and therefore cap rewards at 1%. Let us further assume that Alice holds a 3.6% stake. If Alice does not split her stake, she will only get 1% of total rewards. If, however, Alice splits her stake, putting 0.9% into four different pools, her reward from each pool will not be capped.

The challenge arises if a small but devious stakeholder is allowed to create a large number of pools (possibly under assumed identities). If he manages to attract people to these pools (for example by lying about his costs and promising high rewards to pool members), he might end up controlling a majority stake with very little personal stake in the system. How could this happen? 

Let’s imagine that there are about 100 legitimate, honest pools. If we didn’t guard against it, a malicious player could relatively cheaply create 100, 200 or even 500 pools under false names and claim low operational costs and a low profit margin. Many honest stakeholders would then be tempted to stop delegating to one of the 100 honest pools and instead delegate their stake to one of themalicious pools, which might outnumber the honest pools. As a consequence, the operator of those malicious pools would be selected slot leader for a majority of blocks and so gain control over the blockchain, opening it up to all kinds of mischief and criminal activities, such as double-spending attacks! He would, of course, have to pay for the operation of hundreds of nodes, but that cost pales in comparison with the cost of acquiring a majority stake by buying the majority of all the Ada in existence, which would be in the range of hundreds of millions to billions of dollars.

This would be disastrous because the security of a proof-of-stake system like Cardano relies on the idea that people with a lot of influence over the system should hold a lot of stake and therefore have every reason to help the system run smoothly.
## **Our solution**
This type of attack, where the attacker assumes many identities, is called a Sybil attack, named after the 1973 novel Sybil by Flora Rheta Schreiber about a woman suffering from multiple personality disorder.

How can we prevent Sybil attacks?

One idea might be to make pool registration very expensive. But to prevent attacks, such fees would need to be extremely high and would prevent honest people from creating legitimate pools. Such a hurdle would be bad for decentralization; we want to encourage members of our community to start their own pools and not hinder their entry! There does have to be a modest fee for the simple reason that each registration certificate has to be stored on the blockchain and will consume resources, which have to be paid for.

Our [game theoretical analysis](https://arxiv.org/pdf/1807.11218.pdf "Reward Sharing Schemes for Stake Pools, arxiv.org") led us to a different solution, one that won’t bar ‘small’ stakeholders from starting their own pools by burdening them with prohibitively high fees and a high financial risk.

*When registering a pool, the pool operator can decide to ‘pledge’ some of his personal stake to the pool. Pledging more will slightly increase the potential rewards of his pool.*

This means that pools whose operators have pledged a lot of stake will be a little bit more attractive. So, if an attacker wants to create dozens of pools, he will have to split his personal stake into many parts, making all of his many pools less attractive, thereby causing people to delegate to pools run by honest stakeholders instead.

In other words, an attacker who creates a large number of pools will have to spread himself too thinly. He can’t make all of his many pools attractive, because he has to split his stake into too many parts. Honest pool operators will bundle all their personal stake into their one pool, thus having a much better chance of attracting members.

The degree of influence a pool operator’s pledged stake has on pool rewards can be fine-tuned by a configurable parameter. Being a bunch of mathematicians with little imagination, we called this parameter ‘a0’. (A colleague suggested the Greek letter phi because it sounds like part of the nasty giant’s chant in Jack and the Beanstalk – ‘Fee-fo-fi-fum’ – and we’re trying to ward off harmful stake pool giants, but we’d be grateful to any member of the community who can come up with a good name!).

Setting a0 to zero would mean: ‘Pool rewards do not depend on the operator’s pledged stake.’ Picking a high value for a0 would result in a strong advantage for pool operators who pledge a lot of stake to their pools.

We have a classical trade-off here, between fairness and an even playing field on the one hand (a0 = 0) and security and Sybil-attack protection on the other hand (a0 is large).

To demonstrate the effect of a0, let’s look at the three graphs in Figure 1.

![](img/2018-10-29-preventing-sybil-attacks.010.png) 

Figure 1. How a pool operator’s pledged stake affects pool rewards.

In the graphs, we are aiming for ten pools, so rewards will be capped at 10%. The size of the pool stake is plotted on the horizontal axis and the vertical axis shows pool rewards. Each graph depicts three hypothetical pools, where the operators have pledged 0%, 5% and 8% respectively to their pools (the pledged amount is called s in the graphs).

The first graph uses a0 = 0, so the pledged stake has no influence on pool rewards, and the three pools behave in the same way: rewards keep climbing as the pool size grows until they are capped when the pool controls 10% of the stake.

In the second graph, we see the effect of a0 = 0.1. The three pools are still similar, especially for small sizes, but they are capped at slightly different values. Pools with more pledged stake enjoy slightly higher rewards when they grow bigger.

Finally, the third graph shows the effect of a0 = 0.5. It is similar to the second graph, but the differences between the three pools are more pronounced. We still have to choose a “good” value for a0. This choice will depend on quantities such as expected operational pool costs, total rewards and – most importantly – the desired level of security.

We will want to keep a0 as small as possible, while still guaranteeing high levels of security against Sybil attacks.

In any case, it is important to keep in mind that the introduction of a0 does not prevent ‘small’ stakeholders from running successful pools because somebody with a great idea can always reach out to the community, convince others and invite them to work together and pool resources to pledge to the pool. In the end, running a solid, reliable pool and working closely with the community will be more important than just owning a lot of stake.

We have also started thinking about replacing the dependency of rewards on the pool leader’s stake with a reputation system. This would allow people with little stake to make their pools more attractive by running their pools reliably and efficiently over a long period of time. This won’t be implemented in the first iteration, but is on the table for future versions of Cardano.

You might also like to read the IOHK technical report [‘Design Specification for Delegation and Incentives in Cardano’](https://hydra.iohk.io/build/790053/download/1/delegation_design_spec.pdf "Delegation Design Spec, iohk.io") for a broader, more detailed description of the system.

*On Monday, 5 November, IOHK will hold an AMA (Ask Me Anything) on staking in Cardano, where anyone will have the opportunity to put questions to the IOHK team. Details of the AMA will be announced soon.*

Artwork, [](https://creativecommons.org/licenses/by/4.0/ "Creative Commons")

![Creative Commons](img/2018-10-29-preventing-sybil-attacks.011.png)[](https://creativecommons.org/licenses/by/4.0/ "Creative Commons")[](http://www.beeple-crap.com)

[Mike Beeple](http://www.beeple-crap.com)
