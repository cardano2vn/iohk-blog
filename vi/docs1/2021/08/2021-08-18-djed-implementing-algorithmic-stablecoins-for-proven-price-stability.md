# Djed: Stablecoin thuật toán đã được xác minh chính thức

### **Djed is the first coin to use formal verification to eliminate price volatility**

![](img/2021-08-18-djed-implementing-algorithmic-stablecoins-for-proven-price-stability.002.png) 18 August 2021![](img/2021-08-18-djed-implementing-algorithmic-stablecoins-for-proven-price-stability.002.png)[ Olga Hryniuk](tmp//en/blog/authors/olga-hryniuk/page-1/)![](img/2021-08-18-djed-implementing-algorithmic-stablecoins-for-proven-price-stability.003.png) 7 mins read

![Olga Hryniuk](img/2021-08-18-djed-implementing-algorithmic-stablecoins-for-proven-price-stability.004.png)[](tmp//en/blog/authors/olga-hryniuk/page-1/)

### [**Olga Hryniuk**](tmp//en/blog/authors/olga-hryniuk/page-1/)

Technical Writer

Marketing &amp; Communications

- ![](img/2021-08-18-djed-implementing-algorithmic-stablecoins-for-proven-price-stability.005.png)[](https://www.linkedin.com/in/olga-hryniuk-1094a3160/ "LinkedIn")
- ![](img/2021-08-18-djed-implementing-algorithmic-stablecoins-for-proven-price-stability.006.png)[](https://github.com/olgahryniuk "GitHub")

![Djed: implementing algorithmic stablecoins for proven price stability](img/2021-08-18-djed-implementing-algorithmic-stablecoins-for-proven-price-stability.007.png)

Sự biến động của tiền mã hóa là một trong những trở ngại khi mở rộng khả năng áp dụng của nó. Công nghệ blockchain cung cấp các ưu điểm như tính minh bạch và bất biến của dữ liệu cũng như tính bảo mật đã được chứng minh cho các hoạt động tài chính. Tuy nhiên, việc dự đoán thị trường sẽ hoạt động như thế nào hoặc dự báo giá trị của một loại tiền mã hóa còn khó hơn so với các loại tiền pháp định. Điều này cản trở việc sử dụng tiền mã hóa làm đơn vị thanh toán và trao đổi trong các hoạt động hàng ngày.

A stablecoin is a cryptocurrency pegged to a basket of fiat currencies or a single currency (eg, USD or EUR); commodities like gold or silver; stocks; or other cryptocurrencies. Stablecoins include mechanisms that maintain a low price deviation from their target price and so are useful to store or exchange value, as their built-in mechanisms remove the volatility.

Một số stablecoin thiếu tính minh bạch và thanh khoản của nguồn dự trữ, điều này làm ảnh hưởng đến sự ổn định giá của chúng. Để giải quyết những thách thức này, IOG đã hợp tác với Emurgo, một trong ba đối tác sáng lập khác của Cardano và blockchain Ergo. Họ sử dụng mô hình sổ cái dựa trên UTXO như Cardano, để làm việc trên một hợp đồng stablecoin, được gọi là Djed. Các thuật toán được sử dụng để thiết kế Djed. Nghĩa là nó sử dụng các hợp đồng thông minh (smart contract) để đảm bảo tính ổn định giá và như vậy, đồng tiền này sẽ hữu ích cho các hoạt động tài chính phi tập trung (decentralized finance-DeFi).

## **How stablecoins work**

Different mechanisms contribute to the stability of the coinâ€™s value and help eliminate price variations. These mechanisms are underpinned by the economic principles of supply and demand.

Một cơ chế phổ biến để đảm bảo stablecoin là sử dụng một khoản dự trữ tiền tệ làm cột mốc. Nếu nhu cầu cao hơn lượng cung từ các lệnh bán hoặc mua, lượng cung này sẽ được tăng lên để tránh biến động về giá. Thông thường, lượng dự trữ stablecoin không được lưu trữ bằng tiền mặt. Thay vào đó, chúng được giữ trong các công cụ tài chính có lãi suất như trái phiếu. Lợi nhuận từ những thứ này mang lại doanh thu cho các nhà khai thác.

Miễn sao stablecoin được đảm bảo toàn bộ từ một khoản dự trữ dựa trên tiền tệ, được sử dụng làm cột mốc - và các nhà khai thác có thể phản ứng nhanh chóng trước các thay đổi của nhu cầu - đồng thời vẫn duy trì được sự ổn định giá.

## **Common risks**

Dự trữ stablecoin thường được kết hợp với các khoản đầu tư. Tính thiếu thanh khoản của các khoản đầu tư này có thể khiến nhà khai thác khó phản ứng nhanh trước các nhu cầu. Điều này làm ảnh hưởng đến sự ổn định giá trong ngắn hạn.

A drawback of fiat-backed stablecoins is that they require trust in the entities keeping the reserves. Lack of the reservesâ€™ transparency or of the â€˜full-backingâ€™ claim, combined with inefficient stabilization measures, have already caused Tether stablecoin (USDT) to fall below $0.96, as shown in Figure 1.

![USDT price](img/2021-08-18-djed-implementing-algorithmic-stablecoins-for-proven-price-stability.008.png)

Figure 1. Price of the Tether stablecoin (USDT) in the past three years

Issues of transparency do not arise when the backing asset is a cryptocurrency on a public blockchain. Furthermore, the use of smart contracts ensures efficient and reliable execution of stabilization measures due to its automated and secure mechanisms.

## **Enhanced stabilization mechanisms of Djed algorithmic stablecoin**

Djed là một hợp đồng stablecoin được đảm bảo bằng tiền mã hóa và hoạt động như một ngân hàng tự trị. Nó hoạt động bằng cách giữ một khoản dự trữ đồng cơ sở gọi là *base coin*, đồng thời đúc (minting) và đốt (burning) đồng *stablecoin* và *reserve coin* (đồng dự trữ). Hợp đồng duy trì mức cột mốc của stablecoin ở mức giá mục tiêu bằng cách mua và bán stablecoin, sử dụng khoản dự trữ và phí giao dịch được tích lũy trong khoản dự trữ, như được thể hiện trong Hình 2. Người hưởng lợi cuối cùng của nguồn doanh thu này là người nắm giữ reserve coin. Những người này tăng khoản dự trữ bằng cách ký quỹ trong quá trình giả định rủi ro biến động giá.

![How Djed works](img/2021-08-18-djed-implementing-algorithmic-stablecoins-for-proven-price-stability.009.png)

Figure 2. How Djed works

The Djed stablecoin is designed as an asset pegged to a fiat currency (USD), along with a governing algorithm. This approach provides a stable means of exchange. But Djed is not limited to being pegged to the dollar. It can work with other currencies, as long as there are oracles providing the contract with the corresponding pricing index.

## **The first formally verified stablecoin protocol**

Djed is the first *formally verified* stablecoin protocol. The use of formal methods in the programming process has greatly contributed to the design and stability properties of Djed. Using formal techniques, the properties are proven by mathematical theorems:

- **Cột mốc duy trì giới hạn trên và dưới**: giá sẽ không cao hơn hoặc thấp hơn mức giá đã đặt. Trong phạm vi tỷ lệ dự trữ thông thường, việc mua &amp; bán không bị hạn chế và người dùng không có động cơ để giao dịch stablecoin ngoài phạm vi neo giá trên thị trường thứ cấp.
- **Peg robustness during market crashes**: up to a set limit that depends on the reserve ratio, the peg is maintained even when the price of the base coin falls sharply.
- **No insolvency**: no bank is involved, so there is no bank contract to go bankrupt.
- **No bank runs**: all users are treated fairly and paid accordingly, so there is provably no incentive for users to race to redeem their stablecoins.
- **Monotonically increasing equity per reserve coin**: under some conditions, the reserve surplus per reserve coin is guaranteed to increase as users interact with the contract. Under these conditions, reserve coin holders are guaranteed to profit.
- **No reserve draining**: under some conditions, it is impossible for a malicious user to execute a sequence of actions that would steal reserves from the bank.
- **Bounded dilution**: there is a limit to how many reserve coin holders and their profit can be diluted due to the issuance of more reserve coins.

## **Các phiên bản của Djed**

There are two versions of Djed:

- **Minimal Djed**: this version is designed to be as simple, intuitive, and straightforward as possible, without compromising stability.
- **Extended Djed**: this more complex version provides some additional stability benefits. The main differences are the use of a continuous pricing model and dynamic fees to further incentivize the maintenance of the reserve ratio at an optimal level.

## **Implementations**

IOG, Ergo, and Emurgo teams have been working on the implementation of the Djed algorithmic stablecoin contract earlier in 2021 to test different models.

The first implementation of a Djed stablecoin contract was [SigmaUSD](https://sigmausd.io/#/) on Ergo. This was the first algorithmic stablecoin deployed on a UTXO-based ledger in Q1 2021. It had a fee of 1% for buying or selling operations, and an oracle that updated the exchange rate every hour. This initial version was subject to a reserve draining attack by an anonymous user who owned a large number of ERGs (Ergoâ€™s native coin). The attack was ultimately unsuccessful, and it is estimated that the attacker lost $100,000.

To further discourage such attacks, this initial deployment of Minimal Djed was replaced by a version where the fee was set to 2%, the oracle updated every 12 minutes, and every oracle update was allowed to change the price by at most 0.49%, unless the price difference was greater than 50%. This provided stronger resilience against reserve draining attacks.

Djed has also been implemented by the IOG team in Solidity. One version uses the native currency of the Ethereum blockchain as a base coin, and another uses any ERC20-compliant token as a base coin. So far, these implementations have been deployed to testnets for Binance Smart Chainâ€™s testnet, Avalancheâ€™s Fuji, Polygonâ€™s Mumbai, Ethereumâ€™s Kovan, Ethereumâ€™s Rinkeby, and RSKâ€™s testnet.

## **Djed: Triển khai trên Cardano**

The Alonzo update to Cardano will enable smart contracts using Plutus. Plutus is powered by Haskell, which guarantees a safe, full-stack programming environment.

Draft implementation of an earlier version of Minimal Djed is [available in the Plutus language](https://github.com/input-output-hk/plutus/blob/master/plutus-use-cases/src/Plutus/Contracts/Stablecoin.hs). In this implementation, stablecoins and reserve coins are native assets uniquely identified by the hash of the monetary policy that controls their minting and burning according to the Djed protocol. This implementation also assumes that oracle data such as the exchange rate is provided as signed data directly to the transactions, instead of being posted on-chain.

There is also an ongoing OpenStar implementation. OpenStar is a framework for private permissioned blockchains developed in Scala. The implementation of Djed using OpenStar follows the idea of off-chain smart contract execution to have a stablecoin on Cardano that does not depend on smart contracts executed on-chain.

To find out more about Djed stablecoin, see the [recently published research paper](https://iohk.io/en/research/library/papers/djeda-formally-verified-crypto-backed-pegged-algorithmic-stablecoin/) or check out the [presentation by Bruno Woltzenlogel Paleo](https://www.youtube.com/watch?v=zG-rxMCDIa0&t=8366s), IOG technical director, at Ergo summit 2021.

*Chúng tôi muốn cảm ơn và ghi nhận Bruno Woltzenlogel Paleo đã đóng góp ý kiến cho bài viết này và sự hỗ trợ trong suốt quá trình tạo ra nó. Bài dịch được dịch bởi Chitk, Review bởi Quang Pham, Biên tập bởi ... Bài viết nguồn [tại đây](https://iohk.io/en/blog/posts/2021/08/18/djed-implementing-algorithmic-stablecoins-for-proven-price-stability/).*Dự án này được tài trợ bởi Catalyst*.*
