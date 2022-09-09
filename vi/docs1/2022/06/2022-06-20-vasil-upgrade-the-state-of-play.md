# Cập nhật về nâng cấp Vasil

### **Rất gần nhưng vẫn còn nhiều việc phải làm- Đây là thông tin cập nhật về tiến trình nâng cấp Vasil**

![](img/2022-06-20-vasil-upgrade-the-state-of-play.002.png)20 tháng 6 năm 2022![](img/2022-06-20-vasil-upgrade-the-state-of-play.002.png) [Nigel Hemsley](/en/blog/authors/nigel-hemsley/page-1/)![](img/2022-06-20-vasil-upgrade-the-state-of-play.003.png) 4 phút đọc

![Nigel Hemsley](img/2022-06-20-vasil-upgrade-the-state-of-play.004.png)[](/en/blog/authors/nigel-hemsley/page-1/)

### [**Nigel Hemsley**](/en/blog/authors/nigel-hemsley/page-1/)

Head of Delivery and Projects

Operations

- ![](img/2022-06-20-vasil-upgrade-the-state-of-play.005.png)[](mailto:nigel.hemsley@iohk.io "Email")
- ![](img/2022-06-20-vasil-upgrade-the-state-of-play.006.png)[](tmp/www.linkedin.com/in/nigel-hemsley-433a213 "LinkedIn")

![Cập nhật về nâng cấp Vasil](https://github.com/cardano2vn/iohk-blog/blob/main/vi/docs1/2022/06/img/2022-06-20-vasil-upgrade-the-state-of-play.007.png?raw=true)

On Friday, the core Input Output Global (IOG) team working toward the Vasil upgrade held its regular end-of-week evaluation call. Today (Monday, June 20) was the latest date that we could facilitate a Cardano testnet upgrade before the next epoch boundary, so we agreed to re-evaluate the latest status this afternoon, taking into account the work our engineers did over the weekend.

Nhóm kỹ sư của IOG đang gần hoàn thiện công việc cốt lõi, chỉ còn bảy lỗi vẫn còn tồn tại để hoàn thành công việc hard fork, không có lỗi nào hiện được xếp hạng là 'nghiêm trọng'. Sau một số cân nhắc, chúng tôi đã đồng ý KHÔNG gửi đề xuất cập nhật hard fork testnet ngay hôm nay để có thêm thời gian thử nghiệm.

Cho đến nay, chúng tôi đã quản lý để vượt qua phần lớn (khoảng 95%) các [tập lệnh thử nghiệm Plutus V2](https://github.com/input-output-hk/cardano-node-tests/issues/1079) của chúng tôi. Tuy nhiên, chúng tôi vẫn còn một vài mục còn tồn đọng mà chúng tôi cần chạy để xác nhận mọi thứ đang hoạt động như mong đợi. Chúng tôi đã xác định rằng chúng tôi sẽ cần một vài ngày nữa cho việc này. Điều này khiến chúng tôi chậm tiến độ so với mục tiêu đã thông báo trước đó của chúng tôi là ngày 29 tháng 6 để tiến hành hard fork trên mainnet.

Since the start of June, we have been successfully running an early build of the new node (which includes diffusion pipelining and the new Plutus v2 CIPs among other enhancements) as a semi-public Vasil developer testnet (Devnet). We now have some 35 developers from across 27 projects testing their DApps and helping identify any issues, along with 16 stake pool operators (SPOs) supporting. We’re also working closely with some of the leading tool/API providers, including [Blockfrost](https://blockfrost.io/), Cardano Serialization library (EMURGO), and Cardano Multiplatform Library (dcSpark). We want to call out the work of Mlabs and Dquadrant in particular for providing great support throughout the process. This developer testnet stage puts us in a good position when it comes to Plutus code compatibility and functionality. This valuable work will continue on this development testnet over the next few weeks.

Nâng cấp Vasil là chương trình phát triển và tích hợp phức tạp nhất cho đến nay, từ nhiều góc độ. Đó là một quá trình đầy thử thách, không chỉ đòi hỏi công việc quan trọng của các nhóm cốt lõi mà còn cả sự phối hợp chặt chẽ trong toàn bộ hệ sinh thái.

Quyết định cuối cùng về hard fork Cardano Testnet sẽ được đưa ra - với sự tham vấn của các thành viên của cộng đồng phát triển SPO và DApp - dựa trên 3 tiêu chí chính:

1. Không có vấn đề quan trọng nào còn tồn tại trên node (bao gồm sổ cái, CLI, sự đồng thuận, v.v.) hoặc chức năng kiểm toán nội bộ của chúng tôi,
2. Đo điểm chuẩn và phân tích hiệu suất-chi phí có thể chấp nhận được, và
3. Cộng đồng (bao gồm các sàn giao dịch và các dự án DApp) đã được thông báo chính xác và đã có đủ thời gian để chuẩn bị cho sự kiện tổ hợp hard fork.

The project continues to track well against these criteria. Once we can comfortably and confidently tick all these boxes, we can move forward and hard fork the Cardano testnet, marking the final countdown to the mainnet hard fork. The Cardano Foundation integration team leads this process, and typically aims to give exchanges 4 weeks to finish their own integrations/updates. The pareto principle tends to be followed here - aiming to achieve 80% exchange compliance (by liquidity) before mainnet hard fork thus minimizing inconvenience for users while recognizing different exchanges can work to different timelines.

Hôm nay, IOG và Cardano Foundation đã thống nhất một mục tiêu mới để hard fork testnet vào cuối tháng 6. Sau khi hoàn thành, chúng tôi sẽ đợi bốn tuần để các sàn giao dịch và SPO thực hiện bất kỳ công việc tích hợp và thử nghiệm bắt buộc nào. Điều này là hợp lý và không nên vội vàng. Do đó, giả định đang hoạt động bây giờ sẽ là một đợt hard fork của mạng chính Cardano xảy ra vào tuần cuối cùng của tháng Bảy.

Chúng tôi nhận ra rằng tin tức này sẽ gây thất vọng cho một số người. Tuy nhiên, chúng tôi đang hết sức thận trọng để đảm bảo rằng chúng tôi thực hiện việc triển khai này một cách chính xác.

As we have consistently communicated, and most in the community recognizes, no timelines can be absolute in software development. Quality and security must remain paramount. If more time is needed to get the core code right - and ensure all ecosystem players (SPOs, DApp projects, tools, exchanges, etc.) are fully comfortable – so be it. Giving the process longer is the only responsible thing to do.

The IOG and Cardano Foundation teams will continue to work closely with the developer community and exchanges as we draw closer to the Vasil hardfork on mainnet. And to keep the updates to the community coming. Thanks to all of you for your support.
