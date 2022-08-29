# Tất cả những gì bạn cần biết về layer 1 và layer 2 của blockchain

### **Khi thảo luận về kiến trúc blockchain, các thuật ngữ 'layer 1' và 'layer 2' thường được đề cập. Đây là những khái niệm quan trọng phục vụ hai mục đích: giải thích cách blockchain được xây dựng và cung cấp hình ảnh trực quan dễ hiểu để hình dung blockchain trông như thế nào. Hãy cùng tìm hiểu về chúng dưới đây.**

![](img/2022-08-05-layer-1-layer-2-all-you-need-to-know.002.png) 5 tháng 8 năm 2022![](img/2022-08-05-layer-1-layer-2-all-you-need-to-know.002.png) [Fernando Sanchez](/en/blog/authors/fernando-sanchez/page-1/)![](img/2022-08-05-layer-1-layer-2-all-you-need-to-know.003.png) 13 phút đọc

![Fernando Sanchez](img/2022-08-05-layer-1-layer-2-all-you-need-to-know.004.png)[](/en/blog/authors/fernando-sanchez/page-1/)

### [**Fernando Sanchez**](/en/blog/authors/fernando-sanchez/page-1/)

Technical Writer

Marketing and Communications

- ![](img/2022-08-05-layer-1-layer-2-all-you-need-to-know.005.png)[](mailto:fernando.sanchez@iohk.io "E-mail")
- ![](img/2022-08-05-layer-1-layer-2-all-you-need-to-know.006.png)[](https://www.linkedin.com/in/linkedinsanchezf/ "LinkedIn")

![Lớp 1 & Lớp 2: tất cả những gì bạn cần biết](https://github.com/cardano2vn/iohk-blog/blob/main/vi/docs1/2022/08/img/2022-08-05-layer-1-layer-2-all-you-need-to-know.007.jpeg?raw=true)

Layer 1: Nói về định nghĩa

Hãy tưởng tượng một chiếc bánh cưới nhiều tầng, được trang trí với bức tượng nhỏ của cô dâu chú rể ở trên cùng. Chiếc bánh bắt mắt này nằm trên một giá đỡ có chân đế vững chắc. Với hình ảnh chiếc bánh này, phần đế chắc chắn và vững vàng đó là tầng đầu tiên (layer 1) hỗ trợ cấu trúc chiếc bánh. Đây là cách mà blockchain được xây dựng. Trong blockchain, layer 1 là nền móng của mạng lưới để xây dựng các giải pháp cho layer 2 bên trên.

![](img/2022-08-05-layer-1-layer-2-all-you-need-to-know.008.jpeg)

## **Layer 1: Chức năng**

Với hình dung kể trên, Cardano là layer 1 (là mạng cơ sở), bản thân nó bao gồm ba lớp độc lập:

- Lớp mạng lưới
- Lớp đồng thuận
- Lớp sổ cái

**Lớp mạng lưới**

Lớp này duy trì các kết nối giữa tất cả các node phân tán trong mạng lưới Cardano, ghi nhận các khối mới được tạo ra từ node, tạo các giao dịch mới được đúc vào khối và lan truyền khối giữa các node.

**Lớp đồng thuận**

Lớp này thực hiện hai chức năng cơ bản:

- Chạy giao thức đồng thuận [Ouroboros](https://www.essentialcardano.io/glossary/ouroboros) . Lớp này đưa ra các quyết định như nhận khối nào, lựa chọn chuỗi nào khi có xung đột và quyết định khi nào tạo ra các khối của riêng nó.
- Duy trì các trạng thái cần thiết để đưa ra các quyết định được thực hiện trong lớp đồng thuận.

**Lớp sổ cái**

Lớp này quy định:

- Trạng thái của sổ cái đang như thế nào.
- Sổ cái phải được cập nhật như thế nào cho mỗi khối mới.

Lớp sổ cái đơn thuần có chức năng chỉ định việc chuyển đổi trạng thái giữa các sổ cái. Lý do cho điều này bắt nguồn từ quy tắc sổ cái chính thức, đã và đang dùng mô hình kế toán UTxO mở rộng (hay còn gọi là EUTxO). Việc chuyển đổi trạng thái này được chỉ định bởi tập hợp các giao dịch trong các khối Cardano, hoặc từ các sự kiện nổi bật như chuyển đổi các epoch.

Lớp đồng thuận không cần biết chi tiết chính xác trạng thái sổ cái, cũng như nội dung của các khối, ngoại trừ các trường tiêu đề cần thiết để chạy giao thức đồng thuận.

Về tổng thể, ba lớp kể trên tạo thành giải pháp layer 1 của Cardano.

## **Layer 1: Khả năng mở rộng**

Lấy lại ví dụ chiếc bánh cưới. Nó là chiếc bánh lớn với các tầng xếp chồng lên nhau. Nhưng hãy nhìn vào nền móng, phần đế bánh này. Phần này đó có kích thước cố định và không thể tự dưng lớn hơn. Nhưng kích thước của nó cần phải đủ lớn để nâng các tầng nằm phía trên. Các tầng phía trên cũng cần có kích thước phù hợp, tất cả tạo nên ý nghĩa của một chiếc bánh nhiều tầng. Mỗi tầng (suy nghĩ layer) sẽ bày trí thêm một yếu tố tương thích vào phần nền móng. Lớp kem nền, phủ tuyết, các kiểu trang trí khác ... Nói cách khác, lớp nền móng sẽ gánh ngày một nhiều khối lượng của các tầng phía trên nó.

Cuộc các mạng phi tập trung cho cộng đồng cũng gặp phải vấn đề tương tự. Như phần đế bánh chỉ có thể chứa được một khối lượng bánh vừa phải phía trên nó, phần mạng cơ sở (layer 1) chỉ có thể xử lý lượng giao dịch nhất định. Nếu bạn cố gắng thêm nhiều bánh hơn khả năng chịu của đế, chiếc bánh chắc chắn không còn nguyên vẹn dẫn đến hỏng mất ngày trọng đại này. Tương tự, các node trong mạng layer 1 chỉ có thể xử lý một lượng giao dịch nhất định trước khi xảy ra tắc nghẽn. Khi phát triển số lượng người dùng, chúng ta sẽ cần nhiều node hơn để xử lý các nhu cầu giao dịch. Để giải quyết vấn đề này, mạng cần phải được mở rộng quy mô, nếu không các giao dịch sẽ bắt đầu tụt hậu.

Có nhiều cách để mở rộng quy mô mạng layer 1. Ví dụ: tăng kích thước khối để các khối mang nhiều dữ liệu giao dịch hơn. Kích thước khối gần đây đã tăng thêm 8KB để lên 72KB (tăng 12,5%). Đây là một trong những cách Cardano sẽ mở rộng quy mô trong năm 2022.

Quay lại hình ảnh chiếc bánh cưới, việc thêm tầng không chỉ làm cho cả chiếc bánh lớn hơn, mà nó còn cho thấy khả năng nâng đỡ vững chắc của tầng nền móng. Ta có thể trình bày các tầng riêng biệt với các hương vị, nhân, kiểu dáng khác nhau, v.v. Tùy vào nhu cầu khách hàng và thị hiếu khác nhau. Trong blockchain, việc thêm một lớp mới (layer 2) không dừng lại ở việc mở rộng quy mô layer 1 mà còn cho phép các giao dịch và quy trình diễn ra độc lập với chuỗi chính (layer 1).

### **Các giải pháp mở rộng layer 1 của Cardano**

Cardano hiện đang phát triển trong kỷ nguyên Basho, là kỷ nguyên về mở rộng quy mô và tối ưu hóa. Trong khi mạng lưới hiện đang quản lý nhu cầu rất hiệu quả, hệ sinh thái ứng dụng phi tập trung (DApp) đang phát triển nhanh chóng và sẽ ngày càng có nhiều nhu cầu hơn đối với hệ thống. Để giải quyết vấn đề này, nhiều phương án về khả năng mở rộng (bao gồm các giải pháp ở layer 1 và layer 2) đang được triển khai trên Cardano cho hàng trăm nghìn người, và hàng triệu người dùng mới.

**Tăng kích thước khối**

Khối càng lớn thì càng có nhiều giao dịch. Khối đầu tiên được đúc trên Cardano có kích thước 665 byte (0,665KB). Ngày nay, khối có kích thước 72KB. Đã tăng hơn 10.000%! Việc tăng thêm kích thước trong tương lai sẽ được áp dụng liên tục dựa trên việc giám sát hệ thống và tình trạng tổng thể mạng lưới.

**Pipelining**

Cải thiện thời gian phát tán khối bằng cách vừa xác thực vừa phát tán. Mục tiêu là để các khối được truyền tải tới ít nhất 95% đối tượng ngang hàng trong vòng năm giây, bằng cách giảm thời gian chờ giữa các khối (chi phí truyền khối). Điều này cung cấp thêm không gian để thực hiện các thay đổi tích cực hơn, chẳng hạn như tăng kích thước khối hoặc tăng giới hạn tham số Plutus.

**Người xác nhận đầu vào (Input Endorsers)**

Sâu xa hơn, Input Endorsers sẽ cải thiện thời gian và thông lượng truyền khối bằng cách cho phép các giao dịch được tách thành các khối đã được xây dựng sẵn. Điều này cải thiện tính nhất quán của thời gian truyền khối và cho phép tần suất giao dịch cao hơn.

**Thông số bộ nhớ / CPU cho Plutus**

Sử dụng bộ nhớ hiệu quả hơn trên toàn bộ chuỗi. Cụ thể, có những cải tiến về bộ nhớ trong việc xử lý Đầu ra giao dịch chưa được gửi (UTXO), phân phối cổ phần, phân phối cổ phần trực tiếp và các pool, hay biểu diễn hàm băm.

**Cải tiến tập lệnh Plutus**

Sử dụng mô hình EUTxO hiệu quả hơn thông qua tối ưu hóa hợp đồng thông minh, bao gồm:

- Đầu vào tham chiếu (CIP-0031) - Các tập lệnh Plutus có thể kiểm tra các đầu vào giao dịch mà không cần sử dụng chúng. Điều này có nghĩa là không cần thiết phải tạo UTXO chỉ để kiểm tra thông tin do đầu vào nắm giữ.
- Plutus Datums (CIP-0032) - Các dữ liệu có thể được gắn trực tiếp vào đầu ra thay vì băm dữ liệu. Điều này đơn giản hóa cách dữ liệu được sử dụng, vì người dùng có thể thấy dữ liệu thực tế hơn là phải cung cấp dữ liệu khớp với hàm băm đã cho.
- Chia sẻ tập lệnh (CIP-0033) - Các tham chiếu tập lệnh Plutus có thể được liên kết với các đầu ra giao dịch, nghĩa là chúng có thể được ghi lại trên chuỗi để sử dụng lại sau này. Việc không cung cấp một bản sao của tập lệnh với mỗi giao dịch làm giảm đáng kể sự bất tiện cho các nhà phát triển. Việc sử dụng lại các tập lệnh trong nhiều giao dịch làm giảm đáng kể kích thước giao dịch, cải thiện thông lượng và giảm chi phí thực thi tập lệnh.

**Cải tiến node**

Các cải tiến đối với node sẽ giúp phân bổ đồng đều các phép tính tiền cược và phần thưởng trên các epoch, do đó cần thêm không gian để tăng kích thước khối. Ngoài ra, việc sử dụng bộ nhớ giờ đây hiệu quả hơn. Nén bộ nhớ nghĩa là làm giảm dấu vết RSS và chia sẻ bộ nhớ nghĩa là chúng ta cần ít dữ liệu được khởi tạo hơn. Phiên bản Node 1.34.1, từ tháng 3 năm 2022, giảm tải cao điểm tại các điểm quan trọng, bao gồm cả ranh giới epoch.

**Lưu trữ trên đĩa**

Bằng cách lưu trữ các phần của trạng thái giao thức trên đĩa, các node sẽ cần ít bộ nhớ hơn, nghĩa là các hệ thống gặp hạn chế về RAM có thể chạy các node miễn là chúng có đủ dung lượng lưu trữ, thì bộ nhớ sẽ không gặp tình trạng tắc nghẽn khi mở rộng. Điều này sẽ cho phép tăng trưởng đáng kể trong trạng thái blockchain .

## **Interlude: Ba vấn đề cốt lõi trên blockchain**

Khả năng mở rộng của một hệ thống phân tán - chẳng hạn như một blockchain - là một vấn đề phức tạp.

Mọi người đồng tình rằng một hệ thống blockchain 'phù hợp' phải có ba thuộc tính: khả năng mở rộng, bảo mật và phân tán. Nhưng có một niềm tin phổ biến không kém trong cái gọi là bộ ba này cho rằng các hệ thống phi tập trung chỉ có thể cung cấp được hai trong số ba thuộc tính, và phải hy sinh cái còn lại. Điều này được công nhận lần đầu tiên bởi người sáng lập Ethereum, Vitalik Buterin, bộ ba này cho thấy rằng các nhà phát triển phải luôn chấp nhận thỏa hiệp, hoặc đánh đổi khi thiết kế mạng blockchain. Sự thỏa hiệp này có nghĩa là một thành phần phải chịu lép vế cho hai thành phần còn lại.

Ví dụ: mạng lưới càng có nhiều node thì mạng lưới càng trở nên phi tập trung hơn, nhưng điều đó cũng có nghĩa là càng cần nhiều node đáng tin cậy để duy trì bảo mật. Để duy trì bảo mật, các khoản phí phải được áp dụng khiến chi phí tiềm ẩn có thể cao đến mức nghiêm trọng. Tuy nhiên, mạng lưới phải khuyến khích sự tham gia, vì vậy chi phí cho mỗi node phải tương đối thấp. Ngoài ra, đặc điểm của tính bất biến ngụ ý rằng dữ liệu blockchain sẽ được thêm vào miễn là blockchain tồn tại, nhưng không bao giờ bị xóa, có nghĩa là blockchain sẽ tiếp tục phát triển. Mạng lưới lớn hơn có nghĩa là cần nhiều tài nguyên tính toán hơn để duy trì hiệu suất. Hiệu suất tốt hơn cần phần cứng tốt hơn, có nghĩa là phần thưởng phải hấp dẫn để khiến việc đầu tư trở nên xứng đáng v...v...

### **Mở rộng theo chiều dọc và chiều ngang**

Giải quyết vấn đề nan giải này đòi hỏi một cách tiếp cận thận trọng và cân bằng, để cả ba yếu tố này luôn ở trạng thái cân bằng.

Về lý thuyết, một hệ thống blockchain sẽ tiếp tục phát triển vô thời hạn. Khi càng có nhiều node trở thành một phần của hệ thống, thì sẽ có nhiều dữ liệu và tài sản lưu chuyển hơn, đồng thời sẽ cần xử lý nhiều giao dịch hơn. Tất cả điều này đòi hỏi sức mạnh tính toán và khả năng lưu trữ. Theo thời gian, nhu cầu sẽ tiếp tục tăng, vì vậy hệ thống cơ bản sẽ cần phải mở rộng quy mô phù hợp để ngăn chặn sự sụt giảm nghiêm trọng về hiệu suất.

Hai hướng mở rộng đang có: dọc và ngang.

**Mở rộng theo chiều dọc**

Kỹ thuật này liên quan đến việc mở rộng khả năng tính toán của các node riêng lẻ bằng cách thêm nhiều bộ nhớ hơn và các thành phần tốt hơn. Nói cách khác, nâng cấp phần cứng của mạng để đạt được hiệu suất tổng thể tốt hơn.

Ví dụ, có một mạng bao gồm các node hiệu suất cao hỗ trợ kích thước khối lớn hơn và khuếch tán khối nhanh hơn. Nhưng nhược điểm là sự phân quyền sẽ bị hạn chế, do chi phí vận hành cao, điều này sẽ khiến các nhà khai thác node mới phải suy nghĩ kỹ về việc tham gia và do đó hạn chế sự mở rộng của mạng. Ngoài ra, một mạng như vậy sẽ mang lại chi phí cao hơn cho các node xác nhận.

**Mở rộng theo chiều ngang**

Ngược lại với mở rộng theo chiều dọc, mở rộng theo chiều ngang có thể đạt được theo hai cách. Một, đơn giản bằng cách thêm nhiều máy tính (node) vào mạng hiện có. Lý do là bằng cách thêm các node bổ sung, mạng sẽ có khả năng xử lý nhiều giao dịch hơn.

Và thứ hai, bằng cách sử dụng sidechains, sẽ có lợi thế khi loại bỏ một số khối lượng tính toán khỏi chuỗi chính, ví dụ cho phép tùy chỉnh dưới dạng các giao thức đồng thuận khác nhau hoặc các mô hình quản trị, để phù hợp với một dự án hoặc ngành cụ thể. Từ quan điểm bảo mật, các sidechains có thể tạo ra một hệ sinh thái an toàn hơn bằng cách cô lập các mối đe dọa tiềm ẩn đối với chuỗi chính. Nếu một sidechain bị xâm nhập theo bất kỳ cách nào, nguy cơ sẽ chỉ trong sidechain đó, do đó bảo vệ phần còn lại của mạng lưới.

## **Layer 2: Giải quyết vấn đề nan giải về khả năng mở rộng**

Nói chung, các giải pháp layer 2 giải quyết vấn đề khả năng mở rộng vốn có đối với chuỗi layer 1. Được xây dựng trên nền tảng của một blockchain hiện có (giống như việc thêm một tầng bánh trong bánh cưới), các giao thức layer 2 thực hiện rất nhiều công việc xử lý thay cho chuỗi chính. Điều này làm tăng thông lượng của chuỗi chính. Điểm cộng là trong khi layer 2 thực hiện công việc khó khăn, thì layer 1 vẫn đảm bảo tính bảo mật của nó.

### **Layer 2: Định nghĩa**

Là một giao thức được bổ sung ngoài chuỗi và hoạt động trên layer 1 của blockchain. Các bên có thể chuyển tiền một cách an toàn từ chuỗi khối sang một giao thức ngoài chuỗi, giải quyết các giao dịch trong giao thức này một cách độc lập với chuỗi cơ sở và chuyển tiền một cách an toàn trở lại chuỗi cơ sở nếu cần. Các giao thức layer 2 cải thiện thông lượng tổng thể và khả năng mở rộng vì chúng làm giảm tắc nghẽn mạng lưới.

### **Các giải pháp về khả năng mở rộng layer 2 của Cardano**

**Sidechains**

Sidechain được định nghĩa là một phương pháp cho phép nhiều blockchain giao tiếp với nhau và có một chuỗi phản hồi với các sự kiện, nó là một chuỗi khối riêng biệt được kết nối với một chuỗi khối chính (chuỗi 'chính', còn được gọi là chuỗi mẹ), thông qua cơ chế hai chiều (gọi là 'cầu nối') cho phép token và các tài sản kỹ thuật số khác từ một chuỗi này được sử dụng trong chuỗi khác và kết quả được trả về chuỗi ban đầu. Tài sản có thể được di chuyển giữa các chuỗi khi cần thiết. Một chuỗi chính duy nhất có thể chứa nhiều sidechains có thể tương tác được kết nối với nó, có thể hoạt động theo những cách hoàn toàn khác nhau. EVM sidechains trên Cardano bao gồm [Milkomeda của dcSpark](https://www.milkomeda.com/) và [dự án EVM sidechain của IOG.](https://iohk.io/en/blog/posts/2022/07/06/introducing-the-cardano-evm-sidechain/)

**Hydra**

Hydra là giải pháp với khả năng mở rộng layer 2 cho Cardano, nhằm mục đích tăng tốc độ giao dịch thông qua độ trễ thấp, thông lượng cao và giảm thiểu chi phí giao dịch.

[Hydra Head](https://hydra.family/head-protocol/) là giao thức đầu tiên của dòng Hydra và là nền tảng cho các kịch bản triển khai nâng cao hơn dựa trên các kênh trạng thái đa bên, đẳng hình. Bằng cách cung cấp các phương tiện xử lý giao dịch ngoài chuỗi hiệu quả hơn cho một nhóm người dùng, đồng thời sử dụng sổ cái của chuỗi chính làm lớp thanh toán an toàn, Hydra Head đảm bảo trạng thái an toàn trong khi liên kết với chuỗi chính. Do không cần toàn bộ sự đồng thuận, nên nó có thể thích nghi với nhiều loại ứng dụng. Ngoài ra, Hydra Head chấp nhận phí Tx, các ngân sách thực thi tập lệnh và các thông số giao thức khác cấu hình ở mức thấp hoặc cao tùy theo trường hợp sử dụng. Điều này rất quan trọng để kích hoạt các giao dịch vi mô.

Hơn thế, Hydra Head còn đưa ra [khái niệm về nhiều kênh trạng thái đẳng hình](https://eprint.iacr.org/2020/299.pdf) : nghĩa là thống nhất và dùng chung cách biểu diễn sổ cái cho các sổ cái trong cùng nhánh, đây là lý do vì sao chúng tôi gọi là Heads (dùng trong tên Hydra). Đặc biệt với Cardano, điều này giúp cho các tài sản gốc, NFT, các tập lệnh Plutus sẽ luôn hiện diện trong mỗi head của Hydra. Đẳng hình cho phép hệ thống mở rộng một cách tự động, thay vì tự tạo bằng cách thủ công.

Hydra Head tỏ ra vượt trội trong việc đạt được kết quả ngay lập tức với mỗi head. Quá trình thiết lập khi tạo và dừng mỗi head có thể mất vài block, nhưng một khi nó hoàn tất thì việc tiến hành giao dịch giữa các bên tham gia diễn ra vô cùng nhanh chóng. Vì các đầu của Hydra cũng là đẳng hình và dùng chung mô hình EUTXO, nên chúng có thể xử lý nhiều giao dịch cùng lúc mà không bị xung đột, chúng kết hợp với nhau và tạo ra một hệ thống ổn định cho phép sử dụng các tài nguyên sẵn có một cách tối ưu.

### **Các giải pháp khác về khả năng mở rộng**

**Tính toán ngoài chuỗi**

Giảm tải các tính toán, ví dụ như trong Thực thi hợp đồng không đồng bộ (ACE), điều này giúp phần lõi của mạng lưới hoạt động hiệu quả hơn. Do các giao dịch xảy ra bên ngoài chuỗi blockchain, nên chúng sẽ nhanh hơn. phí giao dịch rẽ hơn thông qua mô hình tin cậy.

**Mithril**

Để đạt khả năng mở rộng lớn hơn, cần phải giải quyết các phức tạp trọng điểm xung quanh việc phụ thuộc vào Loogarit và số lượng người tham gia. [Mithril](https://iohk.io/en/blog/posts/2021/10/29/mithril-a-stronger-and-lighter-blockchain-for-better-efficiency/) là một giao thức được phát triển bởi IOG, hoạt động theo cơ chế xác định lượng chữ ký dựa vào ủy thác, tạo đòn bẩy cho việc tận dụng các ưu điểm của ví như sự an toàn, minh bạch và khối lượng nhẹ. Mithril sẽ cải thiện việc đồng bộ hóa chuỗi song song với duy trì sự tin cậy. Kết quả tổng hợp chữ ký được đưa ra nhanh chóng và hiệu quả mà không ảnh hưởng tính năng bảo mật.

## **Kết luận**

Trước đây mạng blockchain và những khái niệm của nó về hệ sinh thái, sổ cái phi tập trung sẽ thường mù mờ và khó hiểu.

Tuy nhiên, khi dùng hình ảnh chiếc bánh để hình dung, ta có thể hiểu đơn giản layer 1 và layer 2 là:

- Layer 1 (như phần đế bánh): là mạng cơ sở mạnh mẽ và an toàn, dựa trên đó các giải pháp của layer 2 được xây dựng bên trên.
- Layer 2 (các tầng bánh): là các giải pháp được xây dựng trên mạng cơ sở để giải quyết các vấn đề về khả năng mở rộng vốn có.

Đây là cách đơn giản nhất để hình dung và hiểu về layer 1 và layer 2 là gì.

## **Những điều lưu ý**

- Cardano là layer 1 (mạng cơ sở).
- Giải pháp layer 2 là một cấu trúc được xây dựng phía trên chuỗi layer 1 để giải quyết các vấn đề về khả năng mở rộng và tốc độ giao dịch sau này. Lightning Network của Bitcoin là một ví dụ về giải pháp layer 2, cũng như Hydra của Cardano.
- Có hai hướng mở rộng là theo chiều dọc và theo chiều ngang.
- Mở rộng quy mô theo chiều dọc là việc mở rộng khả năng tính toán của các node riêng lẻ bằng cách thêm nhiều bộ nhớ hơn và các thành phần tốt hơn.
- Mở rộng quy mô theo chiều ngang có thể đạt được theo hai cách. Thứ nhất, đơn giản bằng cách thêm nhiều máy tính (node) vào mạng hiện có. Thứ hai, bằng cách sử dụng sidechains, sẽ loại bỏ một số khối lượng tính toán khỏi chuỗi chính.
- Cardano sẽ cho thấy hàng loạt các phương pháp về khả năng mở rộng được triển khai từ 2022 đến 2023.<br><br>Bài này được dịch bởi Hoang Tran. <a class="_active_edit_href" href="https://iohk.io/en/blog/posts/2022/08/05/layer-1-layer-2-all-you-need-to-know">với bài gốc</a><br><em>Dự án này được tài trợ bởi Catalyst</em>
