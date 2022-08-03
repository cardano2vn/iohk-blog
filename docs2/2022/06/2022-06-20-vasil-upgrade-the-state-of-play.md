# Vasil upgrade - the state of play
### **Very close but a little further still to go. Here’s an update on the progress towards the Vasil upgrade** 
![](img/2022-06-20-vasil-upgrade-the-state-of-play.002.png) 20 June 2022![](img/2022-06-20-vasil-upgrade-the-state-of-play.002.png)[ Nigel Hemsley](tmp//en/blog/authors/nigel-hemsley/page-1/)![](img/2022-06-20-vasil-upgrade-the-state-of-play.003.png) 4 mins read

![Nigel Hemsley](img/2022-06-20-vasil-upgrade-the-state-of-play.004.png)[](tmp//en/blog/authors/nigel-hemsley/page-1/)
### [**Nigel Hemsley**](tmp//en/blog/authors/nigel-hemsley/page-1/)
Head of Delivery and Projects

Operations

- ![](img/2022-06-20-vasil-upgrade-the-state-of-play.005.png)[](mailto:nigel.hemsley@iohk.io "Email")
- ![](img/2022-06-20-vasil-upgrade-the-state-of-play.006.png)[](tmp/www.linkedin.com/in/nigel-hemsley-433a213 "LinkedIn")

![Vasil upgrade - the state of play](img/2022-06-20-vasil-upgrade-the-state-of-play.007.png)

On Friday, the core Input Output Global (IOG) team working toward the Vasil upgrade held its regular end-of-week evaluation call. Today (Monday, June 20) was the latest date that we could facilitate a Cardano testnet upgrade before the next epoch boundary, so we agreed to re-evaluate the latest status this afternoon, taking into account the work our engineers did over the weekend. 

Vào thứ Sáu, nhóm đầu ra cốt lõi toàn cầu (IOG) làm việc hướng tới việc nâng cấp Vasil đã tổ chức cuộc gọi đánh giá cuối tuần thường xuyên.
Hôm nay (Thứ Hai, ngày 20 tháng 6) là ngày mới nhất mà chúng tôi có thể tạo điều kiện nâng cấp Cardano Testnet trước ranh giới kỷ nguyên tiếp theo, vì vậy chúng tôi đã đồng ý đánh giá lại tình trạng mới nhất vào chiều nay, có tính đến công việc các kỹ sư của chúng tôi đã làm vào cuối tuần.

The IOG engineering team is extremely close to finalizing the core work, with just seven bugs still outstanding to complete the hard fork work, with none currently ranked as ‘severe’. After some consideration, we have agreed NOT to send the hard fork update proposal to the testnet today to allow more time for testing.

Nhóm IOG Engineering rất gần để hoàn thiện công việc cốt lõi, chỉ với bảy lỗi vẫn còn nổi bật để hoàn thành công việc khó khăn, không có công việc nào được xếp hạng là ’nghiêm trọng.
Sau một số xem xét, chúng tôi đã đồng ý không gửi đề xuất cập nhật hard fork cho testnet ngay hôm nay để cho phép nhiều thời gian hơn để thử nghiệm.

To date, we’ve managed to get through the majority (approx 95%) of our [Plutus V2 test scripts](https://github.com/input-output-hk/cardano-node-tests/issues/1079). However, we still have a few outstanding items that we need to run to confirm everything is working as expected. We have determined we'll need a few more days for this. This puts us behind schedule on our previously communicated target date of June 29 for a mainnet hard fork.

Cho đến nay, chúng tôi đã quản lý để vượt qua đa số (khoảng 95%) của [SScripts V2 của Plutus V2] (https://github.com/input-output-hk/cardano-node-tests/issues/1079)
.
Tuy nhiên, chúng tôi vẫn có một vài mục nổi bật mà chúng tôi cần chạy để xác nhận mọi thứ đang hoạt động như mong đợi.
Chúng tôi đã xác định chúng tôi sẽ cần thêm một vài ngày cho việc này.
Điều này đặt chúng tôi đằng sau lịch trình vào ngày mục tiêu được truyền đạt trước đây của chúng tôi là ngày 29 tháng 6 cho một hard hard chính.

Since the start of June, we have been successfully running an early build of the new node (which includes diffusion pipelining and the new Plutus v2 CIPs among other enhancements) as a semi-public Vasil developer testnet (Devnet). We now have some 35 developers from across 27 projects testing their DApps and helping identify any issues, along with 16 stake pool operators (SPOs) supporting. We’re also working closely with some of the leading tool/API providers, including [Blockfrost](https://blockfrost.io/), Cardano Serialization library (EMURGO), and Cardano Multiplatform Library (dcSpark). We want to call out the work of Mlabs and Dquadrant in particular for providing great support throughout the process. This developer testnet stage puts us in a good position when it comes to Plutus code compatibility and functionality. This valuable work will continue on this development testnet over the next few weeks. 

Kể từ đầu tháng 6, chúng tôi đã chạy thành công bản dựng sớm của nút mới (bao gồm đường ống khuếch tán và CIP Plutus V2 mới trong số các cải tiến khác) như một nhà phát triển Vasil bán công khai (DevNet).
Bây giờ chúng tôi có khoảng 35 nhà phát triển từ 27 dự án kiểm tra DAPP của họ và giúp xác định bất kỳ vấn đề nào, cùng với 16 nhà khai thác nhóm cổ phần (SPO) hỗ trợ.
Chúng tôi cũng hợp tác chặt chẽ với một số nhà cung cấp công cụ/API hàng đầu, bao gồm [Blockfrost] (https://blockfrost.io/), Thư viện tuần tự hóa Cardano (EMURGO) và Thư viện đa dạng Cardano (DCSPARK).
Chúng tôi muốn gọi ra công việc của MLABS và Dquadrant nói riêng để cung cấp hỗ trợ tuyệt vời trong suốt quá trình.
Giai đoạn TestNet nhà phát triển này đặt chúng ta vào một vị trí tốt khi nói đến tính tương thích và chức năng của mã Plutus.
Công việc có giá trị này sẽ tiếp tục trên TestNet phát triển này trong vài tuần tới.

The work on Vasil has been the most complex program of development and integration to date, from several angles. It's a challenging process that requires not only significant work from core teams, but also close coordination across the ecosystem.

Công việc trên Vasil là chương trình phát triển và tích hợp phức tạp nhất cho đến nay, từ một số góc độ.
Đó là một quá trình đầy thách thức đòi hỏi không chỉ công việc quan trọng từ các nhóm cốt lõi, mà còn phối hợp chặt chẽ trên toàn hệ sinh thái.

The final decision to hard fork the Cardano Testnet will be made – in consultation with members of the SPO and DApp development community – against 3 key criteria:

Quyết định cuối cùng về Hard Fork The Cardano Testnet sẽ được đưa ra - tham khảo ý kiến của các thành viên của cộng đồng phát triển SPO và DAPP - theo 3 tiêu chí chính:

1. No critical issues outstanding on node (including ledger, CLI, consensus, etc.) or our internal audit function, 

1. Không có vấn đề quan trọng nào nổi bật trên nút (bao gồm sổ cái, CLI, đồng thuận, v.v.) hoặc chức năng kiểm toán nội bộ của chúng tôi,

1. Benchmarking and performance-cost analysis is acceptable, and

1. Phân tích điểm chuẩn và chi phí hiệu suất được chấp nhận và

1. Community (including exchanges and DApp projects) has been properly informed and has had sufficient time to prepare for the hard fork combinator event.

1. Cộng đồng (bao gồm cả trao đổi và các dự án DAPP) đã được thông báo đúng và đã có đủ thời gian để chuẩn bị cho sự kiện tổ hợp hard fork.

The project continues to track well against these criteria. Once we can comfortably and confidently tick all these boxes, we can move forward and hard fork the Cardano testnet, marking the final countdown to the mainnet hard fork. The Cardano Foundation integration team leads this process, and typically aims to give exchanges 4 weeks to finish their own integrations/updates. The pareto principle tends to be followed here - aiming to achieve 80% exchange compliance (by liquidity) before mainnet hard fork thus minimizing inconvenience for users while recognizing different exchanges can work to different timelines.

Dự án tiếp tục theo dõi tốt các tiêu chí này.
Một khi chúng tôi có thể thoải mái và tự tin đánh dấu vào tất cả các hộp này, chúng tôi có thể tiến về phía trước và khó khăn trong cardano testnet, đánh dấu sự đếm ngược cuối cùng đến hardnet hard fork.
Nhóm Tích hợp Cardano Foundation dẫn đầu quá trình này và thường nhằm mục đích cung cấp trao đổi 4 tuần để hoàn thành các tích hợp/cập nhật của riêng họ.
Nguyên tắc Pareto có xu hướng được tuân thủ ở đây - nhằm mục đích đạt được sự tuân thủ trao đổi 80% (bằng thanh khoản) trước khi Fork Mainnet Hard, do đó giảm thiểu sự bất tiện cho người dùng trong khi nhận ra các trao đổi khác nhau có thể hoạt động theo các mốc thời gian khác nhau.

Today, IOG and the Cardano Foundation have agreed a new target date to hard fork the testnet at the end of June. Once completed, we will then allow four weeks for exchanges and SPOs to carry out any required integration and testing work. This is only reasonable and should not be rushed. The working assumption should therefore now be a Cardano mainnet hard fork occurring during the last week of July.

Hôm nay, IOG và Quỹ Cardano đã đồng ý một ngày mục tiêu mới để làm khó thử testnet vào cuối tháng Sáu.
Sau khi hoàn thành, sau đó chúng tôi sẽ cho phép bốn tuần để trao đổi và SPO thực hiện bất kỳ công việc tích hợp và thử nghiệm cần thiết nào.
Điều này chỉ là hợp lý và không nên vội vàng.
Do đó, giả định làm việc bây giờ nên là một chiếc xe ngựa cứng Cardano xảy ra trong tuần cuối cùng của tháng Bảy.

We recognize that this news will be disappointing to some. However, we are taking an abundance of caution to ensure that we do this deployment correctly. 

Chúng tôi nhận ra rằng tin tức này sẽ gây thất vọng cho một số người.
Tuy nhiên, chúng tôi đang thận trọng rất nhiều để đảm bảo rằng chúng tôi thực hiện việc triển khai này một cách chính xác.

As we have consistently communicated, and most in the community recognizes, no timelines can be absolute in software development. Quality and security must remain paramount. If more time is needed to get the core code right - and ensure all ecosystem players (SPOs, DApp projects, tools, exchanges, etc.) are fully comfortable – so be it. Giving the process longer is the only responsible thing to do.

Vì chúng tôi đã liên tục truyền đạt và hầu hết trong cộng đồng nhận ra, không có mốc thời gian nào có thể là tuyệt đối trong phát triển phần mềm.
Chất lượng và bảo mật phải duy trì điều tối quan trọng.
Nếu cần nhiều thời gian hơn để có được mã cốt lõi - và đảm bảo tất cả người chơi hệ sinh thái (SPO, dự án DAPP, công cụ, trao đổi, v.v.) hoàn toàn thoải mái - vì vậy hãy là nó.
Cho quá trình lâu hơn là điều duy nhất có trách nhiệm để làm.

The IOG and Cardano Foundation teams will continue to work closely with the developer community and exchanges as we draw closer to the Vasil hardfork on mainnet. And to keep the updates to the community coming. Thanks to all of you for your support.

Các nhóm IOG và Cardano Foundation sẽ tiếp tục hợp tác chặt chẽ với cộng đồng nhà phát triển và trao đổi khi chúng tôi đến gần hơn với Vasil Hardfork trên Mainnet.
Và để giữ các bản cập nhật cho cộng đồng sắp tới.
Cảm ơn tất cả các bạn vì sự hỗ trợ của bạn.

