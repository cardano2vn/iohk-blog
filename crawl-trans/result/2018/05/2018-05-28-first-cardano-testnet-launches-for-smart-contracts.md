# First Cardano smart contracts testnet launches
### **KEVM software supports applications that run on Ethereum Virtual Machine**
![](img/2018-05-28-first-cardano-testnet-launches-for-smart-contracts.002.png) 28 May 2018![](img/2018-05-28-first-cardano-testnet-launches-for-smart-contracts.002.png)[ Gerard Moroney](/en/blog/authors/gerard-moroney/page-1/)![](img/2018-05-28-first-cardano-testnet-launches-for-smart-contracts.003.png) 3 mins read

![Gerard Moroney](img/2018-05-28-first-cardano-testnet-launches-for-smart-contracts.004.png)[](/en/blog/authors/gerard-moroney/page-1/)
### [**Gerard Moroney**](/en/blog/authors/gerard-moroney/page-1/)
Chief Operating Officer

Operations

- ![](img/2018-05-28-first-cardano-testnet-launches-for-smart-contracts.005.png)[](mailto:gerard.moroney@iohk.io "Email")
- ![](img/2018-05-28-first-cardano-testnet-launches-for-smart-contracts.006.png)[](https://ie.linkedin.com/in/gmoroney "LinkedIn")
- ![](img/2018-05-28-first-cardano-testnet-launches-for-smart-contracts.007.png)[](https://twitter.com/gmanroney "Twitter")
- ![](img/2018-05-28-first-cardano-testnet-launches-for-smart-contracts.008.png)[](https://github.com/gmanroney "GitHub")

The first Cardano smart contracts testnet [launches today](https://testnet.iohkdev.io/goguen/ "https://testnet.iohkdev.io/goguen/"), the KEVM testnet, a correct by construction version of the Ethereum Virtual Machine (EVM) specified in the K framework. This technology, produced by Runtime Verification with the support of IOHK, is the first time that a complete formal semantics of the EVM have been produced. This is an important first in cryptocurrency that is a necessary step towards the promise of third-generation blockchains. A smart contract allows you to exchange something of value - money, property, shares - by means of a software protocol. The terms of exchange are agreed upon by the parties involved in the same way as a traditional contract, and the contract is executed automatically on the blockchain.

Developers will be able to take any application that runs on the EVM and execute it on the KEVM, which can also be used to rigorously prove that smart contracts work correctly. This is done by formally specifying a contract's desired properties in K, combining the contract with the KEVM specification, and then using the K framework to verify those properties.

Our second Cardano testnet to launch will be IELE, which is a new virtual machine for Cardano. IELE will be launched in July and is a register-based virtual machine similar to LLVM with an unbounded number of registers, that supports unbounded integers. With IELE, developers can write, compile and execute smart contracts, with improved security and performance compared to the KEVM testnet.

For now, we recommend that developers use the Solidity language on both testnets. However, the vision is that eventually smart contracts will be written in high-level languages that translate to IELE, such as new languages like Plutus ([being developed by IOHK](https://youtu.be/YMkFBw9F4rI?t=34m17s "IOHK Developers meetup for Cardano, University College London, youtube.com")), but also existing languages such as Java or Python, and then IELE-to-IELE translators ensure the resulting code is optimal.

![Cardano Testnets Website](img/2018-05-28-first-cardano-testnet-launches-for-smart-contracts.009.png) Cardano Testnets Website

K was developed by Runtime Verification in collaboration with Professor Grigore Rosu's Formal Systems Laboratory at the University of Illinois at Urbana-Champaign during the past 15 years, and incorporates the state of the art in language design, semantics and formal methods. Read more about the K framework [in this blog](https://runtimeverification.com/blog/k-framework-an-overview/ "Runtime Verification blog") from Prof Rosu, founder of Runtime Verification. A blog about formal verification and what this means for smart contracts will follow soon.

Smart contracts must be formally verified, so they run exactly as specified and are free from bugs or flaws. Only then can they be widely adopted as financial infrastructure that can be relied upon by billions of people.

We look forward to receiving your valuable feedback about using the testnets which will help us make Cardano best in class.
