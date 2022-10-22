# Cardano is secure against fake stake attacks
### **Peer-reviewed design means Ouroboros is free from a flaw affecting many proof-of-stake blockchains**
![](img/2019-01-29-cardano-is-secure-against-fake-stake-attacks.002.png) 29 January 2019![](img/2019-01-29-cardano-is-secure-against-fake-stake-attacks.002.png)[ Philipp Kant](/en/blog/authors/philipp-kant/page-1/)![](img/2019-01-29-cardano-is-secure-against-fake-stake-attacks.003.png) 6 mins read

![Philipp Kant](img/2019-01-29-cardano-is-secure-against-fake-stake-attacks.004.png)[](/en/blog/authors/philipp-kant/page-1/)
### [**Philipp Kant**](/en/blog/authors/philipp-kant/page-1/)
Formal Methods Director

Engineering

- ![](img/2019-01-29-cardano-is-secure-against-fake-stake-attacks.005.png)[](https://www.linkedin.com/in/dr-philipp-kant-4972b1a3 "LinkedIn")
- ![](img/2019-01-29-cardano-is-secure-against-fake-stake-attacks.006.png)[](https://twitter.com/philipp_kant "Twitter")
- ![](img/2019-01-29-cardano-is-secure-against-fake-stake-attacks.007.png)[](https://github.com/kantp "GitHub")

![Cardano is secure against fake stake attacks](img/2019-01-29-cardano-is-secure-against-fake-stake-attacks.008.jpeg)

Ada is not among the 26 cryptocurrencies identified by US researchers last week as being vulnerable to â€˜fake stakeâ€™ attacks.

[](#1)

1

The Cardano blockchain underlying Ada is based on proof-of-stake (PoS), but its Ouroboros protocol uses no bitcoin code and is not affected by the PoSv3 problem.

[](#2)

2

This is not just good luck, but a consequence of the thorough, formally-verified approach taken during Cardanoâ€™s development.
## **The vulnerability**
The vulnerability is explained very well in the original article. In order to understand why Cardano is not affected by it, we will summarise the essence of the vulnerability here.

All the vulnerable systems are using PoSv3, a modification of the bitcoin code that aims to replace hashing power with stake for the purpose of determining who is eligible to create a block. In the original bitcoin code, the decision of who gets to create the next block is based purely on hashing power: whoever manages to find a suitable random number, and thus get a correct hash first, wins. PoSv3, however, adds an additional variable, to simulate the notion of stake.

In a PoS system, the likelihood of getting to create a block is proportional to how much stake a user has in the system: the more stake a user has, the more likely it is that they get to create the next block. To mimic this functionality, PoSv3 allows users to add additional information to their candidate block, in the form of a â€˜staking transactionâ€™. The more tokens they have available to use in their staking transaction, the easier it becomes for them to get a correct hash, and thus earn the right to create the next block.

Whilst PoSv3 does successfully tie block creation rights to stake in this way, it also makes block validation more difficult. Not only does the hash of the block itself need to be verified (as in bitcoin), but so does a userâ€™s staking transaction: that is, did the user actually own the tokens they used in their staking transaction? To verify this information, a blockchain node has to be able to refer to the ledger, and â€“ if a block does not simply extend the current chain but introduces a fork â€“ also the history of the ledger. Since that is neither cached nor cheap to calculate, blocks in PoSv3 systems are not validated immediately, but are rather (at least partially) stored in memory or on disk when they pass some heuristics.

The vulnerabilities discussed in the original article can be exploited in a number of ways, but ultimately involve fooling those heuristics and presenting lots of invalid blocks to a node, such that the node runs out of memory and crashes before it can correctly identify that the blocks are invalid.
## **Why Cardano is different**
For Cardano, IOHK took a different approach. Instead of finding a minimal variation of bitcoin, we relied on world-leading academics and researchers to create a new protocol and codebase from scratch, with the requirement that it should provide equivalent (or better) security guarantees than bitcoin, but rely entirely on stake. The result is the Ouroboros protocol

[](#3)

3

, the first provably secure PoS protocol, upon which Cardano is built.

The basic design of Ouroboros is remarkably simple: time is divided into discrete increments, called slots, and slots are grouped into longer periods, called epochs. At the start of each epoch, a lottery determines who gets to create a block for every slot. Instead of this lottery being implicit, ie whoever gets a right hash first wins, the lottery is explicit: a generated random number determines a slot leader for each slot, and the chances of winning for any given slot are proportional to the stake one controls

[](#4)

4

.

In this protocol, validating that a block has been signed by the right stakeholder is also simple: it requires only the leader schedule for the current epoch (which will not change in case of a temporary fork), and the checking of a signature. This can and will be done by each node once they get the block header, in contrast to the PoSv3 systems that are vulnerable to fake stake attacks.

In short: Cardano is secure against fake stake attacks because itâ€™s based on a fundamentally different system. PoSv3 cryptocurrencies run on proof-of-work (PoW) systems, modified to take stake into account in the implicit leader election, and the vulnerability in question is a result of that modification, and the additional complexities it involves.

Not only does Cardano have a fundamentally different foundation, but that foundation is the result of multiple peer-reviewed academic papers, and an unprecedented collaboration between researchers and developers. The formal and semi-formal methods involved in creating the upcoming Shelley release of Cardano ensure that its construction at code level evidently matches the protocol described in the peer-reviewed research papers, building in reliability and security by design â€“ and avoiding the problems of PoSv3, which have arisen as a result of modifying an existing protocol instead of creating a thoroughly proven, bespoke protocol like Ouroboros.
### **Footnotes**
\1. â€˜[â€œFake Stakeâ€ attacks on chain-based Proof-of-Stake cryptocurrencies](https://medium.com/@dsl_uiuc/fake-stake-attacks-on-chain-based-proof-of-stake-cryptocurrencies-b8b05723f806)â€™ by Sanket Kanjalkar, Yunqi Li, Yuguang Chen, Joseph Kuo, and Andrew Miller of the Decentralized Systems Lab at the University of Illinois at Urbana-Champaign.[â†©](#f1)

\2. To be precise, the following discussion is targeted at the upcoming Shelley release of Cardano. The currently deployed Byron release is running in a federated setting, and thereby operationally protected from this kind of attack anyway.[â†©](#f2)

\3. There are by now a number of variations of the Ouroboros protocol. We describe only the classic version of Ouroboros here, but the general argument holds for all variants â€“ in particular for Ouroboros Praos, which will be the protocol used in the Shelley release.[â†©](#f3)

\4. To be precise, leader election for a given epoch uses the stake distribution at a point in time before the epoch starts, to prevent grinding attacks and a re-calculation of the schedule in case of a temporary fork at the epoch boundary.[â†©](#f4)

Artwork, [](https://creativecommons.org/licenses/by/4.0/ "Creative Commons")

![Creative Commons](img/2019-01-29-cardano-is-secure-against-fake-stake-attacks.009.png)[](https://creativecommons.org/licenses/by/4.0/ "Creative Commons")[](https://www.lusion.co)

[Edan Kwan](https://www.lusion.co)
