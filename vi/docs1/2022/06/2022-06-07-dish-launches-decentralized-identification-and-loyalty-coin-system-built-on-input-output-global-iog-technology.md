# DISH ra mắt hệ thống nhận dạng phi tập trung và đồng coin cho khách hàng thân thiết được xây dựng trên công nghệ của IOG

### **The initiative is part of a long-term collaboration between DISH and IOG to create innovative blockchain solutions to drive adoption of decentralized technologies into the DISH ecosystem**

![](img/2022-06-07-dish-launches-decentralized-identification-and-loyalty-coin-system-built-on-input-output-global-iog-technology.002.png) 7 June 2022![](img/2022-06-07-dish-launches-decentralized-identification-and-loyalty-coin-system-built-on-input-output-global-iog-technology.002.png)[ Fernando Sanchez](/en/blog/authors/fernando-sanchez/page-1/)![](img/2022-06-07-dish-launches-decentralized-identification-and-loyalty-coin-system-built-on-input-output-global-iog-technology.003.png) 4 mins read

![Fernando Sanchez](img/2022-06-07-dish-launches-decentralized-identification-and-loyalty-coin-system-built-on-input-output-global-iog-technology.004.png)[](/en/blog/authors/fernando-sanchez/page-1/)

### [**Fernando Sanchez**](/en/blog/authors/fernando-sanchez/page-1/)

Technical Writer

Marketing and Communications

- ![](img/2022-06-07-dish-launches-decentralized-identification-and-loyalty-coin-system-built-on-input-output-global-iog-technology.005.png)[](mailto:fernando.sanchez@iohk.io "Email")
- ![](img/2022-06-07-dish-launches-decentralized-identification-and-loyalty-coin-system-built-on-input-output-global-iog-technology.006.png)[](https://www.linkedin.com/in/linkedinsanchezf/ "LinkedIn")

![DISH launches decentralized identification and loyalty coin system built on Input Output Global (IOG) technology](img/2022-06-07-dish-launches-decentralized-identification-and-loyalty-coin-system-built-on-input-output-global-iog-technology.007.jpeg)

Tập đoàn DISH đã thực hiện bước đầu tiên hướng tới việc ra mắt hệ thống nhận dạng phi tập trung và đồng coin cho khách hàng thân thiết được xây dựng trên công nghệ blockchain được thiết kế và phát triển bởi Input Output Global (IOG). Bước đầu tiên này cho phép các khả năng blockchain trong cơ sở hạ tầng của DISH thông qua các dịch vụ nhận dạng của Atala PRISM và các tính năng tài sản gốc của Cardano.

The end objective of this collaboration is to create a robust and fully digital and decentralized identification and loyalty framework built first on the Cardano blockchain.

DISH is a satellite television company headquartered in Colorado, United States. During the 2021 Cardano Summit, [IOG's CEO Charles Hoskinson announced](https://youtu.be/MPobkiSbx5M) that both companies would cooperate to create novel blockchain solutions to drive adoption of decentralized ledger technology.

This MVP is part of the CRONUS project, a long-term, innovative collaboration between IOG and DISH to make blockchain a core part of the DISH ecosystem and its overall consumer strategy going forward.

## **How does the CRONUS MVP work?**

MVP (sản phẩm khả dụng) đại diện cho sự khởi đầu của hành trình hướng tới việc tạo ra một hệ thống khách hàng thân thiết dựa trên mã thông báo được hỗ trợ bởi công nghệ blockchain. Bước đầu tiên trong hành trình đó là cho phép đúc mã thông báo khách hàng thân thiết trên chuỗi khối Cardano để nhân đôi số dư đồng tiền trung thành trong chương trình khách hàng thân thiết BoostOne của DISH.

Cardano tracks the balance of loyalty coins or Boostcoinâ„¢ accrued by customers, and mints or burns the loyalty tokens accordingly. The loyalty token balance is adjusted in a nightly batch operation, using a DISH-controlled wallet. IOG will not have access to this wallet. To avoid including any personally identifiable customer information, the MVP leverages the Atala SDK library to generate an unpublished decentralized identifier (DID).

## **Core MVP capabilities**

Khi ra mắt, MVP sẽ cung cấp các khả năng sau:

- Dữ liệu sổ cái khách hàng thân thiết theo dõi Boostcoins và hiển thị số lượng mã thông báo khách hàng thân thiết cần được đúc/đốt để số dư mã thông báo khớp với số dư đồng loyalty coin.
- API để đúc và kiểm soát token trên mạng chính Cardano.
- Cardano mainnet là nơi token khách hàng thân thiết được đúc và đốt theo dữ liệu được cung cấp bởi cơ sở dữ liệu sổ cái khách hàng thân thiết.
- DISH organizational wallet that holds all Boostcoins. The wallet executes minting and burning transactions during nightly batch updates.
- Generation of an unpublished DID for each customer. This DID is mapped in the customer master, which sits outside the MVP. DIDs are created with the Atala SDK library but are not themselves published on the Cardano blockchain.

The MVP includes two APIs:

1. API để đúc và kiểm soát các tokens trên chuỗi khối mainnet của Cardano

- Đúc/Đốt token khách hàng thân thiết
- Query total number of tokens in circulation

1. API for the loyalty ledger database

- Add loyalty coins to a customerâ€™s account
- Deduct loyalty coins from a customerâ€™s account
- Query loyalty coin balance and transactions of each customer

This MVP represents the first step in a major blockchain adoption journey. This first step is about **blockchain enablement**. DISH will become a participant in the Cardano Ecosystem by running various nodes, issuing DIDs, minting and burning native assets. The next stage will involve **blockchain adoption** where DISH users will be slowly introduced to the different aspects of the blockchain ecosystems. Including but not limited to having a wallet.

## **MVP: user stories**

The CRONUS MVP opens up a range of opportunities, both for DISH itself and for its development partner, IOG. But ultimately, the DISH customer base will get the greatest benefit. The MVP enables BoostOne app users to see their total loyalty coin balance and transactions, for example.

The MVP also enables greater control for backend BoostOne administrators, as they can:

- Thêm hoặc xóa đồng coin trung thành khỏi tài khoản của người dùng ứng dụng BoostOne nếu cần.
- Mint or burn tokens on the Cardano Mainnet as needed to provide BoostOne customers with loyalty coins they have earned.
- Có quyền kiểm soát duy nhất đối với ví token khách hàng thân thiết của Dish vì khách hàng không thể tương tác trực tiếp với token khách hàng thân thiết.
- Reference an unpublished DID to identify the customer associated with a loyalty coin account.

## **Conclusion**

MVP tiên phong này thể hiện một bước tiến quan trọng đối với việc tích hợp các hệ thống hỗ trợ blockchain vào hệ sinh thái viễn thông và đặc biệt để tạo ra các chương trình khách hàng thân thiết được cung cấp bởi các sổ cái phi tập trung.<br><br>Bài này được dịch bởi Lê Nguyên với [nguồn tại đây]( https://iohk.io/en/blog/posts/2022/06/07/dish-launches-decentralized-identification-and-loyalty-coin-system-built-on-input-output-global-iog-technology/ )<br>Dự án này được tài trợ bới Catalyst
