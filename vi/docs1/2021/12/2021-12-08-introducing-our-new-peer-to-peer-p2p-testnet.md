# Giới thiệu mạng thử nghiệm ngang hàng (P2P) mới.

### **Chúng tôi đang làm việc với một nhóm nhỏ các SPO trên mạng thử nghiệm P2P mới để mạng lưới ngày càng phi tập trung hơn**

![](img/2021-12-08-introducing-our-new-peer-to-peer-p2p-testnet.002.png) 8 tháng 12 năm 2021 ![](img/2021-12-08-introducing-our-new-peer-to-peer-p2p-testnet.002.png) [Olga Hryniuk](tmp//en/blog/authors/olga-hryniuk/page-1/) ![](img/2021-12-08-introducing-our-new-peer-to-peer-p2p-testnet.003.png) 3 phút đọc

![Olga Hryniuk](img/2021-12-08-introducing-our-new-peer-to-peer-p2p-testnet.004.png)[](tmp//en/blog/authors/olga-hryniuk/page-1/)

### [**Olga Hryniuk**](tmp//en/blog/authors/olga-hryniuk/page-1/)

Technical Writer

Marketing &amp; Communications

- ![](img/2021-12-08-introducing-our-new-peer-to-peer-p2p-testnet.005.png)[](https://www.linkedin.com/in/olga-hryniuk-1094a3160/ "LinkedIn")
- ![](img/2021-12-08-introducing-our-new-peer-to-peer-p2p-testnet.006.png)[](https://github.com/olgahryniuk "GitHub")

![Introducing our new peer-to-peer (P2P) testnet ](img/2021-12-08-introducing-our-new-peer-to-peer-p2p-testnet.007.png)

Cardano continues to build momentum with more features and capabilities being steadily added to the blockchain. As we recently reported, we are [optimizing the network](https://iohk.io/en/blog/posts/2021/11/10/optimizing-cardano/) to increase throughput so more transactions can be processed faster, and decentralized applications (DApps) and smart contracts created and used more efficiently. This week, we have kicked off an important new initiative to support our ongoing drive toward full decentralization with the launch of a new peer-to-peer (P2P) testnet.

Cardano ensures trust and security in a decentralized setting using proof-of-stake consensus through the Ouroboros algorithm. At the heart of this are about 3,000 stake pools run by operators (SPOs) who manage the distributed nodes that power the network. Clearly, in a decentralized and distributed network, there has to be reliable communication between these nodes. Central to this and vital for verifying blockchain activities is data diffusion â€“ the process of sharing information about transactions and block distribution. This also enables the Ouroboros algorithm to make its â€˜decisionsâ€™.

Until recently, Cardano nodes established connections with peers by looking up a file that described the static configuration of the network. The system also relied on nodes set up by IOG â€“ with a community-managed and configured topology â€“ that helped to establish network connectivity (read more about [the evolution of network connectivity](https://iohk.io/en/blog/posts/2021/05/11/cardano-decentralization-continues/) here). To increase decentralization and simplify node communications, we've been establishing [a P2P network](https://iohk.io/en/blog/posts/2021/04/06/boosting-network-decentralization-with-p2p/). Direct interaction between peers streamlines communication between the thousands of distributed nodes that will maintain the network without reliance on federated relays. This will be done by automated P2P networking components. Automating the process of peer selection brings us closer to a fully decentralized network and simplifies the process of running a relay or a block-producing node.

Từ [Shelley Testnet](https://iohk.io/en/blog/posts/2019/10/24/incentivized-testnet-what-is-it-and-how-to-get-involved/) cho đến [Alonzo Testnet](https://twitter.com/InputOutputHK/status/1423704788512952331), các đợt triển khai do cộng đồng hỗ trợ đã là trọng tâm trong cách tiếp cận của chúng tôi. Để mở rộng thử nghiệm các thay đổi của mạng P2P, chúng tôi hiện đang mời một số SPO tham gia Testnet bán công khai. Sẽ có 11 SPO giúp chúng tôi kiểm tra các thành phần P2P một cách tự động trước khi chương trình được mở rộng.

## **P2P Testnet có gì mới?**

P2P vẫn là một tính năng thử nghiệm. Mặc dù nó sẽ là một phần của các bản phát hành trong tương lai, nhưng chúng tôi vẫn chưa tích hợp nó vào trong các phần công việc. Các SPO sẽ đánh giá môi trường thử nghiệm bằng cách cấu hình để các Node tương tác trực tiếp với nhau. Các khả năng của mạng P2P sẽ được đưa vào [nhánh chính của Cardano-Node](https://github.com/input-output-hk/cardano-node/pull/3363) và trong [các yêu cầu được hợp nhất với "mạng lưới Ouroboros"](https://github.com/input-output-hk/ouroboros-network/pulls?q=is%3Apr+is%3Amerged+label%3Apeer2peer+label%3Anetworking+) trên GitHub.

The P2P mode will enable â€˜churnâ€™ to ensure dynamic promotion and demotion of peers. Updating network configuration will also be simpler for SPOs because their nodes do not have to be restarted.

The semi-public testnet will also improve the nodeâ€™s Prometheus interface. It will include the following statistics:

- outbound connections: warm (active connections that donâ€™t participate in the consensus) and hot (active connections that take part in the consensus)
- inbound connections: warm and hot
- uni-direction/duplex connections.

## **Tiếp theo là gì?**

Việc đánh giá các kết nối mạng lưới trên Testnet bán công khai sẽ giúp chúng tôi thu thập phản hồi có giá trị và nắm bắt các vấn đề cần cải thiện. Khi mọi việc hoạt động ổn định, chúng tôi sẽ mời tất cả SPO thử nghiệm việc trao đổi thông tin với Node P2P trên Testnet công khai. Điều này sẽ đánh dấu việc thực hiện một chính sách thông minh để lựa chọn Node ngang hàng. Chính sách này sẽ cho phép xác định các chỉ số cuối cùng để so sánh với chỉ số trước đó, cài đặt Non-P2P. Quan trọng nhất, chúng tôi sẽ tiếp tục thử nghiệm để xác minh rằng tất cả các thành phần đều tốt khi hoạt động độc lập, cũng như kết hợp trong nhiều điều kiện của mạng lưới.

Follow our [weekly development updates](https://roadmap.cardano.org/en/status-updates/) to find out more about P2P network development and also check out the [Ouroboros network repository](https://github.com/input-output-hk/ouroboros-network) for the latest updates.
