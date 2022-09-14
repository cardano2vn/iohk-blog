# Phân tích về khả năng mở rộng của Cardano

### **Xem xét kỹ hơn nghiên cứu của IOG, phần 4. Cách thức các giải pháp layer 1 và layer 2 tạo ra một blockchain nhanh hơn và linh hoạt hơn**

![](img/2022-07-19-an-analysis-of-the-research-underpinning-cardanos-scalability.002.png) 19 July 2022![](img/2022-07-19-an-analysis-of-the-research-underpinning-cardanos-scalability.002.png)[ Olga Hryniuk](/en/blog/authors/olga-hryniuk/page-1/)![](img/2022-07-19-an-analysis-of-the-research-underpinning-cardanos-scalability.003.png) 7 mins read

![Olga Hryniuk](img/2022-07-19-an-analysis-of-the-research-underpinning-cardanos-scalability.004.png)[](/en/blog/authors/olga-hryniuk/page-1/)

### [**Olga Hryniuk**](/en/blog/authors/olga-hryniuk/page-1/)

Technical Writer

Marketing &amp; Communications

- ![](img/2022-07-19-an-analysis-of-the-research-underpinning-cardanos-scalability.005.png)[](https://www.linkedin.com/in/olga-hryniuk-1094a3160/ "LinkedIn")
- ![](img/2022-07-19-an-analysis-of-the-research-underpinning-cardanos-scalability.006.png)[](https://github.com/olgahryniuk "GitHub")

![An analysis of the research underpinning Cardano's scalability](img/2022-07-19-an-analysis-of-the-research-underpinning-cardanos-scalability.007.png)

Các bài đăng trên blog trước đây đã đi sâu vào [nghiên cứu nền tảng](https://iohk.io/en/blog/posts/2022/06/10/cardanos-foundational-research-overview/) cho phép hỗ trợ sổ cái đa chức năng của Cardano với [các hợp đồng thông minh ](https://iohk.io/en/blog/posts/2022/06/23/overview-of-the-research-enabling-smart-contract-support-on-cardano/) và [tài sản gốc](https://iohk.io/en/blog/posts/2022/07/07/research-overview-part-3-tokens-stablecoins-and-fees/) .

Như là một phần giai đoạn phát triển của kỷ nguyên Basho, Cardano đang tiến hành nâng cấp và tối ưu hóa sự ổn định để tăng khả năng mở rộng và khả năng tương tác. Bài đăng ‘[Cách chúng ta mở rộng mạng Cardano năm 2022](https://iohk.io/en/blog/posts/2022/01/14/how-we-re-scaling-cardano-in-2022/)’ phản ánh các mục tiêu về khả năng mở rộng của Cardano, đồng thời cũng thảo luận về [khả năng tương tác và vai trò của các sidechains](https://iohk.io/en/blog/posts/2022/01/14/how-we-re-scaling-cardano-in-2022/). Bài đăng mới này sẽ xem xét kỹ hơn việc nghiên cứu cho phép thực hiện từng bước những cải tiến này.

## **Mở rộng quy mô cho mạng Cardano**

Khả năng mở rộng là điều cần thiết đối với mạng lưới blockchain để hỗ trợ việc mở rộng người dùng và đảm bảo việc tăng trưởng mà không phải hy sinh thông lượng dữ liệu.

Scaling a blockchain usually requires a combined approach with a diversity of solutions to suit every situation and project. For example:

- Giải pháp layer 1 là các nâng cấp được áp dụng trực tiếp cho giao thức chuỗi chính.
- Giải pháp layer 2 là chuỗi bổ sung (sidechains) hoặc giải pháp layer 2 (ZK rollups) để tăng hiệu suất chuỗi chính.

## **Các giải pháp mở rộng layer 1**

Pipelining and input endorsers are two on-chain solutions planned to be implemented on Cardano in 2022-2023. The paper detailing the research done on pipelining is not yet published, but here are some of the properties and rationale for the introduction of pipelining.

**Pipelining in Ouroboros**

Để hiểu Pipelining là gì, trước tiên chúng ta hãy định nghĩa thuật ngữ truyền block . Truyền block có nghĩa là các node tạo block và phát tán các block mới này trên toàn mạng.

Pipelining improves block propagation times. The goal is for blocks to be propagated to peers within five seconds. Pipelining enables this by giving nodes the ability to pre-notify their downstream peers of an incoming block, enabling the peer to pre-fetch the new block body.

Nghiên cứu đưa ra một ý tưởng để phát tán các khối trước khi xác nhận đầy đủ. Điều này đưa công việc xác thực phần thân khối ra khỏi thời gian truyền tải khối và cho phép thời gian dành cho việc xác nhậnđồng thời với việc gửi khối tới node ngang hàng khác trong mạng. Điều này làm giảm thời gian truyền khối, cho phép tăng kích thước khối hoặc cải tiến Plutus. Do đó, khối càng lớn thì càng có nhiều giao dịch và tập lệnh Plutus, điều này tăng thông lượng của blockchain. Những nâng cấp này được lên kế hoạch áp dụng cho Cardano trong sự kiện  hard fork Vasil.

**Input endorsers**

Việc thực hiện Input endorsers cũng sẽ cải thiện thời gian và lưu lượng truyền khối. Input endorsers theo dõi tất cả các giao dịch đã gửi và đóng gói các giao dịch này trở thành các khối được xây dựng trước. Điều này có nghĩa là có 2 phần của khối, một phần chứa các giao dịch, một phần để đạt được đồng thuận. Các khối thực hiện đồng thuận sẽ tham chiếu đến các khối được xây dựng trước, được truyền liên tục mà không cần phải đợi cho đến khi đạt được sự đồng thuận. Điều này sẽ cải thiện thời gian truyền khối và cho phép tốc độ giao dịch cao hơn.

John Woods, the former Director of Cardano Architecture at IOG, said:

Pipelining implementation is just great technology. Synthetic benchmarks show up to 40% efficiency gains. It's a great part of the story of how Cardano scales to meet demand in 2022. 2023 will see the dawn of [Ouroboros Leios](https://www.youtube.com/watch?v=xKv94MwSNBw) (input endorsers), which will be a game-changer. It is expected that input endorsers are going to scale Cardano for the next half decade.

**Định giá theo bậc thang**

Another research initiative by IOG scientists is the implementation of [tiered pricing](https://iohk.io/en/blog/posts/2021/11/26/network-traffic-and-tiered-pricing/). In the current system, all transactions are treated the same without the possibility to alter their priority by paying higher gas fees, for example. This approach works well as long as the network throughput is comparable to transaction processing demand. However, as the network usage increases, not all the transactions might be eventually included in the blockchain. The possibility of a denial of service (DoS) attack â€“ taking advantage of the fair transaction treatment to pass off malicious spam as legitimate transactions â€“ requires *additional* measures to support network healthiness.

Định giá theo bậc thang cho phép hiệu suất hệ thống ổn định theo cách nhanh lẹ và đặc biệt có liên quan trong việc ngăn chặn các cuộc tấn công DoS. Nghiên cứu đề xuất duy trì khả năng dự đoán, tính công bằng và hiệu quả chi phí của các giao dịch Cardano trong khi giảm thiểu các vấn đề có thể phát sinh từ nhu cầu mạng lưới ngày càng lớn hơn. Cách tiếp cận đưa ra một cơ chế phí giao dịch mới, trong đó mỗi khối được chia thành ba 'cấp' (dựa trên trường hợp sử dụng). Mỗi cấp tạo nên một tỷ lệ phần trăm của kích thước khối tối đa và được thiết kế cho các loại giao dịch khác nhau như: công bằng, cân bằng và tức thì. Khi mạng lưới không bận, các cấp mặc định là tiêu chuẩn cơ bản để ưu tiên giao dịch.

## **Layer 2 scalability solutions**

To help scale a number of transactions that can be processed at once, a blockchain network can spin up a number of sidechains, introduce state channels, or apply a stake-based threshold multi-signature scheme, for example.

**Sidechains**

Bài báo `[Proof-of-Stake Sidechains](https://iohk.io/en/research/library/papers/proof-of-stake-sidechains/)` được xuất bản vào năm 2019. Bài báo này cung cấp định nghĩa chính thức đầu tiên về hệ thống sidechain và cách tài sản có thể được di chuyển an toàn giữa các sidechain.

IOG scientists put forth a security definition that augments the known transaction ledger properties of persistence and liveness to hold across multiple ledgers, and enhances them with a new â€˜firewallâ€™ security property. This safeguards each blockchain from its sidechains, limiting the impact of a potentially catastrophic sidechain failure. The paper also provides a sidechain construction that is suitable for proof-of-stake sidechain systems and is consistent with the Ouroboros consensus protocol. Such techniques as merged staking, cross-chain certification, and multi-signature usage are presented to ensure sidechainsâ€™ resilience to malicious attacks.

As a result of this research, IOG has developed the [Cardano EVM sidechain](https://iohk.io/en/blog/posts/2022/07/06/introducing-the-cardano-evm-sidechain/), which is currently in alpha version on testnet. It will be compatible with Ethereumâ€™s tools and libraries, allowing developers to create Solidity smart contracts, DApps, and ERC20 tokens on Cardano to gain from such benefits as cost-efficiency, scalability, and security.

**Hydra**

Besides sidechains, there are other solutions for improving network scalability. Hydra state channels, for example.

Bài báo nghiên cứu `[Hydra: Fast Isomorphic State Channels](https://iohk.io/en/research/library/papers/hydra-fast-isomorphic-state-channels/)` được xuất bản vào năm 2021. Bài báo giới thiệu về Hydra - một isomorphic multi-party state channel. Các state channel là một giải pháp layer 2 đầy hấp dẫn để cải thiện lưu lượng và độ trễ của các blockchain. Hydra đơn giản hóa giao thức ngoài chuỗi và phát triển hợp đồng thông minh bằng cách áp dụng trực tiếp hệ thống hợp đồng thông minh layer 1, theo cách này cho phép sử dụng cùng một đoạn mã cả trong và ngoài chuỗi. Tận dụng [mô hình EUTxO](https://iohk.io/en/research/library/papers/the-extended-utxo-model/) , nghiên cứu đề xuất cách phát triển một giao thức ngoài chuỗi nhanh chóng dành cho sự phát triển của [Hydra Heads](https://iohk.io/en/blog/posts/2022/02/03/implementing-hydra-heads-the-first-step-towards-the-full-hydra-vision/), giao thức hiện đang được triển khai trên Cardano.

**Mithril**

Finally, to achieve greater scalability, it is also important to streamline the speed and efficiency of data synchronization between applications. Addressing this, the IOG research team published the paper on â€˜[Mithril: Stake-based Threshold Multisignatures](https://iohk.io/en/research/library/papers/mithril-stake-based-threshold-multisignatures/)â€™ in 2021.

Efficient chain validation is essential to achieve greater scalability in a blockchain setting. This also depends on various messages signed by network validators. Mithril addresses the complexity of critical operations that depend logarithmically on the number of these participants. Given the time it takes to validate a particular message, and the resource usage during the validation phase of chain synchronization, Mithril provides a solution that makes multi-signature aggregation fast and efficient without compromising security features.

The paper reflects on how to retain strong security settings in multi-signature aggregation. As a result, Mithril can be applied for fast, efficient, and secure chain synchronization protocol. It is advantageous for secure voting, data exchange between sidechains, and data synchronization within light wallets. It is part of the Basho phase and will be implemented in 2022.

## **The final word**

There are currently [144 papers](https://iohk.io/en/research/library/) hosted in the IOG research library and this number is constantly growing. All the work has always and will further lay the foundation before any feature or upgrade is deployed on Cardano.

*In the coming months, weâ€™ll be reflecting more on the latest development and research taking place in regards to ledger optimizations, scalability improvements, and governance initiatives.*
