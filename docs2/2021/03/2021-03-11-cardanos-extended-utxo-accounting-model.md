# Cardano’s Extended UTXO accounting model – built to support multi-assets and smart contracts
### **Cardano uses an innovative Extended UTXO accounting model to support multi-assets and smart contracts. In the first of a two-part blog, we look at the different blockchain accounting systems and why EUTXO matters**
![](img/2021-03-11-cardanos-extended-utxo-accounting-model.002.png) 11 March 2021![](img/2021-03-11-cardanos-extended-utxo-accounting-model.002.png)[ Fernando Sanchez](tmp//en/blog/authors/fernando-sanchez/page-1/)![](img/2021-03-11-cardanos-extended-utxo-accounting-model.003.png) 5 mins read

![Fernando Sanchez](img/2021-03-11-cardanos-extended-utxo-accounting-model.004.png)[](tmp//en/blog/authors/fernando-sanchez/page-1/)
### [**Fernando Sanchez**](tmp//en/blog/authors/fernando-sanchez/page-1/)
Technical Writer

Marketing and Communications

- ![](img/2021-03-11-cardanos-extended-utxo-accounting-model.005.png)[](mailto:fernando.sanchez@iohk.io "Email")
- ![](img/2021-03-11-cardanos-extended-utxo-accounting-model.006.png)[](https://www.linkedin.com/in/linkedinsanchezf/ "LinkedIn")

![Cardano’s Extended UTXO accounting model – built to support multi-assets and smart contracts](img/2021-03-11-cardanos-extended-utxo-accounting-model.007.jpeg)

Blockchain networks are complex data structures. Transactions continuously crisscross the chain, creating digital footprints that require careful tracking and management to maintain the integrity and reliability of the underlying ledger.

Mạng Blockchain là cấu trúc dữ liệu phức tạp.
Các giao dịch liên tục vượt qua chuỗi, tạo ra các dấu chân kỹ thuật số đòi hỏi phải theo dõi và quản lý cẩn thận để duy trì tính toàn vẹn và độ tin cậy của sổ cái cơ bản.

Two major accounting ledgers exist in the blockchain space: UTXO-based blockchains (Bitcoin, for instance), and Account/Balance chains (Ethereum, and others).

Hai sổ cái kế toán chính tồn tại trong không gian blockchain: blockchain dựa trên UTXO (ví dụ, Bitcoin) và chuỗi tài khoản/số dư (Ethereum và các chuỗi khác).

Each of these crypto heavyweights differs in many fundamental ways, but this article focuses on their accounting models. Bitcoin uses an Unspent Transaction Output (UTXO) model, whereas Ethereum deploys an Account/Balance one.

Mỗi đối thủ nặng ký của Crypto khác nhau theo nhiều cách cơ bản, nhưng bài viết này tập trung vào các mô hình kế toán của họ.
Bitcoin sử dụng mô hình đầu ra giao dịch UNSPENT (UTXO), trong khi Ethereum triển khai tài khoản/số dư.

Cardano sought to combine Bitcoin’s UTXO model with Ethereum’s ability to handle smart contracts into an Extended UTXO (EUTXO) accounting model. The adoption of EUTXO facilitates the implementation of smart contracts into the Cardano chain.

Cardano đã tìm cách kết hợp mô hình Bitcoin từ UTXO với khả năng Ethereum, để xử lý các hợp đồng thông minh thành mô hình kế toán UTXO (EUTXO) mở rộng.
Việc áp dụng EUTXO tạo điều kiện cho việc thực hiện các hợp đồng thông minh vào chuỗi Cardano.

### **What is a blockchain accounting model?**

### ** Mô hình kế toán blockchain là gì? **

Every company, firm, or commercial entity requires a balance sheet to keep an accurate record of profit, loss, cash flow, and other parameters. By maintaining careful accounting of all this data, companies can, at a glance, visualize their financial status at any given point in time. A company's accounting ledger offers another advantage: The ability to trace the provenance and ownership of funds.

Mỗi công ty, công ty hoặc thực thể thương mại yêu cầu một bảng cân đối kế toán để giữ một hồ sơ chính xác về lợi nhuận, lỗ, dòng tiền và các thông số khác.
Bằng cách duy trì kế toán cẩn thận của tất cả các dữ liệu này, các công ty có thể, trong nháy mắt, hình dung tình trạng tài chính của họ tại bất kỳ thời điểm nào.
Sổ cái kế toán của một công ty cung cấp một lợi thế khác: khả năng theo dõi nguồn gốc và quyền sở hữu vốn.

Blockchain networks also require an accounting model to determine who owns what coins (and how many of them), track where those coins go, which ones are used up, and which ones remain available to be spent.

Các mạng Blockchain cũng yêu cầu một mô hình kế toán để xác định ai sở hữu những đồng tiền nào (và bao nhiêu trong số chúng), theo dõi nơi những đồng tiền đó đi, cái nào được sử dụng và cái nào vẫn có sẵn để chi tiêu.

### **UTXO model v Account/Balance model: A brief overview**

### ** UTXO Model V Tài khoản/Mô hình cân bằng: Tổng quan ngắn gọn **

Decades ago, accountants used physical ledger books with handwritten entries to keep records about the movement of funds. Nowadays, companies use electronic versions of the same thing. Blockchains use transactions as records (much like entries on a ledger book) to track provenance and ownership. These transactions contain a lot of information (where the coins come from, where they're going, and whatever change is leftover from these transactions). 

Nhiều thập kỷ trước, kế toán đã sử dụng sách sổ cái vật lý với các mục viết tay để lưu giữ hồ sơ về sự chuyển động của các quỹ.
Ngày nay, các công ty sử dụng các phiên bản điện tử của cùng một thứ.
Blockchains sử dụng các giao dịch làm hồ sơ (giống như các mục trên một cuốn sách sổ cái) để theo dõi nguồn gốc và quyền sở hữu.
Các giao dịch này chứa rất nhiều thông tin (nơi các đồng tiền đến, nơi chúng sẽ đến và bất kỳ thay đổi nào còn sót lại từ các giao dịch này).

Here’s a brief overview of the UTXO and Account/Balance models:

Tại đây, một tổng quan ngắn gọn về các mô hình UTXO và tài khoản/cân bằng:

### **UTXO**

### ** utxo **

In a UTXO model, the movement of assets is recorded in the form of a directed acyclic graph where the nodes are transactions and the edges are transaction outputs, where each additional transaction consumes some of the UTXOs and adds new ones. The users' wallets keep track of a list of unspent outputs associated with all addresses owned by the user, and calculate the users’ balance.

Trong mô hình UTXO, chuyển động của tài sản được ghi lại dưới dạng biểu đồ Acyclic có hướng trong đó các nút là giao dịch và các cạnh là đầu ra giao dịch, trong đó mỗi giao dịch bổ sung tiêu thụ một số UTXOS và thêm các giao dịch mới.
Ví của người dùng theo dõi danh sách các đầu ra chưa được liên kết với tất cả các địa chỉ thuộc sở hữu của người dùng và tính toán số dư của người dùng.

UTXO is, in many ways, similar to cash. A good analogy is this: Imagine you have $50 in your wallet. This amount could be made up with several combinations: two $20 bills and one $10, four $10 bills and two $5 bills, and many others. But regardless of the permutations, the amount ($50) remains equal. UTXOs work in the same way. Whatever balance you have in your blockchain wallet (say, 150 coins) could be made up with many different UTXO combinations, based on previous transactions, but the balance amount remains the same. In other words, the balance held in a given wallet address is the sum of all unspent UTXOs from previous transactions.

UTXO, theo nhiều cách, tương tự như tiền mặt.
Một sự tương tự tốt là thế này: Hãy tưởng tượng bạn có $ 50 trong ví của mình.
Số tiền này có thể được tạo thành với một số kết hợp: hai hóa đơn 20 đô la và một đô la 10 đô la, bốn hóa đơn 10 đô la và hai hóa đơn 5 đô la, và nhiều hóa đơn khác.
Nhưng bất kể các hoán vị, số tiền ($ 50) vẫn bằng nhau.
UTXOS làm việc theo cùng một cách.
Bất cứ số dư nào bạn có trong ví blockchain của mình (giả sử, 150 đồng xu) có thể được tạo thành với nhiều kết hợp UTXO khác nhau, dựa trên các giao dịch trước đó, nhưng số lượng cân bằng vẫn giữ nguyên.
Nói cách khác, số dư được giữ trong một địa chỉ ví nhất định là tổng của tất cả các UTXO chưa sử dụng từ các giao dịch trước đó.

### **The concept of 'change' in UTXO models**

### ** Khái niệm 'thay đổi' trong các mô hình UTXO **

Much like cash transactions in any store, UTXOs introduce ‘change.’ When you take out say a $50 bill from your wallet, you cannot tear that bill into smaller pieces to pay for something that costs $15, for example. You have to hand over the entire $50 bill and receive your change from the cashier. UTXOs work in the same way. You cannot ‘split’ a UTXO into smaller bits. UTXOs are used whole, and change given back to your wallet’s address in the form of a smaller UTXO.

Giống như các giao dịch tiền mặt trong bất kỳ cửa hàng nào, UTXOS giới thiệu ‘Thay đổi. Khi bạn nhận ra một hóa đơn 50 đô la từ ví của mình, bạn không thể xé hóa đơn đó thành các phần nhỏ hơn để trả cho một cái gì đó có giá 15 đô la, ví dụ.
Bạn phải bàn giao toàn bộ hóa đơn 50 đô la và nhận được sự thay đổi của bạn từ nhân viên thu ngân.
UTXOS làm việc theo cùng một cách.
Bạn không thể chia một UTXO thành các bit nhỏ hơn.
UTXO được sử dụng toàn bộ và thay đổi được đưa trở lại địa chỉ ví của bạn dưới dạng UTXO nhỏ hơn.

### **The advantages of UTXO models**

### ** Ưu điểm của các mô hình UTXO **

By checking and tracking the size, age, and amount of UTXOs being transferred around, one can extract accurate metrics about the blockchain’s usage and financial activity of the chain.

Bằng cách kiểm tra và theo dõi kích thước, tuổi tác và số lượng UTXO được chuyển giao xung quanh, người ta có thể trích xuất các số liệu chính xác về việc sử dụng blockchain và hoạt động tài chính của chuỗi.

UTXO models offer other advantages. Better scalability and privacy, for example. Also, the transaction logic is simplified, as each UTXO can only be consumed once and as a whole, which makes transaction verification much simpler.

Các mô hình UTXO cung cấp các lợi thế khác.
Khả năng mở rộng và quyền riêng tư tốt hơn, ví dụ.
Ngoài ra, logic giao dịch được đơn giản hóa, vì mỗi UTXO chỉ có thể được tiêu thụ một lần và nói chung, điều này làm cho xác minh giao dịch đơn giản hơn nhiều.

To sum UTXO up:

Để tổng hợp utxo lên:

- A UTXO is the output of a previous transaction, which can be spent in the future

- UTXO là đầu ra của một giao dịch trước đó, có thể được sử dụng trong tương lai

- UTXO chains have no accounts. Instead, coins are stored as a list of UTXOs, and transactions are created by consuming existing UTXOs and producing new ones in their place

- Chuỗi UTXO không có tài khoản.
Thay vào đó, các đồng tiền được lưu trữ dưới dạng danh sách UTXO và các giao dịch được tạo ra bằng cách tiêu thụ UTXO hiện có và sản xuất những cái mới ở vị trí của chúng

- Balance is the sum of UTXOs controlled by a given address

- Số dư là tổng UTXOS được kiểm soát bởi một địa chỉ nhất định

- UTXOs resemble cash in that they use ‘change’, and are indivisible (UTXOs are used whole)

- UTXOS giống với tiền mặt ở chỗ họ sử dụng ‘thay đổi, và không thể chia cắt (UTXO được sử dụng toàn bộ)

### **The Account/Balance model**

### ** Mô hình tài khoản/số dư **

As the name indicates, blockchain models that deploy an Account/Balance accounting model use an account (which can be controlled by a private key or a smart contract) to hold a coin balance. In this model, assets are represented as balances within users’ accounts, and the balances are stored as a global state of accounts, kept by each node, and updated with every transaction.

Như tên chỉ ra, các mô hình blockchain triển khai mô hình kế toán tài khoản/số dư sử dụng tài khoản (có thể được kiểm soát bởi khóa riêng hoặc hợp đồng thông minh) để giữ số dư tiền xu.
Trong mô hình này, các tài sản được thể hiện dưới dạng số dư trong tài khoản của người dùng và số dư được lưu trữ dưới dạng trạng thái tài khoản toàn cầu, được giữ bởi mỗi nút và được cập nhật với mỗi giao dịch.

In many respects, Account/Balance chains (such as Ethereum) operate in a similar fashion to traditional bank accounts. The wallet's balance increases when coins are deposited, and decreases when coins are transferred elsewhere. The crucial difference here is that, unlike UTXOs, you can use your balance partially. So for example, if you have 100 ETH in your account, you can send a portion of that (say, 30 ETH) to someone else. The resulting balance will be 70 ETH remaining in your account, and the address where you sent the coins to will increase by 30 ETH. The concept of change does not apply in Account/Balance accounting models as it does in UTXO ones.

Trong nhiều khía cạnh, chuỗi tài khoản/số dư (như Ethereum) hoạt động theo cách tương tự như các tài khoản ngân hàng truyền thống.
Số dư của ví tăng khi tiền gửi và giảm khi tiền được chuyển đi nơi khác.
Sự khác biệt quan trọng ở đây là, không giống như UTXOS, bạn có thể sử dụng số dư của mình một phần.
Vì vậy, ví dụ, nếu bạn có 100 ETH trong tài khoản của mình, bạn có thể gửi một phần của điều đó (giả sử, 30 ETH) cho người khác.
Số dư kết quả sẽ là 70 ETH còn lại trong tài khoản của bạn và địa chỉ mà bạn đã gửi các đồng tiền sẽ tăng thêm 30 ETH.
Khái niệm thay đổi không áp dụng trong các mô hình kế toán tài khoản/số dư như trong UTXO.

To sum up the Account/Balance model:

Để tổng hợp mô hình tài khoản/số dư:

- This accounting model resembles how a bank operates

- Mô hình kế toán này giống như cách một ngân hàng hoạt động

- Users have accounts that hold their coin balance

- Người dùng có tài khoản giữ số dư tiền xu của họ

- It is possible to spent partial balances

- Có thể dành số dư một phần

- The concept of change does not apply

- Khái niệm thay đổi không áp dụng

Tomorrow, in the second part of this analysis, we'll discuss how each model deals with transactions, explain the rationale for developing the EUTXO model for Cardano, and provide an in-depth explanation of what EUTXO is and how it works.

Ngày mai, trong phần thứ hai của phân tích này, chúng tôi sẽ thảo luận về cách mỗi mô hình liên quan đến các giao dịch, giải thích cơ sở lý luận để phát triển mô hình EUTXO cho Cardano và đưa ra lời giải thích chuyên sâu về EUTXO là gì và hoạt động của nó.

