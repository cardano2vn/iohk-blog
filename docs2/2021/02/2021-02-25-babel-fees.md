# Babel fees - denominating transaction costs in native tokens
### **Introducing a novel mechanism that allows the payment of transaction fees in user-defined tokens on Cardano**
![](img/2021-02-25-babel-fees.002.png) 25 February 2021![](img/2021-02-25-babel-fees.002.png)[ Prof Aggelos Kiayias](tmp//en/blog/authors/aggelos-kiayias/page-1/)![](img/2021-02-25-babel-fees.003.png) 8 mins read

![Prof Aggelos Kiayias](img/2021-02-25-babel-fees.004.png)[](tmp//en/blog/authors/aggelos-kiayias/page-1/)
### [**Prof Aggelos Kiayias**](tmp//en/blog/authors/aggelos-kiayias/page-1/)
Chief Scientist

Academic Research

- ![](img/2021-02-25-babel-fees.005.png)[](mailto:aggelos.kiayias@iohk.io "Email")
- ![](img/2021-02-25-babel-fees.006.png)[](tmp///www.youtube.com/watch?v=nB6eDbnkAk8 "YouTube")

![Babel fees - denominating transaction costs in native tokens](img/2021-02-25-babel-fees.007.jpeg)

In Douglas Adams' classic The Hitchhiker's Guide to the Galaxy, a [Babel fish](http://www.bbc.co.uk/cult/hitchhikers/guide/babelfish.shtml) is a creature that allows you to hear any language translated into your own. This fantasy of universal translation ensures meaningful interaction despite the myriad different languages in the galaxy.Â 

Trong tác phẩm kinh điển của Douglas Adams, Hướng dẫn về thiên hà của Douglas Adams, một [cá Babel] (http://www.bbc.co.uk/cult/hitchhikers/guide/babelfish.shtml) là một sinh vật cho phép bạn nghe bất kỳ ngôn ngữ nào
dịch sang của riêng bạn.
Sự tưởng tượng về dịch thuật phổ quát này đảm bảo sự tương tác có ý nghĩa mặc dù vô số ngôn ngữ khác nhau trong thiên hà.

In the cryptocurrency space, smart contract platforms enable the development of a myriad custom tokens. Is it possible to interact with the platform using your preferred token? If only there was a â€œBabel feesâ€ mechanism to translate the token you use to the one that the platform requires for posting a transaction.Â 

Trong không gian tiền điện tử, các nền tảng hợp đồng thông minh cho phép phát triển vô số mã thông báo tùy chỉnh.
Có thể tương tác với nền tảng bằng mã thông báo ưa thích của bạn không?
Nếu chỉ có một cơ chế phí - phí để dịch mã thông báo bạn sử dụng cho cơ quan mà nền tảng yêu cầu để đăng một giao dịch.

Common wisdom in blockchain systems suggests that posting a valid transaction must incur a cost to the sender. The argument is that, without such constraint, there is nothing to stop anyone from overloading the system with trivial transactions saturating its capacity and rendering it unusable. Given the above tenet, a frequently made corollary is that in any blockchain system where user-defined tokens are supported, it should be prohibited to pay transaction fees in such tokens. Instead, transactions should carry a fee in the native token of the platform that is accepted by all participants as being valuable.Â  Arguably such a restriction is undesirable. But how is it possible to circumvent the ensuing â€“ and seemingly inevitable â€“ vulnerability?Â 

Trí tuệ thông thường trong các hệ thống blockchain cho thấy rằng việc đăng một giao dịch hợp lệ phải phải chịu chi phí cho người gửi.
Lập luận là, không có ràng buộc như vậy, không có gì ngăn cản bất cứ ai làm quá tải hệ thống với các giao dịch tầm thường bão hòa năng lực của nó và khiến nó không thể sử dụng được.
Với nguyên lý trên, một hệ quả thường xuyên được thực hiện là trong bất kỳ hệ thống blockchain nào nơi hỗ trợ mã thông báo do người dùng xác định, nên cấm trả phí giao dịch trong các mã thông báo đó.
Thay vào đó, các giao dịch sẽ mang một khoản phí trong mã thông báo gốc của nền tảng được tất cả những người tham gia chấp nhận là có giá trị. Có thể cho rằng một hạn chế như vậy là không mong muốn.
Nhưng làm thế nào có thể phá vỡ sự dễ bị tổn thương sau đó và dường như không thể tránh khỏi?

## **The art of the possible**

## ** Nghệ thuật có thể **

Cryptography and game theory have been known to make possible what seemed impossible. Celebrated examples include key exchange over a public channel, Merkle's puzzles, and auctions where being truthful is the rational thing to do, like Vickrey's auctions. And so it also turns out in this case.Â 

Mật mã và lý thuyết trò chơi đã được biết là có thể làm những gì dường như không thể.
Các ví dụ nổi tiếng bao gồm trao đổi quan trọng trên một kênh công cộng, câu đố của Merkle và các cuộc đấu giá trong đó sự thật là điều hợp lý để làm, như các cuộc đấu giá của Vickrey.
Và vì vậy nó cũng hóa ra trong trường hợp này.

First, let us recall how native assets work in Cardano: Tokens can be created according to a minting policy and they are treated natively in the ledger along with ada. Cardano's ledger adopts the Extended UTXO (EUTXO) model, and issuing a valid transaction requires consuming one or more UTXOs. A UTXO in Cardano may carry not just ada but in fact a token bundle that can contain multiple different tokens, both fungible and non-fungible. In this way it is possible to write transactions that transfer multiple different tokens with a single UTXO.Â 

Đầu tiên, chúng ta hãy nhớ lại cách tài sản bản địa hoạt động trong Cardano: mã thông báo có thể được tạo ra theo chính sách khai thác và chúng được đối xử nguyên bản trong sổ cái cùng với ADA.
Ledger của Cardano áp dụng mô hình UTXO (EUTXO) mở rộng và phát hành một giao dịch hợp lệ đòi hỏi phải tiêu thụ một hoặc nhiều UTXO.
Một UTXO trong Cardano có thể mang theo không chỉ ADA mà trên thực tế, một gói mã thông báo có thể chứa nhiều mã thông báo khác nhau, cả nấm và không bị mắc bệnh.
Theo cách này, có thể viết các giao dịch chuyển nhiều mã thông báo khác nhau với một utxo.

Transaction fees in the ledger are denominated in ada according to a function fixed as a ledger parameter. A powerful feature of Cardano's EUTXO model is that the fees required for a valid transaction can be predicted precisely prior to posting it. This is a unique feature that is not enjoyed by other ledger arrangements (such as the account-based model used in Ethereum). Indeed, in this latter case the fees needed for a transaction may change during the time it takes for the transaction to settle, since other transactions may affect the ledger's state in between and influence the required cost for processing the transaction.Â 

Phí giao dịch trong sổ cái được mệnh giá trong ADA theo một hàm được cố định dưới dạng tham số sổ cái.
Một tính năng mạnh mẽ của mô hình EUTXO của Cardano là các khoản phí cần thiết cho một giao dịch hợp lệ có thể được dự đoán chính xác trước khi đăng nó.
Đây là một tính năng độc đáo không được yêu thích bởi các sắp xếp sổ cái khác (chẳng hạn như mô hình dựa trên tài khoản được sử dụng trong Ethereum).
Thật vậy, trong trường hợp sau này, các khoản phí cần thiết cho một giao dịch có thể thay đổi trong thời gian giao dịch để giải quyết, vì các giao dịch khác có thể ảnh hưởng đến trạng thái của sổ cái ở giữa và ảnh hưởng đến chi phí cần thiết để xử lý giao dịch.

## **A thought experiment**

## ** Một thử nghiệm suy nghĩ **

Let's consider the following thought experiment to help us move closer towards our objective of Babel fees. Imagine that it is possible to issue a transaction that declares a liability denominated in ada equal to the amount of fees that the transaction issuer is supposed to pay. Such a transaction would not be admissible to the ledger. However it can be perceived as an open offer that asks for the liability to be covered. Why would anyone respond to such an offer? To entice a response, assuming the token bundle concept already present in Cardano,Â  the transaction can offer some amount of token(s) to whoever covers the liability. This suggests a spot trade between ada and the offered token(s) at a certain exchange rate. Consider now a block producer that sees such a transaction. The block producer can create a matching transaction absorbing the liability covering it with ada as well as claiming the tokens that are on offer.Â 

Chúng ta hãy xem xét các thí nghiệm suy nghĩ sau đây để giúp chúng ta tiến gần hơn đến mục tiêu của chúng ta về phí Babel.
Hãy tưởng tượng rằng có thể phát hành một giao dịch tuyên bố trách nhiệm pháp lý trong ADA bằng với số tiền mà nhà phát hành giao dịch được cho là phải trả.
Một giao dịch như vậy sẽ không được chấp nhận cho sổ cái.
Tuy nhiên, nó có thể được coi là một đề nghị mở yêu cầu trách nhiệm pháp lý được bảo hiểm.
Tại sao mọi người sẽ trả lời một đề nghị như vậy?
Để lôi kéo phản hồi, giả sử khái niệm gói mã thông báo đã có trong Cardano, - giao dịch có thể cung cấp một số lượng mã thông báo cho bất cứ ai bao gồm trách nhiệm pháp lý.
Điều này cho thấy một giao dịch tại chỗ giữa ADA và (các) mã thông báo được cung cấp ở một tỷ giá hối đoái nhất định.
Bây giờ hãy xem xét một nhà sản xuất khối nhìn thấy một giao dịch như vậy.
Nhà sản xuất khối có thể tạo ra một giao dịch phù hợp hấp thụ trách nhiệm bao gồm nó với ADA cũng như yêu cầu các mã thông báo được cung cấp.

By suitably extending the ledger rules, the transaction with the liability as well as its matching transaction become admissible to the ledger as a group. Due to the absorption of the liability, the set of two transactions becomes properly priced in ada as a whole and hence it does not break the ledgers' bookkeeping rules in terms of ada fees. As a result, the transaction with the liability settles, and we have achieved our objective. Users can submit transactions priced in any token(s) they possess and, providing a block producer is willing to take them up on the spot trade, have them settle in the ledger as regular transactions!

Bằng cách mở rộng phù hợp với các quy tắc sổ cái, giao dịch có trách nhiệm cũng như giao dịch phù hợp của nó trở nên đáng chú ý đối với sổ cái như một nhóm.
Do sự hấp thụ trách nhiệm pháp lý, tập hợp hai giao dịch trở nên có giá đúng trong ADA và do đó, nó không phá vỡ các quy tắc ghi sổ của sổ cái về phí ADA.
Do đó, giao dịch với trách nhiệm giải quyết và chúng tôi đã đạt được mục tiêu của mình.
Người dùng có thể gửi các giao dịch có giá trong bất kỳ mã thông báo nào họ sở hữu và, cung cấp một nhà sản xuất khối sẵn sàng đưa họ lên giao dịch tại chỗ, để họ giải quyết trong sổ cái dưới dạng giao dịch thông thường!

## **A concrete example**

## ** một ví dụ cụ thể **

The mechanism is of course conditioned on the presence of liquidity providers that possess ada and are willing to issue matching transactions. In fact the mechanism creates a market for such liquidity providers. For instance, a stake pool operator (SPO), can publish exchange rates for specific tokens they consider acceptable. For instance an SPO can declare that they will accept tokenX for an exchange rate 3:1 over ada. It follows that if a transaction costs, say â‚³0.16, the transaction can declare a liability of â‚³0.16 as well as offer 0.48 of tokenX. In the native asset model of Cardano this can be implemented as a single UTXO carrying a token bundle with the following specification (Adaâ†’ -0.16, tokenXâ†’0.48). Note the negative sign signifying the liability.Â 

Cơ chế tất nhiên được quy định dựa trên sự hiện diện của các nhà cung cấp thanh khoản sở hữu ADA và sẵn sàng phát hành các giao dịch phù hợp.
Trong thực tế, cơ chế tạo ra một thị trường cho các nhà cung cấp thanh khoản như vậy.
Chẳng hạn, một nhà điều hành nhóm cổ phần (SPO), có thể xuất bản tỷ giá hối đoái cho các mã thông báo cụ thể mà họ cho là chấp nhận được.
Ví dụ, một SPO có thể tuyên bố rằng họ sẽ chấp nhận Tokenx cho tỷ giá hối đoái 3: 1 so với ADA.
Theo sau đó, nếu một chi phí giao dịch, giả sử â‚³0.16, giao dịch có thể tuyên bố trách nhiệm pháp lý của â‚³0.16 cũng như cung cấp 0,48 tokenx.
Trong mô hình tài sản gốc của Cardano, điều này có thể được triển khai dưới dạng UTXO duy nhất mang theo gói mã thông báo với đặc điểm kỹ thuật sau (ADAÂ † -0.16, Tokenxâ † 0.48).
Lưu ý dấu hiệu tiêu cực biểu thị trách nhiệm pháp lý.â

Suppose now that the SPO is about to produce a block. She recovers the liability transaction from the mempool and issues a matching transaction consuming the UTXO with the liability. The matching transaction transfers 0.48 of tokenX to a new output which is owned by the SPO. The resulting block contains the two transactions in sequence. The matching transaction provides the missing â‚³0.16 in addition to the fees that are needed for itself. In fact multiple transactions can be batched together and have their fees covered by a single matching transaction.Â 

Giả sử bây giờ SPO sắp tạo ra một khối.
Cô phục hồi giao dịch trách nhiệm pháp lý từ mempool và đưa ra một giao dịch phù hợp tiêu thụ UTXO với trách nhiệm pháp lý.
Giao dịch phù hợp chuyển 0,48 tokenx sang đầu ra mới thuộc sở hữu của SPO.
Khối kết quả chứa hai giao dịch theo trình tự.
Giao dịch phù hợp cung cấp phần còn thiếu â‚³0.16 ngoài các khoản phí cần thiết cho chính nó.
Trên thực tế, nhiều giao dịch có thể được ghép với nhau và có các khoản phí của họ được bảo hiểm bởi một giao dịch phù hợp duy nhất.

![](img/2021-02-25-babel-fees.008.png)

*Figure. Alice sends a quantity of 9 tokens of type X to Bob with the assistance of Stacy, an SPO, who covers Alice's transaction liability and receives tokens of type X in exchange. The implied exchange rate between X and Ada is 3:1.*Â 

*Nhân vật.
Alice gửi số lượng 9 mã thông báo loại X cho BOB với sự hỗ trợ của Stacy, một SPO, người bao gồm trách nhiệm giao dịch của Alice và nhận được các token loại X để trao đổi.
Tỷ giá hối đoái ngụ ý giữa X và ADA là 3: 1.*Â

## **New measures of value**

## ** Các biện pháp giá trị mới **

The above process is entirely opt-in for SPOs. Each one can determine their own policy and exchange rate as well as decide to change the exchange rate for the various tokens they accept on the spot. Moreover, there is no need for agreement between SPOs about the value of a specific token. In fact, different SPOs may provide different exchange rates for the same token and a user issuing a liability transaction can offer an amount of tokens corresponding to the minimum, average or even maximum of the posted exchange rates in the network. In this way, a natural trade off arises between settlement time of liability transactions and the market value of tokens they offer.Â 

Quá trình trên hoàn toàn chọn tham gia cho các SPO.
Mỗi người có thể xác định chính sách và tỷ giá hối đoái của riêng họ cũng như quyết định thay đổi tỷ giá hối đoái cho các mã thông báo khác nhau mà họ chấp nhận tại chỗ.
Hơn nữa, không cần phải thỏa thuận giữa các SPO về giá trị của một mã thông báo cụ thể.
Trên thực tế, các SPO khác nhau có thể cung cấp tỷ giá hối đoái khác nhau cho cùng một mã thông báo và người dùng phát hành giao dịch trách nhiệm pháp lý có thể cung cấp một lượng mã thông báo tương ứng với mức tối thiểu, trung bình hoặc thậm chí tối đa của tỷ giá hối đoái được đăng trong mạng.
Theo cách này, một sự đánh đổi tự nhiên phát sinh giữa thời gian giải quyết các giao dịch trách nhiệm pháp lý và giá trị thị trường của các mã thông báo mà họ cung cấp.

This illustrates how native assets, the EUTXO model, and the simple but powerful tweak of introducing liabilities in the form of negative values in token bundles can accommodate Babel fees empowering users to price transactions in any token supportedÂ natively by the system. It also shows the unique advantage of being an SPO in such a system. It should be noted that SPOs need not be the only entities in the network offering to cover liabilities. In fact, an SPO can readily partner -if they wish- with an external liquidity provider who will be issuing the matching transactions. In addition, third party providers can also act on the network independently and issue matching transactions. Nevertheless, the benefit will remain with the block producers; SPOs can always front-run matching transactions and substitute them for their own if they wish so. This is a case that front-running transactions is a feature: it makes it feasible for SPOs to be paid in the tokens they prefer for their transaction processing services.

Điều này minh họa cách các tài sản bản địa, mô hình EUTXO và tinh chỉnh đơn giản nhưng mạnh mẽ về việc giới thiệu các khoản nợ dưới dạng các giá trị âm trong các gói mã thông báo có thể phù hợp với phí Babel để trao quyền cho người dùng giao dịch định giá theo bất kỳ mã thông báo nào được hỗ trợ bởi hệ thống. Nó cũng cho thấy lợi thế duy nhất của việc trở thành một SPO trong một hệ thống như vậy. Cần lưu ý rằng các SPO không cần phải là thực thể duy nhất trong mạng cung cấp để trang trải các khoản nợ. Trên thực tế, một SPO có thể dễ dàng hợp tác - nếu họ mong muốn - với một nhà cung cấp thanh khoản bên ngoài, người sẽ phát hành các giao dịch phù hợp. Ngoài ra, các nhà cung cấp bên thứ ba cũng có thể hành động trên mạng một cách độc lập và phát hành các giao dịch phù hợp. Tuy nhiên, lợi ích sẽ vẫn còn với các nhà sản xuất khối; SPO luôn có thể có các giao dịch phù hợp trước và thay thế chúng nếu họ muốn như vậy. Đây là một trường hợp mà các giao dịch chạy trước là một tính năng: nó làm cho các SPO được thanh toán trong các mã thông báo mà họ thích cho các dịch vụ xử lý giao dịch của họ.

The mechanism of negative quantities in token bundles can be implemented in the basic ledger rules of Cardano at some point following the introduction of native assets with the Mary Hard Fork. Beyond Babel fees, the mechanism allows a variety of other interesting applications, such as atomic swaps for spot trades, that we will cover in a future blog post. It is yet another illustration of the power of Cardano's approach and its ability to support a diverse and entrepreneurial community of users and stake pool operators.Â 

Cơ chế của số lượng âm trong các bó mã thông báo có thể được thực hiện trong các quy tắc sổ cái cơ bản của Cardano tại một số điểm sau khi giới thiệu tài sản bản địa với Mary Hard Fork.
Ngoài phí Babel, cơ chế cho phép một loạt các ứng dụng thú vị khác, chẳng hạn như hoán đổi nguyên tử cho các giao dịch tại chỗ, mà chúng tôi sẽ đề cập trong một bài đăng trên blog trong tương lai.
Đây là một minh họa khác về sức mạnh của cách tiếp cận của Cardano và khả năng hỗ trợ một cộng đồng người dùng đa dạng và kinh doanh của người dùng và các nhà điều hành nhóm cổ phần.

*I am grateful to Manuel Chakravarty, Michael Peyton Jones, Nikos Karagiannidis, Chad Nester and Polina Vinogradova for helpful discussions, suggestions and comments related to the concept of Babel fees and its implementation in the Cardano ledger. We also have a [video whiteboard walkthrough](https://youtu.be/YXaK0cvgoFQ?t=2184) covering this topic.*

*Tôi biết ơn Manuel Chakravarty, Michael Peyton Jones, Nikos Karagiannidis, Chad Nester và Polina Vinogradova cho các cuộc thảo luận, đề xuất và nhận xét hữu ích liên quan đến khái niệm phí Babel và việc triển khai của nó trong sổ cái Cardano.
Chúng tôi cũng có một [video Whiteboard Walkthrough] (https://youtu.be/yxak0cvgofq?t=2184) bao gồm chủ đề này.*

