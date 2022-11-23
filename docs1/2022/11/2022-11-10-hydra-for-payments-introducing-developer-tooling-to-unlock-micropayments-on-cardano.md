# Hydra for Payments – introducing developer tooling to unlock micropayments on Cardano
### **A guest blog post by the Obsidian Systems Hydra team**
![](img/2022-11-10-hydra-for-payments-introducing-developer-tooling-to-unlock-micropayments-on-cardano.002.png) 10 November 2022![](img/2022-11-10-hydra-for-payments-introducing-developer-tooling-to-unlock-micropayments-on-cardano.002.png)[ Obsidian Systems](/en/blog/authors/obsidian-systems/page-1/)![](img/2022-11-10-hydra-for-payments-introducing-developer-tooling-to-unlock-micropayments-on-cardano.003.png) 6 mins read

![Obsidian Systems](img/2022-11-10-hydra-for-payments-introducing-developer-tooling-to-unlock-micropayments-on-cardano.004.png)[](/en/blog/authors/obsidian-systems/page-1/)
### [**Obsidian Systems**](/en/blog/authors/obsidian-systems/page-1/)
Blockchain developer

Guest author

![Hydra for Payments – introducing developer tooling to unlock micropayments on Cardano](img/2022-11-10-hydra-for-payments-introducing-developer-tooling-to-unlock-micropayments-on-cardano.005.png)

