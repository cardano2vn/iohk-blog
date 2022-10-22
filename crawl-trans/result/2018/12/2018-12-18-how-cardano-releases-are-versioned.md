# A guide to how Cardano is versioned
### **Tatyana Valkevych, Darko Mijić, and Jacob Mitchell explain**
![](img/2018-12-18-how-cardano-releases-are-versioned.002.png) 18 December 2018![](img/2018-12-18-how-cardano-releases-are-versioned.002.png)[ Tatyana Valkevych](/en/blog/authors/tatyana-valkevych/page-1/)![](img/2018-12-18-how-cardano-releases-are-versioned.003.png) 6 mins read

![](img/2018-12-18-how-cardano-releases-are-versioned.004.png)[ Simplicity and Michelson - Input Output](https://ucarecdn.com/cb0054f1-4e81-4617-82c2-6a6a363270c7/-/inline/yes/ "Simplicity and Michelson - Input Output")

![Tatyana Valkevych](img/2018-12-18-how-cardano-releases-are-versioned.005.png)[](/en/blog/authors/tatyana-valkevych/page-1/)
### [**Tatyana Valkevych**](/en/blog/authors/tatyana-valkevych/page-1/)
Release Manager

Development

- ![](img/2018-12-18-how-cardano-releases-are-versioned.006.png)[](https://www.linkedin.com/in/tatyanavalkevych/ "LinkedIn")
- ![](img/2018-12-18-how-cardano-releases-are-versioned.007.png)[](https://twitter.com/tatyanavych "Twitter")
- ![](img/2018-12-18-how-cardano-releases-are-versioned.008.png)[](https://github.com/tatyanavych/ "GitHub")

![A guide to how Cardano is versioned](img/2018-12-18-how-cardano-releases-are-versioned.009.jpeg)

Cardano, the third-generation blockchain, is evolving. Cardano changes are planned as product increments within [Cardano development phases](https://cardanoroadmap.com/), and are implemented and released as Cardano software. In this blog, [product manager Darko Mijic](/en/team/darko-mijic/), [release manager Tatyana Valkevych](/en/team/tatyana-valkevych) and [devOps lead Jacob Mitchell](/en/team/jacob-mitchell/) clarify how Cardano is versioned as a blockchain product and as software, and the correspondence between them.
## **Versioning Cardano as a product and as software**
The Cardano *product* version reflects the evolution of Cardano as a sequence of new feature set deployments within a Cardano development phase, and uses the following versioning scheme of three numbers separated with dots:

**development\_phase.feature\_set-1.refinement**

where the refinement part can be omitted. For example, the Cardano version in production at the time of writing this article is 1.3.2, which means it is the second refinement of the fourth feature set for the first development phase.

Cardano is currently approaching the end of its first development phase called Byron.

Cardano development phases are:

1. **Byron (Cardano 1.N)** In the Byron phase a completely new cryptocurrency technology stack was designed and built, including entirely new code and the implementation of the first generation of Ouroboros, a provably secure proof of stake protocol (PoS) at its core. The settlement layer (Cardano SL) of Cardano was launched in a federated fashion with the system operated by [IOHK](/en/), [Cardano Foundation](https://cardanofoundation.org/en/), and [Emurgo](https://emurgo.io/). It enabled the launch of ada cryptocurrency and allowed users to transfer and trade ada.
1. **Shelley (Cardano 2.N)** The Shelley phase will transition the settlement layer of Cardano from a federated to a completely decentralized system which will allow all users to participate in the protocol, and get rewards for producing blocks by staking individually or within stake pools.
1. **Goguen (Cardano 3.N)** The Goguen phase will bring the second collection of protocols with the computation layer (Cardno CL) deployed as side-chains to Cardano with support for smart contracts.
1. **Basho (Cardano 4.N)** The Basho phase will be focused on performance, security, and scalability improvements. It will enable Cardano to scale to millions and billions of users.
1. **Voltaire (Cardano 5.N)** The final development phase, Voltaire, will add a treasury system and governance, enabling sustainability and self-sufficiency for Cardano.

So far we have released four main stable Byron releases, which are referred to as Cardano 1.0, Cardano 1.1, Cardano 1.2, and Cardano 1.3.

A new feature set implementation is delivered through a main stable release. In this case a release version may be represented by the first two numbers only: for example, Cardano 1.3 is the same as Cardano 1.3.0. Every main release may have subsequent refinement releases that include bug fixes and other improvements, but no new features. So far all main Cardano releases have been followed by refinement releases. It is important to stress that although a full Cardano product version consists of three numbers it does not follow [semantic versioning](http://semver.org).

The live Cardano product is represented by the latest software release, deployed on the Cardano mainnet. When a Cardano release is discussed on public channels it is the Cardano product version that is used by default. When we release a Cardano product increment we specify its software component versions in Release Notes on [daedaluswallet.io](https://daedaluswallet.io/release-notes/) and on GitHub [[Daedalus releases](https://github.com/input-output-hk/daedalus/releases), [Cardano SL releases](https://github.com/input-output-hk/cardano-sl/releases)]. Below we clarify the correspondence between Cardano product and Cardano software versions.

At the time of writing Cardano consists of the following two software components:

- [Cardano settlement layer (CSL)](/en/projects/cardano/) is a backend software component and its code lives in [Cardano SL repository](https://github.com/input-output-hk/cardano-sl). It is the implementation of the Cardano node with all required components such as networking and also the implementation of Cardano wallet and its API. Cardano SL is deployed on Cardano core and relay blockchain nodes, and it is also shipped as a backend software component with Daedalus frontend.
- [Daedalus](/en/projects/daedalus/) software component (D) is a desktop application for personal computers running Windows, Mac and Linux and its code lives in [Daedalus repository](https://github.com/input-output-hk/daedalus). It is a frontend for Cardano end users, and it ships with CLS component as its backend.

These software components are versioned according to the [semantic versioning](https://semver.org/) scheme most software follows, which consists of the three numbers **major.minor.patch** where:

- **major** is incremented when code changes are backwards incompatible
- **minor** is incremented when added functionality is backwards compatible 
- **patch** is incremented when only bugs are fixed in a backwards compatible manner

The Cardano 1.3.0 main release consisted of Cardano SL 1.3.0 and Daedalus 0.11.0, or symbolically can be written as:

C\_1.3.0 = CSL\_1.3.0 + D\_0.11.0

The Cardano 1.3.2 refinement release bundles Cardano SL 1.3.2 and Daedalus 0.11.2:

C\_1.3.2 = CSL\_1.3.2 + D\_0.11.2

Cardano SL and Daedalus software releases are tagged with their version tags in the [IOHK GitHub repository](https://github.com/input-output-hk/) (see [Cardano SL tags](https://github.com/input-output-hk/cardano-sl/tags) and [Daedalus tags](https://github.com/input-output-hk/daedalus/tags)).

Cardano SL and Daedalus software release versions are also currently reflected in the Daedalus installer file name and in the download link on the <https://daedaluswallet.io/download> page, for example, the Cardano 1.3.2 Windows installer has the name

**daedalus-0.11.2-cardano-sl-1.3.2-mainnet-windows-10311.exe**

which includes Daedalus version, Cardano SL version, network, OS, and the build number.

While so far the Cardano product version and Cardano SL version have coincided, this is not the case for the Cardano 1.4 release due to [backwards incompatible changes in the Cardano wallet API](/en/blog/backwards-incompatible-changes-in-cardano-1-4-wallet-api/). The wallet API is part of Cardano SL, and therefore due to these incompatible changes the *major* number of Cardano SL version has been incremented, and this resulted in [Cardano SL 2.0.0](https://github.com/input-output-hk/cardano-sl/blob/release/2.0.0/CHANGELOG.md). So, Cardano 1.4 consists of Cardano SL 2.0.0 and Daedalus 0.12.0:

**C\_1.4.0 = CSL\_2.0.0 + D\_0.12.0**
### **Conclusion**
There is a distinction between the Cardano product version and versions of the Cardano software components. While this has always been the case, Cardano 1.4 is the first release where the distinction is evident, so we wanted to explain exactly how the versioning works.

Cardano 1.4 release is the fifth main release of the Byron phase and consists of the two software components Cardano SL 2.0.0 and Daedalus 0.12.0 versioned according to the [semantic versioning](https://semver.org/). In the future, Cardano will include more components that will follow their own versioning schemes. For example, Cardano wallet is being rewritten as a standalone software component. The following phase in Cardano development Shelley will be versioned as Cardano 2.N.

Artwork, 

[](https://creativecommons.org/licenses/by/4.0/ "Creative Commons")

![Creative Commons](img/2018-12-18-how-cardano-releases-are-versioned.010.png)

[](http://www.beeple-crap.com)

Mike Beeple
## **Attachments**
![](img/2018-12-18-how-cardano-releases-are-versioned.004.png)[ Simplicity and Michelson - Input Output](https://ucarecdn.com/cb0054f1-4e81-4617-82c2-6a6a363270c7/-/inline/yes/ "Simplicity and Michelson - Input Output")
