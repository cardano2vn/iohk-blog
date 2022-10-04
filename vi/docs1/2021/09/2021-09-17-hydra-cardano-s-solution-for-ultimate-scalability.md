# Hydra - Giải pháp Layer 2 để Cardano tối ưu khả năng mở rộng

### **Khả năng mở rộng của Hydra được đưa vào lộ trình phát triển Cardano**

![](img/2021-09-17-hydra-cardano-s-solution-for-ultimate-scalability.002.png) 17 tháng 9 năm 2021 ![](img/2021-09-17-hydra-cardano-s-solution-for-ultimate-scalability.002.png) [Sebastian Nagel](tmp//en/blog/authors/sebastian-nagel/page-1/) ![](img/2021-09-17-hydra-cardano-s-solution-for-ultimate-scalability.003.png) 7 phút đọc

![Sebastian Nagel](img/2021-09-17-hydra-cardano-s-solution-for-ultimate-scalability.004.png)[](tmp//en/blog/authors/sebastian-nagel/page-1/)

### [**Sebastian Nagel**](tmp//en/blog/authors/sebastian-nagel/page-1/)

Software Engineering Lead

Engineering

- ![](img/2021-09-17-hydra-cardano-s-solution-for-ultimate-scalability.005.png)[](mailto:sebastian.nagel@iohk.io "Email")
- ![](img/2021-09-17-hydra-cardano-s-solution-for-ultimate-scalability.006.png)[](https://www.linkedin.com/in/sebastian-nagel-2bb43a1a/ "LinkedIn")
- ![](img/2021-09-17-hydra-cardano-s-solution-for-ultimate-scalability.007.png)[](https://github.com/ch1bo "GitHub")

![Hydra - Giải pháp Layer 2 để Cardano tối ưu khả năng mở rộng](img/2021-09-17-hydra-cardano-s-solution-for-ultimate-scalability.008.jpeg)

The Alonzo upgrade enables the creation of smart contracts, decentralized applications (DApps), and other applications on top of Cardano.

Alonzo marks a significant milestone in the Cardano journey, deploying base level scripting capability that will, in turn, enable further innovation and network development. It also starts the process of transforming a transactions &amp; tokens based blockchain into a dynamic confluence of creativity, financial inclusion, and decentralized development.

Hydra là một trong những phát triển thú vị nhất được Alonzo kích hoạt. Nó là một giải pháp Layer 2 quan trọng để cải thiện hơn nữa khả năng mở rộng của Cardano, phân lớp một giao thức mới trên Blockchain Layer 1 hiện tại.

### **Hydra: Giải pháp Layer 2 của Cardano**

In a blockchain network, a consensus algorithm creates a secure and trustless environment by ensuring agreement on a transaction history. Cardano uses Ouroboros, an efficient proof-of-stake consensus algorithm, for this very purpose. But Cardano also, just like any permissionless blockchain, faces challenges when trying to scale to achieve the throughput required to support applications in the real world, including payment, identification, game, or mobile services. After all, the blockchain needs to reach global consensus on each and every transaction.

Các giao dịch Cardano phải trả phí. Những người vận hành mạng lưới (trong trường hợp của Cardano là cộng đồng SPO) cần được thưởng xứng đáng cho phần công việc mà họ xử lý, vì vậy phí giao dịch cần phải được đặt ở mức hợp lý. Người dùng muốn trả mức phí mà họ có thể chấp nhận được. Ngoài ra, Blockchain cần được bảo vệ trước các cuộc tấn công từ chối dịch vụ (DoS). Do đó, các khoản phí không thể được đặt quá thấp để dẫn đến rủi ro không đáng có. Kẻ tấn công sẽ chịu tổn thất cực kỳ lớn nếu thực hiện các cuộc tấn công DoS. Việc lưu trữ cũng là một mối quan tâm, vì lịch sử giao dịch ngày càng tăng có thể dẫn đến các vấn đề về lưu trữ. Về mặt ảnh hưởng, các Blockchain thành công nhất có nguy cơ trở thành 'nạn nhân' của chính thành công đó.

Hydra là một giải pháp khả năng mở rộng Layer 2. Nó tìm cách giải quyết tất cả những mối quan tâm này với mục đích tối đa hóa thông lượng, giảm thiểu độ trễ, phát sinh chi phí thấp hoặc không tốn kém và giảm đáng kể yêu cầu lưu trữ.

### **Scaling isomorphically**

Vậy Hydra làm điều này như thế nào? Bằng cách cung cấp các phương thức xử lý giao dịch ngoài chuỗi hiệu quả hơn cho một nhóm người dùng, đồng thời sử dụng sổ cái của chuỗi chính làm lớp thanh toán an toàn. Hydra giữ các đảm bảo an toàn trong khi vẫn giữ được liên kết cần thiết với chuỗi chính. Nó không yêu cầu sự đồng thuận toàn cầu và có thể thích ứng với nhiều loại ứng dụng. Ví dụ: Hydra cho phép phí giao dịch và Giá trị UTXO tối thiểu được cài đặt ở mức thấp nhất là 1 hoặc 2 Lovelace, rất quan trọng đối với các giao dịch vi mô và các trường hợp sử dụng mà chúng mở khóa.

Most importantly though, Hydra introduces the concept of [isomorphic state channels](https://eprint.iacr.org/2020/299.pdf): that is, to reuse the same ledger representation to yield uniform, off-chain ledger siblings, which we call Heads (hence the Hydra name, which references the [mythological, multi-headed creature](https://en.wikipedia.org/wiki/Lernaean_Hydra)). Specifically for Cardano, this means that native assets, non-fungible tokens (NFTs), and Plutus scripting are available inside *each* Hydra Head. Isomorphism permits a natural extension of the system, rather than a bolted-on one.

Nhiều giao dịch hiện đang được xử lý bởi chuỗi chính hoặc ứng dụng chạy trên chuỗi chính có thể được hưởng lợi trực tiếp từ Hydra, vì nó chỉ hiểu các định dạng và chữ ký giao dịch giống nhau. Điều này làm giảm đáng kể rào cản gia nhập Hydra đối với các khách hàng mới hiện tại và tiềm năng. Họ có thể sử dụng lại cơ sở hạ tầng đã được thử nghiệm của Cardano để xây dựng ví và ứng dụng tương tác với hệ thống Layer 2. Ngoài ra, một Hydra Head có thể được tạo mà không cần tiền ban đầu từ phía bên nhận, điều này cho phép trải nghiệm người dùng mượt mà.

### **Developing a proof of concept**

Chúng tôi đã triển khai giao thức Hydra Head cơ bản như một bằng chứng về khái niệm Hydra-node. Bản xem trước dành cho nhà phát triển sẽ sẵn sàng vào thời điểm diễn ra Hội nghị thượng đỉnh Cardano sắp tới. Điều này sẽ cho phép các nhà phát triển (hoặc bất kỳ ai quan tâm) chạy một hoặc nhiều node Hydra trực tuyến, mở một Hydra Head với số lượng người tham gia giới hạn và cung cấp các giao dịch cho nó. Người dùng có thể mong đợi một nguyên mẫu hoạt động qua một Testnet chuyên dụng, cộng với các số liệu và tài liệu đo điểm chuẩn sớm trong [kho lưu trữ](https://github.com/input-output-hk/hydra-poc) GitHub này. Có thể sẽ không có bất kỳ thành phần hướng tới người dùng nào (ví, giao diện người dùng, v.v.) có sẵn.

It is also important to make a point about transactions per second (TPS), too often rather clumsily used as the sole measure of ‘success’ when it comes to scalability. Some people tend to rate a network on the basis of its maximum throughput measured in throughput (TPS). While this is a reasonable measure for ‘legacy’ systems where there is high predictability and conformity (e.g., the VISA network) it is a less useful metric for distributed systems. Instead, our initial focus is on latency (the time that elapses until a transaction is confirmed) as another, more practical way to measure speed of blockchain transactions. On the mainnet, minimum latency is 20 seconds (one block). This is the starting point. In a layer 2 system like Hydra, it is possible to achieve confirmation times of *less than one second*. Terms like ‘one million TPS’ have been used before. It is a bold number, and while this remains as an aspirational target, the ultimate goal of any system is the flexibility to grow capability with demand. Throughput measured in TPS per Hydra head is secondary, and mostly limited by the available hardware. In principle, by adding increasing numbers of Hydra heads to the system, arbitrarily high throughput can be achieved by the system as a whole.

### **Sự phát triển của Hydra theo thời gian**

In the short term, we will keep developing the hydra-node and the Hydra Head protocol until it becomes a solid and stable foundation for the community (and us!) to build real-world applications. These new apps will benefit from fast settling and low-to-no-cost transactions. We are also actively developing other key features, including the support of multiple heads per node, persistence, and Head protocol extensions

In the medium term, say 6-12 months, progress will greatly depend on the results of our research and experimentation, plus feedback from the developer community. We are researching ways to interconnect multiple Hydra Heads to increase the “reach” of our layer 2 solution, for example, and also testing different methods to make it easier to integrate and use Hydra. One of the most exciting visions for the long term is the development of ‘Virtual Heads’ by running the Hydra Head protocol *inside* Hydra Heads, thus fully utilizing the isomorphism of our Layer 2 solution. Herein lies true, *theoretical limitless* scalability.

### **Tính linh hoạt là chìa khóa cho khả năng mở rộng và tăng trưởng**

The overarching concept for Hydra is the provision of a pioneering layer 2 scalability solution suitable for Cardano, a third-generation, UTXO-based blockchain capable of supporting smart contracts. Hydra will drive down costs while increasing throughput and maintaining security.

Hydra replicates the main chain's functionality while minimizing friction for users, but still allows the flexibility of having a different fee / cost structure and timing constraints on the layer 2. Any successful ecosystem balances the needs of all users. We want this ecosystem to serve the needs of individual consumers, enterprises, professionals, and the growing list of DApps and their developers.

Với Hardfork Alonzo, Cardano sẽ bắt đầu một hành trình mới với tư cách là một nền tảng hợp đồng thông minh, cho phép các công nghệ như Hydra sẽ cải thiện đáng kể khả năng mở rộng của Cardano và tiếp tục được áp dụng.

*Tại [Hội nghị thượng đỉnh Cardano 2021](https://summit.cardano.org/), diễn ra từ 25-26 tháng 9, chúng tôi sẽ nói nhiều hơn về Hydra, tiến trình của nó cho đến nay và các mục tiêu cho tương lai. Hãy chắc chắn rằng bạn tham gia với chúng tôi! Và bạn cũng có thể muốn xem [phần giải thích Video này](https://www.youtube.com/watch?v=7ySUbFpTrAk) .*

#### ***Matthias Benkort, Arnaud Bailly, and Fernando Sanchez also contributed to this piece.***
