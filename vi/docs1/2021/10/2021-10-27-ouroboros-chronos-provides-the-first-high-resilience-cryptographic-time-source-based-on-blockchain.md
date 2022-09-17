# Ouroboros Chronos cung cấp nguồn thời gian mã hoá có khả năng phục hồi cao đầu tiên dựa trên công nghệ Blockchain

### **Được thiết kế để cung cấp thời gian hiện hành toàn cầu chính xác hơn, Chronos đảm bảo tăng cường bảo mật và khả năng phục hồi mạng lưới đối với sự truyền tải chậm trễ**

![](img/2021-10-27-ouroboros-chronos-provides-the-first-high-resilience-cryptographic-time-source-based-on-blockchain.002.png) 27 tháng 10 năm 2021 ![](img/2021-10-27-ouroboros-chronos-provides-the-first-high-resilience-cryptographic-time-source-based-on-blockchain.002.png) [Olga Hryniuk](tmp//en/blog/authors/olga-hryniuk/page-1/) ![](img/2021-10-27-ouroboros-chronos-provides-the-first-high-resilience-cryptographic-time-source-based-on-blockchain.003.png) 5 phút đọc

![Olga Hryniuk](img/2021-10-27-ouroboros-chronos-provides-the-first-high-resilience-cryptographic-time-source-based-on-blockchain.004.png)[](tmp//en/blog/authors/olga-hryniuk/page-1/)

### [**Olga Hryniuk**](tmp//en/blog/authors/olga-hryniuk/page-1/)

Technical Writer

Marketing &amp; Communications

- ![](img/2021-10-27-ouroboros-chronos-provides-the-first-high-resilience-cryptographic-time-source-based-on-blockchain.005.png)[](https://www.linkedin.com/in/olga-hryniuk-1094a3160/ "LinkedIn")
- ![](img/2021-10-27-ouroboros-chronos-provides-the-first-high-resilience-cryptographic-time-source-based-on-blockchain.006.png)[](https://github.com/olgahryniuk "GitHub")

![Ouroboros Chronos cung cấp nguồn thời gian mã hoá có khả năng phục hồi cao đầu tiên dựa trên công nghệ Blockchain](img/2021-10-27-ouroboros-chronos-provides-the-first-high-resilience-cryptographic-time-source-based-on-blockchain.007.jpeg)

Đồng bộ hóa thời gian toàn cầu trên bất kỳ mạng lưới phân tán nào là điều cần thiết để đảm bảo khả năng phục hồi.

Từ việc đảm bảo thông tin cập nhật giữa những người tham gia đến việc duy trì quá trình xử lý giao dịch chính xác và tạo Block, đồng bộ hóa thời gian là đặc biệt quan trọng trong điều kiện triển khai Hợp đồng thông minh.

Cộng tác với các nhà khoa học từ trường Đại học Edinburgh, Purdue và Connecticut, Input Output đã tìm ra cách đồng bộ hóa đồng hồ trên toàn cầu trên một Blockchain để cung cấp nguồn thời gian toàn cầu an toàn hơn và chống giả mạo. Điều này bao gồm việc đồng bộ hóa thời gian từ các thiết bị Internet vạn vật (IoT), ví dụ như các công cụ đo lường trong chuỗi cung ứng và các hệ thống phân tán chung, đặc biệt khi sự cải tiến của đồng hồ trung tâm gây ra rủi ro bảo mật. Nghiên cứu được thực hiện là Ouroboros Chronos, từ tiếng Hy Lạp chỉ thời gian, là sự cải tiến mới nhất của Ouroboros - thuật toán đồng thuận làm nền tảng cho Cardano Blockchain.

## **Vấn đề thời gian**

Time is an indispensable concept within computer programs and applications. Without this concept, we would not be able to access any transport layer security (TLS) based websites, exchange data, or utilize various cryptographic algorithms.

Tuy nhiên, theo dõi thời gian là một vấn đề khó giải quyết. Đồng bộ hóa thời gian một cách chính xác sẽ dự đoán được việc truyền dữ liệu trên toàn bộ Internet. Điều này cũng mất thời gian. Cũng khó có thể dự đoán được sẽ cần bao nhiêu thời gian để truyền dữ liệu - trạng thái mạng lưới liên tục thay đổi và phụ thuộc vào các yếu tố như tắc nghẽn, kích thước thực của dữ liệu và các yếu tố khác. Do đó, các xung đột thường xảy ra. Điều quan trọng là phải có công cụ và giải pháp để cung cấp thời gian thực một cách chính xác.

## **Thời gian thực**

With common computers, we take timekeeping for granted. However, there is a rigorous mechanism that works behind the scenes. The [Network Time Protocol](http://ntp.org/) (NTP), for instance, addresses the timekeeping issue using a hierarchy of servers distributed globally. This includes up to 15 Stratums the routing paths of which are developed to synchronize in the most optimized manner. This is also enabled by the construction of a [Bellman-Ford](https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm) shortest-path spanning tree that decreases both latency and transmission time inconsistencies.

[Thời gian và vị trí dựa trên vệ tinh của Chính phủ Vương quốc Anh: Đánh giá của Blackett](https://www.gov.uk/government/publications/satellite-derived-time-and-position-blackett-review) gần đây đã nhấn mạnh nhu cầu về dữ liệu thời gian linh hoạt hơn và sự phụ thuộc nguy hiểm của các lĩnh vực quan trọng từ mạng lưới thông minh đến các phương tiện tự hành trên Hệ thống vệ tinh định vị toàn cầu (GNSS) vốn dễ bị gây nhiễu, tấn công mạng và thời tiết vũ trụ. Ngoài ra, [Trung tâm Định giờ Quốc gia](https://www.gov.uk/government/news/worlds-first-timing-centre-to-protect-uk-from-risk-of-satellite-failure) đầu tiên trên thế giới, do Phòng thí nghiệm Vật lý Quốc gia đứng đầu, gần đây đã được thành lập để nghiên cứu các dịch vụ định giờ thay thế và linh hoạt hơn cho mọi thứ từ viễn thông đến vận tải thông minh. Các trung tâm đo lường quốc tế hiện phải [so sánh các đồng hồ](https://www.npl.co.uk/time-frequency/comparison-dissemination) hoạt động ở các tần số khác nhau và ở nhiều vị trí để có độ chính xác.

## **Đồng bộ hóa thời gian Blockchain**

The concept of timekeeping is different for distributed ledger technology. Without an accurate and valid timestamp, the network cannot verify if the transaction that is being processed is valid and does not revert the previous one. There are different timestamping techniques used across a range of blockchain ledgers, however, they arenâ€™t necessarily very accurate. For example, Bitcoin uses timestamps for consensus security reasons, but not primarily for timekeeping; and in Ethereum, on-chain timestamps are determined by miners whereas the consensus wonâ€™t technically block or verify those for validity.

Timekeeping is essential for smart contract execution as well. Inaccuracy poses a risk for decentralized finance (DeFi) smart contract attacks. Smart contract vulnerabilities arenâ€™t always conditioned by poor code, time inconsistencies should be resolved to block any possible attacks within the ledger.

## **Ouroboros Chronos: designed to boost communication and timing resilience**

The new research on Ouroboros Chronos enables blockchain technology to synchronize clocks more securely. Chronos is itself a cryptographically secure blockchain protocol that additionally provides an accurate source of time via a novel time synchronization mechanism, eliminating the vulnerabilities of externally hosted clocks. This also enables blockchain to accurately time-stamp transactions making the ledger more resistant to attacks that target time information.

The new protocol can dramatically boost the resilience of critical telecommunications, transport, trading systems, and infrastructures by synchronizing local time to a unified network clock that has no single point of failure.

Giáo sư Aggelos Kiayias, Giám đốc Phòng thí nghiệm Công nghệ Blockchain tại Đại học Edinburgh, Trưởng nhóm khoa học tại Input Output, người dẫn đầu việc nghiên cứu cho biết:

The problem of synchronizing clocks without a central time-keeper is essential in creating a truly robust decentralized financial system. For the first time, we have developed a blockchain mechanism that enables a dynamically evolving group of parties to calibrate their local clocks so they are consistent â€“ even if they come and go following arbitrary participation patterns. By creating a blockchain-based global clock, we have also paved the way to a more secure, tamper-resistant time source with many possible external applications.

Bằng cách cho phép tính thời gian chính xác và có thể truy xuất nguồn gốc đầy đủ của tất cả các giao dịch, bước đột phá khoa học cũng đánh dấu một bước quan trọng trong việc tạo ra các hệ thống tài chính hoàn toàn có thể kiểm toán và chống gian lận.

Để tìm hiểu thêm, hãy xem nghiên cứu đã xuất bản [tại đây](https://eprint.iacr.org/2019/838.pdf).

*Cảm ơn Rachel Bruce, Jenny Corlett, Rod Alexander và Christian Badertscher đã đóng góp ý kiến và hỗ trợ khi viết bài này.<br><br>Bài này được dịch bởi Nguyễn Văn Tú <a class="_active_edit_href" href="https://iohk.io/en/blog/posts/2021/10/27/ouroboros-chronos-provides-the-first-high-resilience-cryptographic-time-source-based-on-blockchain/">với bài gốc</a>.<br>*Dự án này được tài trợ bởi Catalyst**
