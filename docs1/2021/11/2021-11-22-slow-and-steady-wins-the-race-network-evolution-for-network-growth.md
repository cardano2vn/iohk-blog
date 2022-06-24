# Slow and steady wins the race: network evolution for network growth
### **After a successful start to Cardano’s smart contract era, we’ll soon make the first in a program of network adjustments to support future growth**
![](img/2021-11-22-slow-and-steady-wins-the-race-network-evolution-for-network-growth.002.png) 22 November 2021![](img/2021-11-22-slow-and-steady-wins-the-race-network-evolution-for-network-growth.002.png)[ John Woods](tmp//en/blog/authors/john-woods/page-1/)![](img/2021-11-22-slow-and-steady-wins-the-race-network-evolution-for-network-growth.003.png) 8 mins read

![John Woods](img/2021-11-22-slow-and-steady-wins-the-race-network-evolution-for-network-growth.004.png)[](tmp//en/blog/authors/john-woods/page-1/)
### [**John Woods**](tmp//en/blog/authors/john-woods/page-1/)
Director of Cardano Architecture

Engineering

- ![](img/2021-11-22-slow-and-steady-wins-the-race-network-evolution-for-network-growth.005.png)[](mailto:john.woods@iohk.io "Email")
- ![](img/2021-11-22-slow-and-steady-wins-the-race-network-evolution-for-network-growth.006.png)[](https://www.linkedin.com/in/johnalanwoods/ "LinkedIn")
- ![](img/2021-11-22-slow-and-steady-wins-the-race-network-evolution-for-network-growth.007.png)[](https://github.com/johnalanwoods "GitHub")

![Slow and steady wins the race: network evolution for network growth](img/2021-11-22-slow-and-steady-wins-the-race-network-evolution-for-network-growth.008.jpeg)

From its conception, Cardano has been architected as a platform to best balance the perennial trade-offs of security, scalability and decentralization. Therefore we have architected and built a solid and secure network layer, yet with the flexibility to grow and scale to support a global base of millions of users. 

Từ quan niệm của mình, Cardano đã được kiến trúc như một nền tảng để cân bằng tốt nhất sự đánh đổi lâu năm của bảo mật, khả năng mở rộng và phân cấp.
Do đó, chúng tôi đã kiến trúc và xây dựng một lớp mạng vững chắc và an toàn, nhưng với sự linh hoạt để phát triển và mở rộng để hỗ trợ một cơ sở toàn cầu gồm hàng triệu người dùng.

With a secure, highly decentralized proof of stake network now firmly established, and core smart contract capability deployed, we’re now heading into the Basho phase, focused on optimization, scaling and network growth. 

Với một bằng chứng an toàn, phi tập trung hóa mạng lưới cổ phần hiện đang được thiết lập vững chắc và khả năng hợp đồng thông minh cốt lõi được triển khai, chúng tôi hiện đang tiến vào giai đoạn Basho, tập trung vào tối ưu hóa, tăng trưởng và tăng trưởng mạng.

As a decentralized permissionless blockchain, Cardano is open to anyone who wants to use it or build on it. Recent hard forks (adding native tokens and smart contract capability) have brought many new users into the Cardano ecosystem, and we have seen rapid growth (and spikes) in transaction volumes and network traffic. 

Là một blockchain không được phép phi tập trung, Cardano mở cửa cho bất kỳ ai muốn sử dụng nó hoặc xây dựng trên nó.
Các dĩa khó gần đây (thêm mã thông báo gốc và khả năng hợp đồng thông minh) đã đưa nhiều người dùng mới vào hệ sinh thái Cardano và chúng tôi đã thấy tăng trưởng nhanh (và tăng đột biến) về khối lượng giao dịch và lưu lượng mạng.

As core components – including wallet connectors and the Plutus Application Backend (PAB) are finalized and integrated into mainnet, we anticipate significant growth in network activity. A constellation of projects [building on Cardano](https://github.com/input-output-hk/essential-cardano) will begin to launch, first on testnet then mainnet. These will only increase, with potentially hundreds of thousands of new users coming into Cardano over the coming months, from all sides of the blockchain spectrum. 

Là các thành phần cốt lõi - bao gồm các đầu nối ví và phụ trợ ứng dụng Plutus (PAB) được hoàn thiện và tích hợp vào mainnet, chúng tôi dự đoán sự tăng trưởng đáng kể trong hoạt động mạng.
Một chòm sao của các dự án [xây dựng trên Cardano] (https://github.com/input-oundput-hk/essential-cardano) sẽ bắt đầu khởi chạy, đầu tiên trên testnet sau đó là mainnet.
Những điều này sẽ chỉ tăng lên, với khả năng hàng trăm ngàn người dùng mới đến Cardano trong những tháng tới, từ tất cả các phía của phổ blockchain.

Inevitably, we can expect significant traffic around the launch of new decentralized applications (DApps), especially in the early days and weeks. To accommodate this ongoing growth, and ensure that Cardano maintains its resilience and robustness, we’re now starting to make a series of adjustments to network parameters. These parameter changes will provide ongoing improvements and enhancements to Cardano's usability and experience across its entire range of users. 

Không thể tránh khỏi, chúng ta có thể mong đợi lưu lượng truy cập đáng kể xung quanh việc ra mắt các ứng dụng phi tập trung mới (DAPP), đặc biệt là trong những ngày đầu và tuần.
Để phù hợp với sự tăng trưởng liên tục này và đảm bảo rằng Cardano duy trì khả năng phục hồi và mạnh mẽ của mình, chúng tôi hiện bắt đầu thực hiện một loạt các điều chỉnh cho các tham số mạng.
Những thay đổi tham số này sẽ cung cấp các cải tiến và cải tiến liên tục cho khả năng sử dụng và trải nghiệm của Cardano trên toàn bộ phạm vi người dùng.

### **Architected for growth**

### ** Kiến trúc sư cho tăng trưởng **

Ouroboros is designed to handle a large volume of data as well as transactions and scripts of different complexity and size. At present, and with current parameters, the Cardano network is utilizing on average only around 25% of its capacity. This is sub-optimal because in fact, the most efficient scenario is that Cardano runs at or close to 100% of its capacity (i.e., the network is ‘saturated’). 

Ouroboros được thiết kế để xử lý một khối lượng lớn dữ liệu cũng như các giao dịch và tập lệnh có độ phức tạp và kích thước khác nhau.
Hiện tại và với các tham số hiện tại, mạng Cardano đang sử dụng trung bình chỉ khoảng 25% công suất.
Điều này là tối ưu phụ bởi vì trên thực tế, kịch bản hiệu quả nhất là Cardano chạy ở mức hoặc gần 100% công suất của nó (tức là, mạng là ’bão hòa).

While many networking solutions would suffer under such conditions, both Ouroboros and the Cardano network stack have been designed to be fair and highly resilient, even under heavy saturation. 

Mặc dù nhiều giải pháp kết nối mạng sẽ bị ảnh hưởng trong các điều kiện như vậy, cả Ouroboros và ngăn xếp mạng Cardano đều được thiết kế để công bằng và có khả năng phục hồi cao, ngay cả dưới sự bão hòa nặng.

Efficient systems are designed to minimize congestion while enabling effective management when it does happen. You can read more in [this recent blog](https://iohk.io/en/blog/posts/2021/10/21/cardano-robust-resilient-and-flexible/), but in short, the network uses backpressure to manage the overall system load. So while some individual users during a large NFT drop may experience longer wait times for their transactions, this does not mean that the network is ‘struggling’. It actually means the network is performing as intended. We call it ‘graceful degradation’ and you can study this in greater depth in the network design paper.

Các hệ thống hiệu quả được thiết kế để giảm thiểu tắc nghẽn trong khi cho phép quản lý hiệu quả khi nó xảy ra.
Bạn có thể đọc thêm trong [blog gần đây] (https://iohk.io/en/blog/posts/2021/10/21/cardano-robust-resilient-and-plexible/), nhưng tóm lại, mạng sử dụng
Backpressure để quản lý tải hệ thống tổng thể.
Vì vậy, trong khi một số người dùng cá nhân trong thời gian giảm NFT lớn có thể trải nghiệm thời gian chờ đợi lâu hơn cho các giao dịch của họ, điều này không có nghĩa là mạng đang gặp khó khăn.
Nó thực sự có nghĩa là mạng đang hoạt động như dự định.
Chúng tôi gọi nó là ‘sự xuống cấp duyên dáng và bạn có thể nghiên cứu điều này ở độ sâu lớn hơn trong bài viết thiết kế mạng.

### **Adjusting parameters**

### ** Điều chỉnh tham số **

Aside from the original architectural design, and significant benchmarking across a range of simulated situations, it is only in the real world that we can truly gauge demand and the effectiveness of any changes. 

Ngoài thiết kế kiến trúc ban đầu và điểm chuẩn đáng kể trên một loạt các tình huống mô phỏng, chỉ trong thế giới thực, chúng ta thực sự có thể đánh giá nhu cầu và hiệu quả của bất kỳ thay đổi nào.

Following extensive benchmarking, and developer feedback, we’re now starting to make gradual adjustments and have today submitted two initial changes.These changes are planned to take effect on the testnet on Thursday 25th November. Once tested, we anticipate subsequently applying these to the mainnet, taking effect on epoch 306, on Wednesday December 1, 2021 at 21:45:00 UTC.

Theo điểm chuẩn rộng rãi và phản hồi của nhà phát triển, chúng tôi hiện bắt đầu thực hiện các điều chỉnh dần dần và hôm nay đã gửi hai thay đổi ban đầu. Những thay đổi này được lên kế hoạch để có hiệu lực trên Testnet vào thứ Năm ngày 25 tháng 11.
Sau khi được thử nghiệm, chúng tôi dự đoán sau đó áp dụng những thứ này cho Mainnet, có hiệu lực trên Epoch 306, vào thứ Tư ngày 1 tháng 12 năm 2021 lúc 21:45:00 UTC.

So what are we adjusting?

Vậy chúng ta đang điều chỉnh cái gì?

**We’re increasing block size by 8KB to 72KB (12.5% increase)**

** Chúng tôi tăng kích thước khối lên 8kB lên 72kb (tăng 12,5%) **

There are now well over 2 million Cardano wallets in use and traffic has grown by over 20 times in a year (from less than 10,000 transactions per day in November 2020 to over 200,000 transactions per day. Because of the anticipated rise in traffic as developers roll out new DApps, the block size is quickly becoming a key consideration. Larger block sizes mean that more transactions can fit into a block, thus providing greater capacity for users. Being able to fit 12.5% more transactions into a block is significant, as it means that we’re processing more transactions per second or we argue – [a more useful metric](https://www.youtube.com/watch?v=gpSnyCn2s9U) – greater data throughput.

Hiện tại có hơn 2 triệu ví Cardano được sử dụng và lưu lượng truy cập đã tăng hơn 20 lần trong một năm (từ dưới 10.000 giao dịch mỗi ngày vào tháng 11 năm 2020 lên hơn 200.000 giao dịch mỗi ngày.
Ra các DAPP mới, kích thước khối đang nhanh chóng trở thành một cân nhắc quan trọng. Kích thước khối lớn hơn có nghĩa là nhiều giao dịch có thể phù hợp với một khối, do đó cung cấp công suất lớn hơn cho người dùng. Có thể phù hợp với 12,5% giao dịch vào một khối là rất đáng kể, vì nó
có nghĩa là chúng tôi đang xử lý nhiều giao dịch hơn mỗi giây hoặc chúng tôi tranh luận - [một số liệu hữu ích hơn] (https://www.youtube.com/watch?v=GPSNYCN2S9U) - Thông lượng dữ liệu lớn hơn.

We are taking a steady, methodical approach to changes in Cardano's parameterization. A 12.5% increase is sizable, but not too big. It leaves room for further expansion, and allows stake pool operators (SPOs) to adjust to the increased demands. We will take a 'slow and steady' approach to further block size changes so that we make the underlying network capacity available to end users, while ensuring that we can continue to operate successfully as a globally decentralized blockchain. The current generation of Ouroboros (named Praos) has specific requirements which must be satisfied in order to ensure its security goals are met, one of the most important parameters is block propagation time. Block propagation time is a measure of how long it takes for a freshly minted block to be propagated across nodes on the network representing 95% of the staked ada. For Praos to stay secure the network must propagate new blocks within 5 seconds. 

Chúng tôi đang thực hiện một cách tiếp cận ổn định, có phương pháp để thay đổi tham số hóa của Cardano.
Tăng 12,5% là khá lớn, nhưng không quá lớn.
Nó để lại chỗ cho việc mở rộng hơn nữa và cho phép các nhà khai thác nhóm cổ phần (SPO) điều chỉnh theo nhu cầu gia tăng.
Chúng tôi sẽ thực hiện một cách tiếp cận 'chậm và ổn định' để thay đổi kích thước khối tiếp theo để chúng tôi cung cấp dung lượng mạng cơ bản có sẵn cho người dùng cuối, đồng thời đảm bảo rằng chúng tôi có thể tiếp tục hoạt động thành công như một blockchain phi tập trung toàn cầu.
Thế hệ hiện tại của OuroBoros (có tên PRAOS) có các yêu cầu cụ thể phải được thỏa mãn để đảm bảo các mục tiêu bảo mật của nó được đáp ứng, một trong những thông số quan trọng nhất là thời gian lan truyền khối.
Thời gian lan truyền khối là thước đo mất bao lâu để một khối mới được đúc để truyền qua các nút trên mạng chiếm 95% ADA bị đặt.
Để Praos giữ an toàn, mạng phải lan truyền các khối mới trong vòng 5 giây.

We can consider this 5s limit a ‘budget’ we can ‘spend’ on things like increasing the block size. Changes such as increased block size will naturally increase the time needed to propagate blocks, so we must monitor carefully to ensure changes we make to increase performance don’t affect the security of the network. In future iterations of Ouroboros this budget will be increased. Meanwhile our focus will be on maintaining security while flexing the network to growing demand. 

Chúng ta có thể xem xét điều này 5S giới hạn một ngân sách, chúng ta có thể chi tiêu cho những thứ như tăng kích thước khối.
Những thay đổi như tăng kích thước khối sẽ tự nhiên tăng thời gian cần thiết để truyền các khối, vì vậy chúng tôi phải theo dõi cẩn thận để đảm bảo những thay đổi chúng tôi thực hiện để tăng hiệu suất don don ảnh hưởng đến bảo mật của mạng.
Trong các lần lặp trong tương lai của ouroboros, ngân sách này sẽ được tăng lên.
Trong khi đó, trọng tâm của chúng tôi sẽ là duy trì bảo mật trong khi uốn cong mạng theo nhu cầu ngày càng tăng.

**We’re also increasing of Plutus script memory units per transaction to 11.25 million (again, 12.5% increase)**

** Chúng tôi cũng tăng các đơn vị bộ nhớ script Plutus cho mỗi giao dịch lên 11,25 triệu (một lần nữa, tăng 12,5%) **

This is a powerful change and one that we know DApp developers will very much appreciate. An increase in Plutus memory limits means that they can develop more sophisticated Plutus scripts, or that existing scripts will be able to process more data items, increase concurrency, or otherwise expand their capabilities. This will be the first of a series of changes to the memory unit settings that will greatly enhance the real-world capabilities of Plutus scripts. As with block sizes, we will roll out the changes gradually, but steadily, so that the network and SPOs adjust to the increased demand.

Đây là một thay đổi mạnh mẽ và một thay đổi mà chúng tôi biết các nhà phát triển DAPP sẽ đánh giá rất cao.
Sự gia tăng giới hạn bộ nhớ Plutus có nghĩa là chúng có thể phát triển các tập lệnh Plutus tinh vi hơn hoặc các tập lệnh hiện tại sẽ có thể xử lý nhiều mục dữ liệu hơn, tăng sự đồng thời hoặc mở rộng khả năng của chúng.
Đây sẽ là lần đầu tiên trong một loạt các thay đổi đối với cài đặt đơn vị bộ nhớ sẽ tăng cường đáng kể các khả năng trong thế giới thực của các tập lệnh Plutus.
Cũng như kích thước khối, chúng tôi sẽ đưa ra các thay đổi dần dần, nhưng đều đặn, để mạng và Spos điều chỉnh theo nhu cầu gia tăng.

The changes described below (block size increase and Increase of Plutus script memory units per transaction) were requested by many app developers, for example. Both these changes go hand-in-hand. It’s not just about creating more complex scripts. It’s also about putting *more* data through.

Những thay đổi được mô tả dưới đây (tăng kích thước khối và tăng các đơn vị bộ nhớ tập lệnh Plutus cho mỗi giao dịch) đã được yêu cầu bởi nhiều nhà phát triển ứng dụng, ví dụ.
Cả hai thay đổi này đều đi đôi với nhau.
Nó không chỉ là về việc tạo ra các kịch bản phức tạp hơn.
Nó cũng về việc đặt dữ liệu * thêm * thông qua.

### **Steady and sure**

### ** ổn định và chắc chắn **

As the Cardano platform evolves, every change will be carefully considered and once actioned, subsequently monitored to gauge its impact on performance. All changes will be based on empirical data drawn from the network and based on real, sustained user demand. Critically, it is important not to make decisions with a long-tail impact around short-term surges in network usage. We won't make changes prematurely or make them at a pace that could potentially compromise Cardano's longer-term security, for example. 

Khi nền tảng Cardano phát triển, mọi thay đổi sẽ được xem xét cẩn thận và sau khi được hành động, sau đó được theo dõi để đánh giá tác động của nó đối với hiệu suất.
Tất cả các thay đổi sẽ dựa trên dữ liệu thực nghiệm được rút ra từ mạng và dựa trên nhu cầu người dùng thực tế, duy trì.
Quan trọng, điều quan trọng là không đưa ra quyết định với tác động đuôi dài xung quanh sự gia tăng ngắn hạn trong việc sử dụng mạng.
Chúng tôi sẽ không thực hiện các thay đổi sớm hoặc thực hiện chúng với tốc độ có khả năng thỏa hiệp bảo mật dài hạn của Cardano chẳng hạn.

Cardano development is grounded in both fundamental and ongoing research. Further network enhancements in the mid-longer term will collectively deliver substantial capacity improvements, as well as tuning the network to deliver the best overall experience. 

Phát triển Cardano có căn cứ trong cả nghiên cứu cơ bản và liên tục.
Các cải tiến mạng hơn nữa trong thuật ngữ dài hơn sẽ mang lại những cải tiến năng lực đáng kể, cũng như điều chỉnh mạng để mang lại trải nghiệm tổng thể tốt nhất.

I’ll be joining the November Cardano360 to share further thoughts on this. But in short, this is about building new and capable blockchain infrastructure, built on advanced and fundamentally decentralized technologies. Initially, we will focus on a number of performance improvements that will enable us to exploit the limits of the Ouroboros Praos protocol. We will then focus on optimizing the size of Plutus scripts and the underlying performance of the Plutus interpreter and Cardano node implementations. This will allow us to process more useful work within the same protocol parameters. Related to this will be the use of compression techniques, to reduce the size of scripts and transactions, meaning that more transactions can be carried within the same sized block. All of this (and more) will improve layer 1 performance and capacity. Looking ahead, Hydra will then introduce a layer 2 solution, providing hugely increased scalability by allowing users to provision multiple chains that reuse the same ledger representation. 

Tôi sẽ tham gia Cardano360 tháng 11 để chia sẻ thêm những suy nghĩ về điều này. Nhưng tóm lại, đây là về việc xây dựng cơ sở hạ tầng blockchain mới và có khả năng, được xây dựng trên các công nghệ tiên tiến và phi tập trung về cơ bản. Ban đầu, chúng tôi sẽ tập trung vào một số cải tiến hiệu suất cho phép chúng tôi khai thác các giới hạn của giao thức Ouroboros PRAOS. Sau đó, chúng tôi sẽ tập trung vào việc tối ưu hóa kích thước của các tập lệnh Plutus và hiệu suất cơ bản của trình thông dịch Plutus và triển khai nút Cardano. Điều này sẽ cho phép chúng tôi xử lý công việc hữu ích hơn trong cùng một tham số giao thức. Liên quan đến điều này sẽ là việc sử dụng các kỹ thuật nén, để giảm quy mô của các tập lệnh và giao dịch, có nghĩa là nhiều giao dịch có thể được thực hiện trong cùng một khối có kích thước. Tất cả điều này (và hơn thế nữa) sẽ cải thiện hiệu suất và công suất lớp 1. Nhìn về phía trước, Hydra sau đó sẽ giới thiệu một giải pháp Lớp 2, cung cấp khả năng mở rộng tăng mạnh bằng cách cho phép người dùng cung cấp nhiều chuỗi sử dụng lại cùng một biểu diễn sổ cái.

### **In conclusion**

### **Tóm lại là**

Cardano is, in a manner of speaking, a living entity that grows and adapts with every evolutionary step. It may sound like a contradiction in terms, yet while its foundations are formed from rock-solid fundamental research, flexibility (to change even entire protocol changes via the hard fork combinator (HFC) has been designed in from the beginning. 

Cardano, theo cách nói, một thực thể sống phát triển và thích nghi với mọi bước tiến hóa.
Nghe có vẻ như là một mâu thuẫn về mặt, trong khi các nền tảng của nó được hình thành từ nghiên cứu cơ bản rắn, tính linh hoạt (để thay đổi ngay cả toàn bộ thay đổi giao thức thông qua tổ hợp Fork Fork (HFC) đã được thiết kế ngay từ đầu.

Parameterization changes are part of this transformative process. While inevitably there will be folks who want to move faster, our focus will remain on steady, secure evolution as Cardano grows in reach and adoption. 

Thay đổi tham số hóa là một phần của quá trình biến đổi này.
Mặc dù chắc chắn sẽ có những người muốn di chuyển nhanh hơn, nhưng sự tập trung của chúng tôi sẽ duy trì sự tiến hóa ổn định, an toàn khi Cardano phát triển trong tầm với và nhận con nuôi.

*Thanks to Duncan Coutts, Kevin Hammond, and Fernando Sanchez for their contributions to this article.*

*Cảm ơn Duncan Coutts, Kevin Hammond và Fernando Sanchez vì những đóng góp của họ cho bài viết này.*

