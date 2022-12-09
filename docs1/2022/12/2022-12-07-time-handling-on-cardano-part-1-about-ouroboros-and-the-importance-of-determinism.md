# Time handling on Cardano, part 1. About Ouroboros and the importance of determinism
### **On-chain timekeeping is essential to ensure global consensus in a blockchain setting. This post explains how time is handled on Cardano** 
![](img/2022-12-07-time-handling-on-cardano-part-1-about-ouroboros-and-the-importance-of-determinism.002.png) 7 December 2022![](img/2022-12-07-time-handling-on-cardano-part-1-about-ouroboros-and-the-importance-of-determinism.002.png)[ Arnaud Bailly](/en/blog/authors/arnaud-bailly/page-1/)![](img/2022-12-07-time-handling-on-cardano-part-1-about-ouroboros-and-the-importance-of-determinism.003.png) 6 mins read

![Arnaud Bailly](img/2022-12-07-time-handling-on-cardano-part-1-about-ouroboros-and-the-importance-of-determinism.004.png)[](/en/blog/authors/arnaud-bailly/page-1/)
### [**Arnaud Bailly**](/en/blog/authors/arnaud-bailly/page-1/)
Technical Lead

Engineering

- ![](img/2022-12-07-time-handling-on-cardano-part-1-about-ouroboros-and-the-importance-of-determinism.005.png)[](mailto:arnaud.bailly@iohk.io "Email")
- ![](img/2022-12-07-time-handling-on-cardano-part-1-about-ouroboros-and-the-importance-of-determinism.006.png)[](https://linkedin.com/in/arnaudbailly "LinkedIn")
- ![](img/2022-12-07-time-handling-on-cardano-part-1-about-ouroboros-and-the-importance-of-determinism.007.png)[](https://twitter.com/dr_c0d3 "Twitter")
- ![](img/2022-12-07-time-handling-on-cardano-part-1-about-ouroboros-and-the-importance-of-determinism.008.png)[](https://github.com/abailly "GitHub")

![Time handling on Cardano, part 1. About Ouroboros and the importance of determinism](img/2022-12-07-time-handling-on-cardano-part-1-about-ouroboros-and-the-importance-of-determinism.009.jpeg)

*Image by Noor Younis.*

*This blog post is a collaborative effort carried out by Arnaud Bailly, Michael Peyton Jones, Sebastian Nagel, Polina Vinogradova, and Brian Bush.*

Time is necessarily relative to every participant in the blockchain system and is critically important to support and maintain the safety properties of the Ouroboros consensus protocol. Minted blocks are expected to be propagated to all nodes in the system in a timely manner, so time requires the construction of a globally acceptable representation for consensus to be reached.
## **Time-handling with Ouroboros**
Locally, a node computes the passing of time using a 'wall-clock' system. The code for this clock is complicated because the slot length can vary at a hard fork boundary, so the time must be computed carefully taking this into account.

The code performs four steps to get the currentSlot:

1. Waits for some delay corresponding to either the time left till the next slot, or an arbitrary 60s delay if the current slot is unknown, which happens when syncing
1. Gets current system time and translates it to a slot number according to slot length for the current era
1. If the new slot is greater than the previous one, it 'ticks' a new current slot
1. If the above is not true, it either waits a bit longer or reports an error if current time jumped too far back.

The local currentSlot is compared to the slot reported by the tip of the node's ledger. If the latter is older, it is ignored because this means that the node is synchronizing its state with the chain.

Since the slot length can change at a hard fork, consensus can only convert slots to time up to a fixed point in the future â€“ the 'stability window' â€“ in which no hard forks can happen. In practice, the stability window is essential as it provides a measure of time needed to guarantee transaction finality and chain state immutability. During the stability window, the network must produce at least *k* blocks, where *k* is the number of blocks after which the chain becomes immutable. The stability window can take up to 3*k*/f, which is 36 hours with current parameters, or roughly a day.
## **Current challenges**
There is a fundamental physical limitation to the speed at which information can travel: the speed of light. This implies that synchronizing time over a network of nodes **takes time.**

Network Time Protocol ([NTP](https://www.newyorker.com/tech/annals-of-technology/the-thorny-problem-of-keeping-the-internets-time)) exists to provide a synchronization mechanism, which addresses time limitations and measurement differences. On the other hand, NTP does not guarantee a monotonic increase: time can sometimes jump back and forth a few seconds or even hours. Existing systems providing accurate, precise, and reliable clocks at a global scale are *centralized*, like the global clock provided by [Spanner](https://research.google/pubs/pub39966/), for example.

Currently, on Cardano:

1. Network parameters are set in such a way that the granularity of observable time intervals (eg, block time) on the chain is 20s, which is equal to the slot length (1s) divided by the block coefficient f (the expected block frequency, 0.05). These parameters are unlikely to change in the short-term future.
1. These 20 seconds have been determined as the optimum budget to guarantee the protocol's safety, given the constraints to replicate new transactions and blocks across the network (300ms TCP delay across the globe, with thousands of nodes). While block throughput might be increased in the future, it's unlikely that it will reduce the granularity of observable on-chain time.
1. Transaction finality can be achieved in approximately one day, and *cannot* happen in *less* than a day, according to Ouroboros consensus design. Note that although a high level of confidence is already reached in a matter of minutes or hours, the probability of a block being ultimately discarded decreases exponentially with its depth and the number of nodes that have to adopt this block.

Finally, in the longer term, the current Ouroboros protocol is planned to be replaced with [**Ouroboros Chronos**](https://iohk.io/en/blog/posts/2021/10/27/ouroboros-chronos-provides-the-first-high-resilience-cryptographic-time-source-based-on-blockchain/). Ouroboros Chronos addresses the timekeeping challenges by providing the first high-resilience cryptographic time source based on blockchain technology.
## **The importance of determinism in a blockchain environment**
In the current context, determinism means that a given transaction has a 'fixed effect' on the ledger state. But it is important to distinguish between the concepts of *historical* and *prospective* determinism.

Blockchains are based on the principle of replicating a fixed sequence of transactions (grouped in blocks) to reach a consensus about the state of the world. All blockchains have *historical* determinism, meaning that transactions in the chain have a fixed effect, else the results of validating the chain would be non-deterministic, which would break consensus.

But few blockchains have *prospective* determinism, meaning that a transaction that has not yet been added to the chain does have a fixed effect (or won't apply). Cardano does feature prospective determinism (with the current exception of pointer addresses, which are proposed to be removed in this [CIP](https://github.com/cardano-foundation/CIPs/pull/374)). You can also find out more about [Cardano's transaction cost determinism here](https://docs.cardano.org/plutus/transaction-costs-determinism). 

On blockchains that do not have prospective determinism users cannot know how much gas fees they need to pay for transactions which then results in such users overpaying for transactions. The lack of prospective determinism is also why a risk exists that a transaction on such blockchains can fail while also consuming lots of gas.
### **The power of prospective determinism**
Prospective determinism is a very powerful feature of Cardano, for multiple reasons:

- Users know, ahead of time, what a transaction will do, so there are no surprises. This is particularly relevant for scripts because users know exactly:
  - how the scripts will behave, and
  - how much execution budget is needed.
- Proposed transactions can safely be processed in parallel. This parallelism is one of the reasons for Hydra's speed.
- Because users know in advance whether a transaction will fail or not, script failures can be punished harshly (because they will never happen to non-malicious users)
- Broadly, it makes interacting with, and evolving the blockchain easier and more predictable.

Prospective determinism of transactions requires that every part of transaction validation, including script execution, is completely deterministic. This is ultimately why Cardano cannot have non-deterministic operations in scripts.

One of the ways to get prospective determinism is by having the effect of a transaction be entirely determined by the transaction itself and the outputs it references. In the context of Cardano, this is called *locality*. Locality is also of great benefit for users since it means that anyone can know what a transaction does just by looking at the transaction.

*The second part of this blog post will discuss time-handling use cases on Cardano with Plutus, Marlowe, and Hydra.*
