# Enter the Hydra: scaling distributed ledgers, the evidence-based way
### **Learn about Hydra: the multi-headed ledger protocol** 
![](img/2020-03-26-enter-the-hydra-scaling-distributed-ledgers-the-evidence-based-way.002.png) 26 March 2020![](img/2020-03-26-enter-the-hydra-scaling-distributed-ledgers-the-evidence-based-way.002.png)[ Prof Aggelos Kiayias](/en/blog/authors/aggelos-kiayias/page-1/)![](img/2020-03-26-enter-the-hydra-scaling-distributed-ledgers-the-evidence-based-way.003.png) 10 mins read

![Prof Aggelos Kiayias](img/2020-03-26-enter-the-hydra-scaling-distributed-ledgers-the-evidence-based-way.004.png)[](/en/blog/authors/aggelos-kiayias/page-1/)
### [**Prof Aggelos Kiayias**](/en/blog/authors/aggelos-kiayias/page-1/)
Chief Scientist

Academic Research

- ![](img/2020-03-26-enter-the-hydra-scaling-distributed-ledgers-the-evidence-based-way.005.png)[](mailto:aggelos.kiayias@iohk.io "Email")
- ![](img/2020-03-26-enter-the-hydra-scaling-distributed-ledgers-the-evidence-based-way.006.png)[](tmp///www.youtube.com/watch?v=nB6eDbnkAk8 "YouTube")

![Enter the Hydra: scaling distributed ledgers, the evidence-based way ](img/2020-03-26-enter-the-hydra-scaling-distributed-ledgers-the-evidence-based-way.007.jpeg)

Scalability is the greatest challenge to blockchain adoption. By applying a principled, evidence-based approach, we have arrived at a solution for Cardano and networks similar to it: Hydra. Hydra is the culmination of extensive research, and a decisive step in enabling decentralized networks to securely scale to global requirements. 
## **What is scalability and how do we measure it?**
Scaling a distributed ledger system refers to the capability of providing high transaction throughput, low latency, and minimal storage per node. These properties have been repeatedly touted as critical for the successful deployment of blockchain protocols as part of real-world systems. In terms of throughput, the VISA network [reportedly](https://usa.visa.com/run-your-business/small-business-tools/retail.html) handles an average of 1,736 payment transactions per second (TPS) with the capability of handling up to 24,000 TPS and is frequently used as a baseline comparison. Transaction latency is clearly desired to be as low as possible, with the ultimate goal of appearing instantaneous to the end-user. Other applications of distributed ledgers have a wide range of different requirements in terms of these metrics. When designing a general purpose distributed ledger, it is natural to strive to excel on all three counts. 

Deploying a system that provides satisfactory scaling for a certain use case requires an appropriate combination of two independent aspects: adopting a proper algorithmic design and deploying it over a suitable underlying hardware and network infrastructure.

When evaluating a particular algorithmic design, considering absolute numbers in terms of specific metrics can be misleading. The reason is that such absolute quantities must refer to a particular underlying hardware and network configuration which can blur the advantages and disadvantages of particular algorithms. Indeed, a poorly designed protocol may still perform well enough when deployed over superior hardware and networking.

For this reason, it is more insightful to evaluate the ability of a protocol to reach the physical limits of the underlying network and hardware. This can be achieved by comparing the protocol with simple strawman protocols, in which all the design elements have been stripped away. For instance, if we want to evaluate the overhead of an encryption algorithm, we can compare the communication performance of two end-points using encryption against their performance when they simply exchange unencrypted messages. In such an experiment, the absolute message-per-second rate is unimportant. The important conclusion is the relative overhead that is added by the encryption algorithm. Moreover, in case the overhead approximates 0 for some configuration of the experimental setup, we can conclude that the algorithm approximates the physical limits of the underlying networkâ€™s message-passing ability for that particular configuration, and is hence optimal in this sense. 
## **Hydra â€“ 30,000-feet view**
Hydra is an off-chain scalability architecture for distributed ledgers, which addresses all three of the scalability challenges mentioned above: high transaction throughput, low latency, and minimal storage per node. While Hydra is being designed in conjunction with the Ouroboros protocol and the Cardano ledger, it may be employed over other systems as well, provided they share the necessary salient characteristics with Cardano.

Despite being an integrated system aimed at solving one problem â€“ scalability â€“ Hydra consists of several subprotocols. This is necessary as the Cardano ecosystem itself is heterogenous and consists of multiple entities with differing technical capabilities: the system supports block producers with associated stake pools, high-throughput wallets as used by exchanges, but also end-users with a wide variety of computational performance and availability characteristics. It is unrealistic to expect that a one-shoe-fits-all, single-protocol approach is sufficient to provide overall scalability for such a diverse set of network participants.

The Hydra scalability architecture can be divided into four components: the head protocol, the tail protocol, the cross-head-and-tail communication protocol, as well as a set of supporting protocols for routing, reconfiguration, and virtualization. The centerpiece is the 'head' protocol, which enables a set of high-performance and high-availability participants (such as stake pools) to very quickly process large numbers of transactions with minimal storage requirements by way of a multiparty state channel â€“ a concept that generalizes two-party payment channels as implemented in the context of the Lightning network. It is complemented by the 'tail' protocol, which enables those high-performance participants to provide scalability for large numbers of end-users who may use the system from low-power devices, such as mobile phones, and who may be offline for extended periods of time. While heads and tails can already communicate via the Cardano mainchain, the cross-head-and-tail communication protocol provides an efficient offâ€“chain variant of this functionality. All this is tied together by routing and configuration management, while virtualisation facilitates faster communication generalizing head and tail communication. 
## **The Hydra head protocol**
The Hydra head protocol is the first component of the Hydra architecture to be publicly [released](https://eprint.iacr.org/2020/299). It allows a set of participants to create an off-chain state channel (called a head) wherein they can run smart contracts (or process simpler transactions) among each other without interaction with the underlying blockchain in the optimistic case where all head participants adhere to the protocol. The state channel offers very fast settlement and high transaction throughput; furthermore, it requires very little storage, as the off-chain transaction history can be deleted as soon as its resulting state has been secured via an offâ€“chain 'snapshot' operation.

Even in the pessimistic case where any number of participants misbehave, full safety is rigorously guaranteed. At any time, any participant can initiate the head's 'closure' with the effect that the head's state is transferred back to the (less efficient) blockchain. We emphasize that the execution of any smart contracts can be seamlessly continued on-chain. No funds can be generated off-chain, nor can any single, responsive head participant lose any funds.

The state channels implemented by Hydra are isomorphic in the sense that they make use of the same transaction format and contract code as the underlying blockchain: contracts can be directly moved back and forth between channels and the blockchain. Thus, state channels effectively yield parallel, off-chain ledger siblings. In other words, the ledger becomes multi-headed.

Transaction confirmation in the head is achieved in full concurrency by an asynchronous off-chain certification process using multi-signatures. This high level of parallelism is enabled by use of the extended UTxO model ([EUTxO](https://github.com/hydra-supplementary-material/eutxo-spec/blob/master/extended-utxo-specification.pdf)). Transaction dependencies in the EUTxO model are explicit, which allows for state updates without unnecessary sequentialization of transactions that are independent of each other. 
## **Experimental validation of the Hydra head protocol**
As a first step towards experimentally validating the performance of the Hydra head protocol, we implemented a simulation. The simulation is parameterized by the time required by individual actions (validating transactions, verifying signatures, etc.), and carries out a realistic and timing-correct simulation of a cluster of distributed nodes forming a head. This results in realistic transaction confirmation time and throughput calculations.

We see that a single Hydra head achieves up to roughly 1,000 TPS, so by running 1,000 heads in parallel (for example, one for each stake pool of the Shelley release), we should achieve a million TPS. Thatâ€™s impressive and puts us miles ahead of the competition, but why should we stop there? 2,000 heads will give us 2 million TPS â€“ and if someone demands a billion TPS, then we can tell them to just run a million heads. Furthermore, various performance improvements in the implementation can improve the 1,000 TPS single head measurement, further adding to the protocolâ€™s hypothetical performance. 

So, can we just reach any TPS number that we want? In theory the answer is a solid yes, and that points to a problem with the dominant usage of TPS as a metric to compare systems. While it is tempting to reduce the complexity of assessing protocol performance to a single number, in practice this leads to an oversimplification. Without further context, a TPS number is close to meaningless. In order to properly interpret it, and make comparisons, you should at least ask for the size of the cluster (which influences the communication overhead); its geographic distribution (which determines how much time it takes for information to transit through the system); how the quality of service (transaction confirmation times, providing data to end users) is impacted by a high rate of transactions; how large and complicated the transactions are (which has an impact on transaction validation times, message propagation time, requirements on the local storage system, and composition of the head participants); and what kind of hardware and network connections were used in the experiments. Changing the complexity of transactions alone can change the TPS by a factor of three, as can be seen in the figures in the [paper](https://eprint.iacr.org/2020/299) (refer to Section 7 â€“ Simulations).

Clearly, we need a better standard. Is the Hydra head protocol a good protocol design? What we need to ask is whether it reaches the physical limits of the network, not a mere TPS number. Thus, for this first iteration of the evaluation of the Hydra head protocol, we used the following approach to ensure that the data we provide is properly meaningful: 

1. We clearly list all the parameters that influence the simulation: transaction size, time to validate a single transaction, time needed for cryptographic operations, allocated bandwidth per node, cluster size and geographical distribution, and limits on the parallelism in which transactions can be issued. Without this controlled environment, it would be impossible to reproduce our numbers.
1. We compare the protocolâ€™s performance to baselines that provide precise and absolute limits of the underlying network and hardware infrastructure. How well we approach those limits tells us how much room there would be for further improvements. This follows the methodology explained above using the example of an encryption algorithm.

We use two baselines for Hydra. The first, Full Trust, is universal: it applies to any protocol that distributes transactions amongst nodes and insists that each node validate transactions one after the other â€“ without even ensuring consensus. This yields a limit on TPS by simply adding the message delivery and validation times. How well we approach this limit tells us what price we are paying for consensus, without relying on comparison with other protocols. The second baseline, Hydra Unlimited, yields a TPS limit specifically for the head protocol and also provides the ideal latency and storage for any protocol. We achieve that by assuming that we can send enough transactions in parallel to completely amortize network round-trip times and that all actions can be carried out when needed, without resource contention. The baseline helps us answer the question of what can be achieved under ideal circumstances with the general design of Hydra (for a given set of values of the input parameters) as well as evaluate confirmation latency and storage overhead against any possible protocol. More details and graphs for those interested can be found in our [paper](https://eprint.iacr.org/2020/299) (again, Section 7 â€“ Simulations). 
## **What comes next?**
Solving the scalability question is the holy grail for the whole blockchain space. The time has come to apply a principled, evidence-based approach in designing and engineering blockchain scalability solutions. Comparing scalability proposals against well-defined baselines can be a significant aide in the design of such protocols. It provides solid evidence for the appropriateness of the design choices and ultimately leads to the engineering of effective and performant distributed ledger protocols that will provide the best possible absolute metrics for use cases of interest. While the Hydra head protocol is implemented and tested, we will, in time, release the rest of the Hydra components following the same principled approach. 

As a last note, Hydra is the joint effort of a number of researchers, whom I'd like to thank. These include Manuel Chakravarty, Sandro Coretti, Matthias Fitzi, Peter GaÅ¾i, Philipp Kant, and Alexander Russel. The research was also supported, in part, by EU Project No.780477, PRIVILEDGE, which we gratefully acknowledge.