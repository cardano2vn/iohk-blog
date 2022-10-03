# Xử lý đồng thời: Hợp đồng thông minh của Cardano và mô hình EUTXO

### **Mô hình EUTXO của Cardano cung cấp một môi trường an toàn và linh hoạt để xử lý đa tác vụ mà không gây lỗi hệ thống**

![](img/2021-09-10-concurrency-and-all-that-cardano-smart-contracts-and-the-eutxo-model.002.png) Ngày 10 tháng 9 năm 2021 ![](img/2021-09-10-concurrency-and-all-that-cardano-smart-contracts-and-the-eutxo-model.002.png)[ Olga Hryniuk](tmp//en/blog/authors/olga-hryniuk/page-1/) ![](img/2021-09-10-concurrency-and-all-that-cardano-smart-contracts-and-the-eutxo-model.003.png) 7 phút đọc

![Olga Hryniuk](img/2021-09-10-concurrency-and-all-that-cardano-smart-contracts-and-the-eutxo-model.004.png)[](tmp//en/blog/authors/olga-hryniuk/page-1/)

### [**Olga Hryniuk**](tmp//en/blog/authors/olga-hryniuk/page-1/)

Technical Writer

Marketing &amp; Communications

- ![](img/2021-09-10-concurrency-and-all-that-cardano-smart-contracts-and-the-eutxo-model.005.png)[](https://www.linkedin.com/in/olga-hryniuk-1094a3160/ "LinkedIn")
- ![](img/2021-09-10-concurrency-and-all-that-cardano-smart-contracts-and-the-eutxo-model.006.png)[](https://github.com/olgahryniuk "GitHub")

![Xử lý đồng thời: Hợp đồng thông minh của Cardano và mô hình EUTXO](img/2021-09-10-concurrency-and-all-that-cardano-smart-contracts-and-the-eutxo-model.007.jpeg)

Cardano is a UTXO-based blockchain, which utilizes a different programming paradigm for decentralized applications (DApps) from other account-based blockchains like Ethereum. The specific flavor Cardano uses is the [Extended Unspent Transaction Output (EUTXO) model](https://iohk.io/en/blog/posts/2021/03/11/cardanos-extended-utxo-accounting-model/) introduced by the Alonzo upgrade. EUTXO offers greater security allowing for smart contract execution cost predictability (without unpleasant surprises) and, as a result, offers a different approach to parallelization.

EUTXO inherits the per-branches design of the UTXO (Bitcoin) model, where one branch is by definition a sequence of transactions that requires a sequence of validations. To split the logic across different branches and enforce more parallelism, it is essential to build DApps and other solutions using *multiple UTXOs*. This provides benefits in terms of scaling, just like developing Bitcoin services prerequisites splitting one wallet into sub wallets.

DApps built on Cardano are **not limited** to one transaction per block. In fact, the block budget (that is the maximum number of transactions it can hold) allows the execution of hundreds of simple transactions and several complex scripts. However, the EUTXO model allows spending a transaction output only once. Given that users can face contention issues trying to access the same UTXO, it is important to use many different UTXOs. Note that this is important unless such a design would benefit from a strict ordering of clients. Sets of UTXOs can be used to implement design patterns that include semaphores. In addition, different users can interact with one smart contract without any concurrency failure. That is because a smart contract can handle *a number of different UTXOs* that make up its current state and off-chain metadata that allows interpreting those UTXOs.

## **Thực thi song song**

Các blockchain đạt được tính bất biến và minh bạch trong quá trình xử lý giao dịch theo nhiều cách khác nhau. Bất kỳ hệ thống blockchain nào cũng phải sở hữu một tập hợp các thuộc tính để đáp ứng nhu cầu ngày càng tăng về xử lý hoạt động an toàn nhưng nhanh chóng, cụ thể là:

- **Thông lượng** - số lượng hoạt động mà hệ thống có thể thực hiện trong một khoảng thời gian nhất định. Ví dụ: liên quan đến số lượng giao dịch hoặc hợp đồng thông minh được xử lý trong một giây.
- **Hiệu suất** - hệ thống hoạt động nhanh như thế nào. Hiệu suất đo lường thời gian thực hiện giao dịch hoặc hợp đồng thông minh.
- **Khả năng mở rộng** - khả năng hệ thống thực hiện nhiều hoạt động mà không xảy ra quá tải mạng hoặc ảnh hưởng đến các thuộc tính hiệu suất.

By increasing parallelism, we can ultimately improve the throughput of the system while keeping the performance of individual operations the same, but this sort of scalability will always be limited by the degree of contention.

When it comes to scalability, we also distinguish such system properties as *concurrency*, *parallelism*, and *contention*. Concurrency is essential to allow multiple actors to progress on a certain task without interfering with each other. Parallelism allows such progress *at the same time* without any interference. Contention occurs when those multiple actors interfere with each other while working either concurrently or in parallel.

## **Hiểu về tính đồng thời**

Tính đồng thời có thể hoặc không giúp cải thiện hiệu suất, thông lượng hoặc khả năng đáp ứng của hệ thống. Số lượng các tác vụ đồng thời bị giới hạn bởi số lượng tối đa các hoạt động đồng thời có thể được thực hiện.

Để đạt được những cải thiện về hiệu suất *thực tế* trong một blockchain dựa trên UTXO, bộ xử lý hoặc các tác nhân khác phải có thể thực hiện nhiều tác vụ đồng thời. Mức độ đồng thời càng cao thì khả năng song song tối đa càng cao. Cách tiếp cận như vậy sẽ giúp cải tiến hiệu suất và thông lượng. Nó cũng cung cấp những lợi thế đáng kể so với các hệ thống dựa trên tài khoản (như Ethereum).

## ***Sự khác biệt* khi triển khai DApp trên sổ cái UTXO**

Cardano’s approach to DApp deployment is different and thus it requires a learning curve and a different approach. This is like working with different programming languages: there is one goal – to deploy a solution, but so many programming languages to use for this purpose.

Maximizing concurrency is a skill that needs to be learned: developers need to write code in a way that severely restricts the opportunities for contention (e.g., by avoiding shared states and accidental dependencies). The system must then translate this concurrency into parallelism. A number of developers have already identified ways to approach this, while others are still developing solutions. Simply transplanting lessons learned on one blockchain will not work; while the learning curve is a little steeper, the results make this worthwhile.

Either way, it is important to understand that to deploy a scalable DApp on Cardano, a developer can’t just use an adapted Ethereum contract. Cardano is based on the UTXO model; it is not account-based. And this means that a single on-chain state will not meet the concurrency property on Cardano. Instead, DApps should split up their on-chain state across many UTXOs. This will increase the concurrency in their application, thereby allowing higher throughput.

Our education team has previously shared a simple AMM-style DEX implementation in the Plutus Pioneer course. While this is useful for teaching purposes, this architecture would not directly support a commercial DEX where an order book approach and additional concurrency are required. A developer looking to deploy on the Cardano mainnet would need to improve the scalability of the architecture accordingly.

We proposed a solution within our recent [Djed stablecoin paper](https://iohk.io/en/research/library/papers/djeda-formally-verified-crypto-backed-pegged-algorithmic-stablecoin/). For the Djed implementation on Cardano, an order book modeling pattern is favored whereby an order maker is responsible for forwarding any minting or burning order to the stablecoin smart contract, with an additional incentive fee imposed on each would-be buyer or seller of stablecoins and reserve coins. Several security mechanisms – via the extensive use of non-fungible tokens (NFTs) – are also used to guarantee the uniqueness of transactions, the correctness of each submitted order, and to prevent front-running attacks. NFT tokens are also used to report successful or failed minting and burning orders. We’ll publish a fuller article on this shortly.

Để tìm hiểu thêm về khả năng mở rộng, bạn có thể đọc [cách thiết kế ứng dụng Plutus có khả năng mở rộng](https://plutus.readthedocs.io/en/latest/plutus/howtos/writing-a-scalable-app.html) và tìm hiểu cách tổ chức DApp trên Cardano bằng cách sử dụng [các mô hình sổ lệnh](https://plutus.readthedocs.io/en/latest/plutus/explanations/order-book-pattern.html). Các nhà phát triển cũng đã trình bày [các phương pháp tiếp cận tính đồng thời và tính xác định đối với kiến trúc hợp đồng thông minh EUTXO](https://medium.com/meld-labs/concurrent-deterministic-batching-on-the-utxo-ledger-99040f809706) có thể được coi là sự khái quát về các bước của máy trạng thái (state machine) thực thi song song được giới thiệu trong [bài nghiên cứu về Hydra](https://iohk.io/en/research/library/papers/hydrafast-isomorphic-state-channels/) để hiện thực hóa máy trạng thái đa bước (multi-step state machines). Một số [nhà phát triển](https://twitter.com/ErgoDex/status/1434241104015151105?s=20) và thành viên cộng đồng khác cũng đã xuất bản các bài nghiên cứu, [video](https://youtube.com/watch?v=TxnvYsBnLjQ) , [bài báo](https://sundaeswap-finance.medium.com/concurrency-state-cardano-c160f8c07575) và các [chủ đề](https://twitter.com/CardanoMaladex/status/1434960813006200835) hữu ích trên Twitter đưa ra các phương pháp tiếp cận của họ. Đây là một bài học tuyệt vời về cách mà cộng đồng sẽ tiếp tục phát triển các giải pháp sáng tạo của riêng mình, cũng như các phương pháp tiếp cận trở nên chuẩn hóa hơn với sự trưởng thành của nền tảng.

## **Moving forward**

The Alonzo hard fork event will introduce the core building blocks of Plutus 1.0. This is the beginning of ecosystem growth. Although it is still early, the Alonzo testnet allows our developers to assess system properties and build scalable DApps in advance – preparing for their mainnet launch. Dozens of projects have already been working with local instances of Plutus environments. With the main public testnet soon supporting smart contracts, we expect a significant ramping up of activity over the next few weeks and in the months ahead. Later this month, the [Cardano summit](https://summit.cardano.org/) (25-26 September) will showcase many of these projects, plus provide important updates on the smart contracts roadmap and the ongoing evolution of the technology stack. Developer events, hackathons, and, of course, the results of Project Catalyst will continue to bring new tools and abstractions to this fast-growing developer ecosystem.

If you are a developer, make sure to join our [Discord community](https://discord.gg/ScxDkrxpBg) and get involved with [Project Catalyst](https://cardano.ideascale.com/a/index) if you are looking to fund your project.

*I'd like to acknowledge [Lars Brünjes](https://github.com/brunjlar), [Jann Müller](https://github.com/j-mueller), and [Manuel Chakravarty](https://github.com/mchakravarty) for their technical input and support during the blog post preparation.*
