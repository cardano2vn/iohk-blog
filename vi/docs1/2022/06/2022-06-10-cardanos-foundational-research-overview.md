# Tổng quan nghiên cứu mang tính nền tảng của Cardano

### **Đây là bài đầu tiên trong một loạt các bài blog giúp chúng ta có cái nhìn rõ hơn về nghiên cứu mang tính nền tảng của Cardano**

![](img/2022-06-10-cardanos-foundational-research-overview.002.png) 10 June 2022![](img/2022-06-10-cardanos-foundational-research-overview.002.png)[ Olga Hryniuk](/en/blog/authors/olga-hryniuk/page-1/)![](img/2022-06-10-cardanos-foundational-research-overview.003.png) 5 mins read

![Olga Hryniuk](img/2022-06-10-cardanos-foundational-research-overview.004.png)[](/en/blog/authors/olga-hryniuk/page-1/)

### [**Olga Hryniuk**](/en/blog/authors/olga-hryniuk/page-1/)

Technical Writer

Marketing &amp; Communications

- ![](img/2022-06-10-cardanos-foundational-research-overview.005.png)[](https://www.linkedin.com/in/olga-hryniuk-1094a3160/ "LinkedIn")
- ![](img/2022-06-10-cardanos-foundational-research-overview.006.png)[](https://github.com/olgahryniuk "GitHub")

![Cardano's foundational research overview](img/2022-06-10-cardanos-foundational-research-overview.007.jpeg)

Since its inception in 2015, the Cardano project had one clear goal: to alter the way cryptocurrencies are designed and developed. Instead of having a single, authoritative whitepaper, the project combined a range of scientific design principles and engineering best practices to produce a solid, pioneering, research-based blockchain. The key ideas of Cardano development were presented in the '[Why Cardano](https://why.cardano.org/en/introduction/motivation/)' essay and the '[Cardano whiteboard](https://www.youtube.com/watch?v=Ja9D0kpksxw)' video by Charles Hoskinson. This research-driven approach positions Cardano uniquely among other blockchain platforms.

A set of the best practices, ideas, and contributions formed Cardano’s foundation for building a secure, decentralized, and scalable ledger. There is now a substantial body of research, represented by Input Output Global’s extensive [library of papers](https://iohk.io/research/library/), which at the time of writing numbers 139. Many of them have been peer-reviewed and accepted at top-tier academic conferences. [According to Google Scholar](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=ouroboros&btnG=), the original Ouroboros paper has been cited more than 1,200 times.

## **Research papers**

Charles Hoskinson, Giám đốc điều hành IOG, cho biết:

“Phi tập trung đặt ra những thách thức kỹ thuật lớn đối với các hệ thống tài chính trên toàn thế giới và IOG Research quan tâm đến từng vấn đề trong số đó.”

The vision of IOG Research is to be a leading institution in the academic study of blockchain infrastructures and fintech, and, more broadly, distributed systems secured by cryptographic techniques and incentivized through economic game theory. IOG has established its reputation for tackling difficult research questions in general, and for building formal and reliable foundations for the fintech blockchain infrastructure industry in particular.

Trong bài blog này, chúng tôi xem xét một số tài liệu nghiên cứu đặt nền móng cho Cardano.

### **Ouroboros**

Bài báo đầu tiên để thúc đẩy nghiên cứu của dự án là ‘[Ouroboros: A Provably Secure Proof-of-Stake Blockchain Protocol](https://eprint.iacr.org/2016/889.pdf)’, đã được đánh giá xét duyệt về mặt học thuật và được xuất bản tại Crypto 2017.

Sự đồng thuận là một phần quan trọng của các mạng blockchain. Ouroboros là giao thức đồng thuận bằng chứng cổ phần của Cardano. Cái tên 'Ouroboros' xuất phát từ một biểu tượng cổ đại tượng trưng cho sự vĩnh cửu và sự nối tiếp vô tận. Đối với Cardano, Ouroboros tượng trưng cho sự vĩnh cửu về mặt lý thuyết của một blockchain.

Since 2017, a number of Ouroboros protocol versions have been produced. Each ‘flavor’ of Ouroboros adds different features and functionality to support Cardano’s evolution. Starting with [Ouroboros Classic](https://eprint.iacr.org/2016/889.pdf), the ledger has undergone regular upgrades. Ouroboros Classic established the foundation for an energy-efficient proof-of-stake consensus protocol in a federated setting (Cardano’s Byron development theme). [Praos](https://eprint.iacr.org/2017/573.pdf), [Genesis](https://eprint.iacr.org/2018/378.pdf), and [Chronos](https://eprint.iacr.org/2019/838.pdf) were designed to ensure enhanced security in a fully permissionless setting. While Genesis improved the Praos protocol, Chronos will make Genesis even more robust when implemented. [This blog post](https://iohk.io/en/blog/posts/2022/06/03/from-classic-to-chronos-the-implementations-of-ouroboros-explained/) describes the evolution of Ouroboros in more detail.

Cùng với công nghệ độc đáo và các cơ chế được xác minh bằng toán học, Ouroboros nhận ra rằng một ‘[Nakamoto-style consensus](https://bitcoin.org/bitcoin.pdf)’ được điều chỉnh để làm bằng chứng cổ phần. Như chúng ta biết, Ouroboros cung cấp những đảm bảo an ninh mạnh mẽ giống như cơ chế đồng thuận bằng chứng công việc của Bitcoin, đồng thời đảm bảo hiệu quả tốt hơn về mặt tiêu thụ năng lượng. Thay vì dựa vào các thợ đào để giải quyết các vấn đề phức tạp về mặt tính toán để tạo ra một khối, những người tham gia bằng chứng cổ phần tạo ra và xác nhận các khối dựa trên cổ phần mà họ kiểm soát trong mạng lưới.

Trong bài đăng trên blog của mình, [The Ouroboros path to decentralization ](https://iohk.io/en/blog/posts/2020/06/23/the-ouroboros-path-to-decentralization/), [Giáo sư Aggelos Kiayias](https://iohk.io/en/blog/posts/2020/06/23/the-ouroboros-path-to-decentralization/), nhà khoa học hang đầu tại IOG và là chủ nhiệm về an ninh mạng và quyền riêng tư tại Đại học Edinburgh, nói:

Ouroboros is a decentralized ledger protocol that is analyzed in the context of both Byzantine and rational behavior. What makes the protocol unique is the combination of such design elements as stake, dynamic availability, trustless setting, and a reward-sharing incentive scheme.

### **Ủy quyền và nhóm cổ phần**

Việc chuyển đổi từ việc thiết lập liên kết sang phân quyền hoàn toàn yêu cầu một số điều chỉnh đối với giao thức. Điều cần thiết là phải cung cấp các phương tiện để quản lý tài khoản thích hợp (để kích hoạt kỹ thuật ủy quyền cổ phần) và khuyến khích sự tham gia.

Bài báo ‘[Account Management in Proof of Stake Ledgers](https://eprint.iacr.org/2020/525.pdf)’ – được xuất bản vào năm 2020 - khám phá những cách để tối đa hóa sự tham gia của những người nắm giữ cổ phần vào các hoạt động duy trì mạng lưới.

Typically, proof-of-stake blockchains depend – by nature – on the active participation of stakeholders. Stakeholders need to be constantly online to validate network transactions and produce new blocks. However, not every stakeholder has the ability or desire to constantly be online. To ensure that the system is robust and remains secure in such conditions, it is important to enable different types of stakeholder participation.

Stake delegation addresses this problem and allows a user to participate in network activities by delegating their stake to other participants. Stake delegation gives rise to [stake pools](https://iohk.io/en/blog/posts/2018/10/23/stake-pools-in-cardano/) – server nodes holding the staking rights of multiple stakeholders. The paper mathematically analyzes and defines the delegation technique and also implements core wallet properties to process secure payments.

Bài báo ‘[Reward Sharing Schemes for Stake Pools](https://arxiv.org/ftp/arxiv/papers/1807/1807.11218.pdf)’, cũng được xuất bản vào năm 2020, giới thiệu các cơ chế để khuyến khích những người nắm giữ cổ phần tham gia vào các hoạt động của họ.

The power of a stake pool comes from the accumulation of stake that is delegated to it. To avoid monopolization of network validation activities by one single pool, it is essential that network participants are incentivized to delegate to a large set of different pools.

The reward-sharing scheme describes a means to [properly incentivize](https://iohk.io/en/blog/posts/2020/11/30/blockchain-reward-sharing-a-comparative-systematization-from-first-principles/) stake pool operators (SPOs) and delegators for their activities such as transaction validation, block creation, etc. The research shows that the proposed reward mechanism steers the network to a desired level of decentralization and, in particular, offers protection against Sybil attacks. This is enabled by a so-called [pledging mechanism](https://iohk.io/en/blog/posts/2020/05/12/how-pledging-encourages-a-healthy-decentralized-cardano-ecosystem/), which greatly disincentivizes the formation of multiple stake pools controlled by a single real-world entity.

Mô hình khuyến khích của Cardano đã thiết lập một hệ sinh thái nơi những người tham gia hợp pháp được hưởng lợi từ việc tuân theo giao thức, từ đó cho phép blockchain Cardano hoạt động an toàn và hiệu quả. Kết quả là một sổ cái phi tập trung được điều hành một cách đáng tin cậy sẽ được bảo mật bằng các kỹ thuật mã hóa và cơ chế phần thưởng theo lý thuyết trò chơi.

*Stay tuned! In our next posts, we’ll take a closer look at some of the research papers that established the foundation for a functional smart-contract platform. Specifically, we’ll start with the research that enabled an extended UTxO model, explain what that actually means and how it enables the ledger to handle multi-assets and fees with a variety of benefits for users.*
