# Bringing Glow to Cardano
### **We just spun up a devnet to support Glow, the very latest language Cardano will support. We talked to its creator about building a DSL for DApp development.**
![](img/2021-02-26-bringing-glow-to-cardano.002.png) 26 February 2021![](img/2021-02-26-bringing-glow-to-cardano.002.png)[ Eric Czuleger](tmp//en/blog/authors/eric-czuleger/page-1/)![](img/2021-02-26-bringing-glow-to-cardano.003.png) 7 mins read

![Eric Czuleger](img/2021-02-26-bringing-glow-to-cardano.004.png)[](tmp//en/blog/authors/eric-czuleger/page-1/)
### [**Eric Czuleger**](tmp//en/blog/authors/eric-czuleger/page-1/)
Senior Content Editor

Marketing & Communications

- ![](img/2021-02-26-bringing-glow-to-cardano.005.png)[](mailto:eric.czuleger@iohk.io "Email")
- ![](img/2021-02-26-bringing-glow-to-cardano.006.png)[](https://www.linkedin.com/in/eric-czuleger-6b67a395/ "LinkedIn")
- ![](img/2021-02-26-bringing-glow-to-cardano.007.png)[](https://twitter.com/eczuleger "Twitter")

![Bringing Glow to Cardano](img/2021-02-26-bringing-glow-to-cardano.008.jpeg)

*At the end of 2020, we announced our devnets plan to support the longer-term strategic goal of opening up Cardano to multiple development languages â€“ as outlined in the â€˜â€˜[Island, Ocean, Pond](https://youtu.be/k8a6tX53YPs)â€™ video. This week, building on the [Ethereum Virtual Machine](https://developers.cardano.org/en/virtual-machines/welcome/), weâ€™re rolling out a new [development environment](https://developers.cardano.org/en/programming-languages/glow/overview/) to support the Glow language.*

*Vào cuối năm 2020, chúng tôi đã công bố kế hoạch DevNets của chúng tôi để hỗ trợ mục tiêu chiến lược dài hạn là mở Cardano cho nhiều ngôn ngữ phát triển-như được nêu trong "
: //youtu.be/k8a6tx53yps) â € ™ Video.
Tuần này, xây dựng trên [máy ảo Ethereum] (https://developers.cardano.org/en/virtual-machines/welcome/), chúng tôi sẽ tung ra một [môi trường phát triển] mới (https: //
.cardano.org/en/lập trình-ngôn ngữ/phát sáng/tổng quan/) để hỗ trợ ngôn ngữ phát sáng.*

*FranÃ§ois-RenÃ© Rideau of Mutual Knowledge Systems is the creator of Glow, a DSL that will allow anyone to write verifiable DApps from a single spec and deploy it on our EVM network. We caught up with Rideau (also known as Fare) to hear more about his vision for Glow and the Cardano journey so far. The following is a distillation of his thoughts from our previous interviews.*

*FranÃ §ois-RenÃ © Rideau of Mutual Kiến thức là người tạo ra Glow, một DSL sẽ cho phép bất cứ ai viết các DAPP có thể kiểm chứng từ một thông số kỹ thuật và triển khai nó trên mạng EVM của chúng tôi.
Chúng tôi đã bắt kịp Rideau (còn được gọi là giá vé) để nghe thêm về tầm nhìn của anh ấy về Glow và hành trình Cardano cho đến nay.
Sau đây là việc chưng cất suy nghĩ của anh ấy từ các cuộc phỏng vấn trước đây của chúng tôi.*

**We first introduced the community to GLOW and MuKn at the end of [last year](https://youtu.be/lj9SlvOIBgU?t=2902) when we announced our devnets approach â€“Â  but maybe you can remind us how you began working with IOHK?**

** Đầu tiên chúng tôi giới thiệu cộng đồng về Glow và Mukn vào cuối năm ngoái] (https://youtu.be/lj9slvoibgu?t=2902) Khi chúng tôi công bố cách tiếp cận của chúng tôi
Làm thế nào bạn bắt đầu làm việc với iohk? **

I started as a researcher in formal methods for programming languages and distributed systems. But I wanted to build systems actually used by many, so I moved into the industry where I notably worked on proving the correctness of a centralized payment protocol and creating an airline reservation system. After a few years at Google and Bridgewater, I decided life wasnâ€™t worth working under dysfunctional hierarchies, so I started my own cryptocurrency companies. Charles invited me to speak at the IOHK Summit 2019, and I realized how much I like the Cardano community: we have a similar focus on building robust software for the long term. That is why I wanted to port my domain specific language Glow to Cardano.

Tôi bắt đầu như một nhà nghiên cứu về các phương pháp chính thức cho các ngôn ngữ lập trình và hệ thống phân tán.
Nhưng tôi muốn xây dựng các hệ thống thực sự được nhiều người sử dụng, vì vậy tôi đã chuyển sang ngành công nghiệp nơi tôi đáng chú ý là chứng minh tính chính xác của một giao thức thanh toán tập trung và tạo ra một hệ thống đặt phòng hàng không.
Sau một vài năm tại Google và Bridgewater, tôi quyết định cuộc sống không đáng để làm việc theo hệ thống phân cấp rối loạn chức năng, vì vậy tôi đã bắt đầu các công ty tiền điện tử của riêng mình.
Charles đã mời tôi phát biểu tại Hội nghị thượng đỉnh IOHK 2019 và tôi nhận ra rằng tôi thích cộng đồng Cardano: chúng tôi tập trung tương tự vào việc xây dựng phần mềm mạnh mẽ trong thời gian dài.
Đó là lý do tại sao tôi muốn chuyển phát sáng ngôn ngữ cụ thể của mình cho Cardano.

**Tell us a bit why you started your company Mutual Knowledge Systems, or as you call it MuKn (Moon)?**

** Hãy cho chúng tôi biết một chút lý do tại sao bạn bắt đầu các hệ thống kiến thức lẫn nhau của công ty, hoặc như bạn gọi nó là mukn (mặt trăng)? **

Over three years ago, I was reviewing whitepapers. Most papers (about Â¾) had interesting techniques but made no economic sense. Most of the rest (about â…•) made economic sense but had no technical content. Only the top few (about 5%) actually made sense both technically and economically. At some point, I realized I could do better, so I designed a scaling solution using lessons learned from working on Tezos. Arthur Breitman challenged me to use smart contracts instead of trying to modify his protocol. 

Hơn ba năm trước, tôi đã xem xét lại Whitepapers.
Hầu hết các bài báo (về Âmm) đều có kỹ thuật thú vị nhưng không có ý nghĩa kinh tế.
Hầu hết các phần còn lại (về ÂTHER •) đều có ý nghĩa kinh tế nhưng không có nội dung kỹ thuật.
Chỉ có một số ít (khoảng 5%) thực sự có ý nghĩa cả về mặt kỹ thuật và kinh tế.
Tại một số điểm, tôi nhận ra rằng tôi có thể làm tốt hơn, vì vậy tôi đã thiết kế một giải pháp mở rộng bằng cách sử dụng các bài học kinh nghiệm từ làm việc trên Tezos.
Arthur Breitman đã thách thức tôi sử dụng hợp đồng thông minh thay vì cố gắng sửa đổi giao thức của mình.

While trying to prove his challenge absurd, I instead found that he was right and I was wrongâ€”and I finally understood why and how to use smart contracts. I started a company around the resulting scaling solution, raised money, pivoted into building the scaling solution after the language capable of generating it from specification, fought with and fired my then-partner, became my own CEO, started a new company, and, after much struggle, finally found the right founding team. Together, we built Mutual Knowledge Systems around this new programming language, Glowâ€”designed to be much better than existing languages to write decentralized applications.

Trong khi cố gắng chứng minh thách thức của anh ấy vô lý, thay vào đó tôi thấy rằng anh ấy đã đúng và tôi đã sai và cuối cùng tôi đã hiểu tại sao và làm thế nào để sử dụng các hợp đồng thông minh.
Tôi đã bắt đầu một công ty xung quanh giải pháp mở rộng kết quả, quyên góp tiền, xoay vòng để xây dựng giải pháp mở rộng sau khi ngôn ngữ có khả năng tạo ra nó từ đặc điểm kỹ thuật, chiến đấu và sa thải đối tác lúc đó của tôi, trở thành CEO của riêng tôi, bắt đầu một công ty mới, và,,, và
Sau nhiều cuộc đấu tranh, cuối cùng đã tìm thấy đội ngũ sáng lập đúng.
Cùng nhau, chúng tôi đã xây dựng các hệ thống kiến thức lẫn nhau xung quanh ngôn ngữ lập trình mới này, Glowâ € được thiết kế để tốt hơn nhiều so với các ngôn ngữ hiện có để viết các ứng dụng phi tập trung.

**When you say â€˜betterâ€™, what do you really mean?**

** Khi bạn nói - € ˜betterâ € ™, ý bạn là gì? **

Writing a DApp is the single hardest thing to do in the world. This is because you canâ€™t afford a mistake, or your users may lose significant funds. Furthermore, you are not confronting random situations, but active adversaries bent on attacking your code, who will contrive the very worst case scenarios to exploit for their profit. Yet, unlike the military, you canâ€™t hide your code or protect access to your networks: all the critical pieces are necessarily public. On top of that, extant programming tools are not designed for these constraints and even traditional formal methods lack essential concepts to express the issues at stake.

Viết DAPP là điều khó nhất để làm trên thế giới.
Điều này là do bạn không thể có lỗi hoặc người dùng của bạn có thể mất tiền đáng kể.
Hơn nữa, bạn không phải đối mặt với các tình huống ngẫu nhiên, nhưng các đối thủ tích cực đã cố gắng tấn công mã của bạn, người sẽ vượt qua các trường hợp xấu nhất để khai thác vì lợi nhuận của họ.
Tuy nhiên, không giống như quân đội, bạn không thể ẩn mã của mình hoặc bảo vệ quyền truy cập vào mạng của mình: tất cả các phần quan trọng nhất thiết phải công khai.
Trên hết, các công cụ lập trình còn tồn tại không được thiết kế cho các ràng buộc này và thậm chí các phương pháp chính thức truyền thống cũng thiếu các khái niệm thiết yếu để thể hiện các vấn đề đang bị đe dọa.

Thus, we decided to make new tools fit for the challenge. Our domain-specific language (DSL) drastically simplifies DApp development, by abstracting away all the common blockchain infrastructure, so you can focus on your problem domain (trading, derivatives, insurance, supply chain, etc.). Your DApps can be thousands of lines of code that your users can afford to audit, instead of millions of lines of code that require leaps of blind faith. And the programming model will enable developers, auditors and automated verification tools to reason at the level of abstraction of participants exchanging assets, rather than at that of packets of bytes shipped around the Internet.

Vì vậy, chúng tôi quyết định làm cho các công cụ mới phù hợp cho thử thách.
Ngôn ngữ cụ thể về miền (DSL) của chúng tôi đơn giản hóa đáng kể sự phát triển của DAPP, bằng cách trừu tượng hóa tất cả các cơ sở hạ tầng blockchain phổ biến, do đó bạn có thể tập trung vào miền vấn đề của mình (giao dịch, phái sinh, bảo hiểm, chuỗi cung ứng, v.v.).
DAPP của bạn có thể là hàng ngàn dòng mã mà người dùng của bạn có thể đủ khả năng kiểm toán, thay vì hàng triệu dòng mã đòi hỏi niềm tin mù quáng.
Và mô hình lập trình sẽ cho phép các nhà phát triển, kiểm toán viên và công cụ xác minh tự động lý luận ở mức độ trừu tượng của người tham gia trao đổi tài sản, thay vì ở các gói byte được vận chuyển trên internet.

**What is it about Cardano and its community that appeals?**

** Điều gì về Cardano và cộng đồng của nó kháng cáo? **

I started like everyone else, on Ethereum, because its ecosystem is already mature. However, the Ethereum community has this attitude of building as fast as possible experiments that are good enough for now, but lack conceptual integrity and wonâ€™t last; I see a lot of value in that approach and have tremendous respect for those who can thrive this wayâ€”for I cannot. When I met the Cardano community, I felt much more at home because we share a common attitude. We want to do things that are correct by construction and will keep working in the long term. We build concrete towers on the bedrock, not stick shacks on the sand. At times, this can be frustrating because things go slow, but I am happy with the attention to detail and quality in the development of Cardano. Is it perfect? No, itâ€™s not. But itâ€™s got great fundamentals.

Tôi bắt đầu như những người khác, trên Ethereum, bởi vì hệ sinh thái của nó đã trưởng thành.
Tuy nhiên, cộng đồng Ethereum có thái độ xây dựng nhanh nhất có thể là đủ tốt cho đến bây giờ, nhưng thiếu tính toàn vẹn về mặt khái niệm và sẽ không xảy ra cuối cùng;
Tôi thấy rất nhiều giá trị trong cách tiếp cận đó và có sự tôn trọng to lớn đối với những người có thể phát triển mạnh theo cách này vì tôi không thể.
Khi tôi gặp cộng đồng Cardano, tôi cảm thấy ở nhà nhiều hơn vì chúng tôi chia sẻ một thái độ chung.
Chúng tôi muốn làm những việc chính xác bằng cách xây dựng và sẽ tiếp tục làm việc lâu dài.
Chúng tôi xây dựng các tháp bê tông trên nền tảng, không dính lán trên cát.
Đôi khi, điều này có thể gây khó chịu vì mọi thứ diễn ra chậm chạp, nhưng tôi hài lòng với sự chú ý đến chi tiết và chất lượng trong sự phát triển của Cardano.
Nó có hoàn hảo không?
Không, không phải.
Nhưng đó là những nguyên tắc cơ bản tuyệt vời.

**Can you talk about how you hope Glow will change the DApp developer experience?**

** Bạn có thể nói về cách bạn hy vọng Glow sẽ thay đổi trải nghiệm của nhà phát triển DAPP không? **

Glow is portable. Today it works on Cardano and Ethereum but in the future it will work with any blockchain that is sufficiently advanced to support smart contracts. That means that you can write your DApp once and it will run on whichever platform has the users and the liquidity you seek. You donâ€™t have to make a guess about where liquidity will be in the future then sink heavy investments to develop on a single chain that you bet your house on.

Phát sáng là di động.
Ngày nay, nó hoạt động trên Cardano và Ethereum nhưng trong tương lai, nó sẽ hoạt động với bất kỳ blockchain nào đủ nâng cao để hỗ trợ các hợp đồng thông minh.
Điều đó có nghĩa là bạn có thể viết DAPP của mình một lần và nó sẽ chạy trên bất kỳ nền tảng nào có người dùng và thanh khoản bạn tìm kiếm.
Bạn không phải đoán xem thanh khoản sẽ ở đâu trong tương lai sau đó chìm các khoản đầu tư nặng nề để phát triển trên một chuỗi duy nhất mà bạn đặt cược ngôi nhà của mình.

With Glow, developers can run their DApps on all blockchains. Glow will commoditize blockchains. Blockchains will then compete on technical and economic merits, not on user lock-in and inertia. And the value brought to users will increase.

Với Glow, các nhà phát triển có thể chạy DAPP của họ trên tất cả các blockchain.
Glow sẽ hàng hóa blockchains.
Blockchains sau đó sẽ cạnh tranh về giá trị kỹ thuật và kinh tế, không phải trên khóa người dùng và quán tính.
Và giá trị mang lại cho người dùng sẽ tăng lên.

**What can the community expect from Glow?**

** Cộng đồng có thể mong đợi gì từ Glow? **

We have launched this early version of Glow on the Cardano EVM Devnet with a command-line interface. In many ways, it is not yet ready for use by end-users, but it can already demonstrate simple applications. Users can also see how they may write a 6 line application in Glow that would require hundreds of lines in a combination of Solidity and JavaScript. We have a roadmap over the next few months to add a lot of features: from ERC20 tokens (and, on Cardano, native tokens), to generalized state channels, to a web interface, to a more robust runtime, etc. Eventually, we want to become the development environment for all blockchain projects. And Glow is of course an open source software open to the community.

Chúng tôi đã ra mắt phiên bản đầu tiên của Glow trên Cardano EVM DevNet với giao diện dòng lệnh.
Theo nhiều cách, nó vẫn chưa sẵn sàng để sử dụng bởi người dùng cuối, nhưng nó đã có thể chứng minh các ứng dụng đơn giản.
Người dùng cũng có thể thấy cách họ có thể viết một ứng dụng 6 dòng trong Glow sẽ yêu cầu hàng trăm dòng kết hợp giữa độ rắn và JavaScript.
Chúng tôi có một lộ trình trong vài tháng tới để thêm nhiều tính năng: từ các mã thông báo ERC20 (và, trên Cardano, mã thông báo gốc), đến các kênh nhà nước tổng quát, đến giao diện web, đến thời gian chạy mạnh mẽ hơn, v.v.
muốn trở thành môi trường phát triển cho tất cả các dự án blockchain.
Và Glow tất nhiên là một phần mềm nguồn mở mở cho cộng đồng.

**Weâ€™re rolling out the integration with Glow with our EVM and devnet program, so what are some of the benefits of this?**

** Chúng tôi sẽ đưa ra sự tích hợp với Glow với chương trình EVM và DevNet của chúng tôi, vậy một số lợi ích của việc này là gì? **

The Cardano EVM side-chain will enable arbitrary contracts to run on Cardano that use the mature EVM platform, without waiting for Plutus to deliver its promise, to achieve feature-parity, to be considered stable, etc. And Glow can run on this EVM side-chain and provide the simplicity, safety and portability in DApp development that were not available before.

Chuỗi bên Cardano EVM sẽ cho phép các hợp đồng tùy ý chạy trên Cardano sử dụng nền tảng EVM trưởng thành, mà không cần chờ Sao Diêm Vương để thực hiện lời hứa của mình, để đạt được tính năng tương tự, được coi là ổn định, v.v. và phát sáng có thể chạy trên EVM này
Chuỗi phụ và cung cấp tính đơn giản, an toàn và tính di động trong phát triển DAPP mà không có sẵn trước đó.

**What is the rollout process like and how can our community get involved if they want to?**

** Quá trình triển khai như thế nào và làm thế nào cộng đồng của chúng ta có thể tham gia nếu họ muốn? **

Glow is still in development. There are some things that it can do already and some it canâ€™t do yet. We invite DApp developers to join the Glow community and use the language for what it can already do, and otherwise help us build the blockchain development environment of the future. You can build the missing features you need yourself, or contract MuKn to build them for you. Even if you canâ€™t code and have no budget, you can help write the documentation, or even just tell us where it isnâ€™t clear yet, or what features you need most so we know what to prioritize. Together, we can build great DApps that you just couldnâ€™t have achieved safely and within budget with previous tools.

Glow vẫn đang được phát triển.
Có một số điều mà nó có thể làm và một số nó chưa thể làm được.
Chúng tôi mời các nhà phát triển DAPP tham gia cộng đồng Glow và sử dụng ngôn ngữ cho những gì nó đã có thể làm, và nếu không thì giúp chúng tôi xây dựng môi trường phát triển blockchain của tương lai.
Bạn có thể xây dựng các tính năng còn thiếu mà bạn cần hoặc ký hợp đồng MUKN để xây dựng chúng cho bạn.
Ngay cả khi bạn không thể có mã và không có ngân sách, bạn có thể giúp viết tài liệu hoặc thậm chí chỉ cho chúng tôi biết rõ ràng ở đâu, hoặc những tính năng nào bạn cần nhất để chúng tôi biết những gì sẽ ưu tiên.
Cùng nhau, chúng tôi có thể xây dựng các DAPP tuyệt vời mà bạn không thể đạt được một cách an toàn và trong ngân sách với các công cụ trước đó.

*If youâ€™re a developer, we encourage you to get involved with [Mutual Knowledge Systems and Glow](https://mukn.io/). See our full conversation with FranÃ§ois-RenÃ© Rideau and a demonstration of Glow during [Cardano360.*](https://youtu.be/YXaK0cvgoFQ?t=4367)*

*Nếu bạn là nhà phát triển, chúng tôi khuyến khích bạn tham gia vào [hệ thống kiến thức lẫn nhau và phát sáng] (https://mukn.io/).
Xem cuộc trò chuyện đầy đủ của chúng tôi với FranÃ §ois-RenÃ © Rideau và một cuộc biểu tình phát sáng trong [Cardano360.*] (Https://youtu.be/yxak0cvgofq?t=4367)**

