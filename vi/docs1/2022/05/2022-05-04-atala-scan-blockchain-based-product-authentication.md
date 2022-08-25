# Atala SCAN: xác thực sản phẩm dựa trên blockchain

### **Cách một vi mạch thông minh có thể hoạt động với một blockchain tiên tiến để chống lại những kẻ làm giả sản phẩm**

![](img/2022-05-04-atala-scan-blockchain-based-product-authentication.002.png) Ngày 4 tháng 5 năm 2022![](img/2022-05-04-atala-scan-blockchain-based-product-authentication.002.png)[ Neil Burgess](/en/blog/authors/neil-burgess/page-1/)![](img/2022-05-04-atala-scan-blockchain-based-product-authentication.003.png) bài đọc6 phút

![Neil Burgess](img/2022-05-04-atala-scan-blockchain-based-product-authentication.004.png)[](/en/blog/authors/neil-burgess/page-1/)

### [**Neil Burgess**](/en/blog/authors/neil-burgess/page-1/)

Technical Writer

Marketing &amp; Communications

- ![](img/2022-05-04-atala-scan-blockchain-based-product-authentication.005.png)[](mailto:neil.burgess@iohk.io "Email")
- ![](img/2022-05-04-atala-scan-blockchain-based-product-authentication.006.png)[](https://www.linkedin.com/in/neilburgessa84482125 "LinkedIn")

![Atala SCAN: xác thực sản phẩm dựa trên blockchain](img/2022-05-04-atala-scan-blockchain-based-product-authentication.007.jpeg)

Youâ€™ve paid a premium price for that collectible bottle of premium spirits, but thereâ€™s that nagging doubt. Do you trust the retailer and all the actors in the supply chain to act with complete integrity?

Bạn mua một loại thuốc đắt tiền từ một hiệu thuốc trực tuyến. Bạn có chắc chắn bạn nhận được những gì bạn đã trả? Atala SCAN - hệ thống xác thực sản phẩm của IOG - có thể trả lời các câu hỏi của bạn mà không cần phải tin tưởng vào nhà bán lẻ hoặc bất kỳ ai trong chuỗi cung ứng.

Part of the solution for bottles of spirits is a smart seal that knows if it has been tampered with. Atala adds to this an encrypted, auditable link between the seal and the full manufacturing history of the specific bottle to which the seal is attached. You can check the history using a free app on your phone that can instantly verify a productâ€™s authenticity.

[Atala SCAN](https://atalascan.io/) được xây dựng trên công nghệ blockchain thế hệ thứ ba của Cardano. Phần mềm blockchain kết hợp với công nghệ 'chip cảm ứng' mang lại những lợi thế thực sự so với các phương pháp bảo mật truyền thống như niêm phong nắp, ảnh ba chiều và bao bì kỳ công - lịch sử của sản phẩm có thể được khách hàng kiểm tra ngay lập tức.

### **Vấn đề và giải pháp**

The need for improved security on products such as premium spirits, cosmetics, fashion goods, and prescription medication is being driven by the battle against ever-more sophisticated counterfeiters. The United Nations agency that is coordinating the fight against transnational organized crime groups [describes the problem](https://www.unodc.org/toc/en/crimes/counterfeit-goods.html): â€˜The production and sale of counterfeit goods is a global, multi-billion dollar problem and one that has serious economic and health ramifications for governments, businesses and consumers.â€™

The size of the international counterfeit market doubled from US$200bn in 2008 to US$509bn in 2019 â€“ equivalent to 2.5% of world trade, [according to the US Patent and Trademark Office](https://www.uspto.gov/sites/default/files/documents/USPTO-Counterfeit.pdf). Counterfeiting at such a scale costs jobs in manufacturing, endangers the lives of food and pharmacy customers, and deprives innovators of due rewards for their efforts.

IOGâ€™s solution to counterfeiting crime is an integrated system comprising a smart seal based on a â€˜chip with wingsâ€™ that can be linked at the touch of a smartphone to the production records of the item. The records are held in secure storage that cannot be changed. Purchasers can check the provenance quickly, easily, and at no charge.

### **The smart seal**

The smart seal is at the heart of the system. It is a wafer-thin label incorporating a [near-field communication (NFC) chip](http://nearfieldcommunication.org/how-it-works.html). It is small enough to be glued to a product, incorporated in a card, or embedded in a product or its packaging. For example, it can be part of a special bottle cap or stitched into a handbag. You may have seen the NFC logo on a bank card. The technology allows devices to exchange information simply by touching or placing them next to one another. Like the microchips used for pet dogs, the smart seal consumes no power and silently waits for a signal from a reader. The signal induces an electric current in the chipâ€™s antenna, and that is enough power for the chip to transmit its stored data.

Điện thoại thông minh hiện đại kết hợp thiết bị NFC hai chiều như một tính năng tiêu chuẩn để điện thoại có thể hoạt động như một đầu đọc và một thẻ. Nexus S là thiết bị Android đầu tiên có tính năng này vào năm 2010, Apple đã thêm NFC vào iPhone vào năm 2014 - nó đã được tích hợp vào mọi phiên bản iPhone kể từ thế hệ 6.

Most tamper-evident NFC tags are designed to stop working if disturbed. All NFC tags need an antenna to work, and if the antenna is fragile enough, any tampering will stop the tag from working. The NTAG product used in Atala SCAN applications takes this one step further. The chip in the tag has two antennas, only one of which is designed to break. If the tag is disturbed, it continues to work but transmits a modified signal as evidence of the tampering.

Atala SCAN được thực hiện tại điểm đầu tiên trong chuỗi cung ứng, nơi cung cấp thành phẩm cho chủ sở hữu thương hiệu. Hồ sơ của chủ sở hữu thương hiệu có thể bao gồm hình ảnh sản phẩm và lịch sử đầy đủ, bao gồm cả việc truy tìm từng thành phần từ điểm xuất xứ của nó. Chủ sở hữu thương hiệu quyết định thông tin nào được tiết lộ cho khách hàng thông qua chip thông minh được nhúng. Đó có thể là dữ liệu theo dõi cơ bản hoặc một phần của chiến dịch tiếp thị tiêu dùng toàn cầu. Thông tin này được liên kết với số nhận dạng duy nhất của mỗi thẻ. Các kỹ sư của Atala SCAN có thể giúp thiết lập mối liên kết này. Sau đó, thẻ được gắn hoặc được liên kết theo một cách nào đó với từng mặt hàng sản phẩm.

### **Blockchain**

Cardano is a blockchain platform for changemakers, innovators, and visionaries. It uses the Ouroboros proof of stake protocol to achieve consensus so that it is provably secure while consuming only a fraction of the resources required by older blockchains. With Atala, every item is associated with a unique entry on Cardano. That entry cannot be altered, but can be read easily, and can be used as part of an auditing system. Each entry comprises the cryptographic hash of the tagâ€™s identifier and links to the product metadata. The metadata, including images, is stored off-chain.

Juan Ignacio Sierra, the Atala SCAN project manager, says: â€˜Working with blockchain ensures the immutability of the product information, but if thereâ€™s no mechanism in place to securely link the information to the product itself, fake products can take advantage of the same blockchain information as the originals do. In Atala SCAN we use high security cryptographic hardware in the seal to ensure the security of the link between the blockchain information and the physical product.â€™

### **Scan on your smartphone**

If you have a smartphone, you will be able to download the free Atala SCAN app from the relevant online store. This application uses a phoneâ€™s NFC reader to read the chip and look up the product information on Cardano. Simply touch the phone to the product, and know at once if the product is genuine and learn about its history.

IOG đang làm việc với một số công ty về việc khởi chạy hệ thống này.

Juan Sierra cho biết: “Atala SCAN đã ra đời được một thời gian và thật thú vị khi chúng tôi có thể bắt đầu đưa đề xuất này ra thị trường. Chúng tôi đang thảo luận với một số khách hàng tiềm năng. Chúng tôi sẽ sớm có nhiều điều để chia sẻ!"

*Nếu bạn quan tâm đến việc xác thực sản phẩm với bất kỳ lý do gì, vui lòng liên hệ với IOG thông qua trang [web Atala SCAN](https://atalascan.io/), và chúng tôi sẽ rất vui được giải đáp các thắc mắc của bạn.*

*Cảm ơn Anthony Quinn và Rachel Epstein vì những đóng góp không thể thiếu của họ cho bài đăng này.<br><br><br><br>Bài này được dịch bởi Lê Nguyên. <a class="_active_edit_href" href="https://iohk.io/en/blog/posts/2022/05/04/atala-scan-blockchain-based-product-authentication/">với bài gốc</a><br><em>Dự án này được tài trợ bởi Catalyst</em>*
