# Cách chúng tôi mở rộng quy mô Cardano trong năm 2022

### **Với cốt lõi hợp đồng thông minh đã được triển khai, giai đoạn tiếp theo của Cardano tập trung vào tối ưu hóa hiệu suất và mở rộng quy mô. Và nó bắt đầu ngay từ bây giờ…**

![](img/2022-01-14-how-we-re-scaling-cardano-in-2022.002.png) 14 tháng 1 năm 2022![](img/2022-01-14-how-we-re-scaling-cardano-in-2022.002.png) [Tim Harrison](/en/blog/authors/tim-harrison/page-1/)![](img/2022-01-14-how-we-re-scaling-cardano-in-2022.003.png)5 phút đọc

![Tim Harrison](img/2022-01-14-how-we-re-scaling-cardano-in-2022.004.png)[](/en/blog/authors/tim-harrison/page-1/)

### [**Tim Harrison**](/en/blog/authors/tim-harrison/page-1/)

Phó Chủ tịch Cộng đồng &amp; Hệ sinh thái

Thông tin liên lạc

- ![](img/2022-01-14-how-we-re-scaling-cardano-in-2022.005.png)[](mailto:tim.harrison@iohk.io "E-mail")
- ![](img/2022-01-14-how-we-re-scaling-cardano-in-2022.006.png)[](https://uk.linkedin.com/in/timbharrison "LinkedIn")
- ![](img/2022-01-14-how-we-re-scaling-cardano-in-2022.007.png)[](https://twitter.com/timbharrison "Twitter")
- ![](img/2022-01-14-how-we-re-scaling-cardano-in-2022.008.png)[](https://github.com/timbharrison "GitHub")

Dự án Cardano luôn cam kết giải quyết vấn đề tưởng chừng như nan giải của thế hệ blockchain cũ đó là rất khó để vừa mở rộng quy mô, vừa đảm bảo sự an toàn và tính phi tập trung (quan trọng nhất). IOG là tổ chức được giao nhiệm vụ tạo ra nền tảng cốt lõi, chúng tôi luôn xác định một lộ trình để có thể phát huy hết khả năng của Cardano và phát huy hết tiềm năng lâu dài của nó.

Sử dụng các phương pháp phát triển chính thức và ngôn ngữ lập trình Haskell - với nguồn gốc từ phương pháp tiếp cận học thuật peer reviewed - chúng tôi đã cung cấp một nền tảng mạnh mẽ, an toàn và phù hợp cho tương lai. Được xây dựng một cách đúng đắn. Chúng tôi đặt tên cho giai đoạn này là kỷ nguyên Byron.

Một cộng đồng lớn đã phát triển đáng kinh ngạc nhờ những nỗ lực của chúng tôi và thông qua mạng lưới khoảng 3000 nhà vận hành pool ủy thác, chúng tôi hiện có một trong những mạng dPOS (bằng chứng cổ phần) phi tập trung lớn nhất trên thế giới. Kỷ nguyên phân quyền và pool ủy thác này được chúng tôi đặt tên là Shelley, theo tên nhà thơ và nhà chính trị cấp tiến, Percy Bysshe Shelley.

Goguen (which included the Alonzo HFC event) brought with it core smart contract capability, paving the way for DeFi and DApps. With initial Plutus capability now deployed, we continue to evolve the expressiveness of the Plutus language and the overall proposition, in collaboration with a growing community of developers.

Hiện nay, khi bước vào kỷ nguyên Basho, chúng tôi đang đầu tư thêm nguồn lực vào việc tối ưu hóa và mở rộng quy mô. Việc xây dựng được dựa trên những nền tảng này, đồng thời tăng đều đặn dung lượng và thông lượng để đáp ứng với sự phát triển trong hệ sinh thái DApp, trước hết là hàng trăm nghìn, sau đó là hàng triệu người dùng mới. Từ những người tham gia vào DeFi đến công dân của các quốc gia đang phát triển.

During the course of this year, starting right now, we’ll be pursuing this next phase of our mission. Parameter adjustments, improvements, enhancements and other innovations will all play their part in steadily increasing Cardano’s capacity &amp; throughput during 2022. While maintaining the considered, safe approach that has served us to date. Yes, we anticipate periods of high demand, network congestion at times. We’re on an exciting journey and usage will be high. While we may at times feel impatient, this is the way. Here’s how we will optimize and scale as we grow.

## **Các giải pháp On-chain**

**Tăng kích thước khối (block size)**

The bigger the block, the more transactions it can carry. Block size was recently increased by 8KB to 72KB (a 12.5% increase); further increases will be applied over time based on ongoing system monitoring and overall network health.

**Pipelining**

Cải thiện thời gian truyền tải giữa các block bằng cách kết hợp xác thực và lan truyền. Mục tiêu là để các block được truyền cho ít nhất 95% các đối tượng ngang hàng trong vòng năm giây bằng cách giảm 'thời gian chết' giữa các block (giảm chi phí truyền tải). Điều này cung cấp khoảng trống để thực hiện các thay đổi tỷ lệ tích cực hơn, chẳng hạn như tăng kích thước block / tăng giới hạn tham số Plutus.

**Input Endorsers**

Input endorsers improve block propagation times and throughput by allowing transactions to be separated into pre-constructed blocks. This improves the consistency of block propagation times and allows higher transaction rates.

**Memory /CPU parameters for Plutus**

Sử dụng bộ nhớ hiệu quả hơn trên toàn bộ chuỗi. Cụ thể, có những cải tiến về bộ nhớ trong việc xử lý UTXO (Unspent Transaction Output), phân phối cổ phần, phân phối cổ phần trực tiếp và các pool, thể hiện hàm băm (hash).

**Cải tiến tập lệnh Plutus**

Sử dụng hiệu quả, mạnh mẽ hơn nữa mô hình EUTXO thông qua tối ưu hóa hợp đồng thông minh, bao gồm:

- Đầu vào tham chiếu (CIP-0031) - Tập lệnh Plutus có thể kiểm tra đầu vào giao dịch mà không cần phải sử dụng chúng. Điều này có nghĩa là không cần thiết phải tạo UTXO chỉ để kiểm tra thông tin do đầu vào nắm giữ.
- Plutus Datums (CIP-0032) - Datums có thể được gắn trực tiếp vào đầu ra thay vì được xử lý bởi hàm băm. Điều này đơn giản hóa cách sử dụng dữ liệu, vì người dùng có thể thấy dữ liệu thực tế thay vì phải cung cấp dữ liệu khớp với hàm băm đã cho.
- Script sharing (CIP-0033) – Plutus script references can be associated with transaction outputs, meaning that they can be recorded on-chain for subsequent reuse. It will not be necessary to supply a copy of the script with each transaction, hugely reducing friction for developers. Reusing scripts in multiple transactions significantly reduces transaction sizes, improving throughput and reducing script execution costs.

**Node enhancements**

Improvements will help even distribution of stake and reward computations across the epochs, thus providing greater headroom for block size increases. Also, memory usage is now more efficient. Memory compaction reduces RSS footprint, and memory sharing means we need less data instantiated. Node version 1.33.0, from January 2022, reduces peak load at critical points, including the epoch boundary.

**Lưu trữ trên ổ đĩa**

Bằng cách lưu trữ trên ổ đĩa, các node sẽ cần ít bộ nhớ hơn, có nghĩa là các thiết bị hạn chế RAM có thể chạy node, miễn là chúng có đủ bộ nhớ và bộ nhớ sẽ không còn là rào cản đối với khả năng mở rộng của blockchain. Điều này sẽ giúp trạng thái của blockchain tăng trưởng đáng kể.

## **Các giải pháp Off-chain**

**Sidechains**

A sidechain is a separate blockchain connected to a main blockchain (the 'main' chain, also known as parent chain), through a two-way mechanism (the 'bridge') that enables tokens and other digital assets from one chain to be used in another and results returned to the original chain. Assets can be moved between chains as needed. One single parent chain can have multiple interoperable sidechains connected to it, which may operate in completely different ways. EVM sidechains coming to Cardano include dcSpark’s Milkomeda and IOG’s EVM sidechain project, codenamed ‘Mamba’.

**Hydra**

Giới thiệu các giao thức Layer 2 bao gồm các kênh để tối đa hóa thông lượng, giảm thiểu độ trễ, chi phí thấp hoặc không tốn kém và giảm đáng kể yêu cầu lưu trữ. Hydra cung cấp một phương tiện hiệu quả hơn để xử lý các giao dịch ngoài chuỗi (off-chain) trong khi sử dụng sổ cái chuỗi chính (main-chain) làm lớp thanh toán an toàn.

**Sự tính toán ngoài chuỗi**

Offloading some of the computation, for example with Asynchronous Contract Execution (ACE) can drive greater core network efficiency. Transactions occur outside of the blockchain itself, yet can offer fast, cheap transactions via a trust model.

**Mithril**

To achieve greater scalability, you need to address the complexity of critical operations that depend logarithmically on the number of participants. Mithril will improve chain synchronization while maintaining trust. The result? Multi-signature aggregation that is fast and efficient without compromising security features.

![](img/2022-01-14-how-we-re-scaling-cardano-in-2022.009.jpeg)

*Infographic credit: Mikki Pham/Fernando Sanchez*
