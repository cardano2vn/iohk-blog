# Authenticated Dynamic Dictionaries, with Applications to Cryptocurrencies
![](img/2017-02-20-authenticated-dynamic-dictionaries-with-applications-to-cryptocurrencies.002.png) 20 February 2017![](img/2017-02-20-authenticated-dynamic-dictionaries-with-applications-to-cryptocurrencies.002.png)[ Alexander Chepurnoy](/en/blog/authors/alexander-chepurnoy/page-1/)![](img/2017-02-20-authenticated-dynamic-dictionaries-with-applications-to-cryptocurrencies.003.png) 3 mins read

![Alexander Chepurnoy](img/2017-02-20-authenticated-dynamic-dictionaries-with-applications-to-cryptocurrencies.004.png)[](/en/blog/authors/alexander-chepurnoy/page-1/)
### [**Alexander Chepurnoy**](/en/blog/authors/alexander-chepurnoy/page-1/)
Research Fellow

Team Scorex Manager

- ![](img/2017-02-20-authenticated-dynamic-dictionaries-with-applications-to-cryptocurrencies.005.png)[](https://www.youtube.com/watch?v=Pxu4gpuVnQE "YouTube")
- ![](img/2017-02-20-authenticated-dynamic-dictionaries-with-applications-to-cryptocurrencies.006.png)[](https://twitter.com/chepurnoy "Twitter")
- ![](img/2017-02-20-authenticated-dynamic-dictionaries-with-applications-to-cryptocurrencies.007.png)[](https://github.com/kushti "GitHub")

Our paper ["Improving Authenticated Dynamic Dictionaries, with Applications to Cryptocurrencies"](https://eprint.iacr.org/2016/994) will appear at the [Financial Cryptography 2017](http://fc17.ifca.ai/program.html "Financial Cryptography conference") conference in Malta in April. It was also presented at the Real World Crypto 2017 conference in New York and I highly recommend watching the impressive [presentation from Leonid Reyzin](https://www.youtube.com/watch?v=PHY7JnLrK5o "Improving Authenticated Dynamic Dictionaries"), professor of computer science at Boston University and one of the four authors of the paper.

Some background. Previously I worked for the [Nxt platform](https://nxt.org/ "Nxt.org") which has assets and many more cool features. The problem is, the blockchain processing becomes incredibly heavyweight (considering the pretty low number of transactions, in comparison with Bitcoin) with new features added. The same problem with Ethereum these days - after the attacks in autumn, it is nearly impossible to wait until processing being finished on an ordinary laptop.

The problem is in a state (e.g. UTXO set in Bitcoin) persistence. Once it hits a secondary storage (HDD or SSD), processing becomes very slow.

Thus two considerations behind our work on AVL+ trees and a proposed scheme for cryptocurrencies:

- It should be feasible to run a full-node (maybe not a mining node) on commodity hardware
- Initial blockchain processing, and then block processing must use RAM only

As commodity hardware is pretty limited in RAM, the idea is not to store the state for full-nodes at all. The scheme is as follows:

1. The state is authenticated with the help of a 2-party dynamic authenticated dictionary.
1. A mining node is storing the whole state. When packing transactions into a block, it generates proofs of the authenticated state transformations and announces a new root hash after the transformations being done in a blockheader. Proofs are to be included into the block.
1. A full-node receiving the block checks that 1) Transactions are correct (format and signatures are correct etc) 2) State transformation operations derived from the transactions are corresponding to the proofs 3) Proofs are correct 4) Resulting roothash (a verifier is getting it just by processing proofs) is the same as the announced one. Thus the node is checking everything, but without holding the state (e.g. UTXO set).

Then the paper is about to find a most efficient structure out of many candidates (and the winner is custom-tailored authenticated AVL+ trees).

Not mentioned in the paper but worth mentioning is that proofs in a block could be authenticated themselves (with the help of a Merkle tree which is perfect for static data) with a root hash included in a blockheader. Then if node is holding the state it could skip downloading proofs from the network, also there is possibility to prune them in the future (this scheme reminds me of the SegWit proposal for Bitcoin).

Proofs are adding a significant burden regarding block size (actually a proof can be longer than the corresponding transaction), so decreased throughput is to be considered seriously.

The code had been released [on GitHub](https://github.com/input-output-hk/scrypto "GitHub code") during RealWorldCrypto â€“ see the section on authenticated data structures. There are some possible further minor optimizations (possibly reducing proof size by few percent in total) we are now discussing.
