# Xác thực giao dịch trên Cardano

### **Mô hình EUTXO của Cardano cho phép xác định rõ việc thực thi tập lệnh Plutus**

![](img/2021-09-06-no-surprises-transaction-validation-on-cardano.002.png) 6 tháng 9 năm 2021 ![](img/2021-09-06-no-surprises-transaction-validation-on-cardano.002.png) [Polina Vinogradova](tmp//en/blog/authors/polina-vinogradova/page-1/) ![](img/2021-09-06-no-surprises-transaction-validation-on-cardano.003.png) 12 phút đọc

![Polina Vinogradova](img/2021-09-06-no-surprises-transaction-validation-on-cardano.004.png)[](tmp//en/blog/authors/polina-vinogradova/page-1/)

### [**Polina Vinogradova**](tmp//en/blog/authors/polina-vinogradova/page-1/)

Research Engineer

Engineering

- ![](img/2021-09-06-no-surprises-transaction-validation-on-cardano.005.png)[](mailto:polina.vinogradova@iohk.io "Email")
- ![](img/2021-09-06-no-surprises-transaction-validation-on-cardano.006.png)[](https://ca.linkedin.com/in/polina-vinogradova-62105713b "LinkedIn")
- ![](img/2021-09-06-no-surprises-transaction-validation-on-cardano.007.png)[](https://twitter.com/polinavinovino "Twitter")
- ![](img/2021-09-06-no-surprises-transaction-validation-on-cardano.008.png)[](https://github.com/polinavino "GitHub")

![No-surprises transaction validation on Cardano](img/2021-09-06-no-surprises-transaction-validation-on-cardano.009.jpeg)

As the Alonzo hard fork brings core Plutus smart contract capability to Cardano, the ledger evolves to meet the growing need for the deployment of decentralized solutions. Cardano ledger design focuses on high assurance, security, and proven formal verification. In alignment with this strategy, it is also important to ensure that transaction processing is *deterministic*, meaning that a user can predict its impact and outcome before the actual execution.

The ability to guarantee the cost of transaction execution, and how the transaction behaves on the ledger *before* it is submitted, becomes even more prominent with the introduction of smart contract support. [Unspent Transaction Output (UTXO)](https://iohk.io/en/blog/posts/2021/03/11/cardanos-extended-utxo-accounting-model/)-based blockchains, like Cardano, provide such capabilities. Account-based blockchains, like Ethereum, are *indeterministic*, which means that they cannot guarantee the predictability of the transactionâ€™s effect on-chain. This presents risks of monetary loss, unpredictably high fees, and additional opportunities for adversarial behavior.

Trong bài này, chúng tôi xem xét kỹ hơn những lợi ích về thiết kế của Cardano cho phép đánh giá tập lệnh và sự an toàn của giao dịch trước khi thực hiện. Ở bài sau, vào cuối tuần này, chúng ta sẽ thảo luận về hai giai đoạn xác thực giao dịch trên Cardano.

## **Xác định giao dịch là gì và tại sao nó lại quan trọng?**

Tính xác định, trong bối cảnh giao dịch và xử lý tập lệnh được coi là giống với *khả năng dự đoán*. Điều này có nghĩa là người dùng có thể dự đoán cục bộ (ngoài chuỗi) rằng giao dịch của họ sẽ ảnh hưởng như thế nào đến trạng thái trên chuỗi của sổ cái mà không cần phải bận tâm tới:

- unexpected script validation outcomes or failures
- unexpected fees
- unexpected ledger or script state updates.

Một giao dịch trong hệ thống xác định vẫn có thể bị từ chối, ngay cả khi được thực hiện chính xác. *Bị từ chối* nghĩa là giao dịch hoàn toàn không thể được áp dụng cho sổ cái, do đó không ảnh hưởng đến trạng thái của nó, chính vì vậy nên không có chi phí nào được thanh toán. Điều này xảy ra khi các giao dịch được xử lý vào giữa thời điểm giao dịch ban đầu được thực hiện. Điều này cũng có thể xảy ra ngay cả với các giao dịch đơn giản. Ví dụ: một giao dịch khác có thể sử dụng UTXO mà một người cũng đang dự định dùng tới. Tính xác định đảm bảo rằng, bất cứ khi nào một giao dịch được chấp nhận, nó sẽ chỉ tác động tới trạng thái sổ cái (có thể dự đoán được).

## **Giải quyết vấn đề của <em>tính không xác định</em>**

*Tính không xác định* nghĩa là chúng ta không thể dự đoán những ảnh hưởng của một giao dịch trên sổ cái trước khi thực hiện. Khi thiết kế sổ cái, cũng như hợp đồng thông minh, điều quan trọng là phải thấy trước các điều kiện mà tính không xác định *có thể* xảy ra và đưa ra quyết định thiết lập để né tránh chúng. Một trong những nguy cơ là quyền truy cập vào dữ liệu sổ cái có thể thay đổi, tức là dữ liệu có thể tự thay đổi hoặc bị thay đổi. Tính không xác định có thể là vấn đề khi các thay đổi mà giao dịch hoặc hợp đồng thông minh thực hiện dựa trên sổ cái phụ thuộc vào trạng thái của nó tại thời điểm xử lý, thay vì chỉ phụ thuộc vào nội dung của giao dịch

Ethereum is notably susceptible to this problem. For example, gas prices, or a decentralized exchange (DEX) rate can fluctuate between the time a user submits a transaction and the time it gets processed. This results in unexpected gas fees, or price changes of assets being purchased. Or a script might simply fail, resulting in high execution costs (hundreds of dollars) and no other effect. This could occur, for instance, if the funds available to cover the gas costs run out mid-execution. Deterministic ledger design eliminates these possibilities.

Các nguồn không xác định có thể bao gồm việc cho phép các tập lệnh chứa:

- data in the block containing the transaction, but not included in any transaction, e.g., system randomness, block header, or the current slot number
- data altered or substituted by an adversary, which might change the outcome of script validation, while the transaction itself remains processable.

Trên các hệ thống, có nhiều cách để giảm thiểu những vấn đề này bằng phương pháp cải tiến lập trình hoặc giải pháp trên Layer 2. Cardano được thiết kế để đảm bảo kết quả có thể dự đoán cho tất cả các tập lệnh và giao dịch.

## **Tính xác định và lợi ích mô hình UTXO mang lại**

The Cardano ledger is built on a UTXO accounting model, which means that assets are stored on the ledger in *unspent outputs*, rather than in *accounts*. Each of these outputs specifies quantities of assets stored therein, together with its address. Unspent outputs are *immutable*, so a transaction might consume the entire output, but it cannot alter it.

To transfer assets, a transaction consumes one or more outputs and creates new ones, which, in total, contain the same quantities of assets as the ones consumed. These quantities -and their UTXO addresses- are specified in the outputs of the transaction. The only way a transaction can influence the effect of another transaction applied to the ledger is by spending the same UTXO as the later transaction attempts to spend, thus causing the node to reject it. This is the key feature on which the UTXO model relies for maintaining determinism.

Mô hình sổ cái UTXO có cả ưu điểm và nhược điểm so với mô hình dựa trên tài khoản. Không giống như UTXO, mô hình sổ cái dựa trên tài khoản chứa dữ liệu có thể thay đổi. Ví dụ, một giao dịch chứa các số lượng tài sản khác nhau trong một tài khoản, tùy thuộc vào việc nó được xử lý trước hay sau một giao dịch khác cập nhật cùng tài khoản đó. Trường hợp này có thể không khiến giao dịch bị từ chối, nhưng nó có thể dẫn đến những thay đổi "không thể đoán trước" trong sổ cái.

Việc sử dụng UTXO chỉ là một ví dụ về hành động mà một giao dịch có thể thực hiện. Tiếp theo, chúng tôi giải thích các hành động diễn ra trong giao dịch là gì và cách chúng được xác thực. Tập hợp các thay đổi quan trọng nhất được giới thiệu trong hard fork Alonzo là những thay đổi đối với quá trình xác thực hành động.

## **Xác thực các hành động bằng chữ ký và tập lệnh**

Điều quan trọng của việc xử lý giao dịch là xác thực các hành động mà nó thực hiện. Một giao dịch được *thực hiện* khi nó chứa dữ liệu cụ thể của hành động đó. Ví dụ: một giao dịch đang *sử dụng UTXO U* khi nó chứa tham chiếu U trong đầu vào và nó *tạo token X* khi bản thân nó chứa X.

Khi node xử lý một giao dịch, nó sẽ xác minh xem có thể thực hiện được hay không. Về việc này, người tiến hành giao dịch phải cung cấp các phần dữ liệu có liên quan, ví dụ: tập lệnh, trình xác nhận hoặc chữ ký. Một ví dụ phổ biến về hành động yêu cầu xác thực là sử dụng UTXO bị khóa bằng public key. Giao dịch phải cung cấp chữ ký từ private key tương ứng để thực hiện hành động này.

Cardano sử dụng các tập lệnh để xác thực các hành động. Các tập lệnh này là các đoạn mã dùng để triển khai các chức năng với đầu ra *Đúng* hoặc *Sai* . *Xác thực tập lệnh* là quá trình kết nối để chạy một tập lệnh nhất định trên các đối số thích hợp.

Xác thực tập lệnh có thể thực hiện các hành động sau:

- Sử dụng UTXO bị khóa bởi địa chỉ tập lệnh: tập lệnh được xử lý là tập lệnh có hàm băm tạo nên địa chỉ.
- Tạo ra token: tập lệnh được xử lý là tập lệnh có hàm băm tạo nên ID của token từ trước đó.
- Rút tiền thưởng: tập lệnh được xử lý là tập lệnh có hàm băm tạo thành địa chỉ staking.
- Áp dụng chứng chỉ: tập lệnh được xử lý là tập lệnh có hàm băm tạo thành thông tin đăng nhập của người khởi tạo.

Bên cạnh việc báo cho node biết tập lệnh nào sẽ được xử lý, tất cả các hành động giao dịch đều chỉ ra cách tập hợp các đối số được truyền tải cho tập lệnh đó.

Cardanoâ€™s multi-asset ledger (Mary) supports simple *multisig* and *timelock* scripting languages. These allow users to specify signatures required to perform an action (such as spending a UTXO or minting a non-fungible token (NFT)), and the time interval in which it can be performed. A timelock script can never see the actual slot number in the transaction that includes it. Timelock can only see the *validity interval* of the carrying transaction. Allowing a timelock script to see the current slot number (i.e., data coming from the block, rather than the author) would break determinism. This is ensured by the fact that a user cannot know the exact slot in which the transaction gets processed, and therefore they cannot predict how the script will behave.

Các tập lệnh của hard fork Mary, không giống trong các hợp đồng của Plutus ở hard fork Alonzo, nó bị hạn chế nhiều về khả năng diễn giải. Hard fork Alonzo mở ra một kỷ nguyên mới của các hợp đồng có tính hiệu quả rõ ràng mà không làm ảnh hưởng đến tài sản sổ cái.

## **Tập lệnh Plutus**

Alonzo introduces a new approach to transaction validation on Cardano due to the implementation of Plutus scripts. The [extended unspent transaction output](https://iohk.io/en/blog/posts/2021/03/12/cardanos-extended-utxo-accounting-model-part-2/) (EUTXO) model, deployed as part of Alonzo, provides the ledger infrastructure to support Plutus contracts. Below, we provide a high-level overview of ledger and transaction changes. For more details about working with the ledger and Plutus scripts, check out the [Plutus Pioneer program](https://www.youtube.com/watch?v=IEn6jUo-0vU&list=PLK8ah7DzglhhJzuiz7X33UCHSTYPB-8Jt)!

Alonzo thay đổi dữ liệu trên sổ cái dựa theo các yếu tố sau:

1. Tập lệnh Plutus có thể khóa các UTXO.
2. Phần nội dung mới được bổ sung tại các đầu ra của UTXO, cho phép chức năng giống như trạng thái tập lệnh. Ngoài nội dung và địa chỉ, UTXO bị khóa bởi tập lệnh Plutus cũng chứa một *datum*. Datum là một phần dữ liệu được diễn giải của trạng thái tập lệnh.
3. Có các tham số giao thức mới được sử dụng để áp đặt các yêu cầu xác thực bổ sung cho các giao dịch. Chúng bao gồm các giới hạn phía trên về tài nguyên tính toán mà các tập lệnh có thể sử dụng.

Để hỗ trợ tập lệnh Plutus, các giao dịch đã được nâng cấp như sau:

1. For each of its actions, the transaction now carries a user-specified argument, called a *redeemer*. Depending on the script, a redeemer can serve a different purpose. For example, it can act as the bid the user places in an auction, or the userâ€™s guess in a guessing game, among many other functions.
2. Giao dịch xác định ngân sách thực thi tính toán cho mỗi tập lệnh.
3. Để đảm bảo rằng một giao dịch có thể tự trả phí, Alonzo giới thiệu các phần dữ liệu bổ sung mà chúng ta sẽ thảo luận trong bài tiếp theo.
4. Các giao dịch chứa một hàm băm đầy đủ, cần thiết để đảm bảo rằng nó không bị tấn công, quá hạn, v.v.

Ngoài ra còn có một số thay đổi trong các chi tiết cụ thể của xác thực giao dịch hard fork Alonzo so với hard fork Mary. Đối với mỗi hành động, node tập hợp các đối số tập lệnh, bao gồm:

- the datum
- the redeemer
- execution budget
- a summary of the transaction.

Node thực hiện các phần việc mới, dành riêng cho Alonzo để đảm bảo giao dịch được tạo lập chính xác. Ví dụ: nó không được vượt quá ngân sách tối đa. Nó cũng kết hợp cùng Plutus để chạy các tập lệnh.

**Datum so với trạng thái tập lệnh**

Giống như các tài khoản có thể thay đổi, trạng thái tập lệnh có thể thay đổi được xếp chung vào danh mục "dữ liệu sổ cái có thể thay đổi". Chúng tôi thấy rằng mô hình UTXO tránh được vấn đề không xác định tài khoản có thể thay đổi. Nó cũng có thể giúp chúng ta hình dung lại khái niệm trạng thái theo cách duy trì tính xác định. Nếu một UTXO bị khóa bởi tập lệnh Plutus, thì mã tập lệnh của UTXO đó được liên kết với địa chỉ của nó. Tương tự trạng thái của tập lệnh này là dữ liệu được lưu trữ trong UTXO. Khi một giao dịch sử dụng UTXO đó, nó và dữ liệu sẽ bị xóa khỏi sổ cái. Tuy nhiên, nội dung của tập lệnh Plutus bắt buộc giao dịch chứa nó cũng phải tạo ra một UTXO chứa dữ liệu cụ thể được xem như trạng thái tập lệnh được cập nhật.

**Ngân sách thực thi tập lệnh**

The non-deterministic gas model can charge users unpredictably large fees. In Cardano scripts, this source of indeterminism is addressed by requiring that the resource budget itself, as well as the fee required to cover this budget, are included in the transaction. In Alonzo, a user can predict both locally when constructing the transaction. Script execution necessarily returns either *True* or *False*, and will not loop indefinitely. The reason for this is that every operation a script performs takes a non-zero amount of resources, which are tracked by the interpreter. If the budget specified by the transaction is exceeded, script execution terminates and returns *False*.

## **Xác thực giao dịch ở Alonzo**

Đối với việc giải quyết các nguồn không xác định, các điểm sau khiến kết quả của xác thực tập lệnh và giao dịch có thể dự đoán được:

- Quá trình thông dịch tập lệnh sẽ kết thúc và trả về cùng một kết quả xác thực khi được áp dụng cho các đối số giống nhau
- a transaction necessarily fixes all arguments that will be passed to the script interpreter during validation
- a transaction specifies all the actions it is taking that require script validation
- compulsory signatures on a transaction ensure that it cannot be altered by an adversary in a way that causes scripts to fail
- applying a transaction in the EUTXO ledger model is deterministic.

The last point is largely inherited from the UTXO model, as Alonzo ledger protocol updates remain, for the most part, consistent with updates in previous eras (including the delegation scheme, etc.). After the Alonzo upgrade, script validation failure or success does affect how a transaction is processed (more about this in part 2!). However, the *True* or *False* outcome, as well as ledger changes associated with either outcome, are predictable for a given transaction.

Hành vi xác định của tập lệnh Cardano và xác thực giao dịch không phải là kết quả tự nhiên của việc sử dụng mô hình EUTXO. Để đảm bảo thuộc tính này, nhóm IOG đã phải theo dõi cẩn thận nguồn của mọi dữ liệu mà tập lệnh được phép xem.

*The deterministic evaluation property is formally specified in the [Alonzo specification](https://hydra.iohk.io/build/7172824/download/1/alonzo-changes.pdf), and the IOG team has also sketched proof that the interpreter gets only those arguments that would not break the property.*

*In our second blog post, weâ€™ll take a closer look at the 2-phase validation process of Cardano transactions. So, keep an eye out later this week for part two.*
