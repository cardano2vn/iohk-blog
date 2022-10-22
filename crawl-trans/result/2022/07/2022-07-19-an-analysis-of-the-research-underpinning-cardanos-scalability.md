# An analysis of the research underpinning Cardano's scalability
### **Taking a closer look at IOG research, part 4. How layer 1 and layer 2 solutions create a faster and more resilient blockchain**
![](img/2022-07-19-an-analysis-of-the-research-underpinning-cardanos-scalability.002.png) 19 July 2022![](img/2022-07-19-an-analysis-of-the-research-underpinning-cardanos-scalability.002.png)[ Olga Hryniuk](/en/blog/authors/olga-hryniuk/page-1/)![](img/2022-07-19-an-analysis-of-the-research-underpinning-cardanos-scalability.003.png) 7 mins read

![Olga Hryniuk](img/2022-07-19-an-analysis-of-the-research-underpinning-cardanos-scalability.004.png)[](/en/blog/authors/olga-hryniuk/page-1/)
### [**Olga Hryniuk**](/en/blog/authors/olga-hryniuk/page-1/)
Technical Writer

Marketing & Communications

- ![](img/2022-07-19-an-analysis-of-the-research-underpinning-cardanos-scalability.005.png)[](https://www.linkedin.com/in/olga-hryniuk-1094a3160/ "LinkedIn")
- ![](img/2022-07-19-an-analysis-of-the-research-underpinning-cardanos-scalability.006.png)[](https://github.com/olgahryniuk "GitHub")

![An analysis of the research underpinning Cardano's scalability](img/2022-07-19-an-analysis-of-the-research-underpinning-cardanos-scalability.007.png)

Previous blog posts delved into the [foundational research](https://iohk.io/en/blog/posts/2022/06/10/cardanos-foundational-research-overview/) that enabled Cardanoâ€™s multi-functional ledger support for [expressive smart contracts](https://iohk.io/en/blog/posts/2022/06/23/overview-of-the-research-enabling-smart-contract-support-on-cardano/) and [native assets](https://iohk.io/en/blog/posts/2022/07/07/research-overview-part-3-tokens-stablecoins-and-fees/).

As part of the Basho development phase, Cardano is undergoing steady upgrades and optimizations for increased scalability and interoperability. The â€˜[How we are scaling Cardano in 2022](https://iohk.io/en/blog/posts/2022/01/14/how-we-re-scaling-cardano-in-2022/)â€™ post reflected on Cardanoâ€™s scalability goals, and also discussed [interoperability and the role of sidechains](https://iog.io/en/blog/posts/2022/04/28/interoperability-is-key-to-blockchain-growth/). This new post takes a closer look at the research that will enable these gradual enhancements.
## **Scaling Cardano**
Scalability is essential for a blockchain network to support an expanding user base, and ensure growth without sacrificing throughput.

Scaling a blockchain usually requires a combined approach with a diversity of solutions to suit every situation and project. For example:

- Layer 1 solutions: upgrades applied directly to the main-chain protocol. 
- Layer 2 solutions: additional chains (sidechains) or layer 2 solutions (ZK rollups) that boost main-chain performance. 
## **Layer 1 scalability solutions**
Pipelining and input endorsers are two on-chain solutions planned to be implemented on Cardano in 2022-2023. The paper detailing the research done on pipelining is not yet published, but here are some of the properties and rationale for the introduction of pipelining.

**Pipelining in Ouroboros**

To understand what pipelining is, letâ€™s first define the term *block propagation*. Block propagation means that block-producing nodes distribute information about new blocks across the network. 

Pipelining improves block propagation times. The goal is for blocks to be propagated to peers within five seconds. Pipelining enables this by giving nodes the ability to pre-notify their downstream peers of an incoming block, enabling the peer to pre-fetch the new block body. 

The research presents an idea to propagate block bodies before having fully validated them. This takes the block body validation work out of the critical path of block propagation and allows for the time spent on validation to be overlapped with sending the block to the next peer in the network. This reduces block propagation time, which further allows for block size increase or Plutus improvements among others. Consequently, the bigger the block, the more transactions and Plutus scripts it can carry, which also influences the blockchainâ€™s throughput. These upgrades are planned to be applied to Cardano during Vasil hard fork event.

**Input endorsers**

Implementation of input endorsers will also improve block propagation times and throughput. Input endorsers keep track of all submitted transactions and bundle these transactions into pre-constructed blocks. This means there are two sets of blocks, ones that contain the transactions and ones that achieve consensus. The blocks performing consensus will reference the pre-constructed blocks, which are constantly streamed without having to wait for consensus to be achieved. This will improve the consistency of block propagation times and allow higher transaction rates. 

John Woods, the former Director of Cardano Architecture at IOG, said:

Pipelining implementation is just great technology. Synthetic benchmarks show up to 40% efficiency gains. It's a great part of the story of how Cardano scales to meet demand in 2022. 2023 will see the dawn of [Ouroboros Leios](https://www.youtube.com/watch?v=xKv94MwSNBw) (input endorsers), which will be a game-changer. It is expected that input endorsers are going to scale Cardano for the next half decade.

**Tiered pricing**

Another research initiative by IOG scientists is the implementation of [tiered pricing](https://iohk.io/en/blog/posts/2021/11/26/network-traffic-and-tiered-pricing/). In the current system, all transactions are treated the same without the possibility to alter their priority by paying higher gas fees, for example. This approach works well as long as the network throughput is comparable to transaction processing demand. However, as the network usage increases, not all the transactions might be eventually included in the blockchain. The possibility of a denial of service (DoS) attack â€“ taking advantage of the fair transaction treatment to pass off malicious spam as legitimate transactions â€“ requires *additional* measures to support network healthiness.

Tiered pricing enables steady system performance in an agile way, and is especially relevant in preventing DoS attacks. The research proposes to maintain predictability, fairness, and cost-efficiency of Cardano transactions while mitigating the issues that could arise from greater network demand. The approach puts forth a novel transaction fee mechanism, where each block is partitioned into three â€˜tiersâ€™ (based on the use case). Each tier makes up a set percentage of the maximum block size and is designed for different types of transactions â€“ fair, balanced, and immediate. When the network is not busy, tiers default to the standard way of transaction prioritization.
## **Layer 2 scalability solutions**
To help scale a number of transactions that can be processed at once, a blockchain network can spin up a number of sidechains, introduce state channels, or apply a stake-based threshold multi-signature scheme, for example. 

**Sidechains**

The â€˜[Proof-of-Stake Sidechains](https://iohk.io/en/research/library/papers/proof-of-stake-sidechains/)â€™ paper was published in 2019. This paper provides the first formal definition of what a sidechain system is and how assets can be securely moved between sidechains.

IOG scientists put forth a security definition that augments the known transaction ledger properties of persistence and liveness to hold across multiple ledgers, and enhances them with a new â€˜firewallâ€™ security property. This safeguards each blockchain from its sidechains, limiting the impact of a potentially catastrophic sidechain failure. The paper also provides a sidechain construction that is suitable for proof-of-stake sidechain systems and is consistent with the Ouroboros consensus protocol. Such techniques as merged staking, cross-chain certification, and multi-signature usage are presented to ensure sidechainsâ€™ resilience to malicious attacks.

As a result of this research, IOG has developed the [Cardano EVM sidechain](https://iohk.io/en/blog/posts/2022/07/06/introducing-the-cardano-evm-sidechain/), which is currently in alpha version on testnet. It will be compatible with Ethereumâ€™s tools and libraries, allowing developers to create Solidity smart contracts, DApps, and ERC20 tokens on Cardano to gain from such benefits as cost-efficiency, scalability, and security.

**Hydra**

Besides sidechains, there are other solutions for improving network scalability. Hydra state channels, for example.

The research paper â€˜[Hydra: Fast Isomorphic State Channels](https://iohk.io/en/research/library/papers/hydra-fast-isomorphic-state-channels/)â€™ was published in 2021. The paper introduces Hydra â€“ an isomorphic multi-party state channel. State channels are an attractive layer 2 solution for improving the throughput and latency of blockchains. Hydra simplifies off-chain protocol and smart contract development by directly adopting the layer 1 smart contract system, in this way allowing the same code to be used both on- and off-chain. Taking advantage of the [EUTXO model](https://iohk.io/en/research/library/papers/the-extended-utxo-model/), the research suggests how to develop a fast off-chain protocol for the evolution of [Hydra Heads](https://iohk.io/en/blog/posts/2022/02/03/implementing-hydra-heads-the-first-step-towards-the-full-hydra-vision/), whose protocol is currently being implemented on Cardano.

**Mithril**

Finally, to achieve greater scalability, it is also important to streamline the speed and efficiency of data synchronization between applications. Addressing this, the IOG research team published the paper on â€˜[Mithril: Stake-based Threshold Multisignatures](https://iohk.io/en/research/library/papers/mithril-stake-based-threshold-multisignatures/)â€™ in 2021.

Efficient chain validation is essential to achieve greater scalability in a blockchain setting. This also depends on various messages signed by network validators. Mithril addresses the complexity of critical operations that depend logarithmically on the number of these participants. Given the time it takes to validate a particular message, and the resource usage during the validation phase of chain synchronization, Mithril provides a solution that makes multi-signature aggregation fast and efficient without compromising security features.

The paper reflects on how to retain strong security settings in multi-signature aggregation. As a result, Mithril can be applied for fast, efficient, and secure chain synchronization protocol. It is advantageous for secure voting, data exchange between sidechains, and data synchronization within light wallets. It is part of the Basho phase and will be implemented in 2022.
## **The final word**
There are currently [144 papers](https://iohk.io/en/research/library/) hosted in the IOG research library and this number is constantly growing. All the work has always and will further lay the foundation before any feature or upgrade is deployed on Cardano.

*In the coming months, weâ€™ll be reflecting more on the latest development and research taking place in regards to ledger optimizations, scalability improvements, and governance initiatives.*
