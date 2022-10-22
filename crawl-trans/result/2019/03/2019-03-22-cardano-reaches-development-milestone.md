# Cardano reaches development milestone
### **Engineers conclude Byron phase as Shelley work progresses**
![](img/2019-03-22-cardano-reaches-development-milestone.002.png) 22 March 2019![](img/2019-03-22-cardano-reaches-development-milestone.002.png)[ Duncan Coutts](/en/blog/authors/duncan-coutts/page-1/)![](img/2019-03-22-cardano-reaches-development-milestone.003.png) 6 mins read

![Duncan Coutts](img/2019-03-22-cardano-reaches-development-milestone.004.png)[](/en/blog/authors/duncan-coutts/page-1/)
### [**Duncan Coutts**](/en/blog/authors/duncan-coutts/page-1/)
Technical Architect

Well-Typed

- ![](img/2019-03-22-cardano-reaches-development-milestone.005.png)[](mailto:duncan.coutts@iohk.io "Email")
- ![](img/2019-03-22-cardano-reaches-development-milestone.006.png)[](https://www.youtube.com/watch?v=TZGVgNsJSnA "YouTube")
- ![](img/2019-03-22-cardano-reaches-development-milestone.007.png)[](http://www.linkedin.com/in/duncancoutts "LinkedIn")
- ![](img/2019-03-22-cardano-reaches-development-milestone.008.png)[](https://github.com/dcoutts "GitHub")

![Cardano reaches development milestone](img/2019-03-22-cardano-reaches-development-milestone.009.jpeg)

The release of Cardano 1.5 marks the start of the shift from the Cardano Byron era to the Shelley era and is an excellent opportunity to describe the ongoing work for [Shelley and how the transition will happen](https://www.youtube.com/watch?v=g82tvyj4Tik&feature=youtu.be "Cardano 1.5 Road to Shelley Episode 20 - The Cardano Effect, youtube.com"). Roughly six months ago, we switched almost all our development efforts to the Shelley code base, and work has been progressing quickly ever since. The last major work in the Byron code base was completed for Cardano 1.4, and for 1.5 we limited work to only those changes required for a smooth transition to Shelley.

The Shelley code base is not just an extension to the Byron code base, but an entirely new foundation. For the Shelley era, we have taken the opportunity to strip back and rebuild the system, as well as including the new staking and delegation functionality. As a result, we have been able to remedy a number of architectural limitations in the Byron code, as well as engage in the [semi-formal software development](https://www.youtube.com/watch?v=wW1CI9zt1tg "IOHK PlutusFest 2019, Director of Engineering - Duncan Coutts Interview") approach that I keep discussing in my videos.

In particular, we now have formal mathematical specifications of the validation rules for the Byron and Shelley blockchain, and will present these specifications at the [IOHK summit in April](https://iohksummit.io/ "IOHK Summit 2018"). When development is complete, we will be able to provide evidence that the code correctly implements our specifications. This is an exciting step-change in system quality and will be a first for our industry.
## **A seamless transition**
We must, of course, manage the transition from Byron to Shelley very carefully. It is not just a significant change in the rules, but also a migration from one code base to another. We have gone to great lengths to ensure that the transition process will be as smooth as possible.

While you might expect the Shelly transition to involve a single hard fork, it will actually comprise two. It is worth emphasizing that while these are technically hard forks, they will not be disruptive in the way hard forks often are. The changes have been designed to use our existing update system and be minimally disruptive. For Daedalus users, it will be very much like any other update.

![Current Protocol](img/2019-03-22-cardano-reaches-development-milestone.010.png)

For both hard forks, we will deploy an update which includes the rules of the new era in an unactivated state, to be activated several weeks later. This is key to avoiding disruption at the hard fork: no software is updated at the moment of the hard fork itself. The software update happens earlier, and once everyone is ready we can smoothly activate the change.

The only difference between a hard fork and a regular update is that updating is compulsory between the software release and the hard fork activation. For Daedalus users, this happens via the standard software update system. Exchanges will have to upgrade manually, but they have several weeks to do so.
## **Why two hard forks?**
For technical reasons, the transition from Byron to Shelley is more straightforward if we go via an intermediate transitional era. There is one hard fork to enter the transitional era and then a second one to begin the Shelley era proper. The Byron era uses Ouroboros Classic, and the Shelley era uses Ouroboros Genesis (which is an extension of Ouroboros Praos). Both of these are complex protocols. For a single implementation of a full node to manage a hard fork smoothly it is necessary for it to implement the rules both before and after the hard fork. A direct hard fork from Byron to Shelley would require a single implementation to understand Ouroboros Classic, Ouroboros Genesis, and all of the other validity rules â€“ which is a very complicated prospect indeed.

Not only that, but the Byron version of Ouroboros Classic has some additional complexity that would need to be replicated in a new implementation to preserve perfect consensus. Instead, we are using Ouroboros BFT, a simple variant of Ouroboros, for the transitional era. This means that the Byron code base only has to understand Ouroboros Classic and Ouroboros BFT, while the Shelley code base only has to understand Ouroboros BFT and Ouroboros Genesis. Neither one has to understand both Ouroboros Classic and Ouroboros Genesis. In particular, this means that the new Shelley code base does not need to replicate every detail of the Byron implementation of Ouroboros Classic, achieving a genuine reduction in complexity â€“ and in software development, complexity is the enemy.
## **A transitional era**
So this explains what the Cardano 1.5 release is really for: it is the release in which the Byron code base begins to understands Ouroboros BFT, allowing us to complete the first managed hard fork in a few weeks' time. After the hard fork, we will be in the transitional era using Ouroboros BFT and will be able to start deploying the new code base over time as it is developed. This is the new code base that will be used for the Shelley releases later, but is initially still using Ouroboros BFT for perfect compatibility during the transition.

During this transitional period, we will also run [a testnet for delegation and staking](https://testnet.iohkdev.io/ "Cardano Testnets"). Initially, this testnet will use a subset of the Shelley rules, but we will update it over time until the full Shelley rules are implemented and any other issues uncovered by the testnet resolved.

Once we are satisfied with the full implementation of the Shelley rules, then we will deploy an update of the new code base on mainnet. A few weeks later we will activate the hard fork and then we are finally in the Shelley era on mainnet!

In summary, the Cardano 1.5 release is exciting not because of any major features, or the numerous incremental improvements in Daedalus, but because it is the milestone that marks the beginning of the end for Cardano Byron and the start of the transition process into Cardano Shelley.

Artwork, ![Creative Commons](img/2019-03-22-cardano-reaches-development-milestone.011.png)[](https://creativecommons.org/licenses/by/4.0/ "Creative Commons")IOHK | Agency & Dimitris Ladopoulos 
