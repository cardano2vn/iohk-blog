# Runtime Verification & IELE – from interoperability to universality
### **KEVM and IELE will bring unparalleled levels of security, scalability and programmability to Cardano**
![](img/2021-05-10-runtime-verification-iele-from-interoperability-to-universality.002.png) 10 May 2021![](img/2021-05-10-runtime-verification-iele-from-interoperability-to-universality.002.png)[ Alex Hamilton](tmp//en/blog/authors/alex-hamilton/page-1/)![](img/2021-05-10-runtime-verification-iele-from-interoperability-to-universality.003.png) 4 mins read

![Alex Hamilton](img/2021-05-10-runtime-verification-iele-from-interoperability-to-universality.004.png)[](tmp//en/blog/authors/alex-hamilton/page-1/)
### [**Alex Hamilton**](tmp//en/blog/authors/alex-hamilton/page-1/)
Writer

Guest author

- ![](img/2021-05-10-runtime-verification-iele-from-interoperability-to-universality.005.png)[](https://www.linkedin.com/in/alex-hamilton-55b4b6108/ "LinkedIn")
- ![](img/2021-05-10-runtime-verification-iele-from-interoperability-to-universality.006.png)[](https://twitter.com/Immortalxplorer "Twitter")

![ Runtime Verification & IELE – from interoperability to universality](img/2021-05-10-runtime-verification-iele-from-interoperability-to-universality.007.jpeg)

[Professor Grigore Rosu](https://en.wikipedia.org/wiki/Grigore_Rosu), President and CEO of start-up Runtime Verification (RV) joined us on [March's edition of the Cardano360 show](https://youtu.be/ULBLgPgxtN8?t=1563) to share ideas and discuss the collaboration between RV and IOHK.

[Giáo sư Grigore Rosu] (https://en.wikipedia.org/wiki/grigore_rosu), Chủ tịch và Giám đốc điều hành của Xác minh thời gian chạy khởi nghiệp (RV) đã tham gia với chúng tôi trong [Phiên bản tháng 3 của Cardano360 cho thấy
.be/ulblgpgxtn8? t = 1563) để chia sẻ ý tưởng và thảo luận về sự hợp tác giữa RV và IOHK.

Our professional relationship with Grigore and RV started back in 2017, and Grigore’s credentials speak for themselves (in any language). He’s worked for NASA, DARPA, Microsoft, and has taught at the University of Illinois Urbana-Champaign, to name but a few achievements.

Mối quan hệ chuyên nghiệp của chúng tôi với Grigore và RV đã bắt đầu trở lại vào năm 2017 và thông tin đăng nhập của Grigore, nói cho chính họ (bằng bất kỳ ngôn ngữ nào).
Anh ấy làm việc cho NASA, DARPA, Microsoft và đã giảng dạy tại Đại học Illinois Urbana-Champaign, để kể tên nhưng một vài thành tựu.

Grigore is also credited with the creation of the [K Framework](https://runtimeverification.com/blog/k-framework-an-overview/), which has been described as ‘software that simply cannot afford to fail.' Developed over 15 years, the framework’s primary purpose is to enhance security. We’ll get into this in more detail later, but first, a short history lesson.

Grigore cũng được ghi nhận với việc tạo ra [K Framework] (https://runtimeverification.com/blog/k-framework-an-overview/), được mô tả là phần mềm đơn giản là không thể đủ khả năng. '
Được phát triển trong hơn 15 năm, mục đích chính của khung là để tăng cường bảo mật.
Chúng tôi sẽ hiểu chi tiết hơn sau này, nhưng trước tiên, một bài học lịch sử ngắn.

When it comes to smart contracts, the Ethereum Virtual Machine (EVM) set many early standards, for example the creation of the ubiquitous ERC-20 smart contracts, written in Solidity. However, this system isn’t flawless. Smart contracts have known coding vulnerabilities that have caused security issues. 

Khi nói đến các hợp đồng thông minh, Máy ảo Ethereum (EVM) đã thiết lập nhiều tiêu chuẩn ban đầu, ví dụ như việc tạo ra các hợp đồng thông minh ERC-20 phổ biến, được viết bằng sự vững chắc.
Tuy nhiên, hệ thống này không hoàn hảo.
Hợp đồng thông minh đã biết các lỗ hổng mã hóa đã gây ra vấn đề bảo mật.

## **IELE: Unparalleled security, scalability, and programmability**

## ** IELE: Bảo mật, khả năng mở rộng và khả năng lập trình vô song **

Since late 2020, Cardano developers have had a bridge to the Solidity/Ethereum community via the K Ethereum Virtual Machine (KEVM), an implementation of the EVM specified in the K framework, which allows developers to use the formal verification tools that K produces to check a contract's correctness. 

Từ cuối năm 2020, các nhà phát triển Cardano đã có một cầu nối cho cộng đồng Sollity/Ethereum thông qua K Ethereum Virtual Machine (KEVM), việc triển khai EVM được chỉ định trong khung K, cho phép các nhà phát triển sử dụng các công cụ xác minh chính thức mà K tạo ra cho
Kiểm tra tính chính xác của hợp đồng.

IELE takes things a step further. As discussed by Rosu on March’s Cardano360 show, IELE (named after a faerie-like [creature of Romanian myth](https://en.wikipedia.org/wiki/Iele)) is a virtual machine that executes smart contracts, and also provides a human-readable language for blockchain developers. IELE was designed with formal methods in mind to address security and correctness concerns inherent in writing Solidity smart contracts targeting Ethereum, easing the path to heightened levels of security, scalability, and programmability. 

Iele tiến thêm một bước.
Như đã thảo luận bởi Rosu trong chương trình Cardano360 của March's, IELE (được đặt theo tên
Cung cấp một ngôn ngữ có thể đọc được cho con người cho các nhà phát triển blockchain.
IELE được thiết kế với các phương pháp chính thức để giải quyết các mối quan tâm về bảo mật và tính chính xác vốn có trong việc viết các hợp đồng thông minh Solidity nhắm vào Ethereum, giảm bớt con đường đến mức độ bảo mật, khả năng mở rộng và khả năng lập trình cao.

IELE resembles the intermediate representation of the LLVM compiler. This enables drawing on the wealth of knowledge available in the LLVM community, specifically, the work that has gone into writing safe and effective compiler optimization passes over LLVM IR. Much of the effort put into the LLVM compiler can be ported to the IELE optimizer as well.

IELE giống như biểu diễn trung gian của trình biên dịch LLVM.
Điều này cho phép dựa trên sự giàu có của kiến thức có sẵn trong cộng đồng LLVM, cụ thể là công việc đã viết tối ưu hóa trình biên dịch an toàn và hiệu quả vượt qua LLVM IR.
Phần lớn nỗ lực đưa vào trình biên dịch LLVM cũng có thể được chuyển đến trình tối ưu hóa IELE.

## **About LLVM**

## ** Giới thiệu về LLVM **

When IELE is implemented (Rosu indicated that an initial proof of concept would be available for testing around six months from now), the opportunity for development will be even wider. IELE operates more like a passport than a virtual machine, opening the doors – if not the floodgates – to a wealth of new and unique talent. Some developers may have once dismissed the idea of entering the blockchain space, as it would likely have meant learning an entirely new programming language. As a direct result of RV’s innovative approach, any developer wanting to get involved in smart contracts can write them in a language they are comfortable with, including Solidity. The resulting output would run successfully on any IELE-powered blockchain, irrespective of the source language.

Khi IELE được thực hiện (ROSU chỉ ra rằng một bằng chứng ban đầu về khái niệm sẽ có sẵn để thử nghiệm khoảng sáu tháng kể từ bây giờ), cơ hội phát triển sẽ còn rộng hơn.
IELE vận hành giống như một hộ chiếu hơn là một máy ảo, mở cửa - nếu không phải là lũ lụt - với vô số tài năng mới và độc đáo.
Một số nhà phát triển có thể đã từng loại bỏ ý tưởng vào không gian blockchain, vì điều đó có thể có nghĩa là học một ngôn ngữ lập trình hoàn toàn mới.
Do kết quả trực tiếp của cách tiếp cận sáng tạo RV, bất kỳ nhà phát triển nào muốn tham gia vào các hợp đồng thông minh đều có thể viết chúng bằng ngôn ngữ mà họ cảm thấy thoải mái, bao gồm cả sự vững chắc.
Đầu ra kết quả sẽ chạy thành công trên bất kỳ blockchain nào do IELE cung cấp, không phân biệt ngôn ngữ nguồn.

## **What does this mean for Cardano?**

## ** Điều này có ý nghĩa gì đối với Cardano? **

This achievement will offer developers and businesses yet another incentive to migrate from Ethereum and participate in the Cardano blockchain. Openness, inclusivity, and interoperability are the foundations upon which Cardano was built. Our philosophy is – and always has been – to welcome developers from all backgrounds, to ensure Cardano’s steady evolution. Rosu has bold plans. 'IELE is the crown jewel of our research over the past decade,' he says. 'It’s the maximum you can hope for on a universal framework.'

Thành tích này sẽ cung cấp cho các nhà phát triển và doanh nghiệp một động lực khác để di cư từ Ethereum và tham gia vào blockchain Cardano.
Sự cởi mở, bao gồm và khả năng tương tác là những nền tảng mà Cardano được xây dựng.
Triết lý của chúng tôi là - và luôn luôn - để chào đón các nhà phát triển từ tất cả các nền tảng, để đảm bảo sự phát triển ổn định của Cardano.
Rosu có kế hoạch táo bạo.
"IELE là viên ngọc quý của nghiên cứu của chúng tôi trong thập kỷ qua", ông nói.
'Đó là mức tối đa mà bạn có thể hy vọng trên một khung phổ quát.'

## **Final thoughts**

## ** Suy nghĩ cuối cùng **

IOHK’s partnership with RV demonstrates a commitment to innovation, and to opening Cardano to as wide a development community as possible. The KEVM/IELE implementation will expand Cardano’s reach and interoperability by creating novel avenues of cooperation that will lead to the exploration of new ideas, concepts, and technological developments in the context of a ‘correct by construction’ environment. 

Quan hệ đối tác của IOHK với RV thể hiện cam kết đổi mới và mở Cardano cho một cộng đồng phát triển rộng nhất có thể.
Việc triển khai KEVM/IELE sẽ mở rộng phạm vi tiếp cận và khả năng tương tác của Cardano bằng cách tạo ra những con đường hợp tác mới lạ sẽ dẫn đến việc khám phá các ý tưởng, khái niệm và phát triển công nghệ mới trong bối cảnh môi trường xây dựng chính xác.

*You can read more from Alex at Cardano community site [Adapulse](https://adapulse.io/).*

*Bạn có thể đọc thêm từ trang web cộng đồng Alex tại Cardano [Adapulse] (https://adapulse.io/).**

