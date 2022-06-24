# Introducing our new peer-to-peer (P2P) testnet
### **We are working with a small group of stake pool operators on a new P2P testnet to further drive network decentralization**
![](img/2021-12-08-introducing-our-new-peer-to-peer-p2p-testnet.002.png) 8 December 2021![](img/2021-12-08-introducing-our-new-peer-to-peer-p2p-testnet.002.png)[ Olga Hryniuk](tmp//en/blog/authors/olga-hryniuk/page-1/)![](img/2021-12-08-introducing-our-new-peer-to-peer-p2p-testnet.003.png) 3 mins read

![Olga Hryniuk](img/2021-12-08-introducing-our-new-peer-to-peer-p2p-testnet.004.png)[](tmp//en/blog/authors/olga-hryniuk/page-1/)
### [**Olga Hryniuk**](tmp//en/blog/authors/olga-hryniuk/page-1/)
Technical Writer

Marketing & Communications

- ![](img/2021-12-08-introducing-our-new-peer-to-peer-p2p-testnet.005.png)[](https://www.linkedin.com/in/olga-hryniuk-1094a3160/ "LinkedIn")
- ![](img/2021-12-08-introducing-our-new-peer-to-peer-p2p-testnet.006.png)[](https://github.com/olgahryniuk "GitHub")

![Introducing our new peer-to-peer (P2P) testnet ](img/2021-12-08-introducing-our-new-peer-to-peer-p2p-testnet.007.png)

Cardano continues to build momentum with more features and capabilities being steadily added to the blockchain. As we recently reported, we are [optimizing the network](https://iohk.io/en/blog/posts/2021/11/10/optimizing-cardano/) to increase throughput so more transactions can be processed faster, and decentralized applications (DApps) and smart contracts created and used more efficiently. This week, we have kicked off an important new initiative to support our ongoing drive toward full decentralization with the launch of a new peer-to-peer (P2P) testnet.

Cardano tiếp tục xây dựng động lực với nhiều tính năng và khả năng được thêm vào đều đặn vào blockchain.
Như chúng tôi đã báo cáo gần đây, chúng tôi đang [tối ưu hóa mạng] (https://iohk.io/en/blog/posts/2021/11/10/optimizing-cardano/) để tăng thông lượng để có thể xử lý nhiều giao dịch nhanh hơn và có nhiều giao dịch nhanh hơn và
Các ứng dụng phi tập trung (DAPP) và hợp đồng thông minh được tạo và sử dụng hiệu quả hơn.
Tuần này, chúng tôi đã khởi động một sáng kiến mới quan trọng để hỗ trợ cho nỗ lực liên tục của chúng tôi hướng tới sự phân cấp hoàn toàn với việc ra mắt TestNet mới ngang hàng (P2P).

Cardano ensures trust and security in a decentralized setting using proof-of-stake consensus through the Ouroboros algorithm. At the heart of this are about 3,000 stake pools run by operators (SPOs) who manage the distributed nodes that power the network. Clearly, in a decentralized and distributed network, there has to be reliable communication between these nodes. Central to this and vital for verifying blockchain activities is data diffusion â€“ the process of sharing information about transactions and block distribution. This also enables the Ouroboros algorithm to make its â€˜decisionsâ€™.

Cardano đảm bảo niềm tin và bảo mật trong một môi trường phi tập trung bằng cách sử dụng sự đồng thuận bằng chứng thông qua thuật toán OuroBoros.
Trọng tâm của điều này là khoảng 3.000 nhóm cổ phần được điều hành bởi các nhà khai thác (SPO), người quản lý các nút phân tán cung cấp năng lượng cho mạng.
Rõ ràng, trong một mạng lưới phi tập trung và phân tán, phải có sự giao tiếp đáng tin cậy giữa các nút này.
Trọng tâm của điều này và quan trọng để xác minh các hoạt động blockchain là khuếch tán dữ liệu - Quá trình chia sẻ thông tin về giao dịch và phân phối khối.
Điều này cũng cho phép thuật toán OuroBoros thực hiện các quyết định của nó.

Until recently, Cardano nodes established connections with peers by looking up a file that described the static configuration of the network. The system also relied on nodes set up by IOG â€“ with a community-managed and configured topology â€“ that helped to establish network connectivity (read more about [the evolution of network connectivity](https://iohk.io/en/blog/posts/2021/05/11/cardano-decentralization-continues/) here). To increase decentralization and simplify node communications, we've been establishing [a P2P network](https://iohk.io/en/blog/posts/2021/04/06/boosting-network-decentralization-with-p2p/). Direct interaction between peers streamlines communication between the thousands of distributed nodes that will maintain the network without reliance on federated relays. This will be done by automated P2P networking components. Automating the process of peer selection brings us closer to a fully decentralized network and simplifies the process of running a relay or a block-producing node.

Cho đến gần đây, các nút Cardano đã thiết lập các kết nối với các đồng nghiệp bằng cách tìm kiếm một tệp mô tả cấu hình tĩnh của mạng. Hệ thống này cũng dựa vào các nút được thiết lập bởi IOG-với cấu trúc liên kết được quản lý và cấu hình cộng đồng-đã giúp thiết lập kết nối mạng (đọc thêm về [sự phát triển của kết nối mạng] (https://iohk.io/ en/blog/bài viết/2021/05/11/cardano-phân cấp-continues/) tại đây). Để tăng sự phân cấp và đơn giản hóa việc liên lạc nút, chúng tôi đã thiết lập [mạng P2P] (https://iohk.io/en/blog/posts/2021/04/06/boosting-network-decentralization-with-p2p/) . Tương tác trực tiếp giữa các đồng nghiệp hợp lý hóa giao tiếp giữa hàng ngàn nút phân tán sẽ duy trì mạng mà không phụ thuộc vào các rơle liên kết. Điều này sẽ được thực hiện bởi các thành phần mạng P2P tự động. Tự động hóa quá trình lựa chọn ngang hàng đưa chúng ta đến gần hơn với một mạng phi tập trung hoàn toàn và đơn giản hóa quá trình chạy rơle hoặc nút sản xuất khối.

From the early days of the [Shelley incentivized testnet](https://iohk.io/en/blog/posts/2019/10/24/incentivized-testnet-what-is-it-and-how-to-get-involved/) through to the [Alonzo testnets program](https://twitter.com/InputOutputHK/status/1423704788512952331), community-supported rollouts have been central to our approach. To expand testing of the P2P changes, we are now inviting some pool operators to a semi-public testnet. Eleven operators will help us test the automated P2P components before we expand the program more widely.

Từ những ngày đầu của [Shelley khuyến khích Testnet] (https://iohk.io/en/blog/posts/2019/10/24/incentivized-testnet-what-is-it-how-to-get-get-
liên quan/) thông qua [chương trình ALONZO TESTNET] (https://twitter.com/inputoutputhk/status/1423704788512952331), triển khai hỗ trợ cộng đồng là trung tâm của cách tiếp cận của chúng tôi.
Để mở rộng thử nghiệm các thay đổi P2P, chúng tôi hiện đang mời một số nhà khai thác nhóm đến một testnet bán công khai.
Mười một nhà khai thác sẽ giúp chúng tôi kiểm tra các thành phần P2P tự động trước khi chúng tôi mở rộng chương trình rộng rãi hơn.

## **Whatâ€™s new?**

## ** Cái gì mới? **

P2P is still an experimental feature. Although it will be part of future releases, weâ€™re not yet integrating it into all our work. The pool operators will assess the environment by configuring their nodes for direct interaction with each other. P2P capabilities will be included in the [cardano-node master branch](https://github.com/input-output-hk/cardano-node/pull/3363) and in [merged pull requests to â€˜ouroboros-networkâ€™](https://github.com/input-output-hk/ouroboros-network/pulls?q=is%3Apr+is%3Amerged+label%3Apeer2peer+label%3Anetworking+) on GitHub.

P2P vẫn là một tính năng thử nghiệm.
Mặc dù nó sẽ là một phần của các bản phát hành trong tương lai, nhưng chúng tôi chưa tích hợp nó vào tất cả các công việc của chúng tôi.
Các nhà khai thác nhóm sẽ đánh giá môi trường bằng cách định cấu hình các nút của họ để tương tác trực tiếp với nhau.
Khả năng P2P sẽ được bao gồm trong [Cardano-Node Master Branch] (https://github.com/input-oundput-hk/cardano-node/pull/3363) và trong [các yêu cầu kéo được hợp nhất đến "
·

The P2P mode will enable â€˜churnâ€™ to ensure dynamic promotion and demotion of peers. Updating network configuration will also be simpler for SPOs because their nodes do not have to be restarted.

Chế độ P2P sẽ cho phép - ˜churnâ € ™ để đảm bảo quảng bá động và giáng chức của các đồng nghiệp.
Cập nhật cấu hình mạng cũng sẽ đơn giản hơn cho các SPO vì các nút của chúng không phải được khởi động lại.

The semi-public testnet will also improve the nodeâ€™s Prometheus interface. It will include the following statistics:

Testnet bán công khai cũng sẽ cải thiện giao diện Prometheus của Node.
Nó sẽ bao gồm các số liệu thống kê sau:

- outbound connections: warm (active connections that donâ€™t participate in the consensus) and hot (active connections that take part in the consensus)

- Kết nối bên ngoài: ấm áp (kết nối hoạt động không tham gia vào sự đồng thuận) và nóng (kết nối hoạt động tham gia vào sự đồng thuận)

- inbound connections: warm and hot

- Kết nối trong nước: ấm và nóng

- uni-direction/duplex connections.

- Kết nối đơn hướng/song công.

## **Whatâ€™s next?**

## ** tiếp theo là gì? **

The assessment of network connections on the semi-public testnet will help us to gather valuable feedback and catch unknown issues. Once we are satisfied, we will then be ready to invite all SPOs to test P2P node communications on the public testnet. This will mark the implementation of a smart policy for peer selection. This policy will allow defining final metrics to compare with the previous, non-P2P setting. Most importantly, weâ€™ll continue testing to verify that all the components work flawlessly in isolation as well as in combination in a wide range of network conditions.

Việc đánh giá các kết nối mạng trên testnet bán công khai sẽ giúp chúng tôi thu thập phản hồi có giá trị và nắm bắt các vấn đề chưa biết.
Khi chúng tôi hài lòng, sau đó chúng tôi sẽ sẵn sàng mời tất cả các SPO để kiểm tra liên lạc nút P2P trên testnet công khai.
Điều này sẽ đánh dấu việc thực hiện một chính sách thông minh để lựa chọn ngang hàng.
Chính sách này sẽ cho phép xác định các số liệu cuối cùng so sánh với cài đặt không P2P trước đó.
Quan trọng nhất, chúng tôi sẽ tiếp tục thử nghiệm để xác minh rằng tất cả các thành phần hoạt động hoàn hảo trong sự cô lập cũng như kết hợp trong một loạt các điều kiện mạng.

Follow our [weekly development updates](https://roadmap.cardano.org/en/status-updates/) to find out more about P2P network development and also check out the [Ouroboros network repository](https://github.com/input-output-hk/ouroboros-network) for the latest updates.

Thực hiện theo [cập nhật phát triển hàng tuần của chúng tôi] (https://roadmap.cardano.org/en/status-updates/) để tìm hiểu thêm về phát triển mạng P2P và cũng xem [Kho lưu trữ mạng của Ouroboros] (https: // github.
com/input-output-hk/ouroboros-network) cho các bản cập nhật mới nhất.

