# Boosting Cardano’s throughput with script referencing
### **We take a closer look at just some of the enhancements coming to Cardano in June** 
![](img/2022-04-13-boosting-cardano-s-throughput-with-script-referencing.002.png) 13 April 2022![](img/2022-04-13-boosting-cardano-s-throughput-with-script-referencing.002.png)[ Olga Hryniuk](tmp//en/blog/authors/olga-hryniuk/page-1/)![](img/2022-04-13-boosting-cardano-s-throughput-with-script-referencing.003.png) 4 mins read

![Olga Hryniuk](img/2022-04-13-boosting-cardano-s-throughput-with-script-referencing.004.png)[](tmp//en/blog/authors/olga-hryniuk/page-1/)
### [**Olga Hryniuk**](tmp//en/blog/authors/olga-hryniuk/page-1/)
Technical Writer

Marketing & Communications

- ![](img/2022-04-13-boosting-cardano-s-throughput-with-script-referencing.005.png)[](https://www.linkedin.com/in/olga-hryniuk-1094a3160/ "LinkedIn")
- ![](img/2022-04-13-boosting-cardano-s-throughput-with-script-referencing.006.png)[](https://github.com/olgahryniuk "GitHub")

![Boosting Cardano’s throughput with script referencing](img/2022-04-13-boosting-cardano-s-throughput-with-script-referencing.007.jpeg)

During the Basho development phase, the ledger continues to optimize and scale for the growing demand. Along with parameter adjustments and node upgrades, Plutus capability continues to develop at a steady pace.

Trong giai đoạn phát triển Basho, sổ cái tiếp tục tối ưu hóa và mở rộng quy mô cho nhu cầu ngày càng tăng.
Cùng với điều chỉnh tham số và nâng cấp nút, khả năng Plutus tiếp tục phát triển với tốc độ ổn định.

Plutus is a living, evolving smart contract language. [Cardano improvement proposals](https://cardanofoundation.org/en/news/make-it-even-better-cardanos-improvements-proposals/) – also known as CIPs – play an important role in this evolution. Through the CIP mechanism, anyone can suggest an improvement to Cardano. CIPs encourage community engagement and proposal reviews, which are continually maintained on the Cardano Foundation’s [GitHub repository](https://github.com/cardano-foundation/CIPs).

Plutus là một ngôn ngữ hợp đồng thông minh sống, phát triển.
.
Thông qua cơ chế CIP, bất cứ ai cũng có thể đề xuất cải thiện Cardano.
CIP khuyến khích các đánh giá đề xuất và tham gia của cộng đồng, liên tục được duy trì trên Cardano Foundation [Kho lưu trữ GitHub] (https://github.com/cardano-poundation/cips).

Let’s drill down into two of these. CIPs for [reference inputs](https://github.com/cardano-foundation/CIPs/pull/159) (CIP-31) and [reference scripts](https://github.com/cardano-foundation/CIPs/pull/161) (CIP-33) have been submitted to be implemented on Cardano and are among those due to be implemented as part of June’s *Vasil* hard fork. Along with other [scalability improvements](https://iohk.io/en/blog/posts/2022/01/14/how-we-re-scaling-cardano-in-2022/), these enhancements to Plutus will boost throughput for decentralized apps (DApps) decentralized finance (DeFi), RealFi, products, smart contracts, and exchanges building or operating on Cardano.

Hãy để đi sâu vào hai trong số này.
CIP cho [đầu vào tham chiếu] (https://github.com/cardano-foundation/cips/pull/159) (CIP-31) và [tập lệnh tham chiếu] (https://github.com/cardano-foundation/cips//cips/
kéo/161) (CIP-33) đã được gửi để được triển khai trên Cardano và nằm trong số đó do được thực hiện như một phần của hard hard * vasil * tháng sáu.
Cùng với [cải tiến khả năng mở rộng] khác (https://iohk.io/en/blog/posts/2022/01/14/how-we-re-scaling-cardano-in-2022/), những cải tiến này đối với Plutus sẽ tăng cường
Thông lượng cho các ứng dụng phi tập trung (DAPPS) Tài chính phi tập trung (DEFI), RealFi, sản phẩm, hợp đồng thông minh và trao đổi xây dựng hoặc vận hành trên Cardano.

In this post, we take a closer look at what these CIPs are and how they benefit and optimize Cardano's scalability.

Trong bài đăng này, chúng tôi xem xét kỹ hơn về những CIP này là gì và cách chúng có lợi và tối ưu hóa khả năng mở rộng của Cardano.

## **Reference inputs**

## ** Đầu vào tham chiếu **

Transaction outputs carry *datums*, which enable the storage and access to information on the blockchain. However, these datums are constrained in a number of ways. For example, to access datum’s information, you’d have to spend the output that the datum is attached to. This requires the re-creation of a spent output. Any user who wishes to look at the data cannot spend the old output (which is gone), but must spend the new output (which they will not know about until the next block). In practice, this limits some applications to one ‘operation’ per block, thus decreasing the desired performance.

Đầu ra giao dịch mang *mốc dữ liệu *, cho phép lưu trữ và truy cập thông tin trên blockchain.
Tuy nhiên, các dữ liệu này bị hạn chế theo một số cách.
Ví dụ: để truy cập thông tin Datum, bạn phải chi tiêu đầu ra mà mốc dữ liệu được đính kèm.
Điều này đòi hỏi phải tạo lại một đầu ra đã sử dụng.
Bất kỳ người dùng nào muốn xem dữ liệu đều không thể chi tiêu đầu ra cũ (đã biến mất), nhưng phải chi tiêu đầu ra mới (mà họ sẽ không biết cho đến khối tiếp theo).
Trong thực tế, điều này giới hạn một số ứng dụng ở một ’hoạt động trên mỗi khối, do đó làm giảm hiệu suất mong muốn.

CIP-31 introduces a new mechanism for accessing information in datums – a reference input. Reference inputs allow looking at an output without spending it. This will facilitate access to information stored on the blockchain without the need for spending and re-creating unspent transaction outputs (UTXOs).

CIP-31 giới thiệu một cơ chế mới để truy cập thông tin trong mốc dữ liệu-một đầu vào tham chiếu.
Đầu vào tham chiếu cho phép nhìn vào đầu ra mà không chi tiêu.
Điều này sẽ tạo điều kiện truy cập vào thông tin được lưu trữ trên blockchain mà không cần chi tiêu và tạo lại các đầu ra giao dịch không sử dụng (UTXOS).

Reference inputs also enable the other key improvement – reference scripts.

Đầu vào tham chiếu cũng cho phép cải tiến khóa khác - tập lệnh tham chiếu.

## **Reference scripts**

## ** Các tập lệnh tham chiếu **

When you spend an output locked with a Plutus script, you must include the script in the spending transaction. Hence, the size of the scripts contributes to transaction size, which directly influences Cardano’s throughput.

Khi bạn dành một đầu ra bị khóa với tập lệnh Plutus, bạn phải đưa tập lệnh vào giao dịch chi tiêu.
Do đó, quy mô của các tập lệnh đóng góp vào quy mô giao dịch, điều này ảnh hưởng trực tiếp đến thông lượng của Cardano.

Large script sizes pose problems for users because:

Kích thước tập lệnh lớn đặt ra vấn đề cho người dùng vì:

1. Larger transactions result in higher fees.

1. Giao dịch lớn hơn dẫn đến phí cao hơn.

1. Transactions have size limits. Large scripts can hit the limits. Even if one script fits, multiple scripts in one transaction might not fit. This makes it difficult to execute complex transactions that rely on several scripts.

1. Giao dịch có giới hạn kích thước.
Các kịch bản lớn có thể đạt đến các giới hạn.
Ngay cả khi một tập lệnh phù hợp, nhiều tập lệnh trong một giao dịch có thể không phù hợp.
Điều này gây khó khăn cho việc thực hiện các giao dịch phức tạp dựa trên một số tập lệnh.

CIP-33 suggests script referencing as a possible solution. This is the ability to reference a script without including it in each transaction, which hugely reduces the contribution of scripts to the transaction size. Referencing scripts in multiple transactions can significantly reduce transaction sizes, improve throughput, and reduce script execution costs.

CIP-33 gợi ý tham chiếu tập lệnh như một giải pháp khả thi.
Đây là khả năng tham khảo một tập lệnh mà không bao gồm nó trong mỗi giao dịch, điều này làm giảm mạnh mẽ sự đóng góp của các tập lệnh vào quy mô giao dịch.
Tham khảo các tập lệnh trong nhiều giao dịch có thể giảm đáng kể quy mô giao dịch, cải thiện thông lượng và giảm chi phí thực hiện tập lệnh.

**How does script referencing work?**

** Làm thế nào để tham chiếu tập lệnh hoạt động? **

The idea is to use reference inputs and outputs that carry actual scripts (reference scripts). The script referencing proposal eliminates sending frequently-used scripts to the chain every time they are used. Instead, scripts will be available in a persistent way on-chain. This means that the transaction using the script will not need to include the script itself, as long as it references the output that contains it.

Ý tưởng là sử dụng các đầu vào tham chiếu và đầu ra mang các tập lệnh thực tế (tập lệnh tham chiếu).
Đề xuất tham khảo tập lệnh loại bỏ các tập lệnh được sử dụng thường xuyên đến chuỗi mỗi khi chúng được sử dụng.
Thay vào đó, các tập lệnh sẽ có sẵn một cách dai dẳng trên chuỗi.
Điều này có nghĩa là giao dịch sử dụng tập lệnh sẽ không cần bao gồm chính tập lệnh, miễn là nó tham chiếu đầu ra có chứa nó.

This approach follows the reference inputs proposal ([CIP-31](https://github.com/cardano-foundation/CIPs/pull/159)). CIP-31 considers how to enable data sharing on-chain, and concludes that referencing UTXOs is the most appropriate solution. UTXOs store data safely, and take advantage of the existing mechanisms for size control.

Cách tiếp cận này tuân theo đề xuất đầu vào tham chiếu ([CIP-31] (https://github.com/cardano-foundation/cips/pull/159)).
CIP-31 xem xét cách kích hoạt chia sẻ dữ liệu trên chuỗi và kết luận rằng tham chiếu UTXOS là giải pháp phù hợp nhất.
UTXOS lưu trữ dữ liệu một cách an toàn và tận dụng các cơ chế hiện có để kiểm soát kích thước.

For reference scripts, transaction outputs must be extended to carry an optional field to include a script. The minimum UTXO value for such outputs will depend on the size of the script, following the coinsPerUTxOWord protocol parameter.

Đối với các tập lệnh tham chiếu, đầu ra giao dịch phải được mở rộng để mang theo một trường tùy chọn để bao gồm một tập lệnh.
Giá trị UTXO tối thiểu cho các đầu ra như vậy sẽ phụ thuộc vào kích thước của tập lệnh, theo tham số giao thức COINSPERUTXOWORD.

## **Community engagement is key**

## ** Sự tham gia của cộng đồng là chìa khóa **

With the proposals already submitted and implemented, Plutus script referencing and reference inputs are planned to be included in the June *Vasil* hard fork. The CIP process enables the community to contribute to the development of Cardano by proposing, discussing, reviewing, and contributing to improvement proposals. We encourage the developer community to join CIP discussions and visit [Cardano Foundation’s CIP repository](https://github.com/cardano-foundation/CIPs) for more details.

Với các đề xuất đã được gửi và thực hiện, các đầu vào tham chiếu và tham chiếu của Plutus Script được lên kế hoạch để đưa vào hard fork * vasil * tháng sáu.
Quá trình CIP cho phép cộng đồng đóng góp cho sự phát triển của Cardano bằng cách đề xuất, thảo luận, xem xét và góp phần cải tiến các đề xuất.
Chúng tôi khuyến khích cộng đồng nhà phát triển tham gia các cuộc thảo luận CIP và truy cập [Kho lưu trữ CIP của Cardano Foundation] (https://github.com/cardano-foundation/cips) để biết thêm chi tiết.

