# Từ  việc cải tiến node đến việc node được đóng block… Bản phát hành tháng 2 của Cardano

### **Vào năm 2022, chúng tôi sẽ gộp nhiều bản phần mềm để cải thiện khả năng dự đoán phân phối cho hệ sinh thái. Đây là những gì sẽ ra mắt trong bản cập nhật lớn đầu tiên của chúng tôi vào năm 2022**

![](img/2022-02-28-from-node-enhancement-to-block-leadership-cardano-s-february-release.002.png) 28 February 2022![](img/2022-02-28-from-node-enhancement-to-block-leadership-cardano-s-february-release.002.png)[ Tim Harrison](/en/blog/authors/tim-harrison/page-1/)![](img/2022-02-28-from-node-enhancement-to-block-leadership-cardano-s-february-release.003.png) 4 mins read

![Tim Harrison](img/2022-02-28-from-node-enhancement-to-block-leadership-cardano-s-february-release.004.png)[](/en/blog/authors/tim-harrison/page-1/)

### [**Tim Harrison**](/en/blog/authors/tim-harrison/page-1/)

VP of Community &amp; Ecosystem

Communications

- ![](img/2022-02-28-from-node-enhancement-to-block-leadership-cardano-s-february-release.005.png)[](mailto:tim.harrison@iohk.io "Email")
- ![](img/2022-02-28-from-node-enhancement-to-block-leadership-cardano-s-february-release.006.png)[](https://uk.linkedin.com/in/timbharrison "LinkedIn")
- ![](img/2022-02-28-from-node-enhancement-to-block-leadership-cardano-s-february-release.007.png)[](https://twitter.com/timbharrison "Twitter")
- ![](img/2022-02-28-from-node-enhancement-to-block-leadership-cardano-s-february-release.008.png)[](https://github.com/timbharrison "GitHub")

![From node enhancement to block leadership… Cardano’s February release](img/2022-02-28-from-node-enhancement-to-block-leadership-cardano-s-february-release.009.jpeg)

Sau khi triển khai các khả năng của hợp đồng thông minh với bản cập nhật Alonzo, Cardano hiện đang tập trung vào việc tối ưu hóa hiệu suất và khả năng mở rộng. Giờ đây, chúng ta bắt đầu thấy một loạt các ứng dụng phi tập trung (Dapps), sàn giao dịch (DEX) và nhiều ứng dụng khác sẽ ra mắt trong những tháng tới. Năm 2022 là năm Cardano phát triển thành một nền tảng cung cấp tài chính bền vững ([RealFi](https://iohk.io/en/blog/posts/2021/11/25/welcome-to-the-age-of-realfi/)) cho những người thực và là một môi trường nơi các phát triển trong tương lai sẽ được điều chỉnh bởi một hệ thống quản trị phi tập trung.

Throughout the coming weeks and months, we will be optimizing, scaling and bringing new features through new release deployments. We will do this in well-defined incremental updates that groups new features for our technology stack into more manageable periodic releases. We’re now in the very final stages of preparing our February release, the first of three major code drops (June and October will follow) upgrading the core network in 2022.

Chiến lược phân nhóm này có một cơ sở lý luận rõ ràng: là khả năng dự đoán. Cardano đã phát triển đáng kể và dự kiến ​​sẽ còn phát triển hơn nữa sau 2022. Bằng cách tạo lịch phát hành cụ thể, các công ty dựa vào cơ sở hạ tầng của Cardano biết chính xác khi nào các bản phát hành lớn sắp ra mắt, vì vậy họ có thể chuẩn bị cho phù hợp.

### **Coming in this release**

Bản phát hành lớn đầu tiên của năm 2022 chứa một số cải tiến và nâng cấp:

- Ability to create transactions conforming to the Concise Data Definition Language (CDDL) using native tools CLI that ship with the node, rather than requiring third-party tools.
- Multi-signature of transactions in incremental stages. While it is already possible to have a Cardano transaction signed by multiple entities (something similar to a joint bank account) using their private keys, this update makes it possible to sign a transaction incrementally. Now, for example, one party can sign the transaction first, then send it over to someone else, instead of having to sign it together.
- New CLI tool for SPOs to check the leadership schedule. This tool enables SPOs to review the next epoch and check the slots where the SPO that is executing the command will mint a block. Some might think that this ability might raise security questions, but the tool is designed in such a way that any given SPO can only check their own upcoming schedule. They cannot check any other SPO's schedules.
- CLI tool for local mempool inspection. This is a developer tool that enables inspection of the local mempool where transactions sit before they are included in a block. This feature allows developers to follow a transaction's progress before it gets added to a block.
- CLI tool to estimate script cost. Node users will now be able to accurately estimate the cost of running a Plutus script. The utility of this is that it enables developers to look at the resources (memory limits, CPU limits, etc.) they use when writing smart contracts or validation scripts, which is very useful when crafting Plutus transactions. Now, developers can know how much resources will their scripts use when executing on-chain.

Bản phát hành tháng hai của chúng tôi chỉ là khởi đầu. [Trong suốt năm 2022](https://iohk.io/en/blog/posts/2022/01/14/how-we-re-scaling-cardano-in-2022/)- và tập trung vào các sự kiện tổ hợp hard fork (HFC) vào tháng 6 và tháng 10 - chúng tôi sẽ giới thiệu một loạt các cải tiến mở rộng quy mô. Bao gồm các yếu tố chính trong kế hoạch mở rộng quy mô của chúng tôi như pipelining (phát tán đồng thời), Plutus CIPs mới, lưu trữ trên đĩa UTXO và Hydra. Kết hợp với việc điều chỉnh thông số, các tính năng này sẽ nâng cao lưu lượng của Cardano và tối ưu hóa hệ thống để đáp ứng ngày càng nhiều các ứng dụng tài chính phi tập trung (DeFi), hợp đồng thông minh và DEX. Ngoài ra, như đã nêu trong chương trình Cardano360 tháng 2 gần đây của chúng tôi, IOG đang làm việc trên một loạt các sản phẩm và tính năng mới, từ cửa hàng DApp và sản phẩm ví nhẹ mới, đến giải pháp đồng bộ hóa nhanh Mithril và những sidechain. Trong khi đó, một cộng đồng đáng kinh ngạc đang đóng góp những DApp, dịch vụ, trang web, công cụ và API mới để tiếp tục xây dựng một hệ sinh thái phi tập trung phát triển mạnh mẽ. Một năm 2022 thú vị đang ở phía trước. Xa hơn nữa...<br><br><br>Bài này được dịch bởi Lê Nguyên, kiểm tra nội dung bởi Tienna <a class="_active_edit_href" href="https://iohk.io/en/blog/posts/2022/02/28/from-node-enhancement-to-block-leadership-cardano-s-february-release/">với bài gốc</a><br><em>Dự án này được tài trợ bới Catalyst</em>
