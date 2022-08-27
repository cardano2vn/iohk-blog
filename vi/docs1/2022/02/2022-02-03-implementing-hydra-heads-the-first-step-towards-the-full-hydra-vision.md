# Triển khai Hydra Heads: Bước đầu hướng tới tầm nhìn giao thức Hydra hoàn thiện

### **Hydra Head - công cụ đầu tiên trong bộ giao thức, là một yếu tố quan trọng trong hành trình mở rộng quy mô của Cardano. Hãy cùng xem giao thức Hydra Head phù hợp với bức tranh tổng thể lớn hơn như thế nào. Công cụ này có thể sẽ phá vỡ một số quan điểm.**

![](img/2022-02-03-implementing-hydra-heads-the-first-step-towards-the-full-hydra-vision.002.png) 3 February 2022![](img/2022-02-03-implementing-hydra-heads-the-first-step-towards-the-full-hydra-vision.002.png)[ Matthias Benkort](/en/blog/authors/matthias-benkort/page-1/)![](img/2022-02-03-implementing-hydra-heads-the-first-step-towards-the-full-hydra-vision.003.png) 12 mins read

![Matthias Benkort](img/2022-02-03-implementing-hydra-heads-the-first-step-towards-the-full-hydra-vision.004.png)[](/en/blog/authors/matthias-benkort/page-1/)

### [**Matthias Benkort**](/en/blog/authors/matthias-benkort/page-1/)

Software Engineering Lead

Engineering

