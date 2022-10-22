# Taking the next step on the road to Cardano Shelley
### **Networking coming to Jörmungandr testnet in September, paving the way for stake delegation and real ada incentives later this year. Piece written in collaboration with Eric Czuleger and Tim Harrison.**
![](img/2019-09-06-taking-the-next-step-on-the-road-to-cardano-shelley.002.png) 6 September 2019![](img/2019-09-06-taking-the-next-step-on-the-road-to-cardano-shelley.002.png)[ Nicolas Di Prima](/en/blog/authors/nicolas-di-prima/page-1/)![](img/2019-09-06-taking-the-next-step-on-the-road-to-cardano-shelley.003.png) 4 mins read

![Nicolas Di Prima](img/2019-09-06-taking-the-next-step-on-the-road-to-cardano-shelley.004.png)[](/en/blog/authors/nicolas-di-prima/page-1/)
### [**Nicolas Di Prima**](/en/blog/authors/nicolas-di-prima/page-1/)
Software Engineer

Engineering

- ![](img/2019-09-06-taking-the-next-step-on-the-road-to-cardano-shelley.005.png)[](https://www.linkedin.com/in/nicolas-di-prima-1b97224b/?locale=en_US "LinkedIn")
- ![](img/2019-09-06-taking-the-next-step-on-the-road-to-cardano-shelley.006.png)[](https://twitter.com/nicolasdiprima "Twitter")
- ![](img/2019-09-06-taking-the-next-step-on-the-road-to-cardano-shelley.007.png)[](https://github.com/nicolasdp "GitHub")

![Taking the next step on the road to Cardano Shelley](img/2019-09-06-taking-the-next-step-on-the-road-to-cardano-shelley.008.jpeg)

Imagine a blockchain that can connect the world, yet doesn’t need to consume the same amount of energy as Denmark. A currency where the bookkeepers are also the users. A cryptocurrency that is truly decentralized. Jörmungandr is not only a [big mean serpent](https://en.wikipedia.org/wiki/J%C3%B6rmungandr), but also the serpent that in ancient myth holds the waters of the world together. It is global, and it surrounds the earth and every one of its inhabitants. Similarly, the Shelley testnet program and its Rust node (codenamed Jörmungandr) has been designed to connect people from all around the world.

In June, we delivered the first testnet build of Jörmungandr. This ‘self-node’ phase was focused on the single instance implementation, to refine the codebase and ensure that it was robust. It was important to get non-network functionality right before starting the next phase, but we also wanted to provide some of the core network protocols in that early code (hence calling it ‘blockchain in a box’). We’ve had some excellent support from the community, especially the folks on the [Stakepool Telegram channel](https://t.me/CardanoStakePoolWorkgroup). Every piece of feedback has helped us improve the protocol, the ledger, and the node itself. 

It was also a good opportunity for people to test and experiment with the interfaces and the software development kit (SDK). We released the first version at the end of last month and thanks to your feedback and contribution, it is continuously being improved, adding in more features than ever. We will soon be adding new working examples to showcase what can be done with the SDK. We believe these can provide important starting points for great community-driven projects.
## **Joining up the network**
As Charles outlined in his [recent AMA](https://youtu.be/bmkQDlhsNGc?t=104), we will soon enter Phase 2 of the testnet rollout: network implementation. Now that the node is more stable, we can challenge the network stack to see how it holds up and check how our predictions on its behavior measure up. And that means more experimentation with the community, with you.

Throughout this testnet program, the approach has been steady and methodical. Similarly, networking rollout will start gradually, working closely with the stake pool task force to identify and address any initial bugs or code irregularities. Meanwhile, we’ll be creating some documentation to help everyone get involved. As ever, you’ll be able to track our progress via GitHub and download early code if you'd like. Once we have established a network of nodes stable enough for open experimentation, we’ll encourage everyone to join in.

Again, the goal here is to test and iterate until we are confident we have a stable network. Your support and feedback during this process will be invaluable – whether you are there from the beginning or choose to join the network phase later on. 
## **Adding incentives to the testnet**
When Phase 2 is complete, we will have a stable network: a decentralized testnet platform running across multiple nodes. Then we will commence the third and final phase, the incentivized testnet. 

In reality, this is more than a testnet. Instead, it will effectively be a replica of the Cardano mainnet. We will take a UTXO snapshot of the mainnet state and migrate it to the testnet, offering Shelley era functionality within a controlled, sandboxed environment. This will be different from a typical testnet, however, since it will offer real rewards for delegating your ada stake. Jörmungandr will be decentralized, and users will be able to create stake pools or delegate their stake to a stake pool and collect their rewards. We’ll be sure to bring you further details of how this will all work a little further down the line. 

Once we are happy the protocol is stable enough to survive the harsh competition of the real world, we will merge the incentivized testnet rewards back into the Cardano mainnet. All the rewards generated during the Jörmungandr incentivized testnet will become real, live, spendable ada on the Cardano mainnet (so don't lose the mnemonics of your stake keys!).  Doing it this way will give us a realistic test of how the incentives model drives stakeholder and stake pool behavior, not to mention that stakeholders will be able to start getting rewards for holding their ada.

Cardano has a very exciting few months ahead – we’re looking forward to you joining us on the journey.

If you are interested in running a stake pool and would like to get the very latest news on the testnet program, you can sign up for our weekly report newsletter by visiting the form [here](https://forms.gle/JqPjdMkR58tzj4Mn6). Or just visit the Cardano Forum where you’ll find [progress updates](https://forum.cardano.org/t/shelley-testnet-your-weekly-rollout-rollup-week-ten-w-e-30th-august-2019/26154) every week. 
