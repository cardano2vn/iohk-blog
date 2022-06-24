# Cardano's secure switch to decentralization
### **The event will be ushered in with a ‘public assertion of randomness’, featuring entropy infused by the community**
![](img/2021-03-29-the-secure-transition-to-decentralization.002.png) 29 March 2021![](img/2021-03-29-the-secure-transition-to-decentralization.002.png)[ Prof Alexander Russell](tmp//en/blog/authors/alexander-russell/page-1/)![](img/2021-03-29-the-secure-transition-to-decentralization.003.png) 6 mins read

![Prof Alexander Russell](img/2021-03-29-the-secure-transition-to-decentralization.004.png)[](tmp//en/blog/authors/alexander-russell/page-1/)
### [**Prof Alexander Russell**](tmp//en/blog/authors/alexander-russell/page-1/)
Senior Research Fellow

Academic Research

- ![](img/2021-03-29-the-secure-transition-to-decentralization.005.png)[](mailto:alexander.russell@iohk.io "Email")
- ![](img/2021-03-29-the-secure-transition-to-decentralization.006.png)[](tmp///www.youtube.com/watch?v=KkcAic12dvc "YouTube")
- ![](img/2021-03-29-the-secure-transition-to-decentralization.007.png)[](https://github.com/russella "GitHub")

![Cardano's secure switch to decentralization](img/2021-03-29-the-secure-transition-to-decentralization.008.jpeg)

The security of proof-of-stake blockchains is provided by a mutually dependent relationship between its native token and the consensus mechanism that powers it: after all, electing nodes to issue blocks according to their stake requires a consistent global view of the stake distribution, while maintaining consistency itself requires a fair election mechanism. Indeed, the name Ouroboros – a classical symbol suggestive of mathematical recursion – was originally selected to draw attention to this relationship.

Bảo mật của các blockchain bằng chứng được cung cấp bởi mối quan hệ phụ thuộc lẫn nhau giữa mã thông báo gốc và cơ chế đồng thuận cung cấp năng lượng cho nó: sau tất cả, bầu các nút phát hành các khối theo cổ phần của họ đòi hỏi một quan điểm toàn cầu nhất quán về phân phối cổ phần,
Trong khi duy trì tính nhất quán chính nó đòi hỏi một cơ chế bầu cử công bằng.
Thật vậy, cái tên Ouroboros - một biểu tượng cổ điển gợi ý về đệ quy toán học - ban đầu được chọn để thu hút sự chú ý đến mối quan hệ này.

The Ouroboros protocol determines block producers via an evolving sequence of leadership nonces – each nonce runs the show for a 120-hour ‘epoch’, during which it contributes to determining which stake pools are chosen as the one-off leaders for block creation. Along with committing new transactions to the ledger, the blocks appearing in each epoch are additionally responsible for generating the leadership nonce for the following epoch – more recursion! All told, the leadership nonces and stake distributions evolve in concert to provide the fundamental ledger properties we demand of the system. 

Giao thức OuroBoros xác định các nhà sản xuất khối thông qua một chuỗi phát triển của các lãnh đạo không phải là-mỗi người không phát triển chương trình cho một ‘epoch 120 giờ, trong đó góp phần xác định các nhóm cổ phần nào được chọn là các nhà lãnh đạo một lần để tạo khối.
Cùng với việc thực hiện các giao dịch mới cho sổ cái, các khối xuất hiện trong mỗi epoch có trách nhiệm bổ sung để tạo ra sự không lãnh đạo cho thời đại sau - đệ quy hơn!
Tất cả đã nói, các nhà lãnh đạo không phải và phân phối cổ phần phát triển trong buổi hòa nhạc để cung cấp các thuộc tính sổ cái cơ bản mà chúng tôi yêu cầu của hệ thống.

The Cardano blockchain transitions to fully decentralized block production on March 31. Just afterwards, the running leadership nonce will be enhanced by adding in a ‘transition nonce’ that reflects entropy from a variety of external, unpredictable sources. Specifically, all transactions posted to the blockchain before Wednesday, April 7 at 15:44:51 UTC (slot 151200 of epoch 258) will play a distinguished role in the future of the blockchain: their accumulated hash value, reflected in the ‘previous-block hash’ from the first block on chain created on or after this time, will determine the transition nonce and hence directly contribute to the protocol’s perpetual cycle of randomness generation. 

Blockchain Cardano chuyển đổi sang sản xuất khối phi tập trung hoàn toàn vào ngày 31 tháng 3. Ngay sau đó, sự không hoạt động của Lãnh đạo sẽ được tăng cường bằng cách thêm vào một ’chuyển tiếp không phải là phản ánh entropy từ nhiều nguồn bên ngoài, không thể đoán trước.
Cụ thể, tất cả các giao dịch được đăng lên blockchain trước thứ Tư, ngày 7 tháng 4 lúc 15:44:51 UTC (SLOT 151200 của Epoch 258) sẽ đóng một vai trò nổi bật trong tương lai của blockchain: giá trị băm tích lũy của chúng, được phản ánh trong 'trước đó
Khối băm 'từ khối đầu tiên trên chuỗi được tạo vào hoặc sau thời gian này, sẽ xác định quá trình chuyển tiếp không và do đó đóng góp trực tiếp vào chu kỳ tạo ngẫu nhiên vĩnh viễn của giao thức.

IO Global scientists and engineers will contribute a number of specific, external, unpredictable sources of entropy. Additionally, to reflect the decentralized nature of Cardano we are asking the extended community, including stake pool operators and developers, to join us (on chain) for an event we’re calling the Cardano public assertion of randomness. This community exercise will establish the once-in-the-system’s-lifetime random 256-bit transition nonce that will herald the protocol’s official transition to decentralized operation.

Các nhà khoa học và kỹ sư toàn cầu IO sẽ đóng góp một số nguồn entropy cụ thể, bên ngoài, không thể đoán trước.
Ngoài ra, để phản ánh bản chất phi tập trung của Cardano, chúng tôi đang yêu cầu cộng đồng mở rộng, bao gồm các nhà khai thác và nhà phát triển nhóm cổ phần, tham gia với chúng tôi (trên chuỗi) cho một sự kiện mà chúng tôi gọi là sự ngẫu nhiên của Cardano.
Bài tập cộng đồng này sẽ thiết lập sự chuyển tiếp ngẫu nhiên 256 bit của hệ thống một lần, sẽ báo trước sự chuyển đổi chính thức của giao thức sang hoạt động phi tập trung.

We’re going to get more technical now so buckle up, or skip to the end.

Chúng tôi sẽ nhận được nhiều kỹ thuật hơn bây giờ để khóa, hoặc bỏ qua đến cùng.

## **Some background** 

## ** một số nền **

The Ouroboros protocol is organized into five-day (120-hour) periods called ‘epochs’. As described above, these coordinate two critical activities: updating the stake distribution and updating the leadership nonce. The proof of correctness of the protocol shows that it achieves an auspicious steady state: so long as an epoch begins with an unpredictable leadership nonce, it will deliver a fresh, unpredictable leadership nonce to the following epoch. To bootstrap the recursion, this public assertion event is designed to ensure this property of unpredictability. We remark that proof of work protocols are subject to similar randomness demands: famously, Nakamoto included the presumably unpredictable string ‘The Times 03/Jan/2009 Chancellor on brink of second bailout for banks’ in the [genesis block](https://en.bitcoin.it/wiki/Genesis_block#:~:text=Timestamp,days%20after%20the%20genesis%20block.) of Bitcoin.

Giao thức Ouroboros được tổ chức thành các khoảng thời gian năm ngày (120 giờ) được gọi là ‘Epochs.
Như đã mô tả ở trên, các điều phối hai hoạt động quan trọng này: cập nhật phân phối cổ phần và cập nhật các lãnh đạo không phải là lãnh đạo.
Bằng chứng về tính chính xác của giao thức cho thấy nó đạt được trạng thái ổn định tốt lành: miễn là một kỷ nguyên bắt đầu với một sự lãnh đạo không thể đoán trước, nó sẽ mang đến một sự lãnh đạo mới, không thể đoán trước cho kỷ nguyên sau.
Để khởi động đệ quy, sự kiện khẳng định công khai này được thiết kế để đảm bảo tính chất không thể đoán trước này.
Chúng tôi nhận xét rằng bằng chứng về các giao thức công việc phải tuân theo các yêu cầu ngẫu nhiên tương tự: nổi tiếng, Nakamoto bao gồm chuỗi có lẽ không thể đoán trước 'The Times 03/Jan/2009 Chancellor trên bờ vực cứu trợ thứ hai cho các ngân hàng' trong [khối Genesis] (https: //
en.bitcoin.it/wiki/Genesis_Block#:~:Text=Timestamp ,Day

## **The entropy mechanism and the timeline** 

## ** Cơ chế entropy và dòng thời gian **

Cardano’s implementation of the Ouroboros protocol provides an ‘entropy addition mechanism’ that can add a bitstring identified on the blockchain to subsequent leadership nonces; these are exactly the intended targets of the transition nonce. Naturally, this mechanism requires public declaration of the bitstring and explicit, cryptographically secure approval: specifically, only a collection of digitally signed votes from genesis delegates can complete the process. Furthermore, the process has a specific time horizon: votes must appear prior to the 48-hour mark in the epoch.

Việc thực hiện giao thức Ouroboros của Cardano cung cấp một cơ chế bổ sung entropy, có thể thêm một bitring được xác định trên blockchain cho các lãnh đạo tiếp theo không có;
Đây chính xác là các mục tiêu dự định của việc chuyển tiếp không.
Đương nhiên, cơ chế này yêu cầu tuyên bố công khai về sự chấp thuận an toàn, rõ ràng, rõ ràng về mặt mật mã: cụ thể, chỉ một bộ sưu tập phiếu bầu có chữ ký kỹ thuật số từ các đại biểu Genesis có thể hoàn thành quá trình.
Hơn nữa, quá trình này có một khoảng thời gian cụ thể: phiếu bầu phải xuất hiện trước mốc 48 giờ trong kỷ nguyên.

The epoch beginning on Monday, April 5 at 21:44:51 UTC (epoch 258) will invoke the entropy addition mechanism: in particular, the previous block hash appearing in the first block on or after Wednesday April 7 at 15:44:51 UTC (slot 151200 of epoch 258) will determine the transition nonce; this will take place roughly 42 hours after the epoch has begun and thus leave six hours for the genesis delegates to cast their votes. Recalling the hash chain structure of the Ouroboros blockchain, this hash value depends on the entire blockchain up to that point.

Epoch bắt đầu vào thứ Hai, ngày 5 tháng 4 lúc 21:44:51 UTC (Epoch 258) sẽ gọi cơ chế bổ sung entropy: đặc biệt, khối băm trước đó xuất hiện trong khối đầu tiên vào hoặc sau thứ Tư ngày 7 tháng 4 lúc 15:44:51
UTC (SLOT 151200 của Epoch 258) sẽ xác định quá trình chuyển tiếp không;
Điều này sẽ diễn ra khoảng 42 giờ sau khi thời đại đã bắt đầu và do đó để lại sáu giờ để các đại biểu Genesis bỏ phiếu.
Nhớ lại cấu trúc chuỗi băm của blockchain ouroboros, giá trị băm này phụ thuộc vào toàn bộ blockchain cho đến điểm đó.

Closely examining the correctness proofs of the protocol paints a more precise picture of the essential properties of the transition nonce: it must rely on random values – introduced in our setting via Cardano blockchain transactions – that cannot be predicted accurately when the stake distribution for the April 10 epoch is settled. This places special emphasis on transactions appearing in the blockchain between the 12-hour mark, when the stake distribution is firmly settled, and the 42-hour mark, when the hash value will be lifted.

Kiểm tra chặt chẽ các bằng chứng chính xác của giao thức vẽ nên một bức tranh chính xác hơn về các thuộc tính thiết yếu của quá trình chuyển tiếp: nó phải dựa vào các giá trị ngẫu nhiên - được giới thiệu trong cài đặt của chúng tôi thông qua các giao dịch blockchain cardano - không thể dự đoán chính xác khi phân phối cổ phần cho tháng 4
10 Epoch được giải quyết.
Điều này đặt sự nhấn mạnh đặc biệt vào các giao dịch xuất hiện trong blockchain giữa mốc 12 giờ, khi phân phối cổ phần được giải quyết chắc chắn và mốc 42 giờ, khi giá trị băm sẽ được nâng lên.

## **Entropy sources introduced by IO Global**

## ** Nguồn Entropy được giới thiệu bởi IO Global **

While the Cardano community is bound to introduce a wide variety of random sources – see below! – IO Global scientists and engineers will inject transactions with metadata determined by several public sources of entropy: hashes of the closing prices of the New York Stock Exchange on April 6, and real-time seismic data from the US Geological Survey, the University of Athens, and the Japan Meteorological Society. Seismic data from these sources will cover the first 36 hours of the epoch. Further details, including the scripts to be used for harvesting the data and the exact sources, appear in this [public github repository](https://github.com/input-output-hk/cardano-entropy).

Trong khi cộng đồng Cardano bị ràng buộc giới thiệu một loạt các nguồn ngẫu nhiên - xem bên dưới!
-Các nhà khoa học và kỹ sư toàn cầu của IO sẽ tiêm các giao dịch với siêu dữ liệu được xác định bởi một số nguồn entropy công cộng: băm giá đóng cửa của Sở giao dịch chứng khoán New York vào ngày 6 tháng 4 và dữ liệu địa chấn thời gian thực từ Khảo sát Địa chất Hoa Kỳ, Đại học Athens
và Hiệp hội Khí tượng Nhật Bản.
Dữ liệu địa chấn từ các nguồn này sẽ bao gồm 36 giờ đầu tiên của kỷ nguyên.
Thông tin chi tiết, bao gồm các tập lệnh được sử dụng để thu hoạch dữ liệu và các nguồn chính xác, xuất hiện trong [Kho lưu trữ GitHub công khai này) (https://github.com/input-output-hk/cardano-entropy).

We’d also like the more technical members of the Cardano community to join in too, by adding their own contribution to the randomness. Here’s what we’d like you to do.

Chúng tôi cũng thích các thành viên kỹ thuật hơn của cộng đồng Cardano cũng tham gia, bằng cách thêm đóng góp của riêng họ vào sự ngẫu nhiên.
Ở đây, những gì chúng tôi thích bạn làm.

- Select some entertaining sources of randomness: a lottery drawing from your region, a new RSA public key generated using your standard tools, or the outcome of a number of rolls of a 20-sided die. 

- Chọn một số nguồn ngẫu nhiên giải trí: Vẽ xổ số từ khu vực của bạn, khóa công khai RSA mới được tạo bằng các công cụ tiêu chuẩn của bạn hoặc kết quả của một số cuộn của một cái chết 20 mặt.

- Paste the result of these sources into a text document, save it, and hash the file using your favorite hash function, such as SHA256. Post this hash on the blockchain using a [transaction with metadata](https://github.com/input-output-hk/cardano-node/blob/master/doc/reference/tx-metadata.md). (See [this video](https://www.youtube.com/watch?v=fxNx4W1_gro&list=PLnPTB0CuBOBxjtuyI7sseODnMffpVHS2v&index=3&t=3s).)

- Dán kết quả của các nguồn này vào tài liệu văn bản, lưu nó và băm tệp bằng hàm băm yêu thích của bạn, chẳng hạn như SHA256.
Đăng băm này trên blockchain bằng cách sử dụng [giao dịch với siêu dữ liệu] (https://github.com/input-output-hk/cardano-node/blob/master/doc/reference/tx-metadata.md).
.

- To be most useful, your source of randomness should be determined after Tuesday, April 6 at 9:44:51 UTC (slot 43200 of epoch 258) and must be included in a blockchain transaction before Wednesday, April 7 at 15:44:51 UTC (slot 151200 of epoch 258).

- Để hữu ích nhất, nguồn ngẫu nhiên của bạn nên được xác định sau thứ ba, ngày 6 tháng 4 lúc 9:44:51 UTC (SLOT 43200 của Epoch 258) và phải được đưa vào một giao dịch blockchain trước thứ Tư, ngày 7 tháng 4 lúc 15:44:
51 UTC (khe 151200 của Epoch 258).

If you are less technical, you can still join in. You might like to test out an interesting new community tool, [Cardano Wall](https://cardanowall.com/en/). This allows you to easily write to the Cardano blockchain. However you choose to get involved, please announce your act of community service on social media, by publishing both your (unhashed) source along with the hash value appearing in your transaction.

Nếu bạn ít kỹ thuật hơn, bạn vẫn có thể tham gia. Bạn có thể muốn thử nghiệm một công cụ cộng đồng mới thú vị, [Cardano Wall] (https://cardanowall.com/en/).
Điều này cho phép bạn dễ dàng ghi vào blockchain Cardano.
Tuy nhiên, bạn chọn tham gia, vui lòng thông báo hành động dịch vụ cộng đồng của bạn trên phương tiện truyền thông xã hội, bằng cách xuất bản cả nguồn (chưa từng thấy) của bạn cùng với giá trị băm xuất hiện trong giao dịch của bạn.

*Thanks for your support and we’re looking forward to slot 151200 when we can convene, in spirit, for a ‘block party’ to watch the genesis delegates’ votes appear on-chain!*

*Cảm ơn sự hỗ trợ của bạn và chúng tôi mong chờ SLOT 151200 khi chúng tôi có thể triệu tập, về tinh thần, cho một bữa tiệc khối để xem các đại biểu của các đại biểu Genesis xuất hiện trên chuỗi!*

