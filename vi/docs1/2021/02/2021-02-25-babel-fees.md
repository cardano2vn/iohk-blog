# Phí Babel - xác định phí giao dịch bằng Token gốc

### **Giới thiệu một cơ chế mới cho phép thanh toán phí giao dịch bằng Token do người dùng xác định trên Cardano**

![](img/2021-02-25-babel-fees.002.png) 25 February 2021![](img/2021-02-25-babel-fees.002.png)[ Prof Aggelos Kiayias](tmp//en/blog/authors/aggelos-kiayias/page-1/)![](img/2021-02-25-babel-fees.003.png) 8 mins read

![Prof Aggelos Kiayias](img/2021-02-25-babel-fees.004.png)[](tmp//en/blog/authors/aggelos-kiayias/page-1/)

### [**Prof Aggelos Kiayias**](tmp//en/blog/authors/aggelos-kiayias/page-1/)

Chief Scientist

Academic Research

- ![](img/2021-02-25-babel-fees.005.png)[](mailto:aggelos.kiayias@iohk.io "Email")
- ![](img/2021-02-25-babel-fees.006.png)[](tmp///www.youtube.com/watch?v=nB6eDbnkAk8 "YouTube")

![Babel fees - denominating transaction costs in native tokens](img/2021-02-25-babel-fees.007.jpeg)

Trong cuốn sách kinh điển The Hitchhiker's Guide to the Galaxy của Douglas Adams, [cá Babel](http://www.bbc.co.uk/cult/hitchhikers/guide/babelfish.shtml) là sinh vật cho phép bạn nghe bất kỳ ngôn ngữ nào được dịch sang tiếng mẹ đẻ của bạn. Hãy tưởng tượng bản dịch phổ quát này đảm bảo sự tương tác có ý nghĩa bất chấp có vô số ngôn ngữ khác nhau trong thiên hà.

Trong lĩnh vực tiền mã hoá, các nền tảng hợp đồng thông minh cho phép phát triển vô số Token tùy chỉnh. Bạn có thể tương tác với nền tảng bằng cách sử dụng Token ưa thích của mình không? Giá mà có một cơ chế giống như "phí Babel" để chuyển đổi Token bạn sử dụng sang cơ chế mà nền tảng yêu cầu để gửi giao dịch.

Common wisdom in blockchain systems suggests that posting a valid transaction must incur a cost to the sender. The argument is that, without such constraint, there is nothing to stop anyone from overloading the system with trivial transactions saturating its capacity and rendering it unusable. Given the above tenet, a frequently made corollary is that in any blockchain system where user-defined tokens are supported, it should be prohibited to pay transaction fees in such tokens. Instead, transactions should carry a fee in the native token of the platform that is accepted by all participants as being valuable.Â  Arguably such a restriction is undesirable. But how is it possible to circumvent the ensuing â€“ and seemingly inevitable â€“ vulnerability?Â 

## **Nghệ thuật của những điều có thể**

Mật mã học và lý thuyết trò chơi đã được biết đến là có thể biến những gì tưởng chừng như không thể thành có thể. Các ví dụ nổi tiếng bao gồm trao đổi quan trọng qua kênh công khai, câu đố của Merkle, và đấu giá trong đó trung thực là điều hợp lý để làm, như đấu giá của Vickrey. Vì vậy, nó cũng xuất hiện trong trường hợp này.

First, let us recall how native assets work in Cardano: Tokens can be created according to a minting policy and they are treated natively in the ledger along with ada. Cardano's ledger adopts the Extended UTXO (EUTXO) model, and issuing a valid transaction requires consuming one or more UTXOs. A UTXO in Cardano may carry not just ada but in fact a token bundle that can contain multiple different tokens, both fungible and non-fungible. In this way it is possible to write transactions that transfer multiple different tokens with a single UTXO.Â 

Phí giao dịch trong sổ cái được tính bằng ADA theo một hàm được cố định dưới dạng tham số sổ cái. Mô hình EUTXO của Cardano có một tính năng mạnh mẽ là các khoản phí cần thiết cho một giao dịch hợp lệ có thể được dự đoán chính xác trước khi gửi. Đây là một tính năng độc đáo không có trong các sổ cái khác (chẳng hạn như mô hình dựa trên tài khoản được sử dụng trong Ethereum). Thật vậy, trong trường hợp thứ hai này, phí cần thiết cho một giao dịch có thể thay đổi trong thời gian cần thiết để giao dịch được giải quyết, vì các giao dịch khác có thể ảnh hưởng đến trạng thái của sổ cái ở giữa quá trình và ảnh hưởng đến chi phí cần thiết để xử lý giao dịch.

## **Một thử nghiệm đáng suy nghĩ**

Hãy xem xét thử nghiệm đáng suy nghĩ sau đây để tiến gần hơn đến mục tiêu của chúng tôi về phí Babel. Hãy tưởng tượng rằng có thể phát hành một giao dịch tuyên bố một khoản nợ phải trả bằng ADA bằng với số phí mà người tạo giao dịch phải trả. Một giao dịch như vậy sẽ không được chấp nhận vào sổ cái. Tuy nhiên, nó có thể được coi là một đề nghị mở yêu cầu trách nhiệm được bảo hiểm. Tại sao mọi người sẽ phản hồi một đề nghị như vậy? Để thu hút phản hồi, giả sử khái niệm gói Token đã có trong Cardano, giao dịch có thể cung cấp một số lượng Token cho bất kỳ ai đảm nhận trách nhiệm. Điều này gợi ý một giao dịch giao ngay giữa ADA và (các) Token được cung cấp ở một tỷ giá hối đoái nhất định. Bây giờ hãy xem xét một nhà sản xuất Block khi thấy một giao dịch như vậy. Nhà sản xuất Block có thể tạo một giao dịch phù hợp đảm nhận trách nhiệm pháp lý bao gồm nó với ADA cũng như yêu cầu các Token được cung cấp.

Bằng cách mở rộng một cách thích hợp các quy tắc sổ cái, giao dịch với khoản nợ phải trả cũng như giao dịch khớp lệnh của nó trở nên được chấp nhận vào sổ cái như một nhóm. Do việc đảm nhận trách nhiệm, tập hợp hai giao dịch sẽ được định giá thích hợp bằng ADA. Do đó nó không phá vỡ các quy tắc ghi sổ kế toán của sổ cái về phí ADA. Kết quả là giao dịch với trách nhiệm pháp lý được giải quyết và chúng tôi đã đạt được mục tiêu của mình. Người dùng có thể gửi các giao dịch được định giá bằng bất kỳ (các) Token nào mà họ sở hữu và cung cấp cho nhà sản xuất Block sẵn sàng thực hiện giao dịch giao ngay để họ giải quyết trong sổ cái như các giao dịch thông thường!

## **Một ví dụ cụ thể**

The mechanism is of course conditioned on the presence of liquidity providers that possess ada and are willing to issue matching transactions. In fact the mechanism creates a market for such liquidity providers. For instance, a stake pool operator (SPO), can publish exchange rates for specific tokens they consider acceptable. For instance an SPO can declare that they will accept tokenX for an exchange rate 3:1 over ada. It follows that if a transaction costs, say â‚³0.16, the transaction can declare a liability of â‚³0.16 as well as offer 0.48 of tokenX. In the native asset model of Cardano this can be implemented as a single UTXO carrying a token bundle with the following specification (Adaâ†’ -0.16, tokenXâ†’0.48). Note the negative sign signifying the liability.Â 

Giả sử bây giờ SPO sắp sản xuất một Block. Họ khôi phục giao dịch trách nhiệm pháp lý từ Mempool và đưa ra một giao dịch khớp lệnh sử dụng UTXO cùng với khoản nợ phải trả. Giao dịch khớp lệnh chuyển 0,48 Token X sang một đầu ra mới thuộc sở hữu của SPO. Block kết quả chứa hai giao dịch theo trình tự. Giao dịch khớp lệnh cung cấp 0,16 ADA còn thiếu ngoài các khoản phí cần thiết cho chính nó. Trên thực tế, nhiều giao dịch có thể được thực hiện cùng nhau và phí của chúng được chi trả bởi một giao dịch khớp lệnh duy nhất.

![](img/2021-02-25-babel-fees.008.png)

Hình 1. Alice gửi một số lượng gồm 9 Token X cho Bob với sự hỗ trợ của Stacy là một SPO, người chi trả trách nhiệm giao dịch của Alice và nhận các Token X để trao đổi. Tỷ giá hối đoái giữa X và ADA là 3:1.

## **Thước đo giá trị mới**

SPO hoàn toàn nắm quyền lựa chọn tham gia trong quá trình trên. Mỗi SPO có thể xác định chính sách và tỷ giá hối đoái của riêng mình cũng như quyết định thay đổi tỷ giá hối đoái cho các Token khác nhau mà họ chấp nhận giao dịch giao ngay. Trên thực tế, các SPO khác nhau có thể cung cấp tỷ giá hối đoái khác nhau cho cùng một Token. Người dùng phát hành giao dịch trách nhiệm có thể cung cấp số lượng Token tương ứng với mức tối thiểu, trung bình hoặc thậm chí tối đa của tỷ giá hối đoái đã đăng trong mạng lưới. Theo cách này, sự trao đổi tự nhiên phát sinh giữa thời gian thanh toán các giao dịch trách nhiệm pháp lý và giá trị thị trường của các Token mà họ cung cấp.

This illustrates how native assets, the EUTXO model, and the simple but powerful tweak of introducing liabilities in the form of negative values in token bundles can accommodate Babel fees empowering users to price transactions in any token supportedÂ natively by the system. It also shows the unique advantage of being an SPO in such a system. It should be noted that SPOs need not be the only entities in the network offering to cover liabilities. In fact, an SPO can readily partner -if they wish- with an external liquidity provider who will be issuing the matching transactions. In addition, third party providers can also act on the network independently and issue matching transactions. Nevertheless, the benefit will remain with the block producers; SPOs can always front-run matching transactions and substitute them for their own if they wish so. This is a case that front-running transactions is a feature: it makes it feasible for SPOs to be paid in the tokens they prefer for their transaction processing services.

The mechanism of negative quantities in token bundles can be implemented in the basic ledger rules of Cardano at some point following the introduction of native assets with the Mary Hard Fork. Beyond Babel fees, the mechanism allows a variety of other interesting applications, such as atomic swaps for spot trades, that we will cover in a future blog post. It is yet another illustration of the power of Cardano's approach and its ability to support a diverse and entrepreneurial community of users and stake pool operators.Â 

*I am grateful to Manuel Chakravarty, Michael Peyton Jones, Nikos Karagiannidis, Chad Nester and Polina Vinogradova for helpful discussions, suggestions and comments related to the concept of Babel fees and its implementation in the Cardano ledger. We also have a [video whiteboard walkthrough](https://youtu.be/YXaK0cvgoFQ?t=2184) covering this topic.*
