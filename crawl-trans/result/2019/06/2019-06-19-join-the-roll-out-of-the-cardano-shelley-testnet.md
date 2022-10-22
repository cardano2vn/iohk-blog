# Join the roll out of the Cardano Shelley testnet
### **Take part in our testing program**
![](img/2019-06-19-join-the-roll-out-of-the-cardano-shelley-testnet.002.png) 19 June 2019![](img/2019-06-19-join-the-roll-out-of-the-cardano-shelley-testnet.002.png)[ David Esser](/en/blog/authors/david-esser/page-1/)![](img/2019-06-19-join-the-roll-out-of-the-cardano-shelley-testnet.003.png) 6 mins read

![David Esser](img/2019-06-19-join-the-roll-out-of-the-cardano-shelley-testnet.004.png)[](/en/blog/authors/david-esser/page-1/)
### [**David Esser**](/en/blog/authors/david-esser/page-1/)
Senior Product Manager

Cardano

- ![](img/2019-06-19-join-the-roll-out-of-the-cardano-shelley-testnet.005.png)[](https://www.linkedin.com/in/davidesser/ "LinkedIn")
- ![](img/2019-06-19-join-the-roll-out-of-the-cardano-shelley-testnet.006.png)[](https://github.com/davidesser "GitHub")

![Join the roll out of the Cardano Shelley testnet](img/2019-06-19-join-the-roll-out-of-the-cardano-shelley-testnet.007.jpeg)

Many of you will have seen us talk about our [testnets](https://testnet.iohkdev.io/), where we run the versions of Cardano and other testing simulators so we can test our products and get feedback from the community. Some of you have already been playing with the code from our GitHub repos. So as we move from the Byron to the Shelley era, we want to extend that collaboration and learn more from the great talent in our Cardano community.

With the Rust codebase for Shelley now nearing primetime, weâ€™re asking the community to help us build out a testnet. The Shelley era is all about decentralization, so weâ€™re taking a more decentralized approach to testing and documentation. Itâ€™s an important step in expanding the Cardano technical community and ultimately preparing everyone for the day when the community takes over the blockchain. 

For some time, there has been a dedicated and vibrant best practice group on [Telegram](https://t.me/CardanoStakePoolWorkgroup) Â â€“ the Stake Pool Best Practices Telegram group (1,733 members). Thereâ€™s clearly a lot of talent and interest out there. We recently pinned a survey in the channel to learn more about potential stake pool operators. Weâ€™ve had a really positive response, with over 150 full responses so far.

Whatâ€™s the range of technical skills and knowledge in the community? What are peopleâ€™s particular interests in staking? Are they keen hobbyists or entrepreneurs with plans to run a stake pool as a business? What equipment are they planning to use? Would marketing or other business support be useful? We asked lots of questions to learn as much as we could. Ultimately, our goal is to find out how we can support the community in implementing Shelleyâ€™s decentralized model in the most effective way we can. It is these people whoâ€™ll be helping to kick things off.

So, weâ€™ve started harnessing the power of the Cardano community to roll out a staking testnet. Weâ€™ll be supporting this early group along the way in a number of ways. 

Thereâ€™s now a dedicated 

[](https://github.com/input-output-hk/shelley-testnet "Shelley Testnet, github.com")

code repository and log to support the test program, all open. We will soon release new Shelley 

[](https://testnet.iohkdev.io/cardano/ "testnet.iohkdev.io/cardano/")

testnet webpages on our Cardano testnets website. Weâ€™ll publish instructions, videos, tutorials and so on explaining what to do and how to do it. We're writing a pretty good set of documentation for the Rust client. There will be instructional videos on how to install and operate the node as well as report bugs and log issues using GitHub.

A key part of the testing program will be working with people with mixed levels of technical experience, working across different platforms and configurations. The feedback from this group will ultimately make our technology easier to install, configure, and operate for everyone who follows.

The testnet will have a series of releases rolling out in three main phases.
## **Phase 1: The self node, aka â€˜blockchain in a boxâ€™**
The first stage is all about setting up and hosting a â€˜self nodeâ€™. You can think of a self node as â€˜blockchain in a boxâ€™, a minimum viable product (MVP) for testing key capabilities. This is basically a set of tools and documentation to bootstrap your own genesis block and run a multi-node environment on your own machine, where you can see how stake pools actually operate. Itâ€™s like a complete network within a single instance.

Weâ€™ll provide instructions and invite people to run the node through various configurations and give us feedback on what they find. 

But what about the network? Isnâ€™t this supposed to be a decentralized solution weâ€™re testing? Well, although weâ€™re starting with the self node, weâ€™ve coded things so you can implement more features against this self node down the line. So, as we add more functionality â€“ namely the network and incentives components â€“ the code developed against the self node won't have to change much or at all. Thatâ€™s the plan! 

So, the first phase is about establishing the basic configuration for your set-up that gives a sense of how well things are working locally. The early code will contain just the core functionality, designed to explore the fundamental capabilities. Across the stake pool task force, weâ€™ll be learning about operating on different hardware, operating systems, cloud hosting environments, and technical skill levels. We'll get a much broader set of results data by collaborating with the task force. Â 
## **Phase 2: Connecting the network**
Once weâ€™re happy with phase 1, and have a robust set of self nodes up and running, weâ€™ll start connecting them up. The goal will be to create a single, unified testnet and to add more nodes as we go, scaling the network step by step. So, instead of experimenting within your own instance, youâ€™ll now be moving to a system where youâ€™re talking to nodes across the internet. You're gossiping, you're downloading blocks from peers. And then weâ€™ll be learning from a whole new set of behaviors and potential risk scenarios.
## **Phase 3: The incentives system**
This is where we add in a networked incentive system. Moving blocks around is all very well. But Shelleyâ€™s true potential will be realized with staking. This is about demonstrating how staking rewards will go to the stake pools to encourage that.

So, at a high level, that's what youâ€™ll see in the coming months. We'll also be working closely with the folks at EMURGO on this. Theyâ€™ll be helping with testing and also ensuring that their Yoroi wallet has all this interoperability. [Seiza, their new blockchain explorer](https://emurgo.io/#/en/blog/seiza-all-new-cardano-ada-blockchain-explorer-developed-by-emurgo), will be a great tool for visualizing a lot of the things that we do that are unique in our ecosystem.

This testing program is an experiment in community collaboration. Thereâ€™ll be a lot of testing, re-coding, improving documentation and training materials, tweaking, and so on along the way. Weâ€™ll be checking the integrity of individual components as well as demonstrating that those components play with each other nicely. The objective is clear, but itâ€™ll be interesting to see how we get there. Weâ€™re committed to it because it fits: a decentralized process to test a decentralized system. And a broad collaboration with the community to test a system that will be owned by the community.

Weâ€™ll keep you all posted. For those who choose to step up and work with us in the program, a sincere thanks in advance to you for your partnership.
