# Tổng quan về nghiên cứu cho phép hỗ trợ hợp đồng thông minh trên Cardano

### **Phần 2 - Cùng xem xét kỹ lưỡng hơn nghiên cứu của Cardano. Dưới đây là thông tin thêm về mô hình EUTXO của Cardano và cách nó tạo điều kiện để các hợp đồng thông minh trở nên hiệu quả hơn**

![](img/2022-06-23-overview-of-the-research-enabling-smart-contract-support-on-cardano.002.png) 23 tháng 6 năm 2022 ![](img/2022-06-23-overview-of-the-research-enabling-smart-contract-support-on-cardano.002.png) [Olga Hryniuk](/en/blog/authors/olga-hryniuk/page-1/) ![](img/2022-06-23-overview-of-the-research-enabling-smart-contract-support-on-cardano.003.png) 6 phút đọc

![Olga Hryniuk](img/2022-06-23-overview-of-the-research-enabling-smart-contract-support-on-cardano.004.png)[](/en/blog/authors/olga-hryniuk/page-1/)

### [**Olga Hryniuk**](/en/blog/authors/olga-hryniuk/page-1/)

Technical Writer

Marketing &amp; Communications

- ![](img/2022-06-23-overview-of-the-research-enabling-smart-contract-support-on-cardano.005.png)[](https://www.linkedin.com/in/olga-hryniuk-1094a3160/ "LinkedIn")
- ![](img/2022-06-23-overview-of-the-research-enabling-smart-contract-support-on-cardano.006.png)[](https://github.com/olgahryniuk "GitHub")

![Tổng quan về nghiên cứu cho phép hỗ trợ hợp đồng thông minh trên Cardano](img/2022-06-23-overview-of-the-research-enabling-smart-contract-support-on-cardano.007.png)

Our previous [blog post](https://iohk.io/en/blog/posts/2022/06/10/cardanos-foundational-research-overview/) discussed the research underpinning some of the core elements of Cardano, including staking, delegation, and reward sharing. This time, we outline the papers that helped establish a functional smart contract platform for decentralized application (DApp) development – enabled by the [Extended Unspent Transaction Output](https://iohk.io/en/blog/posts/2021/03/11/cardanos-extended-utxo-accounting-model/) (EUTXO) accounting model.

## **UTXO vs mô hình dựa trên tài khoản**

Bitcoin and Ethereum are among the most popular blockchains nowadays. They use two rather different ledger accounting models to track the distribution and ownership of users' funds. These models are Bitcoin's Unspent Transaction Output (UTXO) model and the account-based model, as employed by Ethereum among other blockchains.

Mô hình UTXO đảm bảo tính bảo mật cốt lõi của các hoạt động tài chính. Xét về ngữ nghĩa, UTXO tồn tại trong một môi trường điện toán phân tán và phức tạp, nó bị hạn chế trong việc hỗ trợ các hợp đồng thông minh. Ethereum đã chọn mô hình dựa trên tài khoản một cách rõ ràng để tạo điều kiện cho các hợp đồng thông minh dễ dàng phát huy tính hiệu quả hơn.

Addressing the question of whether it is possible to have expressive smart contracts while keeping the semantic simplicity of the UTXO model, IOG researchers came up with ‘[The Extended UTXO Model](https://iohk.io/en/research/library/papers/the-extended-utxo-model/)’ and ‘[Native Custom Tokens in the Extended UTXO Model](https://iohk.io/en/research/library/papers/native-custom-tokens-in-the-extended-utxo-model/)’ solutions. Both research papers were published in 2020 and fully describe the EUTXO model implemented on Cardano.

Manuel Chakravarty, nhà khoa học Lambda và kiến trúc sư Plutus tại Input Output Global, Inc. cho biết:

The UTXO ledger model, battle-tested by Bitcoin, remains the gold standard for security and scalability. We created the Extended UTXO (EUTXO) model to gain the level of smart contract expressiveness pioneered by Ethereum, while still maintaining UTXO's unrivaled security and scalability. We simply wanted the best of both worlds!

Bài nghiên cứu 'Mô hình UTXO mở rộng' chứng minh khả năng của EUTXO trong việc liên tục duy trì trạng thái của hợp đồng và sử dụng cùng một mã hợp đồng dựa theo toàn bộ chuỗi giao dịch. Một tính năng mạnh mẽ khác của mô hình EUTXO là các khoản phí cần thiết cho một giao dịch hợp lệ có thể được dự đoán chính xác trước khi đăng tải. Đây là một tính năng độc đáo được thúc đẩy bởi [thiết kế của mô hình EUTXO](https://iog.io/en/blog/posts/2021/09/06/no-surprises-transaction-validation-on-cardano/) , không có trong các mô hình dựa trên tài khoản.

### **Plutus**

Hợp đồng thông minh là động lực thúc đẩy thực hiện giao dịch trên Cardano. Họ có thể tự thực hiện nên không bị phụ thuộc vào bên thứ ba.

At the ACM SIGPLAN International Conference on Functional Programming (ICFP'19), [Manuel Chakravarty discussed functional blockchains](https://www.youtube.com/watch?v=zXy4kxUlUmY) and, in particular, presented Plutus as a functional approach to smart contracts:

Moving fast and breaking things isn’t the right way to build a blockchain platform. Broken things can’t be fixed easily. Hence, Plutus was built on the solid mathematical foundation of functional programming. It is a programming platform for smart contracts, which includes elements such as Haskell libraries to write smart contracts, a compiler from Haskell to Plutus Core on-chain code, and various tools to assist development.

Hầu hết các nền tảng lập trình blockchain phụ thuộc vào một ngôn ngữ lập trình, chẳng hạn như Solidity của Ethereum. Plutus đã được hiện thực hóa trên nền của Haskell. Việc lựa chọn Haskell đã cho phép các nhóm nghiên cứu và kỹ thuật của IOG sử dụng lại cơ sở hạ tầng, thư viện và công cụ Haskell với hồ sơ theo dõi đã được thiết lập cho phần mềm có tính đảm bảo cao. Haskell tạo điều kiện cho mã trở nên ngắn gọn và có thể tái sử dụng, đồng thời đơn giản hóa việc lập luận, kiểm tra và sử dụng các phương pháp chính thức để đạt được mức độ bảo mật mong muốn. Các phương pháp chính thức, là hình thức lập luận nghiêm ngặt nhất về tính chính xác của mã, được các hợp đồng thông minh có giá trị cao đặc biệt quan tâm và được hỗ trợ tốt bởi mô hình lập trình chức năng.

IOG research and engineering teams delivered Plutus smart contracts based on such papers as ‘[The Extended UTXO Model](https://iohk.io/en/research/library/papers/the-extended-utxo-model/)’, ‘[Native Custom Tokens in the Extended UTXO Model](https://iohk.io/en/research/library/papers/native-custom-tokens-in-the-extended-utxo-model/)’, ‘[Unraveling recursion: compiling an IR with recursion to System F](https://iohk.io/en/research/library/papers/unraveling-recursioncompiling-an-ir-with-recursion-to-system-f/)’, and ‘[System F in Agda, for fun and profit](https://iohk.io/en/research/library/papers/system-f-in-agdafor-fun-and-profit/)’. Together these papers establish Cardano's smart contract-enabled ledger model as well as the on-chain representation of contract code as so-called lambda terms. ’System F in Agda, for fun and profit’ includes a rigorous mathematical definition, which was computer-checked with the help of the Agda theorem prover.

Plutus hiện là một nền tảng lập trình sống động và đang hỗ trợ phát triển các hợp đồng thông minh trên Cardano. Nhóm giáo dục IOG cũng đã khởi động chương trình Plutus Pioneer (chương trình Tiên phong của Plutus) để tuyển dụng và đào tạo các nhà phát triển ngôn ngữ lập trình Plutus cho hệ sinh thái Cardano. Bạn có thể [tìm hiểu thêm về chương trình tại đây](https://testnets.cardano.org/en/plutus-pioneer-program/) .

### **Marlowe**

Trong khi Plutus là một ngôn ngữ lập trình hợp đồng thông minh chức năng, Marlowe là một nền tảng dựa trên web để xây dựng và chạy các hợp đồng thông minh tài chính với chi phí thấp mà không cần phải hiểu biết nhiều về lập trình. Nó mở ra một loạt các cơ hội cho những người không phải lập trình viên có thể thực hiện các hợp đồng đơn giản và được tối ưu hóa cho các giao dịch tài chính.

Bài báo nghiên cứu đầu tiên trình bày về Marlowe, ' [Marlowe: các hợp đồng tài chính trên blockchain](https://iohk.io/en/research/library/papers/marlowefinancial-contracts-on-blockchain/) ', được xuất bản vào năm 2018. Bài báo này khám phá thiết kế của một ngôn ngữ dành riêng cho mục đích thực hiện các hợp đồng tài chính. Nó trình bày ngữ nghĩa thực thi của Marlowe trong Haskell, một ví dụ về Marlowe trong thực tế và mô tả công cụ cho phép người dùng tương tác trong trình duyệt với các mô phỏng hợp đồng Marlowe.

Sau đó, vào năm 2020, nhóm nghiên cứu của IOG đã xuất bản một bài báo về ' [Phân tích tính hiệu quả của các hợp đồng Marlowe](https://iohk.io/en/research/library/papers/efficient-static-analysis-of-marlowe-contracts/) ', trình bày tóm tắt về công việc tối ưu hóa phân tích các hợp đồng Marlowe. Tiếp theo là ' [Marlowe: thực hiện và phân tích các hợp đồng tài chính trên blockchain](https://iohk.io/en/research/library/papers/marloweimplementing-and-analysing-financial-contracts-on-blockchain/) ' để mô tả việc triển khai Marlowe trên Cardano và môi trường mô phỏng và phát triển dựa trên web của Marlowe Playground (Sân chơi Marlowe). Bài báo cũng chỉ ra rằng các hợp đồng Marlowe có thể được phân tích toàn diện trước khi thực hiện chúng, do đó cung cấp sự đảm bảo chắc chắn cho những người tham gia hợp đồng.

Marlowe is already available for people to try out within the [Marlowe Playground](https://playground.marlowe.iohkdev.io/#/) – a browser-based sandbox environment where you can develop, simulate, and test the process of writing smart contracts. IOG is currently preparing for a Marlowe testnet launch and will use the [Marlowe Pioneers Program](https://pioneers.marlowe-finance.io/) to gather feedback and use cases across the Marlowe suite of products. The team has recently delivered the [Marlowe CLI tool](https://iohk.io/en/blog/posts/2022/04/19/introducing-the-new-command-line-interface-tool-for-marlowe/) to enable users to submit transactions and interact with Marlowe contracts using a command line interface. When launched on mainnet, Marlowe contracts will open up a range of DeFi capabilities.

*Now that we have discussed the characteristics of Cardano’s EUTXO model and how it facilitates smart contract development on Cardano, we will further discuss the research that enabled multi-asset support. Stay tuned for the next blog post!*
