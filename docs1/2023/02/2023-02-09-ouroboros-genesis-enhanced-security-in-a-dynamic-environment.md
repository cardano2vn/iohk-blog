# Ouroboros Genesis: enhanced security in a dynamic environment
### **Ouroboros Genesis comes to Cardano in 2023. Genesis' main feature is enabling participants to safely join the network without the need to trust selected peers to provide a correct snapshot of the current blockchain state. Read on**
![](img/2023-02-09-ouroboros-genesis-enhanced-security-in-a-dynamic-environment.002.png) 9 February 2023![](img/2023-02-09-ouroboros-genesis-enhanced-security-in-a-dynamic-environment.002.png)[ Christian Badertscher](/en/blog/authors/christian-badertscher/page-1/)![](img/2023-02-09-ouroboros-genesis-enhanced-security-in-a-dynamic-environment.003.png) 6 mins read

![Christian Badertscher](img/2023-02-09-ouroboros-genesis-enhanced-security-in-a-dynamic-environment.004.png)[](/en/blog/authors/christian-badertscher/page-1/)
### [**Christian Badertscher**](/en/blog/authors/christian-badertscher/page-1/)
Research Fellow

Academic Research

- ![](img/2023-02-09-ouroboros-genesis-enhanced-security-in-a-dynamic-environment.005.png)[](mailto:christian.badertscher@iohk.io "Email")

![Ouroboros Genesis: enhanced security in a dynamic environment](img/2023-02-09-ouroboros-genesis-enhanced-security-in-a-dynamic-environment.006.png)

