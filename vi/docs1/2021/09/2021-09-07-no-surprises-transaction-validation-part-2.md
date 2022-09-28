# Xác thực giao dịch: phần 2

### **Alonzo transaction validation is performed in two phases to ensure fair compensation for validation work**

![](img/2021-09-07-no-surprises-transaction-validation-part-2.002.png) 7 tháng 9 năm 2021 ![](img/2021-09-07-no-surprises-transaction-validation-part-2.002.png) [Polina Vinogradova](tmp//en/blog/authors/polina-vinogradova/page-1/) ![](img/2021-09-07-no-surprises-transaction-validation-part-2.003.png) 7 phút đọc

![Polina Vinogradova](img/2021-09-07-no-surprises-transaction-validation-part-2.004.png)[](tmp//en/blog/authors/polina-vinogradova/page-1/)

### [**Polina Vinogradova**](tmp//en/blog/authors/polina-vinogradova/page-1/)

Research Engineer

Engineering

- ![](img/2021-09-07-no-surprises-transaction-validation-part-2.005.png)[](mailto:polina.vinogradova@iohk.io "Email")
- ![](img/2021-09-07-no-surprises-transaction-validation-part-2.006.png)[](https://ca.linkedin.com/in/polina-vinogradova-62105713b "LinkedIn")
- ![](img/2021-09-07-no-surprises-transaction-validation-part-2.007.png)[](https://twitter.com/polinavinovino "Twitter")
- ![](img/2021-09-07-no-surprises-transaction-validation-part-2.008.png)[](https://github.com/polinavino "GitHub")

![Xác thực giao dịch: phần 2](img/2021-09-07-no-surprises-transaction-validation-part-2.009.jpeg)

Trong [bài đăng trước trên Blog](https://iohk.io/en/blog/posts/2021/09/06/no-surprises-transaction-validation-on-cardano/), chúng tôi đã thảo luận về bản chất xác định của giao dịch và xác thực tập lệnh trên sổ cái Alonzo, cung cấp sự đảm bảo rằng kết quả của ứng dụng giao dịch trên chuỗi và xác thực tập lệnh có thể được dự đoán chính xác cục bộ, trước khi giao dịch được gửi đi.

Dựa trên những đảm bảo được cung cấp bởi thiết kế xác định của sổ cái Alonzo, chúng tôi đã triển khai một kế hoạch xác thực gồm hai giai đoạn cụ thể. Nó được thiết kế để giảm thiểu tài nguyên mà các node sử dụng để xác thực các giao dịch trên mạng lưới, đồng thời loại bỏ các chi phí không mong muốn cho người dùng. Trong bài đăng trên Blog này, chúng tôi đi sâu hơn vào cách hoạt động của xác thực hai giai đoạn.

In the Shelley, Allegra, and Mary eras, transaction validation was a one-step process. The effect of a valid transaction on the ledger was fully predictable before it was applied. If a transaction was valid, it got included into a block and added to the ledger. If not, a node would reject it after a failed validation attempt and the transaction would not be included in a block. However, nodes that validated incoming transactions used time and resources, regardless of whether or not the transaction ended up in a block.

Alonzo giới thiệu các tập lệnh Plutus, có thể yêu cầu nhiều tài nguyên hơn đáng kể để xác thực so với những tập lệnh đơn giản trong các kỷ nguyên trước. Để giải quyết vấn đề các node sử dụng tài nguyên để xác thực các tập lệnh của các giao dịch bị từ chối, Alonzo giới thiệu phương pháp xác thực hai giai đoạn. Chiến lược này duy trì một kết quả có thể dự đoán được của việc áp dụng các giao dịch vào sổ cái và cũng đảm bảo sự đền bù công bằng cho các node đối với công việc và việc sử dụng tài nguyên của chúng.

## **Xác thực giao dịch hai giai đoạn**

Transaction validation on Cardano is divided into two phases. The main reason for introducing two-phase validation is to limit the amount of uncompensated validation work by nodes. Each phase serves a purpose in achieving this goal. Roughly speaking, the first phase checks whether the transaction is constructed correctly and can pay its processing fee. The second phase runs the scripts included in the transaction. If the transaction is phase-1 valid, phase-2 scripts run. If phase-1 fails, no scripts run, and the transaction is immediately discarded.

Thus, nodes are expected to add processable transactions to a block even if the transactions are not phase-2 valid. This means that either:

- a small amount of uncompensated work is done by a node to find out that a transaction is not processable, but no expensive phase-2 validation is done, or
- the transaction is processable. The node can then perform phase-2 validation of the scripts, tag the transaction accordingly as either phase-2 valid or phase-2 invalid, and add it to a block. In either case, the node will later be compensated for both phases of validation via the fee or collateral collected from this transaction.

The expectation is that phase-2 failure should be rare, because a user submitting a transaction with failing scripts will lose ada while achieving nothing. This is locally predictable, and therefore a preventable event. The phase is a required safeguard to guarantee compensation for scriptsâ€™ potentially resource-intensive computation.

Chúng ta hãy xem xét cụ thể hơn các chi tiết của từng giai đoạn.

**Giai đoạn 1**

The first phase of validation must be simple. If this phase fails, a node does not get compensated for the work it has done, as it cannot accept processing fees from unprocessable transactions.

Xác thực giai đoạn 1 xác minh hai điều: một giao dịch được xây dựng chính xác và có thể thêm nó vào sổ cái. Việc xác thực này bao gồm các kiểm tra sau và một số kiểm tra bổ sung:

- it pays the correct amount of fees and provides the correct amount of collateral (i.e. ada collected in the case of script failure, explained below)
- Nó bao gồm tất cả dữ liệu cần thiết để thực thi các tập lệnh Plutus.
- Nó không vượt quá bất kỳ giới hạn nào được đặt trong các tham số giao thức (về kích thước đầu ra, v.v.).
- Đầu vào của nó đề cập đến các UTXO hiện có trên sổ cái.
- Ngân sách tính toán đã nêu không vượt quá giới hạn tài nguyên tối đa cho mỗi giao dịch.
- integrity hash checks, etc.

Before adding an incoming transaction to the mempool (and eventually, to a block), a node must perform all phase-1 validation checks. If any of these checks fail, the transaction is rejected without being included into a block, and no fees are charged. In previous eras, this was the only validation phase, and Cardano handled all validation failures in this fashion.

Các node trung thực và không bị xâm phạm sẽ không cố tình tạo ra các giao dịch không thể xử lý. Các node cũng có thể ngắt kết nối với kẻ tấn công cố tình thực hiện giao dịch không hợp lệ ở giai đoạn 1.

**Giai đoạn 2**

The second phase of validation runs Plutus scripts, which can be more computationally expensive. Therefore, fees are charged following either a success or a failure in the second phase. Collected ada goes into the fee pot, and thus compensates nodes for the resources used in the validation process.

Việc xác thực giai đoạn 1 thành công không đảm bảo rằng tất cả các hành động của giao dịch đều có thể xử lý được, chỉ có thể thu được tài sản thế chấp. Giai đoạn 2 thực hiện xác thực tập lệnh Plutus và quyết định thực hiện toàn bộ quá trình xử lý hay chỉ thu lại tài sản thế chấp được đưa ra dựa trên kết quả của việc xác thực:

- Áp dụng đầy đủ giao dịch (khả năng duy nhất trước Alonzo) - nếu các tập lệnh Plutus xác thực **tất cả** các hành động của giao dịch, hoặc
- Thu được ADA tài sản thế chấp và bỏ qua phần còn lại của giao dịch - nếu một trong các tập lệnh Plutus không thành công.

Hãy nhớ rằng kết quả xác thực tập lệnh có thể dự đoán cục bộ và được đảm bảo hoàn thành. Người dùng có thể kiểm tra cục bộ kết quả xác thực tập lệnh và sẽ không có bất đồng giữa các node trung thực về cách xử lý một giao dịch nhất định và các tập lệnh trong đó.

**Tài sản thế chấp**

If scripts don't validate, we still need to compensate the nodes for their work. But we can't just take money from the transaction inputs, because those might have been locked with scripts - those that failed! So instead, Alonzo introduces a special provision for this. The *collateral* of a transaction is the amount of ada that will be collected as a fee in case of a phase-2 script validation failure. In a processable transaction, this amount must be at least a certain percentage of the transaction fee, specified in a protocol parameter.

Số tiền này được xác định tại thời điểm xây dựng giao dịch. Không phải trực tiếp, mà bằng cách thêm *đầu vào tài sản thế chấp vào* giao dịch. Tổng số dư trong các UTXO tương ứng với các đầu vào được đánh dấu đặc biệt này là số tiền thế chấp của giao dịch. Các UTXO này phải có địa chỉ khóa công khai (thay vì tập lệnh) và không chứa Token nào khác ngoài ADA.

Các đầu vào tài sản thế chấp chỉ bị xóa khỏi sổ cái UTXO *nếu bất kỳ tập lệnh nào không được xác thực được giai đoạn 2*. Nếu tất cả các tập lệnh được thông qua, số tiền phí giao dịch đã xác định sẽ được thu lại, như trong các kỷ nguyên trước. Đặc biệt, số tiền đến từ các yếu tố đầu vào thông thường, không có tài sản thế chấp, và các yếu tố đầu vào tài sản thế chấp chỉ đơn giản là bị bỏ qua. Tin tốt là được phép sử dụng các đầu vào giống nhau như tài sản thế chấp và thông thường, vì chỉ một trong hai tập hợp được xóa khỏi UTXO.

Các chữ ký cần thiết để xác nhận việc chi tiêu các đầu vào tài sản thế chấp cũng đóng một vai trò quan trọng trong việc duy trì tính toàn vẹn của một giao dịch. Họ làm như vậy bằng cách ngăn chặn kẻ tấn công thay đổi nội dung để nó tiếp tục có thể xử lý được nhưng không xác nhận được giai đoạn 2. Ví dụ về điều này sẽ là một kẻ tấn thay thế một Redeemer. Cần có chữ ký của người nắm giữ khóa tài sản thế chấp để thực hiện thay đổi như vậy. Những người nắm giữ khóa tài sản thế chấp cũng là những người dùng duy nhất chịu mất bất kỳ ADA nào nếu quá trình xác thực tập lệnh không thành công.

Vì đánh giá tập lệnh là xác định, người nắm giữ khóa tài sản thế chấp có thể kiểm tra cục bộ xem giao dịch có vượt qua xác thực giai đoạn 2 trên chuỗi hay không trước khi họ ký nó. Nếu có, thì họ có thể chắc chắn rằng nó cũng sẽ hoạt động trên chuỗi và họ sẽ không bị mất tài sản thế chấp. Người dùng có thiện chí sẽ không bao giờ bị mất tài sản thế chấp. Điều đó cũng có nghĩa là họ có thể tái sử dụng cùng một đầu vào tài sản thế chấp cho nhiều giao dịch và đảm bảo tài sản thế chấp không bị thu lại.

*Now that we have launched the public Alonzo testnet, we welcome all users and developers to assess it by building and executing Plutus scripts. You can find out more information in the dedicated [Alonzo testnet repository](https://github.com/input-output-hk/Alonzo-testnet), or [discuss Plutus and Alonzo topics](https://discord.com/channels/826816523368005654/826829738156621895) with our diverse community.*
