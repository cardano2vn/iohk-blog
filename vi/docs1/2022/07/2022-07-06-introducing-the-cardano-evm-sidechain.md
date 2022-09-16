# Giới thiệu về Cardano EVM Sidechain

### **Cardano EVM Sidechain là một giải pháp mở rộng hoàn toàn phi tập trung được IOG triển khai. Hãy cùng tìm hiểu thêm về các tính năng, lợi ích và kế hoạch phát hành**

![](img/2022-07-06-introducing-the-cardano-evm-sidechain.002.png) 6 July 2022![](img/2022-07-06-introducing-the-cardano-evm-sidechain.002.png)[ Olga Hryniuk](/en/blog/authors/olga-hryniuk/page-1/)![](img/2022-07-06-introducing-the-cardano-evm-sidechain.003.png) 6 mins read

![Olga Hryniuk](img/2022-07-06-introducing-the-cardano-evm-sidechain.004.png)[](/en/blog/authors/olga-hryniuk/page-1/)

### [**Olga Hryniuk**](/en/blog/authors/olga-hryniuk/page-1/)

Technical Writer

Marketing &amp; Communications

- ![](img/2022-07-06-introducing-the-cardano-evm-sidechain.005.png)[](https://www.linkedin.com/in/olga-hryniuk-1094a3160/ "LinkedIn")
- ![](img/2022-07-06-introducing-the-cardano-evm-sidechain.006.png)[](https://github.com/olgahryniuk "GitHub")

![Introducing the Cardano EVM sidechain](img/2022-07-06-introducing-the-cardano-evm-sidechain.007.jpeg)

Cardano is growing. Expanding. The [Vasil upgrade](https://iohk.io/en/blog/posts/2022/07/04/cardano-s-approaching-vasil-upgrade-what-to-expect/) will open up even more opportunities for efficient development and usage of various DApps and DeFi products on Cardano.

Sidechains and layer 2 solutions are key to increasing scalability for projects building on Cardano. In this post, we discuss what sidechains are and how they contribute to an ecosystem of interconnected solutions. We also dive deeper into the unique features that make up the EVM sidechain built by Input Output Global, Inc (IOG).

## **Interoperability**

In a previous [blog post](https://iog.io/en/blog/posts/2022/04/28/interoperability-is-key-to-blockchain-growth/) we discussed how bridges, sidechains, and the AGIX ERC20 converter, enhance Cardano's interoperability, defined as a product or system's ability to understand and interact with other products or systems. When a blockchain network is interoperable, user data and assets generated in one network can be moved between other different networks.

Interoperability is a crucial consideration in decentralized ecosystems. Once users have the tools to reclaim ownership of their data, they will need infrastructure to enable sharing it with others across multiple interconnected networks. A global economy requires that users' tokens are no longer siloed in any single blockchain. Sidechains coupled with bridging protocols are the solutions that facilitate greater freedom of data movement in a decentralized digital economy.

![An example of different types of sidechains](img/2022-07-06-introducing-the-cardano-evm-sidechain.008.png)

Figure 1. An example of different types of sidechains

### **Gia đình của sidechains**

Blockchains cannot succeed in isolation. No single blockchain will transform the entire digital infrastructure for the better, nor will a single blockchain revolutionize the way we share data, transact, or engage with others virtually. Over time there is a need for dedicated sidechains that enable a more diverse network of developers to join Cardano, and the tools needed to support the development of applications for specific use cases.

IOG có kế hoạch tạo ra một "Gia đình" gồm các Sidechain để mang lại khả năng mở rộng, khả năng tương tác và khả năng lập trình cao hơn cho Cardano. Một số đơn vị đóng góp trong hệ sinh thái cũng đang nỗ lực xây dựng các Sidechain của riêng họ để bổ sung thêm nhiều khả năng hơn nữa cho Cardano.

As Cardano evolves to support a multi-chain architecture, developers will be able to leverage the platform in the following ways:

- Use Plutus to create smart contracts and decentralized applications in a high-assurance, resource-efficient environment.
- Use the EVM sidechain to develop and deploy EVM-compatible smart contracts on Cardano (without paying the high gas fees typically found on Ethereum).
- Use the governance features of the EVM sidechain to create decentralized governance applications that optimize on-chain governance and voting experience.

## **Cardano EVM sidechain**

The EVM sidechain will be the first sidechain built and released by IOG, with the goal of opening Cardano up to Solidity developers. The EVM sidechain will allow the Solidity developer community to build DApps on a lower-fees and [environmentally friendly](https://iog.io/en/blog/posts/2021/08/17/why-they-re-calling-cardano-the-green-blockchain/) platform that consumes far less energy than proof-of-work blockchains.

**How does it work?**

Ethereum Virtual Machine (EVM) is a piece of software developed by Ethereum to help computers run smart contracts. Every full Ethereum node runs an instance of the EVM to define how the machine state will change with every new block added to the chain. Sidechains built using the EVM offer features equivalent to the Ethereum blockchain for processing and executing smart contracts. These EVM sidechains are also capable of implementing new features, like a different consensus protocol or ledger model, while still retaining essential EVM scripting capabilities.

### **Key features of the Cardano EVM sidechain**

The main features of the EVM sidechain are:

**Ethereum compatibility:**

- **Hard fork compatibility**. The EVM sidechain will retain compatibility with Ethereum hard forks. This is essential to ensure that the EVM sidechain remains interoperable with Ethereum and other tools and applications built on its network.
- **Developer tool compatibility**. Ethereum developer tools are widely used for asset storage, reading the state of the ledger, monitoring analytics, and more. EVM sidechain users will have access to these tools from the Cardano ecosystem. This creates a lower barrier to entry for Solidity developers looking to build on Cardano.
- **Web3.js wallet compatibility**. Web3 technology provides users with complete control over their own data. This means no involvement of third-party corporations owning usersâ€™ personal data. Web3 wallets are known for ensuring user anonymity and data protection while interacting with DApps.

**Ouroboros consensus protocol**

The EVM sidechain will replace Ethereumâ€™s proof-of-work consensus algorithm with Ouroboros Byzantine Fault Tolerance (OBFT) consensus protocol. OBFT is an implementation of Ouroboros that is able to tolerate Byzantine faults. OBFT offers good transaction processing at full network speed and instant transaction confirmation as well as proof of settlement.

Consensus is typically dependent on a fixed number of its validators (nodes), and the OBFT protocol does not presume that nodes can be dynamic. The EVM sidechain expands the initial OBFT protocol to allow for a *dynamic validator set*. Dynamism will come from committee rotation, but the pool size will stay fixed. The Cardano ledger enables the dynamic validator set feature by acting as a single source of truth to help in the selection of block-producing nodes.

**Permissionless approach**

Decentralization is one of the cornerstones of the digital trust economy. The transparency of blockchain technology inhibits fraud. In order to build a truly decentralized network, it is essential to make sure that the network is permissionless. Permissionless blockchains grant everyone the privilege to take part in network activities without dependence on centralized or federated authority. The EVM sidechain will be a permissionless network.

**Security**

The EVM sidechain includes several features to maintain security, including:

- **State observation**: after spinning up a sidechain validator node, these nodes are able to read the ada stake delegation distribution from the main chain.
- **Validator selection**: a deterministic algorithm is run for all candidates that are eligible and committees are selected by that algorithm.
- **Block production**: validators selected to be a part of the block-producing committee receive rewards for their work.
- **Validator rollover**: after a set interval, a new committee begins producing blocks replacing the previous one (Validator selection is algorithmic and deterministic).

## **The roadmap**

Cardanoâ€™s EVM sidechain is being developed iteratively. As with any other product launch, an iterative approach and performance assessments are necessary to ensure that everything works as intended.

Initial testnet delivery will set the foundation for the EVM sidechain assessments and testing, followed by a passive and active sidechain launch, culminating in mainchain deployment:

![EVM sidechain roadmap](img/2022-07-06-introducing-the-cardano-evm-sidechain.007.jpeg)

Figure 2. Stages of the EVM sidechain deployment

Weâ€™ll be talking about the Cardano EVM sidechain in more detail over the coming months.

*Meanwhile, you can request early access to the EVM sidechain alpha testnet, by filling out [this form](https://alpha-evm-sidechain.iohk.io/). Check out the EVM sidechain [demo](https://www.youtube.com/watch?v=NFxoi3YItEM) to see a smart contract deployed on testnet!*

*Tôi muốn cảm ơn Kathryn Stacy và Dominika Bukowska đã đóng góp ý kiến và hỗ trợ trong việc tạo bài đăng trên Blog này.<br><br>Bài này được dịch bởi Nguyễn Văn Tú [với bài gốc] (https://iohk.io/en/blog/posts/2022/07/06/introducing-the-cardano-evm-sidechain/), kiểm duyệt bởi tienna *Dự án này được tài trợ bởi Catalyst**
