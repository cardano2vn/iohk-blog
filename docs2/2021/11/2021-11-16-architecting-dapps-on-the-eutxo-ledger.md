# Architecting DApps on the EUTXO ledger
### **Taking a closer look at ways of DApp architecture on Cardano**
![](img/2021-11-16-architecting-dapps-on-the-eutxo-ledger.002.png) 16 November 2021![](img/2021-11-16-architecting-dapps-on-the-eutxo-ledger.002.png)[ Jean-Frédéric Etienne](tmp//en/blog/authors/Jean-Frédéric-Etienne/page-1/)![](img/2021-11-16-architecting-dapps-on-the-eutxo-ledger.003.png) 5 mins read

![Jean-Frédéric Etienne](img/2021-11-16-architecting-dapps-on-the-eutxo-ledger.004.png)[](tmp//en/blog/authors/Jean-Frédéric-Etienne/page-1/)
### [**Jean-Frédéric Etienne**](tmp//en/blog/authors/Jean-Frédéric-Etienne/page-1/)
Software Engineer

Engineering

- ![](img/2021-11-16-architecting-dapps-on-the-eutxo-ledger.005.png)[](mailto:jean-frederic.etienne@iohk.io "Email")
- ![](img/2021-11-16-architecting-dapps-on-the-eutxo-ledger.006.png)[](https://www.linkedin.com/in/jean-frédéric-etienne-89607a130 "LinkedIn")
- ![](img/2021-11-16-architecting-dapps-on-the-eutxo-ledger.007.png)[](https://twitter.com/JeanFrdricEtie1 "Twitter")
- ![](img/2021-11-16-architecting-dapps-on-the-eutxo-ledger.008.png)[](https://github.com/etiennejf "GitHub")

![Architecting DApps on the EUTXO ledger](img/2021-11-16-architecting-dapps-on-the-eutxo-ledger.009.jpeg)

Following up on our recent blog post about [Cardano’s performance and ledger optimization roadmap](https://iohk.io/en/blog/posts/2021/11/10/optimizing-cardano/), we prepared a deeper technical dive into the architecture of the EUTXO ledger. 

Theo dõi bài đăng trên blog gần đây của chúng tôi về [Hiệu suất và Lộ trình Tối ưu hóa sổ cái của Cardano] (https://iohk.io/en/blog/posts/2021/11/10/optimizing-cardano/), chúng tôi đã chuẩn bị một cuộc lặn kỹ thuật sâu hơn vào
Kiến trúc của sổ cái Eutxo.

Here, we offer an example architecture and also discuss possible improvements that will boost transaction throughput and minimize delays in transaction processing. 

Ở đây, chúng tôi cung cấp một kiến trúc ví dụ và cũng thảo luận về các cải tiến có thể sẽ tăng cường thông lượng giao dịch và giảm thiểu sự chậm trễ trong xử lý giao dịch.

Cardano’s EUTXO model is a solid basis for decentralized finance (DeFi) and decentralized applications (DApp) development as it facilitates parallel transaction processing, which enables greater scalability than compared to account-based models, as well as providing enhanced security settings. 

Mô hình EUTXO của Cardano là một cơ sở vững chắc cho sự phát triển tài chính phi tập trung (DEFI) và các ứng dụng phi tập trung (DAPP) vì nó tạo điều kiện xử lý giao dịch song song, cho phép khả năng mở rộng lớn hơn so với các mô hình dựa trên tài khoản, cũng như cung cấp các cài đặt bảo mật nâng cao.

However, using a design or mechanisms applicable to account-based systems rather than the EUTXO model (in particular, when building decentralized exchanges) may result in contention issues. This results in a situation when a new transaction is dependent on the output of a previous transaction thus causing delays, especially if there is a large number of transactions. To eliminate this issue, developers should avoid using a single-threaded state machine style and design applications specifically taking into account EUTXO properties. 

Tuy nhiên, sử dụng thiết kế hoặc cơ chế áp dụng cho các hệ thống dựa trên tài khoản thay vì mô hình EUTXO (đặc biệt, khi xây dựng các trao đổi phi tập trung) có thể dẫn đến các vấn đề tranh chấp.
Điều này dẫn đến một tình huống khi một giao dịch mới phụ thuộc vào đầu ra của một giao dịch trước đó, do đó gây ra sự chậm trễ, đặc biệt nếu có một số lượng lớn các giao dịch.
Để loại bỏ vấn đề này, các nhà phát triển nên tránh sử dụng một ứng dụng thiết kế và kiểu máy duy nhất có luồng luồng đặc biệt có tính đến các thuộc tính EUTXO.

## **What does a well-formed architecture look like?**

## ** Kiến trúc được hình thành như thế nào trông như thế nào? **

An [order book pattern](https://www.google.com/url?q=https://plutus-apps.readthedocs.io/en/latest/plutus/explanations/order-book-pattern.html%23what-is-the-order-book-pattern&sa=D&source=docs&ust=1636717791363000&usg=AOvVaw1XLRJgIX-WV7BDp-_EO-A_) is one of the approaches applicable to DEX development if compatible with smart contract logic. And most of the protocol architectures evaluated and presented in [SundaeSwap’s blog post](https://sundaeswap-finance.medium.com/sundaeswap-labs-presents-the-scooper-model-678d6054318d), rely on a general approach whereby:

Một [mẫu sách đặt hàng] (https://www.google.com/url?q=https://plutus-apps.readthedocs.io/en/latest/plutus/explanations/order-book-pattern.html%23whatat
-is-the-order-book-pattern & Sa = d & source = docs & Ust = 1636717791363000 & USG = AOVVAW1XLRJGIX-WV7BDP-_EO-A_) là một trong những phương pháp áp dụng cho DEX Develop
Và hầu hết các kiến trúc giao thức được đánh giá và trình bày trong [Bài đăng trên blog của Sundaeswap] (https://sundaeswap-finance.medium.com/sundaeswap-labs-presents-the-sooper-model-678d60543d)

- a user locks funds in an intermediate script (which we will call the ***request*** script) together with a description of the submitted orders (e.g., token or datum)

-

- a third party (referred to as a *batcher*) aggregates the orders sitting at the ***request*** script into one single transaction such that:

- Bên thứ ba (được gọi là*Batcher*) tổng hợp các đơn đặt hàng tại tập lệnh *** yêu cầu *** vào một giao dịch duy nhất sao cho:

  - the locked orders are spent together with the UTXO holding the global state of the ***main*** script (e.g., liquidity pool) to be updated

- Các đơn đặt hàng bị khóa được chi tiêu cùng với UTXO giữ trạng thái toàn cầu của tập lệnh *** chính *** (ví dụ: nhóm thanh khoản) để được cập nhật

  - results of executed orders are sent back to the original users

- Kết quả của các đơn đặt hàng được thực thi được gửi lại cho người dùng ban đầu

  - a new UTXO holding the updated global state resides at the ***main*** script address

- Một UTXO mới đang giữ trạng thái toàn cầu được cập nhật cư trú tại địa chỉ tập lệnh chính *** ***

When adopting such a batching pattern, one should bear in mind that, whenever *N* orders sitting at the ***request*** script are consumed within a single transaction, the ***request*** script will be executed *N* times on transaction submission. Moreover, the memory limit check (triggered when the transaction is submitted) is realized by aggregating the memory consumption for each single ***request*** script execution, for the *main* script execution, and for any MintingPolicy scripts that may also be executed (i.e., according to protocol design). Additionally, the same transaction context, which is proportional to the number of orders spent, will be passed as an argument for each script execution. 

Khi áp dụng mô hình hàng loạt như vậy, người ta nên nhớ rằng, bất cứ khi nào*n*đơn đặt hàng ngồi tại tập lệnh *** *** được tiêu thụ trong một giao dịch, tập lệnh *** *** sẽ được thực thi*
N* lần gửi giao dịch.
Ngoài ra, kiểm tra giới hạn bộ nhớ (được kích hoạt khi giao dịch được gửi) được thực hiện bằng cách tổng hợp mức tiêu thụ bộ nhớ cho mỗi lần thực hiện tập lệnh *** ***, để thực thi tập lệnh*chính*và cho bất kỳ tập lệnh MiningPolicy nào cũng có thể
được thực hiện (tức là, theo thiết kế giao thức).
Ngoài ra, cùng một bối cảnh giao dịch, tỷ lệ thuận với số lượng đơn đặt hàng đã chi tiêu, sẽ được thông qua như một đối số cho mỗi lần thực thi tập lệnh.

Although this is a good approach, there are possible improvements to make it even better.

Mặc dù đây là một cách tiếp cận tốt, có những cải tiến có thể để làm cho nó thậm chí còn tốt hơn.

One potential solution to avoid triggering the execution of the ***request*** script *N* times (i.e., within the aggregated transaction) is for the user to directly submit orders to their own public key address instead. The ***request*** script is solely used to notify the presence of pending orders and to lock transaction fees that can afterward be claimed by the *batcher* once orders have been processed. Using this solution, users are also required to sign the aggregated transaction to authorize the spending of orders. It is also important to note, that in such a case, all users in the batch should be online to participate. A simplified architecture for such a solution can be summarized as follows:

Một giải pháp tiềm năng để tránh kích hoạt việc thực thi tập lệnh *** *** ****n*lần (tức là, trong giao dịch tổng hợp) là để người dùng gửi trực tiếp đơn đặt hàng đến địa chỉ khóa công khai của riêng họ.
Kịch bản *** yêu cầu *** chỉ được sử dụng để thông báo cho sự hiện diện của các đơn đặt hàng đang chờ xử lý và để khóa phí giao dịch mà sau đó có thể được yêu cầu bởi*Batcher*sau khi các đơn đặt hàng đã được xử lý.
Sử dụng giải pháp này, người dùng cũng được yêu cầu ký giao dịch tổng hợp để ủy quyền chi tiêu đơn đặt hàng.
Điều quan trọng cần lưu ý là, trong trường hợp như vậy, tất cả người dùng trong đợt nên trực tuyến để tham gia.
Một kiến trúc đơn giản hóa cho một giải pháp như vậy có thể được tóm tắt như sau:

**Order submission**:

** Đơn đặt hàng **:

- A specific MintingPolicy script can be used to mint an ‘order’ token submitted to the user's public key address.

- Một tập lệnh khai thác cụ thể có thể được sử dụng để tạo ra một mã thông báo đặt hàng ‘đặt hàng đến địa chỉ khóa công khai của người dùng.

- The hash of the user's public key address, together with the order description and any necessary transaction fees, can be sent to the request script for order notification.

- Hash của địa chỉ khóa công khai của người dùng, cùng với mô tả đặt hàng và bất kỳ phí giao dịch cần thiết nào, có thể được gửi đến tập lệnh yêu cầu để thông báo đặt hàng.

**Order processing**:

** Xử lý đơn hàng **:

- The *batcher* inspects the UTXOs sitting at the request script address to collect ‘order’ tokens and build the aggregated transaction, such that the ‘order’ tokens are used by the main script to validate the aggregated transaction. Note that if an ‘order’ token is not present at the corresponding public key address, the order is considered void.

- * Người bán hàng * kiểm tra UTXOS đang ngồi tại địa chỉ tập lệnh yêu cầu để thu thập ‘đặt hàng mã thông báo và xây dựng giao dịch tổng hợp, sao cho các mã thông báo‘ đặt hàng được sử dụng bởi tập lệnh chính để xác thực giao dịch tổng hợp.
Lưu ý rằng nếu không có mã thông báo đặt hàng tại địa chỉ khóa công khai tương ứng, đơn đặt hàng được coi là vô hiệu.

- The UTXOs sitting at the request script are not spent by the aggregated transaction. They are only used to collect the UTXOs holding the ‘order’ tokens.

- UTXOS ngồi theo kịch bản yêu cầu không được chi cho giao dịch tổng hợp.
Chúng chỉ được sử dụng để thu thập các UTXOS giữ các mã thông báo ’thứ tự.

- The *batcher* notifies the relevant users to sign the aggregated transaction for submission.

- * Batcher * thông báo cho người dùng có liên quan để ký giao dịch tổng hợp để gửi.

- A MintingPolicy, bound to the main script, is used to mint a ‘receipt’ token for each processed order. This ‘receipt’ token will be used by the *batcher* to claim the transaction fees locked at the request script.

- MiningPolicy, bị ràng buộc với tập lệnh chính, được sử dụng để tạo ra một mã thông báo ‘biên lai cho mỗi đơn hàng được xử lý.
Mã thông báo ‘Biên lai này sẽ được sử dụng bởi * Batcher * để yêu cầu các khoản phí giao dịch bị khóa trong tập lệnh yêu cầu.

**Transaction fee collection:**

** Bộ sưu tập phí giao dịch: **

- The *batcher* can consume each UTXO sitting at the request script by providing the corresponding ‘receipt’ token. 

- * Batcher * có thể tiêu thụ mỗi UTXO đang ngồi theo tập lệnh yêu cầu bằng cách cung cấp mã thông báo ‘biên lai tương ứng.

Benchmarks conducted on the public testnet show that with this simple architecture, around 25 to 30 orders can easily be handled within one single transaction, without exceeding the memory limits of 10 million units. We believe that some additional optimizations can still be performed to increase this figure.

Điểm chuẩn được thực hiện trên TestNet công khai cho thấy với kiến trúc đơn giản này, khoảng 25 đến 30 đơn đặt hàng có thể dễ dàng được xử lý trong một giao dịch duy nhất, mà không vượt quá giới hạn bộ nhớ là 10 triệu đơn vị.
Chúng tôi tin rằng một số tối ưu hóa bổ sung vẫn có thể được thực hiện để tăng con số này.

Developers can also extend this architecture to consider more sophisticated mechanisms guaranteeing deterministic ordering, order cancellation by users within a specific time frame, and additional protection against malicious batchers. 

Các nhà phát triển cũng có thể mở rộng kiến trúc này để xem xét các cơ chế tinh vi hơn đảm bảo đặt hàng xác định, hủy bỏ đơn hàng của người dùng trong một khung thời gian cụ thể và bảo vệ bổ sung chống lại những người bán hàng độc hại.

This is just one example of how one can take a EUTXO specific approach to DApp design. We are in the process of extending our documentation and will share other examples in due course. Currently, you can find some code samples for [avoiding concurrency using multi signatures here](https://github.com/input-output-hk/lobster-challenge/tree/concurrency-multisig). 

Đây chỉ là một ví dụ về cách người ta có thể thực hiện một cách tiếp cận cụ thể EUTXO để thiết kế DAPP.
Chúng tôi đang trong quá trình mở rộng tài liệu của chúng tôi và sẽ chia sẻ các ví dụ khác trong khóa học do.
Hiện tại, bạn có thể tìm thấy một số mẫu mã để [tránh đồng thời bằng cách sử dụng nhiều chữ ký ở đây] (https://github.com/input-output

We also anticipate that the development community will identify many further models and we’ll be happy to include these in our repos to build a body of resources for the Plutus development community over the months ahead.

Chúng tôi cũng dự đoán rằng cộng đồng phát triển sẽ xác định nhiều mô hình tiếp theo và chúng tôi sẽ rất vui khi đưa những thứ này vào các repos của chúng tôi để xây dựng một cơ thể tài nguyên cho cộng đồng phát triển Plutus trong những tháng tới.

*Thanks to John Woods and the team for their input and support in preparing this blog post.*

*Cảm ơn John Woods và nhóm đã đầu vào và hỗ trợ của họ trong việc chuẩn bị bài đăng trên blog này.*

