# Giới thiệu Ofelimos : giao thức đồng thuận mới PoUW bằng chứng về công việc hữu ích

### **Nghiên cứu của IOG giới thiệu một giao thức đồng thuận mới, an toàn có thể chứng minh được để giảm thiểu sự lãng phí năng lượng của các blockchains PoW - bằng chứng công việc**

![](img/2022-08-16-introducing-ofelimos-a-proof-of-useful-work-consensus-protocol.002.png) 16 August 2022![](img/2022-08-16-introducing-ofelimos-a-proof-of-useful-work-consensus-protocol.002.png)[ Olga Hryniuk](/en/blog/authors/olga-hryniuk/page-1/)![](img/2022-08-16-introducing-ofelimos-a-proof-of-useful-work-consensus-protocol.003.png) 11 mins read

![Olga Hryniuk](img/2022-08-16-introducing-ofelimos-a-proof-of-useful-work-consensus-protocol.004.png)[](/en/blog/authors/olga-hryniuk/page-1/)

### [**Olga Hryniuk**](/en/blog/authors/olga-hryniuk/page-1/)

Technical Writer

Tiếp thị &amp; Truyền thông

- ![](img/2022-08-16-introducing-ofelimos-a-proof-of-useful-work-consensus-protocol.005.png)[](https://www.linkedin.com/in/olga-hryniuk-1094a3160/ "LinkedIn")
- ![](img/2022-08-16-introducing-ofelimos-a-proof-of-useful-work-consensus-protocol.006.png)[](https://github.com/olgahryniuk "GitHub")

![Introducing Ofelimos: a proof-of-useful-work consensus protocol](img/2022-08-16-introducing-ofelimos-a-proof-of-useful-work-consensus-protocol.007.png)

Việc giảm thiểu chi phí năng lượng và lượng khí thải carbon của cơ chế đồng thuận bằng chứng công việc (PoW) là một trong những chủ đề được thảo luận sôi nổi nhất trong lĩnh vực tiền mã hóa. Việc thay thế PoW nguyên thủy trong giao thức chuỗi dài nhất của Nakamoto bằng một bằng chứng về công việc hữu ích (PoUW) từ lâu đã được biết đến như một lý thuyết về một giải pháp lý tưởng ở nhiều khía cạnh, nhưng cho đến nay, khái niệm này vẫn chưa được xác thực một cách thuyết phục.

Hôm nay, tại hội nghị mật mã quốc tế hàng đầu, [Crypto](https://crypto.iacr.org/2022/) , Input Output Global (IOG) giới thiệu *Ofelimos* , một giao thức blockchain mới dựa trên PoUW-based, có cơ chế đồng thuận đồng thời nhận ra một giải pháp giải quyết vấn đề tối ưu hóa tính phi tập trung. Cơ chế đồng thuận sử dụng công việc để giải quyết các vấn đề liên quan đến tính toán thực tiễn để duy trì chuỗi khối.

## **Bằng chứng về công việc (PoW) so với bằng chứng về công việc hữu ích (PoUW)**

Các giao thức blockchain dựa trên PoW tận dụng công việc được thực hiện bởi những người tham gia giao thức, được gọi là *thợ đào*. PoW đảm bảo tính bảo mật của sổ cái bằng việc khuyến khích các thợ đào cạnh tranh trong việc giải quyết các vấn đề tính toán để đủ điều kiện tạo ra một khối mới. Công việc tính toán này duy trì tính bảo mật của giao thức nhưng yêu cầu sử dụng năng lượng và tài nguyên đáng kể. Tại thời điểm của bài viết, Bitcoin có [mức chi tiêu năng lượng hàng năm](https://ccaf.io/cbeci/index) ngang bằng với sức tiêu thụ năng lượng của nhiều quốc gia vừa và nhỏ.

Bằng chứng về công việc *hữu ích* giải quyết vấn đề hiệu quả năng lượng bằng cách tái định vị nỗ lực tính toán cần thiết để duy trì bảo mật giao thức nhằm giải quyết các vấn đề phức tạp *trong thế giới thực,* chẳng hạn như tối ưu hóa việc logistics của công ty hoặc lập lịch sự kiện.

Một trong những thách thức của PoUW là giải quyết tình huống khó xử sau: nếu các vấn đề cần giải quyết thực sự hữu ích (đến từ thế giới thực), kẻ tấn công có thể điều khiển hệ thống đặt ra các trường hợp hoặc vấn đề có thể dễ dàng giải quyết (hoặc đã được kẻ tấn công giải quyết). Điều này sẽ tận dụng tài nguyên của kẻ tấn công để tạo ra nhiều khối hơn so với một người tham gia trung thực với cùng một lượng tài nguyên và do đó sẽ làm giảm tính bảo mật của blockchain. Mặt khác, muốn giảm thiểu khả năng của kẻ tấn công để tận dụng sản xuất khối của họ có thể yêu cầu đặt ra các thuật toán ngẫu nhiên, do đó làm cho các tính toán của hệ thống trở nên vô dụng trong thực tế.

Ofelimos giải quyết tình huống khó xử này cùng với phân tích tính hữu ích và bảo mật chính thức.

## **Tổng quan về Ofelimos**

Các máy trạm công bố các vấn đề cần giải quyết và phần thưởng sẽ được trả cho những thợ đào thành công. Cũng giống như trong PoW, thợ đào giải quyết những vấn đề này để tham gia vào một cuộc chơi xổ số quyết định tính đủ điều kiện để tạo khối.

Trong PoW thuần túy, cuộc chơi xổ số này thường bao gồm việc <br>hash - băm lặp đi lặp lại một thử thách (cùng với một bộ đếm) đổi lấy một giá trị mục tiêu nhất định. Người chơi xổ số sẽ thắng nếu giá trị băm nằm dưới mục tiêu. Lưu ý rằng trong PoW nguyên bản, một tính toán đơn lẻ thì rất nhanh trong khi xác suất để đạt được mục tiêu lại rất nhỏ.

Vì nhiều lý do, trong PoUW, bạn cũng nên giữ cho một tính toán (tương đối) nhanh, điều này giảm thiểu xác suất nhiều khối được tạo ra đồng thời. Mặt khác, trường hợp vấn đề của máy trạm phải đủ lớn để giải quyết việc thuê tính toán bên ngoài là hấp dẫn. Đối với PoUW, điều tự nhiên là hướng đến các lớp tính toán phức tạp như một tổng thể, nhưng có thể chia thành các bước nhỏ "giống nhau". Mỗi bước phải yêu cầu cùng một lượng công việc (theo kỳ vọng) và tương ứng với một tính toán PoW thuần túy.

Tìm kiếm cục bộ ngẫu nhiên (SLS) là một loại tính toán rõ ràng như vậy. Các thuật toán SLS được áp dụng cho các bài toán tối ưu hóa mà không có thuật toán xác định hiệu quả nào được biết đến. Thay vào đó, SLS thực hiện một bước đi ngẫu nhiên trong lĩnh vực giải pháp tối ưu hóa dần dần giải pháp bằng cách sử dụng một số phương pháp heuristics nhất định. Vì mỗi bước tính trong bước đi ngẫu nhiên là một ví dụ khác nhau của cùng một phép tính, SLS là một ứng cử viên sáng giá cho PoUW theo các yêu cầu trên. Hơn nữa, SLS có mức độ liên quan đến thực tế cao với các ứng dụng kinh tế thực trong các lĩnh vực như lập kế hoạch hậu cần, lập lịch sự kiện, v.v.

## **Chuyển đổi từng bước từ PoW sang PoUW**

Thợ đào tiếp nhận và giải quyết các vấn đề của máy trạm được đăng trên blockchain. Bản cập nhật sự cố liên tục được lưu trữ trong blockchain cho đến khi xuất hiện một số tiêu chí chấm dứt, ví dụ: một số mục tiêu cố định được đưa ra tại một bước tính hoặc nếu tìm thấy được một giải pháp thích hợp .

Bây giờ chúng tôi xây dựng lại cách chuyển đổi PoW thuần túy thành PoUW trong cài đặt này.

1. Trong PoW nguyên bản, thợ đào phải mở rộng chuỗi dài nhất của họ bằng một khối mới, băm lặp lại khối mới theo một mục tiêu nhất định (bằng cách thay đổi bộ đếm có trong khối). Bước đầu tiên, chúng tôi thay thế băm lặp lại bằng tính toán lặp lại của bước thăm dò SLS M trên trạng thái tính toán trước đó được lưu trữ trên chuỗi khối, trong đó khối xác định thông số đầu vào ngẫu nhiên cho bước tính toán. Xem Hình 1 (bên phải): Trạng thái tính toán trước đó được mở rộng bước tính toán ngẫu nhiên M bằng cách sử dụng thông số đầu vào kết quả từ việc băm khối cùng với trạng thái s, tạo ra trạng thái tính toán mới (có thể tốt hơn). Quá trình này được lặp lại cho đến khi đáp ứng được điều kiện chưa được chỉ định "?", cho phép người thợ đào xuất bản khối. Khi quá trình này diễn ra, người thợ đào theo dõi trạng thái tốt nhất sbest đã được tìm thấy trong quá trình lặp đi lặp lại này.

![](img/2022-08-16-introducing-ofelimos-a-proof-of-useful-work-consensus-protocol.008.png)

Hình 1: Bắn vào mục tiêu T (PoW, bên trái). Lặp lại bước thăm dò M (PoUW, bên phải).

1. Bây giờ chúng tôi khắc phục điều kiện thành công còn thiếu ˜?". Để đạt được các đặc tính ngẫu nhiên tốt mà không bị sai lệch tính toán cụ thể, việc tìm kiếm một khối được tách biệt khỏi chất lượng của trạng thái được tính toán s', bằng cách thêm vào sau bước tính toán, một "hậu hash" cho bước tính toán (sử dụng lại thông số đầu vào ban đầu) - xem Hình 2 - và khối đủ điều kiện để xuất bản nếu giá trị băm này thấp hơn một số mục tiêu T3. Bên cạnh giải pháp tốt nhất hiện tại là sbest tốt nhất, điều này thể hiện trạng thái ST mới phải được xuất bản cùng với khối, trạng thái dẫn đến băm bên dưới T3 - chứng minh tính đủ điều kiện để xuất bản khối. Lưu ý rằng chỉ sbest phục vụ như một bản cập nhật trạng thái tốt nhất (sẽ được các thợ đào tính toán thêm) trong khi sT chỉ đóng vai trò là nhân chứng đủ điều kiện để xuất bản khối.

![](img/2022-08-16-introducing-ofelimos-a-proof-of-useful-work-consensus-protocol.009.png)

Hình 2: Ngẫu nhiên hóa tính đủ điều kiện để xuất bản khối

1. Xét rằng M khó tính toán hơn H và không phải tất cả các trường hợp của M đều có thể yêu cầu cùng một lượng công việc, đối thủ có thể lặp lại những dữ liệu đầu vào ngẫu nhiên cho phép họ tăng tốc độ tính toán M so với một người thợ đào trung thực, do đó đạt được một lợi thế trong việc tạo ra các khối nhanh hơn và làm giảm tính bảo mật của hệ thống. Chúng tôi giảm thiểu việc lặp lại như vậy bằng cách yêu cầu băm ban đầu thấp hơn T1 mục tiêu. Ví dụ: trước khi thực hiện bước tính toán M, người thợ đào phải tìm giá trị băm thấp bằng cách thay đổi bộ đếm khối dọc theo các dòng của PoW thuần túy. Xem Hình 3. Cụ thể, T1 được chọn sao cho công việc dự kiến để tìm một giá trị băm dưới mục tiêu T1 tốn ít nhất bằng mức độ phức tạp về thời gian trong trường hợp xấu nhất của tính toán M - việc thực hiện lặp lại cho một trường hợp dễ dàng cũng tốn kém như việc tính toán một phiên bản “bất tiện” của M. Bộ ba (Bctr, sbest, sT) thỏa mãn các điều kiện trên do đó tạo thành PoUW.

![](img/2022-08-16-introducing-ofelimos-a-proof-of-useful-work-consensus-protocol.010.png)

Hình 3: Bảo vệ chống lặp lại bằng cách tiền băm đối với mục tiêu T1

1. Trái ngược với PoW nguyên bản, chúng tôi không có khả năng xác minh các node của PoUW bằng cách lặp lại phép tính M của thợ đào, vì điều này sẽ kéo theo một lượng lớn tính toán được sao chép và do đó giảm đáng kể phần tính toán thực sự hữu ích trong hệ thống. Để tránh điều này, khi 'tìm thấy một khối có thể xuất bản, thợ đào được yêu cầu tạo một đối số không tương tác ngắn gọn (SNARG) để chứng minh sự thành công đó - với lợi ích là độ phức tạp xác minh trở nên độc lập với độ phức tạp để tính toán M. Hơn nữa, tính toán chính xác của giải pháp Sbest đã được chứng minh. Xem Hình 4.

![](img/2022-08-16-introducing-ofelimos-a-proof-of-useful-work-consensus-protocol.011.png)

Hình 4: Giảm thiểu xác minh phân tán bằng cách thêm bằng chứng không tương tác

1. Để tận dụng lợi thế của việc khai thác phân tán đồng thời, cá thể SLS được song song hóa (ví dụ: bằng cách duy trì nhiều tính toán) vì, nếu không, tất cả các thợ đào sẽ đồng thời tính toán cùng một trạng thái, (về cơ bản) tạo ra rất nhiều các bước tính toán dư thừa. Lưu ý rằng, vì lý do bảo mật, quá trình sản xuất khối trong PoW "Nakamoto" tiêu chuẩn và các bản cập nhật trạng thái gắn liền với các khối diễn ra rất chậm. Ngược lại, bản cập nhật trạng thái phải tiến hành nhanh chóng để tránh các thợ đào phát hiện ra các trạng thái 'lỗi thời'. Do đó, chúng tôi giới thiệu hai loại khối, "khối xếp hạng - ranking block" khó tìm thấy có cùng chức năng như trong sự đồng thuận của Nakamoto và khối đầu vào - input block " dễ tìm "có chức năng giống như các giao dịch được các khối xếp hạng tham chiếu cuối cùng. Bằng cách này, giải pháp tốt nhất của thợ đào có thể được phổ biến tương đối nhanh, do đó giữ cho tất cả các thợ đào luôn cập nhật. Đặc biệt, điều này đạt được bằng cách đánh giá lần đầu băm cuối cùng với  mục tiêu "dễ dàng" T3. Nếu nó nằm dưới mục tiêu, nó đủ điều kiện để có thể xuất bản một khối, nhưng chỉ khi mục tiêu nằm dưới mục tiêu " khó hơn" T2, thì khối đó mới đủ điều kiện là một khối xếp hạng  - ranking block "có liên quan đến tính đồng thuận" - nếu không thì nó là được định nghĩa như một khối đầu vào - input block. Xem Hình 5.

![](img/2022-08-16-introducing-ofelimos-a-proof-of-useful-work-consensus-protocol.012.png)

Hình 5: Một hậu băm - post hash bên dưới T2 đủ điều kiện cho khối đó là khối xếp hạng - ranking block. Sau băm giữa mục tiêu T2 và T3 đủ điều kiện khối này là khối đầu vào -  input block.

## **Thuộc tính của giao thức**

Việc đưa ra một phân tích kỹ lưỡng về tính bảo mật và tính hữu dụng của giao thức nằm ngoài phạm vi của bài viết này. Vẫn có thể hữu ích khi nhắc lại một số khả năng giả định tại sao giao thức lại an toàn và sau đó kết luận bằng cách kiểm tra hiệu quả của giao thức.

**Bảo mật chuỗi khối:**

- **Lặp lại** : đối thủ không có lợi thế bằng cách  lặp lại các trường hợp dễ tính toán của M. Điều này đạt được bằng cách điều chỉnh ngưỡng tiền băm T1 sao cho việc tính toán M trên bất kỳ trường hợp nào cũng khó bằng việc tìm một tiền băm mới bên dưới T1 (trong kỳ vọng).
- **Khả năng chống lại lợi thế của đối thủ: Lợi thế** của đối thủ trong việc tính toán PoUW nhanh hơn so với các bên trung thực bị hạn chế. Điều này đạt được bằng cách tách khối thành công khỏi tính toán thực tế và bằng cách tiền băm dưới mục tiêu T1. Đặc biệt, theo mô hình tiêu chuẩn trong [GKL14, PSS16] và giả định rằng đối thủ không có lợi thế trong việc tính toán M nhanh hơn so với các bên trung thực, giao thức cho phép đối thủ kiểm soát bất kỳ sức mạnh tính toán thiểu số nào dành riêng cho mạng - giống như Bitcoin. Ngược lại, ngay cả khi đối thủ có thể tính toán M miễn phí trong mọi trường hợp, giao thức vẫn cho phép đối thủ kiểm soát tới một phần ba tổng số tài nguyên tính toán - như chúng vẫn hoạt động với chi phí bằng một nửa do quá trình tiền băm so với mục tiêu T1.
- Độ khó thay đổi: Trong các giao thức đồng thuận PoW/PoUW, độ khó để tìm một khối phải được điều chỉnh liên tục cho phù hợp với mức độ về sức mạnh tính toán hiện tại dành riêng cho hệ thống. Trong Ofelimos, điều này dễ dàng đạt được bằng cách điều chỉnh mục tiêu T2 cho (đơn) hậu băm được thực hiện sau bước tính toán - đủ điều kiện để tạo khối xếp hạng - ranking block.

Hiệu quả:

- Cập nhật thường xuyên: Sự tách biệt giữa khối xếp hạng và khối đầu vào đảm bảo rằng các cập nhật trạng thái được phổ biến nhanh chóng.
- Tính hữu ích: Theo tính hữu ích, chúng tôi xác định tỷ lệ của công việc tính toán tổng thể dành cho vấn đề SLS (đây là một sự đơn giản hóa - một định nghĩa và phân tích cẩn thận hơn, có thể được tìm thấy trong bài báo này). Các nguồn chính của hoạt động "không hữu dụng" trong hệ thống là quá trình tiền băm lặp đi lặp lại đối với T1 và tính toán của SNARG. Lưu ý rằng:
    - quá trình hậu băm chỉ được thực hiện một lần cho mỗi lần gọi M và so độ phức tạp của M, có thể bị bỏ qua vì những lý do thực tế.
    - SNARG chỉ phải được tính toán đối với hai trong số nhiều lệnh gọi M, lệnh này đưa ra kết quả St (ngụ ý khối thành công) và sbest (giải pháp tốt nhất). Do đó, chi phí của việc tính toán SNARGs có thể được giảm thiểu bằng cách hạ thấp ngưỡng T3 quyết định sự thành công của khối để đánh đổi với các cập nhật trạng thái chậm hơn.

Độ hữu dụng phụ thuộc vào các đặc tính của M. Nếu thời gian chạy của M được tập trung đủ, độ khó tiền băm có thể được đặt gần với độ phức tạp trường hợp trung bình của M. Xem xét các quan sát trên, độ hữu dụng đạt được khoảng ½ nghĩa là người khai thác dành khoảng một nửa thời gian của họ để tính toán M. Nhiều vấn đề SLS cổ điển dường như nằm trong những trường hợp này. Tuy nhiên, nếu M không được "đối xử tốt", thì mức độ hữu dụng có thể gần bằng không. Do đó, việc lựa chọn các thuật toán SLS cụ thể và các bước tính toán, thăm dò M của chúng là rất quan trọng để PoUW đạt được mức độ hữu ích hợp lý.

## **Kết luận**

Ofelimos chỉ là bước đầu tiên hướng tới PoUW an toàn và hữu ích. Khi việc nghiên cứu hiện tại dễ dàng cung cấp khả năng bảo mật có thể chứng minh được đối với các mức độ tham nhũng cao, thì vẫn cần nghiên cứu thêm về mặt thuật toán nhằm cung cấp các lớp vấn đề tối ưu hóa phù hợp để có thể chứng minh một cách rõ ràng về tính hữu ích cao.

Ofelimos: Tối ưu hóa tổ hợp thông qua bài báo nghiên cứu Bằng chứng về công việc hữu ích được xuất bản lần đầu tiên vào tháng 10 năm 2021.

*Tôi muốn cảm ơn [Matthias Fitzi](https://iohk.io/en/team/matthias-fitzi) vì những ý kiến đóng góp và hỗ trợ của anh ấy trong việc chuẩn bị bài đăng trên blog này.<br><br>Bài này được dịch bởi minh-hieu-102 [với bài gốc](https://iohk.io/en/blog/posts/2022/08/16/introducing-ofelimos-a-proof-of-useful-work-consensus-protocol/)<br>*Dự án này được tài trợ bới Catalyst**
