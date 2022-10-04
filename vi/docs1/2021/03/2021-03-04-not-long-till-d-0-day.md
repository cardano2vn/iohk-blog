# Gần tới ngày hệ số 'd'= 0

### **Chúng ta đang tiến nhanh đến phi tập trung hoàn toàn việc đóng block trên Cardano. Đây là thời điểm thích hợp để suy ngẫm về sự phát triển của mạng lưới**

![](img/2021-03-04-not-long-till-d-0-day.002.png) 4 March 2021![](img/2021-03-04-not-long-till-d-0-day.002.png)[ Colin L Edwards](tmp//en/blog/authors/colin-edwards/page-1/)![](img/2021-03-04-not-long-till-d-0-day.003.png) 8 mins read

![Colin L Edwards](img/2021-03-04-not-long-till-d-0-day.004.png)[](tmp//en/blog/authors/colin-edwards/page-1/)

### [**Colin L Edwards**](tmp//en/blog/authors/colin-edwards/page-1/)

Quantitative Strategist

Commercial

- ![](img/2021-03-04-not-long-till-d-0-day.005.png)[](mailto:colin.edwards@iohk.io "Email")
- ![](img/2021-03-04-not-long-till-d-0-day.006.png)[](https://www.linkedin.com/in/colin-edwards-04938a5/ "LinkedIn")

![Not long till 'd' (=0) day](img/2021-03-04-not-long-till-d-0-day.007.jpeg)

Vào cuối tháng 3, chúng ta sẽ đạt được một cột mốc quan trọng khác cho Cardano khi chúng ta thấy hệ số "d", hệ số điều chỉnh tỷ lệ phần trăm giao dịch được xử lý bởi các node genesis, về 0. Tại thời điểm này, trách nhiệm đóng block sẽ được phi tập trung hoàn toàn. Nói cách khác, mạng lưới hơn 1.800 pool cộng đồng của Cardano sẽ tự chịu trách nhiệm sản xuất các block.

Ngày *d*=0 sẽ là một thời điểm quan trọng trong hành trình của Cardano. Khi chúng tôi triển khai bản cập nhật Shelley vào tháng 7 năm 2020, "d" được đặt thành 1.0, có nghĩa là mọi block được tạo ra bởi mạng lưới các node liên kết của IOHK. Tất nhiên, điều này trái ngược với phi tập trung nhưng là một cách tiếp cận khôn ngoan (tức là an toàn) trong thời gian tới trong khi mạng lưới các nhà điều hành pool cổ phần (SPO) bắt đầu và vận hành.

### **Preparing for *d*=0 day**

Theo thời gian, chúng tôi đã giảm dần *d* với tốc độ 0,02 mỗi epoch (nói cách khác, cứ năm ngày lại tăng hai điểm phần trăm để trao quyền sản xuất block cho cộng đồng). Vào ngày bài blog này được xuất bản, chúng tôi đang ở mức *d* = 0,12 với 88% block được tạo bởi các pool cộng đồng và chỉ 12% bởi các node liên kết.

Nói một cách đơn giản, khi *d* giảm, cộng đồng sẽ tạo ra nhiều block hơn và nhiều stake pool hơn có thể đóng block. Khi hệ số *d* giảm đi, sự đa dạng của mạng lưới và sự phân bố địa lý sẽ mở rộng.

On March 31, at the boundary of epoch 257, *d* will reach zero. That day will be special because while *d* may be small, its significance is huge. In this context, that zero heralds the most important outward indicator of decentralization, a parameterized symbol supporting a core tenet of our philosophy – *d=0 pushes power to the edges*.

Khi chúng tôi tiếp tục chuyển sang phi tập trung hoàn toàn, đây cũng là thời điểm tốt để tham khảo các thông số khác chi phối sự phát triển của mạng lưới Cardano và xem xét một số thay đổi mà chúng tôi đã nhìn thấy.

 Số *d* chỉ là một trong hơn 20 tham số chi phối hoạt động và tình trạng mạng lưới. Bộ thông số này là 'đòn bẩy' để quản lý và chỉ đạo hoạt động hiệu quả và tự nhiên của [hệ thống proof of stake phi tập trung](https://iohk.io/en/blog/posts/2020/11/13/the-general-perspective-on-staking-in-cardano/). Cuối cùng cộng đồng sẽ thúc đẩy sự phát triển của Cardano thông qua các quy tắc quản trị ở kỷ nguyên Voltaire, nhưng cho đến lúc đó, nhiệm vụ của chúng tôi là quản lý các thông số này. Quyền giám hộ của chúng tôi yêu cầu chúng tôi thực hiện các điều chỉnh theo yêu cầu để xây dựng và duy trì sức khỏe của mạng lưới.

### **Why the *k* parameter is special**

Aside from more technical considerations, we remain committed to supporting smaller stake pools, because we believe this approach aligns with our long-term goal of creating the most decentralized and economically sustainable ecosystem of stake pools. This is further reflected in our [delegation approach](https://iohk.io/en/blog/posts/2020/12/10/delegating-to-decentralize-and-build-value/), which throughout 2021 will aim to support stake pool diversity.

Năm ngoái, chúng tôi đã thực hiện điều chỉnh đáng kể đầu tiên đối với các thông số mạng khi chuyển *k* từ 150 thành *k* = 500 (nghĩa là một hệ thống được tối ưu hóa khi khởi chạy cho 150 pool đóng block, mặc dù các pool khác có thể đóng block). Điều này xảy ra sau cuộc tranh luận rộng rãi, cả trong IOHK, Cardano Foundation và với cộng đồng SPO.

Việc chuyển sang *k* = 500 là một quyết định cân bằng dựa trên nhu cầu tạo cơ hội cho nhiều pool đóng block hơn (bằng cách khuyến khích cổ phần từ các pool bão hòa sang các pool mới), đồng thời hỗ trợ các pool đóng được block và giảm thiểu sự gián đoạn cho người ủy quyền. Nhìn chung, nó đã được chứng minh là thành công - hãy đi sâu hơn một chút.

### **The change to *k*=500**

Prior to the announcement that *k* was changing, 54.6% of all delegated ada was represented by the 10 largest stake pools and 45.4% of ada represented by smaller pools. Following the change to *k*=500, those numbers have reversed: 55.9% of ada is now represented by pools other than the 10 largest.

![](img/2021-03-04-not-long-till-d-0-day.008.png)

This was a dramatic change directly linked to the change in *k*.

![](img/2021-03-04-not-long-till-d-0-day.009.png)

It is a great start, but our goal is to continue to optimize the network. So we observed what happened, gathered feedback, and incorporated everything we learned into making the next round of changes.

Pools will split when it makes economic sense to do so. For those pools with a greater proportion of pledge, the more pledge they have, the more valuable it is and the more reason SPOs have to keep their pledge together. Conversely, if a pool has a low level of pledge, there is very little reason not to split it further to start additional pools.

While there is a cost associated with running a small pool, and given the current appreciation in the value of ada, we believe that the financial incentive for splitting pledge is even stronger now. Increasing *k* – for example to 1,000 – without addressing this first, would not lead to a more distributed and diverse ecosystem which, to be clear, is the objective. We will simply see many of the same operators just running twice as many pools.

### **Changing pledge**

The *a0* parameter rewards SPOs for concentrating their pledge into a small number of pools. This has been effective in encouraging pools with high levels of ada pledge to consolidate that into large private pools (as we at IOHK do) and therefore give smaller pools greater opportunity to attract delegation.

However, we believe the current system can be improved, so for some time now, we have been discussing and modeling options to make pledge more effective at addressing pool splitting for lower pledge levels.

The current structure of the rewards formula does not give us the flexibility to tweak the impact by a simple parameter change; we will need to modify the rewards formula, which is something our research team has been working on for some time.

Several promising candidates have come out of that evaluation process. We’d like at this point to acknowledge the valuable work from community contributor Shawn McMurdo in his [Curve Pledge Benefit improvement proposal](https://github.com/cardano-foundation/CIPs/pull/12) for helping to develop the thinking in this area.

Our research team is in the late stages of finalizing an approach. They will soon present their findings, and we will update the community then. However, the team has now concluded that *a0* should change. We believe this change will greatly benefit the network, making the system more sustainable, widely distributed, and globally diverse. It will also increase the earnings of all public pools (ie, those that are not already fully 'saturated' with pledge).

Mặc dù đây là một vấn đề thảo luận nội bộ, chúng tôi cũng đã kết luận rằng bất kỳ sự thay đổi nào của hệ số *k* sẽ đến sau khi thay đổi công thức cho *a0* để mang lại kết quả như mong muốn (đặc biệt khuyến khích tiền đặt cược tham gia vào các pool nhỏ hơn là chia nhỏ các pool). Vì đây là sự sửa đổi công thức hoàn chỉnh và không còn nằm trong một epoch đơn giản, nên nó cần được phát hành như một phần của hard fork. Với sản phẩm pipeline và sự tập trung hiện tại của pool vào việc tiếp tục triển khai Goguen và chúng tôi sẽ thực hiện thay đổi này trong quý ba của năm.

### **Other considerations**

Other factors need to be considered. Chief among these is the availability of multi-pool delegation, to allow ada holders to spread their stake across a number of pools from a single wallet. This requires significant backend work from the core development team, along with a new interface and business rules adjustments. We would also like – if possible – to offer better pledging options for SPOs from Daedalus in a similar timeframe (currently only available via CLI or AdaLite), which means additional development work not only for internal teams but also for the Ledger and Trezor wallet companies.

Chúng tôi cũng sẽ tiếp tục nghiên cứu các thông số khác như phí tối thiểu (được thực hiện để ngăn chặn 'race to the bottom (cuộc đua xuống đáy)' tuy nhiên bị lệch so với các pool nhỏ hơn) trong khi tiếp tục đo điểm chuẩn và tối ưu hóa hiệu suất node khi chức năng hợp đồng thông minh ra mắt. Trách nhiệm và cam kết của chúng tôi vẫn là đạt được sự cân bằng tinh tế giữa tính ổn định, khả năng mở rộng và sức khỏe tổng thể của mạng lưới với một hệ sinh thái phát triển mạnh mẽ của các nhà điều hành pool và người ủy quyền.

### **Evolving into the future**

As we promote the health of the network and stake pool ecosystem, we continue to monitor and research other important parameters and values. This work considers both the tactical and strategic approaches we may take.

With the increase in the price of ada, implementation of native tokens, and anticipating smart contracts, we also continue to assess and review the Cardano fee structure. For example, based on community feedback, we are considering the tactical approach of immediately lowering some fees. The minimum fixed fee of 340 ada for stake pools is one strong candidate for change; network transaction fees and deposits for smart contracts are also under discussion.

Our researchers and analysts are also working with an external economic consulting group to formalize an optimization approach that ensures fees will remain stable and predictable over the longer term. The results of this review will include a governance model with a clear mandate about when and how fees should be determined in the future as we develop, optimize and scale the network. We’ll be sure to keep the community informed and involved as our thinking develops.

*Tôi muốn cảm ơn và ghi nhận ý kiến đóng góp của Francisco Landino, Lars Brünjes, Aikaterini-Panagiota Stouka, Aggelos Kiayias và Tim Harrison ​​cho bài viết và cảm ơn sự phản hồi của họ trong cả bài viết.Bài này được dịch bởi Thanhtintran, Review bởi Pham Quang, biên tập bởi ... Bài viết nguồn [tại đây]https://iohk.io/en/blog/posts/2021/03/04/not-long-till-d-0-day/*Dự án này được tài trợ bởi Catalyst**
