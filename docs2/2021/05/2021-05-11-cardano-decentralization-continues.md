# Cardano decentralization continues: insights into our P2P deployment
### **Stake pools will soon be able to test automated peer-to-peer connections**
![](img/2021-05-11-cardano-decentralization-continues.002.png) 11 May 2021![](img/2021-05-11-cardano-decentralization-continues.002.png)[ Marcin Szamotulski](tmp//en/blog/authors/marcin-szamotulski/page-1/)![](img/2021-05-11-cardano-decentralization-continues.003.png) 5 mins read

![Marcin Szamotulski](img/2021-05-11-cardano-decentralization-continues.004.png)[](tmp//en/blog/authors/marcin-szamotulski/page-1/)
### [**Marcin Szamotulski**](tmp//en/blog/authors/marcin-szamotulski/page-1/)
Software Engineering Lead

Engineering

- ![](img/2021-05-11-cardano-decentralization-continues.005.png)[](mailto:marcin.szamotulski@iohk.io "Email")
- ![](img/2021-05-11-cardano-decentralization-continues.006.png)[](https://www.linkedin.com/in/marcin-szamotulski/ "LinkedIn")
- ![](img/2021-05-11-cardano-decentralization-continues.007.png)[](https://twitter.com/me_coot "Twitter")
- ![](img/2021-05-11-cardano-decentralization-continues.008.png)[](https://github.com/coot "GitHub")

Decentralization of the Cardano network is key to ensuring its long-term sustainability, resilience, and independence from centralized governing entities. Now that block production is [fully decentralized](https://iohk.io/en/blog/posts/2021/03/31/decentralization-to-d-0-day-and-beyond/), our next focus is on developing our decentralized stake pool operator (SPO) ecosystem to build reliable and effective connections between distributed nodes.

Phân cấp mạng lưới Cardano là chìa khóa để đảm bảo tính bền vững, khả năng phục hồi và độc lập lâu dài của nó từ các thực thể quản lý tập trung.
Bây giờ sản xuất khối đó được [phi tập trung hoàn toàn] (https://iohk.io/en/blog/posts/2021/03/31/decentralization-to-d-0-day-and-beyond/), trọng tâm tiếp theo của chúng tôi là
Khi phát triển hệ sinh thái vận hành nhóm cổ phần (SPO) phi tập trung của chúng tôi để xây dựng các kết nối đáng tin cậy và hiệu quả giữa các nút phân tán.

Giving the power to validate blocks and transactions to stake pool operators requires enhancements to the network software. The activation of the peer-to-peer (P2P) governor, along with the deployment of the connection manager, enabled the release of a private P2P testnet in late April. We are now assessing this engineering testnet before deploying a semi-public P2P testnet for a group of invited SPOs to help us test and tune.

Đưa ra sức mạnh để xác nhận các khối và giao dịch để đặt cược các nhà khai thác nhóm yêu cầu cải tiến phần mềm mạng.
Việc kích hoạt thống đốc ngang hàng (P2P), cùng với việc triển khai Trình quản lý kết nối, đã cho phép phát hành P2P Testnet riêng vào cuối tháng Tư.
Chúng tôi hiện đang đánh giá TestNet kỹ thuật này trước khi triển khai Testnet P2P bán công khai cho một nhóm các Spo được mời để giúp chúng tôi kiểm tra và điều chỉnh.

In the [P2P governor post](https://iohk.io/en/blog/posts/2021/04/06/boosting-network-decentralization-with-p2p/), we discussed the networkâ€™s architecture and the interaction between mini protocols and the components that enable direct and automated communication between nodes. Here, we assess how the connectivity model has matured to enable automated peer connectivity and reflect on the results of the private testnet launch.

Trong [P2P Post Post] (https://iohk.io/en/blog/posts/2021/04/06/boosting-network-decentralization
Tương tác giữa các giao thức mini và các thành phần cho phép giao tiếp trực tiếp và tự động giữa các nút.
Ở đây, chúng tôi đánh giá làm thế nào mô hình kết nối đã trưởng thành để cho phép kết nối ngang hàng tự động và phản ánh về kết quả khởi chạy testnet riêng tư.

## **Evolution of network connectivity**

## ** Sự phát triển của kết nối mạng **

When Cardano was launched, the Byron network connectivity model operated in a federated state. In that setting, IOHK maintained core and relay nodes that connected to about 200 other relays (Figure 1).

Khi Cardano được ra mắt, mô hình kết nối mạng Byron hoạt động ở trạng thái liên kết.
Trong cài đặt đó, IOHK duy trì các nút lõi và rơle kết nối với khoảng 200 rơle khác (Hình 1).

![federated network connectivity](img/2021-05-11-cardano-decentralization-continues.009.png)

Figure 1. Byron federated network structure 

Hình 1. Cấu trúc mạng liên kết Byron

With the launch of Shelley last year, Cardano started functioning in a hybrid setting. This allowed stake pools to construct their P2P network manually by connecting to core and relay nodes and also to the seven federated relays that helped maintain the network during this transitional phase (Figure 2).

Với sự ra mắt của Shelley năm ngoái, Cardano đã bắt đầu hoạt động trong một môi trường lai.
Điều này cho phép các nhóm cổ phần xây dựng mạng P2P của họ theo cách thủ công bằng cách kết nối với các nút lõi và rơle và cũng với bảy rơle liên kết giúp duy trì mạng trong giai đoạn chuyển tiếp này (Hình 2).

![Hybrid network connectivity](img/2021-05-11-cardano-decentralization-continues.009.png)

Figure 2. Shelleyâ€™s initial hybrid network structure

Hình 2. Cấu trúc mạng lai ban đầu của Shelley

Since March, block production has been entirely decentralized, with stake pools following manual topologies for P2P connections. This means that SPOs have been using a list of relay nodes registered across the globe to generate their configuration for connections with other peers. To provide better efficiency, it is essential to enable automated node communication without reliance on IO-run relay nodes. Thus, the networking team is now deploying the automated P2P code, which will allow pool operators to create and run a more decentralized network. 

Kể từ tháng 3, sản xuất khối đã được phân cấp hoàn toàn, với các nhóm cổ phần theo các cấu trúc liên kết thủ công cho các kết nối P2P.
Điều này có nghĩa là các SPO đã sử dụng một danh sách các nút chuyển tiếp được đăng ký trên toàn cầu để tạo cấu hình của chúng cho các kết nối với các đồng nghiệp khác.
Để cung cấp hiệu quả tốt hơn, điều cần thiết là cho phép giao tiếp nút tự động mà không cần phụ thuộc vào các nút chuyển tiếp IO chạy.
Do đó, nhóm kết nối mạng hiện đang triển khai mã P2P tự động, điều này sẽ cho phép các nhà khai thác nhóm tạo và chạy một mạng phi tập trung hơn.

In this way, once the P2P mainnet is deployed, Cardano will be maintained solely by community-run nodes (Figure 3).

Theo cách này, một khi P2P chính được triển khai, Cardano sẽ chỉ được duy trì bởi các nút do cộng đồng điều hành (Hình 3).

![p2p network](img/2021-05-11-cardano-decentralization-continues.010.png)

Figure 3. Final network structure with automated node communication

Hình 3. Cấu trúc mạng cuối cùng với giao tiếp nút tự động

## **P2P testnet and node communication**

## ** P2P Testnet và Node Truyền thông **

The first stage in the P2P rollout was the launch of the private P2P testnet last month. This has been used to test the basic capabilities of the components:

Giai đoạn đầu tiên trong buổi giới thiệu P2P là sự ra mắt của P2P Testnet riêng vào tháng trước.
Điều này đã được sử dụng để kiểm tra các khả năng cơ bản của các thành phần:

- **P2P governor**: manages hot, warm, and cold sets of peers and ensures that the node meets the target number of each type of peer. 

- ** Thống đốc P2P **: Quản lý các bộ đồng nghiệp nóng, ấm và lạnh và đảm bảo rằng nút đáp ứng số mục tiêu của từng loại ngang hàng.

- **Connection manager**: creates outbound connections or registers inbound connections, tracks their state, and allows full-duplex TCP connections to be reused. 

- ** Trình quản lý kết nối **: Tạo các kết nối bên ngoài hoặc các đăng ký kết nối trong nước, theo dõi trạng thái của chúng và cho phép các kết nối TCP song công hoàn toàn được sử dụng lại.

- **Server**: accepts connections and performs dynamic rate limiting. 

- ** Máy chủ **: Chấp nhận kết nối và thực hiện giới hạn tốc độ động.

- **Inbound protocol governor**: responsible for running and tracking the state of the inbound connection side. This includes tracking the state of each remote peer (cold, warm, or hot) and the state of each inbound mini-protocol. 

- ** Thống đốc giao thức gửi đến **: Chịu trách nhiệm chạy và theo dõi trạng thái của phía kết nối trong nước.
Điều này bao gồm theo dõi trạng thái của mỗi đồng đẳng từ xa (lạnh, ấm hoặc nóng) và trạng thái của mỗi giao thức nhỏ trong nước.

The P2P system was deployed in a private environment and tested between eight nodes that connected to the mainnet and established communication with active SPO relay nodes; these further connected to other relays and block-producing nodes. The system enabled nodes to discover stake pool relays using the on-chain stake pool registry, which includes the DNS name or IP address of each relay.

Hệ thống P2P đã được triển khai trong môi trường riêng và được thử nghiệm giữa tám nút kết nối với Mainnet và thiết lập giao tiếp với các nút tiếp sức hoạt động SPO;
Chúng được kết nối thêm với các rơle khác và các nút sản xuất khối.
Hệ thống cho phép các nút khám phá rơle nhóm cổ phần bằng cách sử dụng sổ đăng ký nhóm cổ phần trên chuỗi, bao gồm tên DNS hoặc địa chỉ IP của mỗi rơle.

Test results show that the nodes could arbitrarily select peers for communication, including those from the mainnet. The use of an â€˜upstreamâ€™ metric enabled the discarding of the worst-performing peers and random selection of new peers for connection. This policy has been demonstrated in large-scale simulations (10,000 nodes), providing close-to-optimal results. In the live testing, the team saw many iterations of the optimization procedure. The team also observed that a range of peer connections occurred â€“ with both nearby and far-away peers from different locations, which was inherent to all the eight nodes run in different parts of the world.

Kết quả kiểm tra cho thấy các nút có thể tùy ý chọn các đồng nghiệp để liên lạc, bao gồm cả các nút từ mainnet.
Việc sử dụng một số liệu "Upstreamâ ™ cho phép loại bỏ các đồng nghiệp hoạt động tồi tệ nhất và lựa chọn ngẫu nhiên các đồng nghiệp mới để kết nối.
Chính sách này đã được chứng minh trong các mô phỏng quy mô lớn (10.000 nút), cung cấp kết quả gần tối ưu.
Trong thử nghiệm trực tiếp, nhóm nghiên cứu đã thấy nhiều lần lặp lại của quy trình tối ưu hóa.
Nhóm nghiên cứu cũng quan sát thấy rằng một loạt các kết nối ngang hàng đã xảy ra-với cả hai đồng nghiệp gần đó và xa từ các địa điểm khác nhau, vốn có của tất cả tám nút chạy ở các nơi khác nhau trên thế giới.

The networking and DevOps teams are now working together to improve the testnet environment, so all SPOs invited to the semi-public testnet can establish direct peer connections. This includes work on feature enhancements and testing processes to deliver the most efficient results. Thus, to introduce new targets for local root peers, the team is finalizing the tests for such related features as targets for known, established, and active peers.

Các nhóm Mạng và DevOps hiện đang hợp tác để cải thiện môi trường Testnet, vì vậy tất cả các SPO được mời đến Testnet bán công khai có thể thiết lập các kết nối ngang hàng trực tiếp.
Điều này bao gồm công việc về cải tiến tính năng và quy trình thử nghiệm để cung cấp kết quả hiệu quả nhất.
Do đó, để giới thiệu các mục tiêu mới cho các đồng nghiệp gốc địa phương, nhóm nghiên cứu đang hoàn thiện các bài kiểm tra cho các tính năng liên quan như các mục tiêu cho các đồng nghiệp đã biết, thành lập và tích cực.

*We will be soon launching the semi-public P2P testnet, with the support of a small group of SPO partners to help with initial testing, before broadening this out to the wider SPO community. As ever, early feedback and ideas from our community are central to test, iterate, and improve processes as we progress towards a fully automated and decentralized P2P architecture for the Cardano mainnet.*

*Chúng tôi sẽ sớm ra mắt P2P Testnet bán công khai, với sự hỗ trợ của một nhóm nhỏ các đối tác SPO để giúp thử nghiệm ban đầu, trước khi mở rộng điều này cho cộng đồng SPO rộng lớn hơn.
Như mọi khi, phản hồi ban đầu và ý tưởng từ cộng đồng của chúng tôi là trung tâm để kiểm tra, lặp lại và cải thiện các quy trình khi chúng tôi tiến tới một kiến trúc P2P hoàn toàn tự động và phi tập trung cho Cardano Mainnet.*

*Additional contributions from Karl Knutsson, Duncan Coutts, Neil Davies, Prashanti Naik, and Olga Hryniuk.*

*Đóng góp bổ sung từ Karl Knutsson, Duncan Coutts, Neil Davies, Prashanti Naik và Olga Hryniuk.*

