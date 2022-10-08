# Tiến đến cập nhật hợp đồng thông minh

### **Alonzo sẽ xây dựng dựa trên các nâng cấp token của Cardano để cung cấp cho các nhà lập trình công cụ để tạo các ứng dụng kinh doanh**

![](img/2021-04-08-smart-contracts-%E2%80%93-here-we-come.002.png) Ngày 8 tháng 4 năm 2021![](img/2021-04-08-smart-contracts-%E2%80%93-here-we-come.002.png)[ Olga Hryniuk](tmp//en/blog/authors/olga-hryniuk/page-1/)![](img/2021-04-08-smart-contracts-%E2%80%93-here-we-come.003.png) bài đọc 6 phút

![Olga Hryniuk](img/2021-04-08-smart-contracts-%E2%80%93-here-we-come.004.png)[](tmp//en/blog/authors/olga-hryniuk/page-1/)

### [**Olga Hryniuk**](tmp//en/blog/authors/olga-hryniuk/page-1/)

Technical Writer

Marketing &amp; Communications

- ![](img/2021-04-08-smart-contracts-%E2%80%93-here-we-come.005.png)[](https://www.linkedin.com/in/olga-hryniuk-1094a3160/ "LinkedIn")
- ![](img/2021-04-08-smart-contracts-%E2%80%93-here-we-come.006.png)[](https://github.com/olgahryniuk "GitHub")

![Tiến đến cập nhật hợp đồng thông minh](img/2021-04-08-smart-contracts-%E2%80%93-here-we-come.007.jpeg)

Vào đầu tháng 3, chúng tôi đã triển khai Mary - một bản nâng cấp giao thức đa tài sản cho phép người dùng tạo token duy nhất cho các giao dịch trên Cardano. Với việc giới thiệu [siêu dữ liệu giao dịch](https://iohk.io/en/blog/posts/2020/10/29/bringing-new-value-and-utility-to-the-cardano-blockchain/), sau đó là [khóa token](https://iohk.io/en/blog/posts/2020/12/02/goguen-brings-token-locking-to-cardano/) với Allegra vào tháng 12 và [tạo token gốc](https://iohk.io/en/blog/posts/2021/02/18/building-native-tokens-on-cardano-for-pleasure-and-profit/), chúng tôi đang tạo nền tảng để thiết lập Cardano trở thành nền tảng hợp đồng thông minh hàng đầu.

Alonzo, bản nâng cấp giao thức tiếp theo của chúng tôi, sẽ xây dựng dựa trên những khả năng này. Được triển khai bằng cách sử dụng công nghệ tổ hợp hard fork, Alonzo sẽ bổ sung hỗ trợ cho các hợp đồng thông minh - thỏa thuận kỹ thuật số - cho Cardano trong khoảng bốn tháng kể từ bây giờ. Nó sẽ mở ra cơ hội cho các doanh nghiệp và nhà lập trình, bằng cách cho phép tạo ra các hợp đồng thông minh và các ứng dụng phi tập trung (DApps) cho tài chính phi tập trung (DeFi).

When it came to naming these upgrades, we chose Allegra (Lord Byron's daughter) for token-locking, and Mary (the novelist and wife of Shelley) for multi-asset support. Alonzo comes from a more contemporary figure, Alonzo Church (1903-95). Church was a US mathematician and logician who worked on logic and the foundations of theoretical computer science. He is also known for inventing lambda calculus ‒ a formal system used to prove the unsolvability of the *Entscheidungsproblem*. Later, while working with fellow mathematician Alan Turing, they discovered that the lambda calculus and the Turing machine were equal in capabilities, demonstrating various mechanical processes for computations. One of the reasons for naming our smart contract upgrade after Church is that Plutus Core (the Cardano smart contract language) is a variation of lambda calculus.

## **Tại sao lại là hợp đồng thông minh?**

Hợp đồng thông minh đánh dấu giai đoạn tiếp theo trong quá trình phát triển của Cardano với tư cách là một sổ cái phi tập trung trên toàn thế giới. Khi hỗ trợ hoạt động kinh doanh hàng ngày, blockchain phải đảm bảo rằng các cá nhân có thể chuyển tiền của họ và thanh toán cho các sản phẩm một cách an toàn.

Smart contracts can be used to settle complex deals, hold funds in escrow, and secure movement of funds under predefined conditions. Cardano will allow DApps to interact with the ledger to record their activities and execute smart contracts. These digital agreements express the story of a transaction, specify where funds should go, and under what conditions they will be sent, executing a deal only when all the conditions are met. Alonzo will lay the foundation for Cardano to support such applications.

## **Giải quyết nhu cầu kinh doanh với Alonzo**

Trong khi hỗ trợ đa tài sản cho phép người dùng tạo ra các loại tiền tệ duy nhất đáp ứng nhu cầu kinh doanh, Alonzo giới thiệu một nền tảng đa năng để xây dựng các hợp đồng thông minh. Ví dụ, bạn có thể làm việc với các hoạt động sưu tầm, huy động vốn từ cộng đồng hoặc đấu giá.

Areas of exploration might include the deployment of escrow-based decentralized cryptocurrency exchanges (DEX), or the creation of complex applications supporting centralized stablecoins (track-and-trace applications for product provenance within a supply chain, for example). With token-locking, users will be able to issue utility tokens with vesting periods, meaning that a number of tokens can be locked or frozen to be released after a specific time.

## **Sức mạnh tập lệnh Plutus Core**

Với Alonzo, chúng tôi đang bổ sung các công cụ cần thiết và cơ sở hạ tầng để cho phép phát triển ứng dụng bằng nền tảng Plutus.

Áp dụng một cách tiếp cận nghiêm ngặt dựa trên các phương pháp chính thức và xác minh, Alonzo mở rộng tập lệnh ngôn ngữ cơ bản đa chữ ký (multisig) được sử dụng trong Cardano Shelley. Multisig sẽ được nâng cấp lên ngôn ngữ Plutus Core để có các tùy chọn tập lệnh mạnh mẽ và an toàn hơn. Sổ cái Alonzo triển khai [mô hình EUTXO](https://iohk.io/en/blog/posts/2021/03/12/cardanos-extended-utxo-accounting-model-part-2/), sử dụng Plutus Core để cung cấp tập lệnh mạnh mẽ.

Một nền tảng hợp đồng thông minh phải vừa an toàn vừa đáng tin cậy. Đó là lý do tại sao chúng tôi chọn Haskell làm cơ sở để viết các hợp đồng thông minh Plutus Core. Haskell là một ngôn ngữ cấp cao mà các nhà lập trình sẽ sử dụng để viết các đoạn mã và sau đó [biên dịch nó sang Plutus Core](https://iohk.io/en/blog/posts/2021/02/02/plutus-tx-compiling-haskell-into-plutus-core/).

Haskell đã xuất hiện từ năm 1987, nổi bật so với các ngôn ngữ lập trình khác về mức độ tin cậy cao. Viết bằng Haskell đảm bảo rằng các hợp đồng thông minh được lập trình để thực hiện chính xác những gì chúng được mong đợi và có thể kiểm tra độ chính xác trước khi thực hiện. Có nghĩa là các hợp đồng thông minh được xây dựng trên Cardano sẽ đơn giản và có khả năng chống lại các lỗ hổng bảo mật, điều này rất quan trọng đối với các ứng dụng xử lý giao dịch tự động hoặc di chuyển các khoản tiền lớn.

**Công cụ và API**

Các nhà lập trình sẽ có các công cụ chức năng để thử nghiệm và tùy chỉnh xác thực giao dịch trên Cardano. Thư viện API sẽ được mở rộng để cho phép triển khai và vận hành mã Plutus Core trên Cardano trong khi tương thích với ví và sổ cái.

Deploying Alonzo is a complex process. Once functional smart contracts are running on the mainnet, we will continue improving the off-chain infrastructure to deliver software development kits.

## **Bây giờ chúng ta đang ở đâu?**

![Lộ trình Alonzo](img/2021-04-08-smart-contracts-%E2%80%93-here-we-come.008.jpeg)

Hình 1. Lộ trình Alonzo. Bộ mã sẽ bị khóa trong bốn tuần trước khi phát hành

Trong tháng 3 và tháng 4, đội ngũ IO Global đã dần dần kết hợp các quy tắc Alonzo với node Cardano và bộ mã sổ cái. Khi quá trình tích hợp Alonzo với node hoàn tất, Cardano sẽ cung cấp các công cụ API hoạt động và hỗ trợ giao diện dòng lệnh (CLI).

Từ giữa tháng 4 đến đầu tháng 5, đội ngũ sẽ tiếp tục phát triển Plutus để khởi chạy testnet riêng. Trong giai đoạn này, các đối tác của chúng tôi (các nhà lập trình nâng cao) sẽ thử nghiệm nền tảng, tạo và triển khai các token không thể thay thế (NFT), các cửa hàng hoặc DApp chạy các hợp đồng thông minh trên Cardano. Quá trình này sẽ tập trung vào các cải tiến từng bước để đảm bảo rằng mọi thứ hoạt động hiệu quả.

In May, we’ll start working with our [Plutus pioneers](https://developers.cardano.org/en/plutus-pioneer-program/). These certified program trainees will continue testing the platform by writing Plutus applications and putting them into production for DApps and DeFi. During this phase, the team will be performing the ledger, node, and wallet backend integration. We will also be preparing and releasing documentation, including specification examples and developer guides.

Tháng 5 và tháng 6 sẽ là thời gian dành cho khâu đảm bảo chất lượng và thử nghiệm với người dùng, sau đó sẽ là đợt khóa tính năng kéo dài trong 4 tuần. Điều này sẽ cung cấp cho các sàn giao dịch và ví tiền mã hóa có thời gian để nâng cấp và chuẩn bị cho bản cập nhật giao thức Alonzo. Chúng tôi hy vọng nâng cấp Alonzo (hard fork) sẽ diễn ra vào cuối mùa hè và chúng tôi sẽ công bố một ngày chắc chắn trong chương trình Cardano360 vào tháng Tư.

Để biết lộ trình chi tiết hơn, hãy xem [bài thuyết trình Cardano360 tháng 3 của Charles Hoskinson](https://www.youtube.com/watch?v=ULBLgPgxtN8&t=5805s).

These are exciting times and we encourage you to stay tuned. The next blog post will delve into the relationship between the Plutus concepts that underpin Alonzo development. Meanwhile, the [developers’ website](https://developers.cardano.org/en/programming-languages/plutus/overview/) has more about programming with Plutus, Marlowe, and Glow.
