# Optimizing Cardano
### **The path to network optimization lies in gradual step-by-step adjustments**
![](img/2021-11-10-optimizing-cardano.002.png) 10 November 2021![](img/2021-11-10-optimizing-cardano.002.png)[ Tim Harrison](tmp//en/blog/authors/tim-harrison/page-1/)![](img/2021-11-10-optimizing-cardano.003.png) 10 mins read

![Tim Harrison](img/2021-11-10-optimizing-cardano.004.png)[](tmp//en/blog/authors/tim-harrison/page-1/)
### [**Tim Harrison**](tmp//en/blog/authors/tim-harrison/page-1/)
VP of Community & Ecosystem

Communications

- ![](img/2021-11-10-optimizing-cardano.005.png)[](mailto:tim.harrison@iohk.io "Email")
- ![](img/2021-11-10-optimizing-cardano.006.png)[](https://uk.linkedin.com/in/timbharrison "LinkedIn")
- ![](img/2021-11-10-optimizing-cardano.007.png)[](https://twitter.com/timbharrison "Twitter")
- ![](img/2021-11-10-optimizing-cardano.008.png)[](https://github.com/timbharrison "GitHub")

![Optimizing Cardano ](img/2021-11-10-optimizing-cardano.009.jpeg)

As a proof-of-stake blockchain, Cardano is built to be highly secure and resilient to network failures. Driven by the Ouroboros consensus algorithm, built-in Haskell that uses formal methods, and peer-reviewed academic research, Cardano is designed to provide a rock-solid environment to process millions of transactions globally, in a decentralized and highly scalable manner. 

Là một blockchain bằng chứng, Cardano được xây dựng để rất an toàn và kiên cường cho các lỗi mạng.
Được thúc đẩy bởi thuật toán đồng thuận Ouroboros, Haskell tích hợp sử dụng các phương pháp chính thức và nghiên cứu học thuật được đánh giá ngang hàng, Cardano được thiết kế để cung cấp môi trường vững chắc để xử lý hàng triệu giao dịch trên toàn cầu, theo cách thức phi tập trung và có khả năng mở rộng cao.

In our [previous blog post](https://iohk.io/en/blog/posts/2021/10/21/cardano-robust-resilient-and-flexible/), we discussed network performance â€“ how the system works as a whole when processing, verifying, and signing transactions. Getting this right at the very earliest design stage is crucial if you want a system that is built for the long term. Yet, network capacity is a valuable resource, so for the most efficient performance metrics, it is essential that computation, memory, storage, and network resources are consumed effectively. 

Trong [bài đăng trên blog trước] của chúng tôi (https://iohk.io/en/blog/posts/2021/10/21/cardano-robust-resilient-and-pracyible/), chúng tôi đã thảo luận về hiệu suất mạng-Làm thế nào hệ thống
Hoạt động chung khi xử lý, xác minh và ký giao dịch.
Nhận được điều này ngay trong giai đoạn thiết kế sớm nhất là rất quan trọng nếu bạn muốn một hệ thống được xây dựng trong dài hạn.
Tuy nhiên, dung lượng mạng là một nguồn tài nguyên có giá trị, vì vậy đối với các số liệu hiệu suất hiệu quả nhất, điều cần thiết là tính toán, bộ nhớ, lưu trữ và tài nguyên mạng được tiêu thụ hiệu quả.

Cardano is built to be flexible. It is designed to maximize throughput while allowing for responsiveness to increasing demand. As the network grows, we are tuning protocol parameters to adjust to pricing fluctuations, extend scalability and throughput properties. So letâ€™s take a closer look at how we will be optimizing network performance over time.

Cardano được xây dựng để linh hoạt.
Nó được thiết kế để tối đa hóa thông lượng trong khi cho phép đáp ứng với nhu cầu tăng lên.
Khi mạng phát triển, chúng tôi đang điều chỉnh các tham số giao thức để điều chỉnh theo biến động định giá, mở rộng khả năng mở rộng và các thuộc tính thông lượng.
Vì vậy, hãy xem xét kỹ hơn về cách chúng ta sẽ tối ưu hóa hiệu suất mạng theo thời gian.

## **Defining congestion**

## ** Xác định tắc nghẽn **

Efficient systems â€“ from networks to roads â€“ are built to minimize congestion, while enabling effective management when it does happen. In blockchain terms, congestion implies that the network is oversaturated and experiences difficulties when processing large volumes of transactions and signing associated blocks. On average, Cardano blocks are approximately 25% utilized across a given epoch, which shows that generally, the network is *not* congested and thereâ€™s significant spare capacity to process an even larger number of transactions. 

Các hệ thống hiệu quả - từ các mạng đến các con đường - được xây dựng để giảm thiểu tắc nghẽn, đồng thời cho phép quản lý hiệu quả khi nó xảy ra.
Trong các điều khoản blockchain, tắc nghẽn ngụ ý rằng mạng bị quá bão hòa và gặp khó khăn khi xử lý khối lượng lớn các giao dịch và ký kết các khối liên quan.
Trung bình, các khối Cardano được sử dụng khoảng 25% trên một kỷ nguyên nhất định, cho thấy nói chung, mạng không * bị tắc nghẽn và có khả năng dự phòng đáng kể để xử lý số lượng giao dịch thậm chí còn lớn hơn.

Cardano is designed to be fair and highly resilient even under heavy saturation. Letâ€™s remind ourselves about the current parameter settings and look at future optimizations that are planned. Current performance metrics depend on the following measures:

Cardano được thiết kế để công bằng và có khả năng phục hồi cao ngay cả dưới sự bão hòa nặng.
Hãy nhắc nhở bản thân về các cài đặt tham số hiện tại và xem xét các tối ưu hóa trong tương lai được lên kế hoạch.
Các số liệu hiệu suất hiện tại phụ thuộc vào các biện pháp sau:

- **Throughput** â€” the volume of transferred data. The current block size is set to 64 KB. A single Plutus script transaction is currently limited to 16 KB, and simple transactions can commonly take up to around 300 bytes. These measures have been balanced to ensure good network utilization while minimizing transaction latencies. If increased significantly and at once, users will face increased delay in block adoption time. That is because throughput and timeliness are in tension with each other â€“ maximizing throughput implies better network performance, but this can come at the cost of increased delay when the system is heavily saturated.

- ** Thông lượng ** - khối lượng dữ liệu được chuyển.
Kích thước khối hiện tại được đặt thành 64 kb.
Một giao dịch Plutus Script duy nhất hiện được giới hạn ở mức 16 KB và các giao dịch đơn giản thường có thể mất tới khoảng 300 byte.
Các biện pháp này đã được cân bằng để đảm bảo sử dụng mạng tốt trong khi giảm thiểu độ trễ giao dịch.
Nếu tăng đáng kể và cùng một lúc, người dùng sẽ phải đối mặt với sự chậm trễ trong thời gian áp dụng khối.
Đó là bởi vì thông lượng và tính kịp thời đang căng thẳng với nhau - tối đa hóa thông lượng tối đa hóa hiệu suất mạng tốt hơn, nhưng điều này có thể đến với chi phí tăng độ trễ khi hệ thống bị bão hòa mạnh.

- **Timeliness** â€” i.e. the block adoption time. The total â€˜budgetâ€™ for block adoption is set to 5 seconds for a block to propagate across the network (95% of the stake) with a budget of approximately 50 milliseconds available for Plutus scripts. This is designed to allow the block to include both scripts and simple transactions without monopolization. 

- ** Tính kịp thời ** â €, tức là thời gian áp dụng khối.
Tổng số khả năng áp dụng khối được đặt thành 5 giây cho một khối để tuyên truyền trên mạng (95% cổ phần) với ngân sách khoảng 50 mili giây có sẵn cho các tập lệnh Plutus.
Điều này được thiết kế để cho phép khối bao gồm cả tập lệnh và giao dịch đơn giản mà không độc quyền.

Recently, users recorded an increased waiting time for transaction processing which has been caused by large NFT (non-fungible token) drops. The reason for this oversaturation lies in the fact that a high quantity of NFTs was released at once which caused the following:

Gần đây, người dùng đã ghi lại thời gian chờ đợi tăng lên để xử lý giao dịch được gây ra bởi các giọt NFT (mã thông báo không bị tăng) lớn).
Lý do cho sự quá bão hòa này nằm ở chỗ một lượng lớn NFT được phát hành cùng một lúc gây ra những điều sau đây:

- a large number of simultaneous NFT transactions

- Một số lượng lớn các giao dịch NFT đồng thời

- several users trying to purchase the same NFT and thus attempting to process transactions at the same time

- Một số người dùng cố gắng mua cùng một NFT và do đó cố gắng xử lý các giao dịch cùng một lúc

- simultaneous refund transactions to users who were unable to purchase the NFT

- Giao dịch hoàn trả đồng thời cho người dùng không thể mua NFT

This scenario created network scarcity for the NFT sale and therefore a huge demand on the service â€“ 43,000% of the supply. It is also worth noting that the â€˜congestionâ€™ period lasted for less than one hour. 

Kịch bản này đã tạo ra sự khan hiếm mạng cho việc bán NFT và do đó, một nhu cầu lớn đối với dịch vụ - 43.000% nguồn cung.
Điều đáng chú ý là thời kỳ "thời gian của" thời gian kéo dài chưa đầy một giờ.

This is a growing market and NFT creators are already starting to iterate their processes to minimize the impact of such drops on the user experience. It's still early and we are all learning fast. It should be noted that the process of minting NFTs is perfectly parallelizable, meaning there is no limit to this process. Once minted, NFTs storing the programmable swap code and assets required to transact are ready to interact with the market. 

Đây là một thị trường đang phát triển và người tạo NFT đã bắt đầu lặp lại các quy trình của họ để giảm thiểu tác động của những giọt như vậy đối với trải nghiệm người dùng.
Vẫn còn sớm và tất cả chúng ta đều học nhanh.
Cần lưu ý rằng quá trình khai thác NFT là hoàn toàn có thể song song, có nghĩa là không có giới hạn cho quá trình này.
Sau khi được đúc, NFTS lưu trữ mã hoán đổi và tài sản có thể lập trình cần thiết để giao dịch đã sẵn sàng để tương tác với thị trường.

But in the short to mid-term at least, this is a matter of building more efficient traffic systems rather than widening the roads. Some developers are already producing such systems specifically for NFT drops, which should reduce costs as well as short-term network loads.

Nhưng ít nhất là ngắn gọn đến giữa kỳ, đây là vấn đề xây dựng các hệ thống giao thông hiệu quả hơn thay vì mở rộng các con đường.
Một số nhà phát triển đã sản xuất các hệ thống như vậy dành riêng cho các giọt NFT, điều này sẽ làm giảm chi phí cũng như tải mạng ngắn hạn.

**Decentralized exchanges (DEXs)**

** Trao đổi phi tập trung (DEXS) **

Many early DApps being built on Cardano are DEXs or Decentralized Exchanges. And in some applications users tend to experience contention while placing their orders. Because the DApp design prerequisites that the whole state is kept within one UTXO (rather than spread across multiple UTXOs), there occurs a dependency of a future transaction on an output from a previous transaction. This has been widely referred to as the concurrency â€˜issueâ€™. However, trundling out that automobile analogy again, it is no more of an â€˜issueâ€™ than driving on the left is an â€˜issueâ€™ in the UK or Japan. It does require a learning curve but ultimately it is just a different way of doing things. And if a developer doesnâ€™t do it, yes, they will encounter problems! Nor is it inherently more complex â€“ just requires a different approach.

Nhiều DAPP ban đầu được xây dựng trên Cardano là DEXS hoặc trao đổi phi tập trung.
Và trong một số ứng dụng, người dùng có xu hướng trải nghiệm sự tranh chấp trong khi đặt hàng.
Bởi vì các điều kiện tiên quyết của thiết kế DAPP mà toàn bộ trạng thái được giữ trong một UTXO (thay vì trải rộng trên nhiều UTXO), nên xảy ra sự phụ thuộc của một giao dịch trong tương lai vào đầu ra từ một giao dịch trước đó.
Điều này đã được gọi là rộng rãi là sự đồng thời - vấn đề này.
Tuy nhiên, việc loại bỏ sự tương tự ô tô một lần nữa, nó không còn là một vấn đề nào nữa so với lái xe bên trái là một vấn đề "Điều kiện ở Anh hoặc Nhật Bản.
Nó đòi hỏi một đường cong học tập nhưng cuối cùng nó chỉ là một cách làm khác nhau.
Và nếu một nhà phát triển không làm điều đó, vâng, họ sẽ gặp phải vấn đề!
Nó cũng không phức tạp hơn - chỉ cần một cách tiếp cận khác.

Cardanoâ€™s EUTXO model is different from the account-based model. DApps built on Cardano should move away from the single-threaded state machine style and go down a level of abstraction to the EUTXO directly, constructing a solution that involves concurrent edges in the EUTXO graph. It is important to use different sets of UTXOs thereby enforcing parallelism which will improve the throughput of the system while keeping the performance of individual operations the same. Sure, this does require a shift in mindset to any developer used to Ethereumâ€™s approach. Yet, the UTXO-based model is more secure than the account-based model because keeping all the state in a single account is more vulnerable to attacks. If using parallelism techniques correctly, users will enjoy improved results in terms of throughput and scalability whereas off-chain solutions are better applicable to UTXO ledgers. For more details read the [concurrency blog post](https://iohk.io/en/blog/posts/2021/09/10/concurrency-and-all-that-cardano-smart-contracts-and-the-eutxo-model/) and [how to build a scalable Plutus DApp](https://plutus-apps.readthedocs.io/en/latest/plutus/howtos/writing-a-scalable-app.html). Weâ€™ll publish further content on this in due course to provide additional guidance on making the most of the model. 

Mô hình EUTXO của Cardano khác với mô hình dựa trên tài khoản. Các DAPP được xây dựng trên Cardano nên tránh xa kiểu máy trạng thái đơn luồng và trực tiếp đi xuống mức độ trừu tượng của EUTXO, xây dựng một giải pháp liên quan đến các cạnh đồng thời trong biểu đồ EUTXO. Điều quan trọng là sử dụng các bộ UTXO khác nhau do đó thực thi song song, điều này sẽ cải thiện thông lượng của hệ thống trong khi vẫn giữ hiệu suất của các hoạt động riêng lẻ. Chắc chắn, điều này đòi hỏi một sự thay đổi trong suy nghĩ cho bất kỳ nhà phát triển nào được sử dụng để tiếp cận của Ethereum. Tuy nhiên, mô hình dựa trên UTXO an toàn hơn mô hình dựa trên tài khoản vì giữ tất cả trạng thái trong một tài khoản dễ bị tấn công hơn. Nếu sử dụng các kỹ thuật song song một cách chính xác, người dùng sẽ tận hưởng kết quả được cải thiện về mặt thông lượng và khả năng mở rộng trong khi các giải pháp ngoài chuỗi được áp dụng tốt hơn cho các sổ cái UTXO. Để biết thêm chi tiết, hãy đọc [bài đăng trên blog đồng thời] (https://iohk.io/en/blog/posts/2021/09/10/concurrency-and-all-that-cardano-smart-contracts-and-the-eutxo -model/) và [Cách xây dựng một plutus dapp có thể mở rộng] (https://plutus-apps.readthedocs.io/en/latest/plutus/howtos/writing-a-scalable-app.html). Chúng tôi sẽ xuất bản nội dung tiếp theo về điều này trong khóa học do cung cấp hướng dẫn bổ sung về việc tận dụng tối đa mô hình.

## **The optimization roadmap**

## ** Lộ trình tối ưu hóa **

Our focus at launch was always to provide core capability and correctness, before optimizing. This has always been our stated goal. Weâ€™re continuing to monitor performance and benchmark adjustments. As the network grows and Cardano functions at a higher capacity, we will be adjusting the parameterization to keep up with network demand. These are gradual upgrades that will be implemented step-by-step over the next few months to ensure that changes meet the network requirements and do not compromise on different properties. 

Trọng tâm của chúng tôi khi ra mắt là luôn luôn cung cấp khả năng và tính chính xác cốt lõi, trước khi tối ưu hóa.
Đây luôn là mục tiêu đã nêu của chúng tôi.
Chúng tôi đang tiếp tục theo dõi hiệu suất và điều chỉnh điểm chuẩn.
Khi mạng phát triển và các chức năng Cardano ở công suất cao hơn, chúng tôi sẽ điều chỉnh tham số hóa để theo kịp nhu cầu mạng.
Đây là những nâng cấp dần dần sẽ được thực hiện từng bước trong vài tháng tới để đảm bảo rằng các thay đổi đáp ứng các yêu cầu mạng và không thỏa hiệp về các thuộc tính khác nhau.

We have carried out extensive analysis and started to implement node metrics that accurately measure the data diffusion time. Data diffusion is the process of distributing transactions and blocks across nodes that verify the blockchain. It is essential to provide nodes with the needed information so that the consensus algorithm can make its decisions.

Chúng tôi đã thực hiện phân tích sâu rộng và bắt đầu thực hiện các số liệu nút nhằm đo lường chính xác thời gian khuếch tán dữ liệu.
Khuếch tán dữ liệu là quá trình phân phối các giao dịch và khối trên các nút xác minh blockchain.
Điều cần thiết là cung cấp cho các nút thông tin cần thiết để thuật toán đồng thuận có thể đưa ra quyết định của mình.

Weâ€™ll likely be implementing an average waiting time from transaction submission to transaction adoption. Along with that, we are investigating and analyzing scenarios that will boost network performance iteratively over the short and longer term, including:

Chúng tôi có thể sẽ thực hiện thời gian chờ trung bình từ đệ trình giao dịch đến áp dụng giao dịch.
Cùng với đó, chúng tôi đang điều tra và phân tích các kịch bản sẽ tăng hiệu suất mạng lặp đi lặp lại trong thời gian ngắn và dài hạn, bao gồm:

- **Block size increase** â€” increased block size means more transactions in a block. The benefit is that there will be less waiting time for transactions to be adopted by a block during the periods of network saturation. However, there is a trade-off. Larger blocks take longer to propagate across the network. This also means that nodes will need more time to verify transactions. Although the block size increase is an option to increase network performance, such changes should be executed with caution. To ensure that the increase does not compromise block adoption time, we will gradually change parameters and assess the results during high saturation periods. This is not a one-step update, but rather an iterative approach that will provide us with clear results and help ensure the most efficient adjustments. 

- ** Tăng kích thước khối ** - tăng kích thước khối có nghĩa là nhiều giao dịch hơn trong một khối.
Lợi ích là sẽ có ít thời gian chờ đợi cho các giao dịch được thông qua bởi một khối trong các giai đoạn bão hòa mạng.
Tuy nhiên, có một sự đánh đổi.
Các khối lớn hơn mất nhiều thời gian hơn để nhân giống trên mạng.
Điều này cũng có nghĩa là các nút sẽ cần thêm thời gian để xác minh các giao dịch.
Mặc dù việc tăng kích thước khối là một tùy chọn để tăng hiệu suất mạng, nhưng những thay đổi đó nên được thực hiện một cách thận trọng.
Để đảm bảo rằng sự gia tăng không ảnh hưởng đến thời gian áp dụng khối, chúng tôi sẽ dần thay đổi các tham số và đánh giá kết quả trong thời gian bão hòa cao.
Đây không phải là bản cập nhật một bước, mà là một cách tiếp cận lặp đi lặp lại sẽ cung cấp cho chúng tôi kết quả rõ ràng và giúp đảm bảo các điều chỉnh hiệu quả nhất.

- **Mempool size** â€” currently, the size of the mempool is set to 128 KB, which is twice the size of the current block. The mempool works as the network buffer and may cause short delay when including transactions into a block. However, mempool size increase *wonâ€™t* improve network throughput â€“ transaction queues will stay the same. The mempool allows for a fair adoption of new transactions that enter it randomly based on the producing node that is chosen by the lottery algorithm. 

- ** Kích thước mempool ** Hiện tại, kích thước của mempool được đặt thành 128 kb, có kích thước gấp đôi khối hiện tại.
Mempool hoạt động như bộ đệm mạng và có thể gây ra độ trễ ngắn khi đưa các giao dịch vào một khối.
Tuy nhiên, việc tăng kích thước mempool * sẽ cải thiện thông lượng mạng - hàng đợi giao dịch sẽ giữ nguyên.
Mempool cho phép áp dụng công bằng các giao dịch mới nhập ngẫu nhiên dựa trên nút sản xuất được chọn bởi thuật toán xổ số.

- **Script compression** â€” given that the current transaction size is set to 16 KB, weâ€™re continuing to work on compression, which allows the protocol to â€˜zipâ€™ the code in a transparent manner. This means more script transactions in one block due to their decreased size â€“ developers will be able to submit more sophisticated code compressing it to 16 KB or less, and there will be more space left for other transactions. 

- ** Nén tập lệnh ** - cho rằng kích thước giao dịch hiện tại được đặt thành 16 kb, chúng tôi đang tiếp tục hoạt động trong nén, cho phép giao thức "mã theo cách minh bạch.
Điều này có nghĩa là nhiều giao dịch tập lệnh hơn trong một khối do kích thước giảm của chúng - các nhà phát triển sẽ có thể gửi mã tinh vi hơn khi nén nó xuống còn 16 kb hoặc ít hơn và sẽ còn nhiều không gian hơn cho các giao dịch khác.

## **Architecting for EUTXO**

## ** Kiến trúc cho eutxo **

As described in our [previous concurrency blog post](https://iohk.io/en/blog/posts/2021/09/10/concurrency-and-all-that-cardano-smart-contracts-and-the-eutxo-model/), Cardanoâ€™s EUTXO model eliminates entire classes of problems when designing DeFi applications. In addition to EUTXOâ€™s native ability to process transactions in parallel, the modelâ€™s [deterministic nature](https://iohk.io/en/blog/posts/2021/09/06/no-surprises-transaction-validation-on-cardano/) ensures that developers and users can avoid wasted â€˜gasâ€™.

Như được mô tả trong [Bài đăng trên blog đồng thời trước đây của chúng tôi (https://iohk.io/en/blog/posts/2021/09/10/concurrency-and-all-that-cardano-smart-contracts-and-the-eutxo
-Model/), mô hình EUTXO của Cardano loại bỏ toàn bộ các loại vấn đề khi thiết kế các ứng dụng DEFI.
Ngoài khả năng tự nhiên của EUTXO để xử lý các giao dịch song song, bản chất xác định của mô hình] (https://iohk.io/en/blog/posts/2021/09/06/no-surprises-transaction
-Validation-on-cardano/) đảm bảo rằng các nhà phát triển và người dùng có thể tránh bị lãng phí-Gasâ € ™.

That said, the EUTXO model isnâ€™t the same as the account-based model. Lifting and shifting application architecture intended for account-based systems to a EUTXO-based system will result in a suboptimal application design. Applications *designed specifically* for Cardanoâ€™s EUTXO model will provide the best user experience. 

Điều đó nói rằng, mô hình EUTXO không giống như mô hình dựa trên tài khoản.
Kiến trúc ứng dụng nâng và chuyển dành cho các hệ thống dựa trên tài khoản sang hệ thống dựa trên EUTXO sẽ dẫn đến thiết kế ứng dụng dưới mức tối ưu.
Các ứng dụng * Được thiết kế cụ thể * cho mô hình EUTXO của Cardano sẽ cung cấp trải nghiệm người dùng tốt nhất.

**Weâ€™ll publish a deeper technical dive on how developers can optimize order submission and processing, for example, to the EUTXO model shortly.**

** Chúng tôi sẽ xuất bản một nỗ lực kỹ thuật sâu hơn về cách các nhà phát triển có thể tối ưu hóa việc gửi và xử lý đơn hàng, ví dụ, vào mô hình EUTXO trong thời gian ngắn. **

## **Iteration & Improvement**

## ** Lặp lại & cải thiện **

So there is plenty of work going on behind the scenes as we continue to evolve and iterate. These are still early days, and we will continuously assess network performance and adjust parameters accordingly as we go. In the short term, weâ€™ll be able to ease NFT drop congestion by more evenly spreading the stake distribution and reward distribution computation. This will in turn enable us to increase the block size, eliminate pauses and congestion at epoch boundaries, and remove computational spikes (which can cause slower block propagation). Gradual block size increase will also let us assess the best case scenarios for network performance and these results will be soon visible on the network. 

Vì vậy, có rất nhiều công việc đang diễn ra đằng sau hậu trường khi chúng tôi tiếp tục phát triển và lặp lại.
Đây vẫn là những ngày đầu và chúng tôi sẽ liên tục đánh giá hiệu suất mạng và điều chỉnh các tham số theo đó khi chúng tôi đi.
Trong ngắn hạn, chúng ta sẽ có thể giảm bớt tắc nghẽn NFT bằng cách truyền đều hơn về phân phối cổ phần và tính toán phân phối phần thưởng.
Điều này sẽ lần lượt cho phép chúng tôi tăng kích thước khối, loại bỏ tạm dừng và tắc nghẽn ở ranh giới kỷ nguyên và loại bỏ các gai tính toán (có thể gây ra sự lan truyền khối chậm hơn).
Tăng kích thước khối dần dần cũng sẽ cho phép chúng tôi đánh giá các kịch bản trường hợp tốt nhất về hiệu suất mạng và những kết quả này sẽ sớm được hiển thị trên mạng.

We also plan to move the ledger state to disk storage to ease the on-chain load, alongside script compression and on-chain sharing features implementation. When finalized, they will greatly complement network adjustments. 

Chúng tôi cũng có kế hoạch chuyển trạng thái sổ cái sang lưu trữ đĩa để giảm tải trên chuỗi, bên cạnh việc nén tập lệnh và triển khai các tính năng chia sẻ trên chuỗi.
Khi hoàn thành, họ sẽ bổ sung rất nhiều điều chỉnh mạng.

In the mid-term, [Hydra](https://iohk.io/en/blog/posts/2021/09/17/hydra-cardano-s-solution-for-ultimate-scalability/) will bring additional capability. Longer-term, our Chief Scientist and team continue to research other methods and mechanisms around pricing frameworks and enhancing the Ouroboros protocol to increase transaction throughput. More on this in future blog posts! 

Vào giữa kỳ, [Hydra] (https://iohk.io/en/blog/posts/2021/09/17/hydra-cardano-solution
Về lâu dài, nhà khoa học và nhóm chính của chúng tôi tiếp tục nghiên cứu các phương pháp và cơ chế khác xung quanh các khung giá cả và tăng cường giao thức Ouroboros để tăng thông lượng giao dịch.
Thêm về điều này trong các bài viết trên blog trong tương lai!

## **Two months in**

## ** Hai tháng trong **

We are just two months since the start of the smart contracts era on Cardano. Whatever the weight of expectation and anticipation around the â€˜launchâ€™, this was never going to be a one-hit upgrade. Just as it was always going to take time for the ecosystem to build momentum, there was always going to be a period of bedding in and then adjusting, as demands on the network grow. Weâ€™re on a journey and understanding community feedback remains key. Talking to many of the exciting new projects #BuildingOnCardano, weâ€™re building a better understanding of their plans and objectives â€“ along with any issues they are facing â€“ so we can support and serve as needed. Weâ€™re also closely following the community debate. 

Chúng tôi chỉ hai tháng kể từ khi bắt đầu kỷ nguyên hợp đồng thông minh trên Cardano.
Bất kể trọng lượng của sự mong đợi và dự đoán xung quanh-˜launchâ € ™, đây sẽ không bao giờ là một bản nâng cấp một lần.
Giống như luôn luôn dành thời gian để hệ sinh thái xây dựng động lực, luôn luôn có một khoảng thời gian giường và sau đó điều chỉnh, khi nhu cầu trên mạng tăng lên.
Chúng tôi đang trên hành trình và hiểu phản hồi của cộng đồng vẫn là chìa khóa.
Nói chuyện với nhiều dự án mới thú vị #buildingoncardano, chúng tôi sẽ xây dựng sự hiểu biết tốt hơn về các kế hoạch và mục tiêu của họ - cùng với bất kỳ vấn đề nào mà họ đang phải đối mặt - để chúng tôi có thể hỗ trợ và phục vụ khi cần thiết.
Chúng tôi cũng đang theo sát cuộc tranh luận của cộng đồng.

Itâ€™s early days and weâ€™re all still learning. Yet, by design, Cardano is set up to flex and grow alongside its nascent â€“ yet already vibrant â€“ ecosystem. Letâ€™s *all* keep building!

Đó là những ngày đầu và tất cả chúng ta vẫn đang học.
Tuy nhiên, theo thiết kế, Cardano được thiết lập để uốn cong và phát triển cùng với hệ sinh thái mới sinh của nó.
Hãy * tất cả * tiếp tục xây dựng!

*If you are a developer and want guidance, support, or just fancy dropping by for a chat to one of our open sessions â€“ make sure you join our* growing technical community on [*Discord*](https://discord.com/channels/826816523368005654/892858202851516457).

*Nếu bạn là nhà phát triển và muốn hướng dẫn, hỗ trợ hoặc chỉ thích ghé qua để trò chuyện với một trong các phiên mở của chúng tôi - Hãy chắc chắn rằng bạn tham gia cộng đồng kỹ thuật*phát triển của chúng tôi trên [*Discord*]
.com/kênh/826816523368005654/892858202851516457).

*My thanks to John Woods, Vitor Silva, Kevin Hammond, Duncan Coutts, Romain Pellerin, Michael Peyton Jones, Jean-Frederic Etienne & Olga Hryniuk for their support and feedback in preparing this blog post.*

*Tôi cảm ơn John Woods, Vitor Silva, Kevin Hammond, Duncan Coutts, Romain Pellerin, Michael Peyton Jones, Jean-Frederic Etienne & Olga Hryniuk vì sự hỗ trợ và phản hồi của họ trong việc chuẩn bị bài đăng trên blog này.*

