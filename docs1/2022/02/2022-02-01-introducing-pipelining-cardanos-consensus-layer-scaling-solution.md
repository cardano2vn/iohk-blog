# Introducing pipelining: Cardano's consensus layer scaling solution
### **Pipelining is one of the key scaling improvements to be deployed in 2022. Here’s how it works and why it matters**
![](img/2022-02-01-introducing-pipelining-cardanos-consensus-layer-scaling-solution.002.png) 1 February 2022![](img/2022-02-01-introducing-pipelining-cardanos-consensus-layer-scaling-solution.002.png)[ John Woods](tmp//en/blog/authors/john-woods/page-1/)![](img/2022-02-01-introducing-pipelining-cardanos-consensus-layer-scaling-solution.003.png) 4 mins read

![John Woods](img/2022-02-01-introducing-pipelining-cardanos-consensus-layer-scaling-solution.004.png)[](tmp//en/blog/authors/john-woods/page-1/)
### [**John Woods**](tmp//en/blog/authors/john-woods/page-1/)
Director of Cardano Architecture

Engineering

- ![](img/2022-02-01-introducing-pipelining-cardanos-consensus-layer-scaling-solution.005.png)[](mailto:john.woods@iohk.io "Email")
- ![](img/2022-02-01-introducing-pipelining-cardanos-consensus-layer-scaling-solution.006.png)[](https://www.linkedin.com/in/johnalanwoods/ "LinkedIn")
- ![](img/2022-02-01-introducing-pipelining-cardanos-consensus-layer-scaling-solution.007.png)[](https://github.com/johnalanwoods "GitHub")

![Introducing pipelining: Cardano's consensus layer scaling solution](img/2022-02-01-introducing-pipelining-cardanos-consensus-layer-scaling-solution.008.jpeg)

You’d be forgiven for thinking that pipelining sounds like a remodelling procedure a plumber might employ. In a way, this isn’t too far from the truth. Pipelining is, effectively, an evolution in Cardano’s ‘plumbing’. It is a key element in our scaling plan this year, one in the series of [published steps](https://iohk.io/en/blog/posts/2022/01/14/how-we-re-scaling-cardano-in-2022/#modal=https://ucarecdn.com/fc644130-c13d-43f9-a966-14290687d190/) covering our methodical approach to flex Cardano’s capacity as the ecosystem grows.

Bạn có thể được tha thứ vì nghĩ rằng đường ống nghe có vẻ như là một thủ tục tu sửa mà một thợ sửa ống nước có thể sử dụng.
Theo một cách nào đó, đây là quá xa sự thật.
Pipelining, một cách hiệu quả, là một sự tiến hóa trong Cardano, hệ thống ống nước.
Đó là một yếu tố quan trọng trong kế hoạch mở rộng của chúng tôi trong năm nay, một trong loạt các [các bước được xuất bản] (https://iohk.io/en/blog/posts/2022/01/14/how-we-re-re-scaling-
cardano-in-2022/#modal = https: //ucarecdn.com/fc644130-c13d-43f9-a966-14290687d190/) bao gồm phương pháp có phương pháp của chúng tôi đối với khả năng của Flex Cardano khi hệ sinh thái phát triển.

Scaling and throughput are crucial considerations for any blockchain, if growth and competitiveness are to be maintained. As Cardano enters the Basho phase of development, we're laser-focused on ensuring that Cardano scales to meet the growing needs of the ecosystem. In other words, we need to ensure that the underlying protocol – Ouroboros Praos – operates fast enough for the plethora of decentralized applications now deploying or lining up to launch on Cardano.

Việc mở rộng và thông lượng là những cân nhắc quan trọng đối với bất kỳ blockchain nào, nếu tăng trưởng và khả năng cạnh tranh sẽ được duy trì.
Khi Cardano bước vào giai đoạn phát triển Basho, chúng tôi tập trung vào laser để đảm bảo rằng các quy mô Cardano để đáp ứng nhu cầu ngày càng tăng của hệ sinh thái.
Nói cách khác, chúng tôi cần đảm bảo rằng giao thức cơ bản - OuroBoros PRAOS - hoạt động đủ nhanh để rất nhiều ứng dụng phi tập trung hiện đang triển khai hoặc xếp hàng để khởi chạy trên Cardano.

Cardano will continue to be steadily optimized in a series of measured steps, carefully & methodically scaling #Cardano for future growth as demand increases. The changes introduced by the release of node 1.33.0 in early January gave us additional headroom to modify some network parameters, including block size and memory units. Adjustments here have a direct bearing on how Cardano handles network traffic in volume and we continue to monitor network performance closely.

Cardano sẽ tiếp tục được tối ưu hóa đều đặn trong một loạt các bước đo lường, cẩn thận và mở rộng một cách có phương pháp #cardano cho sự tăng trưởng trong tương lai khi nhu cầu tăng.
Những thay đổi được giới thiệu bởi việc phát hành Node 1.33.0 vào đầu tháng 1 đã cho chúng tôi thêm khoảng trống để sửa đổi một số tham số mạng, bao gồm kích thước khối và đơn vị bộ nhớ.
Điều chỉnh ở đây có liên quan trực tiếp đến cách Cardano xử lý lưu lượng mạng về khối lượng và chúng tôi tiếp tục theo dõi hiệu suất mạng một cách chặt chẽ.

Continuing close observation of real world network performance and - importantly - the cumulative impact of parameter changes will be key throughout this process. Following each update, we carefully monitor and assess across at least one epoch (5 days) before continuing with further adjustments. As much as extensive research and engineering work has gone into designing and deploying the system, a decentralized network architecture needs to be scaled based on real world user behaviours and usage.

Tiếp tục quan sát chặt chẽ về hiệu suất mạng trong thế giới thực và - quan trọng - tác động tích lũy của các thay đổi tham số sẽ là chìa khóa trong suốt quá trình này.
Theo sau mỗi bản cập nhật, chúng tôi cẩn thận theo dõi và đánh giá ít nhất một kỷ nguyên (5 ngày) trước khi tiếp tục điều chỉnh thêm.
Nhiều như công việc nghiên cứu và kỹ thuật mở rộng đã đi vào thiết kế và triển khai hệ thống, một kiến trúc mạng phi tập trung cần được thu nhỏ dựa trên hành vi và cách sử dụng của người dùng trong thế giới thực.

## **Introducing pipelining**

## ** Giới thiệu đường ống **

Pipelining – or more precisely, diffusion pipelining – is an improvement to the consensus layer that facilitates faster block propagation. It enables even greater gains in headroom, which will enable further increases to Cardano's performance and competitiveness.

Đường ống - hay chính xác hơn là đường ống khuếch tán - là một cải tiến cho lớp đồng thuận tạo điều kiện lan truyền khối nhanh hơn.
Nó cho phép lợi ích lớn hơn trong khoảng trống, điều này sẽ cho phép tăng thêm hiệu suất và khả năng cạnh tranh của Cardano.

To understand how this technique achieves its intended goal, let's recap how blocks propagate at present.

Để hiểu làm thế nào kỹ thuật này đạt được mục tiêu dự định của nó, hãy tóm tắt lại cách các khối tuyên truyền hiện tại.

Currently, a block goes through six steps as it moves across the chain:

Hiện tại, một khối trải qua sáu bước khi nó di chuyển qua chuỗi:

1. Block header transmission

1. Hộp số tiêu đề chặn

1. Block header validation

1. Chặn xác thực tiêu đề

1. Block body request and transmission

1. Khối yêu cầu và truyền tải cơ thể

1. Block body validation and local chain extension

1. Chặn xác thực cơ thể và mở rộng chuỗi cục bộ

1. Block header transmission to downstream nodes

1. Chặn truyền tiêu đề đến các nút hạ lưu

1. Block body transmission to downstream nodes

1. Chặn truyền cơ thể đến các nút hạ nguồn

A block’s journey is a very serialized one. All steps happen in the same sequence every time, at every node. Considering the volume of nodes and the ever-growing number of blocks, block transmission takes a considerable amount of time.

Một hành trình khối khối là một cuộc hành trình rất tuần tự hóa.
Tất cả các bước xảy ra trong cùng một chuỗi mỗi lần, ở mỗi nút.
Xem xét khối lượng của các nút và số lượng khối ngày càng tăng, việc truyền khối mất một khoảng thời gian đáng kể.

Diffusion pipelining overlays some of those steps on top of each other so they happen concurrently. This saves time and increases throughput.

Đường ống khuếch tán bao phủ một số bước trên đầu nhau để chúng xảy ra đồng thời.
Điều này tiết kiệm thời gian và tăng thông lượng.

![](img/2022-02-01-introducing-pipelining-cardanos-consensus-layer-scaling-solution.009.png) The time saving afforded by this technique will lead to even more headroom to further scale Cardano, including changes to: 

- Block size - the bigger the block, the more transactions and scripts it can carry

- Kích thước khối - khối càng lớn, càng nhiều giao dịch và tập lệnh mà nó có thể thực hiện

- Plutus memory limits - the amount of memory available for a Plutus script to run

- Giới hạn bộ nhớ của Plutus - lượng bộ nhớ có sẵn cho tập lệnh Plutus để chạy

- Plutus CPU limits - more computational resources can be allocated for a script to run more efficiently

- Giới hạn CPU Plutus - Tài nguyên tính toán nhiều hơn có thể được phân bổ cho một tập lệnh để chạy hiệu quả hơn

## **Implementing pipelining**

## ** Thực hiện đường ống **

One of the design principles behind diffusion pipelining was to achieve faster block propagation while avoiding ‘destructive’ changes to the chain. We did not want to remove any of the protocols, primitives, or interactions already happening in Cardano, because nodes rely on these established mechanisms. We wanted full backwards compatibility, so instead of changing the way things currently work, we're adding a new mini-protocol whose job is to pre-notify subscribed entities when a new desirable block is seen, prior to full validation.

Một trong những nguyên tắc thiết kế đằng sau đường ống khuếch tán là đạt được sự lan truyền khối nhanh hơn trong khi tránh những thay đổi phá hoại đối với chuỗi.
Chúng tôi không muốn loại bỏ bất kỳ giao thức, nguyên thủy hoặc tương tác nào đã xảy ra trong Cardano, bởi vì các nút dựa vào các cơ chế đã được thiết lập này.
Chúng tôi muốn có khả năng tương thích ngược hoàn toàn, vì vậy thay vì thay đổi cách mọi thứ hiện đang hoạt động, chúng tôi sẽ thêm một giao dịch nhỏ mới có công việc được thông báo trước các thực thể đã đăng ký khi nhìn thấy một khối mong muốn mới, trước khi xác nhận đầy đủ.

The key change introduced by pipelining is the ability to pre-notify peers and give them a block before it is validated, which enables the downstream peer to pre-fetch the new block body. This saves a lot of time because we dramatically reduce the time it takes to validate a block across the multiple hops.

Thay đổi quan trọng được giới thiệu bởi đường ống là khả năng thông báo trước các đồng nghiệp và cung cấp cho họ một khối trước khi nó được xác thực, cho phép người ngang hàng hạ nguồn để lấy trước thân khối mới.
Điều này tiết kiệm rất nhiều thời gian vì chúng tôi giảm đáng kể thời gian cần thiết để xác nhận một khối trên nhiều bước nhảy.

## **In conclusion**

## **Tóm lại là**

Pipelining is just one of the pillars supporting Cardano's scaling this year. Combined, all these changes will lead Cardano to a position where it is faster than its competitors, and a highly competitive platform for decentralized finance (DeFi) this year.

Pipelining chỉ là một trong những trụ cột hỗ trợ tỷ lệ của Cardano trong năm nay.
Kết hợp lại, tất cả những thay đổi này sẽ dẫn Cardano đến một vị trí nhanh hơn so với các đối thủ cạnh tranh và một nền tảng cạnh tranh cao cho tài chính phi tập trung (DEFI) trong năm nay.

## **Key takeaways**

## ** Key Takeaways **

![](img/2022-02-01-introducing-pipelining-cardanos-consensus-layer-scaling-solution.010.png)

***Fernando Sanchez contributed to this article.***

*** Fernando Sanchez đã đóng góp cho bài viết này. ***

