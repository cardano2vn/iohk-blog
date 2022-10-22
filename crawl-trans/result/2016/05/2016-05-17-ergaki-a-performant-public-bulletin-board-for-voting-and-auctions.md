# Announcing Ergaki - A performant, public bulletin board for voting and auctions
![](img/2016-05-17-ergaki-a-performant-public-bulletin-board-for-voting-and-auctions.002.png) 17 May 2016![](img/2016-05-17-ergaki-a-performant-public-bulletin-board-for-voting-and-auctions.002.png)[ Alexander Chepurnoy](/en/blog/authors/alexander-chepurnoy/page-1/)![](img/2016-05-17-ergaki-a-performant-public-bulletin-board-for-voting-and-auctions.003.png) 2 mins read

![](img/2016-05-17-ergaki-a-performant-public-bulletin-board-for-voting-and-auctions.004.png)[ Announcing Ergaki - A performant, public bulletin board for voting and auctions - Input Output HongKong](https://ucarecdn.com/a2b0fa9a-59f1-474a-bb33-9fd68477d23e/-/inline/yes/ "Announcing Ergaki - A performant, public bulletin board for voting and auctions - Input Output HongKong")

![Alexander Chepurnoy](img/2016-05-17-ergaki-a-performant-public-bulletin-board-for-voting-and-auctions.005.png)[](/en/blog/authors/alexander-chepurnoy/page-1/)
### [**Alexander Chepurnoy**](/en/blog/authors/alexander-chepurnoy/page-1/)
Research Fellow

Team Scorex Manager

- ![](img/2016-05-17-ergaki-a-performant-public-bulletin-board-for-voting-and-auctions.006.png)[](https://www.youtube.com/watch?v=Pxu4gpuVnQE "YouTube")
- ![](img/2016-05-17-ergaki-a-performant-public-bulletin-board-for-voting-and-auctions.007.png)[](https://twitter.com/chepurnoy "Twitter")
- ![](img/2016-05-17-ergaki-a-performant-public-bulletin-board-for-voting-and-auctions.008.png)[](https://github.com/kushti "GitHub")

![Announcing Ergaki - A performant, public bulletin board for voting and auctions](img/2016-05-17-ergaki-a-performant-public-bulletin-board-for-voting-and-auctions.009.jpeg)

The first Scorex-based testnet, Lagonaki, combines the Permacoin consensus protocol implementation with a simple, Nxt-like payments module. After Lagonaki, the next Scorex-based testnet will be *Ergaki*, a block chain system that will be used as a public and performant bulletin board for various protocols including voting and auctions. The components of Ergaki are the following:

1. A new Proof-of-Work scheme based on [RollerChain](http://arxiv.org/abs/1603.07926). By default, nodes will follow a "rational behavior", and will remove blocks that are not needed for Proof-of-Work mining. Potentially, a scheme like Ghost/Spectre or Bitcoin-NG/ByzCoin will be used to increase the system's troughput.
1. A new transactional module where state will be comprised of [boxes](http://chepurnoy.org/blog/2016/03/cryptocurrency-minimal-state-representation-boxes-vs-accounts/). This transactional model will be different from that of Bitcoin, therefore there will be no stack-language scripts. 
1. A new fee model by which mandatory fees will not be based on transaction size but on state increment. For example, a transaction that is lowering the state size would have a minimal or no fee at all. In addition, the storage of boxes in a state will incur fees not only based on size, but also based on life timespan also, with a possible exception for a box of some minimal size. So, unlike all other blockchains, it would be not possible to store anything in the Ergaki blockchain forever by paying only once. 
1. A new improved difficulty-adjustment algorithm. A white-paper on that is basically ready and will be published before the release of Ergaki.

The IOHK Scorex team will test the Ergaki testnet on some applications by using a large testbed against a private Ethereum network. The goal is outperform the latter by the orders of magnitude.

Ergaki is planned to be released in September, 2016.
## **Attachments**
![](img/2016-05-17-ergaki-a-performant-public-bulletin-board-for-voting-and-auctions.004.png)[ Announcing Ergaki - A performant, public bulletin board for voting and auctions - Input Output HongKong](https://ucarecdn.com/a2b0fa9a-59f1-474a-bb33-9fd68477d23e/-/inline/yes/ "Announcing Ergaki - A performant, public bulletin board for voting and auctions - Input Output HongKong")