[Ouroboros Genesis](https://www.essentialcardano.io/glossary/ouroboros-genesis) is a proof-of-stake (PoS) blockchain protocol that extends its predecessor â€“ [Ouroboros Praos](https://www.essentialcardano.io/glossary/ouroboros-praos).

Letâ€™s first recall that Ouroboros is a [Nakamoto-style PoS protocol](https://iohk.io/en/research/library/papers/ouroboros-a-provably-secure-proof-of-stake-blockchain-protocol/) with built-in resilience to potentially heavily fluctuating participation. This means that it is resilient to the many challenges that may arise from network issues, wrong configuration of nodes, or race conditions that may cause node downtime. Ouroboros is proven to be secure as long as less than half of the total active stake is in the hands of malicious actors. And even if this assumption was temporarily violated, Ouroboros would self-heal quickly after the honest-majority condition holds again. A [2020 research paper by IOG](https://eprint.iacr.org/2020/1021.pdf) analyzes this situation.

An important and often overlooked question in dynamic PoS systems has for a long time been: how can parties safely join or rejoin the system under the same security assumption â€“ and in particular without relying on trusted peers that serve a correct version of the current blockchain? This question has been regarded as a major drawback for PoS systems â€“ until a [2018 research paper by IOG](https://eprint.iacr.org/2018/378.pdf) proposed a solution to this problem. This post explains the importance and main idea behind Genesis.
## **The importance of dynamic availability**
Dynamic availability in a blockchain setting can be regarded as a property that allows block-producing [nodes](https://www.essentialcardano.io/glossary/node) to go online and offline without notice. At the same time, the system stays operational for any participation level and remains secure as long as (among the active nodes) more than 50% of the resources, such as computational power in Bitcoin or stake in Cardano are controlled by honest participants. The consensus mechanism, whose purpose is bringing all the nodes into agreement, uses those resources to elect leaders with the right to extend the blockchain by a block containing valid transactions.

In this context, dynamic availability provides enhanced network liveness, and is essential for a truly decentralized system, since not all nodes can be assumed to be constantly online. However, to make this story complete, nodes must be able to easily rejoin the system, just by observing the network and knowing the genesis block. Any further trust assumption, like the requirement for checkpoints served by trusted peers, goes against the vision of decentralization.

In 2018, IOG research presented and analyzed the Ouroboros Genesis algorithm that provably fulfills the above requirements in a strong cryptographic model. The Genesis algorithm is essentially Praos, with a novel chain selection rule added that enables parties to safely join and bootstrap the blockchain from scratch without requiring trusted advice, or any other help such as knowledge of past availability.
## **Security guarantees through chain selection rule**
Genesis has a similar structure to Ouroboros Praos. In fact, considering the case that all parties are always available, the two protocols behave identically. When it comes to dynamic availability though, newly joining parties require advice in Praos: to be able to safely extend the longest chain. Newcomers must first be made aware of the current (true) ledger state, eg, by asking trusted peers. If an attacker can serve a fake chain to those newcomers, it is possible to prevent them from joining and contributing to the systemâ€™s security and performance. So, how does Genesis avoid such trusted advice? The technical innovation lies in the novel chain selection rule.

Put simply, think of chain selection as a filter. This filter, when presented with all blockchains observed on the network, detects the one that is *most useful* for the system. In principle, in Nakamoto-consensus, the approach is to go with the longest chain. While this is fine for Bitcoin, in the PoS case the [simple longest-chain rule is not a good idea](https://eprint.iacr.org/2018/248.pdf): an adversary could fork from an honest chain and keep creating blocks privately. After a substantial amount of time (in the order of several epochs), the adversary will essentially be the majority stakeholder in his private chain and thus be able to create blocks much faster than the honest chain, eventually surpassing it in length. Praos and other PoS algorithms prevent being tricked into such an adversarial chain by introducing rolling checkpoints that all chains need to comply with. As mentioned above, introducing such checkpoints has the drawback that joining parties need trusted advice.

So what can be done? The key insight is that whenever an adversary forks off from some honest chain and extends the chain privately, the adversary cannot avoid the fact that any such private chain has an initial segment of slots, right after the forking point, that is less dense (has fewer blocks) than the chain honest participants do create for that segment. This can be leveraged to tell apart the good from the bad and therefore also to get rid of the aforementioned rolling checkpoints by introducing a novel chain-selection rule.

Assume a newcomer starting from the genesis block as the initial chain. Whenever a new chain is seen on the network, this newcomer compares the locally held chain with the new one according to density in that particular segment after the two chains start to fork from one another. The newcomer adopts the new chain only if it is denser in that segment, and keeps iterating this process with other newly received chains. By the observation above, it can be concluded that when the newcomer happens to observe the actual chain supported by the honest majority of the active stake in the network, this chain will be adopted. Consequently, the newcomer locks in the state of the blockchain exactly as other already active participants do.

For the complete technical argument, refer to the [2018 research paper](https://eprint.iacr.org/2018/378.pdf) and see a [presentation on Ouroboros Genesis](https://www.youtube.com/watch?v=LCeK_4o-NCc) by Aggelos Kiayias.

In summary, the chain selection rule allows Ouroboros to seamlessly handle changes in the number of active parties in a decentralized way by bootstrapping from the genesis block and staying secure, as long as honest participants hold the majority of the active stake.

**When on Cardano?**

Cardano currently runs on Ouroboros Praos and the teams are already working on the consensus redesign. There is a working partial Genesis prototype, which is being tuned for performance and audited for new attack vectors. The teams also worked on a self-contained implementation of the Genesis disconnection logic, which is the main component of the implementation. This logic is currently going through testing and requires additional integration efforts.

If youâ€™re interested in the development process, see [this Genesis roadmap](https://github.com/input-output-hk/ouroboros-network/blob/a626c84f6df585dd27d735eb7eec73904a1f570e/ouroboros-consensus/docs/2023-Jan-Genesis-roadmap.md). To stay tuned, follow [technical updates from the consensus team](https://input-output-hk.github.io/cardano-updates/tags/consensus) and [IOG media](https://twitter.com/InputOutputHK?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor) channels.

*Olga Hryniuk contributed to this blog post.*
