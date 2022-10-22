# IELE: A New Virtual Machine for the Blockchain
### **Specialized smart contract execution on the blockchain**
![](img/2017-12-15-iele-a-new-virtual-machine-for-the-blockchain.002.png) 15 December 2017![](img/2017-12-15-iele-a-new-virtual-machine-for-the-blockchain.002.png)[ Grigore Rosu](/en/blog/authors/grigore-rosu/page-1/)![](img/2017-12-15-iele-a-new-virtual-machine-for-the-blockchain.003.png) 8 mins read

![](img/2017-12-15-iele-a-new-virtual-machine-for-the-blockchain.004.png)[ IELE- A New Virtual Machine for the Blockchain - Input Output](https://ucarecdn.com/0dc38324-8874-47e4-9376-d03adaa32a42/-/inline/yes/ "IELE- A New Virtual Machine for the Blockchain - Input Output")

![Grigore Rosu](img/2017-12-15-iele-a-new-virtual-machine-for-the-blockchain.005.png)[](/en/blog/authors/grigore-rosu/page-1/)
### [**Grigore Rosu**](/en/blog/authors/grigore-rosu/page-1/)
President/CEO Runtime Verification

![IELE: A New Virtual Machine for the Blockchain](img/2017-12-15-iele-a-new-virtual-machine-for-the-blockchain.006.jpeg)

Runtime Verification (RV) is proud to release their first version of IELE, a new virtual machine for the blockchain.
## **What is IELE?**
IELE is a variant of [LLVM](http://llvm.org/ "llvm.org") specialized to execute smart contracts on the blockchain. Its design, definition and implementation have been done at the highest mathematical standards, following a semantics-first approach with verification of smart contracts as a major objective. Specifically, we have defined the formal syntax and semantics of IELE using the K framework, which in return gives us an executable reference model in addition to a series of program analysis tools, including a program verifier. K was created by our team during the last 15 years and incorporates the state of the art in language design, semantics and formal methods. The design of IELE was based on our experience with formally defining [dozens of languages in K](https://github.com/kframework "K Framework, Github"), but especially on recent experience and lessons learned while formally defining two other virtual machines in K, namely:

- [KEVM](https://github.com/kframework/evm-semantics "EVM Semantics, Github"), our semantics of the [Ethereum Virtual Machine](https://github.com/ethereum/yellowpaper "Ethereum Virtual Machine Yellow Paper") (EVM); and
- KLLVM, our semantics of [LLVM](http://llvm.org/ "llvm.org"); the latest version of the LLVM semantics will be made public when complete and published, but an earlier version [is available](https://github.com/kframework/llvm-semantics "LLVM Semantics").

Unlike the EVM, which is a stack-based machine, IELE is a register-based machine, like LLVM. It has an unbounded number of registers and also supports unbounded integers. To get a feel for how IELE programs look like, here are two of them (these have not been verified yet and may change):

- [erc20.iele](https://github.com/runtimeverification/iele-semantics/blob/master/iele-examples/erc20.iele "IELE Examples, erc20") - a IELE implementation of an ERC20 token
- [forwardingWallet.iele](https://github.com/runtimeverification/iele-semantics/blob/master/iele-examples/forwardingWallet.iele "forwardingwallet.iele, Github") - a wallet implementation that creates and calls into another contract
## **Design Rationale**
Here are the forces that drove the design of IELE:

1. To serve as a uniform, lower-level platform for translating and executing smart contracts from higher-level languages. The contracts can interact with each other by means of an ABI (Application Binary Interface). The ABI is a core element of IELE, and not just a convention on top of it. The unbounded integers and unbounded number of registers should make compilation from higher-level languages more straightforward and elegant and, looking at the success of LLVM, more efficient in the long term. Indeed, many of the LLVM optimizations are expected to carry over. For that reason, IELE followed the design choices and representation of LLVM as much as possible. The team also includes LLVM experts from the University of Illinois (where LLVM was created).
1. To provide a uniform gas model, across all languages. The general design philosophy of gas calculation in IELE is "no limitations, but pay for what you consume". For example, the more registers a IELE program uses, the more gas it consumes. Or the larger the numbers computed at runtime, the more gas it consumes. The more memory it uses, in terms of both locations and size of data stored at locations, the more gas it consumes. And so on.
1. To make it easier to write secure smart contracts. This includes writing requirements specifications that smart contracts must obey as well as making it easier to develop automated techniques that mathematically verify / prove smart contracts correct with respect to such specifications. For example, pushing a possibly computed number on the stack and then jumping to it regarded as an address makes verification hard, and thus security weaker, with current smart contract paradigms. IELE has named labels, like LLVM, and jump statements can only jump to those labels. Also, it avoids the use of a bounded stack and not having to worry about stack or arithmetic overflow makes specification and verification of smart contracts significantly easier.

Like [KEVM](https://github.com/kframework/evm-semantics "EVM Semantics, Github"), the formal semantics of EVM that we previously defined, validated and evaluated using the [K framework](http://www.kframework.org/index.php/Main_Page "kframework.org"), the design of IELE was also done in a semantics-based style, using K. Together with a fast (LLVM-based) execution backend for K that is still under development, it is expected that the interpreter obtained automatically from the semantics of IELE will be sufficiently efficient to serve as a reference implementation of IELE.
## **What's next?**
To achieve the full potential of IELE, we plan to next work on the following:

- Efficient backend for K. Then K semantics, including IELE, can be executed at acceptable performance. As discussed in our KEVM paper, the current version of K can execute the EVM semantics at performance that stays within an order of magnitude from the performance of the [reference C++ implementation of the EVM](https://github.com/ethereum/cpp-ethereum/ "cpp-ethereum, Github"). We believe that we can improve the execution performance of K by one order of magnitude. If this is achieved, then there is no incentive to implement IELE in an ad-hoc way: the K executable semantics of IELE will also be its implementation, so it will be correct by construction and thus implementation defects of the VM itself cannot be exploited anymore. Also, IELE itself would be easier to maintain and future versions will be easier to deploy.
- Compilers/Translators from [Solidity](https://solidity.readthedocs.io/en/develop/ "Solidity Documentation") and [Plutus](https://cardanodocs.com/technical/plutus/introduction/ "Plutus Introduction, cardanodocs.com") to IELE. Writing smart contracts directly in IELE is a bit more feasible than in the EVM, because IELE follows the LLVM IR which was designed to be human-readable, but the IELE code is still low-level and thus error-prone. To properly test IELE and gain confidence in its overall design and capabilities, we will implement a compiler/translator from [Solidity](https://solidity.readthedocs.io/en/develop/ "Solidity Documentation") to IELE, also in K. Since [Plutus](https://cardanodocs.com/technical/plutus/introduction/ "Plutus Introduction, cardanodocs.com") rises as a star among the functional programming languages for smart contracts and since we are defining a [formal semantics of Plutus](https://github.com/kframework/plutus-core-semantics "Plutus Core Semantics, Github") as well, a compiler from Plutus to IELE will be developed immediately after Solidity's.
- Semantics-based compilation. In addition to improving K's performance, we plan to implement a tool that we call semantics-based compiler on top of K. See our previous [blog post](https://runtimeverification.com/blog/?p=459 "New Technologies for the Blockchain: IELE, runtimeverification.com") for details. The idea is to take a programming language semantics L and a program P in L, and generate (using symbolic execution heavily) a new language semantics L' which is a specialization of L for P. We expect at least one order of magnitude increase in performance. More importantly, this will give us a uniform mechanism to translate any programs in any programming languages that have a K semantics to IELE, thus making IELE and K into a universal platform for executing smart contracts in any language.
- Deploy IELE on the Cardano blockchain.
## **Technical Details and Download**
IELE is thoroughly commented and freely available under the UIUC license (as permissive as the MIT license) on Github:

- [IELE repository on Github](https://github.com/runtimeverification/iele-semantics "IELE Semantics, Github")

In addition to the two IELE programs mentioned above, erc20.iele and forwardingWallet.iele showing that the IELE code is human readable, the following links into the github repo will give a good idea what IELE is and how it differs from EVM and LLVM:

- [iele-syntax.md](https://github.com/runtimeverification/iele-semantics/blob/master/iele-syntax.md "IELE Textual Syntax") - the complete formal syntax of the IELE language.
- [iele.md](https://github.com/runtimeverification/iele-semantics/blob/master/iele.md "IELE Execution") - the complete formal executable semantics of the IELE language
- [Design.md](https://github.com/runtimeverification/iele-semantics/blob/master/Design.md "IELE Design") - the design rationale of IELE, as well as detailed comparisons with LLVM and EVM
- [iele-gas.md](https://github.com/runtimeverification/iele-semantics/blob/master/iele-gas.md "IELE Gas Calculation") - the current gas model of IELE (which is still to be tuned as we develop compilers to IELE)
## **Get involved**
In the spirit of open source, community-driven development, we will be holding all IELE discussions on our channels

- [#IELE:matrix.org](https://riot.im/app/#/room/#IELE:matrix.org "IELE Riot") on [Riot](https://about.riot.im/ "riot.im")
- [runtimeverification/iele-semantics](https://gitter.im/runtimeverification/iele-semantics "IELE Gitter") on [Gitter](https://gitter.im/ "Gitter")

We encourage any interested parties to engage us, ask questions, contribute code, or build experience with our tools. We are also always looking for contributors able to work on documentation, efficient install/quickstart process for new developers, and more examples and tests. We are hiring, and will be sure to keep an eye open for helpful contributors!

We will also be posting updates on our brand new Twitter page [@rv_inc](https://twitter.com/rv_inc "Runtime Verification on Twitter"), which we hope any interested developers will follow and interact with.

Let's build more secure smart contracts for everybody, together!
## **Acknowledgements**
We warmly thank [IOHK](https://iohk.io/ "iohk.io") for their generous funding support of both [IELE](https://github.com/runtimeverification/iele-semantics "IELE Semantics, Github") and [KEVM](https://github.com/kframework/evm-semantics "EVM Semantics, Github"). IELE, in particular, would have not been possible without IOHK's support, its continuous research meetings, and the stimulating technical discussions we had with their research team.

We also thank the K team who defined the [KEVM](https://github.com/kframework/evm-semantics "EVM Semantics, Github") semantics (see [technical report](https://www.ideals.illinois.edu/handle/2142/97207 "KEVM: A Complete Semantics of the Ethereum Virtual Machine"), too) and verified smart contracts for ERC20 compliance. Their effort and non-trivial proofs at the EVM level led to the quest for a new VM with better support for verification of smart contracts.

Artwork, [](https://creativecommons.org/licenses/by/4.0/ "Creative Commons")

![Creative Commons](img/2017-12-15-iele-a-new-virtual-machine-for-the-blockchain.007.png)[](https://creativecommons.org/licenses/by/4.0/ "Creative Commons")[](http://www.beeple-crap.com/resources.php)

[Mike Beeple](http://www.beeple-crap.com/resources.php)
## **Attachments**
![](img/2017-12-15-iele-a-new-virtual-machine-for-the-blockchain.004.png)[ IELE- A New Virtual Machine for the Blockchain - Input Output](https://ucarecdn.com/0dc38324-8874-47e4-9376-d03adaa32a42/-/inline/yes/ "IELE- A New Virtual Machine for the Blockchain - Input Output")
