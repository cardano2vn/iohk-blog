# Nghiên cứu tổng quan phần 3: Tokens, Stablecoin, và phí.

### **IOG research enabled the implementation of multi-asset support, stablecoins, and friendly fees on Cardano**

![](img/2022-07-07-research-overview-part-3-tokens-stablecoins-and-fees.002.png) 7 July 2022![](img/2022-07-07-research-overview-part-3-tokens-stablecoins-and-fees.002.png)[ Olga Hryniuk](/en/blog/authors/olga-hryniuk/page-1/)![](img/2022-07-07-research-overview-part-3-tokens-stablecoins-and-fees.003.png) 5 mins read

![Olga Hryniuk](img/2022-07-07-research-overview-part-3-tokens-stablecoins-and-fees.004.png)[](/en/blog/authors/olga-hryniuk/page-1/)

### [**Olga Hryniuk**](/en/blog/authors/olga-hryniuk/page-1/)

Technical Writer

Marketing &amp; Communications

- ![](img/2022-07-07-research-overview-part-3-tokens-stablecoins-and-fees.005.png)[](https://www.linkedin.com/in/olga-hryniuk-1094a3160/ "LinkedIn")
- ![](img/2022-07-07-research-overview-part-3-tokens-stablecoins-and-fees.006.png)[](https://github.com/olgahryniuk "GitHub")

![Nghiên cứu tổng quan phần 3: Tokens, Stablecoin, và phí.](img/2022-07-07-research-overview-part-3-tokens-stablecoins-and-fees.007.png)

[Bài đăng trước](https://iohk.io/en/blog/posts/2022/06/23/overview-of-the-research-enabling-smart-contract-support-on-cardano/) của chúng tôi đã thảo luận về sự đột phá của mô hình EUTxO trên mạng Cardano và cách nó tạo điều kiện để Smart contract trên Cardano hoạt động. Lần này, chúng tôi xem xét kỹ hơn nghiên cứu cho phép hỗ trợ đa tài sản và tạo ra nhiều loại tokens do người dùng xác nhận và chúng tôi cũng thảo luận về lợi ích của phí Babel.

## **Multi-asset support**

Ethereum is known for providing the ability to create various user-defined assets (tokens). However, Ethereumâ€™s token standards are not directly supported by the ledger and require repetitive custom code. This adds a layer of complexity, extra cost, and inefficiency since token code is replicated and adapted rather than being part of the system itself. This leaves room for human error and can introduce bugs potentially leading to financial losses.

Bài báo nghiên cứu ' [UTXOma: UTXO with Multi-Asset Support](https://iohk.io/en/research/library/papers/utxomautxo-with-multi-asset-support/)' của các nhà khoa học của IOG và được trình bày tại hội nghị ISoLA 2020. Bài báo nghiên cứu việc tạo ra một loạt các token do người dùng tạo thông qua các tập lệnh hợp đồng được gọi là *chính sách đúc tiền* .

Bài báo khám phá một thiết kế thay thế cho việc tạo tài sản do người dùng xác nhận dựa trên những sổ cái UTXO của Bitcoin. Nó đề xuất một phần mở rộng của mô hình UTXO, trong đó cấu trúc tính toán của một loại tiền điện tử duy nhất được thay thế bằng một cấu trúc mới quản lý một số lượng không giới hạn các token gốc, do người dùng xác nhận, được gọi là *các gói token*.

In this new model, token creation is controlled by minting policy scripts that, just like Bitcoin validator scripts, use a domain-specific language with bounded computational expressiveness. This favors Bitcoinâ€™s security and results in a lightweight and low cost approach to custom asset creation and transfer.

The â€˜[Native Custom Tokens in the Extended UTXO Model](https://iohk.io/en/research/library/papers/native-custom-tokens-in-the-extended-utxo-model/)â€™ paper suggests a generalization of the EUTXO model with native user-defined tokens. The paper explores the synergy between the native tokens from UTXOma with expressive smart contracts on the basis of a UTXO ledger as proposed by the EUTXO model. This results in more expressive minting policies and a direct mapping of versatile contracts based on state machines to the multi-asset EUTXO ledger. The paper formally establishes the correctness of this mapping.

## **Stable coin Djed**

Bên cạnh các token tùy chỉnh, IOG đã thực hiện nghiên cứu về việc triển khai một stablecoin trên Cardano. Bài báo ‘[Djed: A Formally Verified Crypto-Backed Pegged Algorithmic Stablecoin](https://iohk.io/en/research/library/papers/djed-a-formally-verified-crypto-backed-pegged-algorithmic-stablecoin/)’  được xuất bản vào năm 2021.

The paper introduces a stablecoin contract based on algorithmic design, which uses smart contracts to ensure price stabilization. This is a very useful feature for decentralized finance (DeFi) environments. [Djed acts as an autonomous bank](https://iog.io/en/blog/posts/2021/08/18/djed-implementing-algorithmic-stablecoins-for-proven-price-stability/). It mints and burns stablecoins and reserve coins while keeping a reserve of base coins. The contract maintains the peg of stablecoins to a target price by buying and selling stablecoins, using the reserve, and charging fees, which accumulate in the reserve.

Djed hiện đang được [triển khai bởi COTI.](https://iog.io/en/blog/posts/2021/09/26/coti-to-issue-djed-stablecoin-on-cardano/)

## **Phí Babel**

Những lợi ích của mô hình EUTXO đa tài sản của Cardano đã mở ra một con đường nghiên cứu khác dẫn đến '[phí Babel](https://iohk.io/en/research/library/papers/babel-fees-via-limited-liabilities/)'. Phí Babel là một cơ chế cho phép thanh toán phí giao dịch bằng các đồng tiền khác ngoài ada trên Cardano. Bài báo đã được chấp thuận để xuất bản tại [ACNS 2022](https://acns22.di.uniroma1.it/home), diễn ra vào tháng sáu.

Blockchain transactions require fees for their execution. To ensure network security, fees usually must be paid in the currency native to a chosen blockchain, like ada on Cardano, for example. However, allowing the fee to be paid in other valuable tokens that a user possesses improves the convenience of use and also benefits interoperability. IOGâ€™s research in the paper on Babel fees explains how this is possible.

Several innovative features of Cardano, such as the EUTXO model and custom native assets are coming together to enable Babel fees. Cardanoâ€™s multi-asset support allows for the creation of tokens treated as native on the ledger. This means that new user-defined tokens â€” if only enough users consider them valuable â€” can be used to pay transaction fees just like ada, Cardanoâ€™s primary currency.

Manuel Chakravarty, nhà khoa học về Lambda và là kiến ​​trúc sư Plutus tại IOG cho biết:

Cardano encourages special-interest communities to form around new custom tokens that these communities create themselves using Plutus. Members of these communities may possess plenty of liquidity in a custom token without holding much ada. To support such communities, we want them to be able to pay for the use of the network using their own tokens.

So when a user wishes to pay the transaction fee in tokens other than ada, they can make such an offer by way of a Babel fee transaction offering a custom token, but incurring an ada liability. A block producer that validates this transaction can then accept this offer setting up a spot trade between ada and the offered token(s) at a previously advertised exchange rate. The block producer then creates a second transaction, covering the fee in ada, while receiving the offered tokens in exchange. By suitably extending the ledger rules, the transaction with the liability - as well as its matching transaction - become admissible to the ledger as a group. The beauty of the scheme is that users who stake their ada still get the staking reward paid out in ada as usual.

Manuel Chakravarty cho biết thêm:

Bước tiếp theo đối với việc triển khai phí Babel trên Cardano là viết một Đề xuất cải tiến Cardano (CIP) trên các cơ sở của bài báo nghiên cứu. Chúng tôi sẽ trình bày điều này cho cộng đồng thảo luận ngay sau khi phiên bản đầu tiên hoàn thành.

*Với sự hỗ trợ đa tài sản và hợp đồng thông minh được giới thiệu trên Cardano vào năm 2020-2021, sổ cái đã trở thành một môi trường chức năng để tạo ra vô số ứng dụng phi tập trung (DApps). Hiện với hơn một nghìn dự án được xây dựng trên Cardano, nghiên cứu và phát triển của IOG tập trung vào việc mở rộng quy mô và tối ưu hóa sự ổn định của Cardano. Vì vậy, trong bài blog tiếp theo, chúng tôi sẽ phản ánh nhiều hơn về nghiên cứu thúc đẩy khả năng mở rộng và khả năng tương tác của Cardano.<br><br><br>Bài này được dịch bởi Lê Nguyên. <a class="_active_edit_href" href="https://iohk.io/en/blog/posts/2022/07/07/research-overview-part-3-tokens-stablecoins-and-fees/">với bài gốc</a><br><em>Dự án này được tài trợ bới Catalyst</em>*
