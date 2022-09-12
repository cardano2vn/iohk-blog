# Mithril: Một Blockchain mạnh hơn, nhẹ hơn để hiệu quả hơn

### **Một giao thức mới do IOHK phát triển hoạt động với một sơ đồ chữ ký ngưỡng dựa trên cổ phần cho phép tận dụng cổ phần một cách minh bạch, an toàn và nhanh chóng**

![](img/2021-10-29-mithril-a-stronger-and-lighter-blockchain-for-better-efficiency.002.png) 29 October 2021![](img/2021-10-29-mithril-a-stronger-and-lighter-blockchain-for-better-efficiency.002.png)[ Olga Hryniuk](tmp//en/blog/authors/olga-hryniuk/page-1/)![](img/2021-10-29-mithril-a-stronger-and-lighter-blockchain-for-better-efficiency.003.png) 10 mins read

![Olga Hryniuk](img/2021-10-29-mithril-a-stronger-and-lighter-blockchain-for-better-efficiency.004.png)[](tmp//en/blog/authors/olga-hryniuk/page-1/)

### [**Olga Hryniuk**](tmp//en/blog/authors/olga-hryniuk/page-1/)

Technical Writer

Marketing &amp; Communications

- ![](img/2021-10-29-mithril-a-stronger-and-lighter-blockchain-for-better-efficiency.005.png)[](https://www.linkedin.com/in/olga-hryniuk-1094a3160/ "LinkedIn")
- ![](img/2021-10-29-mithril-a-stronger-and-lighter-blockchain-for-better-efficiency.006.png)[](https://github.com/olgahryniuk "GitHub")

![Mithril: a stronger and lighter blockchain for better efficiency](img/2021-10-29-mithril-a-stronger-and-lighter-blockchain-for-better-efficiency.007.jpeg)

At the [Cardano Summit 2021](https://summit.cardano.org/), IOHK researchers Pyrros Chaidos and Roman Oliynykov presented the design and goals of Mithril â€“ new research and engineering effort carried out by IOHK. Mithril will provide a stake-based threshold signature scheme that can be implemented as the protocol to solve chain synchronization, state bootstrapping, and trust issues in blockchain applications.

Mithril là tên của một kim loại hư cấu ở Trung Địa - một vật liệu dễ uốn, trọng lượng rất nhẹ nhưng bền như 'thép Triple', không bị xỉn màu hoặc ăn mòn. Do đó, cái tên này tượng trưng cho sức mạnh về mặt bảo mật và tiếp cận một cách gọn nhẹ đối với giao thức đã phát triển.

## **Sử dụng cổ phần để tổng hợp chữ ký**

Letâ€™s start with some background information to understand Mithril's benefits for the development of blockchain solutions.

Cardano là một Blockchain sử dụng Bằng chứng cổ phần (POS). Do đó, thuật toán đồng thuận sẽ chọn ngẫu nhiên các node để trở thành người sản xuất Block theo số lượng cổ phần mà họ nắm giữ. Đối với một số thông điệp hoặc hành động nhất định, điều quan trọng là một số lượng các bên liên quan phải cung cấp chữ ký mã hoá của họ. Giao thức đồng thuận xác định cách các node riêng lẻ đánh giá trạng thái hiện tại của hệ thống sổ cái và có 3 trách nhiệm chính:

- perform a leader check and decide if a block should be produced
- handle chain selection
- verify produced blocks.

Để đạt được khả năng mở rộng hơn trong cách thiết kế một Blockchain, điều cần thiết là phải giải quyết sự phức tạp của các hoạt động quan trọng phụ thuộc vào Logarit về số lượng người tham gia. Điều này có nghĩa là số lượng người tham gia càng cao (số lượng rất lớn), thì việc tổng hợp *hiệu quả* chữ ký của họ càng trở nên phức tạp hơn. Trong một kịch bản cơ sở, để giả định một chữ ký thể hiện cho đa số các bên liên quan, mọi bên liên quan cần phải ký vào thông điệp cá nhân thích hợp. Mặc dù điều này là có thể, nhưng nó không hiệu quả về khả năng mở rộng và tốc độ.

Given the time it takes to validate a particular message, and the resource usage during chain synchronization, it is vital to provide a solution that makes multi-signature aggregation fast and efficient without compromising security features.

## **Mithril protocol design**

Mithril is a protocol designed to:

- leverage stake to obtain higher efficiency
- ensure transparent setup while not requiring increased trust settings
- Tận dụng sự cân bằng giữa kích thước và hiệu quả, được đảm bảo bởi thành phần mô-đun thiết kế.

Mithril hoạt động công khai, người ký không cần phải tương tác với những người ký khác để tạo ra chữ ký hợp lệ. Người tổng hợp sẽ tổng hợp tất cả các chữ ký thành một và quá trình này là Logarit đối với số lượng chữ ký, dẫn đến hiệu suất  tuyến tính dưới cho phép tổng hợp Mithril. Ví dụ: khi được áp dụng cho các node đầy đủ như Daedalus, Mithril có thể tăng cường đồng bộ hóa dữ liệu cho node đầy đủ, đảm bảo tốc độ và giảm mức tiêu thụ tài nguyên.

To represent a significant fraction of the total stake, Mithril uses the stake-based *threshold* setting. This behavior is different from the standard setting in which the given number of participants are required to validate a particular message. In the stake-based threshold setting, the protocol requires a fraction of the total stake to validate a given message to generate a correct signature.

Mithril cũng chứng nhận sự đồng thuận trong một môi trường không cần lòng tin. Điều này nghĩa là nó không bao gồm bất kỳ giả định tin cậy bổ sung nào. Có thể đạt được chứng nhận đồng thuận mà không bao gồm bất kỳ giả định bổ sung nào, ngoài những giả định đã có trong bằng chứng cổ phần. Ví dụ: nó có thể hoạt động trong Ví như một dịch vụ và ứng dụng khách di động sẽ sử dụng chứng chỉ thu được từ một node Mithril. Với cài đặt bảo mật nâng cao, quy trình như vậy có khả năng hiệu quả hơn so với xác minh SPO Blockchain.

Cuối cùng, để đảm bảo việc khởi động trạng thái chuỗi một cách nhanh chóng, sơ đồ chữ ký cho phép các bên liên quan khác nhau chỉ xác nhận một điểm kiểm tra nhất định của chuỗi. Các bên liên quan không cần phải xem toàn bộ lịch sử giao dịch của trạng thái nhất định - họ chỉ cần thông qua các trạm kiểm soát để xác minh rằng cổ phần cuối cùng là hợp lệ. Điều này có lợi cho các ứng dụng khách nhẹ như Ví nhẹ cần hoạt động nhanh mà không cần đồng bộ hóa toàn bộ dữ liệu của Blockchain. Chữ ký Mithril cũng có thể hữu ích cho việc xác minh kiểm đếm nhanh chóng hoặc ra quyết định quản trị đối với tiền mã hoá.

## **How it works**

Mithril cho phép chữ ký của nhiều bên bằng cách nắm giữ một số xổ số riêng lẻ (*M*) và coi một thông điệp là hợp lệ nếu nó đã được ký bởi một số người chiến thắng khác nhau (*K*) đối với các xổ số đó. Do đó, mỗi người dùng cố gắng ký vào thông điệp. Sau đó họ chuyển chữ ký thông qua một chức năng xổ số. Chức năng này cho phép người dùng cá nhân kiểm tra xem chữ ký của họ có đủ điều kiện là người trúng xổ số hay không và xuất ra những chữ ký đó mà không cần chờ đợi. Điều này khác với thiết lập tiêu chuẩn, ở đó các Slot Leader cần đợi cho đến khi Slot của họ hoạt động để tham gia. Khi có chữ ký qua các loại xổ số khác nhau, chúng có thể được tổng hợp thành một chữ ký Mithril duy nhất.

**Phases**

The design of Mithril involves three phases:

![Mithril design](img/2021-10-29-mithril-a-stronger-and-lighter-blockchain-for-better-efficiency.008.jpeg)

Hình 1. Các giai đoạn hoạt động của Mithril

**Parameter setup**

To set up a Mithril protocol, users need to:

- fix the group setting where the cryptography will take place
- select the index range *M*, which is the number of elections they will be holding
- set the quorum size *K*, which is the number of election winners that need to sign a signature for it to be accepted.

It is also important to provide a reference string for the proof system. This is possible in a transparent manner and does not require any high trust assumptions.

**Initialization**

Trong giai đoạn này, người dùng nên *cập nhật phân phối trạng thái.* Điều này cho phép mọi bên liên quan biết họ đang nắm giữ cổ phần nào. Sau đó, mỗi bên liên quan có trách nhiệm *đăng ký khóa của họ*. Điều này có thể xảy ra trên chuỗi (On-Chain) hoặc ngoài chuỗi (Off-Chain).

Cuối cùng, người dùng cần *phân phối cổ phần và nén các khóa kiểm tra của họ*. Điều này được thực hiện bằng cách sử dụng [Merkle Tree](https://docs.cardano.org/glossary/#merkletree). Chức năng này cho phép các chữ ký Mithril được xác minh dựa trên một hàm băm duy nhất đại diện cho Merkle Tree đó. Vì vậy, kích thước trạng thái cần thiết lập để xác minh chữ ký có thể được giữ ở mức thấp.

**Hoạt động**

Trong khi làm việc với chuỗi, người dùng có thể tạo, tổng hợp và xác minh chữ ký Mithril. Việc tạo chữ ký liên quan đến việc người dùng cố gắng kiểm tra xem chữ ký mà họ tạo ra có thực sự là người chiến thắng ở một trong các lần quay xổ số được tổ chức song song hay không. Nếu đúng, người dùng sẽ phát tán đi chữ ký của họ. Nếu có đủ chữ ký hỗ trợ một thông điệp cụ thể qua các lần quay xổ số khác nhau, chúng có thể được tổng hợp thành một chữ ký Mithril duy nhất. Sau đó, nó có thể được truyền phát và xác minh bởi bất kỳ ai chỉ sử dụng chuỗi tham chiếu cho hệ thống bằng chứng và phân phối cổ phần băm Merkle Tree rất nhanh.

For example, a single user can create a signature with Mithril as follows:

![Mithril signature](img/2021-10-29-mithril-a-stronger-and-lighter-blockchain-for-better-efficiency.009.jpeg)

Figure 2. Mithril signature creation

Đầu tiên, người dùng sẽ kiểm tra số cổ phần mà họ nắm giữ và chuyển nó qua một chức năng tính điểm để nhận được ngưỡng điểm *T* của họ. Sau đó, họ sẽ cố gắng tạo ra một chữ ký ứng viên *S.* Đối với mỗi chỉ số, họ sẽ đánh giá xem chữ ký ứng viên có tương ứng với thông điệp mà họ vừa ký hay không. Số chỉ số của xổ số mà họ đang kiểm tra cũng phải tạo ra một giá trị điểm nhỏ hơn ngưỡng *T* của họ. Nếu điều đó là đúng, thì chữ ký ứng viên mà họ đưa ra đã thực sự trúng xổ số trên số chỉ số cụ thể đó. Nếu không, họ sẽ thực hiện lần tiếp theo.

Sau khi thử tất cả các chỉ số có thể có, người dùng có thể sẽ có một hoặc nhiều chỉ số mà chữ ký *S* của họ là hợp lệ. Đối với mỗi chỉ số đó, họ có thể xuất ra một chữ ký riêng bao gồm chữ ký ứng viên, số chỉ số hợp lệ và bằng chứng xác minh rằng điểm của họ phù hợp với số cổ phần đã đăng ký.

## **Kiến trúc mạng lưới**

Triển khai Mithril trên Cardano, chúng tôi có thể biểu diễn tương tác phần mềm như sau:

![Mithril network architecture](img/2021-10-29-mithril-a-stronger-and-lighter-blockchain-for-better-efficiency.010.jpeg)

Figure 3. Mithril network architecture

A high-level representation of software around a stake pool operator (SPO) includes its connection to the Cardano peer-to-peer (P2P) network, the Mithril nodeâ€™s P2P network, and the Mithril client connected to the node run by an SPO.

The Mithril node at the SPO platform accesses its verified blockchain at the local storage and runs the protocol to produce Mithril certificates that are kept at the Mithril storage. Produced Mithril certificates can be verifiably synchronized across the whole network. Thus, the SPO can share both the full Cardano blockchain *and* the list of valid Mithril certificates for it. When the Mithril client connects to the network, it requests a list of Mithril certificates and asks only for the longest chain of the Cardano blockchain.

Several SPOs can also participate in such a setting. The Mithril client will then verify that certificates fully confirm the obtained Cardano blockchain. The whole procedure is lightweight and will not require the involvement of significant network storage or computational resources. Moreover, Cardano full node sync and fast sync with Mithril procedures are not mutually exclusive â€“ they can be run in parallel. Mithril fast sync will be later confirmed by the full node sync.

## **Use cases**

Letâ€™s take a look at the use cases where Mithril applicability is highly beneficial.

Mithril boosts the efficiency of *full node clients* or applications such as [Daedalus](https://www.google.com/url?q=https://docs.cardano.org/cardano-components/daedalus-wallet&sa=D&source=editors&ust=1633506174851000&usg=AOvVaw1TSia4xDEiu6-d-ClvqO6a). It ensures fast and secure synchronization of the full node data, significantly improving time and required resources including computation, network exchange, and local storage while keeping high-level security guarantees.

Mithril cũng có thể áp dụng cho *các ứng dụng khách nhẹ và  ứng dụng di động*, đảm bảo cách tiếp cận không cần lòng tin. Một lợi thế đáng kể khác là sử dụng chữ ký Mithril để chạy các *Sidechain*. Blockchain chính có thể kết nối với các Sidechain khác nhau, thậm chí có thể có các giao thức đồng thuận khác nhau. Mithril có lợi ích trong việc xác minh trạng thái Blockchain mà tốn rất ít tài nguyên. Do đó, các chứng chỉ có thể xác thực trạng thái hiện tại của Blockchain cũng như tính đúng đắn của việc chuyển tiếp và lan truyền một cách an toàn.

Finally, stake-based voting applications and governance solutions can use Mithril regardless of the voting protocolâ€™s complexity. Mithril signatures can be utilized for secure and lightweight tally verification. This is also useful in governance when stakeholders go through a decentralized decision-making process and provide the final result in an easy and verifiable way.

## **Implementations**

Một số công ty đã quan tâm đến việc triển khai Mithril trong các giải pháp Blockchain của họ. [Galois](https://galois.com/research-development/), một công ty nghiên cứu và phát triển tiên tiến tập trung vào các phương pháp chính thức, mật mã và phần cứng, sẽ triển khai nguyên mẫu Mithril đầu tiên dựa trên nghiên cứu do IOHK thực hiện. Galois sẽ triển khai Mithril bằng ngôn ngữ lập trình Rust vì nó có tính năng tạo mẫu nhanh. Trước tiên, họ có kế hoạch trình bày các chữ ký nhỏ hơn với BulletProofs. Sau đó là các triển khai sẵn sàng cho quá trình sản xuất và cuối cùng là các bằng chứng chính thức về tính đúng đắn.

[Idyllic Vision](https://www.google.com/url?q=https://idyllicvision.com/%23/&sa=D&source=editors&ust=1633533919267000&usg=AOvVaw1sXpYwItx-H5CX6OgJ-wzT) is another company focused on building a self-sovereign identity protocol based on zero-knowledge proofs, a credential management system for organizations, and a mobile wallet for end users that supports interoperability between diverse society solutions. They are planning to implement the proof of concept of the Mithril node. In the following months, they will begin with creating a blueprint of solution architecture, defining a number of system components that should be developed and organically integrated into the existing infrastructure. This includes integration with the Mithril crypto library and the Cardano node, and a networking layer for communication between nodes. The result of this phase should be integrated into Cardano to enable fast bootstrapping of the node and support for extra functionality like lightweight clients as others.

Để tìm hiểu thêm, hãy đọc [nghiên cứu về Mithril](https://iohk.io/en/research/library/papers/mithrilstake-based-threshold-multisignatures/) và xem [bài thuyết trình của Hội nghị thượng đỉnh Cardano](https://summit.cardano.org/sessions/mithril-linking-together-a-stronger-and-lighter-blockchain).<br> <br>Bài này được dịch bởi Nguyễn Văn Tú <a class="_active_edit_href" href="https://iohk.io/en/blog/posts/2021/10/29/mithril-a-stronger-and-lighter-blockchain-for-better-efficiency/">với bài gốc</a><em><br>Dự án này được tài trợ bới Catalyst</em>
