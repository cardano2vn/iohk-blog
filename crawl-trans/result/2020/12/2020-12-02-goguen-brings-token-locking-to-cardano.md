# Goguen brings token locking to Cardano
### **We’re deploying the same process used for the Shelley update to deliver a smooth upgrade path to Goguen**
![](img/2020-12-02-goguen-brings-token-locking-to-cardano.002.png) 2 December 2020![](img/2020-12-02-goguen-brings-token-locking-to-cardano.002.png)[ Kevin Hammond](/en/blog/authors/kevin-hammond/page-1/)![](img/2020-12-02-goguen-brings-token-locking-to-cardano.003.png) 7 mins read

![Kevin Hammond](img/2020-12-02-goguen-brings-token-locking-to-cardano.004.png)[](/en/blog/authors/kevin-hammond/page-1/)
### [**Kevin Hammond**](/en/blog/authors/kevin-hammond/page-1/)
Software Engineer

Engineering

- ![](img/2020-12-02-goguen-brings-token-locking-to-cardano.005.png)[](https://twitter.com/inputoutputhk "Twitter")

![Goguen brings token locking to Cardano](img/2020-12-02-goguen-brings-token-locking-to-cardano.006.jpeg)

Your browser does not support the audio element.

Cardano’s [development](https://roadmap.cardano.org/en/) has been conceived as a journey involving five overlapping development themes, each of which is underpinned by a *consensus* protocol – Ouroboros. As Cardano evolves, the protocol must also change as fresh functionality and utility are brought onto the platform. Upgrades require gradual changes to the network protocol and in this article, we will explain how these protocol changes are implemented and what goes on behind the scenes to make this process smooth and straightforward.
## **Reducing complexity in protocol changes**
In the crypto world, any fundamental change to the blockchain protocol is referred to as a *hard fork*. In most blockchains, a hard fork is a ‘traumatic’ event that causes a – hopefully short – break in block production. In contrast, Cardano handles hard forks automatically, *without* stopping block production. This gives a uniquely smooth upgrade process that allows new features to be introduced easily and evolve the platform’s capabilities.

Traditionally, when a hard fork event occurs, the current protocol stops operating. All block producers upgrade to a new version of the software that implements the new block production rules or other changes. Having done this, the chain history is erased and block production is restarted. This means that a hard-forked chain will be different from the previous version, which can raise concerns over the integrity of the blockchain, or even lead to splits in the chain.
## **With Cardano, we do things differently**
The way that Cardano implements protocol changes is completely different from the way other blockchains handle hard forks. Our goal has always been to make these changes as seamless as possible. To enable a smooth transition, Cardano automatically preserves the history of previous blocks. This allows the protocol to be upgraded without radical interference to the chain. The previous state does not vanish. Rather, it is extended to include new capabilities. Instead of splitting into two different chains, Cardano combines the original blocks that comply with the current block production rules with new blocks that comply with the *new* block production rules. 

We have christened the mechanism that does this the [*hard-fork combinator*](https://docs.cardano.org/en/latest/explore-cardano/what-is-a-hard-fork-combinator.html) since it combines protocols without triggering interruptions or forcing a restart to Cardano. The [Byron to Shelley](https://iohk.io/en/blog/posts/2020/05/07/combinator-makes-easy-work-of-shelley-hard-fork/) transition used this technique for the first time. But the crucial point here is that Byron’s chain history did not disappear. Byron and Shelley chains appear ‘as one’, where the Shelley blocks extend the chain that was produced in the Byron era. Shifting from Byron’s Byzantine Fault Tolerance consensus protocol (OBFT) to Shelley’s Ouroboros Praos did not require block production to be stopped or all the nodes to update simultaneously. Instead, nodes could update independently. 

As Cardano and Ouroboros evolve, the hard fork combinator approach ensures that Goguen, Basho, and Voltaire blocks will all be held in a single chain. Features will be added at each stage in successive hard forks. Some new features may not even need a hard fork (where the consensus protocol does not change).
## **The advent of token locking**
*Token locking* is a feature in the next protocol update that we are now preparing to deploy on mainnet. Internally, we are calling this development stage *Allegra* (named after Lord Byron’s daughter). Alongside the [integration of metadata](https://iohk.io/en/blog/posts/2020/11/03/getting-to-grips-with-metadata-on-cardano/) on the network, this is the next significant upgrade for Goguen. 

This represents a relatively small technical change to the consensus protocol, with a slight impact on the actual ledger. However, it is significant since it will prepare the platform for smart contracts and the creation of assets (in addition to ada) that run on Cardano. It also provides an important piece of Voltaire (governance) functionality, supporting a voting mechanism. Underlying this are system changes to ensure that we can continue to develop through future hard forks.

Token locking is a way of recording that a specific token is being used for some purpose. By *token*, we mean the items that are counted by the blockchain ledger. Until now, there has only been ada, but soon many other custom tokens will be able to use the Cardano platform. *Locking*, in this case, means ‘reserving’ a certain number of tokens for a specified period of time so they cannot be disposed of to gain a benefit (such as voting, or running a smart contract). 

We can compare this with earning dividends from shares. A person who buys shares in a company might be rewarded with a dividend from the company’s profits. Let’s assume that this dividend is paid at the end of each calendar year and requires the shareholder to have held their shares for the entire year. If they were to sell some of their shares at the end of November, they would lose *all* the dividends for those shares for that year. They have entered a conditional contract with the share provider that gives them something of value (here, a dividend) in return for holding a specific token (here, a share) for a certain period (in this case, a full calendar year).
## **Enabling complex smart contracts**
Token locking is essential to enable complex smart contracts, and to support certain conditions, for example, when making a purchase. Thus, when someone enters into a contractual agreement to sell a house, a promise is made by the vendor that this house won’t be sold to another person – only to the person who actually pays the money. So, the token can represent the house in this case, whereas the ‘promise’ will be the actual token locking. If the house is sold to a third party, the promise in the contract will have been broken and any penalties will be invoked. This precise functionality will become available to contract providers with the introduction of token locking, using ada coins as the tokens. The ada may still be delegated to a stake pool as usual.

Within the Voltaire mechanism – which will be first used with Project Catalyst Fund2 voting – those ada holders who wish to participate in the voting process will need to ‘lock’ some ada. This will represent their voting rights, according to the amount of ada that they lock. It will prove that individuals have a certain number of votes, and eliminate the possibility of any votes being counted more than once. An individual cannot allocate more votes than they hold, or vote on contradictory ideas, or duplicate the votes.
## **How is this implemented?**
The introduction of token locking will happen behind the scenes. It will not affect the experience of ada holders because Daedalus and Yoroi wallets will automatically be updated without requiring any action from ada holders. 

However, to implement the updated version of Ouroboros that will support token locking, all the nodes that run the network will have to ‘agree’ on it (that is, reach consensus). To achieve this, stake pool operators and exchanges that are running nodes will simply have to download the new version of the code and check its operation. IOHK’s development teams will support stake pool operators and monitor the network throughout this process to ensure that the transition goes smoothly. 

Once token locking is running on the mainnet Cardano ledger, subsequent hard forks will introduce multi-asset and other smart contract capabilities. These will also be able to use token locking, opening up many new possibilities for Cardano users. In time, this will also lay the groundwork for creating non-fungible (unique) tokens on the Cardano blockchain. 

IOHK’s innovative hard fork combinator has given Cardano a secure, smooth path to regular protocol updates – each bringing fresh value and utility to the network while minimizing disruption and risk. We’re in the final stages of quality testing and will start the testnet deployment process this month, with an expectation of moving to the mainnet around the middle of December. During 2021, there will be more upgrades using the combinator – multi-asset support is coming up – as the Cardano platform continues to fulfill its potential. Stay tuned for an exciting year.
