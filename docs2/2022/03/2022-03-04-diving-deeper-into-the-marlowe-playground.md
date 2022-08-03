# Diving deeper into the Marlowe Playground
### **Learn how to make your own templates from Marlowe contracts and provide hints to users using custom metadata**
![](img/2022-03-04-diving-deeper-into-the-marlowe-playground.002.png) 4 March 2022![](img/2022-03-04-diving-deeper-into-the-marlowe-playground.002.png)[ Pablo Lamela](tmp//en/blog/authors/pablo-lamela-seijas/page-1/)![](img/2022-03-04-diving-deeper-into-the-marlowe-playground.003.png) 7 mins read

![Pablo Lamela](img/2022-03-04-diving-deeper-into-the-marlowe-playground.004.png)[](tmp//en/blog/authors/pablo-lamela-seijas/page-1/)
### [**Pablo Lamela**](tmp//en/blog/authors/pablo-lamela-seijas/page-1/)
Research Fellow

Research

- ![](img/2022-03-04-diving-deeper-into-the-marlowe-playground.005.png)[](mailto:pablo.lameja-seijas@iohk.io "Email")
- ![](img/2022-03-04-diving-deeper-into-the-marlowe-playground.006.png)[](https://www.linkedin.com/in/palas87/ "LinkedIn")
- ![](img/2022-03-04-diving-deeper-into-the-marlowe-playground.007.png)[](https://github.com/palas "GitHub")

![Diving deeper into the Marlowe Playground](img/2022-03-04-diving-deeper-into-the-marlowe-playground.008.jpeg)

Marlowe is a domain-specific language (DSL) embedded in Haskell that offers financial contracts for blockchain that everyone can code. It is a platform for decentralized finance (DeFi) that supports direct, peer-to-peer lending, contracts for difference (CFD), and other similar instruments. Marlowe allows users to apply their domain expertise to write and manage contracts conveniently, without the steep learning curve associated with software development, blockchain, or smart contracts.

Marlowe là ngôn ngữ cụ thể về miền (DSL) được nhúng trong Haskell cung cấp các hợp đồng tài chính cho blockchain mà mọi người đều có thể mã hóa.
Đây là một nền tảng cho tài chính phi tập trung (DEFI) hỗ trợ cho vay trực tiếp, ngang hàng, hợp đồng cho sự khác biệt (CFD) và các công cụ tương tự khác.
Marlowe cho phép người dùng áp dụng chuyên môn miền của họ để viết và quản lý hợp đồng một cách thuận tiện, mà không cần đường cong học tập dốc liên quan đến phát triển phần mềm, blockchain hoặc hợp đồng thông minh.

The [Marlowe Playground](https://play.marlowe-finance.io/#/) is the sandbox environment where you can practice writing your financial contracts. This playground offers you a choice of working directly in a range of languages such as Marlowe itself, [JavaScript](https://play.marlowe-finance.io/doc/marlowe/tutorials/javascript-embedding.html), [Haskell](https://play.marlowe-finance.io/doc/marlowe/tutorials/embedded-marlowe.html), or [Blockly](https://play.marlowe-finance.io/doc/marlowe/tutorials/playground-blockly.html), depending on which you prefer to use. We have recently added new features to the Marlowe Playground for constructing and editing templates and customizing metadata, as well as a new JSON download option for the contracts themselves. In this post, we take a closer look at these new features.

[Sân chơi Marlowe] (https://play.marlowe-finance.io/#/) là môi trường hộp cát nơi bạn có thể thực hành viết hợp đồng tài chính của mình.
Sân chơi này cung cấp cho bạn sự lựa chọn làm việc trực tiếp trong một loạt các ngôn ngữ như chính Marlowe, [JavaScript] (https://play.marlowe-finance.io/doc/marlowe/tutorials/javascript-embedding.html), [Haskell
].
Sân chơi khối.html), tùy thuộc vào nơi bạn thích sử dụng.
Gần đây, chúng tôi đã thêm các tính năng mới vào Sân chơi Marlowe để xây dựng và chỉnh sửa các mẫu và tùy chỉnh siêu dữ liệu, cũng như tùy chọn tải xuống JSON mới cho chính các hợp đồng.
Trong bài đăng này, chúng tôi xem xét kỹ hơn về các tính năng mới này.

### **From contracts to templates**

### ** Từ hợp đồng đến mẫu **

With the introduction of Marlowe Run, we have extended the Marlowe Playground to support what we call *templates*. These *templates* are implemented using an extended version of Marlowe (known as Extended Marlowe, the version available in the Marlowe Playground). These new templates will mean users can easily reuse and repurpose contracts for different scenarios and contexts. 

Với việc giới thiệu Marlowe Run, chúng tôi đã mở rộng Sân chơi Marlowe để hỗ trợ những gì chúng tôi gọi là *Mẫu *.
Các * mẫu * này được triển khai bằng phiên bản mở rộng của Marlowe (được gọi là Marlowe mở rộng, phiên bản có sẵn trong Sân chơi Marlowe).
Các mẫu mới này sẽ có nghĩa là người dùng có thể dễ dàng sử dụng lại và tái sử dụng các hợp đồng cho các kịch bản và bối cảnh khác nhau.

Extended Marlowe offers greater flexibility than plain Marlowe (or Core Marlowe). Contracts are very concrete, and specify timeouts in absolute values, originally through slot numbers, and more recently using standardized timestamps (POSIX time).

Marlowe mở rộng cung cấp tính linh hoạt cao hơn so với Marlowe đơn giản (hoặc Marlowe cốt lõi).
Hợp đồng rất cụ thể và chỉ định thời gian chờ trong các giá trị tuyệt đối, ban đầu thông qua các số khe và gần đây hơn bằng cách sử dụng dấu thời gian tiêu chuẩn hóa (thời gian POSIX).

Additionally, Marlowe Values are typically hardcoded in Marlowe, except those passed as Inputs. For example, you can implement a loan for â‚³100 or one that asks the user how much to lend through a Choice in a When construct, but we could not have a reusable Marlowe contract that could be deployed at any time and with any given parameters. Extended Marlowe addresses these limitations by adding the option to include contract parameters. Currently, extended Marlowe is practically identical to plain Marlowe except in that it includes two extra constructors that represent *parameters* of the *template*:

Ngoài ra, các giá trị Marlowe thường được mã hóa cứng trong Marlowe, ngoại trừ các giá trị được truyền dưới dạng đầu vào.
Ví dụ: bạn có thể thực hiện một khoản vay cho
thông số.
Marlowe mở rộng giải quyết các hạn chế này bằng cách thêm tùy chọn để bao gồm các tham số hợp đồng.
Hiện tại, Marlowe mở rộng thực tế giống hệt với Marlowe đơn giản ngoại trừ ở chỗ nó bao gồm hai hàm tạo bổ sung đại diện cho *tham số *của mẫu * *:

- SlotParam â€” can be written in place of a timeout in a When construct

- slotparam - có thể được viết thay cho thời gian chờ trong khi xây dựng

- ConstantParam â€” is a type of Value construct

- ConstantParam - là một loại cấu trúc giá trị

Both constructors take, as their only parameter, a string that serves as an identifier for the parameter, for example:

Cả hai bộ xây dựng đều lấy, làm tham số duy nhất của chúng, một chuỗi đóng vai trò là mã định danh cho tham số, ví dụ:

- SlotParam "Payment deadline

- SlotParam "Hạn chót thanh toán

- ConstantParam "Price"

- Constantparam "Giá"

Two parameters of the same type (either SlotParam or ConstantParam) and with the same identifier are considered the same parameter, even if they appear in different places.

Hai tham số cùng loại (slotparam hoặc hằng số) và với cùng một định danh được coi là cùng một tham số, ngay cả khi chúng xuất hiện ở những nơi khác nhau.

If a contract contains parameters (in other words, if it is a *template*), then the user will be asked to input values for those parameters before starting a simulation of the contract, or before deploying the contract in Marlowe Run:

Nếu một hợp đồng chứa các tham số (nói cách khác, nếu đó là một mẫu * *), thì người dùng sẽ được yêu cầu nhập các giá trị cho các tham số đó trước khi bắt đầu mô phỏng hợp đồng hoặc trước khi triển khai hợp đồng trong Marlowe Run:

![](img/2022-03-04-diving-deeper-into-the-marlowe-playground.009.png)

Figure 1. Simulation dialog

Hình 1. Hộp thoại mô phỏng

Note that the value template parameter input in the picture is not just an integer input field. Rather, it expects a number with decimals, and it has a label with a currency symbol that indicates that the number expected represents an amount of ada. This rule is also true for values required through a Choice in a When construct. Also, choices do not need to represent amounts of ada. They can represent anything, like a ratio, as follows:

Lưu ý rằng đầu vào tham số mẫu giá trị trong hình không chỉ là trường nhập số nguyên.
Thay vào đó, nó mong đợi một số có số thập phân và nó có một nhãn có ký hiệu tiền tệ chỉ ra rằng số dự kiến đại diện cho một lượng ADA.
Quy tắc này cũng đúng với các giá trị cần thiết thông qua một lựa chọn trong khi xây dựng.
Ngoài ra, các lựa chọn không cần phải đại diện cho số lượng ADA.
Họ có thể đại diện cho bất cứ điều gì, như một tỷ lệ, như sau:

![](img/2022-03-04-diving-deeper-into-the-marlowe-playground.010.png)

Figure 2. Actions dialog

Hình 2. Hộp thoại hành động

There are also hints for each parameter that a user can display by clicking the purple question mark beside each term. Text in the hints is specific to the contract template, and it contains formatted text, for example, **bold text**, *text in italics*, or underlined text.

Ngoài ra còn có gợi ý cho từng tham số mà người dùng có thể hiển thị bằng cách nhấp vào dấu câu hỏi màu tím bên cạnh mỗi thuật ngữ.
Văn bản trong các gợi ý là cụ thể cho mẫu hợp đồng và nó chứa văn bản được định dạng, ví dụ: ** Văn bản in đậm **,*văn bản in nghiêng*hoặc văn bản được gạch chân.

![](img/2022-03-04-diving-deeper-into-the-marlowe-playground.011.png)

Figure 3. Parameter hints

Hình 3. Gợi ý tham số

User-defined contracts can customize all these details through the use of *metadata*. Letâ€™s take a look at how this is done.

Các hợp đồng do người dùng xác định có thể tùy chỉnh tất cả các chi tiết này thông qua việc sử dụng *siêu dữ liệu *.
Hãy xem xét cách thức này được thực hiện.

## **Customizing metadata**

## ** Siêu dữ liệu tùy chỉnh **

There is a *Metadata* tab at the bottom of each of the editors in the Marlowe Playground. There, users can customize the metadata as needed. For example: 

Có một tab * siêu dữ liệu * ở dưới cùng của mỗi biên tập viên trong sân chơi Marlowe.
Ở đó, người dùng có thể tùy chỉnh siêu dữ liệu khi cần thiết.
Ví dụ:

![](img/2022-03-04-diving-deeper-into-the-marlowe-playground.012.png)

Figure 4. Metadata tab

Hình 4. tab Siêu dữ liệu

There is some basic metadata that every contract is expected to include, such as:

Có một số siêu dữ liệu cơ bản mà mọi hợp đồng dự kiến sẽ bao gồm, chẳng hạn như:

- **Contract type** â€” What type of contract is it? This category will help classify contracts so that they are easier to find in the future. Currently, there are very few categories available, but we will add more in the future. If no category fits your contract, you can always choose â€œOtherâ€.

- ** Loại hợp đồng ** - Loại hợp đồng nào?
Danh mục này sẽ giúp phân loại các hợp đồng để chúng dễ tìm hơn trong tương lai.
Hiện tại, có rất ít danh mục có sẵn, nhưng chúng tôi sẽ thêm nhiều hơn trong tương lai.
Nếu không có danh mục phù hợp với hợp đồng của bạn, bạn luôn có thể chọn "điều khác.

- **Contract name** â€” Just a short name to identify the contract.

- ** Tên hợp đồng ** - Chỉ là một tên ngắn để xác định hợp đồng.

- **Contract short description** â€” A very brief description to show in listings.

- ** Hợp đồng Mô tả ngắn ** - Một mô tả rất ngắn gọn để hiển thị trong danh sách.

- **Contract long description** â€” A more detailed description that will be shown following the short description in cases when the user has already selected the template and wants to know more (for example, when creating a contract in Marlowe Run).

- ** Hợp đồng Mô tả dài
.

Note that the text in descriptions supports using some of the formatting functionality included in Markdown. For example, adding two asterisks before and after a part of the text of a description will make that text appear in bold when simulating the contract, as we saw in the previous section. In this way the plain text:

Lưu ý rằng văn bản trong các mô tả hỗ trợ bằng cách sử dụng một số chức năng định dạng có trong Markdown.
Ví dụ: thêm hai dấu sao trước và sau một phần của văn bản mô tả sẽ làm cho văn bản đó xuất hiện in đậm khi mô phỏng hợp đồng, như chúng ta đã thấy trong phần trước.
Theo cách này, văn bản đơn giản:

Amount of \*\*money\*\* to pay

Số tiền \*\*tiền \*\*để trả

will be rendered as

sẽ được hiển thị là

Amount of **money** to pay

Số tiền ** tiền ** để trả

We recommend using this functionality to highlight which keywords represent entities that have special meaning in the context of the contract, like names of roles or choices, for example.

Chúng tôi khuyên bạn nên sử dụng chức năng này để làm nổi bật các từ khóa nào đại diện cho các thực thể có ý nghĩa đặc biệt trong bối cảnh hợp đồng, như tên của vai trò hoặc lựa chọn chẳng hạn.

The metadata tab also supports specifying hints for the roles, choices, slot, and value parameters defined in the contract, as well as formatting for choices and value parameters.

Tab Siêu dữ liệu cũng hỗ trợ chỉ định các gợi ý cho vai trò, lựa chọn, vị trí và các tham số giá trị được xác định trong hợp đồng, cũng như định dạng cho các lựa chọn và tham số giá trị.

A new role or choice, slot, or value parameter added to a contract will appear in the Metadata tab in red. In the case of the Haskell and JavaScript editors, it may be necessary to compile the code successfully before this happens.

Một vai trò hoặc lựa chọn mới, vị trí hoặc tham số giá trị được thêm vào hợp đồng sẽ xuất hiện trong tab Siêu dữ liệu màu đỏ.
Trong trường hợp của các biên tập viên Haskell và JavaScript, có thể cần phải biên dịch mã thành công trước khi điều này xảy ra.

![](img/2022-03-04-diving-deeper-into-the-marlowe-playground.013.png)

Figure 5. Metadata tab - adding metadata entries

Hình 5. Tab Siêu dữ liệu - Thêm mục nhập siêu dữ liệu

Pressing the red â€œ+â€ button will create a new metadata entry for the given item. In the same way, if a role, choice, or slot or value parameter stops being used in the contract, the existing metadata will be flagged in red for deletion, and the user must press the â€œ-â€ button to delete the metadata entry from the contract.

Nhấn nút Đỏ -+ - nút sẽ tạo một mục siêu dữ liệu mới cho mục đã cho.
Theo cách tương tự, nếu một vai trò, lựa chọn hoặc tham số giá trị hoặc giá trị dừng được sử dụng trong hợp đồng, siêu dữ liệu hiện có sẽ được gắn cờ màu đỏ để xóa và người dùng phải nhấn nút "
Mục nhập siêu dữ liệu từ hợp đồng.

![](img/2022-03-04-diving-deeper-into-the-marlowe-playground.014.png)

Figure 6. Metadata tab - deleting metadata entries

Hình 6. Tab Siêu dữ liệu - Xóa các mục nhập siêu dữ liệu

In addition to the description, in the cases of choices and value parameters, a user can optionally specify a formatting for the number that they want the end user to provide. To do that, select â€œFixed point amountâ€ from the dropdown menu. This will provide two extra fields:

Ngoài mô tả, trong các trường hợp lựa chọn và tham số giá trị, người dùng có thể tùy ý chỉ định định dạng cho số mà họ muốn người dùng cuối cung cấp.
Để làm điều đó, chọn số lượng điểm đã giảm dần từ menu thả xuống.
Điều này sẽ cung cấp hai trường bổ sung:

- **Number of decimal digits for value** (bottom left) â€” numbers in Marlowe are internally always integers, but for convenience, users can input numbers as fixed-point. For example, Marlowe amounts of ada are represented in lovelace (a millionth of an ada) but, in general, end users prefer to work with amounts of ada (since they are more readable). Developers can support this by writing 6 in the number of decimal places. As a result, the end user will see a decimal separator in the 6th position, even though internally the contract still works with lovelace (ada units).

- ** Số chữ số thập phân cho giá trị ** (dưới cùng bên trái) Các số trong Marlowe luôn là số nguyên, nhưng để thuận tiện, người dùng có thể nhập số dưới dạng điểm cố định.
Ví dụ, số lượng ADA của Marlowe được thể hiện bằng Lovelace (một phần triệu của ADA), nhưng nói chung, người dùng cuối thích làm việc với số lượng ADA (vì chúng dễ đọc hơn).
Các nhà phát triển có thể hỗ trợ điều này bằng cách viết 6 ở số lượng thập phân.
Do đó, người dùng cuối sẽ thấy dấu phân cách thập phân ở vị trí thứ 6, mặc dù bên trong hợp đồng vẫn hoạt động với Lovelace (đơn vị ADA).

- **Currency label for the value** (bottom right) â€” developers can also present a currency symbol near the input box of the value as a hint to end users about the unit of the amount that we expect from them. For example, in the case of ada, just write the ada symbol â€œâ‚³â€.

- ** Nhãn tiền tệ cho giá trị ** (dưới cùng bên phải) - Các nhà phát triển cũng có thể trình bày một ký hiệu tiền tệ gần hộp đầu vào của giá trị như một gợi ý cho người dùng cuối về đơn vị của số tiền mà chúng tôi mong đợi từ chúng.
Ví dụ, trong trường hợp của ADA, chỉ cần viết biểu tượng ADA - œâ œâ € €.

![](img/2022-03-04-diving-deeper-into-the-marlowe-playground.015.png)

Figure 7. Number formatting

Hình 7. Định dạng số

Finally, the order of parameters is important. For example, imagine several slot parameters for the end user to choose. It would be logical to display those parameters in chronological order.

Cuối cùng, thứ tự của các tham số là quan trọng.
Ví dụ, hãy tưởng tượng một số tham số khe để người dùng cuối chọn.
Sẽ là hợp lý khi hiển thị các tham số theo thứ tự thời gian.

To arrange the metadata, drag entries into the desired order, for example:

Để sắp xếp siêu dữ liệu, ví dụ như kéo các mục vào thứ tự mong muốn:

![](img/2022-03-04-diving-deeper-into-the-marlowe-playground.016.png)

Figure 8. Metadata ordering

Hình 8. Đặt hàng siêu dữ liệu

The order of the parameters in the metadata will be used for generating the form shown at the beginning of the simulation or execution of the contract.

Thứ tự của các tham số trong siêu dữ liệu sẽ được sử dụng để tạo biểu mẫu được hiển thị khi bắt đầu mô phỏng hoặc thực hiện hợp đồng.

# **Conclusion**

# **Sự kết luận**

With the new template and metadata extensions to Marlowe, contract developers can now provide hints and parameters to make it easier for end users to reuse the same contract in several circumstances, without having to understand the full implementation and the details of the contract.

Với các phần mở rộng mẫu và siêu dữ liệu mới cho Marlowe, các nhà phát triển hợp đồng giờ đây có thể cung cấp các gợi ý và tham số để giúp người dùng cuối dễ dàng sử dụng lại hợp đồng tương tự trong một số trường hợp, mà không phải hiểu toàn bộ và chi tiết hợp đồng.

These are just some of the new improvements that the Marlowe team continues to work on, and we look forward to sharing the details of more enhancements soon.

Đây chỉ là một số cải tiến mới mà nhóm Marlowe tiếp tục làm việc và chúng tôi mong muốn được chia sẻ chi tiết về các cải tiến nhiều hơn sớm.

*To find out more about upcoming Marlowe releases and new features, keep an eye on our social media channels or the new [Marlowe Discord channel](https://discord.com/channels/826816523368005654/936295815926927390/936316494042779698) for more information. Also, stay tuned for details about our first Marlowe Pioneers Program launching soon!*

*Để tìm hiểu thêm về các bản phát hành sắp tới của Marlowe và các tính năng mới, hãy để mắt đến các kênh truyền thông xã hội của chúng tôi hoặc [Kênh Disc của Marlowe] (https://discord.com/channels/82681652368005654/936295815926
Ngoài ra, hãy theo dõi để biết chi tiết về chương trình Tiên phong Marlowe đầu tiên của chúng tôi sẽ sớm ra mắt!*

