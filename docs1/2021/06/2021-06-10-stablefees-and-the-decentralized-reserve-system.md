# Stablefees and the Decentralized Reserve System
### **Exploring a new mechanism to help make fees fair, stable, and more predictable over time**
![](img/2021-06-10-stablefees-and-the-decentralized-reserve-system.002.png) 10 June 2021![](img/2021-06-10-stablefees-and-the-decentralized-reserve-system.002.png)[ Prof Aggelos Kiayias](tmp//en/blog/authors/aggelos-kiayias/page-1/)![](img/2021-06-10-stablefees-and-the-decentralized-reserve-system.003.png) 7 mins read

![Prof Aggelos Kiayias](img/2021-06-10-stablefees-and-the-decentralized-reserve-system.004.png)[](tmp//en/blog/authors/aggelos-kiayias/page-1/)
### [**Prof Aggelos Kiayias**](tmp//en/blog/authors/aggelos-kiayias/page-1/)
Chief Scientist

Academic Research

- ![](img/2021-06-10-stablefees-and-the-decentralized-reserve-system.005.png)[](mailto:aggelos.kiayias@iohk.io "Email")
- ![](img/2021-06-10-stablefees-and-the-decentralized-reserve-system.006.png)[](tmp///www.youtube.com/watch?v=nB6eDbnkAk8 "YouTube")

![Stablefees and the Decentralized Reserve System](img/2021-06-10-stablefees-and-the-decentralized-reserve-system.007.jpeg)

Facilitating transactions in cryptocurrency platforms stumbles on the dual utility of the platformâ€™s underlying asset. On the one hand, users can hold and trade it as part of their investment portfolios. On the other hand, it supplies the necessary â€œfuelâ€ for processing transactions. This duality suggests that the system should have a mechanism for adjusting transaction costs, so they remain competitive and reasonable. Also, the bounded throughput of decentralized platforms per unit of time introduces another hurdle: the system should also allow the users to discover the correct price for timely transaction processing, depending on their individual needs. 

Tạo điều kiện cho các giao dịch trong các nền tảng tiền điện tử vấp ngã vào tiện ích kép của tài sản cơ bản của nền tảng.
Một mặt, người dùng có thể nắm giữ và giao dịch nó như một phần của danh mục đầu tư của họ.
Mặt khác, nó cung cấp cho các giao dịch cần thiết cho các giao dịch.
Tính hai mặt này cho thấy rằng hệ thống nên có một cơ chế để điều chỉnh chi phí giao dịch, vì vậy chúng vẫn cạnh tranh và hợp lý.
Ngoài ra, thông lượng giới hạn của các nền tảng phi tập trung mỗi đơn vị thời gian giới thiệu một trở ngại khác: hệ thống cũng sẽ cho phép người dùng khám phá giá chính xác để xử lý giao dịch kịp thời, tùy thuộc vào nhu cầu cá nhân của họ.

Why not drop transaction fees altogether? Three reasons: One, transaction processing incurs costs on the systemâ€™s side (in terms of computation and storage). It is reasonable to allow transaction processors (stake pool operators, in the case of Cardano) to offset their costs. Two, even with a theoretically infinite capacity, it is important to prevent transaction issuers from saturating the network with worthless transactions. Three, it is appropriate to incentivize transaction processors to provide quality of service. A surge in demand should influence their payoffs accordingly.

Tại sao không bỏ phí giao dịch hoàn toàn?
Ba lý do: một, xử lý giao dịch gây ra chi phí ở phía hệ thống (về mặt tính toán và lưu trữ).
Thật hợp lý khi cho phép các bộ xử lý giao dịch (các nhà khai thác nhóm cổ phần, trong trường hợp của Cardano) để bù đắp chi phí của họ.
Hai, ngay cả với năng lực vô hạn về mặt lý thuyết, điều quan trọng là ngăn chặn các nhà phát hành giao dịch bão hòa mạng với các giao dịch vô giá trị.
Ba, phù hợp để khuyến khích các bộ xử lý giao dịch cung cấp chất lượng dịch vụ.
Một sự gia tăng trong nhu cầu sẽ ảnh hưởng đến tiền chi trả của họ cho phù hợp.

Adding a fee to each transaction can address the above considerations. 

Thêm một khoản phí cho mỗi giao dịch có thể giải quyết các cân nhắc trên.

### **Bitcoin and beyond**

### ** Bitcoin và hơn thế nữa **

Bitcoin set out the first mechanism for pricing transactions in distributed ledger platforms. This mechanism resembles a first-price auction: transactions bid for a place in a block naming a specific reward, and block producers select the transactions that they prefer to include. Block producers also get rewarded with the right to mint new coins, i.e., their operation is subsidized by the whole community via inflation of the total coin supply. Inflation drops geometrically over time, and transaction fees become increasingly dominant in the rewards. This mechanism, while enabling Bitcoin to run for well over a decade, has been criticized for its inefficiency. Transaction costs have also risen over time.

Bitcoin đặt ra cơ chế đầu tiên cho các giao dịch định giá trong các nền tảng sổ cái phân tán.
Cơ chế này giống như một cuộc đấu giá giá đầu tiên: Giá thầu giao dịch cho một vị trí trong một khối đặt tên một phần thưởng cụ thể và các nhà sản xuất khối chọn các giao dịch mà họ thích bao gồm.
Các nhà sản xuất khối cũng được thưởng bằng quyền Mint mới, tức là, hoạt động của họ được toàn bộ cộng đồng trợ cấp thông qua lạm phát của tổng nguồn cung.
Lạm phát giảm về mặt hình học theo thời gian và phí giao dịch ngày càng chiếm ưu thế trong phần thưởng.
Cơ chế này, trong khi cho phép Bitcoin chạy trong hơn một thập kỷ, đã bị chỉ trích vì sự kém hiệu quả của nó.
Chi phí giao dịch cũng tăng theo thời gian.

In this blog post, we explore a new mechanism that builds on Cardano's approach to ledger rules and system assets, and complements the [Babel fees](https://iohk.io/en/blog/posts/2021/02/25/babel-fees/) concept. The objective is making fees fair, stable, and predictable over time. We describe the mechanism in the context of Cardano. However, it can be adapted to any other cryptocurrency with similar characteristics.

Trong bài đăng trên blog này, chúng tôi khám phá một cơ chế mới dựa trên cách tiếp cận của Cardano đối với các quy tắc và tài sản hệ thống của Cardano và bổ sung cho [phí Babel] (https://iohk.io/en/blog/posts/2021/02/25/
Babel-fees/) khái niệm.
Mục tiêu là làm cho phí công bằng, ổn định và có thể dự đoán theo thời gian.
Chúng tôi mô tả cơ chế trong bối cảnh Cardano.
Tuy nhiên, nó có thể được điều chỉnh với bất kỳ loại tiền điện tử nào khác với các đặc điểm tương tự.

### **Introducing 'Stablefees'**

### ** Giới thiệu 'StableFees' **

The core idea behind Stablefees is to have a base price for transactions through pegging to a basket of commodities or currencies. Stablefees includes a native "decentralized reserve" contract that issues and manages a stablecoin pegged to the basket. A comparison in the fiat world might be the International Monetary Fundâ€™s[SDR](https://www.imf.org/en/About/Factsheets/Sheets/2016/08/01/14/51/Special-Drawing-Right-SDR), (established in 1969) and valued based on a basket of five currenciesâ€”the U.S. dollar, the euro, the Chinese renminbi, the Japanese yen, and the British pound sterling. The stablecoin --- letâ€™s call it "Basket Equivalent Coin" (BEC) --- is the currency used for paying transaction fees (and all other real world pricing needs of the platform, e.g., SPO costs). 

Ý tưởng cốt lõi đằng sau StableFees là có một mức giá cơ bản cho các giao dịch thông qua việc gắn kết một rổ hàng hóa hoặc tiền tệ.
StableFees bao gồm một hợp đồng "Dự trữ phi tập trung" bản địa, các vấn đề và quản lý một stablecoin được chốt vào giỏ.
Một so sánh trong thế giới fiat có thể là [SDR] của Quỹ Tiền tệ Quốc tế (https://www.imf.org/en/about/factsheets/sheets/2016/08/01/14/51/special-drawing
-Right-sdr), (được thành lập năm 1969) và được đánh giá cao dựa trên một rổ năm loại tiền tệ của đồng đô la Mỹ, đồng euro, tái tạo Trung Quốc, đồng yên Nhật Bản và đồng bảng Anh.
StableCoin --- Hãy gọi nó là "đồng tiền tương đương rổ" (BEC) --- là loại tiền được sử dụng để trả phí giao dịch (và tất cả các nhu cầu định giá trong thế giới thực khác của nền tảng, ví dụ, chi phí SPO).

In this system, ada will play a dual role: Reserve asset of the decentralized reserve, and reward currency for staking. It will also be the fall-back currency in extreme scenarios where the reserve contract is in a liquidity crunch. Before a transaction, the issuer will have to obtain BECs, either via other third parties or directly by sending ada to the decentralized reserve contract. On what basis will the reserve issue BECs? The reserve contract will also issue equity shares -we will call them decentralized equity coins (DECs)-, in exchange of ada. Leveraging the value of DECs, the decentralized reserve will often adjust the value of BEC so it is pegged on the underlying basket of commodities. In other words, DECs will absorb the fluctuations of ada vs. the basket to ensure that the real-world value of BECs remains stable (cf. the [AgeUSD stablecoin design](https://github.com/Emurgo/age-usd) that has been already [deployed and used on Ergo](https://sigmausd.io/#/)). 

Trong hệ thống này, ADA sẽ đóng một vai trò kép: tài sản dự trữ của dự trữ phi tập trung và tiền thưởng cho việc đặt cược.
Nó cũng sẽ là loại tiền tệ mùa thu trong các tình huống cực đoan trong đó hợp đồng dự trữ trong một cuộc khủng hoảng thanh khoản.
Trước một giao dịch, nhà phát hành sẽ phải có được BECS, thông qua các bên thứ ba khác hoặc trực tiếp bằng cách gửi ADA đến hợp đồng dự trữ phi tập trung.
Trên cơ sở nào sẽ phát hành dự trữ BECS?
Hợp đồng dự trữ cũng sẽ phát hành cổ phiếu vốn -chúng tôi sẽ gọi chúng là tiền vốn tài trợ (DECS) -, để đổi lấy ADA.
Tận dụng giá trị của DECS, Khu bảo tồn phi tập trung thường sẽ điều chỉnh giá trị của BEC để nó được chốt trên giỏ hàng hóa cơ bản.
Nói cách khác, DECS sẽ hấp thụ các biến động của ADA so với giỏ để đảm bảo rằng giá trị trong thế giới thực của BECS vẫn ổn định (x.
) đã được [triển khai và sử dụng trên ERGO] (https://sigmausd.io/#/)).

This trinity of coinage, issued natively by the system, will attract different cohorts. BECs' stability and liquidity might be attractive to risk-averse, transaction-intensive holders. DECs will offer the highest rewards if ada goes up, but also take the most significant hit when ada goes down. Long-term holders may find DECs more attractive. Also, since decentralized reserve prices these coins in ada, both BECs and DECs can facilitate participation in staking and governance. Returns can be issued at different rates, reflecting the different nature of each coin. Ultimately, rewards will always be denominated and payable in ada, which will remain the most versatile of all three coins.

Bộ ba tiền này, được hệ thống ban hành, sẽ thu hút các đoàn hệ khác nhau.
Sự ổn định và thanh khoản của BECS có thể hấp dẫn đối với những người nắm giữ ít rủi ro, chuyên sâu giao dịch.
DECS sẽ cung cấp phần thưởng cao nhất nếu ADA đi lên, nhưng cũng có một cú đánh đáng kể nhất khi ADA đi xuống.
Những người nắm giữ lâu dài có thể thấy DEC hấp dẫn hơn.
Ngoài ra, vì giá dự trữ phi tập trung, các đồng tiền này ở ADA, cả BECS và DEC đều có thể tạo điều kiện cho việc tham gia vào việc đặt cược và quản trị.
Trả lại có thể được phát hành ở các mức giá khác nhau, phản ánh bản chất khác nhau của mỗi đồng tiền.
Cuối cùng, phần thưởng sẽ luôn được định mệnh và phải trả trong ADA, sẽ vẫn là linh hoạt nhất trong cả ba đồng tiền.

### **Oracles**

### ** oracles **

The centerpiece of this mechanism is an on-chain oracle that determines the price of the basket in ada. SPOs can implement this oracle in a decentralized manner. The reserve can offer extra rewards to all oracle contributors from the fees collected during BEC/DEC issuances. This will ensure two things: thousands of geographically-diverse contributors, and ledger rules calculating a synthesized exchange rate in some canonical way (through a weighted median across all price submissions in an epoch, for example). If oracle contributors manipulate their contributions, they can be held accountable by tracking their reputation and performance on-chain.

Trung tâm của cơ chế này là một nhà tiên tri trên chuỗi xác định giá của giỏ trong ADA.
SPO có thể thực hiện nhà tiên tri này một cách phi tập trung.
Dự trữ có thể cung cấp thêm phần thưởng cho tất cả những người đóng góp của Oracle từ các khoản phí được thu thập trong quá trình phát hành BEC/DEC.
Điều này sẽ đảm bảo hai điều: hàng ngàn người đóng góp đa dạng về mặt địa lý và các quy tắc sổ cái tính toán tỷ giá hối đoái tổng hợp theo một cách chính tắc (thông qua một trung bình có trọng số trên tất cả các bài nộp giá trong một kỷ nguyên, chẳng hạn).
Nếu những người đóng góp của Oracle thao túng những đóng góp của họ, họ có thể chịu trách nhiệm bằng cách theo dõi danh tiếng và hiệu suất của họ trên chuỗi.

### **The pricing mechanism**

### ** Cơ chế định giá **

How would one price transactions and reward block producers? Using the current approach in Cardano, each transaction will be deterministically mapped to a precise value denominated in BECs, using a formula determined by the ledger rules. The formula will take into account both transaction size and its computational requirements, and may also incorporate runtime metrics (such as the average system load). The resulting value will be the base fee guaranteeing that the transaction will be processed by the system. Given the base fee, end users will be able to apply a multiplier if they wish (which will be a value at least 1, e.g., 1.5x, 3x, etc.) to increase the fee and accelerate processing. This will become relevant at times of surging demand. 

Làm thế nào một giao dịch giá và các nhà sản xuất khối thưởng?
Sử dụng phương pháp hiện tại trong Cardano, mỗi giao dịch sẽ được ánh xạ xác định theo giá trị chính xác được mệnh giá trong BECS, sử dụng một công thức được xác định bởi các quy tắc sổ cái.
Công thức sẽ tính đến cả kích thước giao dịch và các yêu cầu tính toán của nó và cũng có thể kết hợp các số liệu thời gian chạy (như tải hệ thống trung bình).
Giá trị kết quả sẽ là phí cơ sở đảm bảo rằng giao dịch sẽ được hệ thống xử lý.
Với phí cơ sở, người dùng cuối sẽ có thể áp dụng hệ số nhân nếu họ muốn (sẽ là giá trị ít nhất 1, ví dụ: 1,5 lần, 3x, v.v.) để tăng phí và tăng tốc xử lý.
Điều này sẽ trở nên có liên quan tại thời điểm nhu cầu tăng.

This approach has one advantage when compared with the first-price auction model: the pricing mechanism is continuously stabilized to a reasonable default value. Users perform price discovery in one direction only to accelerate processing, if required. Also, transaction issuers can store BECs to secure their future transaction-issuing ability without being affected by ada price volatility.

Cách tiếp cận này có một lợi thế khi so sánh với mô hình đấu giá giá đầu tiên: cơ chế định giá liên tục ổn định với giá trị mặc định hợp lý.
Người dùng thực hiện khám phá giá theo một hướng chỉ để tăng tốc xử lý, nếu được yêu cầu.
Ngoài ra, các nhà phát hành giao dịch có thể lưu trữ BECS để đảm bảo khả năng phát hành giao dịch trong tương lai của họ mà không bị ảnh hưởng bởi biến động giá ADA.

### **Stablefees and Babel fees**

### ** STABLEFEES VÀ BABEL Phí **

The Stablefees mechanism can be considered a natural extension of [Babel fees](https://iohk.io/en/blog/posts/2021/02/25/babel-fees/) ---spot conversion of BECs into ada by the decentralized reserve. Both mechanisms complement (and are compatible with) each other. Babel fees can be deployed together with Stablefees with just one change: Using BECs to cover Babel fee liabilities, instead of ada. This also means that fees will always be payable in ada (via a Babel fee liability convertible in ada on the spot). Hence, the whole mechanism is backwards compatible: it wonâ€™t affect occasional users who just hold ada and do not wish to obtain BECs. 

Cơ chế stablefees có thể được coi là một phần mở rộng tự nhiên của [phí Babel] (https://iohk.io/en/blog/posts/2021/02/25/babel-fees/) --- Chuyển đổi SPOT của BEC thành ADA bởi
Khu bảo tồn phi tập trung.
Cả hai cơ chế bổ sung (và tương thích với) nhau.
Phí Babel có thể được triển khai cùng với StableFees chỉ với một thay đổi: sử dụng BECS để trang trải các khoản nợ phí của Babel, thay vì ADA.
Điều này cũng có nghĩa là các khoản phí sẽ luôn phải trả trong ADA (thông qua trách nhiệm pháp lý phí Babel tại ADA ngay tại chỗ).
Do đó, toàn bộ cơ chế tương thích ngược: nó sẽ không ảnh hưởng đến người dùng thỉnh thoảng chỉ giữ ADA và không muốn có được BECS.

A final point about diversity. While the above narrative identifies a unique and global BEC, the same mechanism can be used to issue regional BECs pegged to different baskets of commodities, which could possibly be weighted differently. Such â€œregionalâ€ BECs will be able to increase system inclusivity, while enabling SPOs to have more fine-grained policies in terms of transaction inclusion.

Một điểm cuối cùng về sự đa dạng.
Mặc dù tường thuật ở trên xác định một BEC duy nhất và toàn cầu, nhưng cùng một cơ chế có thể được sử dụng để phát hành các BEC khu vực được gắn với các giỏ hàng hóa khác nhau, có thể có trọng số khác nhau.
Các BECS "như vậy sẽ có thể tăng tính bao gồm hệ thống, đồng thời cho phép các SPO có nhiều chính sách chi tiết hơn về mặt bao gồm giao dịch.

### **Stablefees 'lite'**

### ** stablefees 'lite' **

The above mechanism requires a decentralized reserve contract and the issuance of BECs and DECs by the contract to buyers. A â€œliteâ€ version avoids the reserve contract and directly adjusts the fee formula by pegging it onto the agreed basket of commodities through the price oracle. The resulting system denominates transaction fees nominally in BECs and immediately converts them into ada. The payable amount fluctuates, depending on the value of BEC. The mechanism is otherwise identical, also facilitating unidirectional price discovery through the multiplier. The only disadvantage is that a prospective transaction issuer has no access to a native token that enables transaction processing predictably; transaction issuers must pay fees in ada. Still, the fees will continuously adjust and remain stable via the pegging mechanism with respect to the basket. As a result, a transaction issuer will be able to organize their off-chain asset portfolio to meet their transaction needs effectively.

Cơ chế trên yêu cầu một hợp đồng dự trữ phi tập trung và ban hành BECS và DECS bằng hợp đồng cho người mua. Một phiên bản â € "Tránh hợp đồng dự trữ và trực tiếp điều chỉnh công thức lệ phí bằng cách dán nó vào giỏ hàng hóa đã thỏa thuận thông qua giá. Hệ thống kết quả có giá trị phí giao dịch trên danh nghĩa trong BECS và ngay lập tức chuyển đổi chúng thành ADA. Số tiền phải trả dao động, tùy thuộc vào giá trị của BEC. Cơ chế khác là giống hệt nhau, cũng tạo điều kiện cho việc phát hiện giá một chiều thông qua hệ số nhân. Nhược điểm duy nhất là nhà phát hành giao dịch tiềm năng không có quyền truy cập vào mã thông báo gốc cho phép xử lý giao dịch có thể dự đoán được; Nhà phát hành giao dịch phải trả phí trong ADA. Tuy nhiên, các khoản phí sẽ liên tục điều chỉnh và duy trì ổn định thông qua cơ chế gắn kết đối với giỏ. Do đó, một nhà phát hành giao dịch sẽ có thể tổ chức danh mục tài sản ngoài chuỗi của họ để đáp ứng nhu cầu giao dịch của họ một cách hiệu quả.

### **The road ahead**

### **Con đường phía trước**

Our team is currently researching the granular details of the Stablefees mechanism. Once this research is complete, Stablefees can be integrated into Cardano to offer fair and predictable transaction pricing. Moreover, the price oracle and the global BEC (and regional variants, if included) will undoubtedly find uses beyond paying transaction fees, expanding the capabilities of decentralized applications in the Cardano ecosystem.

Nhóm của chúng tôi hiện đang nghiên cứu các chi tiết chi tiết của cơ chế stablefees.
Khi nghiên cứu này hoàn tất, StableFees có thể được tích hợp vào Cardano để cung cấp giá giao dịch công bằng và có thể dự đoán được.
Hơn nữa, giá Oracle và BEC toàn cầu (và các biến thể khu vực, nếu được bao gồm) chắc chắn sẽ tìm thấy việc sử dụng ngoài phí giao dịch, mở rộng khả năng của các ứng dụng phi tập trung trong hệ sinh thái Cardano.

