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

Sự phi tập trung của Cardano đặt trách nhiệm vận hành blockchain vào các stake pool. Một yếu tố thiết yếu trong việc này là các kết nối đáng tin cậy và hiệu quả giữa tất cả các node phân tán và đảm bảo rằng mạng lưới có khả năng phục hồi sau sự cố.

Với phiên bản Byron đơn giản hơn của blockchain, các node liên kết (OBFT) được kiểm soát bởi Cardano Foundation, Emurgo và IOHK chịu trách nhiệm hoàn toàn về việc quản lý sản xuất block và kết nối mạng lưới. Điều này duy trì mạng lưới, đồng thời xây dựng một hệ thống gồm hàng nghìn node phân tán, được vận hành bởi các stake pool. Để đạt được sự phi tập trung, Cardano hiện đã dừng các node liên kết đã hỗ trợ hệ thống kể từ khi được tạo ra vào năm 2017.

Vào ngày 6 tháng 12 năm 2020, chúng tôi thiết lập [ *thông số k thành 500*](https://iohk.io/en/blog/posts/2020/11/05/parameters-and-decentralization-the-way-ahead/)  để mở rộng số lượng pool 'khả thi' và thúc đẩy phi tập trung hơn nữa. Chúng tôi cũng đã [giảm dần tham số *d*](https://iohk.io/en/blog/posts/2021/03/04/not-long-till-d-0-day/) để đưa hoàn toàn sức mạnh sản xuất block vào tay cộng đồng. 100% block hiện đang được sản xuất bởi cộng đồng nhà điều hành stake pool (SPO), có nghĩa là việc sản xuất block trong Cardano hoàn toàn phi tập trung. Những thay đổi thông số này hỗ trợ tính bền vững của chuỗi trong dài hạn và khuyến khích việc chia sẻ cổ phần và phần thưởng tiềm năng đồng đều hơn giữa các stake pool.

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

**Giao thức mini**

Một tập hợp các giao thức mini cho phép giao tiếp giữa các node. Mỗi giao thức thực hiện một yêu cầu trao đổi thông tin cơ bản, chẳng hạn như thông báo ngang hàng về block mới nhất, block chia sẻ hoặc xử lý các giao dịch. *Chain-sync*, *block-fetch* và các giao thức *tx-submission* đã được sử dụng để phân phối chuỗi block và các giao dịch giữa node với node trong mạng lưới:

- *Block-fetch* lấy thông tin từ cơ sở dữ liệu chuỗi.
- *Chain-sync* đồng bộ hóa dữ liệu đã tìm nạp trên mạng lưới.
- *Tx-submission2* sử dụng các giao dịch từ các mempools ngang hàng và thêm chúng vào mempool cục bộ, cho phép gửi các giao dịch ngang hàng đến node. Đây là một sửa đổi của giao thức *tx-submission*.

Các giao thức mini này hỗ trợ giao thức đồng thuận Ouroboros. Để đảm bảo tối ưu dịch vụ mạng lưới, đội ngũ đã triển khai các giao thức bổ sung:

- *Keep-alive*: đảm bảo kết nối liên tục giữa các node và giảm thiểu lỗi hiệu suất.
- *Tip-sample*: cung cấp thông tin về việc cặp kết nối ngang hàng nào cung cấp kết nối tốt hơn về mặt hiệu suất.

Bạn có thể tìm hiểu thêm về kiến ​​trúc mạng lưới và các ví dụ về giao thức mini trên [trang web tài liệu Cardano](https://docs.cardano.org/en/latest/explore-cardano/cardano-network.html).

**Quản lý kết nối**

Dịch vụ mạng hỗ trợ Linux, Windows và macOS, nhưng số lượng kết nối được hỗ trợ bởi mỗi hệ điều hành khác nhau.

Để tránh quá tải hệ thống, [bộ ghép kênh](https://docs.cardano.org/en/latest/explore-cardano/cardano-architecture-overview/connection-management.html#multiplexing) kết hợp nhiều kênh thành một kênh kết nối Transmission Control Protocol  (TCP) duy nhất. Điều này mang lại hai lợi thế: Một, giao tiếp hai chiều ngang hàng (vì vậy bất kỳ đồng đẳng nào cũng có thể bắt đầu giao tiếp mà không có hạn chế vì cả hai bên đều có quyền đọc và ghi trong cùng một kênh) và giao tiếp giữa các node với nhau được nâng cao mà không ảnh hưởng đến hiệu suất.

Đội ngũ phụ trách vấn đề mạng lưới đã triển khai một 'trình quản lý kết nối' nhận biết hai chiều tích hợp với trình quản lý P2P, hiện đang trải qua thử nghiệm cuối cùng trước khi triển khai. Ngoài ra, API của bộ ghép kênh đã được nâng cấp để giám sát các kết nối và giao thức mới. Cải tiến này giới thiệu quản lý kết nối hiệu quả hơn và cải tiến theo dõi sự cố.

**Chức năng quản trị P2P**

Mạng lưới Cardano liên quan đến nhiều node ngang hàng. Một số hoạt động tích cực hơn những số khác, một số đã thiết lập kết nối và một số cần được thúc đẩy để đảm bảo hệ thống hoạt động tốt nhất. Như đã thảo luận trong ['Cardano’s path to decentralization'](https://iohk.io/en/blog/posts/2020/07/09/cardanos-path-to-decentralization-by-marcin-szamotulski/), mạng ngang hàng được chia thành ba loại:

- cold peers
- warm peers
- hot peers

Để thiết lập kết nối hai chiều giữa chúng, điều quan trọng là chúng ta phải biết kết nối nào đang hoạt động.

![Khám phá ngang hàng trên Cardano](img/2021-04-06-boosting-network-decentralization-with-p2p.008.jpeg)

Hình 2. Khám phá ngang hàng trên Cardano

[Quản trị P2P](https://input-output-hk.github.io/ouroboros-network/ouroboros-network/Ouroboros-Network-PeerSelection-Governor.html) quản lý các kết nối và cung cấp thông tin về những kết nối ngang hàng nào đang hoạt động và hoạt động tốt. Tính năng này thúc đẩy các kết nối ngang hàng để nâng cao hiệu suất hệ thống và cũng cung cấp khả năng hiển thị tuyệt vời bằng cách xây dựng và duy trì bản đồ kết nối của toàn bộ mạng lưới. Quản trị sẽ đơn giản hóa quá trình định nghĩa kết nối bằng cách xử lý chúng tự động để một số stake pool trung tâm không còn phải cấu hình chúng theo cách thủ công. Quản trị thúc đẩy hoặc hạ cấp các kết nối ngang hàng giữa các trạng thái lạnh, ấm, nóng đồng thời tương tác với người quản lý kết nối để mở các kết nối mới hoặc sử dụng lại các kết nối hiện có.

## **Lộ trình triển khai P2P**

Đội ngũ mạng lưới IOHK đang trong giai đoạn cuối cùng của quá trình kiểm tra chất lượng tích hợp quản trị P2P với node. Sau đó, pool sẽ mở rộng stack  mạng lưới với nhiều giao thức hơn - đặc biệt, sẽ cung cấp trao đổi dữ liệu liền mạch giữa các kết nối ngang hàng và giúp xây dựng bản đồ giao tiếp phi tập trung.

Những nâng cấp kỹ thuật này cho phép chúng tôi đơn giản hóa các giao diện node của Cardano và cải thiện cấu hình của hệ thống. Khi quá trình thử nghiệm được hoàn tất, tất cả SPO sẽ có thể cập nhật và đơn giản hóa các tùy chọn cấu hình của họ để tăng cường kết nối.

Điều này liên quan đến các giai đoạn sau đây trước khi triển khai P2P đầy đủ:

![Lộ trình triển khai P2P](img/2021-04-06-boosting-network-decentralization-with-p2p.008.jpeg)

Hình 3. Lộ trình triển khai P2P

Để có hướng dẫn chi tiết từ kiến ​​trúc sư trưởng Duncan Coutts, hãy xem video này từ [buổi trình diễn Cardano360 tháng 3](https://youtu.be/mXYIQDUitYI).

*Mặc dù quản trị đóng một vai trò quan trọng trong việc thiết lập, duy trì và hỗ trợ mạng lưới, nhưng chỉ với sự phi tập trung, chúng ta mới có thể đạt được sự bền vững thực sự của mạng lưới để đảm bảo cơ hội bình đẳng cho tất cả các stake pool. Do đó, mục tiêu của cải tiến stack là cho phép tất cả các stake pool chạy cùng một cấu hình, thiết lập các khả năng bình đẳng trong một môi trường phi tập trung.*

*Chúng tôi sẽ tiếp tục cung cấp thêm các bản cập nhật phát triển trong bài blog này và bạn cũng có thể theo dõi [cập nhật về các status](https://roadmap.cardano.org/en/status-updates/) của Cardano để tìm hiểu về các cải tiến và phát triển gần đây.<br><br><br><br>Bài này được dịch bởi Lê Nguyên, soát xét bởi Brit Nguyễn. <a>với bài gốc</a><br><em>Dự án này được tài trợ bởi Catalyst</em><br>https://iohk.io/en/blog/posts/2021/04/06/boosting-network-decentralization-with-p2p/*
