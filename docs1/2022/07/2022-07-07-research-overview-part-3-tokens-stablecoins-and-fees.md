# Research overview part 3: tokens, stablecoins, and fees
### **IOG research enabled the implementation of multi-asset support, stablecoins, and friendly fees on Cardano**
![](img/2022-07-07-research-overview-part-3-tokens-stablecoins-and-fees.002.png) 7 July 2022![](img/2022-07-07-research-overview-part-3-tokens-stablecoins-and-fees.002.png)[ Olga Hryniuk](/en/blog/authors/olga-hryniuk/page-1/)![](img/2022-07-07-research-overview-part-3-tokens-stablecoins-and-fees.003.png) 5 mins read

![Olga Hryniuk](img/2022-07-07-research-overview-part-3-tokens-stablecoins-and-fees.004.png)[](/en/blog/authors/olga-hryniuk/page-1/)
### [**Olga Hryniuk**](/en/blog/authors/olga-hryniuk/page-1/)
Technical Writer

Marketing & Communications

- ![](img/2022-07-07-research-overview-part-3-tokens-stablecoins-and-fees.005.png)[](https://www.linkedin.com/in/olga-hryniuk-1094a3160/ "LinkedIn")
- ![](img/2022-07-07-research-overview-part-3-tokens-stablecoins-and-fees.006.png)[](https://github.com/olgahryniuk "GitHub")

![Research overview part 3: tokens, stablecoins, and fees](img/2022-07-07-research-overview-part-3-tokens-stablecoins-and-fees.007.png)

Our [previous post](https://iohk.io/en/blog/posts/2022/06/23/overview-of-the-research-enabling-smart-contract-support-on-cardano/) discussed Cardanoâ€™s innovative EUTXO model and how it facilitates expressive smart contracts on Cardano. This time, we take a closer look at the research that enabled multi-asset support and the creation of a variety of user-defined tokens, and we also discuss the benefits of Babel fees.
## **Multi-asset support**
Ethereum is known for providing the ability to create various user-defined assets (tokens). However, Ethereumâ€™s token standards are not directly supported by the ledger and require repetitive custom code. This adds a layer of complexity, extra cost, and inefficiency since token code is replicated and adapted rather than being part of the system itself. This leaves room for human error and can introduce bugs potentially leading to financial losses.

The research paper â€˜[UTXOma: UTXO with Multi-Asset Support](https://iohk.io/en/research/library/papers/utxomautxo-with-multi-asset-support/)â€™ was written by IOG scientists and presented at the ISoLA 2020 conference. The paper studies the creation of a wide range of user-defined tokens through the use of contract scripts called *minting policies*.

The paper explores an alternative design to user-defined asset creation based on Bitcoin-style UTXO ledgers. It proposes an extension of the UTXO model, where the accounting structure of a single cryptocurrency is replaced with a new structure that manages an unbounded number of user-defined, native tokens, called *token bundles*.

In this new model, token creation is controlled by minting policy scripts that, just like Bitcoin validator scripts, use a domain-specific language with bounded computational expressiveness. This favors Bitcoinâ€™s security and results in a lightweight and low cost approach to custom asset creation and transfer.

The â€˜[Native Custom Tokens in the Extended UTXO Model](https://iohk.io/en/research/library/papers/native-custom-tokens-in-the-extended-utxo-model/)â€™ paper suggests a generalization of the EUTXO model with native user-defined tokens. The paper explores the synergy between the native tokens from UTXOma with expressive smart contracts on the basis of a UTXO ledger as proposed by the EUTXO model. This results in more expressive minting policies and a direct mapping of versatile contracts based on state machines to the multi-asset EUTXO ledger. The paper formally establishes the correctness of this mapping.
## **Djed stablecoin**
Besides custom tokens, IOG carried out research on the implementation of a stablecoin on Cardano. The â€˜[Djed: A Formally Verified Crypto-Backed Pegged Algorithmic Stablecoin](https://iohk.io/en/research/library/papers/djed-a-formally-verified-crypto-backed-pegged-algorithmic-stablecoin/)â€™ paper was published in 2021.

The paper introduces a stablecoin contract based on algorithmic design, which uses smart contracts to ensure price stabilization. This is a very useful feature for decentralized finance (DeFi) environments. [Djed acts as an autonomous bank](https://iog.io/en/blog/posts/2021/08/18/djed-implementing-algorithmic-stablecoins-for-proven-price-stability/). It mints and burns stablecoins and reserve coins while keeping a reserve of base coins. The contract maintains the peg of stablecoins to a target price by buying and selling stablecoins, using the reserve, and charging fees, which accumulate in the reserve.

Djed is currently being [implemented by COTI.](https://iog.io/en/blog/posts/2021/09/26/coti-to-issue-djed-stablecoin-on-cardano/)
## **Babel fees**
The benefits of Cardanoâ€™s multi-asset EUTXO model opened up another research avenue that led to â€˜[Babel fees](https://iohk.io/en/research/library/papers/babel-fees-via-limited-liabilities/)â€™. Babel fees is a mechanism that will allow for transaction fees to be paid in coins other than ada on Cardano. The paper has been accepted for publication at [ACNS 2022](https://acns22.di.uniroma1.it/home), which took place in June.

Blockchain transactions require fees for their execution. To ensure network security, fees usually must be paid in the currency native to a chosen blockchain, like ada on Cardano, for example. However, allowing the fee to be paid in other valuable tokens that a user possesses improves the convenience of use and also benefits interoperability. IOGâ€™s research in the paper on Babel fees explains how this is possible.

Several innovative features of Cardano, such as the EUTXO model and custom native assets are coming together to enable Babel fees. Cardanoâ€™s multi-asset support allows for the creation of tokens treated as native on the ledger. This means that new user-defined tokens â€” if only enough users consider them valuable â€” can be used to pay transaction fees just like ada, Cardanoâ€™s primary currency.

Manuel Chakravarty, Lambda scientist and Plutus architect at IOG says:

Cardano encourages special-interest communities to form around new custom tokens that these communities create themselves using Plutus. Members of these communities may possess plenty of liquidity in a custom token without holding much ada. To support such communities, we want them to be able to pay for the use of the network using their own tokens.

So when a user wishes to pay the transaction fee in tokens other than ada, they can make such an offer by way of a Babel fee transaction offering a custom token, but incurring an ada liability. A block producer that validates this transaction can then accept this offer setting up a spot trade between ada and the offered token(s) at a previously advertised exchange rate. The block producer then creates a second transaction, covering the fee in ada, while receiving the offered tokens in exchange. By suitably extending the ledger rules, the transaction with the liability - as well as its matching transaction - become admissible to the ledger as a group. The beauty of the scheme is that users who stake their ada still get the staking reward paid out in ada as usual.

Manuel Chakravarty adds: 

The next step towards the implementation of Babel fees on Cardano is to write a Cardano Improvement Proposal (CIP) on the basis of the research paper. We will present this to the community for discussion as soon as the first version is complete.

*With multi-asset and smart contract support introduced to Cardano in 2020-2021, the ledger became a functional environment for the creation of myriad decentralized applications (DApps). Now with over a thousand projects building on Cardano, IOG research and development is focused on Cardanoâ€™s scaling and steady optimizations. So, in the next blog post, weâ€™ll reflect more on the research driving Cardanoâ€™s scalability and interoperability.*
