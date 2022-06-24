# Cardano’s Extended UTXO accounting model – built to support multi-assets and smart contracts (part 2)
### **In the second part of our blog on Cardano’s EUTXO accounting model, we take a more technical look at transaction components, the UTXO set, and delve deeper into the rationale for Cardano’s EUTXO model**
![](img/2021-03-12-cardanos-extended-utxo-accounting-model-part-2.002.png) 12 March 2021![](img/2021-03-12-cardanos-extended-utxo-accounting-model-part-2.002.png)[ Fernando Sanchez](tmp//en/blog/authors/fernando-sanchez/page-1/)![](img/2021-03-12-cardanos-extended-utxo-accounting-model-part-2.003.png) 5 mins read

![Fernando Sanchez](img/2021-03-12-cardanos-extended-utxo-accounting-model-part-2.004.png)[](tmp//en/blog/authors/fernando-sanchez/page-1/)
### [**Fernando Sanchez**](tmp//en/blog/authors/fernando-sanchez/page-1/)
Technical Writer

Marketing and Communications

- ![](img/2021-03-12-cardanos-extended-utxo-accounting-model-part-2.005.png)[](mailto:fernando.sanchez@iohk.io "Email")
- ![](img/2021-03-12-cardanos-extended-utxo-accounting-model-part-2.006.png)[](https://www.linkedin.com/in/linkedinsanchezf/ "LinkedIn")

![Cardano’s Extended UTXO accounting model – built to support multi-assets and smart contracts (part 2)](img/2021-03-12-cardanos-extended-utxo-accounting-model-part-2.007.jpeg)

Yesterday we offered an [overview](https://iohk.io/en/blog/posts/2021/03/11/cardanos-extended-utxo-accounting-model/) of the Extended UTXO model employed by Cardano, explaining how it differs from the approaches taken by Bitcoin and Ethereum. Now let’s dive a little deeper into inputs and outputs, the component parts of a transaction. 

Hôm qua, chúng tôi đã cung cấp một [tổng quan] (https://iohk.io/en/blog/posts/2021/03/11/cardanos-extends-utxo-accounting-model/) của mô hình UTXO mở rộng được sử dụng bởi Cardano, giải thích làm thế nào
Nó khác với các phương pháp được thực hiện bởi Bitcoin và Ethereum.
Bây giờ, hãy để lặn sâu hơn một chút vào đầu vào và đầu ra, các phần thành phần của giao dịch.

### **We need to talk about transactions: Outputs and Inputs**

### ** Chúng ta cần nói về các giao dịch: Đầu ra và đầu vào **

The term *transaction* usually evokes financial echoes. While such meaning would apply to Bitcoin (since the Bitcoin blockchain is used to move funds between peers), many other blockchains (including Cardano) are far more versatile. In these cases, the term ‘transaction’ is much more nuanced. One can think of transactions as transfers of value.

Thuật ngữ * giao dịch * thường gợi lên tiếng vang tài chính.
Mặc dù ý nghĩa như vậy sẽ áp dụng cho Bitcoin (vì blockchain bitcoin được sử dụng để di chuyển tiền giữa các đồng nghiệp), nhiều blockchain khác (bao gồm cả Cardano) linh hoạt hơn nhiều.
Trong những trường hợp này, thuật ngữ ‘giao dịch, có nhiều sắc thái hơn.
Người ta có thể nghĩ về các giao dịch như chuyển giao giá trị.

In a blockchain environment, each transaction can have one or multiple inputs, and one or multiple outputs. The concepts of **Inputs** and **Outputs** must be understood, if one wants to understand how a transaction works, and how it relates to UTXO. In abstract terms, think of a transaction as *the action that unlocks previous outputs, and creates new ones*.

Trong môi trường blockchain, mỗi giao dịch có thể có một hoặc nhiều đầu vào và một hoặc nhiều đầu ra.
Các khái niệm về ** đầu vào ** và ** đầu ra ** phải được hiểu, nếu người ta muốn hiểu cách thức hoạt động của một giao dịch và nó liên quan đến UTXO như thế nào.
Trong các thuật ngữ trừu tượng, hãy nghĩ về một giao dịch là *hành động mở ra các kết quả đầu ra trước đó và tạo ra các giao dịch mới *.

**Transaction output**

** Đầu ra giao dịch **

A transaction output includes an address (that you can think of as a lock) and a value. In keeping with this analogy, the signature that belongs to the address is the key to unlock the output. Once unlocked, an output can be used as input. New transactions spend outputs of previous transactions, and produce new outputs that can be consumed by future transactions. Each UTXO can only be consumed once, and as a whole. Each output can be spent by exactly one input, *and one input only.*

Đầu ra giao dịch bao gồm một địa chỉ (mà bạn có thể nghĩ là khóa) và một giá trị.
Để phù hợp với sự tương tự này, chữ ký thuộc địa chỉ là chìa khóa để mở khóa đầu ra.
Sau khi mở khóa, đầu ra có thể được sử dụng làm đầu vào.
Các giao dịch mới chi tiêu đầu ra của các giao dịch trước đó và tạo ra các đầu ra mới có thể được tiêu thụ bởi các giao dịch trong tương lai.
Mỗi UTXO chỉ có thể được tiêu thụ một lần, và nói chung.
Mỗi đầu ra có thể được chi tiêu cho chính xác một đầu vào, *và một đầu vào chỉ. *

**Transaction input**

** Đầu vào giao dịch **

A transaction input is the output of a previous transaction. Transaction inputs include a pointer and a cryptographic signature that acts as the unlocking key. The pointer points back to a previous transaction output, and the key unlocks this output. When an output is unlocked by an input, the blockchain marks the unlocked output as “spent”. New outputs created by a given transaction can then be pointed to by new inputs, and so the chain continues. These new outputs (which have not yet been unlocked, i.e., spent) are the UTXOs. **Unspent outputs are simply that, outputs that have not yet been spent**.

Đầu vào giao dịch là đầu ra của một giao dịch trước đó.
Đầu vào giao dịch bao gồm một con trỏ và chữ ký mật mã hoạt động như khóa mở khóa.
Con trỏ hướng trở lại đầu ra giao dịch trước đó và khóa mở ra đầu ra này.
Khi một đầu ra được mở khóa bởi một đầu vào, blockchain đánh dấu đầu ra đã được mở khóa dưới dạng chi tiêu.
Các đầu ra mới được tạo bởi một giao dịch nhất định sau đó có thể được chỉ ra bởi các đầu vào mới, và do đó chuỗi tiếp tục.
Những đầu ra mới này (chưa được mở khóa, tức là đã chi tiêu) là UTXOS.
** Đầu ra chưa được sử dụng chỉ đơn giản là, các đầu ra chưa được sử dụng **.

### **How UTXO works, in a nutshell**

### ** Cách hoạt động của UTXO, trong một Nutshell **

In a UTXO accounting model, transactions consume unspent outputs from previous transactions, and produce new outputs that can be used as inputs for future transactions.

Trong mô hình kế toán UTXO, các giao dịch tiêu thụ các đầu ra chưa được sử dụng từ các giao dịch trước đó và tạo ra các đầu ra mới có thể được sử dụng làm đầu vào cho các giao dịch trong tương lai.

![](img/2021-03-12-cardanos-extended-utxo-accounting-model-part-2.008.png)

The users' wallets manage these UTXOs and initiate transactions involving the UTXOs owned by the user. Every blockchain node maintains a record of the subset of all UTXOs at all times. This is called the *UTXO set*. In technical terms, this is the *chainstate*, which is stored in the data directory of every node. When a new block is added to the chain, the chainstate is updated accordingly. This new block contains the list of latest transactions (including of course a record of spent UTXOs, and new ones created since the chainstate was last updated). Every node maintains an exact copy of the chainstate. 

Ví của người dùng quản lý các UTXO này và bắt đầu các giao dịch liên quan đến UTXO thuộc sở hữu của người dùng.
Mỗi nút blockchain duy trì một bản ghi của tập hợp con của tất cả các UTXO mọi lúc.
Đây được gọi là *UTXO SET *.
Về mặt kỹ thuật, đây là *Chainstate *, được lưu trữ trong thư mục dữ liệu của mọi nút.
Khi một khối mới được thêm vào chuỗi, dây chuyền được cập nhật tương ứng.
Khối mới này chứa danh sách các giao dịch mới nhất (bao gồm tất nhiên là một bản ghi UTXOS đã qua sử dụng và các giao dịch mới được tạo kể từ khi dây chuyền được cập nhật lần cuối).
Mỗi nút duy trì một bản sao chính xác của chuỗi.

### **EUTXO: The rationale behind Cardano's choice**

### ** EUTXO: Cơ sở lý luận đằng sau sự lựa chọn của Cardano **

Bitcoin’s ‘vanilla’ UTXO accounting model would not suit Cardano, as Cardano is designed to do more than handle payments. Particularly, the need for more programming expressiveness for the upcoming smart contracts functionality in the Alonzo era required a novel (‘Extended’) solution.

Mô hình kế toán Bitcoin Bitcoin Vanilla Vanilla UTXO sẽ không phù hợp với Cardano, vì Cardano được thiết kế để thực hiện nhiều hơn là xử lý các khoản thanh toán.
Đặc biệt, sự cần thiết phải có nhiều biểu cảm lập trình cho chức năng hợp đồng thông minh sắp tới trong kỷ nguyên Alonzo yêu cầu một giải pháp tiểu thuyết (‘mở rộng).

The 'basic' UTXO model has a limited expressiveness of programmability. Ethereum's Account/Balance accounting model addressed this specific problem with the development of an account-based ledger and associated contract accounts. But by doing so, the semantics of the contract code became far more complex, which had the unwanted effect of forcing contract authors to fully grasp the nuances of the semantics to avoid the introduction of potentially very costly vulnerabilities in the code.

Mô hình UTXO 'cơ bản' có tính biểu cảm hạn chế về khả năng lập trình.
Mô hình kế toán tài khoản/số dư của Ethereum đã giải quyết vấn đề cụ thể này với việc phát triển sổ cái dựa trên tài khoản và các tài khoản hợp đồng liên quan.
Nhưng bằng cách đó, ngữ nghĩa của mã hợp đồng trở nên phức tạp hơn nhiều, điều này có tác dụng không mong muốn của việc buộc các tác giả hợp đồng nắm bắt hoàn toàn các sắc thái của ngữ nghĩa để tránh việc đưa ra các lỗ hổng có khả năng rất tốn kém trong mã.

An ‘extended’ UTXO solution would require two pieces of additional functionality that the existing UTXO model could not provide: 

Một giải pháp UTXO mở rộng sẽ yêu cầu hai phần chức năng bổ sung mà mô hình UTXO hiện tại không thể cung cấp:

1 - To be able to maintain the contract state

1 - Để có thể duy trì trạng thái hợp đồng

2 - To be able to enforce that the same contract code is used along the entire sequence of transactions. We call this continuity.

2 - Để có thể thực thi rằng cùng một mã hợp đồng được sử dụng dọc theo toàn bộ chuỗi giao dịch.
Chúng tôi gọi sự liên tục này.

A powerful feature of the EUTXO model is that the fees required for a valid transaction can be predicted precisely prior to posting it. This is a unique feature not found in account-based models.

Một tính năng mạnh mẽ của mô hình EUTXO là các khoản phí cần thiết cho một giao dịch hợp lệ có thể được dự đoán chính xác trước khi đăng nó.
Đây là một tính năng độc đáo không được tìm thấy trong các mô hình dựa trên tài khoản.

### **How does the EUTXO model extend UTXO?**

### ** Mô hình EUTXO mở rộng UTXO như thế nào? **

By adding custom data to outputs (in addition to value), and by allowing for more "locks" and "keys" deciding under which condition an output can be unlocked for consumption by a transaction. In other words, instead of just having public keys (hashes) for locks and corresponding signatures serving as "keys", EUTXO enables arbitrary logic in the form of scripts. This arbitrary logic inspects the transaction and the data to decide whether the transaction is allowed to use an input or not.

Bằng cách thêm dữ liệu tùy chỉnh vào đầu ra (ngoài giá trị) và bằng cách cho phép thêm "Khóa" và "Khóa" quyết định theo điều kiện nào có thể mở khóa để tiêu thụ bằng giao dịch.
Nói cách khác, thay vì chỉ có các khóa công khai (băm) cho các khóa và chữ ký tương ứng đóng vai trò là "khóa", EUTXO cho phép logic tùy ý dưới dạng tập lệnh.
Logic tùy ý này kiểm tra giao dịch và dữ liệu để quyết định xem giao dịch có được phép sử dụng đầu vào hay không.

### **Conclusion: What makes the EUTXO model innovative and relevant**

### ** Kết luận: Điều gì làm cho mô hình EUTXO sáng tạo và có liên quan **

Cardano's ledger model extends the UTXO model to support multi-assets and smart contracts without compromising the core advantages of a UTXO model. Our innovative research enables functionality beyond what is supported in any other UTXO ledger, making Cardano a unique competitor in the next-generation blockchain space.

Mô hình sổ cái của Cardano mở rộng mô hình UTXO để hỗ trợ các hợp đồng đa tài sản và hợp đồng thông minh mà không ảnh hưởng đến các lợi thế cốt lõi của mô hình UTXO.
Nghiên cứu sáng tạo của chúng tôi cho phép chức năng vượt ra ngoài những gì được hỗ trợ trong bất kỳ sổ cái UTXO nào khác, biến Cardano thành một đối thủ cạnh tranh độc đáo trong không gian blockchain thế hệ tiếp theo.

