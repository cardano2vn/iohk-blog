# Từ Classic đến Chronos: Giải mã việc triển khai Ouroboros

### **Ouroboros is the consensus protocol of Cardano. Here, we explain what it does and how it’s evolving**

![](img/2022-06-03-from-classic-to-chronos-the-implementations-of-ouroboros-explained.002.png) 3 tháng 6 năm 2022 ![](img/2022-06-03-from-classic-to-chronos-the-implementations-of-ouroboros-explained.002.png) [Olga Hryniuk](/en/blog/authors/olga-hryniuk/page-1/) ![](img/2022-06-03-from-classic-to-chronos-the-implementations-of-ouroboros-explained.003.png) 9 phút đọc

![Olga Hryniuk](img/2022-06-03-from-classic-to-chronos-the-implementations-of-ouroboros-explained.004.png)[](/en/blog/authors/olga-hryniuk/page-1/)

### [**Olga Hryniuk**](/en/blog/authors/olga-hryniuk/page-1/)

Technical Writer

Marketing &amp; Communications

- ![](img/2022-06-03-from-classic-to-chronos-the-implementations-of-ouroboros-explained.005.png)[](https://www.linkedin.com/in/olga-hryniuk-1094a3160/ "LinkedIn")
- ![](img/2022-06-03-from-classic-to-chronos-the-implementations-of-ouroboros-explained.006.png)[](https://github.com/olgahryniuk "GitHub")

![From Classic to Chronos: the implementations of Ouroboros explained](img/2022-06-03-from-classic-to-chronos-the-implementations-of-ouroboros-explained.007.jpeg)

Có thể nhiều người đã nghe đến Ouroboros: một giao thức đồng thuận bằng chứng cổ phần (proof of stake - POS) mang tính đột phá được Cardano sử dụng. Giao thức này được phát triển như một giải pháp thay thế hiệu quả về mặt năng lượng và bền vững hơn cơ chế đồng thuận bằng chứng công việc (proof of work-POW). Các đồng tiền mã hóa trước đó như Bitcoin và hiện tại là Ethereum đều được xây dựng dựa trên cơ chế đồng thuận bằng chứng công việc. Ouroboros là giao thức đồng thuận blockchain đầu tiên được phát triển dựa trên những nghiên cứu đã được hội đồng khoa học thẩm định (peer-reviewed).

Led by [Prof. Aggelos Kiayias](https://en.wikipedia.org/wiki/Aggelos_Kiayias) of the University of Edinburgh, Ouroboros and its subsequent implementations provide a new baseline to solve some of the world’s greatest challenges, securely and at scale.

Yet recognition begins with education. This article presents an overview of how Ouroboros works. It examines the tangibles and covers what each implementation introduces, to further the community’s understanding of the protocol, and illustrates why it’s such a game-changer. A detailed analysis of each implementation can be found in the corresponding papers below. For a broad-stroke explanation of Ouroboros and its implementations, however, read on.

- [Ouroboros Classic](https://iohk.io/en/research/library/papers/ouroborosa-provably-secure-proof-of-stake-blockchain-protocol/)
- [Ouroboros BFT](https://iohk.io/en/research/library/papers/ouroboros-bfta-simple-byzantine-fault-tolerant-consensus-protocol/)
- [Ouroboros Praos](https://iohk.io/en/research/library/papers/ouroboros-praosan-adaptively-securesemi-synchronous-proof-of-stake-protocol/)
- [Ouroboros Genesis](https://iohk.io/en/research/library/papers/ouroboros-genesiscomposable-proof-of-stake-blockchains-with-dynamic-availability/)
- [Ouroboros Crypsinous](https://iohk.io/en/research/library/papers/ouroboros-crypsinousprivacy-preserving-proof-of-stake/)
- [Ouroboros Chronos](https://iohk.io/en/research/library/papers/ouroboros-chronospermissionless-clock-synchronization-via-proof-of-stake/)

## **A word on consensus protocols, and why Ouroboros is different**

It’s reasonable to assume that anybody new to the space might be confused by the term 'consensus protocol'. Put simply, a consensus protocol is the system of laws and parameters that govern the behavior of distributed ledgers: a ruleset by which each network participant plays to reach an agreement with everyone else.

Public blockchains aren’t controlled by any single, central authority. Instead, a consensus protocol is used to allow distributed network participants to agree on the history of the network captured on the blockchain – to reach a consensus on what has happened, and continue from a single source of truth.

That single source of truth provides a single record. This is why blockchains are sometimes referred to as trustless: instead of requiring participants to trust one another, trust is built into the protocol. Unknown actors may interact and transact with each other without relying on an intermediary to mediate, or for there to be a prerequisite exchange of personal data.

Ouroboros là một giao thức bằng chứng cổ phần, nó khác biệt với bằng chứng công việc. Thay vì dựa vào 'thợ đào' để giải các phương trình toán học phức tạp với mục đích tạo ra các khối mới - và thưởng cho người đầu tiên giải được - bằng chứng cổ phần chọn những người tham gia (trong trường hợp của Cardano, nhóm cổ phần (stake pool)) để tạo các block mới dựa trên số tiền mà họ nắm giữ trong mạng lưới.

Networks using Ouroboros are many times more energy-efficient than those using proof of work – and, through Ouroboros, Cardano is able to achieve unparalleled energy efficiency. As of 2022, Bitcoin, for example, requires [204.50 TWh](https://digiconomist.net/bitcoin-energy-consumption) per year which is comparable to the power consumption of Thailand. Ouroboros, on the other hand, runs a [Raspberry Pi](https://www.reddit.com/r/cardano/comments/e8t34d/rock_pi_cardano_full_node_for_100/), which has a power consumption of 15 to 18W (watts). The resulting difference in energy use can be analogized to that between a household and a country: one can be scaled to the mass market; the other cannot.

Now, let’s take a closer look at how the Ouroboros protocol works, and what each new implementation adds.

## **Ouroboros Classic**

Let’s start with [Ouroboros](https://iohk.io/en/research/library/papers/ouroborosa-provably-secure-proof-of-stake-blockchain-protocol/): the first implementation of the Ouroboros protocol, published in 2017. This first implementation (referred to as Ouroboros Classic) laid the foundations for the protocol as an energy-efficient rival to proof of work, introduced the mathematical framework to analyze proof of stake, and introduced a novel incentive mechanism to reward participants in a proof-of-stake setting.

More than this, however, what separated Ouroboros from other blockchains, and, specifically, proof-of-stake protocols was its ability to generate unbiased randomness in the protocol’s leader selection algorithm, and the subsequent security assurances that provided. Randomness prevents the formation of patterns and is a critical part of maintaining the protocol’s security. Whenever a behavior can be predicted, it can be exploited – and though Ouroboros ensures transparency, it prevents coercion. Significantly, Ouroboros was the first blockchain protocol to be developed with this type of rigorous security analysis.

## **How Ouroboros works**

A comprehensive explanation of how Ouroboros works can be found in its [research paper](https://iohk.io/en/research/library/papers/ouroborosa-provably-secure-proof-of-stake-blockchain-protocol/). Ouroboros divides time on Cardano into epochs where each epoch is divided into slots. A slot is a short period of time in which a block can be created and grouping slots into epochs is central to adjusting the leader election process to the dynamically changing stake distribution.

Trung tâm trong thiết kế Ouroboros là phải duy trì tính bảo mật của chính nó trước các cuộc tấn công. Do đó, giao thức này được tích hợp khả năng bảo vệ để ngăn những kẻ tấn công và tuyên truyền các phiên bản thay thế blockchain. Có thể giả định rằng, bất cứ lúc nào cũng có kẻ tấn công gửi bất kỳ thông điệp nào cho bất kỳ người tham gia nào. Trên thực tế, sự an toàn của giao thức được đảm bảo trong một khái niệm gọi là cài đặt đồng bộ (nghĩa là với được đảm bảo chắc chắn về thời gian gửi tin nhắn), miễn là có hơn 51% cổ phần được những người tham gia trung thực kiểm soát (nghĩa là những người ủng hộ giao thức).

Một slot đứng đầu được bầu chọn cho mỗi slot. Slot đứng đầu này chịu trách nhiệm thêm một khối vào chuỗi và chuyển nó cho slot đứng đầu tiếp theo. Để tự bảo vệ trước những nỗ lực phá hoại giao thức, mỗi slot đứng đầu mới được yêu cầu chú ý tạm thời đến một vài khối cuối cùng của chuỗi đã nhận: chỉ chuỗi đứng trước một số lượng khối tạm thời được xác định trước mới được xem là chắc chắn. Đây cũng được gọi là thời gian giải quyết trì hoãn.<br>Bên cạnh những yếu tố khác, điều này có nghĩa là một người nắm giữ cố phần có thể ngoại tuyến nhưng vẫn được đồng bộ hóa với blockchain, miễn là nó không vượt quá thời gian giải quyết trì hoãn.

Within the Ouroboros protocol, each network node stores a copy of the transaction mempool – where transactions are added if they are consistent with existing transactions – and the blockchain. The locally stored blockchain is replaced when the node becomes aware of an alternative, longer valid chain.

The drawback of Ouroboros Classic was that it was susceptible to adaptive attackers – a significant threat in a real-world setting that was resolved with Ouroboros Praos – and had no secure way for a new participant to bootstrap from the blockchain, which was resolved with Ouroboros Genesis.

**Ouroboros BFT**

[Ouroboros BFT](https://iohk.io/en/research/library/papers/ouroboros-bfta-simple-byzantine-fault-tolerant-consensus-protocol/) came next, derived as a simple special case from the analysis of Classic. Ouroboros BFT (Byzantine Fault Tolerance) is a simple protocol that was used by Cardano during the [Byron reboot](https://iohk.io/en/blog/posts/2020/03/30/what-the-byron-reboot-means-for-cardano/), which was the transition of the old Cardano codebase to the new. Ouroboros BFT helped prepare Cardano’s network for Shelley’s release and, with that, its decentralization.

Rather than requiring nodes to be online all of the time, Ouroboros BFT assumed a federated network of servers and synchronous communication between the servers for building the blockchain. In this federated setting, it is a consensus protocol that is attractive due to its simplicity and deterministic nature. It is worth noting that BFT required a larger fraction of honest parties than other Ouroboros versions.

## **Ouroboros Praos**

[Ouroboros Praos](https://iohk.io/en/research/library/papers/ouroboros-praosan-adaptively-securesemi-synchronous-proof-of-stake-protocol/) builds upon – and provides substantial security and scalability improvements to – Ouroboros Classic.

As with Ouroboros Classic, Ouroboros Praos processes transaction blocks by dividing chains into slots, which are aggregated into epochs. Unlike Ouroboros Classic, however, Praos is analyzed in a semi-synchronous setting and is secure against adaptive attackers.

It assumes two possibilities: that adversaries can delay honest participant messages for longer than one slot, and that an adversary may send arbitrary messages to any participant at any time.

Through private-leader selection and forward-secure, key-evolving signatures, Praos provides better epoch randomness and ensures that a strong adversary cannot predict the next slot leader and launch a focused attack (such as a DDoS attack) to subvert the protocol. Praos is also able to tolerate adversarially-controlled message delivery delays and gradual corruption of individual participants in an evolving stakeholder population, which is critical for maintaining network security in a global setting, provided that an honest majority of stake is maintained.

## **Ouroboros Genesis**

Then, there is [Ouroboros Genesis.](https://iohk.io/en/research/library/papers/ouroboros-genesiscomposable-proof-of-stake-blockchains-with-dynamic-availability/) Genesis further improves upon Ouroboros Praos by adding a novel chain selection rule, which enables parties to bootstrap from a genesis block – without, significantly, the need for trusted checkpoints or assumptions about past availability. Genesis also provides proof of the protocol’s Universal Composability, which demonstrates that the protocol can be composed with other protocols in arbitrary configurations in a real-world setting, without losing its security properties. This significantly contributes to its security and sustainability, and that of the networks using it.

**Ouroboros Crypsinous**

[Ouroboros Crypsinous](https://iohk.io/en/research/library/papers/ouroboros-crypsinousprivacy-preserving-proof-of-stake/) equips Genesis with privacy-preserving properties. It is the first formally analyzed privacy-preserving proof-of-stake blockchain protocol, which achieves security against adaptive attacks while maintaining strong privacy guarantees by introducing a new coin evolution technique relying on SNARKs and key-private forward-secure encryption. Crypsinous isn’t currently planned to be implemented on Cardano, but it can be used by other chains for increased privacy-preserving settings.

## **Ouroboros Chronos**

Last but not least is [Ouroboros Chronos](https://iohk.io/en/research/library/papers/ouroboros-chronospermissionless-clock-synchronization-via-proof-of-stake/). [Chronos](https://iohk.io/en/blog/posts/2021/10/27/ouroboros-chronos-provides-the-first-high-resilience-cryptographic-time-source-based-on-blockchain/) achieves two goals: first, it shows how blockchain protocols can synchronize clocks securely via a novel time synchronization mechanism and thereby become independent of external time services. Second, it is a cryptographically secure blockchain protocol that additionally provides a cryptographically secure source of time to other protocols. In short, Chronos makes the ledger more resistant to attacks that target time information.

From an application point of view, Chronos can dramatically boost the resilience of critical telecommunications, transport, and other IT infrastructures that require the synchronization of local time to a unified network clock that has no single point of failure.

## **The future of Ouroboros**

Ouroboros, named after the symbol of infinity, is the backbone of the Cardano ecosystem. The protocol serves as a foundation and staging point for self-propagating systems that cyclically transform and grow, supplanting existing systems – financial and otherwise – and disintermediating the power structures upon which they rely. It is the beginning of a new standard, defined not from the center but, instead, from the margins.

Currently, Cardano operates based on Ouroboros Praos. Genesis is being implemented for 2022 after which the ledger will be upgraded to support Ouroboros Chronos.

Its future is as its past: a tireless effort to explore, iterate, optimize, and drive positive change through rigorous research. Each step in Ouroboros’ journey is a new evolution, which takes us closer to the vision of a fairer, securer, and more sustainable world.

*Bài đăng này là phiên bản cập nhật của bản gốc (do Kieran Costello tạo) đã được cập nhật để bao gồm các phiên bản giao thức mới. <br><br>Bài này được dịch bởi Chitk <a class="_active_edit_href" href="https://iohk.io/en/blog/posts/2022/06/03/from-classic-to-chronos-the-implementations-of-ouroboros-explained/">với bài gốc</a><br><em>Dự án này được tài trợ bới Catalyst</em>*
