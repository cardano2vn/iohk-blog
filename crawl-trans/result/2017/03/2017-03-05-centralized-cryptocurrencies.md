# Centralized cryptocurrencies
![](img/2017-03-05-centralized-cryptocurrencies.002.png) 5 March 2017![](img/2017-03-05-centralized-cryptocurrencies.002.png)[ Alexander Chepurnoy](/en/blog/authors/alexander-chepurnoy/page-1/)![](img/2017-03-05-centralized-cryptocurrencies.003.png) 6 mins read

![](img/2017-03-05-centralized-cryptocurrencies.004.png)[ Centralized cryptocurrencies - Input Output](https://ucarecdn.com/4f9418f2-9aa8-4a53-99cc-ae3c8fc18bf9/-/inline/yes/ "Centralized cryptocurrencies - Input Output")

![Alexander Chepurnoy](img/2017-03-05-centralized-cryptocurrencies.005.png)[](/en/blog/authors/alexander-chepurnoy/page-1/)
### [**Alexander Chepurnoy**](/en/blog/authors/alexander-chepurnoy/page-1/)
Research Fellow

Team Scorex Manager

- ![](img/2017-03-05-centralized-cryptocurrencies.006.png)[](https://www.youtube.com/watch?v=Pxu4gpuVnQE "YouTube")
- ![](img/2017-03-05-centralized-cryptocurrencies.007.png)[](https://twitter.com/chepurnoy "Twitter")
- ![](img/2017-03-05-centralized-cryptocurrencies.008.png)[](https://github.com/kushti "GitHub")

![Centralized cryptocurrencies](img/2017-03-05-centralized-cryptocurrencies.009.jpeg)

This article is inspired by my recent visit to a [blockchain technology conference](http://www.osp.ru/iz/blockchain "blockchain technology conference") and my discussions with colleagues about ideas to improve blockchain. Most of the conference speakers were from big Russian banks and their talks were about blockchain use cases, mainly as databases or smart contract platforms. However, none of the speakers were able to answer the question, âwhy did they really need blockchain?â. The correct answer for this question recently came from the R3 CEV consortium: ["no blockchain because we don't need one"](https://twitter.com/Beautyon_/status/834152812405735425?ref_src=twsrc%5Etfw "R3 Twitter - no blockchain"). Blockchain is not needed for banks, it is needed instead of banks. It is required for decentralized systems only, applications with a trusted party will always be more efficient, simple, etc. The meaning of decentralization has been widely discussed (see, for example, this post from [Vitalik Buterin](https://medium.com/@VitalikButerin/the-meaning-of-decentralization-a0c92b76a274#.x5k6j4cxg "Vitalik Buterin - the meaning of decentralization") and it is the only real purpose of blockchains. In this blog post I'm going to discuss the degree of centralization of existing cryptocurrencies and the reasons leading to it.
## **Governance and development centralization**
Let's start with a non-technical topic. It is nice to think that **no-one controls blockchain**, ie that network participants (miners) act as a decentralized community and chose the direction of development. In fact, everything is much worse.

The first source of centralization here, is the source of the protocol for improvement. Only a small group of **core developers** is able to accept changes to the source code or even understand some protocol [improvement proposals](https://en.bitcoin.it/wiki/Bitcoin_Improvement_Proposals "Bitcoin Wiki improvement proposals"). No-one works for free and the organization that pays money to the core team in fact controls the cryptocurrencyâs source code. For example, Bitcoin development is controlled by Blockstream, and this organization has its own interests. A **treasury system** like the one for [Dash](/en/research/papers/dash-governance-system-analysis-and-suggestions-for-improvement/ "Suggestions for improvement - IOHK") or the one proposed for [Ethereum Classic](https://www.scribd.com/document/339563725/Ethereum-Classic-Treasury-System-Proposal-Google-Docs "Ethereum Classic treasury system proposal, IOHK") may be the solution here. However, a lot of questions are still open (for example, the 78 pages of ETC treasury proposal are quite complicated, while the Dash treasury system was developed without any documentation).

The next centralization risk in governance is the **cult of personality**. While Vitalik tells us in his [post](https://medium.com/@VitalikButerin/the-meaning-of-decentralization-a0c92b76a274#.x5k6j4cxg "Vitalik Buterin, the meaning of decentralization"), that no-one controls cryptocurrencies, his opinion is so important for the Ethereum community, that most of its members accepted the bailout of the DAO, which breaks the basic immutability principle of cryptocurrencies.

Finally, there are a lot of interested parties behind cryptocurrencies, and the opinion of some of them (for example the end users of the currency) is usually **ignored**. Anyway, the development of cryptocurrencies is a social consensus, and it is good to have a manifesto, declaring its purpose from the start.
## **Services centralization**
One of the biggest problems with existing cryptocurrencies is the centralization of services. Blockchain **processing is heavy** (eg Ethereum processing from the genesis block may take weeks) and regular users that just want to send some coins have to **trust centralized services**. Most Bitcoin users trust [blockchain.info](http://blockchain.info/ "Blockchain.info"), Ethereum users trust [myetherwallet](https://www.myetherwallet.com/ "MyEtherWallet.com") and so on. If these popular wallets were to be compromised, usersâ funds would be lost.

Moreover, most users trust in blockchain explorers and never check that the blocks in it are correct. What is the meaning of the "decentralized" social network Steemit, if almost none of its users download a blockchain and believe that the data on [Steemit.com](https://steemit.com "Steemit.com") is correct? Or imagine that blockchain.info was compromised: an attacker could steal all the usersâ money from their wallets, hide the criminal transactions and show user-created transactions in blockchain explorer, and the attack could go unnoticed for a long time. Thus, trust in centralized services produces a **single point of failure**, allows **censorship** and puts user coins in **jeopardy**.
## **Mining centralization**
With popular cryptocurrencies, **hardware requirements are high** even just for blockchain validation. Even if you own modern hardware able to process blocks fast, your network channel may not be wide enough to download the created blocks fast enough. This leads to a situation where only a few high-end computers are able to create new blocks, which leads to mining centralization. Being open by design, Bitcoin mining power is now concentrated in a limited group of miners, which could easily meet and agree to perform a 51% attack (or just censor selected transactions or blocks). Mining pools worsen the situation, for example, in Bitcoin just five mining pools control more than 50% of the hash rate (at least if you believe [blockchain.info](https://blockchain.info/pools "Hash rate distribution - blockchain.info"). Another option for miners is to skip transaction processing and produce empty blocks, which would also make blockchain meaningless.

Proof-of-Stake is usually regarded as more hardware friendly, however, a really popular blockchain requires a wide network channel to synchronize the network anyway. Also, it is usually unprofitable to keep a mining node in PoS and just a small percentage of coins are online that makes the network vulnerable. This is usually fixed by delegating mining power to someone else, that also leads to a **small amount of mining nodes**.
## **Centralization as a solution**
The most scary point of all this is that more and more often, centralization is regarded as a solution for some problems of cryptocurrencies. To fix scalability issues, cryptocurrencies propose to use a limited number of trusted ["masternodes"](http://dashmasternode.org/what-is-a-masternode/ "What is a master node?"), ["witnesses"](https://byteball.org/Byteball.pdf "Byteball: A Decentralized System for Storage and Transfer of Value"), ["delegates"](https://bitshares.org/technology/delegated-proof-of-stake-consensus/ "Delegated Proof-of-Stake consensus"), ["federations"](https://blockstream.com/2017/01/16/strong-federations-paper-released-liquid.html "Strong Federations, Foundation of Liquid, Whitepaper Released") and so on to "fix" the too-large amount of mining nodes in the network. The number of these trusted nodes may vary, but by using this method to fix scalability issues, developers also **destroy the decentralized nature of the currency**. Eventually this would lead to a cryptocurrency with only one performing node, that processes transactions very efficiently, without confirmation delays and forks, but suddenly a blockchain is not needed, as in R3's case.

Unfortunately, most users are not able to determine the lie in cryptocurrencies and like these centralized blockchains more and more, because for sure, the centralized way is (and will always be) more simple and user-friendly.
## **Conclusion**
We are going to see more centralized cryptocurrencies and that will inevitably lead to mass disappointment in blockchain technology, because it is not needed for centralized solutions. It is still a user choice, whether to believe a beautiful and fast web interface or to use trustless, but harmful software, requiring you to download blockchain data and process it.

Most centralization risks may be fixed, if trustless full-nodes, wallets, explorers are cheap to launch and easy to use. I'm not going to propose a solution in this paper, but I hope it is coming soon!
## **Attachments**
![](img/2017-03-05-centralized-cryptocurrencies.004.png)[ Centralized cryptocurrencies - Input Output](https://ucarecdn.com/4f9418f2-9aa8-4a53-99cc-ae3c8fc18bf9/-/inline/yes/ "Centralized cryptocurrencies - Input Output")