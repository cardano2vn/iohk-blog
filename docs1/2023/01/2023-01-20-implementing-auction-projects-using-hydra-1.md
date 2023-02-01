# Implementing auction projects using Hydra
### **IOG and MLabs cooperate to develop a reference implementation of an auction using Hydra protocols**
![](img/2023-01-20-implementing-auction-projects-using-hydra-1.002.png) 20 January 2023![](img/2023-01-20-implementing-auction-projects-using-hydra-1.002.png)[ Olga Hryniuk](/en/blog/authors/olga-hryniuk/page-1/)![](img/2023-01-20-implementing-auction-projects-using-hydra-1.003.png) 4 mins read

![Olga Hryniuk](img/2023-01-20-implementing-auction-projects-using-hydra-1.004.png)[](/en/blog/authors/olga-hryniuk/page-1/)
### [**Olga Hryniuk**](/en/blog/authors/olga-hryniuk/page-1/)
Senior Technical Writer

Marketing & Communications

- ![](img/2023-01-20-implementing-auction-projects-using-hydra-1.005.png)[](https://www.linkedin.com/in/olga-hryniuk-1094a3160/ "LinkedIn")
- ![](img/2023-01-20-implementing-auction-projects-using-hydra-1.006.png)[](https://github.com/olgahryniuk "GitHub")

![Implementing auction projects using Hydra](img/2023-01-20-implementing-auction-projects-using-hydra-1.007.png)

Input Output Global, Inc. (IOG) and MLabs Ltd. (MLabs) are collaborating on developing a reference implementation of an auction using Hydra protocols. The first outcome of this collaboration is a [paper](https://iohk.io/en/blog/posts/2023/01/20/implementing-auction-projects-using-hydra/) outlining possible approaches to the implementation of digital asset auctions using the Hydra Head protocol with respective advantages and current limitations. This post introduces a brief summary of the topics covered in more detail in the paper. 

This collaboration aims to demonstrate the feasibility of the current implementation of the Hydra Head protocol to develop auction applications. The proposed reference implementation also constructively determines and aligns the Hydra Head protocol design with the concrete use cases in the Cardano ecosystem. 
## **A word about auctions**
Decentralized auctions use smart contracts to execute a deal between buyers and sellers. 

The benefits of blockchain auctions include:

![](img/2023-01-20-implementing-auction-projects-using-hydra-1.008.png)
## **Running auctions on Cardano**
The [Hydra Head protocol](https://hydra.family/head-protocol/) is a layer 2 scalability solution on Cardano. The protocol consists of smart contracts and software that allow any group of participants to establish isomorphic, multi-party state channels ([Hydra Heads](https://iohk.io/en/blog/posts/2022/02/03/implementing-hydra-heads-the-first-step-towards-the-full-hydra-vision/)) with each other. 

Hydra Head channels are beneficial for running auctions on Cardano because layer 2 solutions provide better capabilities in terms of:

![](img/2023-01-20-implementing-auction-projects-using-hydra-1.009.png)
## **The Hydra Head auction design**
Cardano can run different auction types using the Hydra Head protocol. Auction designs on a single Head can cover basic single-head auctions, single-head secret auctions, delegated custodial auctions, voucher auctions, or delegated voucher auctions. Auction designs on networks of Hydra Heads can cover such cases as star-shaped auctions or constellation schema auctions. 

For the reference implementation of an auction using the Hydra Head protocol, the teams chose the delegated voucher auction design including core English-style auction features. 

For a detailed analysis of possible options with their benefits and limitations, see the full paper linked below. 

The initial design of the auction aims to provide the following features:

- A group of delegates can open a Hydra Head capable of hosting an auction for an NFT asset provided by a seller.
- The seller can distribute the right to participate (eg, via participation tokens) in the auction to prospective bidders who have locked their deductible deposits in a smart contract for the auction.
- Each bidder can submit a bid to the auction by sending it to one of the delegates, who will then broadcast it to the rest of the delegates.
- Delegates can collectively acknowledge bids by multi-signing via the Hydra Head protocol, thus including the bids in the Hydra Head ledger state.
- When the auction deadline elapses, the delegates can deterministically settle the bids within the Hydra Head to determine the winning bid.
- Delegates can close the Hydra Head:
  - If the auction is settled, a voucher can be issued to the winning bidder, which allows the winning bidder to redeem the sellerâ€™s NFT asset in exchange for the bid amount.
  - If the auction is not settled, its bids can be settled on layer 1 to determine the winning bid, and *then* the voucher can be issued to the winning bidder.
- Losing bidders can redeem their deductible deposits when the auctionâ€™s Hydra Head closes and the auction is settled.
- The winning bidder can use the funds in his deductible deposit in his payment to the seller for the NFT asset.
- When the voucher is issued to the winning bidder, a deadline is set to redeem the sellerâ€™s NFT asset. If the winning bidder does not redeem the sellerâ€™s NFT asset by the deadline, the seller can claim the winning bidderâ€™s deductible deposit.
- The voucher UTXO can only be spent by the winning bidder to redeem the sellerâ€™s NFT, or by the seller to claim the winning bidderâ€™s deductible deposit after the redemption deadline.
## **Learn more from the paper**
If you are interested to find out more, read this **â€˜[Implementing auction projects using Hydra](https://iohk.io/en/blog/posts/2023/01/20/implementing-auction-projects-using-hydra/)â€™ paper.**

The paper reflects on:

- The current needs of projects running digital asset auctions (eg, NFT marketplaces) in the Cardano ecosystem and the challenges they face on the Cardano layer 1 chain. 
- The analysis of challenges and requirements suggests possible auction designs to use Hydra for running digital asset auctions and their respective implications for liveness, decentralization, security, and efficiency.
- The proposed Hydra Head auction design implementation based on current capabilities.
- Suggested improvements to the current Hydra Head protocol along with proposed extensions to the Hydra family of protocols to benefit running digital asset auctions.

To get involved join [this Discord channel](https://discord.gg/Qq5vNTg9PT) or take part in [GitHub discussions](https://github.com/input-output-hk/hydra/discussions).
