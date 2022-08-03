# Ouroboros Chronos provides the first high-resilience, cryptographic time source based on blockchain technology
### **Designed to provide more accurate global timekeeping, Chronos ensures increased security and network resilience to communication delays**
![](img/2021-10-27-ouroboros-chronos-provides-the-first-high-resilience-cryptographic-time-source-based-on-blockchain.002.png) 27 October 2021![](img/2021-10-27-ouroboros-chronos-provides-the-first-high-resilience-cryptographic-time-source-based-on-blockchain.002.png)[ Olga Hryniuk](tmp//en/blog/authors/olga-hryniuk/page-1/)![](img/2021-10-27-ouroboros-chronos-provides-the-first-high-resilience-cryptographic-time-source-based-on-blockchain.003.png) 5 mins read

![Olga Hryniuk](img/2021-10-27-ouroboros-chronos-provides-the-first-high-resilience-cryptographic-time-source-based-on-blockchain.004.png)[](tmp//en/blog/authors/olga-hryniuk/page-1/)
### [**Olga Hryniuk**](tmp//en/blog/authors/olga-hryniuk/page-1/)
Technical Writer

Marketing & Communications

- ![](img/2021-10-27-ouroboros-chronos-provides-the-first-high-resilience-cryptographic-time-source-based-on-blockchain.005.png)[](https://www.linkedin.com/in/olga-hryniuk-1094a3160/ "LinkedIn")
- ![](img/2021-10-27-ouroboros-chronos-provides-the-first-high-resilience-cryptographic-time-source-based-on-blockchain.006.png)[](https://github.com/olgahryniuk "GitHub")

![Ouroboros Chronos provides the first high-resilience, cryptographic time source based on blockchain technology](img/2021-10-27-ouroboros-chronos-provides-the-first-high-resilience-cryptographic-time-source-based-on-blockchain.007.jpeg)

Global time synchronization across any distributed network is essential to ensure its resilience.

Đồng bộ hóa thời gian toàn cầu trên bất kỳ mạng phân tán nào là điều cần thiết để đảm bảo khả năng phục hồi của nó.

From ensuring up-to-date information between all participants, maintaining accurate transaction processing and block creation, time synchronization is especially important in terms of smart contract deployment. 

Từ việc đảm bảo thông tin cập nhật giữa tất cả những người tham gia, việc duy trì xử lý giao dịch chính xác và tạo khối, đồng bộ hóa thời gian đặc biệt quan trọng về việc triển khai hợp đồng thông minh.

In collaboration with scientists from the Universities of Edinburgh, Purdue, and Connecticut, Input Output found a way to globally synchronize clocks across a blockchain to provide a more secure and tamper-proof global time source. This includes synchronization of time from internet of things (IoT) devices, like measurement tools in supply chains, and general distributed systems, particularly where the disruption of a central clock represents a security risk. The research is realized by Ouroboros Chronos, the Greek word for time, which is the latest iteration of Ouroboros â€“ the consensus algorithm that underpins the Cardano blockchain.

Phối hợp với các nhà khoa học từ các trường đại học Edinburgh, Purdue và Connecticut, đầu vào đã tìm ra cách để đồng bộ hóa đồng hồ toàn cầu trên một blockchain để cung cấp nguồn thời gian toàn cầu an toàn và giả mạo hơn.
Điều này bao gồm đồng bộ hóa thời gian từ các thiết bị Internet of Things (IoT), như các công cụ đo lường trong chuỗi cung ứng và các hệ thống phân tán chung, đặc biệt là khi sự gián đoạn của đồng hồ trung tâm thể hiện rủi ro bảo mật.
Nghiên cứu được thực hiện bởi Ouroboros Chronos, từ Hy Lạp cho thời gian, đây là lần lặp mới nhất của Ouroboros - Thuật toán đồng thuận làm nền tảng cho blockchain cardano.

## **Time matters**

## ** Vấn đề thời gian **

Time is an indispensable concept within computer programs and applications. Without this concept, we would not be able to access any transport layer security (TLS) based websites, exchange data, or utilize various cryptographic algorithms. 

Thời gian là một khái niệm không thể thiếu trong các chương trình và ứng dụng máy tính.
Nếu không có khái niệm này, chúng tôi sẽ không thể truy cập bất kỳ trang web dựa trên bảo mật lớp vận chuyển (TLS) nào, trao đổi dữ liệu hoặc sử dụng các thuật toán mật mã khác nhau.

Yet, time tracking is a difficult problem to solve. Accurate time synchronization presumes data transmission across the whole internet, and this, in turn, takes time too. It is also hard to predict how much time would be required for certain data transmission â€“ the network state constantly changes and relies on such factors as congestion and the actual size of data among others. Thus, inconsistencies often occur and it is important to provide the tools and solutions for accurate timekeeping.

Tuy nhiên, theo dõi thời gian là một vấn đề khó giải quyết.
Đồng bộ hóa thời gian chính xác giả định truyền dữ liệu trên toàn bộ internet và đến lượt nó, điều này cũng cần có thời gian.
Cũng rất khó để dự đoán bao nhiêu thời gian sẽ được yêu cầu đối với một số truyền dữ liệu nhất định - trạng thái mạng liên tục thay đổi và dựa vào các yếu tố như tắc nghẽn và kích thước thực tế của dữ liệu trong số những người khác.
Do đó, sự không nhất quán thường xảy ra và điều quan trọng là cung cấp các công cụ và giải pháp để chấm công chính xác.

## **Real time**

## **Thời gian thực**

With common computers, we take timekeeping for granted. However, there is a rigorous mechanism that works behind the scenes. The [Network Time Protocol](http://ntp.org/) (NTP), for instance, addresses the timekeeping issue using a hierarchy of servers distributed globally. This includes up to 15 Stratums the routing paths of which are developed to synchronize in the most optimized manner. This is also enabled by the construction of a [Bellman-Ford](https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm) shortest-path spanning tree that decreases both latency and transmission time inconsistencies.

Với các máy tính phổ biến, chúng tôi coi thời gian là điều hiển nhiên.
Tuy nhiên, có một cơ chế nghiêm ngặt hoạt động đằng sau hậu trường.
[Giao thức thời gian mạng] (ví dụ, http://ntp.org/) (NTP), giải quyết vấn đề thời gian bằng cách sử dụng hệ thống phân cấp các máy chủ được phân phối trên toàn cầu.
Điều này bao gồm tối đa 15 tầng các đường dẫn định tuyến được phát triển để đồng bộ hóa theo cách tối ưu nhất.
Điều này cũng được kích hoạt bằng cách xây dựng [Bellman-Ford] (https://en.wikipedia.org/wiki/bellman%E2%80

The UK Governmentâ€™s [Satellite-derived time and position: Blackett review](https://www.gov.uk/government/publications/satellite-derived-time-and-position-blackett-review) recently highlighted the need for more resilient timing data and the dangerous dependence of critical sectors from smart grids to autonomous vehicles on Global Navigation Satellite Systems (GNSS) that are vulnerable to jamming, cyber attacks, and space weather. Additionally, the worldâ€™s first [National Timing Centre](https://www.gov.uk/government/news/worlds-first-timing-centre-to-protect-uk-from-risk-of-satellite-failure), led by the National Physical Laboratory, was recently created to investigate alternative and more resilient timing services for everything from telecommunications to smart transport. International metrology centers currently have to [compare clocks](https://www.npl.co.uk/time-frequency/comparison-dissemination) operating at different frequencies and in multiple locations for accuracy.

Chính phủ Vương quốc Anh [Thời gian và vị trí có nguồn gốc từ vệ tinh: Đánh giá Blackett] (https://www.gov.uk/government/publication
Đối với dữ liệu thời gian kiên cường hơn và sự phụ thuộc nguy hiểm của các lĩnh vực quan trọng từ lưới thông minh đến các phương tiện tự trị trên các hệ thống vệ tinh điều hướng toàn cầu (GNSS) dễ bị kẹt, tấn công mạng và thời tiết không gian.
Ngoài ra, [Trung tâm thời gian quốc gia] đầu tiên của thế giới (https://www.gov.uk/government/news/worlds-first-timing-centre-to-protect-uk-grom-risk-of-f
Thất bại), dẫn đầu bởi Phòng thí nghiệm vật lý quốc gia, gần đây đã được tạo ra để điều tra các dịch vụ thời gian thay thế và kiên cường hơn cho mọi thứ, từ viễn thông đến vận tải thông minh.
Các trung tâm đo lường quốc tế hiện đang phải [so sánh đồng hồ] (https://www.npl.co.uk/time-frequency/comparison-dissemination) hoạt động ở các tần số khác nhau và ở nhiều vị trí chính xác.

## **Blockchain time synchronization**

## ** Đồng bộ hóa thời gian blockchain **

The concept of timekeeping is different for distributed ledger technology. Without an accurate and valid timestamp, the network cannot verify if the transaction that is being processed is valid and does not revert the previous one. There are different timestamping techniques used across a range of blockchain ledgers, however, they arenâ€™t necessarily very accurate. For example, Bitcoin uses timestamps for consensus security reasons, but not primarily for timekeeping; and in Ethereum, on-chain timestamps are determined by miners whereas the consensus wonâ€™t technically block or verify those for validity.

Khái niệm về thời gian là khác nhau đối với công nghệ sổ cái phân tán.
Nếu không có dấu thời gian chính xác và hợp lệ, mạng không thể xác minh xem giao dịch đang được xử lý có hợp lệ hay không và không hoàn nguyên giao dịch trước.
Có nhiều kỹ thuật hẹn giờ khác nhau được sử dụng trên một loạt các sổ cái blockchain, tuy nhiên, chúng không nhất thiết phải rất chính xác.
Ví dụ, Bitcoin sử dụng dấu thời gian cho các lý do bảo mật đồng thuận, nhưng không chủ yếu để chấm công;
Và trong Ethereum, dấu thời gian trên chuỗi được xác định bởi các công ty khai thác trong khi sự đồng thuận sẽ không chặn kỹ thuật hoặc xác minh những điều đó về tính hợp lệ.

Timekeeping is essential for smart contract execution as well. Inaccuracy poses a risk for decentralized finance (DeFi) smart contract attacks. Smart contract vulnerabilities arenâ€™t always conditioned by poor code, time inconsistencies should be resolved to block any possible attacks within the ledger.

Đồng hồ bấm giờ là điều cần thiết để thực hiện hợp đồng thông minh là tốt.
Không chính xác gây ra rủi ro cho các cuộc tấn công hợp đồng thông minh tài chính phi tập trung (DECI).
Các lỗ hổng hợp đồng thông minh luôn luôn được điều hòa bởi mã kém, sự không nhất quán về thời gian nên được giải quyết để chặn mọi cuộc tấn công có thể có trong sổ cái.

## **Ouroboros Chronos: designed to boost communication and timing resilience**

## ** Ouroboros Chronos: Được thiết kế để tăng cường khả năng phục hồi giao tiếp và thời gian **

The new research on Ouroboros Chronos enables blockchain technology to synchronize clocks more securely. Chronos is itself a cryptographically secure blockchain protocol that additionally provides an accurate source of time via a novel time synchronization mechanism, eliminating the vulnerabilities of externally hosted clocks. This also enables blockchain to accurately time-stamp transactions making the ledger more resistant to attacks that target time information.

Nghiên cứu mới về Ouroboros Chronos cho phép công nghệ blockchain đồng bộ hóa đồng hồ an toàn hơn.
Chronos tự nó là một giao thức blockchain bảo mật bằng mã hóa, cũng cung cấp một nguồn thời gian chính xác thông qua cơ chế đồng bộ hóa thời gian mới, loại bỏ các lỗ hổng của đồng hồ được lưu trữ bên ngoài.
Điều này cũng cho phép blockchain giao dịch dấu thời gian chính xác làm cho sổ cái chống lại các cuộc tấn công nhắm mục tiêu thông tin thời gian.

The new protocol can dramatically boost the resilience of critical telecommunications, transport, trading systems, and infrastructures by synchronizing local time to a unified network clock that has no single point of failure.

Giao thức mới có thể thúc đẩy đáng kể khả năng phục hồi của viễn thông quan trọng, vận chuyển, hệ thống giao dịch và cơ sở hạ tầng bằng cách đồng bộ hóa thời gian địa phương với đồng hồ mạng thống nhất không có điểm thất bại duy nhất.

Professor Aggelos Kiayias, director of the Blockchain Technology Laboratory at the University of Edinburgh and Chief Scientist at Input Output, who led the research, says: 

Giáo sư Aggelos Kiayias, Giám đốc Phòng thí nghiệm Công nghệ Blockchain tại Đại học Edinburgh và nhà khoa học trưởng tại Input Pr sản xuất, người đã lãnh đạo nghiên cứu, nói:

The problem of synchronizing clocks without a central time-keeper is essential in creating a truly robust decentralized financial system. For the first time, we have developed a blockchain mechanism that enables a dynamically evolving group of parties to calibrate their local clocks so they are consistent â€“ even if they come and go following arbitrary participation patterns. By creating a blockchain-based global clock, we have also paved the way to a more secure, tamper-resistant time source with many possible external applications.

Vấn đề đồng bộ hóa đồng hồ không có người giữ thời gian trung tâm là điều cần thiết trong việc tạo ra một hệ thống tài chính phi tập trung thực sự mạnh mẽ.
Lần đầu tiên, chúng tôi đã phát triển một cơ chế blockchain cho phép một nhóm các bên phát triển động để hiệu chỉnh đồng hồ cục bộ của họ để họ nhất quán - ngay cả khi họ đến và đi theo các mô hình tham gia tùy ý.
Bằng cách tạo ra một đồng hồ toàn cầu dựa trên blockchain, chúng tôi cũng đã mở đường đến một nguồn thời gian an toàn hơn, chống giả mạo hơn với nhiều ứng dụng bên ngoài có thể.

By enabling accurate timing and thus full traceability of all transactions, the scientific breakthrough also marks a major step towards creating fully auditable and fraud-proof financial systems.

Bằng cách cho phép thời gian chính xác và do đó khả năng truy xuất nguồn gốc đầy đủ của tất cả các giao dịch, bước đột phá khoa học cũng đánh dấu một bước quan trọng để tạo ra các hệ thống tài chính chống gian lận và có thể kiểm toán đầy đủ.

To find out more, see the published research [here](https://eprint.iacr.org/2019/838.pdf).

Để tìm hiểu thêm, xem nghiên cứu được công bố [tại đây] (https://eprint.iacr.org/2019/838.pdf).

*Thanks to Rachel Bruce, Jenny Corlett, Rod Alexander, and Christian Badertscher for their input and support in writing this post.*

*Cảm ơn Rachel Bruce, Jenny Corlett, Rod Alexander và Christian Badertscher vì đầu vào và hỗ trợ của họ bằng văn bản bài viết này.*

