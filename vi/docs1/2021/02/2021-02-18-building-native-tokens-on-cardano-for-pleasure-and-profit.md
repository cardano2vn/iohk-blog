# Xây dựng token gốc trên Cardano để mang lại niềm vui và lợi nhuận

### **Các tính năng mới trên Cardano sẽ cho phép người dùng chọn các công cụ đơn giản và mạnh mẽ để đưa tài sản của họ vào thực tế cuộc sống**

![](img/2021-02-18-building-native-tokens-on-cardano-for-pleasure-and-profit.002.png) 18 tháng 2 năm 2021 ![](img/2021-02-18-building-native-tokens-on-cardano-for-pleasure-and-profit.002.png) [Tim Harrison](tmp//en/blog/authors/tim-harrison/page-1/) ![](img/2021-02-18-building-native-tokens-on-cardano-for-pleasure-and-profit.003.png) 9 phút đọc

![Tim Harrison](img/2021-02-18-building-native-tokens-on-cardano-for-pleasure-and-profit.004.png)[](tmp//en/blog/authors/tim-harrison/page-1/)

### [**Tim Harrison**](tmp//en/blog/authors/tim-harrison/page-1/)

VP of Community &amp; Ecosystem

Communications

- ![](img/2021-02-18-building-native-tokens-on-cardano-for-pleasure-and-profit.005.png)[](mailto:tim.harrison@iohk.io "Email")
- ![](img/2021-02-18-building-native-tokens-on-cardano-for-pleasure-and-profit.006.png)[](https://uk.linkedin.com/in/timbharrison "LinkedIn")
- ![](img/2021-02-18-building-native-tokens-on-cardano-for-pleasure-and-profit.007.png)[](https://twitter.com/timbharrison "Twitter")
- ![](img/2021-02-18-building-native-tokens-on-cardano-for-pleasure-and-profit.008.png)[](https://github.com/timbharrison "GitHub")

![Building native tokens on Cardano for pleasure and profit](img/2021-02-18-building-native-tokens-on-cardano-for-pleasure-and-profit.009.jpeg)

With the â€˜Maryâ€™ protocol upgrade, which will be implemented using our [hard fork combinator](https://docs.cardano.org/en/latest/explore-cardano/what-is-a-hard-fork-combinator.html) technology, native tokens and multi-asset capability are coming to Cardano.

On February 3, we upgraded[the Cardano public testnet](https://iohk.io/en/blog/posts/2021/02/04/native-tokens-to-bring-new-utility-to-life-on-cardano/) to â€˜Maryâ€™ for final testing. We plan to deploy the Cardano update proposal to mainnet on February 24, which would therefore deploy ahead of the boundary of epoch 250 and take effect on March 1. If we need a few more days of testing, we'll deploy â€˜Maryâ€™ the following epoch instead, which will take a five-day period required for updates to take effect. â€˜Maryâ€™ has been successfully running on our testing environments for several weeks, so our confidence level remains high. As always, however, weâ€™ll follow a strict process (developed and honed over the previous Shelley and Allegra HFC events) to get this right.

Once the code is successfully deployed to mainnet, weâ€™ll release a new [Daedalus Flight ](https://iohk.io/en/blog/posts/2020/04/01/we-need-you-for-the-daedalus-flight-testing-program/)version for user testing, which will be our first Cardano wallet with integrated multi-asset capability. Once we are happy with wallet performance and usability, weâ€™ll deliver the Daedalus mainnet release bringing the full-fat native token experience to every Cardano user.

## **Tại sao cần có token gốc?**

Các token gốc sẽ mang lại khả năng hỗ trợ đa tài sản cho Cardano, cho phép người dùng tạo các token được xác định duy nhất (tùy chỉnh) và thực hiện các giao dịch với chúng trực tiếp trên blockchain Cardano.

Việc sử dụng token trong các hoạt động tài chính đang trở nên phổ biến hơn bao giờ hết. Nó giúp cắt giảm chi phí đồng thời với việc cải thiện tính minh bạch, tăng cường thanh khoản và tất nhiên, độc lập với các thực thể tập trung như các ngân hàng lớn. Token hóa là quá trình đại diện cho tài sản thực (ví dụ: tiền tệ fiat, cổ phiếu, kim loại quý và tài sản) ở dạng kỹ thuật số, có thể được sử dụng để tạo công cụ tài chính cho các hoạt động thương mại.

Cardano will provide many [tokenization options](https://iohk.io/en/blog/posts/2020/12/08/native-tokens-on-cardano/). With the â€˜Maryâ€™ upgrade, the ledgerâ€™s accounting infrastructure will process not only ada transactions but also transactions that simultaneously carry several asset types. Native support grants distinct advantages for developers as there is no need to create smart contracts to handle custom token creation or transactions. This means that the accounting ledger will track the ownership and transfer of assets instead, removing extra complexity and potential for manual errors, while ensuring significant cost efficiency.

**Tương lai và tiện ích**

Các nhà phát triển, doanh nghiệp và ứng dụng có thể tạo token mục đích chung (có thể thay thế) hoặc chuyên biệt (không thể thay thế) để sử dụng trong hoạt động thương mại hoặc kinh doanh. Chúng có thể bao gồm việc tạo token thanh toán tùy chỉnh hoặc phần thưởng cho các ứng dụng phi tập trung; stablecoin được chốt với các loại tiền tệ khác; hoặc các tài sản duy nhất đại diện cho tài sản trí tuệ. Tất cả những tài sản này sau đó có thể được mua bán, trao đổi hoặc được sử dụng để thanh toán cho các sản phẩm hoặc dịch vụ.

Không giống như token ERC-20 dựa trên các hợp đồng thông minh của Ethereum, việc theo dõi và hạch toán token tùy chỉnh trên Cardano được hỗ trợ bởi sổ cái. Vì token gốc không yêu cầu hợp đồng thông minh chuyển giá trị của chúng nên người dùng có thể gửi, nhận và ghi token của họ mà không phải trả phí giao dịch cần thiết cho hợp đồng thông minh hoặc thêm logic xử lý sự kiện để theo dõi giao dịch.

## **Làm việc với token gốc trên Cardano**

Trong việc tạo ra một [môi trường cho các token gốc](https://iohk.io/en/blog/posts/2020/12/09/native-tokens-on-cardano-core-principles-and-points-of-difference/) , chúng tôi đã tập trung vào sự đơn giản trong cách làm việc, khả năng chi trả và tất nhiên là cả vấn đề bảo mật.

Tùy thuộc vào sở thích và chuyên môn kỹ thuật, người dùng sẽ có thể chọn trong số ba cách để tạo, phân phối, trao đổi và lưu trữ token:

- **Giao diện dòng lệnh Cardano (Cardano command-line interface - CLI)**. Người dùng với tính nâng cao hiện có thể truy cập CLI thông qua môi trường thử nghiệm chuyên dụng. Chúng tôi sẽ triển khai CLI trên mainnet khi hard fork diễn ra.
- **A â€˜token builderâ€™ graphical user interface (GUI)**. This will follow the native token CLI launch, providing an easier way for creating tokens.
- **The Daedalus wallet**. Daedalus will provide support for sending and receiving custom-created tokens. Daedalus Flight will test native token functionality in March, which will be shortly followed by the mainnet release.

Hãy cùng tìm hiểu một chút về từng tùy chọn.

**Làm việc với Cardano CLI**

Các nhà phát triển nâng cao có thể sử dụng môi trường thử nghiệm token gốc để tạo tài sản (đúc) và gửi các giao dịch thử nghiệm đến các địa chỉ khác nhau.

Bản chất của làm việc với CLI giả định rằng một người nào đó quen thuộc với việc thiết lập và vận hành node trên Cardano và có kinh nghiệm làm việc với các giao dịch và quản lý địa chỉ và giá trị. Để tạo token gốc [bằng cách sử dụng Cardano CLI](https://docs.cardano.org/en/latest/native-tokens/getting-started-with-native-tokens.html) , bạn cần phải:

- Thiết lập và khởi động node trên Cardano
- Định cấu hình node chuyển tiếp để kết nối với môi trường thử nghiệm token gốc
- Bắt đầu tương tác với mạng (liên quan tới Cardano CLI)
- Construct a monetary policy script
- Tạo token bằng cách sử dụng tập lệnh chính sách tiền tệ
- Cuối cùng, gửi và ký các giao dịch để chuyển token giữa các địa chỉ.

Các hướng dẫn và bài tập về token gốc có sẵn trên [trang web tài liệu Cardano](https://docs.cardano.org/en/latest/native-tokens/learn-about-native-tokens.html) của chúng tôi có thể giúp các nhà phát triển đúc token, tạo chính sách tiền tệ và tìm hiểu cách thực hiện các giao dịch đa tài sản.

We are already seeing particular interest from stake pool operators for this. So far, hundreds of test tokens have been created, and we continue to improve the CLI based on feedback. We welcome your comments and encourage community testing.

**Trình tạo token: một GUI thân thiện giúp ích cho người dùng trong việc tạo token**

CLI yêu cầu một trình độ nhất định. Vì vậy, chúng tôi đã nghĩ ra các cách khác cho người ít thành thạo về kỹ thuật cũng có thể tạo ra token. Để đạt được điều này, chúng tôi dự định khởi chạy trình tạo token sau khi đã khởi chạy mainnet CLI.

Trình tạo token là một giao diện đồ họa giúp tạo token dễ dàng hơn. Nếu bạn quan tâm đến việc tạo token cho ứng dụng phi tập trung của mình, muốn mã hóa tài sản của bạn, tạo nên một bộ sưu tập NFT được đại diện như tài sản chuyên dụng hoặc bạn muốn tạo một stablecoin được gắn với giá trị của các loại tiền tệ khác, trình tạo token có thể giúp bạn làm điều đó .

Để tạo token, bạn chỉ cần điền vào:

- Tên của token (ví dụ: Hello World)
- Tên viết tắt của token (ví dụ: HEW)
- Icon của token (được tạo tự động)
- Tổng số token cần tạo (ví dụ: 1.000)
- Địa chỉ ví Cardano (dùng để lưu trữ các token mới được tạo).

Việc tự động tạo token cũng sẽ tự động tạo ra chính sách tiền tệ - bạn sẽ không cần phải tự mình xác định chính sách đó. Điều này hợp lý hóa việc tạo token và đơn giản hóa nó cho người dùng không chuyên về kỹ thuật.

![token builder dashboard](img/2021-02-18-building-native-tokens-on-cardano-for-pleasure-and-profit.010.png)

Hình 1. Trang tổng quan của trình tạo token nguyên mẫu

Initially, the token builder will be supporting only fungible token creation (while non-fungible tokens can be created using Cardano CLI). In time, weâ€™ll extend the functionality to allow creating non-fungible tokens and changing the monetary policy according to specific preferences. This means that users will be able to specify the conditions under which tokens are minted (or burned), or who has control over the asset supply, for example.

Finally, when tokens are minted, it will be possible to mint more by clicking the â€˜Mint moreâ€™ button. This can be done based on the same policy to create more tokens of the same kind, or you can create other tokens that represent different values based on a different policy. For example, you can create more Hello World tokens, or, starting from scratch, you can create 500 â€˜testâ€™ tokens that will be used for other purposes (these will have a different minting policy).

Trình tạo token nhằm mục đích giảm sự phức tạp của việc tạo token và cũng tập trung vào việc nâng cao và trình bày trực quan các quy trình chức năng. Kết quả là, chúng tôi mong muốn cung cấp khả năng hiển thị xung quanh tất cả các token được tạo, giá trị, số lượng và địa chỉ của chúng mà chúng đang được chuyển - tất cả ở cùng một nơi.

**Ví Daedalus**

Những người dùng không muốn tạo token của riêng mình nhưng muốn sử dụng token hiện có để thanh toán, mua hàng hoặc trao đổi, sẽ có thể sử dụng các ví như Daedalus và sau này là Yoroi.

Đội nhóm Daedalus tiếp tục làm việc để tích hợp phần phụ trợ của ví với giao diện người dùng để hỗ trợ chức năng token gốc. Sau đó, người dùng sẽ có thể giữ các token gốc trong ví của họ, gửi và nhận chúng như cách họ làm với ada.

Native tokens are uniquely identified by two hexadecimal numbers stored on-chain â€’ the Policy ID and the Asset Name. Considering that these numbers are not 'human-friendly', we have created fingerprints for easier identification of native tokens by users. Fingerprints are 44 character long alphanumeric strings beginning with the prefix 'token'.

Dữ liệu của token bổ sung được hiển thị trong giao diện người dùng của ví (tên, mô tả và từ viết tắt) sẽ được cung cấp bởi cơ quan đăng ký token Cardano, do Cardano Foundation quản lý từ đầu.

![Daedalus native tokens Mary UI](img/2021-02-18-building-native-tokens-on-cardano-for-pleasure-and-profit.011.png)

Hình 2. Giao diện người dùng token gốc Daedalus

**Vòng đời của token gốc**

Khi tất cả các thành phần cần thiết được triển khai, vòng đời của token gốc sẽ hoàn tất. Nó bao gồm năm giai đoạn:

- minting
- issuing
- using
- redeeming
- burning.

![Multi asset token life cycle](img/2021-02-18-building-native-tokens-on-cardano-for-pleasure-and-profit.012.png)

Hình 3. Các giai đoạn vòng đời của token gốc

Trong các giai đoạn này, người kiểm soát tài sản sẽ có thể xác định chính sách cho loại tài sản và ủy quyền cho các tổ chức phát hành token có thể đúc hoặc đốt token. Các nhà phát hành token sau đó có thể đúc token (ví dụ: cho các ứng dụng), duy trì lưu thông của chúng và phát hành chúng cho chủ sở hữu token. Cuối cùng, chủ sở hữu token (ví dụ: người dùng cá nhân hoặc sàn giao dịch) sẽ có thể gửi token cho người khác, sử dụng chúng để thanh toán hoặc đổi trả khi họ đã sử dụng xong.

## **Tiếp theo là gì?**

We launched the testing environment in December 2020, laying the foundation for native token development. We also added a staging environment to enable initial testing by exchanges and stake pool operators. It features a faucet and allows a network of nodes to be built while connecting to the relays.

Hãy theo dõi [cập nhật trạng thái Cardano](https://roadmap.cardano.org/en/status-updates/) của chúng tôi để nắm được tiến trình hàng tuần. Khi chúng tôi mở rộng khả năng của các token gốc, thêm các công cụ và giao diện, chúng tôi sẽ cung cấp tài liệu và hướng dẫn để khuyến khích mọi người tham gia. Đương nhiên, với cơ sở là mã nguồn mở và chúng tôi đã thấy một số dự án thú vị xuất hiện mang tính cộng đồng (ví dụ: xung quanh [các bộ sưu tập kỹ thuật số](https://www.cnft.io/) ).

Vì vậy, rất nhiều điều sẽ xảy ra vào cuối tháng 2 và đầu tháng 3, từ thử nghiệm cuối cùng và sự kiện HFC, đến các token gốc trên Cardano trong trải nghiệm ví Daedalus hoàn toàn mới. Quãng thời gian thú vị đang chờ chúng ta ở phía trước!

*Tìm hiểu thêm bằng cách tham gia cùng các thành viên cộng đồng khác để thảo luận về token gốc trong [phần dành riêng cho token](https://forum.cardano.org/c/developers/cardano-tokens/150) của Diễn đàn Cardano. Và đừng quên đăng ký [chương trình devnets](https://input-output.typeform.com/c/OJsf0XcD) của chúng tôi.*

*Additional technical input by Olga Hryniuk.*