- ![](img/2022-02-03-implementing-hydra-heads-the-first-step-towards-the-full-hydra-vision.005.png)[](https://www.linkedin.com/in/matthias-benkort-47186a57/ "LinkedIn")
- ![](img/2022-02-03-implementing-hydra-heads-the-first-step-towards-the-full-hydra-vision.006.png)[](https://twitter.com/MBenkort "Twitter")
- ![](img/2022-02-03-implementing-hydra-heads-the-first-step-towards-the-full-hydra-vision.007.png)[](https://github.com/KtorZ "GitHub")

![Triển khai Hydra Heads: Bước đầu hướng tới tầm nhìn giao thức Hydra hoàn thiện](img/2022-02-03-implementing-hydra-heads-the-first-step-towards-the-full-hydra-vision.008.jpeg)

We’ve done the science and the theory. We have laid the foundations for a scalable, versatile, and high-throughput blockchain. Now it’s time for steady growth and system enhancements. With the goal of creating an optimized ecosystem to support and foster decentralized applications (DApps) development, Cardano is in the foothills of the Basho phase. With smart contracts already in place, Basho is all about [scaling](https://iohk.io/en/blog/posts/2022/01/14/how-we-re-scaling-cardano-in-2022/) and network optimization. The [Hydra](https://iohk.io/en/blog/posts/2021/09/17/hydra-cardano-s-solution-for-ultimate-scalability/) protocol family is a key component for this.

Chúng ta đã nói về Hydra trước đây. Hydra là một tổ hợp các giải pháp của Layer 2 được thiết kế để giải quyết vấn đề bảo mật mạng lưới và khả năng mở rộng. Ban đầu Layer 2 được hình thành trong phần việc của nhóm nghiên cứu Ouroboros, nhưng trên thực tế, điều này đã tạo ra một hành trình độc lập kể từ khi xuất bản báo cáo đầu tiên. Hydra cung cấp thông lượng tăng lên, giảm thiểu độ trễ và các giải pháp tiết kiệm chi phí mà không cần yêu cầu lưu trữ lượng dữ liệu lớn hơn. Giao thức Hydra Head được định hình vào [năm 2020](https://eprint.iacr.org/2020/299) và kể từ đó, tư duy của chúng tôi đã được phát triển - đặc biệt là trong suốt giai đoạn triển khai và chứng minh khái niệm ban đầu này. Dựa trên ý tưởng ban đầu đó, **giao thức Hydra Head ** đã phát triển thành [một bằng chứng về mặt  khái niệm](https://iohk.io/en/blog/posts/2021/09/17/hydra-cardano-s-solution-for-ultimate-scalability/) và tiếp tục như vậy khi chúng tôi hướng tới việc triển khai rõ hơn cho testnet MVP.

We have seen plenty of excitement (great!) along with misconceptions and misunderstandings (not so great). Most of these have arisen from the idea statement, rather than the actual protocol *implementation* and some of our earlier blogs have perhaps contributed to these misunderstandings. But the Hydra Head protocol isn’t solely about SPO implementation as much as the theoretical ‘1 million TPS’ – which needs to be caveated and better explained.

In this article, we – the Hydra engineering team – outline our current progress, our approach, and our near and long-term roadmap. We’ll demystify some misconceptions, clarify the benefits and reflect on development challenges.

## **Hydra Head in a nutshell**

Let’s first re-introduce Hydra Heads, which involve not only a robust networking layer between peers and an integrated Cardano ledger, but also, several on-chain scripts (smart contracts) that drive the lifecycle of a Hydra Head.

A Hydra Head is a provably secure [isomorphic state channel](https://www.google.com/url?q=https://eprint.iacr.org/2020/299.pdf&sa=D&source=docs&ust=1643024354663393&usg=AOvVaw2qBMRPzWu0H_7oIkQZkQX-). Simply put, it is an off-chain mini-ledger between a restricted set of participants, which works similarly (albeit significantly quicker) to the on-chain main ledger.

The first thing to understand is that a channel is a communication path between two or more peers. To be part of a Head means being one of those peers. Channels form isolated networks that can evolve in parallel to the main network. On these alternative networks, participants follow a different, simpler, consensus algorithm: everyone needs to agree on all transactions flowing through. A consequence of this is that, as a participant, I cannot lose money I haven't explicitly agreed to lose. Why? Because any valid transaction requires my *explicit* approval.

Khi thành lập một Head, những người tham gia có thể cam kết chuyển tiền cho nó. Điều này có nghĩa là chuyển tiền trên chuỗi đến một địa chỉ tập lệnh rồi khóa chúng theo các quy tắc cụ thể. Tập lệnh đảm bảo thực thi an toàn giao thức trên chuỗi và đặc biệt, những người tham gia không thể gian lận lẫn nhau. Tuy nhiên, bất kỳ người tham gia nào cũng có thể quyết định rời bỏ Head bằng cách đóng nó bất cứ lúc nào. Trong trường hợp này, tất cả những người tham gia bỏ đi với trạng thái mới nhất mà họ đã đồng thuận với off-chain, trên mạng song song của họ.

Think of Heads as ‘private poker tables’ where participants bring their own chips to play the game. Participants can play for as long as they want. If someone doesn't play, then the game doesn't progress. Yet, participants are still free to walk away with their chips. If they do so, the game ends with the current wealth distribution.

![Hydra Head (simplified) lifecycle](img/2022-02-03-implementing-hydra-heads-the-first-step-towards-the-full-hydra-vision.009.jpeg)

**Figure 1**. Hydra Head (simplified) life cycle

The dealer at the table (the on-chain script) ensures that people play by the rules and don't cheat. In the end, there are as many chips out as there were chips in, but they may have been redistributed during the course of the game. While the final result is known outside of the table, the history of all actions that happened during the game is only known to the participants.

This protocol is one of a whole suite of protocols that we usually refer to as ‘Hydra’. The current engineering effort is focused on implementing the Hydra Head protocol as published in [Hydra: Fast Isomorphic State-Channels](https://eprint.iacr.org/2020/299) by Chakravarty et al.

Khoảng cuối năm 2021, Maxim Jourenko, Mario Larangeira và Keisuke Tanaka đã xuất bản một bản lặp lại trên Hydra Head có tên là [Interhead Hydra: Two Heads are Better than One](https://eprint.iacr.org/2021/1188) . Sự lặp lại này xác định một phương pháp để kết nối hai Head với nhau, về lâu dài cho phép tạo ra một mạng lưới các Hydra Head được kết nối với nhau. Trước đây, đã có đề cập đến các giao thức khác như 'Hydra Tail'. Tuy nhiên, những điều này vẫn đang được nghiên cứu, cùng với những ý tưởng mới đến từ công việc gần đây về giao thức Hydra Head.

## **Hydra misconceptions**

Gần đây, chúng tôi đã thấy rất nhiều bình luận định vị Hydra là giải pháp 'tối thượng' cho khả năng mở rộng của Cardano. Hydra Heads chắc chắn tạo ra một nền tảng vững chắc để xây dựng một Layer về khả năng mở rộng cho Cardano. Chúng là một thành phần thiết yếu tận dụng sức mạnh của mô hình [ (EUTXO)](https://iohk.io/en/blog/posts/2021/03/12/cardanos-extended-utxo-accounting-model-part-2/) để cho phép các giải pháp phức tạp hơn ở trên cùng. Chúng là một yếu tố quan trọng của hành trình mở rộng, nhưng chúng không phải là đích đến *cuối cùng* .

**Scalability isn’t about a million TPS**

Before talking about scalability metrics, let’s clarify a few things about transactions per second (TPS). Amongst all those available, TPS is probably the least meaningful metric to consider as a means of comparison. Transactions come in different shapes and sizes. While this is true for Cardano, it’s even more essential when comparing two drastically different systems.

Hãy nghĩ về đường cao tốc và các phương tiện đi lại. Người ta có thể xem có bao nhiêu 'Xe mỗi giây' (VPS) mà đường cao tốc có thể quản lý giữa hai điểm. Tuy nhiên, nếu không có định nghĩa chung về phương tiện là gì, thì việc so sánh 10 VPS với 100 VPS dường như là vô nghĩa. Nếu 10 chiếc xe trong ví dụ là những chiếc xe tải chở hàng lớn, liệu có hợp lý khi so sánh chúng với 100 chiếc xe tay ga về khả năng giao hàng của chúng không? Điều này cũng áp dụng cho các giao dịch. Một giao dịch mang hàng trăm tài sản gốc và đầu ra chắc chắn không giống như một giao dịch thanh toán ADA đơn lẻ giữa hai diễn viên.

Using TPS as a metric within the same context (for example, to compare two versions of the Cardano node) is meaningful. Using it as a means of comparison between blockchains isn’t.

With that in mind, we suggest looking not only at throughput, but also at finality and concurrency as important metrics to consider and discuss scalability:

- **Thông lượng** (Throughput) là khối lượng dữ liệu được hệ thống xử lý trong một khoảng thời gian nhất định.
- [**&nbsp;Tính minh bạch**](https://docs.cardano.org/core-concepts/chain-confirmation-versus-transaction-confirmation) (finality) là thời gian cần thiết để kết quả của một số hành động trở thành bất biến và đúng với mọi người trong hệ thống.
- **Tính đồng thời** (concurrency) là số lượng công việc có thể được thực hiện bởi các tác nhân khác nhau mà không cản trở nhau.

Hydra Heads nổi trội trong việc đạt được kết quả gần như tức thì trong một Head. Quá trình thiết lập và đóng Head có thể mất một vài block, nhưng sau khi được thiết lập, các giao dịch có thể diễn ra nhanh chóng giữa những người tham gia hợp tác. Vì các Hydra Heads cũng sử dụng mô hình EUTXO nên chúng có thể xử lý đồng thời các giao dịch mà không có mâu thuẫn, điều này - đi đôi với việc có mạng lưới tốt - cho phép sử dụng tối ưu các tài nguyên có sẵn. Các mô phỏng đầu tiên của giao thức Hydra Head vào năm 2020 cho thấy '1000 TPS' là rất hứa hẹn. Hiện chúng tôi đang trong quá trình đánh giá việc triển khai thực tế về mặt thông lượng và tính minh bạch.

Có một lưu ý: Hydra Head là một công trình *cục bộ* trong một nhóm nhỏ những người tham gia. Các nhóm này ban đầu sẽ độc lập và do đó, việc xem xét tổng thể các chỉ số riêng lẻ của họ là sai lệch. Vì các nhóm độc lập và có thể được tạo ra độc lập theo ý muốn, nên dễ dàng đạt được bất kỳ con số nào bằng cách cộng chúng thành: mười, một nghìn, một triệu, một tỷ, v.v.

Consequently, while the first version of the Hydra Head protocol will allow for small groups of participants to scale up their traffic at low cost, it won’t immediately offer a solution for global consumer-to-consumer (micro) payments or NFT sales. Why? Because the consensus inside a Head requires every participant to react to every transaction. And a single head doesn't scale infinitely with the number of participants, at least not without some additional engineering efforts. For example, the interconnection of Hydra Heads paves the way for larger networks of participants, effectively turning local Heads into a global network. We are exploring several other ideas to extend the Hydra Head protocol to broaden the set of use cases it can cover. We will talk more about that in the next sections and in future updates.

**Use cases and the role of SPOs**

So when are Heads useful? Hydra Heads shine when a small group of participants need to process many quick interactions. Imagine, for example, a pay-per-use API service, a bank-to-bank private network, or a fast-paced auction between a seller and a small group of bidders. The use cases are plenty and take various forms. Some of them may be long-running Heads going for months, whereas others may be much shorter and only last a few hours.

Our [initial Hydra research in 2020](https://iohk.io/en/blog/posts/2020/03/26/enter-the-hydra-scaling-distributed-ledgers-the-evidence-based-way/) suggested stake pool operators (SPOs) as *likely* candidates for running Hydra Heads. However, as the Hydra Head protocol has been researched and built as a proof of concept, we can firmly state that it is a misunderstanding to say that *only* SPOs should run a Hydra Head to ensure ledger scalability. In fact, SPOs have no intrinsic interest in opening Heads between each other without a reason to transact (tipping or trading NFTs, for example). In a way, SPOs are like any other actor when it comes to the Hydra Head protocol. They can be a participant and open up Heads with other peers, but so can anyone interested.

Admittedly, SPOs are good in operating infrastructure and can be some of the first users running instances of the Hydra Head protocol. Still, this only allows participating SPOs to transact with one another, which limits use cases for end users. Only advanced layer 2 system designs like the Interhead Hydra protocol require intermediaries to run infrastructure to the benefit of end users. In fact, we anticipate that one likely setup for Hydra Heads will be providing users managed Hydra Heads as a service (HaaS). We can achieve this without giving up custody of funds by running the infrastructure on the behalf of end users, who generally have neither the interest nor the technical skills to maintain such infrastructure.

This is very similar to the current operational model of light wallets and light wallet providers that are much more likely to be running Hydra Heads in the long run. Imagine a network composed of the top light wallet providers within the Cardano ecosystem. Such providers can then facilitate instant and cheap payments between their users while ensuring overall trust.

We also envision that services for developers and DApp providers will be likely candidates for running Hydra Heads. Indeed, DApp developers require access to on-chain information. For that, developers may rely on online services that provide adequate interfaces and typically charge monthly usage fees. Hydra Heads can improve this process enabling a more decentralized business model with pay-per-use API calls between service providers and DApp developers.

## **The roadmap**

Là một nhóm các giao thức sẽ được phân phối theo thời gian và liên quan đến các thiết kế hệ thống Layer 2 được trau chuốt hơn trên giao thức Hydra Head, điều quan trọng là chúng tôi phải thường xuyên tham gia cùng các nhà phát triển của hệ sinh thái Cardano. Đây không phải là về một bản phát hành 'lớn' mà là một chu kỳ phát hành lặp đi lặp lại. Chúng tôi cần hiểu những thách thức của nhà phát triển, đảm bảo đáp ứng nhu cầu của họ và cuối cùng đảm bảo rằng chúng tôi đang xây dựng thứ gì đó hữu ích. Đây là lý do tại sao, năm ngoái, chúng tôi đã phát triển Hydra Head như một dự án GitHub có mã nguồn mở, bắt đầu với một bằng chứng về khái niệm ban đầu. Điều này nhằm mục đích hướng tới một chu kỳ phát hành thường xuyên và liên tục, chúng tôi đã phát hành bản xem trước dành cho nhà phát triển ban đầu của mình vào tháng 9 năm 2021 (0.1.0), sau đó là lần lặp thứ hai (0.2.0) trước Giáng sinh. Bản cập nhật tiếp theo (0,3,0) sẽ vào tháng Hai năm 2022. Chúng tôi tuân theo cách lập phiên bản ngữ nghĩa và mỗi bản phát hành trước đó (0.x.0) đều bổ sung các tính năng có sẵn cho các đối tác của chúng tôi và những người chấp nhận sớm để thử nghiệm trên (các) mạng testnet riêng của Cardano và trên mạng công khai của cộng đồng.

We’re delighted to announce that *our [roadmap is now also available on Github](https://github.com/orgs/input-output-hk/projects/21)!* As a means to engage with our community of developers and to be transparent about the course of our development efforts, you will find [feature issues](https://github.com/input-output-hk/hydra-poc/labels/feature), [milestones](https://github.com/input-output-hk/hydra-poc/milestones), and [projects boards](https://github.com/input-output-hk/hydra-poc/projects?type=beta) available on the [Hydra Head repository.](https://github.com/input-output-hk/hydra-poc/)

While our focus is creating meaningful and feature-packed releases as we journey along testnet and later mainnet maturity with version 1.0.0, the roadmap also includes tentative dates. These forecasts stem from both the work accomplished so far and our estimates of the work remaining ahead. We’ll reflect on the content and the dates regularly in an agile manner to keep the roadmap as accurate as possible.

**Community feedback is essential**

We will measure our success by how much traffic will be running in Hydra Heads in comparison to the Cardano mainnet. This means that we can’t reach our goal without the community, and Hydra can only be successful if it is useful to current and future Cardano users.

Tùy thuộc vào thời gian, kỹ năng và chuyên môn của bạn, chúng tôi hoan nghênh bạn tham gia cùng chúng tôi để chia sẻ câu hỏi, đưa ra các phản hồi hoặc đóng góp vào nỗ lực phát triển. Đây là cơ hội tuyệt vời để cùng nhau xây dựng toàn bộ hệ sinh thái gồm các giải pháp Layer 2 cho Cardano. Giao thức Hydra Head sẽ là thành phần đầu tiên của nhiều giải pháp tiên tiến ra đời. Tại IOG, chúng tôi đã bắt đầu làm việc với một trong số đó, mong rằng một số chắc chắn sẽ thành công (và may mắn thay!) Được xây dựng bởi các thành viên trong cộng đồng, nơi mà chúng tôi luôn mong muốn được hỗ trợ.

We’ll talk about Hydra Heads in more detail during February’s mid month development update. Subscribe to our [Youtube channel](https://www.youtube.com/c/IohkIo) and come join us!

*Tôi muốn cảm ơn Sebastian Nagel, Olga Hryniuk, Mark Irwin và Tim Harrison vì những ý kiến đóng góp và hỗ trợ của họ trong việc chuẩn bị bài đăng trên blog này.<br><br>Bài này được dịch bởi minh-hieu-102 <a class="_active_edit_href" href="https://iohk.io/en/blog/posts/2022/02/03/implementing-hydra-heads-the-first-step-towards-the-full-hydra-vision/)&lt;br&gt;">với bài gốc</a><br>*Dự án này được tài trợ bới Catalyst**
