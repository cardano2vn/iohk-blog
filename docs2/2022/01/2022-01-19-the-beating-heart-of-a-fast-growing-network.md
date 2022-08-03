# The beating heart of a fast-growing network
### **At the core of the Cardano network lies the node. Here’s how this integral technology will play its part as we scale Cardano during 2022**
![](img/2022-01-19-the-beating-heart-of-a-fast-growing-network.002.png) 19 January 2022![](img/2022-01-19-the-beating-heart-of-a-fast-growing-network.002.png)[ John Woods](tmp//en/blog/authors/john-woods/page-1/)![](img/2022-01-19-the-beating-heart-of-a-fast-growing-network.003.png) 5 mins read

![John Woods](img/2022-01-19-the-beating-heart-of-a-fast-growing-network.004.png)[](tmp//en/blog/authors/john-woods/page-1/)
### [**John Woods**](tmp//en/blog/authors/john-woods/page-1/)
Director of Cardano Architecture

Engineering

- ![](img/2022-01-19-the-beating-heart-of-a-fast-growing-network.005.png)[](mailto:john.woods@iohk.io "Email")
- ![](img/2022-01-19-the-beating-heart-of-a-fast-growing-network.006.png)[](https://www.linkedin.com/in/johnalanwoods/ "LinkedIn")
- ![](img/2022-01-19-the-beating-heart-of-a-fast-growing-network.007.png)[](https://github.com/johnalanwoods "GitHub")

![The beating heart of a fast-growing network](img/2022-01-19-the-beating-heart-of-a-fast-growing-network.008.jpeg)

In a [recent post](https://iohk.io/en/blog/posts/2021/11/22/slow-and-steady-wins-the-race-network-evolution-for-network-growth/), we discussed our methodical approach to preparing Cardano for its expected growth over the coming weeks and months. As more and more decentralized applications make Cardano their home, and as the decentralized finance (DeFi) and ‘[RealFi](https://iohk.io/en/blog/posts/2021/11/25/welcome-to-the-age-of-realfi/)’ ecosystem expands and evolves, the blockchain needs to be able to perform accordingly.

Trong một [bài đăng gần đây] (https://iohk.io/en/blog/posts/2021/11/22/slow-andeady-wins-the-race-network-evolution-for-network-growth/)
, chúng tôi đã thảo luận về cách tiếp cận có phương pháp của chúng tôi để chuẩn bị Cardano cho sự tăng trưởng dự kiến trong những tuần và tháng tới.
Khi ngày càng có nhiều ứng dụng phi tập trung trở thành nhà của Cardano, và là tài chính phi tập trung (defi) và '[realfi] (https://iohk.io/en/blog/posts/2021/11/25/welcome-to-the
-Age-of-realfi/) 'Hệ sinh thái mở rộng và phát triển, blockchain cần có khả năng thực hiện tương ứng.

Cardano is entering the Basho phase with a focus on [optimization, scaling, and network growth](https://iohk.io/en/blog/posts/2022/01/14/how-we-re-scaling-cardano-in-2022/). We anticipate a significant increase in transactional traffic over the months ahead, and here’s where we start the process of flexing to meet this. Improvements to the core node are part of this and we have packed node v1.33.0 full of new features and improvements to existing elements, upping Cardano’s expressiveness and the chain’s ability to do more.

Cardano đang bước vào giai đoạn BASHO với trọng tâm là [tối ưu hóa, mở rộng và tăng trưởng mạng] (https://iohk.io/en/blog/posts/2022/01/14/how-we-re-re-scaling-cardano-
Trong 2022/).
Chúng tôi dự đoán sẽ tăng đáng kể lưu lượng giao dịch giao dịch trong những tháng tới, và tại đây, nơi chúng tôi bắt đầu quá trình uốn cong để đáp ứng điều này.
Những cải tiến cho nút lõi là một phần của điều này và chúng tôi đã đóng gói nút V1.33.0 đầy đủ các tính năng và cải tiến mới cho các yếu tố hiện có, tăng tính biểu cảm của Cardano, và khả năng của chuỗi để làm nhiều hơn.

## **What's in a node?**

## ** Có gì trong nút? **

Node v1.33.0 – released in early January and now running on circa 80% of SPO systems – has been designed with elegance and efficiency in mind. The improvements made are designed to reduce block propagation time, so we get greater headroom to make the changes we need to accommodate DApps, decentralized exchanges (DEXs), DeFi environments, and so on.

Node v1.33.0 - được phát hành vào đầu tháng 1 và hiện đang chạy trên khoảng 80% hệ thống SPO - đã được thiết kế với sự thanh lịch và hiệu quả trong tâm trí.
Các cải tiến được thiết kế để giảm thời gian lan truyền khối, vì vậy chúng tôi có được khoảng trống lớn hơn để thực hiện những thay đổi chúng tôi cần để phù hợp với DAPP, trao đổi phi tập trung (DEXS), môi trường DEFI, v.v.

Following the implementation of the version of the node, blocks now propagate faster. This gives us extra time that we can use to implement other enhancements.

Sau khi thực hiện phiên bản của nút, các khối hiện tuyên truyền nhanh hơn.
Điều này cho chúng ta thêm thời gian mà chúng ta có thể sử dụng để thực hiện các cải tiến khác.

Technical improvements included in node v1.33.0 can be broadly categorized in **RAM usage optimization** and **efficiency upgrades**.

Các cải tiến kỹ thuật bao gồm trong nút v1.33.0 có thể được phân loại rộng rãi trong ** Tối ưu hóa sử dụng RAM ** và ** nâng cấp hiệu quả **.

**RAM usage optimization**

** Tối ưu hóa sử dụng RAM **

The new node supports a significant drop in memory usage because of two factors: memory compaction and more efficient memory sharing (rather than multiple instances of the same object, now multiple flows within the system will use the same object.)

Nút mới hỗ trợ việc sử dụng bộ nhớ giảm đáng kể do hai yếu tố: nén bộ nhớ và chia sẻ bộ nhớ hiệu quả hơn (thay vì nhiều trường hợp của cùng một đối tượng, bây giờ nhiều luồng trong hệ thống sẽ sử dụng cùng một đối tượng.)

Specifically, there are memory improvements in Unspent Transaction Output (UTXO) handling, stake distribution, live stake distribution and pools, and hash representation. 

Cụ thể, có những cải tiến bộ nhớ trong xử lý đầu ra giao dịch không sử dụng (UTXO), phân phối cổ phần, phân phối cổ phần trực tiếp và nhóm và đại diện băm.

These improvements are:

Những cải tiến này là:

- UTXO handling

- Xử lý UTXO

Node v1.33.0 uses fewer words for transaction inputs.

Node v1.33.0 sử dụng ít từ hơn cho đầu vào giao dịch.

- Stake distribution

- Phân phối cổ phần

Stake distribution snapshots represent 35% of total live data. The new node achieves a reduction by a factor of eight by sharing and changing representation.

Ảnh chụp nhanh phân phối đại diện cho 35% tổng dữ liệu trực tiếp.
Node mới đạt được mức giảm bởi một hệ số tám bằng cách chia sẻ và thay đổi đại diện.

- Live stake distribution

- Phân phối cổ phần trực tiếp

Live stake distribution accounts for 22% of total live data within the system.

Phân phối trực tiếp chiếm 22% tổng số dữ liệu trực tiếp trong hệ thống.

Node v1.33.0 saves memory in two ways:

Node v1.33.0 lưu bộ nhớ theo hai cách:

Sharing by combining multiple maps that are keyed on stake addresses (a saving of 11 words per stake address for each map combined), and sharing of stake pool IDs (5 words).

Chia sẻ bằng cách kết hợp nhiều bản đồ được khóa trên địa chỉ cổ phần (lưu 11 từ trên mỗi địa chỉ cổ phần cho mỗi bản đồ kết hợp) và chia sẻ ID nhóm cổ phần (5 từ).

- Hash representation

- Đại diện băm

Hash representation now uses 5 words instead of 6. Since hashes are ubiquitous in the system, this change, while apparently insignificant, will lead to considerable improvements in efficiency.

Biểu diễn băm bây giờ sử dụng 5 từ thay vì 6. Vì băm có mặt khắp nơi trong hệ thống, sự thay đổi này, trong khi dường như không đáng kể, sẽ dẫn đến những cải thiện đáng kể về hiệu quả.

**Key facts about RAM memory usage optimization**

** Sự thật chính về Tối ưu hóa sử dụng bộ nhớ RAM **

The new node enables great savings in live data due to compaction and sharing.

Nút mới cho phép tiết kiệm lớn trong dữ liệu trực tiếp do nén và chia sẻ.

**Efficiency upgrades**

** Nâng cấp hiệu quả **

Apart from making memory usage far more efficient than in previous versions, node v1.33.0 includes changes to the algorithms that Cardano uses to calculate rewards and stake distribution.

Ngoài việc sử dụng bộ nhớ hiệu quả hơn nhiều so với các phiên bản trước, Node v1.33.0 bao gồm các thay đổi đối với các thuật toán mà Cardano sử dụng để tính toán phần thưởng và phân phối cổ phần.

The rationale for these changes is to address the uneven network performance that occurred when calculating rewards, which led to spikes in network load. The new reward calculation algorithm is now in place, so these spikes will not happen anymore.

Lý do cho những thay đổi này là giải quyết hiệu suất mạng không đồng đều xảy ra khi tính toán phần thưởng, dẫn đến tăng đột biến trong tải mạng.
Thuật toán tính toán phần thưởng mới hiện đã được áp dụng, vì vậy những chiếc gai này sẽ không xảy ra nữa.

The algorithm to calculate the rewards has changed from “column-major” over 4,000 pools, to a “row-major” over ~1m stake addresses. This allows spreading the calculation over 3 days, instead of 1 day (4,000 blocks).

Thuật toán để tính toán phần thưởng đã thay đổi từ các cột cột của Cột, hơn 4.000 nhóm, thành một địa chỉ cổ phần của Row Row Major trên ~ 1M.
Điều này cho phép lan truyền tính toán trong 3 ngày, thay vì 1 ngày (4.000 khối).

We have also made changes to make the calculation of stake distribution more efficient.

Chúng tôi cũng đã thực hiện các thay đổi để làm cho việc tính toán phân phối cổ phần hiệu quả hơn.

**Pipelining**

** Đường ống **

Later this year, we’ll make further significant improvements to the node. A node does a lot of work processing a block, then waits for another block to come along, etc. In between, the node is not so busy. This block propagation overhead (that is, the time interval where the node is relatively idle, often called 'dead space') can be reduced through certain techniques to make good use of that otherwise 'dead' time. This is where pipelining comes in. 

Cuối năm nay, chúng tôi sẽ cải thiện đáng kể hơn cho nút.
Một nút thực hiện rất nhiều công việc xử lý một khối, sau đó chờ một khối khác xuất hiện, v.v. Ở giữa, nút không quá bận.
Chi phí lan truyền khối này (nghĩa là khoảng thời gian mà nút tương đối không hoạt động, thường được gọi là 'không gian chết') có thể được giảm thông qua một số kỹ thuật nhất định để sử dụng tốt thời gian 'chết' đó.
Đây là nơi đường ống đến.

This technique coalesces the validation and propagation of blocks. Now, instead of following the process of getting a header, validate it, then get its corresponding block, validate, and then send it to peer, now we get a header, validate, and send it to the peer, without validating the block. This streamlining will give the network even more headroom to make more changes.

Kỹ thuật này kết hợp việc xác nhận và lan truyền các khối.
Bây giờ, thay vì tuân theo quá trình nhận tiêu đề, xác thực nó, sau đó lấy khối tương ứng của nó, xác thực và sau đó gửi nó cho ngang hàng, bây giờ chúng tôi nhận được một tiêu đề, xác thực và gửi nó cho ngang hàng mà không cần xác thực khối.
Việc hợp lý hóa này sẽ cung cấp cho mạng nhiều hơn nữa để thực hiện nhiều thay đổi hơn.

Pipelining will significantly increase the scope/headroom we have to make further improvements to the network by reducing the block propagation overhead ('dead time').

Đường ống sẽ làm tăng đáng kể phạm vi/khoảng không, chúng tôi phải cải thiện hơn nữa cho mạng bằng cách giảm chi phí lan truyền khối ('thời gian chết').

## **Looking ahead**

## ** Nhìn về phía trước **

The Cardano project has always been committed to building out a secure, resilient and highly decentralized network that can meet the needs of the next decade and beyond. And taking a methodical, responsible long-term approach is central to this. As the saying goes, “Measure twice, cut once.”

Dự án Cardano luôn cam kết xây dựng một mạng lưới an toàn, kiên cường và phi tập trung cao, có thể đáp ứng nhu cầu của thập kỷ tới và hơn thế nữa.
Và thực hiện một cách tiếp cận dài hạn có phương pháp, có trách nhiệm là trung tâm của điều này.
Như đã nói, Biện pháp hai lần, cắt một lần.

With the launch of many exciting new projects on Cardano, the ecosystem will see explosive growth. Inevitably, short-term capacity will not always keep pace with demand and periods of heavy congestion will occur. This is a journey that every new chain goes through. But with careful monitoring throughout, we’ll continue to work to increase Cardano’s efficiency, throughput, and capability over the weeks and months ahead. While maintaining the considered, safe approach that has served us well to date.

Với sự ra mắt của nhiều dự án mới thú vị trên Cardano, hệ sinh thái sẽ chứng kiến sự phát triển bùng nổ.
Không thể tránh khỏi, năng lực ngắn hạn sẽ không luôn luôn theo kịp nhu cầu và thời gian tắc nghẽn nặng sẽ xảy ra.
Đây là một hành trình mà mọi chuỗi mới trải qua.
Nhưng với sự giám sát cẩn thận trong suốt, chúng tôi sẽ tiếp tục làm việc để tăng hiệu quả, thông lượng và khả năng của Cardano, trong các tuần và tháng tới.
Trong khi duy trì cách tiếp cận được xem xét, an toàn đã phục vụ chúng tôi tốt cho đến nay.

##### **Fernando Sanchez contributed to this article.**

#### ** Fernando Sanchez đã đóng góp cho bài viết này. **

