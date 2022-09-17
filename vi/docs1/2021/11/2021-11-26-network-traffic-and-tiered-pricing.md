# Lưu lượng mạng lưới và hệ thống phí phân cấp

### **Tài chính phi tập trung (DeFi) sẽ tiếp tục thúc đẩy nhu cầu trên Cardano. Dự án nghiên cứu của chúng tôi đang tìm cách duy trì quyền truy cập và thông lượng công bằng cho mọi người dùng**

![](img/2021-11-26-network-traffic-and-tiered-pricing.002.png) Ngày 26 tháng 11 năm 2021![](img/2021-11-26-network-traffic-and-tiered-pricing.002.png) [Philip Lazos](tmp//en/blog/authors/philip-lazos/page-1/)![](img/2021-11-26-network-traffic-and-tiered-pricing.003.png) 7 phút đọc

![Philip Lazos](https://gitlocalize.com/repo/7823/vi/docs1/2021/11/img/2021-11-26-network-traffic-and-tiered-pricing.004.png)[](tmp//en/blog/authors/philip-lazos/page-1/)

### [**Philip Lazos**](tmp//en/blog/authors/philip-lazos/page-1/)

Research Fellow

Academic Research

- ![](img/2021-11-26-network-traffic-and-tiered-pricing.005.png)[](mailto:philip.lazos@iohk.io "Email")

![Network traffic and tiered pricing](https://gitlocalize.com/repo/7823/vi/docs1/2021/11/img/2021-11-26-network-traffic-and-tiered-pricing.006.jpeg)

Một bài đăng trên blog gần đây đã tóm lược một số cách mà mạng lưới Cardano sẽ [phát triển và điều chỉnh linh hoạt](https://iohk.io/en/blog/posts/2021/11/22/slow-and-steady-wins-the-race-network-evolution-for-network-growth/) để đáp ứng nhu cầu toàn cầu của các hợp đồng thông minh và DeFi. Tương tự như vậy, việc nâng cấp hệ thống phí giao dịch sử dụng cho Cardano cũng trở nên cần thiết.

Hệ thống hiện tại hoạt động một cách đơn giản và công bằng: mọi giao dịch đều được đối xử như nhau và người dùng không thể thay đổi mức độ ưu tiên của giao dịch bằng cách trả phí cao hơn. Miễn là năng lực thông lượng mạng đáp ứng được nhu cầu, thì cách tiếp cận này vẫn hoạt động tốt.

Tuy nhiên, hệ thống này tồn tại những hạn chế. Khi việc sử dụng Cardano tăng lên, đến một lúc nào đó, không phải tất cả các giao dịch đều có thể được đưa vào blockchain, ngay cả khi đã thực hiện điều chỉnh các tham số hệ thống. Mặc dù việc gia tăng năng lực của chuỗi chính và/hoặc chuyển hướng giao dịch sang [Hydra](https://iohk.io/en/blog/posts/2021/09/17/hydra-cardano-s-solution-for-ultimate-scalability/) hoặc các giải pháp layer 2 khác có thể giúp giảm bớt mối lo ngại này, tuy nhiên hệ thống cốt lõi vẫn phải hoạt động một cách nhẹ nhàng trong mọi trường hợp có thể và mọi lúc.

This is especially relevant in the case of a denial of service (DoS) attack. With the system as is, an attacker could take advantage of the fair treatment and pass off their malicious spam as legitimate transactions, increasing waiting times for everyone else. There are measures in place (eg, relating to transaction propagation through the peer-to-peer network) that make such an attack technically challenging. However, for extra protection, we would like to be able to increase the costs of such attacks without jeopardizing the fairness and price efficiency of the whole system.

This is a topic members of IO Groupâ€™s research team have been looking at this year. The resulting approach proposed in this post maintains the pillars of Cardano transaction processing (predictability, fairness and inexpensive access) while mitigating the issues that could arise from greater demand. Our approach puts forth a novel transaction fee mechanism for blockchains. The key to the design is partitioning each block into three â€˜tiersâ€™ based on use case. Each tier makes up a set percentage of the maximum block size and is designed for different types of transactions (Figure 1). The tiers, along with the suggested split we are analyzing at present, would be:

- fair (50%)
- balanced (30%)
- immediate (20%)

![](img/2021-11-26-network-traffic-and-tiered-pricing.007.jpeg)

#### **Figure 1. Each block would be split into three tiers.**

We will discuss the fair segment last, because it works differently from the other two. Balanced and immediate work by having a â€˜fee thresholdâ€™, which is different for each. To be included in a block, transaction issuers would specify the tier of service they need. This can be done by setting a maximum fee for the transaction. Then, each block would be filled starting with the immediate, then balanced, and finally fair tiers. Similar transactions within the same tier would pay the same fee. To make this choice simple, each transaction would only be charged the lowest fee that would guarantee its entry in the block. After every block, fees for immediate and balanced tiers would be updated dynamically and deterministically (reflecting the level of demand in previous blocks) to ensure that each segment uses its target percentage of the block.

Sự khác biệt giữa cấp 'ngay lập tức' và cấp 'cân bằng' là cách mà phí được cập nhật, cụ thể là 'tốc độ' điều chỉnh phí căn cứ theo lượng tải mạng hiện tại. Ngưỡng phí cho dịch vụ 'ngay lập tức' sẽ luôn cao hơn mức 'cân bằng' và sẽ phản ứng mạnh hơn với nhu cầu, đảm bảo rằng giao dịch yêu cầu sẽ được phục vụ càng sớm càng tốt. Ngưỡng phí 'cân bằng' sẽ chậm thích ứng hơn và ổn định hơn: điều này khiến nó không phù hợp với các giao dịch nhạy cảm về thời gian, nhưng sẽ cung cấp mức phí thấp hơn, độ tin cậy cao hơn, đổi lại là thời gian chờ nhiều hơn.

While the balanced and immediate tiers aim to handle transactions with different levels of urgency, the fair tier handles ordinary transactions. The fair segment is intended to serve as a refinement of the current system in Cardano, keeping the fees low (or in the future even stable, by pegging to a basket of commodities/fiat, as explained in the [post on stablefees](https://iohk.io/en/blog/posts/2021/06/10/stablefees-and-the-decentralized-reserve-system/)) and removing any unpredictability from the userâ€™s perspective. As long as demand is low (and the transactions fit into half of the block) this segment would function as Cardano does now.

However, once demand rises, a special mechanism would kick in for fair tier transactions. The mechanism would filter transactions in a manner independent of fees and be based on a prioritization function. One example of this would be to give priority to transactions depending on the age and amount of their UTXOs. In particular, the priority of a given transaction would be equal to the sum of the amount of each input multiplied by its age and then divided by the total size of the transactions in bytes. This priority could be used in conjunction with a threshold (updated dynamically after every block) that would filter transactions whose priority is too low. Such an approach guarantees liveness for each transaction at a low and predictable price and limits the effect a malicious attacker (or a surge of demand) could have on prices, by always providing an inexpensive way into each block.

The tiered pricing idea presented here also extends and clarifies the concept of the multiplier that we introduced in the stablefees post. Viewed in this way, each of the three tiers is associated with a deterministically calculated multiplier (with the fair tier always at a multiplier of 1) whose value depends on the congestion of the respective tier in previous blocks.

This mechanism is different from current pricing approaches, as used by Bitcoin or Ethereum (even with Ethereum Improvement Proposal 1559), where there is a variable fee that each transaction must exceed to make it into a block. The downside of this approach is that the fee everyone needs to pay is dictated by the â€˜richestâ€™ consumers. Even worse, this is the fee paid by the richest consumers to make it into a block â€˜immediatelyâ€™. In addition, even though the fees are mostly a function of supply and demand, these particular types of transaction fee mechanism can inadvertently â€˜shapeâ€™ demand, or inadvertently increase prices because the optimal bidding strategy is not clear to users. Imagine if the transaction fees of Bitcoin were halved suddenly and everyone forgot what they used to be, would they still rise to their current levels? Answering â€˜noâ€™ to this question illustrates the downsides of such mechanisms and is a predicament that tiered pricing precludes by design.

Cách tiếp cận theo cấp được tinh chỉnh hơn. Nó hiểu rằng không phải mọi giao dịch đều có nhu cầu giống nhau, đảm bảo rằng các tình huống sử dụng khác nhau có thể xảy ra đồng thời và giúp người dùng dễ dàng lựa chọn loại dịch vụ mong muốn. Theo cách này, phí phân cấp giúp có các khoản phí hợp lý và có thể đoán trước được trong khi kiểm soát được các giai đoạn tắc nghẽn trên chuỗi chính. Kết hợp với các cải tiến trong thiết kế sẽ được tiết lộ trong các bài đăng sau, tập trung vào việc tăng năng lực thông lượng thô và sức mạnh xử lý của chuỗi chính, hệ thống phí phân cấp cho thấy Cardano sẽ có thể đáp ứng bất kỳ tình huống nào về nhu cầu xử lý giao dịch.

*Tôi muốn ghi nhận những đóng góp của Giorgos Panagiotakos, Aggelos Kiayias và Elias Koutsoupias cho bài đăng này. Chúng tôi cùng nhau thành lập nhóm nghiên cứu về thiết kế của cơ chế này. Sẽ sớm có bài báo kỹ thuật.<br><br><br><br>Bài này được dịch bởi Hoàng Tâm <a class="_active_edit_href" href="https://iohk.io/en/blog/posts/2021/11/26/network-traffic-and-tiered-pricing/">[với bài gốc]</a><br><em>Dự án này được tài trợ bởi Catalyst</em>*
