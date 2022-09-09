# Các bài kiểm tra thuộc tính đơn giản cho trình xác thực Plutus

### **Cách viết mã off-chain với thư viện 'cook-validators' và nhận các bài kiểm tra thuộc tính đơn giản một cách miễn phí**

![](img/2022-01-27-simple-property-based-tests-for-plutus-validators.002.png) 27 January 2022![](img/2022-01-27-simple-property-based-tests-for-plutus-validators.002.png)[ Victor Cacciari Miraldo](/en/blog/authors/victor-miraldo/page-1/)![](img/2022-01-27-simple-property-based-tests-for-plutus-validators.003.png) 8 mins read

![Victor Cacciari Miraldo](img/2022-01-27-simple-property-based-tests-for-plutus-validators.004.jpeg)[](/en/blog/authors/victor-miraldo/page-1/)

### [**Victor Cacciari Miraldo**](/en/blog/authors/victor-miraldo/page-1/)

Software Engineer

![Simple property-based tests for Plutus validators](img/2022-01-27-simple-property-based-tests-for-plutus-validators.005.jpeg)

*Gần đây, chúng tôi đã nghe [Victor Miraldo](https://victorcmiraldo.github.io/) , người đứng đầu nhóm kiểm toán và xác minh hợp đồng thông minh tại [Tweag](https://www.tweag.io/) trình bày về tầm quan trọng của việc xác minh vì lý do bảo mật trong thế giới tài chính phi tập trung (DeFi). Victor là kỹ sư về các giải pháp đến từ ngôn ngữ lập trình Haskell và cam kết đảm bảo tính an toàn, chính xác của các ứng dụng phi tập trung (DApps) thông qua các công cụ và quy trình. Trong bài này, anh ấy đề cập đến việc viết và triển khai DApp theo cách đơn giản là chưa đủ, và tại sao mọi nhà phát triển nên kiểm tra thật kỹ tất cả mã on-chain và tập lệnh Plutus để ngăn chặn và loại bỏ các tác nhân xấu. Vì vậy, anh ấy giới thiệu một thư viện các công cụ sẵn có để tương tác với các tập lệnh của trình xác thực Plutus - được gọi là [cooked-validators](https://github.com/tweag/plutus-libs/tree/main/cooked-validators) , được phát triển tại Tweag. Thư viện này giúp triển khai layer ở phía trong cùng cho mã của off-chain, nó chịu trách nhiệm tạo và gửi các giao dịch. Bằng cách sử dụng thư viện này, bạn có thể nhận các bài kiểm tra thuộc tính đơn giản ở cấp độ giao dịch một cách miễn phí.*

*Let's hear what Victor had to say about using their library.*

## **Introduction**

Transaction-level tests enable us to submit arbitrary transactions to the validator scripts and to assess their behavior. This process differs from testing a whole smart contract using the defined endpoints as part of the off-chain code of the contract. After all, that off-chain code was designed to seamlessly cooperate with the on-chain code and will have its own intrinsic security and safety checks. This method works for normal operations, but in a testing setup, it often shields on-chain validator scripts from ill-formed or even malicious inputs. Therefore, for transaction-level testing, we want to circumvent the sanitising off-chain code and hammer on-chain scripts with all the same might that an attackerâ€™s hand-crafted off-chain infrastructure might bring. As an analogy with web services, you often want to test your server by sending it arbitrary requests, in addition to those requests that are permitted by the client's user interface.

The cooked-validators library enables you to write the off-chain code responsible for generating and submitting transactions and use the same code for executing and testing your contract, at the transaction-level. This makes it much easier to write tests for the on-chain that can detect whether a number of bad things can or cannot happen.

## **About the 'cooked-validators' library**

Việc xây dựng hợp đồng của bạn với cooked-validators không khác nhiều so với những gì bạn đã quen với Hợp đồng đơn nguyên. Giả sử bạn đã làm theo [hướng dẫn về Hợp đồng phân tách](https://plutus-apps.readthedocs.io/en/latest/plutus/tutorials/basic-apps.html#defining-the-validator-script) bao gồm phần 'Xác định tập lệnh trình xác thực'. Cuối cùng, bạn có một hàm [splitValidator](https://github.com/tweag/plutus-libs/blob/30f4c061cc8d38e5968bbb6418b40a6f4e9e25fa/examples/src/Split.hs) thực thi phần *on-chain* của hợp đồng đó. Nếu bạn không làm theo hướng dẫn, hợp đồng splitValidator sẽ khóa một lượng tiền nhất định mà chỉ có thể mở được bằng cách chia tiền cho cả hai bên đã được chỉ định từ trước.

Now, to interact with that contract itself, we need to write the *off-chain* code, which generates and sends the necessary transactions to the blockchain. Instead of doing that directly in the Contract monad, we'll rely on the cooked-validators library. The [lockFunds](https://plutus-apps.readthedocs.io/en/latest/plutus/tutorials/basic-apps.html#locking-the-funds) transaction can be written as follows:

lockFunds :: (MonadBlockChain m) =&gt; SplitData -&gt; m ()

lockFunds s@SplitData{amount} = void $ validateTxConstr

`  `[PaysScript splitValidator [(datum, Ada.toValue amount)]]

This is very similar to the [lockFunds](https://plutus-apps.readthedocs.io/en/latest/plutus/tutorials/basic-apps.html#locking-the-funds) we'd have written in the Contract monad directly. The difference being that here we used an arbitrary [MonadBlockChain](https://github.com/tweag/plutus-libs/blob/30f4c061cc8d38e5968bbb6418b40a6f4e9e25fa/cooked-validators/src/Cooked/MockChain/Monad.hs#L45) monad. This technique enables us to use the same lockFunds for two purposes:

1. Tạo giao dịch, vì Hợp đồng đơn nguyên là một bản sao của MonadBlockChain, và
2. Viết các bài kiểm tra cho các trình xác nhận *on-chain* bằng cách sử dụng cơ sở là cooked-validators.

Giả sử rằng chúng tôi cũng đã xác định các giao dịch unlockFunds ([mã để sử dụng](https://github.com/tweag/plutus-libs/blob/30f4c061cc8d38e5968bbb6418b40a6f4e9e25fa/examples/src/Split/OffChain.hs#L54)), để cooked-validators sẽ tương tác liền mạch với Hợp đồng đơn nguyên. Trên thực tế, chúng ta có thể định nghĩa hàm endpoints giống như trong [hướng dẫn](https://plutus-apps.readthedocs.io/en/latest/plutus/tutorials/basic-apps.html#deploying-the-app-on-the-playground) :

endpoints :: (AsContractError e) =&gt; Promise w SplitSchema e ()

endpoints = selectList [lock, unlock]

`  `where

`    `lock = endpoint @"lock" (lockFunds . mkSplitData)

`    `unlock = endpoint @"unlock" (const unlockFunds)

## **Testing the contract**

Bởi vì chúng tôi đã xác định layer đầu tiên của mã off-chain của chúng tôi (tạo và gửi các giao dịch thô) với cooked-validators, chúng tôi có thể sử dụng cơ sở hạ tầng thử nghiệm của nó để kiểm tra trình xác thực *on-chain*. Một bài kiểm tra cơ bản về việc có thể mở các khoản tiền đã bị khóa hay không được viết như sau:

unlockPossible1 = assertSucceeds $ do

`  `lockFunds sd `as` wallet 1 -- sends the lockFunds pretending to be user 1,

`  `unlockFunds `as` wallet 2 -- sends the unlockFunds pretending to be user 2.

where

`  `-- makes a split of 10 ada between users 2 and 3 that only those users should be able to unlock.

`  `sd = SplitData (wallet 2) (wallet 3) 10

Here, the as combinator only works when testing code and it enables us to interact with our contract in the same way as many users would.

Chức năng unlockPossible1 là một đơn vị để kiểm tra xem có điều gì tốt xảy ra hay không. Chúng tôi có thể dễ dàng kiểm tra xem có điều gì đó tồi tệ *không* xảy ra không:

unlockImpossible1 = assertFails $ do

`  `lockFunds sd `as` wallet 1

`  `unlockFunds `as` wallet 5 -- user 5 shouldn't be able to unlock the funds.

where

`  `sd = SplitData (wallet 2) (wallet 3) 10

Chúng tôi cũng có thể sử dụng các bài kiểm tra này như các bài *kiểm tra thuộc tính đơn giản*. Trong trường hợp này, thuộc tính đang được kiểm tra là một trong hai người nhận phân tách luôn luôn có thể mở khóa:

unlockProp1 = forAllTr tr assertSucceeds

`  `where

`    `tr = do

`      `-- generates a random SplitData

`      `sd &lt;- genSplitData

`      `-- generates a random wallet; anyone can lock funds.

`      `w &lt;- genArbitraryWallet

`      `lockFunds sd `as` w

`      `-- but only the recipients can unlock the funds

`      `unlocker &lt;- choose [ recipient1 params , recipient2 params ]

`      `unlockFunds `as` unlocker

Additionally, if one of our tests fails, we will receive a readable summary of the transactions that caused the test to fail. Here's an excerpt of the first three transactions from a test failure of a more involved validator:

\1) ValidateTxSkel

`     `- Signers: [wallet #1 (a2c20c)]

`     `- Label: ProposalSkel 2(Payment{paymentAmount = 4200000,paymentRecipient = a96a66})

`     `- Constraints:

`        `/\ Mints

`            `- (18ab4cc $ "threadToken"): 1

`            `- Policies: [18ab4c]

`        `/\ PaysScript script 9d52e00:

`            `- Accumulator{payment = Payment{paymentAmount = 4200000,paymentRecipient = a96a66},signees = []}

`              `{ Lovelace: 6200000

`                `(18ab4cc $ "threadToken"): 1 }

\2) ValidateTxSkel

`     `- Signers: [wallet #1 (a2c20c)]

`     `- Constraints:

`        `/\ PaysScript script 9d52e00:

`            `- Sign{signPk = a2c20c,signSignature = 8fef22}

`              `Lovelace: 1

\3) ValidateTxSkel

`     `- Signers: [wallet #2 (80a4f4)]

`     `- Constraints:

`        `/\ PaysScript script 9d52e00:

`            `- Sign{signPk = 80a4f4,signSignature = 6853e0}

`              `Lovelace: 1

...

The trace that is displayed to the developer contains all the information necessary to debug the issue, and it tries to present the information in a readable manner.

Ngoài kiểm tra thuộc tính đơn giản, cooked-validators cũng cung cấp khả năng sửa đổi các giao dịch dựa vào theo dõi một số chức năng. Điều này có thể mô phỏng một cuộc tấn công theo nhiều cách khác nhau. Ví dụ, viết một bài kiểm tra như:

attackNotPossibleOnSplit = assertFails $ do

`  `somewhere doAttack $ do

`    `lockFunds sd `as` wallet 1

`    `unlockFunds `as` wallet 2

` `where

`  `sd = SplitData (wallet 2) (wallet 3) 10

will cause cooked-validators to attempt to execute two tests, both of which should fail, as follows:

1. Sửa đổi giao dịch sd lockFunds theo doAttack và gửi; sau đó gửi một unlockFunds không sửa đổi hoặc
2. Gửi sd lockFunds; sau đó sửa đổi và gửi unlockFunds theo doAttack.

The details of the somewhere combinator can get a little complex, hence we will omit it here. There is a separate [blog post](https://www.tweag.io/blog/2022-01-26-property-based-testing-of-monadic-code) giving the technical details on the Tweag blog for those who are interested.

## **Related libraries and conclusion**

Mặc dù Plutus [đã hỗ trợ](https://plutus-pioneer-program.readthedocs.io/en/latest/pioneer/week8.html#property-based-testing) một hình thức kiểm tra thuộc tính đơn giản của các điểm kết thúc hợp đồng (endpoints) với lớp [ContractModel](https://marlowe-playground-staging.plutus.aws.iohkdev.io/doc/haddock/plutus-contract/html/Plutus-Contract-Test-ContractModel.html) của nó, nó không cung cấp kiểm tra ở cấp độ giao dịch. Kiểm tra cấp độ giao dịch là rất quan trọng đối với chúng tôi tại Tweag. Khi kiểm tra một hợp đồng Plutus, chúng ta cần có khả năng hoạt động như một kẻ tấn công và sửa đổi các giao dịch để nghiên cứu cách những người xác nhận sẽ phản ứng.

Bằng cách sử dụng cooked-validators để phát triển mã off-chain của bạn, bạn có thể tự kiểm tra nhiều thuộc tính an toàn và chính xác của mã on-chain và điều này có thể làm tăng đáng kể sự tin tưởng vào tính đúng đắn của mã. Điều đó có thể tiết kiệm thời gian và tiền bạc trong quá trình kiểm tra. Trên thực tế, bước đầu tiên của quá trình kiểm tra Tweag là viết mã tạo giao dịch bằng cách sử dụng cooked-validators, để sau đó có thể tương tác với cơ sở hạ tầng của chúng tôi một cách tự do.<br><br><br>Bài này được dịch bởi Max Long <a class="_active_edit_href" href="https://iohk.io/en/blog/posts/2022/01/27/simple-property-based-tests-for-plutus-validators/">với bài gốc</a><br>*Dự án này được tài trợ bới Catalyst*
