# Xác minh thời gian chạy và IELE - từ khả năng tương tác đến tính phổ biến

### **KEVM và IELE sẽ mang lại mức độ bảo mật, khả năng mở rộng và khả năng lập trình vô song cho Cardano**

![](img/2021-05-10-runtime-verification-iele-from-interoperability-to-universality.002.png) 10 tháng 5 năm 2021 ![](img/2021-05-10-runtime-verification-iele-from-interoperability-to-universality.002.png) [Alex Hamilton](tmp//en/blog/authors/alex-hamilton/page-1/) ![](img/2021-05-10-runtime-verification-iele-from-interoperability-to-universality.003.png) 4 phút đọc

![Alex Hamilton](img/2021-05-10-runtime-verification-iele-from-interoperability-to-universality.004.png)[](tmp//en/blog/authors/alex-hamilton/page-1/)

### [**Alex Hamilton**](tmp//en/blog/authors/alex-hamilton/page-1/)

Writer

Tác giả khách mời

- ![](img/2021-05-10-runtime-verification-iele-from-interoperability-to-universality.005.png)[](https://www.linkedin.com/in/alex-hamilton-55b4b6108/ "LinkedIn")
- ![](img/2021-05-10-runtime-verification-iele-from-interoperability-to-universality.006.png)[](https://twitter.com/Immortalxplorer "Twitter")

![ Runtime Verification & IELE – from interoperability to universality](img/2021-05-10-runtime-verification-iele-from-interoperability-to-universality.007.jpeg)

[Giáo sư Grigore Rosu](https://en.wikipedia.org/wiki/Grigore_Rosu) , Chủ tịch kiêm Giám đốc điều hành của công ty khởi nghiệp Runtime Verification (RV) đã tham gia với chúng tôi trong [ấn bản tháng 3 của chương trình Cardano360](https://youtu.be/ULBLgPgxtN8?t=1563) để chia sẻ ý tưởng và thảo luận về sự hợp tác giữa RV và IOHK.

Mối quan hệ công việc của chúng tôi với Grigore và RV bắt đầu từ năm 2017 và Các chứng chỉ của Grigore thể hiện tất cả bằng bất kỳ ngôn ngữ nào). Anh ấy đã làm việc cho NASA, DARPA, Microsoft và đã giảng dạy tại Đại học Illinois Urbana-Champaign, có thể kể đến một vài thành tựu.

Grigore cũng được ghi nhận là người đã tạo ra [K Framework](https://runtimeverification.com/blog/k-framework-an-overview/) , được mô tả là 'phần mềm đơn giản là không thể thất bại.' Được phát triển trong hơn 15 năm, mục đích chính của khung là tăng cường bảo mật. Chúng ta sẽ đi vào chi tiết hơn về vấn đề này sau, nhưng trước tiên, là một bài học lịch sử ngắn.

When it comes to smart contracts, the Ethereum Virtual Machine (EVM) set many early standards, for example the creation of the ubiquitous ERC-20 smart contracts, written in Solidity. However, this system isn’t flawless. Smart contracts have known coding vulnerabilities that have caused security issues. 

## **IELE: Bảo mật, khả năng mở rộng và khả năng lập trình vô song**

Since late 2020, Cardano developers have had a bridge to the Solidity/Ethereum community via the K Ethereum Virtual Machine (KEVM), an implementation of the EVM specified in the K framework, which allows developers to use the formal verification tools that K produces to check a contract's correctness. 

IELE đưa mọi thứ tiến thêm một bước. Như đã được Rosu thảo luận trên chương trình Cardano360 vào tháng 3, IELE (được đặt tên theo một [sinh vật giống thần tiên trong thần thoại Romania](https://en.wikipedia.org/wiki/Iele) ) là một máy ảo thực thi các hợp đồng thông minh và cũng cung cấp một ngôn ngữ có thể đọc được cho các nhà phát triển blockchain. IELE được thiết kế với các phương pháp chính thức nhằm giải quyết các mối quan tâm về tính bảo mật và tính đúng đắn vốn có trong việc viết các hợp đồng thông minh Solidity nhắm mục tiêu Ethereum, giúp giảm bớt con đường dẫn đến mức độ bảo mật, khả năng mở rộng và khả năng lập trình cao hơn.

IELE giống như đại diện trung gian của trình biên dịch LLVM. Điều này cho phép thu hút sự phong phú của kiến thức có sẵn trong cộng đồng LLVM, đặc biệt, công việc đã đi vào viết tối ưu hóa trình biên dịch an toàn và hiệu quả vượt qua LLVM IR. Phần lớn nỗ lực dành cho trình biên dịch LLVM cũng có thể được chuyển sang trình tối ưu hóa IELE.

## **Về LLVM**

When IELE is implemented (Rosu indicated that an initial proof of concept would be available for testing around six months from now), the opportunity for development will be even wider. IELE operates more like a passport than a virtual machine, opening the doors – if not the floodgates – to a wealth of new and unique talent. Some developers may have once dismissed the idea of entering the blockchain space, as it would likely have meant learning an entirely new programming language. As a direct result of RV’s innovative approach, any developer wanting to get involved in smart contracts can write them in a language they are comfortable with, including Solidity. The resulting output would run successfully on any IELE-powered blockchain, irrespective of the source language.

## **Điều này có ý nghĩa gì đối với Cardano?**

Thành tựu này sẽ khuyến khích các nhà phát triển và doanh nghiệp di chuyển từ Ethereum và tham gia vào chuỗi khối Cardano. Tính cởi mở, toàn diện và khả năng tương tác là những nền tảng mà Cardano xây dựng nên. Triết lý của chúng tôi là luôn luôn chào đón các nhà phát triển từ mọi nền tảng, để đảm bảo sự phát triển ổn định của Cardano. Rosu có những kế hoạch táo bạo. Ông nói: “IELE là viên ngọc quý trong nghiên cứu của chúng tôi trong thập kỷ qua. 'Đó là điều lớn nhất mà bạn có thể hy vọng trên một khuôn khổ chung.'

## **Lời cuối**

Quan hệ đối tác của IOHK với RV thể hiện cam kết đổi mới và mở rộng Cardano tới một cộng đồng phát triển rộng rãi nhất có thể. Việc triển khai KEVM / IELE sẽ mở rộng phạm vi tiếp cận và khả năng tương tác của Cardano bằng cách tạo ra các con đường hợp tác mới dẫn đến việc khám phá các ý tưởng, khái niệm và phát triển công nghệ mới trong bối cảnh môi trường 'đúng theo xây dựng'.

*You can read more from Alex at Cardano community site [Adapulse](https://adapulse.io/).*
