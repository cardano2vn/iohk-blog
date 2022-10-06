# Những điều bạn cần biết về Plutus

### **Các nhà phát triển hiện đang chuẩn bị cho sự xuất hiện của hợp đồng thông minh Cardano, được kích hoạt bởi Plutus và nâng cấp giao thức Alonzo**

![](img/2021-04-13-plutus-what-you-need-to-know.002.png)13 tháng 4 năm 2021![](img/2021-04-13-plutus-what-you-need-to-know.002.png) [Lars Brünjes](tmp//en/blog/authors/lars-brunjes/page-1/)![](img/2021-04-13-plutus-what-you-need-to-know.003.png) 9 phút đọc

![Lars Brünjes](img/2021-04-13-plutus-what-you-need-to-know.004.png)[](tmp//en/blog/authors/lars-brunjes/page-1/)

### [**Lars Brünjes**](tmp//en/blog/authors/lars-brunjes/page-1/)

Education Director

Education

- ![](img/2021-04-13-plutus-what-you-need-to-know.005.png)[](mailto:lars.bruenjes@iohk.io "Email")
- ![](img/2021-04-13-plutus-what-you-need-to-know.006.png)[](https://www.linkedin.com/in/dr-lars-br%C3%BCnjes-1640993b "LinkedIn")
- ![](img/2021-04-13-plutus-what-you-need-to-know.007.png)[](https://twitter.com/LarsBrunjes "Twitter")
- ![](img/2021-04-13-plutus-what-you-need-to-know.008.png)[](https://github.com/brunjlar "GitHub")

![Plutus: what you need to know](img/2021-04-13-plutus-what-you-need-to-know.009.jpeg)

Trong bài đăng trên Blog trước, chúng tôi đã thảo luận về [*Alonzo*](https://iohk.io/en/blog/posts/2021/04/08/smart-contracts-%E2%80%93-here-we-come/) - cái tên được đặt cho bản nâng cấp giao thức sẽ hỗ trợ hợp đồng thông minh trên Cardano. Alonzo sẽ thiết lập cơ sở hạ tầng và thêm các công cụ để phát triển chức năng của hợp đồng thông minh bằng cách sử dụng Plutus.

Nền tảng Plutus cung cấp ngôn ngữ hợp đồng thông minh gốc cho Cardano Blockchain. Để hiểu và thành thạo Plutus, chúng ta phải hiểu ba khái niệm:

- *Mô hình UTXO mở rộng (EUTXO)*
- *Plutus Core* - phần 'trên chuỗi' của Plutus.
- *Khung ứng dụng Plutus (PAF - Plutus Application Framework )* - một phần 'ngoài chuỗi' của Plutus cho phép tương tác với hợp đồng thông minh.

Plutus contracts consist of parts that run on the blockchain (on-chain code) and parts that run on a user’s machine (off-chain or client code). Both the on-chain and off-chain code are written in Haskell, and Plutus smart contracts are effectively Haskell programs. Off-chain code can be written using PAF and this code is then compiled by the GHC (Glasgow Haskell Compiler), whereas on-chain code (written using the Plutus Core) is compiled by the Plutus compiler.

It is crucial to understand the relationship between these Plutus concepts and native tokens functionality to see how their interaction turns the latter into a more useful and powerful feature.

## **Mô hình UTXO mở rộng**

Cardano (like Bitcoin) uses the unspent (U) transaction (TX) output (O) accounting model. In the UTXO model, a *transaction* has *inputs* and *outputs*, where the **inputs** are unspent outputs from previous transactions. As soon as an output is used as input in a transaction, it becomes *spent* and can never be used again. The **output** is specified by an *address* (a public key or public key hash) and a *value* (consisting of an ada amount and optional, additional native token amounts). An output’s address determines which transactions are allowed to ‘unlock’ the output and use it as an input. A transaction must be *signed* by the owner of the private key corresponding to the address. Think of an address as a ‘lock’ that can only be ‘unlocked’ by the right ‘key’ ‒ the correct signature.

Mô hình EUTXO *mở rộng* mô hình này theo hai hướng:

1. Nó khái quát khái niệm 'địa chỉ' bằng cách sử dụng phép tương tự khóa và chìa khóa. Thay vì giới hạn khóa đối với khóa công khai và khóa đối với chữ ký, các địa chỉ trong mô hình EUTXO có thể chứa Logic tùy ý dưới dạng *tập lệnh*. Ví dụ như khi một node xác thực một giao dịch, node đó sẽ xác định xem giao dịch đó có được phép sử dụng một đầu ra nhất định làm đầu vào hay không. Giao dịch sẽ tra cứu tập lệnh được cung cấp bởi địa chỉ của đầu ra và sẽ thực thi tập lệnh nếu giao dịch có thể sử dụng đầu ra làm đầu vào.
2. Sự khác biệt thứ hai giữa UTXO và EUTXO là đầu ra có thể mang (hầu như) dữ liệu tùy ý ngoài một địa chỉ và giá trị. Điều này làm cho các tập lệnh trở nên mạnh mẽ hơn nhiều bằng cách cho phép chúng mang *trạng thái*.

When validating an address, the script will access the data being carried by the output, the transaction being validated, and some additional pieces of data called *redeemers*, which the transaction provides for every input. By looking up all this information, the script has enough context to give a ‘yes’ or ‘no’ answer in what can be highly complex situations and use cases.

Tóm lại, EUTXO mở rộng mô hình UTXO bằng cách cho phép các địa chỉ đầu ra chứa Logic phức tạp để quyết định giao dịch nào có thể mở khóa chúng và bằng cách thêm dữ liệu *tùy chỉnh* vào *tất cả* đầu ra.

Mô hình EUTXO cung cấp những lợi thế độc đáo so với các mô hình kế toán khác. Việc xác thực giao dịch thành công hay thất bại chỉ phụ thuộc vào bản thân giao dịch và các đầu vào của nó, *chứ không* phụ thuộc vào bất kỳ thứ gì khác trên Blockchain. Do đó, tính hợp lệ của giao dịch có thể được kiểm tra *ngoài chuỗi*, trước khi giao dịch được gửi lên Blockchain. Một giao dịch vẫn có thể không thành công nếu một số giao dịch khác đồng thời sử dụng đầu vào mà giao dịch đang mong đợi, nhưng nếu tất cả các đầu vào vẫn còn, giao dịch được *đảm bảo* thành công.

Điều này trái ngược với mô hình dựa trên tài khoản (được Ethereum sử dụng), trong đó một giao dịch có thể không thành công khi thực hiện đến giữa tập lệnh. Điều này không bao giờ có thể xảy ra trong EUTXO. Ngoài ra, chi phí thực hiện giao dịch có thể được xác định ngoài chuỗi trước khi lan truyền - một tính năng khác mà Ethereum không thể có.

Cuối cùng, do tính chất 'cục bộ' của xác thực giao dịch, mức độ song song cao là có thể xảy ra: về nguyên tắc, một node có thể xác thực các giao dịch song song, nếu các giao dịch đó không cố gắng sử dụng cùng một đầu vào. Điều này rất tốt cho cả hiệu quả và lý luận, đơn giản hóa việc phân tích các kết quả có thể xảy ra và chứng minh rằng 'không có gì xấu' có thể xảy ra. Bạn có thể tìm hiểu sâu hơn về [mô hình EUTXO trong bài đăng trên Blog trước](https://iohk.io/en/blog/posts/2021/03/12/cardanos-extended-utxo-accounting-model-part-2/) .

## **Plutus Core**

Để triển khai mô hình EUTXO, cần phải xác định rõ ràng điều khoản *tập lệnh* và *dữ liệu*. Các tập lệnh yêu cầu một ngôn ngữ tập lệnh xác định và được chỉ định rõ ràng. Điều quan trọng là phải xác định loại dữ liệu được gắn vào các đầu ra và được sử dụng làm Redeemer.

Đây là nơi *xuất hiện của Plutus Core*. Plutus Core là ngôn ngữ tập lệnh được Cardano sử dụng. Nó là một ngôn ngữ lập trình hàm đơn giản tương tự như Haskell và một tập hợp con lớn của Haskell có thể được sử dụng để viết các tập lệnh Plutus Core. Là người tạo hợp đồng, bạn không viết bất kỳ Plutus Core nào. Tất cả các chương trình Plutus Core đều được tạo bởi một Plugin trình biên dịch Haskell.

Những tập lệnh này sẽ được thực thi bởi các node trong quá trình xác thực giao dịch 'trực tiếp' trên chuỗi. Họ sẽ khóa các UTXO dưới dạng *tập lệnh trình xác thực* hoặc dưới dạng *các chính sách đúc tiền*, kiểm soát việc đúc và đốt Token gốc (xem bên dưới).

Dữ liệu của Redeemer là một kiểu dữ liệu (đại số) đơn giản có thể được định nghĩa dễ dàng trong Haskell. Đó cũng là một lý do tại sao Haskell là một lựa chọn tốt để viết các tập lệnh Plutus Core. Trên thực tế, một nhà phát triển hợp đồng thông minh sẽ viết các tập lệnh trình xác thực trong Haskell. Sau đó chúng sẽ được tự động [biên dịch thành Plutus Core](https://iohk.io/en/blog/posts/2021/02/02/plutus-tx-compiling-haskell-into-plutus-core/).

Các thư viện Haskell thích hợp giúp đơn giản hóa việc viết Logic xác thực bằng cách cung cấp các kiểu dữ liệu cốt lõi để kiểm tra các giao dịch trong quá trình xác thực. Bằng cách cung cấp nhiều hàm trợ giúp và mức trừu tượng cao hơn, nó cho phép người tạo hợp đồng tập trung vào Logic nghiệp vụ và không phải lo lắng quá nhiều về các chi tiết ở cấp độ thấp.

## **Khung ứng dụng Plutus (PAF)**

Trạng thái trên chuỗi của các tập lệnh trình xác thực chỉ có thể được sửa đổi bằng các giao dịch chi tiêu và tạo ra đầu ra tập lệnh. Khi viết một ứng dụng Plutus, chúng ta cần xem xét không chỉ phần trên chuỗi của ứng dụng (các tập lệnh Plutus Core) mà còn cả phần ngoài chuỗi để xây dựng và gửi các giao dịch.

Mã Code ngoài chuỗi được viết bằng Haskell giống như mã Code trên chuỗi. Bằng cách đó, chúng ta chỉ cần viết Logic nghiệp vụ một lần. Sau đó, chúng ta có thể sử dụng nó trong tập lệnh trình xác thực và trong mã Code để xây dựng các giao dịch chạy tập lệnh trình xác thực.

Nhiều ứng dụng cần theo dõi bộ UTXO để thay đổi các địa chỉ cụ thể. Vì vậy, nếu viết hợp đồng dưới dạng máy trạng thái (State Machine), chúng ta cần theo dõi đầu ra chưa sử dụng đại diện cho trạng thái hiện tại của máy và cập nhật trạng thái cục bộ khi thay đổi trạng thái trên chuỗi. Tương tự như vậy, nhiều ứng dụng cần giao tiếp với phần phụ trợ ví để truy cập vào tiền mã hoá mà chúng đang sử dụng cho các giao dịch.

PAF cung cấp khả năng truy cập dễ dàng vào các dịch vụ thường được các ứng dụng Plutus sử dụng. Các ứng dụng được triển khai bằng cách sử dụng thư viện của khuôn khổ có thể được chạy trên phần phụ trợ ứng dụng Plutus. Nó cung cấp hỗ trợ thời gian chạy để truy cập vào Blockchain và các mối quan tâm khác như tính bền bỉ, ghi nhật ký và giám sát. Các ứng dụng được viết trên PAF tự động cung cấp giao diện HTTP và WebSocket có thể được sử dụng để tương tác với ứng dụng từ trình duyệt Web.

## **Token gốc**

*Native tokens* became available on Cardano with February’s *Mary* hard fork. Any user can create their own tokens, and tokens can be sent and received freely, just like ada. Each native token comes with its own [*minting policy*](https://docs.cardano.org/en/latest/native-tokens/learn-about-native-tokens.html#minting-policy), which determines the conditions under which tokens can be minted and burnt.

Hiện tại, chính sách đúc tiền bao gồm sự kết hợp của các quy tắc đơn giản xác định *chữ ký* và *thời gian*. Ví dụ: một chính sách có thể nêu rõ rằng chỉ các giao dịch được ký bởi hai trong số năm chữ ký mới có thể được phép đúc hoặc đốt Token. Một chính sách khác có thể chỉ cho phép đúc tiền trước hoặc sau một khoảng thời gian cụ thể.

Mạnh mẽ như những Block được xây dựng cơ bản, chúng không bao gồm mọi mục đích sử dụng có thể tưởng tượng được. Ví dụ, mặc dù khó khăn, nhưng nó có thể mô hình hóa các Token không thể thay thế (NFT) bằng cách sử dụng các chính sách đơn giản. Điều này có thể được thực hiện bằng cách sử dụng một mốc thời gian để đúc một NFT, bằng cách giới hạn hoạt động đúc trong một thời điểm cụ thể. Nếu chỉ có một Token được đúc trước khi đạt đến thời điểm đó, thì về mặt kỹ thuật, Token là không thể thay thế được (vì chỉ có một). Nhưng để kiểm tra điều này, chỉ cần kiểm tra chính sách đúc tiền thôi là chưa đủ. Chúng ta cần phải xem xét lịch sử đúc của Token để đảm bảo rằng nó thực sự chỉ được đúc một lần.

With the deployment of Plutus, users will be able to write minting policies using Plutus core. During minting or burning, the Plutus Core policy script will be executed in the context of the minting or burning transaction, and the script will have to approve or forbid the action. This will further accelerate the growth of NFTs on Cardano by enabling the creation of much more complex minting policies, and allowing the creation of NFTs in a trustless manner.

Alonzo is being gradually deployed to the mainnet via several testnets, so our partners and [Plutus pioneers](https://iohk.io/en/blog/posts/2021/04/01/everything-you-need-to-know-about-our-new-plutus-pioneer-program/) will be able to test Plutus Core by writing applications on Cardano throughout May and June prior to a code freeze. This will also be the period of quality assurance and user acceptance testing by exchanges to ensure that the platform is fully ready at the time of the Alonzo mainnet upgrade. If you are a developer and want to learn more about Plutus, consider joining a [future pioneer cohort](https://developers.cardano.org/en/plutus-pioneer-program/). Alternatively, take a look at [Plutus GitHub](https://github.com/input-output-hk/plutus) repositories, and engage in the discussions about Plutus at [Cardano Forum](https://forum.cardano.org/c/developers/cardano-plutus/148).

*I’d like to acknowledge Jann Müller for additional input and contribution to this blog post.*
