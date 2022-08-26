# Giới thiệu công cụ giao diện dòng lệnh mới cho Marlowe

### **Tìm hiểu cách gửi giao dịch và tương tác với các hợp đồng Marlowe từ CLI**

![](img/2022-04-19-introducing-the-new-command-line-interface-tool-for-marlowe.002.png) Ngày 19 tháng 4 năm 2022![](img/2022-04-19-introducing-the-new-command-line-interface-tool-for-marlowe.002.png)[ Niamh Ahern](/en/blog/authors/niamh-ahern/page-1/)![](img/2022-04-19-introducing-the-new-command-line-interface-tool-for-marlowe.003.png) bài đọc 5 phút

![Niamh Ahern](img/2022-04-19-introducing-the-new-command-line-interface-tool-for-marlowe.004.png)[](/en/blog/authors/niamh-ahern/page-1/)

### [**Niamh Ahern**](/en/blog/authors/niamh-ahern/page-1/)

Education Manager

Education

- ![](img/2022-04-19-introducing-the-new-command-line-interface-tool-for-marlowe.005.png)[](mailto:niamh.ahern@iohk.io "Email")
- ![](img/2022-04-19-introducing-the-new-command-line-interface-tool-for-marlowe.006.png)[](https://www.linkedin.com/in/niamh-ahern-67849949/ "LinkedIn")
- ![](img/2022-04-19-introducing-the-new-command-line-interface-tool-for-marlowe.007.png)[](https://twitter.com/nahern_iohk?lang=en "Twitter")
- ![](img/2022-04-19-introducing-the-new-command-line-interface-tool-for-marlowe.008.png)[](https://github.com/nahern "GitHub")

![Giới thiệu công cụ giao diện dòng lệnh mới cho Marlowe](img/2022-04-19-introducing-the-new-command-line-interface-tool-for-marlowe.009.jpeg)

Marlowe is an open source, domain specific language (DSL) with a suite of products for the community that will catalyze the adoption of Cardano in finance. It is constantly being enhanced and updated, and a command line interface (CLI) is just something you can't do without. So, we created a more convenient way to interact with Marlowe using the new CLI tool. This new tool supports a straightforward workflow for users who want to run contracts from the command line. It lets you focus on the Marlowe contract itself, while the tool manages details of the input and state for the contract. Additionally, it automates many aspects of Plutus as well as interaction with the Cardano node itself to reduce the burden on users.

### **Mục đích**

Công cụ [Marlowe CLI](https://github.com/input-output-hk/marlowe-cardano/blob/cli-blog-april2022/marlowe-cli/ReadMe.md) mới tạo điều kiện thuận lợi cho sự phát triển nội bộ và thử nghiệm các hợp đồng Marlowe. Điều này bao gồm việc đo kích thước giao dịch, gửi giao dịch, thử nghiệm tích hợp ví và gỡ lỗi trình xác thực. Nó cũng được tích hợp với quy trình làm việc của nhà phát triển bên ngoài và bộ công cụ cho các hợp đồng Marlowe, tương tự như cách cộng đồng phát triển Cardano đã tích hợp mạnh mẽ công cụ Cardano CLI vào các dịch vụ khác nhau như thư viện, phân phối, đúc token, chợ giao dịch,…

Đây cũng là một bước quan trọng trong lộ trình thử nghiệm căng thẳng việc  mã hóa của chúng tôi trước khi ra mắt chính thức Marlowe, vì nó cung cấp quyền truy cập sớm vào các tính năng và khả năng trên testnet và sau đó trên mainnet.

Ngoài ra, công cụ CLI mới này sẽ trở thành một công cụ hữu ích để đào tạo người dùng về cách bắt kịp tốc độ sử dụng Marlowe. Chúng tôi sẽ trình bày cách sử dụng nó trong chương trình những người tiên phong sử dụng Marlowe sắp ra mắt trong vài tuần tới! Hãy theo dõi [ kênh Marlowe Discord](https://discord.com/channels/826816523368005654/936295815926927390/936316494042779698)  của chúng tôi để biết chi tiết về thời điểm bắt đầu khóa học này và cách bạn có thể tham gia.

## **Running Marlowe contracts**

The marlowe-cli command supports several fine-grained and high-level workflows for running Marlowe contracts, but here we will focus on a workflow that abstracts away the specifics of Marloweâ€™s use of the Plutus language. The tool is installed similarly to other Cardano tools, using standard Cabal or Nix commands. Basic use just involves a couple of commands:

- Create an example contract from a template
- Khởi tạo hợp đồng để có thể gửi giao dịch đã tạo
-  Áp dụng đầu vào cho hợp đồng
- Rút tiền từ hợp đồng
- Gửi một giao dịch từ việc tạo, áp dụng đầu vào hoặc rút tiền
- Truy vấn lịch sử của một hợp đồng

![](img/2022-04-19-introducing-the-new-command-line-interface-tool-for-marlowe.010.jpeg)

Figure 1: High-level workflow for running Marlowe contracts at the command line. Each rectangle corresponds to running a marlowe-cli command.

There are several ways to design Marlowe contracts, but the easiest are to use the CLIâ€™s template command or the [Marlowe Playground](https://iohk.io/en/blog/posts/2022/03/04/diving-deeper-into-the-marlowe-playground/). One can also create contracts programmatically using Haskell, JavaScript, or any other language that can output the required JSON files that embody the contract and its initial state. The CLIâ€™s template command can generate simple test contracts, escrow contracts, zero-coupon bonds, token swaps, and covered calls. The Playground contains eight example contracts, but you can also design a custom Marlowe contract with it.

Khi một hợp đồng đã được tạo và trạng thái bắt đầu của nó được xác định, lệnh initialize của CLI sẽ bó những thông tin đó lại cùng với các chi tiết của mạng Cardano nơi nó sẽ được chạy. Tệp kết quả .marlowe theo chuẩn JSON duy nhất chứa tất cả thông tin cần thiết để chạy hoặc nghiên cứu hợp đồng Marlowe. Ngoài hợp đồng và trạng thái hiện tại, nó còn chứa địa chỉ của trình xác thực Marlowe, bản sao trình tự hóa của tập lệnh Plutus và các chi tiết mạng. Việc kiểm tra và trích xuất thông tin từ tệp JSON này có thể hữu ích trong việc tìm hiểu về cách hoạt động của Marlowe, nhưng không cần thiết để chạy các hợp đồng Marlowe. Khi thông tin cần thiết này đã được đóng gói, CLI sẽ chạy lệnh execute gửi giao dịch Plutus thực tế đến blockchain Cardano, in số liệu thống kê về giao dịch và chờ xác nhận.

Applying inputs to a contract follows a simpler process. The CLIâ€™s prepare command lets you set up a deposit of funds to the contract, make a choice in it, or notify it. This takes the previous .marlowe file as input and produces a new one as output, which you can submit with the execute command. The prepare command will warn you if the input is illegal or untimely.

Việc rút tiền được thanh toán bằng hợp đồng Marlowe được thực hiện bằng lệnh withdraw, cho phép bạn chọn địa chỉ nhận tiền. Lựa chọn địa chỉ nhận tiền cung cấp sự linh hoạt trong việc giải ngân vốn, để các địa chỉ đầu ra không bị “mắc kẹt” vào chính hợp đồng.

Truy vấn lịch sử của hợp đồng cũng có thể được thực hiện từ dòng lệnh hoặc bạn có thể sử dụng trình khám phá của blockchain Cardano.

# **Tương lai**

Công cụ dòng lệnh cũng cung cấp các tính năng nâng cao để tạo và thao tác các trình xác nhận, dữ liệu, trình xác nhận lại và hàm băm của Plutus liên quan đến hợp đồng Marlowe. Các hợp đồng cũng có thể được nén (sử dụng hàm băm Merkle), điều này giúp bạn có thể chạy các hợp đồng lớn hơn nhiều so với giới hạn của giao thức Cardano về kích thước giao dịch và bộ nhớ, điều này trái lại với việc cho phép. Bạn cũng có thể sử dụng CLI để chạy các hợp đồng Marlowe trên PAB, loại bỏ nhu cầu quản lý UTxO và thay vào đó là dùng ví  để quản lý điều đó.

This CLI tool is periodically enhanced to meet developer needs as they emerge. In addition to further simplifying Marlowe workflows, the toolâ€™s contract-testing capabilities are being expanded.

*Hãy tham gia với chúng tôi trên [kênh Marlowe Discord](https://discord.com/channels/826816523368005654/936295815926927390/936316494042779698) để tham gia vào các cuộc thảo luận, đặt câu hỏi và nghe tin tức mới nhất về Marlowe.*

*Tôi muốn cảm ơn Brian Bush, kỹ sư phần mềm của Marlowe, vì sự giúp đỡ của anh ấy trong việc viết bài blog này.<br><br><br><br>Bài này được dịch bởi Lê Nguyên. <a class="_active_edit_href" href="https://iohk.io/en/blog/posts/2022/04/19/introducing-the-new-command-line-interface-tool-for-marlowe/#">với bài gốc</a><br><em>Dự án này được tài trợ bởi Catalyst</em>*
