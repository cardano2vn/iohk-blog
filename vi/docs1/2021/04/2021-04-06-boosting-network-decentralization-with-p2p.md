# Tăng cường mạng lưới phi tập trung với P2P

### **Giao tiếp ngang hàng giữa các stake pool sẽ làm cho Cardano năng động hơn và hiệu quả hơn khi mạng lưới phát triển**

![](img/2021-04-06-boosting-network-decentralization-with-p2p.002.png) Ngày 6 tháng 4 năm 2021![](img/2021-04-06-boosting-network-decentralization-with-p2p.002.png)[ Olga Hryniuk](tmp//en/blog/authors/olga-hryniuk/page-1/)![](img/2021-04-06-boosting-network-decentralization-with-p2p.003.png) bài đọc 7 phút

![Olga Hryniuk](img/2021-04-06-boosting-network-decentralization-with-p2p.004.png)[](tmp//en/blog/authors/olga-hryniuk/page-1/)

### [**Olga Hryniuk**](tmp//en/blog/authors/olga-hryniuk/page-1/)

Technical Writer

Marketing &amp; Communications

- ![](img/2021-04-06-boosting-network-decentralization-with-p2p.005.png)[](https://www.linkedin.com/in/olga-hryniuk-1094a3160/ "LinkedIn")
- ![](img/2021-04-06-boosting-network-decentralization-with-p2p.006.png)[](https://github.com/olgahryniuk "GitHub")

![Tăng cường mạng lưới phi tập trung với P2P](img/2021-04-06-boosting-network-decentralization-with-p2p.007.jpeg)

The decentralization of Cardano puts responsibility for running the blockchain in the hands of stake pools. An essential element in this is reliable and effective connections between all the distributed nodes, and ensuring that the network is resilient to failure.

Với phiên bản Byron đơn giản hơn của blockchain, các node liên kết (OBFT) được kiểm soát bởi Cardano Foundation, Emurgo và IOHK chịu trách nhiệm hoàn toàn về việc quản lý sản xuất block và kết nối mạng lưới. Điều này duy trì mạng lưới, đồng thời xây dựng một hệ thống gồm hàng nghìn node phân tán, được vận hành bởi các stake pool. Để đạt được sự phi tập trung, Cardano hiện đã dừng các node liên kết đã hỗ trợ hệ thống kể từ khi được tạo ra vào năm 2017.

On December 6, 2020, we set the [*k* parameter to 500](https://iohk.io/en/blog/posts/2020/11/05/parameters-and-decentralization-the-way-ahead/) to expand the number of â€˜viableâ€™ pools and further promote decentralization. We have also [gradually reduced *d*](https://iohk.io/en/blog/posts/2021/03/04/not-long-till-d-0-day/) to put the power of block production entirely into the hands of the community. 100% of blocks are now being produced by the stake pool operator (SPO) community, which means that block production in Cardano is completely decentralized. These parameter changes support long-term chain sustainability and encourage the spreading of stake and potential rewards more evenly among stake pools.

Chỉ trong hơn sáu tháng, chúng tôi đã phát triển từ một hệ thống dựa trên một số ít các node được liên kết, thành một hệ thống proof of stake do cộng đồng điều hành, với hàng nghìn block được tạo ra mỗi epoch bởi hơn 2.000 stake pool

## **Mạng lưới**

Mạng lưới layer của Cardano là một cơ sở hạ tầng vật lý kết hợp các node và sự tương tác của chúng tạo thành một hệ thống thống nhất. Mạng lưới phân phối thông tin về các giao dịch và tạo block giữa tất cả các node đang hoạt động. Bằng cách này, hệ thống xác nhận và thêm các block vào chuỗi và xác minh các giao dịch. Do đó, một mạng lưới phân tán gồm các node phải giữ cho độ trễ giao tiếp ở mức tối thiểu và đủ khả năng phục hồi để đối phó với sự cố, hạn chế về dung lượng hoặc tin tặc.

Theo hệ thống liên kết cũ, các node được kết nối bằng cấu hình tĩnh được xác định trong tệp cấu trúc liên kết. Kể từ khi Shelley ra đời, hệ thống đã hoạt động ở chế độ kết hợp, nơi các node kết nối với các relay liên hợp và với các relay khác của SPO. Kết nối này được xây dựng một phần theo cách thủ công, tuy nhiên, các SPO có thể trao đổi thông tin block và giao dịch mà không cần dựa vào các node liên kết.

Trong bài viết ['Cardano’s path to decentralization'](https://iohk.io/en/blog/posts/2020/07/09/cardanos-path-to-decentralization-by-marcin-szamotulski/), Marcin Szamotulski đã thảo luận về thiết kế của mạng lưới và giải thích cách tiếp cận của Cardano đối với mạng lưới phi tập trung cùng với sự ra đời của Shelley. Giờ đây, chúng tôi đã đạt được sự phi tập trung hoàn toàn về mặt sản xuất block, điều cần thiết là kết nối mạng cũng được phi tập trung. Cardano sẽ đạt được điều này thông qua sự chuyển đổi sang kết nối ngang hàng (P2P).

## **Mạng P2P**

Tại thời điểm này, chúng ta nên nói về ‘stack’ mạng lưới, một bộ công cụ phần mềm được đội ngũ kỹ sư của chúng tôi cải tiến gần đây để đối phó với một mạng lưới lớn hơn, năng động hơn và phức tạp hơn.

Giao tiếp P2P sẽ tăng cường luồng thông tin giữa các node, do đó làm giảm (và cuối cùng là loại bỏ) sự phụ thuộc của mạng lưới vào các node được liên kết và cho phép phi tập trung Cardano. Để đạt được khả năng phục hồi mong muốn, đội ngũ của IOHK đã bận rộn cải thiện hệ thống mạng lưới với các khả năng P2P nâng cao. Những cải tiến này không yêu cầu thay đổi giao thức mà cho phép lựa chọn và giao tiếp ngang hàng tự động.

Mạng P2P được bật do sử dụng các thành phần sau:

![Kiến trúc mạng P2P](img/2021-04-06-boosting-network-decentralization-with-p2p.008.jpeg)

Hình 1. Kiến trúc mạng P2P

Chúng ta hãy xem xét kỹ hơn quá trình thiết lập các kết nối node và xem những phát triển mới nhất hợp lý hóa việc trao đổi dữ liệu giữa các node như thế nào.

**Mini protocols**

Một tập hợp các giao thức mini cho phép giao tiếp giữa các node. Mỗi giao thức thực hiện một yêu cầu trao đổi thông tin cơ bản, chẳng hạn như thông báo ngang hàng về block mới nhất, block chia sẻ hoặc xử lý các giao dịch. *Chain-sync*, *block-fetch* và các giao thức *tx-submission* đã được sử dụng để phân phối chuỗi block và các giao dịch giữa node với node trong mạng lưới:

- *Block-fetch* lấy thông tin từ cơ sở dữ liệu chuỗi.
- *Chain-sync* đồng bộ hóa dữ liệu đã tìm nạp trên mạng lưới.
- *Tx-submission2* sử dụng các giao dịch từ các mempools ngang hàng và thêm chúng vào mempool cục bộ, cho phép gửi các giao dịch ngang hàng đến node. Đây là một sửa đổi của giao thức *tx-submission*.

Các giao thức mini này hỗ trợ giao thức đồng thuận Ouroboros. Để đảm bảo tối ưu dịch vụ mạng lưới, đội ngũ đã triển khai các giao thức bổ sung:

- *keep-alive*: this ensures continuous connection between nodes and minimizes performance faults.
- *tip-sample*: this provides information about which peers offer better connectivity in terms of performance.

Bạn có thể tìm hiểu thêm về kiến ​​trúc mạng lưới và các ví dụ về giao thức mini trên [trang web tài liệu Cardano](https://docs.cardano.org/en/latest/explore-cardano/cardano-network.html).

**Quản lý kết nối**

Dịch vụ mạng hỗ trợ Linux, Windows và macOS, nhưng số lượng kết nối được hỗ trợ bởi mỗi hệ điều hành khác nhau.

Để tránh quá tải hệ thống, [bộ ghép kênh](https://docs.cardano.org/en/latest/explore-cardano/cardano-architecture-overview/connection-management.html#multiplexing) kết hợp nhiều kênh thành một kênh kết nối Transmission Control Protocol  (TCP) duy nhất. Điều này mang lại hai lợi thế: Một, giao tiếp hai chiều ngang hàng (vì vậy bất kỳ đồng đẳng nào cũng có thể bắt đầu giao tiếp mà không có hạn chế vì cả hai bên đều có quyền đọc và ghi trong cùng một kênh) và giao tiếp giữa các node với nhau được nâng cao mà không ảnh hưởng đến hiệu suất.

The networking team has implemented a bidirectional-aware â€˜connection managerâ€™ that integrates with the P2P governor, which is currently undergoing final testing before deployment. Additionally, the multiplexerâ€™s API has been upgraded to monitor new connections and protocols. This enhancement introduces more efficient connection management and improved issue tracking.

**Chức năng quản trị P2P**

Mạng lưới Cardano liên quan đến nhiều node ngang hàng. Một số hoạt động tích cực hơn những số khác, một số đã thiết lập kết nối và một số cần được thúc đẩy để đảm bảo hệ thống hoạt động tốt nhất. Như đã thảo luận trong ['Cardano’s path to decentralization'](https://iohk.io/en/blog/posts/2020/07/09/cardanos-path-to-decentralization-by-marcin-szamotulski/), mạng ngang hàng được chia thành ba loại:

- cold peers
- warm peers
- hot peers

Để thiết lập kết nối hai chiều giữa chúng, điều quan trọng là chúng ta phải biết kết nối nào đang hoạt động.

![Khám phá ngang hàng trên Cardano](img/2021-04-06-boosting-network-decentralization-with-p2p.008.jpeg)

Hình 2. Khám phá ngang hàng trên Cardano

The [P2P governor](https://input-output-hk.github.io/ouroboros-network/ouroboros-network/Ouroboros-Network-PeerSelection-Governor.html) manages connections and provides information on which peers are active and performing well. This feature promotes peer connections for enhanced system performance and also provides excellent visibility by building and maintaining a connectivity map of the entire network. The governor will simplify the process of connection definitions by handling these automatically so a few central stake pools no longer have to configure them manually. The governor promotes or demotes peers between cold, warm, and hot states, and also interacts with the connection manager to open new connections or reuse existing ones.

## **Lộ trình triển khai P2P**

Đội ngũ mạng lưới IOHK đang trong giai đoạn cuối cùng của quá trình kiểm tra chất lượng tích hợp quản trị P2P với node. Sau đó, pool sẽ mở rộng stack  mạng lưới với nhiều giao thức hơn - đặc biệt, sẽ cung cấp trao đổi dữ liệu liền mạch giữa các kết nối ngang hàng và giúp xây dựng bản đồ giao tiếp phi tập trung.

These technical upgrades allow us to simplify Cardano node interfaces and improve the systemâ€™s configuration. When testing is finalized, all SPOs will be able to update and simplify their configuration preferences for enhanced connectivity.

Điều này liên quan đến các giai đoạn sau đây trước khi triển khai P2P đầy đủ:

![Lộ trình triển khai P2P](img/2021-04-06-boosting-network-decentralization-with-p2p.008.jpeg)

Hình 3. Lộ trình triển khai P2P

Để có hướng dẫn chi tiết từ kiến ​​trúc sư trưởng Duncan Coutts, hãy xem video này từ [buổi trình diễn Cardano360 tháng 3](https://youtu.be/mXYIQDUitYI).

*Mặc dù quản trị đóng một vai trò quan trọng trong việc thiết lập, duy trì và hỗ trợ mạng lưới, nhưng chỉ với sự phi tập trung, chúng ta mới có thể đạt được sự bền vững thực sự của mạng lưới để đảm bảo cơ hội bình đẳng cho tất cả các stake pool. Do đó, mục tiêu của cải tiến stack là cho phép tất cả các stake pool chạy cùng một cấu hình, thiết lập các khả năng bình đẳng trong một môi trường phi tập trung.*

*Weâ€™ll keep providing more development updates in this blog, and you can also follow Cardano [status updates](https://roadmap.cardano.org/en/status-updates/) to learn about recent improvements and developments.*