*IOG is collaborating with the Obsidian Systems team to drive the development of use cases based on the Hydra Head protocol. Hydra for Payments is one such use case.*
## **Introduction**
Scalability is key to ensuring that a blockchain can process millions of transactions without large increases in fees and transaction settlement times. Addressing scalability issues was one of the founding principles of Cardano and is the focus of the [Basho](https://www.essentialcardano.io/glossary/basho) development phase.

The Cardano platform will scale by improving the processing power of the main chain by implementing layer 1 enhancements, and also by adding processing power that works off the main blockchain – layer 2 solutions. Together, [these solutions](https://www.essentialcardano.io/article/layer-1-and-layer-2-all-you-need-to-know) boost network performance, providing higher throughput and low transaction processing cost.

The Hydra family of protocols is one of the key components of Cardano’s layer 2 scaling journey. The [*Hydra Head*](https://hydra.family/head-protocol/) is the first in this suite of protocols. It provides the foundation on which to build out further scalability. The Hydra Head is an off-chain miniledger between a relatively small group of participants, which works similarly but faster than the main on-chain ledger.

Here we introduce Hydra for Payments – open-source developer tooling for implementing payment solutions in the Cardano ecosystem.
## **Introducing Hydra for Payments**
Hydra for Payments will simplify the use of the Hydra Head protocol for a variety of payment use cases. Just as the first generation of light wallet functionality served as an enabler for basic network access, Hydra for Payments will unlock the power of micropayments in the Cardano ecosystem.

Hydra for Payments will offer a toolkit for light wallet developers to continuously leverage the Hydra family of protocols for building products that better serve user needs, reduce operating costs, and enable higher throughput across the growing Cardano network.

Efforts will be made to ensure the developer experience is familiar while remaining flexible enough to accommodate Cardano’s diverse set of wallet providers.

In later phases, Hydra for Payments will include the basic back-office interface that light wallet providers will require to:

- maintain their own Hydra Head service
- inspect their node infrastructure
- significantly scale operations
- offer such a service to others

Just as Hydra is only one part of Cardano’s overall scalability strategy, Hydra for Payments will ultimately form a *part* of a larger layer 2 light wallet story.
### **Hydra for Payments features**
- **Available**: Hydra for Payments is open source and accessible today.
- **Familiar**: Interaction with layer 1 is straightforward and doesn’t introduce significant new context or techniques for developers to master.
- **Fast**: Transactions tend to be constrained only by the speed of the network the nodes converse on top of.
- **Simple**: Due to Hydra’s isomorphic nature, Hydra for Payments does not introduce significant implementation complexity for developers.
- **Isomorphic**: Isomorphic design also allows for reuse of existing developer tooling with little modification.

Throughout the development of the Hydra for Payments toolkit, two perspectives will coexist and progress in parallel:

- First, the technical fundamentals described in the generic [Hydra Head](https://hydra.family/head-protocol/) protocol will be continuously validated to ensure they are preserved in Hydra for Payments. This is especially critical as it relates to assurances around trust, security, and correctness.
- Second, the practical considerations of light wallet developers will permeate the entire toolkit. Features will always be designed to be reasonable to develop, deploy, and maintain. Once integrated, Hydra for Payments will measurably improve light wallet developers’ operating costs, ability to monitor their infrastructure, and enhance their users’ experience.

![Hydra for Payments Cardano](img/2022-11-10-hydra-for-payments-introducing-developer-tooling-to-unlock-micropayments-on-cardano.006.png)

Figure 1. Basic light wallet integration with Hydra for Payments and Hydra Heads

A range of widely-varied layer 2 solutions currently exist or are in design and development. Multiple approaches are passionately discussed or endorsed but remain far from implementation or deployment.

Sidechains and rollups are great candidates to solve specific sets of problems while offering different trade-offs around development costs, time-to-market, security, and the complexity of their initial implementation. One trade-off, for example, is that some of these solutions require explicit asset bridges, increasing the overall attack surface for the developer to consider. Similarly, solutions that are not isomorphic also increase developer overhead by diverging from the mainnet semantics.
## **Hydra for Payments roadmap**
Initially, the API will directly map the primitives and domain of the Hydra Head protocol and provide convenient manipulation of Heads. Over time and in response to developers integrating Hydra for Payments, we will add specialized or auxiliary features that cater to specific micropayment use cases.
### **Q4 2022**
Hydra for Payments tooling will gradually roll out to assist developers in managing credentials, managing the entire Hydra Head lifecycle, and interacting with Heads through a common convenient interface.

The Hydra Head protocol is undergoing some important enhancements in Q4, which won’t immediately affect the initial Hydra for Payments interface.

A functional demo portion of Hydra for Payments will focus on a limited fast payment system allowing a group of people to opt into a Head and transfer assets at unmatched speed and cost.
### **Standards**
Just as light wallet developers benefitted from the [CIP-30 standard](https://cips.cardano.org/cips/cip30/) for lightweight general-purpose DApp connection, Hydra-based solutions should benefit from the formation of standards for managing Hydra infrastructure. This will eventually allow for interacting with layer 2 DApps to meet end-users' needs.

Aside from participating in the discussion and formation of such standards, Hydra for Payments will contribute by deploying and creating a shared reference that ensures that the evolving standards are practical.
### **2023**
Moving forward, we will continue to see new features, enhancements to the Hydra protocols, and their eager use in Hydra for Payments. One early example will be a full Hydra for Payments implementation that adds the ability to *commit* and *de-commit* funds in existing open Heads. This will allow payment channels to stay open while users add or withdraw their assets.

A future real-world reference implementation could see full integration of Hydra for Payments into an existing consumer light wallet. This could potentially be accompanied by the launch of a dedicated Hydra-Head-as-a-Service product, to further reduce time-to-market for light wallet developers while keeping overall operating costs relatively low.

As we continue to validate new features interacting with a single Head, we may consider the transition to initial implementation and the use of a Star-Shaped Head Network topology. The lessons learned from the initial Hydra Head phase will be applied to ensure that Hydra for Payments is rapidly extended to integrate new functionality like inter-head communication. One early example of this may be the ability to connect Hydra Heads to form a proper Hydra Head network, yielding an improved user experience for nearly all payment use cases.

Finally, for the toolkit to evolve with the growing Cardano ecosystem, it will be critical to accumulate feedback, discussion, and *contributions* from the community.

If you are interested to find out more, join the Hydra [Discord channel](https://discord.com/channels/826816523368005654/890903732462710836/890951034099335178) for further discussion.
