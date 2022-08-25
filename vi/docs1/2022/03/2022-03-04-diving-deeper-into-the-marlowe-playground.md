# Tìm hiểu sâu hơn về Sân chơi Marlowe

### **Learn how to make your own templates from Marlowe contracts and provide hints to users using custom metadata**

![](img/2022-03-04-diving-deeper-into-the-marlowe-playground.002.png) 4 March 2022![](img/2022-03-04-diving-deeper-into-the-marlowe-playground.002.png)[ Pablo Lamela](/en/blog/authors/pablo-lamela-seijas/page-1/)![](img/2022-03-04-diving-deeper-into-the-marlowe-playground.003.png) 7 mins read

![Pablo Lamela](img/2022-03-04-diving-deeper-into-the-marlowe-playground.004.png)[](/en/blog/authors/pablo-lamela-seijas/page-1/)

### [**Pablo Lamela**](/en/blog/authors/pablo-lamela-seijas/page-1/)

Research Fellow

Research

- ![](img/2022-03-04-diving-deeper-into-the-marlowe-playground.005.png)[](mailto:pablo.lameja-seijas@iohk.io "Email")
- ![](img/2022-03-04-diving-deeper-into-the-marlowe-playground.006.png)[](https://www.linkedin.com/in/palas87/ "LinkedIn")
- ![](img/2022-03-04-diving-deeper-into-the-marlowe-playground.007.png)[](https://github.com/palas "GitHub")

![Diving deeper into the Marlowe Playground](img/2022-03-04-diving-deeper-into-the-marlowe-playground.008.jpeg)

Marlowe là một ngôn ngữ miền chuyên biệt (DSL) được nhúng trong Haskell, cung cấp các hợp đồng tài chính cho blockchain mà mọi người đều có thể viết mã. Nó là một nền tảng cho tài chính phi tập trung (DeFi) hỗ trợ cho vay trực tiếp, ngang hàng, hợp đồng giao dịch phái sinh (CFD) và các công cụ tương tự khác. Marlowe cho phép người dùng áp dụng kiến thức chuyên môn riêng của họ để viết và quản lý các hợp đồng một cách thuận tiện mà không cần quá trình học tập phức tạp liên quan đến phát triển phần mềm, blockchain hoặc hợp đồng thông minh.

[Sân chơi Marlowe](https://play.marlowe-finance.io/#/) là môi trường ảo, nơi bạn có thể thực hành viết các hợp đồng tài chính của mình. Sân chơi này cung cấp cho bạn lựa chọn làm việc trực tiếp bằng nhiều ngôn ngữ như viết trực tiếp bằng Marlowe, [JavaScript](https://play.marlowe-finance.io/doc/marlowe/tutorials/javascript-embedding.html), [Haskell](https://play.marlowe-finance.io/doc/marlowe/tutorials/embedded-marlowe.html) hoặc [Blockly](https://play.marlowe-finance.io/doc/marlowe/tutorials/playground-blockly.html), tùy thuộc vào ngôn ngữ bạn muốn sử dụng. Gần đây, chúng tôi đã thêm các tính năng mới vào Sân chơi Marlowe để xây dựng và chỉnh sửa các mẫu và tùy chỉnh siêu dữ liệu, cũng như tùy chọn tải xuống kiểu dữ liệu mới JSON cho chính các hợp đồng. Trong bài viết này, chúng ta sẽ xem xét kỹ hơn các tính năng mới này.

### **Tạo mẫu hợp đồng**

Với sự ra đời của Marlowe Run, chúng tôi đã mở rộng Sân chơi Marlowe để hỗ trợ những gì chúng tôi gọi là *mẫu* . Các *mẫu* này được triển khai bằng phiên bản mở rộng của Marlowe (được gọi là Extended Marlowe, phiên bản có sẵn trong Sân chơi Marlowe). Những mẫu mới này giúp người dùng có thể dễ dàng sử dụng lại các hợp đồng cho các tình huống và bối cảnh khác nhau.

Marlowe mở rộng cung cấp tính linh hoạt cao hơn Marlowe đơn thuần (hoặc Core Marlowe). Các hợp đồng rất cụ thể được mặc định thời gian timeouts (thời gian chờ) theo giá trị tuyệt đối, ban đầu thông qua slot numbers (số lượng khung giờ) và gần đây hơn là sử dụng timestamps (dấu thời gian) chuẩn (thời gian POSIX).

Additionally, Marlowe Values are typically hardcoded in Marlowe, except those passed as Inputs. For example, you can implement a loan for â‚³100 or one that asks the user how much to lend through a Choice in a When construct, but we could not have a reusable Marlowe contract that could be deployed at any time and with any given parameters. Extended Marlowe addresses these limitations by adding the option to include contract parameters. Currently, extended Marlowe is practically identical to plain Marlowe except in that it includes two extra constructors that represent *parameters* of the *template*:

- SlotParam - có thể được viết thay cho timeout (thời gian chờ) khi xây dựng
- ConstantParam - là kiểu cấu trúc "Value"

Cả hai hàm này đều lấy làm tham số duy nhất, một string (chuỗi) đóng vai trò là mã định danh cho tham số, ví dụ:

- SlotParam "Thời hạn thanh toán"
- ConstantParam "Price"

Hai tham số cùng kiểu (SlotParam hoặc ConstantParam) và có cùng số định dạng được coi là cùng một tham số, ngay cả khi chúng xuất hiện ở những nơi khác nhau.

Nếu hợp đồng chứa các tham số (hay được hiểu, nếu đó là một *mẫu* ), thì người dùng sẽ được yêu cầu nhập giá trị cho các tham số đó trước khi bắt đầu mô phỏng hợp đồng hoặc trước khi triển khai hợp đồng trong Marlowe Run:

![](img/2022-03-04-diving-deeper-into-the-marlowe-playground.009.png)

Figure 1. Simulation dialog

Lưu ý rằng đầu vào các tham số giá trị mẫu trong hình không chỉ là một trường nhập số nguyên. Thay vào đó, nó có thể là số thập phân và nó có nhãn với biểu tượng tiền tệ cho biết rằng số được nhập đại diện cho một lượng ada. Quy tắc này cũng đúng đối với các giá trị được yêu cầu lựa chọn khi xây dựng. Ngoài ra, các lựa chọn không cần phải đại diện cho số lượng ada. Chúng có thể đại diện cho bất kỳ thứ gì, chẳng hạn như một tỷ lệ, như sau:

![](img/2022-03-04-diving-deeper-into-the-marlowe-playground.010.png)

Figure 2. Actions dialog

Ngoài ra còn có các gợi ý cho từng tham số mà người dùng có thể hiển thị bằng cách nhấp vào dấu hỏi màu tím bên cạnh mỗi thuật ngữ. Văn bản trong gợi ý dành riêng cho mẫu hợp đồng và nó chứa nội dung được định dạng, ví dụ: **nội dung in đậm** , *nội dung in nghiêng* hoặc nội dung gạch chân.

![](img/2022-03-04-diving-deeper-into-the-marlowe-playground.011.png)

Figure 3. Parameter hints

User-defined contracts can customize all these details through the use of *metadata*. Letâ€™s take a look at how this is done.

## **Customizing metadata**

There is a *Metadata* tab at the bottom of each of the editors in the Marlowe Playground. There, users can customize the metadata as needed. For example:

![](img/2022-03-04-diving-deeper-into-the-marlowe-playground.012.png)

Hình 4. Tab Metadata

Có một số siêu dữ liệu cơ bản mà mọi hợp đồng dự kiến sẽ có, chẳng hạn như:

- **Contract type** - Đó là loại hợp đồng nào? Danh mục này sẽ giúp phân loại các hợp đồng để chúng dễ dàng tìm kiếm hơn trong tương lai. Hiện tại, có rất ít danh mục có sẵn, nhưng chúng tôi sẽ bổ sung thêm trong tương lai. Nếu không có danh mục nào phù hợp với hợp đồng của bạn, bạn luôn có thể chọn "Khác".
- **Contract name** - Chỉ là một cái tên ngắn gọn để xác định hợp đồng.
- **Contract short description** - Một mô tả rất ngắn gọn để hiển thị trong danh sách.
- **Contract long description** - Mô tả chi tiết hơn sẽ được hiển thị sau mô tả ngắn gọn trong trường hợp người dùng đã chọn mẫu và muốn biết thêm (ví dụ: khi tạo hợp đồng trong Marlowe Run).

Lưu ý rằng văn bản trong mô tả hỗ trợ sử dụng một số chức năng định dạng có trong Markdown. Ví dụ: thêm hai dấu hoa thị vào trước và sau một phần của văn bản mô tả sẽ làm cho văn bản đó được in đậm khi mô phỏng hợp đồng, như chúng ta đã thấy trong phần trước. Theo cách này, văn bản thuần túy:

Amount of **money** to pay

will be rendered as

Amount of **money** to pay

Chúng tôi khuyên bạn nên sử dụng chức năng này để làm nổi bật những từ khóa nào đại diện cho các thực thể có ý nghĩa đặc biệt trong ngữ cảnh của hợp đồng, chẳng hạn như tên của các roles hoặc choices.

Tab metadata cũng hỗ trợ chỉ định gợi ý cho các roles, choices, slot và các tham số giá trị được xác định trong hợp đồng, cũng như định dạng cho các lựa chọn và tham số giá trị.

Thông số role hoặc choice, slot hoặc giá trị mới được thêm vào hợp đồng sẽ xuất hiện trong tab metadata với màu đỏ. Trong trường hợp của trình chỉnh sửa Haskell và JavaScript, có thể cần phải biên dịch mã thành công trước khi điều này xảy ra.

![](img/2022-03-04-diving-deeper-into-the-marlowe-playground.013.png)

Hình 5. Tab Metadata - thêm các mục siêu dữ liệu

Nhấn nút “+” màu đỏ sẽ tạo mục nhập siêu dữ liệu mới cho mục đã cho. Theo cách tương tự, nếu role, choice, hoặc slot hoặc tham số value ngừng được sử dụng trong hợp đồng, siêu dữ liệu hiện có sẽ được gắn cờ màu đỏ để xóa và người dùng phải nhấn nút “-” để xóa mục siêu dữ liệu khỏi hợp đồng.

![](img/2022-03-04-diving-deeper-into-the-marlowe-playground.014.png)

Hình 6. Tab Metadata - xóa các mục siêu dữ liệu

Ngoài mô tả, trong các trường hợp tham số choices và value, người dùng có thể lựa chọn định dạng cho số mà họ muốn người dùng cuối cung cấp. Để làm điều đó, hãy chọn "Fixed point amount" từ menu thả xuống. Điều này sẽ cung cấp hai trường bổ sung:

- **Số chữ số thập phân cho giá trị** (dưới cùng bên trái) - các số trong Marlowe bên trong luôn là số nguyên, nhưng để thuận tiện, người dùng có thể nhập số chữ số sau dấu chấm được cố định. Ví dụ: lượng ada của Marlowe được biểu thị bằng lovelace (một phần triệu ada) nhưng nói chung, người dùng cuối thích làm việc với lượng ada hơn (vì chúng dễ đọc hơn). Các nhà phát triển có thể hỗ trợ điều này bằng cách viết 6 số chữ số thập phân. Do đó, người dùng cuối sẽ thấy dấu phân tách thập phân ở vị trí thứ 6, mặc dù nội bộ hợp đồng vẫn hoạt động với lovelace (đơn vị ada).
- **Nhãn tiền tệ cho giá trị** (dưới cùng bên phải) - các nhà phát triển cũng có thể hiển thị biểu tượng tiền tệ gần hộp nhập giá trị như một gợi ý cho người dùng cuối về đơn vị số tiền mà chúng tôi mong đợi từ họ. Ví dụ: trong trường hợp của ada, chỉ cần viết ký hiệu ada là “₳”.

![](img/2022-03-04-diving-deeper-into-the-marlowe-playground.015.png)

Figure 7. Number formatting

Cuối cùng, thứ tự của các tham số là quan trọng. Ví dụ: hãy tưởng tượng một số thông số slot để người dùng cuối chọn. Sẽ là hợp lý nếu hiển thị các thông số đó theo thứ tự thời gian.

To arrange the metadata, drag entries into the desired order, for example:

![](img/2022-03-04-diving-deeper-into-the-marlowe-playground.016.png)

Hình 8. Thứ tự Metadata

Thứ tự của các tham số trong metadata sẽ được sử dụng để tạo biểu mẫu được hiển thị ở phần đầu của mô phỏng hoặc thực hiện hợp đồng.

# **Kết luận**

With the new template and metadata extensions to Marlowe, contract developers can now provide hints and parameters to make it easier for end users to reuse the same contract in several circumstances, without having to understand the full implementation and the details of the contract.

These are just some of the new improvements that the Marlowe team continues to work on, and we look forward to sharing the details of more enhancements soon.

*Để tìm hiểu thêm về các bản phát hành Marlowe sắp tới và các tính năng mới, hãy theo dõi các kênh truyền thông xã hội của chúng tôi hoặc kênh [Marlowe Discord mới](https://discord.com/channels/826816523368005654/936295815926927390/936316494042779698) để biết thêm thông tin. Ngoài ra, hãy theo dõi để biết thông tin chi tiết về chương trình Người tiên phong Marlowe đầu tiên của chúng tôi sẽ sớm ra mắt!<br><br>Bài này được dịch bởi LinhPool [với bài gốc]<br>(https://iohk.io/en/blog/posts/2022/03/04/diving-deeper-into-the-marlowe-playground/} <br>*Dự án này được tài trợ bởi Catalyst**
