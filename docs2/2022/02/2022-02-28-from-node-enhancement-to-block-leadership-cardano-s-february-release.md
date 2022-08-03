# From node enhancement to block leadership… Cardano’s February release
### **In 2022 we’re grouping multiple code releases to improve delivery predictability for the ecosystem. Here’s what’s coming in our first major update of 2022**
![](img/2022-02-28-from-node-enhancement-to-block-leadership-cardano-s-february-release.002.png) 28 February 2022![](img/2022-02-28-from-node-enhancement-to-block-leadership-cardano-s-february-release.002.png)[ Tim Harrison](tmp//en/blog/authors/tim-harrison/page-1/)![](img/2022-02-28-from-node-enhancement-to-block-leadership-cardano-s-february-release.003.png) 4 mins read

![Tim Harrison](img/2022-02-28-from-node-enhancement-to-block-leadership-cardano-s-february-release.004.png)[](tmp//en/blog/authors/tim-harrison/page-1/)
### [**Tim Harrison**](tmp//en/blog/authors/tim-harrison/page-1/)
VP of Community & Ecosystem

Communications

- ![](img/2022-02-28-from-node-enhancement-to-block-leadership-cardano-s-february-release.005.png)[](mailto:tim.harrison@iohk.io "Email")
- ![](img/2022-02-28-from-node-enhancement-to-block-leadership-cardano-s-february-release.006.png)[](https://uk.linkedin.com/in/timbharrison "LinkedIn")
- ![](img/2022-02-28-from-node-enhancement-to-block-leadership-cardano-s-february-release.007.png)[](https://twitter.com/timbharrison "Twitter")
- ![](img/2022-02-28-from-node-enhancement-to-block-leadership-cardano-s-february-release.008.png)[](https://github.com/timbharrison "GitHub")

![From node enhancement to block leadership… Cardano’s February release](img/2022-02-28-from-node-enhancement-to-block-leadership-cardano-s-february-release.009.jpeg)

Following the deployment of smart contract capabilities with the Alonzo update, Cardano is now focused on performance optimization and scalability. We’re now starting to see a diverse range of decentralized applications (DApps) and exchanges (DEXs) launch, with many more to come over the months ahead. 2022 is the year when Cardano starts evolving into a platform to provide sustainable finance ([RealFi](https://iohk.io/en/blog/posts/2021/11/25/welcome-to-the-age-of-realfi/)) for real people, and an environment where future developments will be regulated by a framework of decentralized governance. 

Sau khi triển khai các khả năng hợp đồng thông minh với bản cập nhật Alonzo, Cardano hiện đang tập trung vào tối ưu hóa hiệu suất và khả năng mở rộng.
Hiện tại, chúng tôi bắt đầu thấy một loạt các ứng dụng phi tập trung (DAPP) và trao đổi (DEXS), với nhiều hơn nữa sẽ đến trong những tháng tới.
2022 là năm mà Cardano bắt đầu phát triển thành một nền tảng để cung cấp tài chính bền vững ([realfi] (https://iohk.io/en/blog/posts/2021/11/25/welcome-to-the-age-of-
Realfi/)) cho người thật, và một môi trường nơi phát triển trong tương lai sẽ được điều chỉnh bởi một khuôn khổ quản trị phi tập trung.

Throughout the coming weeks and months, we will be optimizing, scaling and bringing new features through new release deployments. We will do this in well-defined incremental updates that groups new features for our technology stack into more manageable periodic releases. We’re now in the very final stages of preparing our February release, the first of three major code drops (June and October will follow) upgrading the core network in 2022.

Trong suốt những tuần và tháng tới, chúng tôi sẽ tối ưu hóa, mở rộng và mang lại các tính năng mới thông qua triển khai phát hành mới.
Chúng tôi sẽ thực hiện điều này trong các bản cập nhật gia tăng được xác định rõ ràng, nhóm các tính năng mới cho công nghệ của chúng tôi vào các bản phát hành định kỳ dễ quản lý hơn.
Bây giờ chúng tôi đang trong giai đoạn cuối của việc chuẩn bị phát hành tháng 2, lần đầu tiên trong ba lần giảm mã chính (tháng 6 và tháng 10 sẽ theo sau) nâng cấp mạng cốt lõi vào năm 2022.

This grouping strategy has one clear rationale: predictability. Cardano has grown significantly, and it's expected to grow even more as 2022 goes on. By creating specific release windows, companies that rely on Cardano's infrastructure know exactly when major releases are coming, so they can prepare accordingly.

Chiến lược nhóm này có một lý do rõ ràng: dự đoán.
Cardano đã phát triển đáng kể và dự kiến sẽ phát triển hơn nữa khi năm 2022 tiếp tục.
Bằng cách tạo ra các cửa sổ phát hành cụ thể, các công ty dựa vào cơ sở hạ tầng của Cardano biết chính xác khi nào các bản phát hành chính sắp ra mắt, vì vậy họ có thể chuẩn bị cho phù hợp.

### **Coming in this release**

### ** sắp phát hành này **

The first major release of 2022 contains some powerful improvements and enhancements:

Bản phát hành chính đầu tiên của năm 2022 chứa một số cải tiến và cải tiến mạnh mẽ:

- Ability to create transactions conforming to the Concise Data Definition Language (CDDL) using native tools CLI that ship with the node, rather than requiring third-party tools.

- Khả năng tạo các giao dịch phù hợp với ngôn ngữ định nghĩa dữ liệu (CDDL) ngắn gọn bằng cách sử dụng các công cụ gốc CLI vận chuyển với nút, thay vì yêu cầu các công cụ của bên thứ ba.

- Multi-signature of transactions in incremental stages. While it is already possible to have a Cardano transaction signed by multiple entities (something similar to a joint bank account) using their private keys, this update makes it possible to sign a transaction incrementally. Now, for example, one party can sign the transaction first, then send it over to someone else, instead of having to sign it together.

- Đa tín hiệu của các giao dịch trong các giai đoạn gia tăng.
Mặc dù đã có thể có một giao dịch Cardano có chữ ký của nhiều thực thể (một thứ tương tự như tài khoản ngân hàng chung) bằng cách sử dụng khóa riêng của họ, bản cập nhật này có thể ký một giao dịch tăng dần.
Bây giờ, ví dụ, một bên có thể ký giao dịch trước, sau đó gửi nó cho người khác, thay vì phải ký hợp đồng với nhau.

- New CLI tool for SPOs to check the leadership schedule. This tool enables SPOs to review the next epoch and check the slots where the SPO that is executing the command will mint a block. Some might think that this ability might raise security questions, but the tool is designed in such a way that any given SPO can only check their own upcoming schedule. They cannot check any other SPO's schedules.

- Công cụ CLI mới cho SPO để kiểm tra lịch trình lãnh đạo.
Công cụ này cho phép các SPO xem xét kỷ nguyên tiếp theo và kiểm tra các vị trí trong đó spo đang thực thi lệnh sẽ đúc một khối.
Một số người có thể nghĩ rằng khả năng này có thể đưa ra các câu hỏi bảo mật, nhưng công cụ được thiết kế theo cách mà bất kỳ SPO nào chỉ có thể kiểm tra lịch trình sắp tới của riêng họ.
Họ không thể kiểm tra bất kỳ lịch trình của SPO nào khác.

- CLI tool for local mempool inspection. This is a developer tool that enables inspection of the local mempool where transactions sit before they are included in a block. This feature allows developers to follow a transaction's progress before it gets added to a block. 

- Công cụ CLI để kiểm tra mempool địa phương.
Đây là một công cụ phát triển cho phép kiểm tra các mempool địa phương nơi các giao dịch ngồi trước khi chúng được đưa vào một khối.
Tính năng này cho phép các nhà phát triển theo dõi tiến trình của giao dịch trước khi nó được thêm vào một khối.

- CLI tool to estimate script cost. Node users will now be able to accurately estimate the cost of running a Plutus script. The utility of this is that it enables developers to look at the resources (memory limits, CPU limits, etc.) they use when writing smart contracts or validation scripts, which is very useful when crafting Plutus transactions. Now, developers can know how much resources will their scripts use when executing on-chain.

- Công cụ CLI để ước tính chi phí tập lệnh.
Người dùng nút bây giờ sẽ có thể ước tính chính xác chi phí chạy tập lệnh Plutus.
Tiện ích của điều này là nó cho phép các nhà phát triển xem xét các tài nguyên (giới hạn bộ nhớ, giới hạn CPU, v.v.) họ sử dụng khi viết hợp đồng thông minh hoặc tập lệnh xác thực, rất hữu ích khi chế tạo các giao dịch Plutus.
Bây giờ, các nhà phát triển có thể biết các tập lệnh của họ sẽ sử dụng bao nhiêu tài nguyên khi thực hiện trên chuỗi.

Our February release is just the start. [Throughout 2022](https://iohk.io/en/blog/posts/2022/01/14/how-we-re-scaling-cardano-in-2022/) – and focused around June and October hard fork combinator (HFC) events – we will introduce an array of scaling enhancements. These include key elements of our scaling plan like pipelining, new Plutus CIPs, UTXO on-disk storage and Hydra. In combination with parameter adjustments, these features will enhance Cardano's throughput and optimize the system to accommodate an increasing range of decentralized finance (DeFi) apps, smart contracts, and DEXs. Plus as outlined in our recent Cardano360 February show, IOG is working across a host of new products and features, from a DApp store and a new light wallet product, to Mithril fast sync solution and sidechains. All the while an incredible community contributes new DApps, services, sites, tools and APIs to keep building out a flourishing decentralized ecosystem. An exciting 2022 lies ahead. Onwards…

Bản phát hành tháng hai của chúng tôi chỉ là khởi đầu.
[Trong suốt năm 2022] (https://iohk.io/en/blog/posts/2022/01/14/how-we-re-scaling-cardano-in-2022/)-và tập trung vào khoảng tháng 6 và tháng 10
(HFC) Sự kiện - Chúng tôi sẽ giới thiệu một loạt các cải tiến tỷ lệ.
Chúng bao gồm các yếu tố chính của kế hoạch mở rộng của chúng tôi như đường ống, CIP Plutus mới, lưu trữ trên đĩa UTXO và hydra.
Kết hợp với các điều chỉnh tham số, các tính năng này sẽ tăng cường thông lượng của Cardano và tối ưu hóa hệ thống để phù hợp với phạm vi ngày càng tăng của các ứng dụng tài chính phi tập trung (hợp đồng thông minh và DEXS.
Ngoài ra, như được nêu trong chương trình Cardano360 tháng 2 gần đây của chúng tôi, IOG đang hoạt động trên một loạt các sản phẩm và tính năng mới, từ một cửa hàng DAPP và một sản phẩm ví nhẹ mới, đến giải pháp đồng bộ hóa nhanh Mithril.
Tất cả trong khi một cộng đồng đáng kinh ngạc đóng góp DAPP, dịch vụ, trang web, công cụ và API mới để tiếp tục xây dựng một hệ sinh thái phi tập trung hưng thịnh.
Một năm 2022 thú vị nằm ở phía trước.
Trở đi…

