# Concurrency and all that: Cardano smart contracts and the EUTXO model
### **Cardano’s EUTXO model provides a secure and versatile environment to process multiple operations without system failures**
![](img/2021-09-10-concurrency-and-all-that-cardano-smart-contracts-and-the-eutxo-model.002.png) 10 September 2021![](img/2021-09-10-concurrency-and-all-that-cardano-smart-contracts-and-the-eutxo-model.002.png)[ Olga Hryniuk](tmp//en/blog/authors/olga-hryniuk/page-1/)![](img/2021-09-10-concurrency-and-all-that-cardano-smart-contracts-and-the-eutxo-model.003.png) 7 mins read

![Olga Hryniuk](img/2021-09-10-concurrency-and-all-that-cardano-smart-contracts-and-the-eutxo-model.004.png)[](tmp//en/blog/authors/olga-hryniuk/page-1/)
### [**Olga Hryniuk**](tmp//en/blog/authors/olga-hryniuk/page-1/)
Technical Writer

Marketing & Communications

- ![](img/2021-09-10-concurrency-and-all-that-cardano-smart-contracts-and-the-eutxo-model.005.png)[](https://www.linkedin.com/in/olga-hryniuk-1094a3160/ "LinkedIn")
- ![](img/2021-09-10-concurrency-and-all-that-cardano-smart-contracts-and-the-eutxo-model.006.png)[](https://github.com/olgahryniuk "GitHub")

![Concurrency and all that: Cardano smart contracts and the EUTXO model](img/2021-09-10-concurrency-and-all-that-cardano-smart-contracts-and-the-eutxo-model.007.jpeg)

Cardano is a UTXO-based blockchain, which utilizes a different programming paradigm for decentralized applications (DApps) from other account-based blockchains like Ethereum. The specific flavor Cardano uses is the [Extended Unspent Transaction Output (EUTXO) model](https://iohk.io/en/blog/posts/2021/03/11/cardanos-extended-utxo-accounting-model/) introduced by the Alonzo upgrade. EUTXO offers greater security allowing for smart contract execution cost predictability (without unpleasant surprises) and, as a result, offers a different approach to parallelization. 

Cardano là một blockchain dựa trên UTXO, sử dụng một mô hình lập trình khác cho các ứng dụng phi tập trung (DAPP) từ các blockchain dựa trên tài khoản khác như Ethereum.
Hương vị cụ thể Cardano sử dụng là mô hình [EUTXO) [EUTXO) [EUTXO)
Bằng cách nâng cấp Alonzo.
EUTXO cung cấp bảo mật lớn hơn cho phép dự đoán chi phí thực hiện hợp đồng thông minh (không có bất ngờ khó chịu) và do đó, cung cấp một cách tiếp cận khác để song song hóa.

EUTXO inherits the per-branches design of the UTXO (Bitcoin) model, where one branch is by definition a sequence of transactions that requires a sequence of validations. To split the logic across different branches and enforce more parallelism, it is essential to build DApps and other solutions using *multiple UTXOs*. This provides benefits in terms of scaling, just like developing Bitcoin services prerequisites splitting one wallet into sub wallets. 

EUTXO kế thừa thiết kế trên mỗi nhánh của mô hình UTXO (Bitcoin), trong đó một nhánh theo định nghĩa là một chuỗi các giao dịch yêu cầu một chuỗi xác nhận.
Để phân chia logic trên các nhánh khác nhau và thực thi song song hơn, điều cần thiết là xây dựng DAPP và các giải pháp khác bằng cách sử dụng *nhiều utxos *.
Điều này cung cấp lợi ích về mặt mở rộng, giống như phát triển các điều kiện tiên quyết của Dịch vụ Bitcoin chia một ví vào ví phụ.

DApps built on Cardano are **not limited** to one transaction per block. In fact, the block budget (that is the maximum number of transactions it can hold) allows the execution of hundreds of simple transactions and several complex scripts. However, the EUTXO model allows spending a transaction output only once. Given that users can face contention issues trying to access the same UTXO, it is important to use many different UTXOs. Note that this is important unless such a design would benefit from a strict ordering of clients. Sets of UTXOs can be used to implement design patterns that include semaphores. In addition, different users can interact with one smart contract without any concurrency failure. That is because a smart contract can handle *a number of different UTXOs* that make up its current state and off-chain metadata that allows interpreting those UTXOs.

DApps được xây dựng trên Cardano ** không giới hạn ** đối với một giao dịch cho mỗi khối.
Trên thực tế, ngân sách khối (đó là số lượng giao dịch tối đa mà nó có thể nắm giữ) cho phép thực hiện hàng trăm giao dịch đơn giản và một số tập lệnh phức tạp.
Tuy nhiên, mô hình EUTXO chỉ cho phép chi tiêu đầu ra giao dịch một lần.
Cho rằng người dùng có thể phải đối mặt với các vấn đề tranh chấp khi cố gắng truy cập cùng một UTXO, điều quan trọng là sử dụng nhiều UTXO khác nhau.
Lưu ý rằng điều này rất quan trọng trừ khi một thiết kế như vậy sẽ được hưởng lợi từ việc đặt hàng nghiêm ngặt của khách hàng.
Các bộ UTXOS có thể được sử dụng để thực hiện các mẫu thiết kế bao gồm các semaphores.
Ngoài ra, người dùng khác nhau có thể tương tác với một hợp đồng thông minh mà không có bất kỳ sự cố đồng thời nào.
Đó là bởi vì một hợp đồng thông minh có thể xử lý * một số utxos khác nhau * tạo nên trạng thái hiện tại và siêu dữ liệu ngoài chuỗi cho phép giải thích các UTXO đó.

## **Doing things in parallel**

## ** Làm mọi thứ song song **

Blockchains achieve immutability and transparency of transaction processing differently. Any blockchain system should have a set of properties to meet the ever-growing need for secure yet swift operation processing, namely:

Blockchains đạt được tính bất biến và minh bạch của xử lý giao dịch khác nhau.
Bất kỳ hệ thống blockchain nào cũng phải có một tập hợp các thuộc tính để đáp ứng nhu cầu ngày càng tăng đối với xử lý hoạt động hoàn toàn nhưng an toàn, cụ thể là:

- **Throughput** – the number of operations a system can perform within a certain time period. This relates, for example, to the number of transactions or smart contracts processed in one second.

- ** Thông lượng ** - Số lượng hoạt động mà một hệ thống có thể thực hiện trong một khoảng thời gian nhất định.
Điều này liên quan, ví dụ, với số lượng giao dịch hoặc hợp đồng thông minh được xử lý trong một giây.

- **Performance** – how fast the system works. Performance measures the time of transaction or smart contract execution. 

- ** Hiệu suất ** - Hệ thống hoạt động nhanh như thế nào.
Hiệu suất đo thời gian giao dịch hoặc thực hiện hợp đồng thông minh.

- **Scalability** – the ability of the system to perform multiple operations without overloading the network or influencing performance properties.

- ** Khả năng mở rộng ** - Khả năng của hệ thống thực hiện nhiều hoạt động mà không làm quá tải mạng hoặc ảnh hưởng đến các thuộc tính hiệu suất.

By increasing parallelism, we can ultimately improve the throughput of the system while keeping the performance of individual operations the same, but this sort of scalability will always be limited by the degree of contention.

Bằng cách tăng sự song song, cuối cùng chúng ta có thể cải thiện thông lượng của hệ thống trong khi vẫn giữ hiệu suất của các hoạt động riêng lẻ, nhưng loại khả năng mở rộng này sẽ luôn bị giới hạn bởi mức độ tranh chấp.

When it comes to scalability, we also distinguish such system properties as *concurrency*, *parallelism*, and *contention*. Concurrency is essential to allow multiple actors to progress on a certain task without interfering with each other. Parallelism allows such progress *at the same time* without any interference. Contention occurs when those multiple actors interfere with each other while working either concurrently or in parallel.

Khi nói đến khả năng mở rộng, chúng tôi cũng phân biệt các thuộc tính hệ thống như *đồng thời *, *song song *và *tranh chấp *.
Đồng thời là điều cần thiết để cho phép nhiều tác nhân tiến triển theo một nhiệm vụ nhất định mà không can thiệp vào nhau.
Sự song song cho phép tiến trình như vậy * cùng một lúc * mà không có bất kỳ sự can thiệp nào.
Sự tranh chấp xảy ra khi nhiều diễn viên đó can thiệp vào nhau trong khi làm việc đồng thời hoặc song song.

## **Understanding concurrency**

## ** Hiểu đồng thời **

Concurrency may or may not improve a system’s performance, throughput, or responsiveness. The amount of concurrency limits the maximum number of simultaneous operations that can be performed. 

Đồng thời có thể hoặc không thể cải thiện hiệu suất, thông lượng hoặc khả năng đáp ứng của hệ thống.
Số lượng đồng thời giới hạn số lượng hoạt động đồng thời tối đa có thể được thực hiện.

To obtain *actual* performance improvements in a UTXO-based blockchain, processors or other actors should be able to perform multiple actions simultaneously. The higher the level of concurrency, the higher the maximum possible parallelism. Such an approach then translates to performance improvements and throughput. It also provides significant advantages over account-based systems (like Ethereum).

Để có được các cải tiến hiệu suất * thực tế * trong blockchain, bộ xử lý hoặc các tác nhân khác dựa trên UTXO sẽ có thể thực hiện đồng thời nhiều hành động.
Mức độ đồng thời càng cao, sự song song tối đa có thể càng cao.
Cách tiếp cận như vậy sau đó chuyển sang cải tiến hiệu suất và thông lượng.
Nó cũng cung cấp những lợi thế đáng kể so với các hệ thống dựa trên tài khoản (như Ethereum).

## **Deploying DApps on UTXO ledgers *is different***

## ** Triển khai DApps trên sổ cái UTXO*là khác nhau ***

Cardano’s approach to DApp deployment is different and thus it requires a learning curve and a different approach. This is like working with different programming languages: there is one goal – to deploy a solution, but so many programming languages to use for this purpose. 

Cách tiếp cận của Cardano, để triển khai DAPP là khác nhau và do đó, nó đòi hỏi một đường cong học tập và một cách tiếp cận khác.
Điều này giống như làm việc với các ngôn ngữ lập trình khác nhau: có một mục tiêu - để triển khai một giải pháp, nhưng rất nhiều ngôn ngữ lập trình để sử dụng cho mục đích này.

Maximizing concurrency is a skill that needs to be learned: developers need to write code in a way that severely restricts the opportunities for contention (e.g., by avoiding shared states and accidental dependencies). The system must then translate this concurrency into parallelism. A number of developers have already identified ways to approach this, while others are still developing solutions. Simply transplanting lessons learned on one blockchain will not work; while the learning curve is a little steeper, the results make this worthwhile.

Tối đa hóa đồng thời là một kỹ năng cần học: các nhà phát triển cần viết mã theo cách hạn chế nghiêm trọng các cơ hội tranh chấp (ví dụ: bằng cách tránh các trạng thái chung và phụ thuộc vô tình).
Hệ thống sau đó phải dịch đồng thời này thành song song.
Một số nhà phát triển đã xác định các cách để tiếp cận điều này, trong khi những người khác vẫn đang phát triển các giải pháp.
Đơn giản chỉ cần cấy ghép các bài học kinh nghiệm trên một blockchain sẽ không hoạt động;
Trong khi đường cong học tập dốc hơn một chút, kết quả làm cho điều này đáng giá.

Either way, it is important to understand that to deploy a scalable DApp on Cardano, a developer can’t just use an adapted Ethereum contract. Cardano is based on the UTXO model; it is not account-based. And this means that a single on-chain state will not meet the concurrency property on Cardano. Instead, DApps should split up their on-chain state across many UTXOs. This will increase the concurrency in their application, thereby allowing higher throughput. 

Dù bằng cách nào, điều quan trọng là phải hiểu rằng để triển khai DAPP có thể mở rộng trên Cardano, một nhà phát triển có thể chỉ sử dụng hợp đồng Ethereum thích nghi.
Cardano dựa trên mô hình UTXO;
Nó không dựa trên tài khoản.
Và điều này có nghĩa là một trạng thái duy nhất trên chuỗi sẽ không đáp ứng tài sản đồng thời trên Cardano.
Thay vào đó, DApps nên chia trạng thái trên chuỗi của họ trên nhiều UTXO.
Điều này sẽ tăng sự đồng thời trong ứng dụng của họ, do đó cho phép thông lượng cao hơn.

Our education team has previously shared a simple AMM-style DEX implementation in the Plutus Pioneer course. While this is useful for teaching purposes, this architecture would not directly support a commercial DEX where an order book approach and additional concurrency are required. A developer looking to deploy on the Cardano mainnet would need to improve the scalability of the architecture accordingly.

Nhóm giáo dục của chúng tôi trước đây đã chia sẻ một triển khai DEX kiểu AMM đơn giản trong khóa học Pioneer Plutus.
Mặc dù điều này rất hữu ích cho mục đích giảng dạy, kiến trúc này sẽ không trực tiếp hỗ trợ DEX thương mại nơi cần có một cách tiếp cận sách đặt hàng và cần có thêm sự đồng thời.
Một nhà phát triển đang tìm cách triển khai trên Cardano Mainnet sẽ cần cải thiện khả năng mở rộng của kiến trúc cho phù hợp.

We proposed a solution within our recent [Djed stablecoin paper](https://iohk.io/en/research/library/papers/djeda-formally-verified-crypto-backed-pegged-algorithmic-stablecoin/). For the Djed implementation on Cardano, an order book modeling pattern is favored whereby an order maker is responsible for forwarding any minting or burning order to the stablecoin smart contract, with an additional incentive fee imposed on each would-be buyer or seller of stablecoins and reserve coins. Several security mechanisms – via the extensive use of non-fungible tokens (NFTs) – are also used to guarantee the uniqueness of transactions, the correctness of each submitted order, and to prevent front-running attacks. NFT tokens are also used to report successful or failed minting and burning orders. We’ll publish a fuller article on this shortly.

Chúng tôi đã đề xuất một giải pháp trong [Giấy StableCoin DJ gần đây của chúng tôi (https://iohk.io/en/research/l Library/papers/djeda-formally-verified-crypto-backed-pegged-algorithmic-stablecoin/).
Đối với việc triển khai DJ trên Cardano, một mô hình mô hình sách đặt hàng được ưa chu
Tiền dự trữ.
Một số cơ chế bảo mật-thông qua việc sử dụng rộng rãi các mã thông báo không bị tăng (NFT)-cũng được sử dụng để đảm bảo tính duy nhất của các giao dịch, tính chính xác của mỗi đơn đặt hàng được gửi và để ngăn chặn các cuộc tấn công chạy trước.
Mã thông báo NFT cũng được sử dụng để báo cáo các lệnh khai thác và đốt thành công hoặc thất bại.
Chúng tôi sẽ xuất bản một bài viết đầy đủ hơn về điều này trong thời gian ngắn.

To learn more about scalability, you can read [how to design a scalable Plutus application](https://plutus.readthedocs.io/en/latest/plutus/howtos/writing-a-scalable-app.html) and find out how to organize DApps on Cardano using [order book patterns](https://plutus.readthedocs.io/en/latest/plutus/explanations/order-book-pattern.html). Developers have also presented [concurrent and deterministic approaches to the EUTXO smart contract architecture](https://medium.com/meld-labs/concurrent-deterministic-batching-on-the-utxo-ledger-99040f809706) that might be regarded as a generalization of the parallel state machine steps introduced in the [Hydra paper](https://iohk.io/en/research/library/papers/hydrafast-isomorphic-state-channels/) to realize multi-step state machines. A number of other [developers](https://twitter.com/ErgoDex/status/1434241104015151105?s=20) and community members have also published papers, [videos](https://youtube.com/watch?v=TxnvYsBnLjQ), [articles](https://sundaeswap-finance.medium.com/concurrency-state-cardano-c160f8c07575), and useful [threads](https://twitter.com/CardanoMaladex/status/1434960813006200835) on Twitter outlining their approaches. It’s a brilliant lesson in how the community will continue to develop its own innovative solutions, as approaches become more standardized with platform maturity.

Để tìm hiểu thêm về khả năng mở rộng, bạn có thể đọc [Cách thiết kế ứng dụng Plutus có thể mở rộng] (https://plutus.readthedocs.io/en/latest/plutus/howtos/writing-a-scalable-app.html) và tìm hiểu Cách tổ chức DApps trên Cardano bằng cách sử dụng [mẫu sách đặt hàng] (https://plutus.readthedocs.io/en/latest/plutus/explanations/order-book-pattern.html). Các nhà phát triển cũng đã trình bày [các phương pháp đồng thời và xác định đối với kiến trúc hợp đồng thông minh EUTXO] (https://medium.com/meld-labs/concien Việc khái quát hóa các bước máy trạng thái song song được giới thiệu trong [giấy hydra] (https://iohk.io/en/research/l Library/papers/hydrafast-isomorphic-tate-channels/) để nhận ra các máy đa trạng thái. Một số [nhà phát triển] khác (https://twitter.com/ergodex/status/1434241104015151105?s=20) và các thành viên cộng đồng cũng đã xuất bản các bài báo, [video] (https://youtube.com/watch?v= Txnvysbnljq), [bài viết] (https://sundaeswap-finance.medium.com/concurrency-tate-cardano-c160f8c07575) và hữu ích [chủ đề] (https://twitter.com/cardanomalade phác thảo cách tiếp cận của họ. Nó là một bài học tuyệt vời trong cách cộng đồng sẽ tiếp tục phát triển các giải pháp sáng tạo của riêng mình, khi các phương pháp tiếp cận trở nên tiêu chuẩn hơn với sự trưởng thành của nền tảng.

## **Moving forward**

## **Tiến về phía trước**

The Alonzo hard fork event will introduce the core building blocks of Plutus 1.0. This is the beginning of ecosystem growth. Although it is still early, the Alonzo testnet allows our developers to assess system properties and build scalable DApps in advance – preparing for their mainnet launch. Dozens of projects have already been working with local instances of Plutus environments. With the main public testnet soon supporting smart contracts, we expect a significant ramping up of activity over the next few weeks and in the months ahead. Later this month, the [Cardano summit](https://summit.cardano.org/) (25-26 September) will showcase many of these projects, plus provide important updates on the smart contracts roadmap and the ongoing evolution of the technology stack. Developer events, hackathons, and, of course, the results of Project Catalyst will continue to bring new tools and abstractions to this fast-growing developer ecosystem.

Sự kiện Alonzo Hard Fork sẽ giới thiệu các khối xây dựng cốt lõi của Plutus 1.0.
Đây là sự khởi đầu của sự tăng trưởng hệ sinh thái.
Mặc dù vẫn còn sớm, Alonzo Testnet cho phép các nhà phát triển của chúng tôi đánh giá các thuộc tính hệ thống và xây dựng các DAPP có thể mở rộng trước - chuẩn bị cho sự ra mắt chính của họ.
Hàng chục dự án đã làm việc với các trường hợp địa phương của môi trường Plutus.
Với TestNet công cộng chính đã sớm hỗ trợ các hợp đồng thông minh, chúng tôi hy vọng sẽ tăng cường hoạt động đáng kể trong vài tuần tới và trong những tháng tới.
Cuối tháng này, [Hội nghị thượng đỉnh Cardano] (https://summit.cardano.org/) (25-26 tháng 9) sẽ giới thiệu nhiều dự án này, cộng với việc cung cấp các cập nhật quan trọng về lộ trình hợp đồng thông minh và sự phát triển liên tục của công nghệ
cây rơm.
Các sự kiện của nhà phát triển, hackathons, và tất nhiên, kết quả của Project Catalyst sẽ tiếp tục mang lại các công cụ và trừu tượng mới cho hệ sinh thái phát triển phát triển nhanh này.

If you are a developer, make sure to join our [Discord community](https://discord.gg/ScxDkrxpBg) and get involved with [Project Catalyst](https://cardano.ideascale.com/a/index) if you are looking to fund your project.

Nếu bạn là nhà phát triển, hãy đảm bảo tham gia [cộng đồng Discord] của chúng tôi (https://discord.gg/scxdkrxpbg) và tham gia vào [Project Catalyst] (https://cardano.ideascale.com/a/index) nếu
Bạn đang tìm cách tài trợ cho dự án của bạn.

*I'd like to acknowledge [Lars Brünjes](https://github.com/brunjlar), [Jann Müller](https://github.com/j-mueller), and [Manuel Chakravarty](https://github.com/mchakravarty) for their technical input and support during the blog post preparation.*

*Tôi muốn thừa nhận [Lars Brünjes] (https://github.com/brunjlar), [Jann Müller] (https://github.com/j-mueller) và [Manuel Chakravarty] (https:/
/github.com/mchakravarty) cho đầu vào và hỗ trợ kỹ thuật của họ trong quá trình chuẩn bị bài đăng trên blog.*

