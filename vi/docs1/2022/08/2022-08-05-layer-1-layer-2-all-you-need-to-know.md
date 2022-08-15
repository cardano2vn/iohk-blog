# Lớp 1 &amp; Lớp 2: tất cả những gì bạn cần biết

### **When discussing blockchain architecture, the terms 'layer 1' and 'layer 2' are frequently mentioned. These are important concepts that serve two purposes: explain how a blockchain network is built, and provide an easy-to-understand visual representation of what a blockchain network looks like. Let's break these ideas down**

![](img/2022-08-05-layer-1-layer-2-all-you-need-to-know.002.png) 5 tháng 8 năm 2022![](img/2022-08-05-layer-1-layer-2-all-you-need-to-know.002.png) [Fernando Sanchez](/en/blog/authors/fernando-sanchez/page-1/)![](img/2022-08-05-layer-1-layer-2-all-you-need-to-know.003.png) 13 phút đọc

![Fernando Sanchez](img/2022-08-05-layer-1-layer-2-all-you-need-to-know.004.png)[](/en/blog/authors/fernando-sanchez/page-1/)

### [**Fernando Sanchez**](/en/blog/authors/fernando-sanchez/page-1/)

Người viết kỹ thuật

Tiếp thị và Truyền thông

- ![](img/2022-08-05-layer-1-layer-2-all-you-need-to-know.005.png)[](mailto:fernando.sanchez@iohk.io "E-mail")
- ![](img/2022-08-05-layer-1-layer-2-all-you-need-to-know.006.png)[](https://www.linkedin.com/in/linkedinsanchezf/ "LinkedIn")

![Lớp 1 & Lớp 2: tất cả những gì bạn cần biết](img/2022-08-05-layer-1-layer-2-all-you-need-to-know.007.jpeg)

Lớp 1: định nghĩa

Imagine a wedding cake, with different tiers -layers, if you will-, and the figurine of a couple on top. That beautiful cake rests on a solid stand, the base. For all intents and purposes, that robust and solid cake stand is the first layer (layer 1) that supports the cake infrastructure. You can probably see where this is going. In a blockchain, layer 1 is the base network upon which rest layer 2 solutions.

![](img/2022-08-05-layer-1-layer-2-all-you-need-to-know.008.jpeg)

## **Lớp 1: chức năng**

Với sơ đồ trực quan này, Cardano là lớp 1 (mạng cơ sở), bản thân nó bao gồm ba lớp độc lập:

- Lớp mạng
- Lớp đồng thuận
- Lớp sổ cái

**Lớp mạng**

Lớp này duy trì các kết nối giữa tất cả các nút phân tán trong mạng Cardano, nhận các khối mới từ mạng khi chúng được tạo ra bởi các nút tạo khối, xây dựng các giao dịch mới được đúc thành khối và truyền khối giữa các nút.

**Lớp đồng thuận**

Lớp này thực hiện hai chức năng cơ bản:

- Chạy giao thức đồng thuận [Ouroboros](https://www.essentialcardano.io/glossary/ouroboros) . Lớp này đưa ra các quyết định như áp dụng các khối, lựa chọn giữa các chuỗi cạnh tranh (nếu có) và quyết định khi nào sản xuất các khối của riêng nó; và
- Duy trì tất cả trạng thái cần thiết để đưa ra các quyết định được thực hiện trong lớp đồng thuận.

**Lớp sổ cái**

Lớp này chỉ định:

- Trạng thái của sổ cái trông như thế nào; và
- Sổ cái phải được cập nhật như thế nào cho mỗi khối mới.

Lớp sổ cái chỉ bao gồm các chức năng thuần túy chỉ định sự chuyển đổi giữa các trạng thái sổ cái kế tiếp, như bắt nguồn từ các quy tắc sổ cái chính thức, bằng cách sử dụng mô hình kế toán UTxO mở rộng (EUTxO). Các chuyển đổi trạng thái được thúc đẩy bởi tập hợp các giao dịch được chứa trong các khối Cardano và bởi các sự kiện lớn như chuyển đổi ranh giới kỷ nguyên.

Lớp đồng thuận không cần biết bản chất chính xác của trạng thái sổ cái, cũng như nội dung của các khối, ngoài một số trường tiêu đề cần thiết để chạy giao thức đồng thuận.

Nhìn chung, ba lớp này tạo thành giải pháp lớp 1 là Cardano.

## **Lớp 1: khả năng mở rộng**

Look at that wedding cake again. It's big, isn't it, with all those tiers stacked on top of one another. But look at the base, the cake stand. That first layer has certain dimensions and cannot be any bigger. Equally, it needs to be big enough to support the tiers that sit above it. The stuff that rests on it can only be of a certain size, and this is exactly the reason why wedding cakes have multiple tiers. Every tier (think layer) adds something to the base. A new filling, frosting, decoration, etc. In other words, every tier scales the base layer up.

Các mạng công cộng phi tập trung cũng gặp phải vấn đề tương tự. Cũng giống như một đế bánh chỉ có thể chứa được một lượng lát bánh hữu hạn, phần đế (lớp 1) chỉ có thể xử lý một lượng giao dịch nhất định. Nếu bạn cố gắng thêm nhiều lát hơn số lượng bánh đứng, chúng sẽ bắt đầu rơi ra khỏi mép và sự lộn xộn sẽ phá hỏng ngày trọng đại của ai đó. Tương tự, các nút trong mạng lớp 1 chỉ có thể xử lý rất nhiều giao dịch trước khi xảy ra tắc nghẽn. Khi cơ sở người dùng phát triển, nhu cầu về nhiều nút hơn để xử lý giao dịch cũng vậy. Để giải quyết vấn đề này, mạng cần phải mở rộng quy mô, nếu không, các giao dịch sẽ bắt đầu tụt dốc, có thể nói như vậy.

Có nhiều cách để mở rộng quy mô mạng lớp 1. Ví dụ: tăng kích thước khối để các khối mang nhiều dữ liệu giao dịch hơn. Kích thước khối gần đây đã tăng 8KB lên 72KB (tăng 12,5%). Đây là một trong những cách Cardano sẽ mở rộng quy mô vào năm 2022.

Returning to our wedding cake visual, adding tiers not only makes the cake bigger, it also introduces a very useful feature: the ability to make every tier different to the base. We can add different flavors, fillings, designs, and so on, independently of the first layer. To cater for different â€˜guestsâ€™ and different preferences. In blockchain, adding a new layer (layer 2) not only allows the layer 1 to scale, it also enables transactions and processes to happen independently of the main chain (layer 1).

### **Các giải pháp khả năng mở rộng lớp 1 trong Cardano**

Cardano hiện đang trong giai đoạn phát triển Basho, tất cả là về mở rộng quy mô và tối ưu hóa. Trong khi mạng hiện đang quản lý nhu cầu rất hiệu quả, hệ sinh thái ứng dụng phi tập trung (DApp) đang phát triển nhanh chóng và sẽ tiếp tục đặt ra nhu cầu ngày càng tăng đối với hệ thống. Để giải quyết vấn đề này, nhiều phương pháp khả năng mở rộng (bao gồm các giải pháp lớp 1 và lớp 2) đang được triển khai cho Cardano cho hàng trăm nghìn người đầu tiên, sau đó là hàng triệu người dùng mới.

**Tăng kích thước khối**

Khối càng lớn thì càng có nhiều giao dịch. Khối đầu tiên được đúc trên Cardano có kích thước 665 byte (0,665KB). Ngày nay, các khối có kích thước 72KB. Đó là mức tăng hơn 10.000%! Các mức tăng thêm sẽ được áp dụng theo thời gian dựa trên việc giám sát hệ thống liên tục và tình trạng mạng tổng thể.

**Pipelining**

Improves block propagation times by coalescing validation and propagation. The goal is for blocks to be propagated to at least 95% of peers within five seconds by reducing the â€˜dead timeâ€™ between blocks (the block propagation overhead). This provides the headroom to make more aggressive scaling changes, such as increasing block size/increasing Plutus parameter limits.

**Người xác nhận đầu vào**

Xa hơn nữa, người xác nhận đầu vào sẽ cải thiện thời gian và thông lượng truyền khối bằng cách cho phép các giao dịch được tách thành các khối được xây dựng trước. Điều này cải thiện tính nhất quán của thời gian truyền khối và cho phép tỷ lệ giao dịch cao hơn.

**Thông số bộ nhớ / CPU cho Plutus**

Sử dụng bộ nhớ hiệu quả hơn trên toàn bộ chuỗi. Cụ thể, có những cải tiến về bộ nhớ trong việc xử lý Đầu ra giao dịch chưa gửi (UTXO), phân phối cổ phần, phân phối cổ phần trực tiếp và các nhóm, và biểu diễn hàm băm.

**Cải tiến tập lệnh Plutus**

Sử dụng hiệu quả hơn nữa mô hình EUTxO mạnh mẽ thông qua tối ưu hóa hợp đồng thông minh, bao gồm:

- Đầu vào tham chiếu (CIP-0031) - Các tập lệnh Plutus có thể kiểm tra các đầu vào giao dịch mà không cần sử dụng chúng. Điều này có nghĩa là không cần thiết phải tạo UTXO chỉ để kiểm tra thông tin do đầu vào nắm giữ.
- Plutus Datums (CIP-0032) - Các dữ liệu có thể được gắn trực tiếp vào đầu ra thay vì băm dữ liệu. Điều này đơn giản hóa cách dữ liệu được sử dụng, vì người dùng có thể thấy dữ liệu thực tế hơn là phải cung cấp dữ liệu khớp với hàm băm đã cho.
- Chia sẻ tập lệnh (CIP-0033) - Các tham chiếu tập lệnh Plutus có thể được liên kết với các đầu ra giao dịch, nghĩa là chúng có thể được ghi lại trên chuỗi để sử dụng lại sau này. Sẽ không cần thiết phải cung cấp một bản sao của tập lệnh với mỗi giao dịch, giảm đáng kể sự cọ xát cho các nhà phát triển. Việc sử dụng lại các tập lệnh trong nhiều giao dịch làm giảm đáng kể kích thước giao dịch, cải thiện thông lượng và giảm chi phí thực thi tập lệnh.

**Cải tiến nút**

Improvements to the node will help even distribution of stake and reward computations across the epochs, thus providing greater headroom for block size increases. Also, memory usage is now more efficient. Memory compaction reduces RSS footprint, and memory sharing means we need less data instantiated. Node version 1.34.1, from March 2022, reduces peak load at critical points, including the epoch boundary.

**On-disk storage**

Bằng cách lưu trữ các phần của trạng thái giao thức trên đĩa, các nút sẽ cần ít bộ nhớ hơn, có nghĩa là các hệ thống hạn chế RAM sẽ có thể chạy các nút miễn là chúng có đủ dung lượng lưu trữ và bộ nhớ sẽ không gây tắc nghẽn đối với khả năng mở rộng. Điều này sẽ cho phép tăng trưởng đáng kể trong trạng thái blockchain.

## **Interlude: bộ ba blockchain**

Khả năng mở rộng của một hệ thống phân tán - chẳng hạn như một chuỗi khối - là một vấn đề phức tạp.

There is a general consensus that a 'proper' blockchain system must have three properties: scalability, security, and decentralization. But an equally widespread belief is the so-called trilemma, which dictates that decentralized systems can only provide two of these properties, while sacrificing the third. First postulated by Ethereum creator Vitalik Buterin, the trilemma suggests that developers must always accept a compromise, or a trade-off, when designing blockchain networks. This compromise means one property must 'suffer', for the other two to be possible.

Ví dụ: mạng càng có nhiều nút thì mạng càng trở nên phi tập trung hơn, nhưng điều đó cũng có nghĩa là càng cần nhiều nút đáng tin cậy để duy trì bảo mật. Để duy trì bảo mật, các khoản phí phải được áp dụng khiến chi phí của một cuộc tấn công tiềm ẩn cao đến mức nghiêm trọng. Tuy nhiên, một mạng phải khuyến khích sự tham gia, vì vậy chi phí cho mỗi nút phải tương đối thấp. Ngoài ra, đặc điểm của tính bất biến ngụ ý rằng dữ liệu blockchain sẽ được thêm vào miễn là blockchain tồn tại, nhưng không bao giờ bị xóa, có nghĩa là blockchain sẽ tiếp tục phát triển. Mạng lớn hơn có nghĩa là cần nhiều tài nguyên tính toán hơn để duy trì hiệu suất. Hiệu suất tốt hơn cần phần cứng tốt hơn, có nghĩa là phần thưởng phải đủ để khiến khoản đầu tư trở nên đáng giá. Và như thế.

### **Vertical and horizontal scaling**

Giải quyết vấn đề nan giải này đòi hỏi một cách tiếp cận thận trọng và cân bằng, để cả ba yếu tố này luôn ở trạng thái cân bằng.

Về lý thuyết, một hệ thống blockchain sẽ tiếp tục phát triển vô thời hạn. Khi càng có nhiều nút trở thành một phần của hệ thống, thì sẽ có nhiều dữ liệu và tài sản lưu chuyển hơn, đồng thời sẽ cần xử lý nhiều giao dịch hơn. Tất cả điều này đòi hỏi sức mạnh tính toán và khả năng lưu trữ. Theo thời gian, nhu cầu sẽ tiếp tục tăng, vì vậy hệ thống cơ bản sẽ cần phải mở rộng quy mô phù hợp để ngăn chặn sự sụt giảm nghiêm trọng về hiệu suất.

Hai tùy chọn tỷ lệ tồn tại: dọc và ngang.

**Vertical scaling**

Kỹ thuật này liên quan đến việc mở rộng khả năng tính toán của các nút riêng lẻ bằng cách thêm nhiều bộ nhớ hơn và các thành phần tốt hơn. Nói cách khác, hãy nâng cấp phần cứng của mạng để đạt được hiệu suất tổng thể tốt hơn.

Ví dụ, có một mạng bao gồm các nút hiệu suất cao hỗ trợ kích thước khối lớn hơn và khuếch tán khối nhanh hơn. Nhưng nhược điểm là sự phân quyền sẽ bị hạn chế, do chi phí vận hành cao, điều này sẽ khiến các nhà khai thác nút mới phải suy nghĩ kỹ về việc tham gia và do đó hạn chế sự mở rộng của mạng. Ngoài ra, một mạng như vậy sẽ mang lại chi phí cao hơn cho các nút xác nhận.

**Horizontal scaling**

Ngược lại với tỷ lệ theo chiều dọc, tỷ lệ theo chiều ngang có thể đạt được theo hai cách. Một, đơn giản bằng cách thêm nhiều máy tính (nút) vào mạng hiện có. Lý do ở đây là, bằng cách thêm các nút bổ sung, mạng sẽ có khả năng xử lý nhiều giao dịch hơn.

Và hai, bằng cách sử dụng sidechains, sẽ loại bỏ một số tải tính toán khỏi chuỗi chính và, như một lợi thế bổ sung, cho phép tùy chỉnh dưới dạng các giao thức đồng thuận khác nhau hoặc các mô hình quản trị, ví dụ, để phù hợp với một dự án hoặc ngành cụ thể. Từ quan điểm bảo mật, các sidechains có thể tạo ra một hệ sinh thái an toàn hơn bằng cách cô lập các mối đe dọa tiềm ẩn đối với chuỗi chính. Nếu một sidechain bị xâm phạm theo bất kỳ cách nào, nguy cơ sẽ được chứa trong sidechain đó, do đó bảo vệ phần còn lại của mạng.

## **Lớp 2: giải quyết vấn đề nan giải về khả năng mở rộng**

Nói chung, các giải pháp lớp 2 giải quyết vấn đề khả năng mở rộng vốn có đối với chuỗi lớp 1. Được xây dựng trên nền tảng của một blockchain hiện có (giống như việc thêm một tầng mới vào bánh cưới), các giao thức lớp 2 thực hiện rất nhiều công việc xử lý mà nếu không sẽ xảy ra trên chuỗi chính. Điều này làm tăng thông lượng của chuỗi chính. Một phần thưởng bổ sung là, trong khi giải pháp lớp 2 thực hiện công việc khó khăn, lớp 1 vẫn giữ được tính bảo mật của nó.

### **Lớp 2: định nghĩa**

Một giao thức ngoài chuỗi bổ sung hoạt động trên lớp 1 của blockchain. Các bên có thể chuyển tiền một cách an toàn từ chuỗi khối sang một giao thức ngoài chuỗi, giải quyết các giao dịch trong giao thức này một cách độc lập với chuỗi cơ sở và chuyển tiền một cách an toàn trở lại chuỗi cơ sở nếu cần. Các giao thức lớp 2 cải thiện thông lượng tổng thể và khả năng mở rộng vì chúng làm giảm tắc nghẽn mạng.

### **Các giải pháp khả năng mở rộng lớp 2 trong Cardano**

**Sidechains**

A sidechain, defined as a way to enable multiple blockchains to communicate with each other and have one react to events in the other, is a separate blockchain connected to a main blockchain (the 'main' chain, also known as parent chain), through a two-way mechanism (the 'bridge') that enables tokens and other digital assets from one chain to be used in another and results returned to the original chain. Assets can be moved between chains as needed. One single parent chain can have multiple interoperable sidechains connected to it, which may operate in completely different ways. EVM sidechains on Cardano include [dcSparkâ€™s Milkomeda](https://www.milkomeda.com/) and IOGâ€™s [EVM sidechain project.](https://iohk.io/en/blog/posts/2022/07/06/introducing-the-cardano-evm-sidechain/)

**Hydra**

Hydra là giải pháp khả năng mở rộng lớp 2 cho Cardano, nhằm mục đích tăng tốc độ giao dịch thông qua độ trễ thấp, thông lượng cao và giảm thiểu chi phí giao dịch.

[Hydra Head](https://hydra.family/head-protocol/) là giao thức đầu tiên của dòng Hydra và là nền tảng cho các kịch bản triển khai nâng cao hơn dựa trên các kênh nhà nước đa bên, đẳng hình. Bằng cách cung cấp các phương tiện xử lý giao dịch ngoài chuỗi hiệu quả hơn cho một nhóm người dùng, đồng thời sử dụng sổ cái chuỗi chính làm lớp thanh toán an toàn, Hydra Head giữ các đảm bảo an ninh trong khi vẫn được liên kết lỏng lẻo với chuỗi chính. Không đòi hỏi sự đồng thuận toàn cầu, nó có thể thích ứng với nhiều loại ứng dụng. Ngoài ra, Hydra Head cho phép phí Tx, ngân sách thực thi tập lệnh và các thông số giao thức khác được định cấu hình ở mức thấp hoặc cao tùy theo trường hợp sử dụng. Ví dụ, điều này rất quan trọng để kích hoạt các giao dịch vi mô.

Hơn nữa, Hydra Head đưa ra [khái niệm về các kênh trạng thái đẳng cấu](https://eprint.iacr.org/2020/299.pdf) : nghĩa là sử dụng lại cùng một biểu diễn sổ cái để mang lại các anh chị em sổ cái đồng nhất, ngoài chuỗi, mà chúng tôi gọi là Heads (do đó có tên Hydra). Đặc biệt đối với Cardano, điều này có nghĩa là tài sản gốc, mã thông báo không thể thay thế (NFT) và tập lệnh Plutus có sẵn bên trong mỗi Hydra Head. Isomorphism cho phép một phần mở rộng tự nhiên của hệ thống, chứ không phải là một phần mở rộng.

Hydra Heads xuất sắc trong việc đạt được kết quả gần như tức thì trong một Head. Quá trình thiết lập và đóng Head có thể mất một vài khối, nhưng sau khi được thiết lập, các giao dịch có thể diễn ra nhanh chóng giữa những người tham gia hợp tác. Vì Hydra Heads là đồng phân hình và cũng sử dụng mô hình EUTXO, nên chúng có thể xử lý đồng thời các giao dịch không xung đột, điều này "cùng với mạng tốt" cho phép sử dụng tối ưu các tài nguyên có sẵn.

### **Các giải pháp khả năng mở rộng khác**

**Điện toán ngoài chuỗi**

Giảm tải một số tính toán, ví dụ như với Thực thi hợp đồng không đồng bộ (ACE), có thể thúc đẩy hiệu quả mạng lõi cao hơn. Các giao dịch xảy ra bên ngoài chính blockchain, nhưng có thể cung cấp các giao dịch nhanh chóng, giá rẻ thông qua mô hình ủy thác.

**Mithril**

Để đạt được khả năng mở rộng lớn hơn, cần phải giải quyết sự phức tạp của các hoạt động quan trọng phụ thuộc lôgarit vào số lượng người tham gia. [Mithril](https://iohk.io/en/blog/posts/2021/10/29/mithril-a-stronger-and-lighter-blockchain-for-better-efficiency/) là một giao thức do IOG phát triển, hoạt động như một sơ đồ chữ ký ngưỡng dựa trên cổ phần cho phép tận dụng cổ phần minh bạch, an toàn và nhẹ. Mithril sẽ cải thiện đồng bộ hóa chuỗi trong khi duy trì sự tin cậy. Kết quả là tổng hợp đa chữ ký nhanh chóng và hiệu quả mà không ảnh hưởng đến các tính năng bảo mật.

## **Conclusion**

Một mạng lưới blockchain hoạt động theo những cách bí ẩn và một số khái niệm xung quanh hệ sinh thái sổ cái phi tập trung có thể khó hiểu.

Không phải như vậy lớp 1 và lớp 2, nếu bạn sử dụng hình ảnh lớp bánh được trình bày ở đây.

- Layer 1 (the cake stand) = the robust and secure base network upon which rest layer 2 solutions
- Lớp 2 (các tầng bánh) = các giải pháp được xây dựng trên nền tảng để giải quyết các vấn đề về khả năng mở rộng vốn có

Đây là cách đơn giản nhất để hình dung và hiểu lớp 1 và lớp 2 là gì.

## **Những điều quan trọng**

- Cardano là lớp 1 (mạng cơ sở)
- Giải pháp lớp 2 là một cấu trúc được xây dựng trên đầu chuỗi lớp 1 để giải quyết các vấn đề về khả năng mở rộng và tốc độ giao dịch sau này. Lightning Network của Bitcoin là một ví dụ về giải pháp lớp 2, cũng như Hydra cho Cardano
- Có hai tùy chọn chia tỷ lệ: dọc và ngang
- Mở rộng quy mô dọc liên quan đến việc mở rộng khả năng tính toán của các nút riêng lẻ bằng cách thêm nhiều bộ nhớ hơn và các thành phần tốt hơn.
- Quy mô theo chiều ngang có thể đạt được theo hai cách. Một, đơn giản bằng cách thêm nhiều máy tính (nút) vào mạng hiện có và hai, bằng cách sử dụng sidechains, sẽ loại bỏ một số tải tính toán khỏi chuỗi chính.
- Cardano sẽ thấy một loạt các phương pháp khả năng mở rộng được triển khai trong suốt 2022/2023
