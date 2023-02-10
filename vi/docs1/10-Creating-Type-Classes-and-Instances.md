---
jupyter:
  celltoolbar: trình chiếu
  kernelspec:
    display_name: Haskell
    language: haskell
    name: haskell
  language_info:
    codemirror_mode: ihaskell
    file_extension: ".hs"
    mimetype: văn bản/x-haskell
    name: haskell
    pygments_lexer: Haskell
    version: 8.10.7
  nbformat: '4'
  nbformat_minor: '4'
  vscode:
    interpreter:
      hash: 31f2aee4e71d21fbe5cf8b01ff0e069b9275f58929596ceb00d14d90e3e16cd6
---

# Tạo các lớp và trường hợp loại

## Đề cương

- quá tải
- Các bước để tạo Type Classes và Instances
- Lớp loại `Eq`
    - Xác định loại lớp
    - Xác định nhiều trường hợp
    - Cải thiện lớp loại `Eq` của chúng tôi với đệ quy lẫn nhau (và MCD)
    - Xác định một thể hiện cho một loại tham số.
- Lớp loại `WeAccept`
- Lớp loại `Container`
- Khám phá lớp loại `Ord` (Phân lớp)
- xuất phát
    - Bắt nguồn có thể đi sai

## quá tải

Trước khi tìm hiểu Overloading là gì, chúng ta hãy tìm hiểu nghĩa của từ "date".

NGÀY:

"date" có nghĩa là gì? Nếu tôi nói rằng bạn chỉ có một cơ hội để trả lời và tôi sẽ cho bạn 100 đô la nếu bạn trả lời đúng, thì câu trả lời trực quan là: "Còn tùy!"

Nếu bạn đang nói: "Ngày sinh của bạn là ngày nào?" thì điều đó có nghĩa là:

1. Thời gian mà một sự kiện xảy ra.

Nếu bạn đang nói: "Joe đã đưa Laura đi hẹn hò.", thì điều đó có nghĩa là:

`

1. Một sự tham gia xã hội thường có tính chất lãng mạn (trừ khi Joe được khoanh vùng kết bạn).

Nếu bạn đang nói: "Tôi muốn hẹn hò với một hóa thạch", tôi muốn tin rằng bạn không đề cập đến một cuộc hẹn hò lãng mạn mà là:

`

1. Hành động ước tính hoặc tính toán ngày tháng hoặc niên đại.

Và nếu bạn tra cứu từ này, "date" cũng là tên của một loại trái cây và thậm chí còn có nhiều định nghĩa hơn!

Trong lập trình, chúng tôi sẽ nói rằng từ "ngày" bị quá tải. Bởi vì nó có nhiều định nghĩa cho cùng một tên.

Bản thân từ "quá tải" là quá tải.

QUÁ TẢI:

Trong bối cảnh hàng ngày, nó thường có nghĩa là:

`

1. Để đặt một tải trọng quá lớn lên hoặc vào (cái gì đó).

Trong bối cảnh lập trình thông thường, nó có nghĩa là:

`

1. Có nhiều triển khai của một chức năng có cùng tên.

Làm thế nào điều này làm việc trong thực tế phụ thuộc vào ngôn ngữ. Ví dụ: một số ngôn ngữ, chẳng hạn như JavaScript, không hỗ trợ nạp chồng. Vì vậy, bạn không thể làm điều đó. Và trong các hàm khác, như C++, bạn có thể tạo nhiều hàm có cùng tên và trình biên dịch sẽ chọn định nghĩa sẽ sử dụng dựa trên các loại đối số.

Trong Haskell, "quá tải" có nghĩa là:

`

1. Có nhiều triển khai của một chức năng hoặc giá trị có cùng tên.

Tất nhiên, Haskell phải đẩy mạnh trò chơi. Trong Haskell, quá tải không bị hạn chế đối với các chức năng. Các giá trị cũng có thể bị quá tải. Ví dụ:

- Các chữ `1` , `2` , v.v. bị quá tải vì chúng có thể được hiểu là bất kỳ loại số nào ( `Int` , `Integer` , `Float` , v.v.)

- Giá trị `minBound` bị quá tải vì, ví dụ: khi được sử dụng dưới dạng `Char` , giá trị này sẽ có giá trị `'\NUL'` trong khi dưới dạng `Int` , giá trị đó là `-2147483648` .

- Toán tử đẳng thức ( `==` ) hoạt động với nhiều kiểu, mỗi kiểu có cách triển khai riêng.

- Hàm `max` cũng hoạt động với nhiều loại, mỗi loại có cách thực hiện riêng.

Hai giá trị đầu tiên là các giá trị bị quá tải và giá trị cuối cùng là các hàm bị quá tải. Vì vậy, chúng ta đã và đang sử dụng các hàm và giá trị quá tải. Câu hỏi đặt ra là: Làm thế nào để chúng ta có được những thứ đó ngay từ đầu? Chà, cơ chế cho phép quá tải trong Haskell là Type Classes.

## Các bước để tạo Type Classes và Instances

Trong bài "giới thiệu về lớp kiểu", chúng ta đã thấy tiện ích của lớp kiểu. Về cơ bản, nó tập trung vào việc có các chức năng có thể được sử dụng bởi nhiều loại khác nhau trong khi vẫn đảm bảo an toàn rằng chúng chỉ sử dụng những chức năng mà chúng có thể làm việc cùng. Vì vậy, nếu bạn tạo một hàm lấy hai số và cộng chúng lại với nhau, thì hàm đó sẽ hoạt động với tất cả các loại số đồng thời khiến trình biên dịch dừng bạn khi cố gắng cung cấp cho nó một loại không phải là số.

Các lớp kiểu là một tính năng khá độc đáo - không nhiều ngôn ngữ lập trình có chúng. Nhưng điều tốt là chúng rất dễ sử dụng!

Khi tạo các lớp kiểu của riêng mình, chúng ta chỉ cần hai thứ.

`

1. Tạo một Type Class nêu rõ một số hành vi.

2. Tạo một Loại một thể hiện của Loại Loại đó với việc triển khai các hành vi đó cho loại cụ thể đó.

Đó là nó.

Thực hành tạo nên sự hoàn hảo, vì vậy hãy học bằng cách thực hành. Chúng ta sẽ bắt đầu bằng cách xác định lại Loại `Eq` .

## Lớp loại `Eq`

Lớp loại `Eq` đi kèm với Haskell, vì vậy bạn không cần phải định nghĩa nó. Nhưng giả sử rằng chúng ta đang sống trong một thế giới không tồn tại lớp loại `Eq` và mỗi loại đều có chức năng riêng để kiểm tra sự bằng nhau. Do đó, bạn phải học một loạt các chức năng khác nhau mà tất cả đều thực hiện giống nhau: Kiểm tra sự bằng nhau.

Nhưng, như Lennon đã nói, hãy tưởng tượng. Khi sống trong thế giới khủng khiếp đó, hãy tưởng tượng tất cả các loại sống trong hòa bình và sử dụng cùng một chức năng. Thật dễ dàng nếu bạn cố gắng. Bạn có thể nói tôi là một kẻ mơ mộng, nhưng hãy cứ làm đi!

Chúng ta có thể định nghĩa lớp kiểu `Eq` như sau:

`

```{.haskell}
class Eq a where
  (==) :: a -> a -> Bool
  (/=) :: a -> a -> Bool
```

Trong dòng đầu tiên, chúng tôi bắt đầu với từ khóa `class` để cho biết chúng tôi đang tạo một loại lớp. Tiếp theo là cách lớp loại sẽ được gọi ( `Eq` ). Sau đó, chúng ta viết một biến kiểu ( `a` ) đại diện cho bất kỳ kiểu nào sẽ được tạo thành một thể hiện của lớp kiểu này trong tương lai. Vì vậy, nó giống như một trình giữ chỗ. Và cuối cùng, chúng tôi sử dụng từ khóa `where` để bắt đầu khối nơi chúng tôi xác định các hành vi của lớp loại mới được tạo.

Và bây giờ đến phần thú vị. Chúng ta phải xác định các hành vi. Để làm điều đó, chúng tôi viết tên và loại chức năng hoặc giá trị mà chúng tôi cần. Trong trường hợp này, chúng tôi xác định các hành vi là hàm `==` --để kiểm tra xem hai giá trị có bằng nhau hay không và hàm `/=` --để kiểm tra xem hai giá trị có khác nhau không.

Chúng tôi cũng chỉ ra rằng cả hai đều nhận hai giá trị của loại `a` mà chúng tôi đã chỉ định làm tham số của lớp loại và trả về một `Bool` . `True` nếu điều kiện vượt qua và `False` nếu không.

Và thực hiện! Chúng tôi đã có lớp loại `Eq` sẵn sàng hoạt động! Điều này có nghĩa là chúng ta có tên và kiểu của hai hàm mà lớp kiểu `Eq` cung cấp. Chúng tôi không có các định nghĩa ở đây vì mỗi loại sẽ có các định nghĩa riêng. Và những định nghĩa đó được cung cấp khi định nghĩa một thể hiện cho lớp kiểu.

### Xác định một thể hiện cho lớp loại `Eq`

Trước tiên, chúng tôi cần một loại, vì vậy, hãy xác định một loại cho các phương thức thanh toán mà khách hàng có thể sử dụng trong ứng dụng của chúng tôi:

```{.haskell}
data PaymentMethod = Cash | Card | CC -- CC stands for Cryptocurrency

type User = (String, PaymentMethod)
```

Và nếu chúng ta muốn, ví dụ, để kiểm tra xem hai người dùng có cùng một phương thức thanh toán hay không, chúng ta có thể viết một hàm như sau:

```{.haskell}
samePM :: User -> User -> Bool
samePM (_, pm1) (_, pm2) = pm1 == pm2  -- Won't work!
```

{.output .error ename="" evalue=""}<interactive> :2:28: lỗi: • Không có trường hợp nào cho (Eq PaymentMethod) phát sinh từ việc sử dụng '==' • Trong biểu thức: pm1 == pm2 Trong một phương trình cho 'samePM': samePM ( <em>, pm1) (</em> , pm2) = chiều1 == chiều2</interactive>

Tuy nhiên, trình biên dịch sẽ không cho phép bạn sử dụng mã này! Và nó cho chúng ta biết tại sao:

```
No instance for (Eq PaymentMethod) arising from a use of ‘==’
In the expression: pm1 == pm2
```

Chúng tôi đang sử dụng `==` trong biểu thức `pm1 == pm1` . Tuy nhiên, bởi vì `==` là một hành vi của lớp loại `Eq` và loại Phương thức `PaymentMethod` mới của chúng tôi không phải là một thể hiện của lớp loại `Eq` ! Vì vậy, nó không có triển khai `==` và `/=` để sử dụng. Để khắc phục điều này, chúng tôi sẽ biến nó thành một ví dụ!

```{.haskell}
-- class Eq a where
--   ...

instance Eq PaymentMethod where
  -- Implementations for Eq behaviors specific to PaymentMethod
```

Để tạo một thể hiện, chúng ta sử dụng từ khóa `instance` hiện theo sau là tên của lớp loại mà chúng ta muốn tạo một thể hiện, loại sẽ là một thể hiện của lớp kiểu đó và từ khóa `where` . Sau đó, bên trong khối đó, chúng tôi triển khai các chức năng được định nghĩa trong lớp loại đó.

Như bạn có thể thấy, bởi vì bây giờ chúng ta đang tạo một thể hiện cho một loại, nên chúng ta thay thế biến loại ( `a` ) mà chúng ta có trong định nghĩa lớp loại bằng loại cụ thể của mình ( `PaymentMethod` ).

Và bởi vì chúng ta đang tạo một thể hiện cho lớp kiểu Eq, nên chúng ta cần triển khai các hàm `==` và `/=` . Vì vậy, chúng tôi sẽ làm điều đó:

```{.haskell}
-- class Eq a where
--   (==) :: a -> a -> Bool
--   (/=) :: a -> a -> Bool

-- data PaymentMethod = Cash | Card | CC

instance Eq PaymentMethod where
  -- Implementation of ==
  Cash == Cash = True
  Card == Card = True -- Same as: (==) Card Card = True
  CC == CC = True
  _ == _ = False
  
  -- Implementation of /=
  Cash /= Cash = False
  Card /= Card = False
  CC /= CC = False
  _ /= _ = True
```

Và thế là xong! Đó là cách bạn định nghĩa một lớp kiểu và biến một kiểu thành một thể hiện của nó! Giờ đây, `PaymentMethod` có thể tự do sử dụng các hành vi `Eq` ( `==` và `/=` ):

"số 8"

```{.haskell}
Card == Cash
CC /= Card
```

Kết quả: Sai

Kết quả: Đúng

Và chức năng trước đó sẽ hoạt động ngay bây giờ:

```{.haskell}
samePM :: User -> User -> Bool
samePM (_, pm1) (_, pm2) = pm1 == pm2  -- It's alive!

samePM ("Rick", CC) ("Marta", CC)
```

Kết quả: Đúng

### Cải thiện lớp loại `Eq` của chúng tôi với Đệ quy lẫn nhau

Công việc của chúng tôi được thực hiện về mặt kỹ thuật. Chúng tôi có lớp loại của chúng tôi và ví dụ của chúng tôi. Nhưng có một thuộc tính của các hàm mà chúng ta vừa định nghĩa mà chúng ta không tận dụng được.

Nếu hai giá trị bằng nhau, điều đó có nghĩa là chúng không khác nhau và nếu chúng khác nhau, điều đó có nghĩa là chúng không bằng nhau. Vì vậy, chúng tôi biết rằng đối với mỗi cặp giá trị, `==` và `/=` sẽ luôn cho chúng tôi giá trị `Bool` ngược lại.

Chúng tôi đang trên đường trở thành những nhà phát triển Haskell vĩ đại và những nhà phát triển Haskell vĩ đại có thể làm tốt hơn thế. Vì vậy, hãy sử dụng kiến thức này để cải thiện lớp kiểu và thể hiện của chúng ta! Bắt đầu bằng cách xác định lại lớp loại `Eq` như thế này:

```{.haskell}
class Eq a where
  (==), (/=)  :: a -> a -> Bool
  x /= y      = not (x == y)
  x == y      = not (x /= y)
```

**Đó là cách `Eq` thực sự được xác định trong Haskell!**

Hãy phân tích mã này. Vì cả hai hàm đều có cùng kiểu nên chúng ta có thể chỉ định chúng trong một dòng. Và vâng, chúng ta cũng đang viết các định nghĩa hàm bên trong lớp kiểu. Chúng ta có thể làm điều đó miễn là chúng không phụ thuộc vào kiểu vì chúng phải làm việc với tất cả các kiểu.

Xem xét các định nghĩa chi tiết hơn, chúng ta thấy mình đang sử dụng hàm `not` . Hàm `not` nhận một giá trị boolean và trả về giá trị ngược lại của nó.

Vì vậy, trong dòng thứ ba, chúng ta đang nói rằng kết quả của việc áp dụng `/=` cho `x` và `y` là đối lập ( `not` ) của kết quả của việc áp dụng `==` cho cùng một `x` và `y` . Và ở dòng thứ tư, chúng ta đang nói rằng kết quả của việc áp dụng `==` cho `x` và `y` là đối lập ( `not` ) của kết quả của việc áp dụng `/=` cho cùng một `x` và `y` .

Điều này được gọi là đệ quy lẫn nhau vì cả hai chức năng được xác định theo thuật ngữ của nhau. Bằng cách định nghĩa `==` và `/=` là đối lập của nhau, Haskell có thể suy ra hành vi của cái này từ cái kia.

Và, tất nhiên, giống như bất kỳ đệ quy nào khác, nó cần một trường hợp cơ sở để biết khi nào nên dừng đệ quy! Và đó là những gì chúng tôi cung cấp khi triển khai một phiên bản! Ví dụ: hãy xác định lại đối tượng PaymentMethod cho loại lớp mới này:

{.cell .code

```{.haskell}
instance Eq PaymentMethod where
  Cash == Cash = True
  Card == Card = True
  CC == CC = True
  _ == _ = False
```

Đó là nó! Bởi vì bây giờ trình biên dịch có thể suy ra giá trị của hàm này với hàm kia, nên chúng ta không cần triển khai cả `==` và `/=` . Chúng ta có thể thực hiện một cách thuận tiện hơn và gọi nó là một ngày!

Điều này được gọi là **định nghĩa đầy đủ tối thiểu** . Bởi vì đó là mức tối thiểu bạn phải thực hiện để có được một phiên bản đầy đủ chức năng. Bạn có thể tận dụng điều này bằng cách kiểm tra định nghĩa đầy đủ tối thiểu của bất kỳ loại lớp nào bằng cách sử dụng `:i <type class>` và chỉ thực hiện các hành vi đó. Ví dụ: nếu bạn chạy `:i Eq` trong GHCi, bạn sẽ nhận được:

```{.haskell}
type Eq :: * -> Constraint -- Eq takes a concrete type and returns a Constraint
class Eq a where
  (==) :: a -> a -> Bool
  (/=) :: a -> a -> Bool
  {-# MINIMAL (==) | (/=) #-}

-- ... and a bunch of instances.
```

Trong dòng này:

```{.haskell}
{-# MINIMAL (==) | (/=) #-}
```

Nó nói rằng để có *định nghĩa đầy đủ tối thiểu* của lớp loại, bạn phải triển khai `==` OR `/=` .

Trong thế giới thực, hầu hết tất cả các kiểu đều là thể hiện của lớp kiểu `Eq` . Nhưng hãy nhớ rằng, chúng ta đang ở trong một vũ trụ song song nơi bạn là người có tầm nhìn xa tạo ra lớp loại `Eq` để biến thế giới thành một nơi tốt đẹp hơn. Vì vậy, nếu chúng ta dừng ở đây, các hàm `==` và `/=` sẽ không bị quá tải! Bởi vì họ sẽ chỉ có định nghĩa cho `PaymentMethod` .

Nhưng có một lý do khiến bạn quyết định tạo lớp loại `Eq` này. Và lý do là bạn nghĩ rằng các hành vi mà nó cung cấp là hữu ích cho nhiều loại. Ví dụ như loại Blockchain:

"11" cuộn = "false"

```{.haskell}
-- Create data type
data Blockchain = Cardano | Ethereum | Bitcoin

-- Create instance of Eq
instance Eq Blockchain where
    Cardano == Cardano = True
    Ethereum == Ethereum = True
    Bitcoin == Bitcoin = True
    _ == _ = False


-- Test
Cardano /= Cardano
```

Kết quả: Sai

Bây giờ, `==` và `/=` thực sự bị quá tải vì chúng có nhiều hơn một định nghĩa tùy thuộc vào loại giá trị mà chúng được áp dụng.

Chúng ta làm được rồi!! Và chúng ta đang trên đà phát triển, vì vậy hãy tiếp tục!

Cho đến nay, chúng tôi đã tạo hai phiên bản của lớp loại `Eq` . Cả hai cho các loại không tham số. Hãy tìm hiểu cách chúng ta có thể định nghĩa một thể hiện cho một kiểu được tham số hóa.

### Xác định một thể hiện cho một loại tham số

Để tạo một thể hiện cho kiểu được tham số hóa, trước tiên, chúng ta cần kiểu được tham số hóa:

"32"

```{.haskell}
data Box a = Empty | Has a
```

Bây giờ chúng ta có thể tạo ví dụ của mình. Nhưng chúng ta không thể làm điều đó như thế này:

`

```{.haskell}
instance Eq Box where
-- ...
```

Tại sao? Chà, nếu chúng ta xem lớp loại bằng cách sử dụng lệnh `:i` :

```{.haskell}
type Eq :: * -> Constraint -- Eq takes a concrete type and returns a Constraint
class Eq a where
  (==) :: a -> a -> Bool
  (/=) :: a -> a -> Bool
  {-# MINIMAL (==) | (/=) #-}

-- ... and a bunch of instances.
```

Chúng ta được nhắc nhở rằng biến kiểu `a` là một kiểu cụ thể. Chúng ta có thể thấy điều này ở hai nơi:

- Nếu chúng ta kiểm tra các loại hàm, chúng ta sẽ thấy rằng biến loại `a` nằm một mình giữa các mũi tên, do đó, nó đại diện cho một loại cụ thể.
- Và do đó, loại `Eq` ( `type Eq :: * -> Constraint` ) nói rõ rằng nó lấy một loại cụ thể và tạo ra một `Constraint` .

Các lớp loại luôn có một loại trả về một `Constraint` vì các lớp loại không tạo ra một loại. Chúng tạo ra một ràng buộc cho các giá trị đa hình. Vì vậy, nếu chúng ta thấy một loại kết thúc bằng `Constraint` , chúng ta biết đó là một loại lớp và nó nằm ở bên trái của mũi tên `=>` để hạn chế các loại đa hình.

Trên hết, chúng ta không cần kiểm tra các hàm để biết cách lớp kiểu sử dụng biến kiểu `a` . Loại đã cho chúng tôi biết nếu nó cần một loại cụ thể hoặc một hàm tạo loại cụ thể.

Vì vậy, vì `Eq :: * -> Constraint` , chúng tôi biết rằng `a` trong `Eq a` là một loại cụ thể. Nhưng nếu chúng ta kiểm tra loại `Box` :

```{.haskell}
:k Box
```

Chúng ta thấy rằng nó không phải là một kiểu cụ thể mà là một hàm tạo kiểu lấy một kiểu làm tham số và trả về một kiểu cụ thể.

Vậy ta phải làm sao? Chúng ta có thể áp dụng `Box` cho một loại khác để có được một loại cụ thể, như sau:

```{.haskell}
:k Box Int
```

Về mặt kỹ thuật, điều đó mang lại cho chúng tôi một loại cụ thể, vì vậy chúng tôi có thể tạo các phiên bản như thế này:

`

```{.haskell}
instance Eq (Box Int) where
-- ...

instance Eq (Box String) where
-- ...

instance Eq (Box PaymentMethod) where
-- ...

--- etc
```

Và nó sẽ hoạt động hoàn hảo. Nhưng, Hmm, đây là rất nhiều công việc. Và chúng ta đã trải qua điều này khi định nghĩa các hàm và giải quyết nó bằng các biến kiểu. Thời gian này là không khác nhau!:

```{.haskell}
instance Eq (Box a) where
-- ...
```

Bằng cách xác định thể hiện này, tất cả các loại được tạo bằng hàm tạo kiểu `Box` (như `Box String` hoặc `Box Int` ) sẽ là một thể hiện của `Eq` .

Bây giờ, đợi một chút. Làm cách nào để chúng tôi xác định thể hiện nếu chúng tôi không biết loại giá trị bên trong hộp? Chà, nếu chúng ta quyết định rằng:

- Hai hộp chứa các phần tử bằng nhau thì bằng nhau.
- Hai ô trống bằng nhau.
- Và mọi thứ khác là khác nhau.

Chúng ta có thể định nghĩa các hành vi như thế này:

```{.haskell}
instance Eq (Box a) where
  Has x == Has y = x == y
  Empty == Empty = True
  _ == _ = False
```

```
    <interactive>:2:20: error:
        • No instance for (Eq a) arising from a use of ‘==’
          Possible fix: add (Eq a) to the context of the instance declaration
        • In the expression: x == y
          In an equation for ‘==’: Has x == Has y = x == y
          In the instance declaration for ‘Eq (Box a)’
```

Trong công thức đầu tiên, chúng tôi xác định `==` cho loại `Box a` bằng cách áp dụng `==` cho `a` mà nó chứa. Vì `Has x` thuộc loại `Box a` nên `x` thuộc loại `a` . Tương tự cho các giá trị còn lại. Vì vậy, nếu cả hai hộp chứa cùng một phần tử, thì bản thân các hộp đều giống nhau. Khác, họ khác nhau. Vì vậy, chúng ta đã làm cho phiên bản của `Box a` phụ thuộc vào phiên `a` của .

Trong công thức thứ hai, chúng tôi xác định rằng nếu cả hai ô đều trống thì chúng bằng nhau.

Đối với mọi trường hợp khác, các hộp là khác nhau.

Điều này có ý nghĩa, nhưng có một sự giám sát LỚN từ phía chúng tôi! Bạn có phát hiện ra nó không? Không sao đâu. Đó là mục đích của trình biên dịch ở đây! Nếu chúng ta chạy ô, chúng ta sẽ gặp lỗi trình biên dịch:

```
No instance for (Eq a) arising from a use of ‘==’
```

Ok, vì vậy trình biên dịch cho chúng tôi biết rằng chúng tôi đang áp dụng hàm `==` cho một loại không có phiên bản `Eq` .

Chúng ta đang làm điều đó ở đâu?

```
In the expression: x == y
In an equation for ‘==’: Has x == Has y = x == y
In the instance declaration for ‘Eq (Box a)’
```

Trình biên dịch là chính xác! Chúng tôi đang sử dụng `==` giữa hai giá trị ( `x` và `y` ) của loại `a` mà không đảm bảo rằng chính loại `a` là một thể hiện của `Eq` !

Vậy chúng ta nên làm gì? Chà, trình biên dịch cũng cho chúng tôi biết cách sửa lỗi này:

```
Possible fix: add (Eq a) to the context of the instance declaration
```

Tương tự với các hàm, chúng ta có thể thêm ràng buộc rằng kiểu `a` trong thể hiện của `Eq (Box a)` cũng phải là một thể hiện của lớp kiểu `Eq` . Như thế này:

```{.haskell}
instance (Eq a) => Eq (Box a) where
  Has x == Has y = x == y
  Empty == Empty = True
  _ == _ = False
```

Bằng cách này, loại `Box a` sẽ là một thể hiện của `Eq` cho tất cả các loại `a` cũng là một thể hiện của `Eq` .

Aaaaa và chúng ta xong rồi! Chúng ta có thể sử dụng ví dụ mới này như thế này:

```{.haskell}
Has Cardano /= Has Ethereum -- True

Has Card == Empty           -- False

Has Bitcoin /= Has Bitcoin  -- False


data Choice = Yes | No      -- We didn't create an Eq instance for Choice

Has Yes == Has No           -- Angry compiler: There's no instance for (Eq Choice), you fool!
```

```
    <interactive>:1:1: error:
        • No instance for (Eq Choice) arising from a use of ‘==’
        • In the expression: Has Yes == Has No
          In an equation for ‘it’: it = Has Yes == Has No
```

Vì vậy, ngay cả khi bọc loại này bên trong loại khác, trình biên dịch vẫn sẽ bảo vệ chúng ta khỏi những sai lầm của con người.

Được rồi. Bây giờ chúng ta đã làm mọi thứ từng bước với lớp loại `Eq` , hãy làm lại mọi thứ, nhưng nhanh hơn và với một lớp loại mới không phải là một phần của Haskell tiêu chuẩn.

## Lớp loại `WeAccept`

Hãy tưởng tượng chúng tôi đang viết một ứng dụng chấp nhận thanh toán cho một công ty và công ty này không chấp nhận tất cả các phương thức thanh toán, chuỗi khối và quốc gia. Vì vậy, bạn phải tạo các chức năng để kiểm tra xem:

```{.haskell}
-- Function to check if we accept that payment method
weAcceptPayment :: PaymentMethod -> Bool
weAcceptPayment p = case p of
   Cash -> False
   Card -> True
   CC   -> True

-- Function to check if we accept that blockchain
weAcceptBlockchain :: Blockchain -> Bool
weAcceptBlockchain b = case b of
   Bitcoin  -> True
   Ethereum -> False
   Cardano  -> True

-- Country type
newtype Country = Country { countryName :: String }

-- Function to check if we accept that country
weAcceptCountry :: Country -> Bool
weAcceptCountry c = case countryName c of
   "Mordor"  -> False
   _         -> True
```

Xem mã này, chúng tôi nhận ra rằng hành vi kiểm tra xem công ty có chấp nhận điều gì đó hay không có thể được sử dụng trong nhiều khía cạnh khác. Như nhà cung cấp, công nghệ, v.v. Có rất nhiều thứ mà một công ty có thể quyết định chấp nhận hay không.

Để tránh có nhiều chức năng khác nhau thực hiện giống nhau trên tất cả mã của bạn, chúng tôi quyết định tạo một lớp loại đại diện cho hành vi này.

Và loại lớp đó trông như thế này:

```{.haskell}
-- Creating WeAccept type class
class WeAccept a where
  weAccept :: a -> Bool

-- Checking kind of WeAccept
:k WeAccept
```

Bây giờ chúng ta đã có lớp loại của mình, chúng ta có thể tạo các thể hiện cho `PaymentMethod` , `Blockchain` , `Country` và thậm chí cả `Box` như thế này:

```{.haskell}
instance WeAccept PaymentMethod where
  weAccept x = case x of
   Cash -> False
   Card -> True
   CC   -> True

instance WeAccept Blockchain where
  weAccept x = case x of
   Bitcoin  -> True
   Ethereum -> False
   Cardano  -> True

instance WeAccept Country where
  weAccept x = case countryName x of
    "Mordor" -> False
    _        -> True

instance (WeAccept a) => WeAccept (Box a) where
  weAccept (Has x) = weAccept x
  weAccept Empty   = False
```

Và thực hiện! Điều này cho chúng ta khả năng áp dụng hàm `weAccept` quá tải cho ba loại khác nhau:

```{.haskell}
weAccept Cardano

Kết quả:
    True

weAccept Cash
Kết quả:
    False

weAccept (Country "Mordor")
Kết quả:
    False

weAccept (Has Bitcoin)
Kết quả:
    True
```

Chúng tôi cũng có thể tạo các chức năng có thể được áp dụng cho tất cả các loại là phiên bản của `WeAccept` :

```{.haskell}
-- Creating fancyFunction
fancyFunction :: (WeAccept a) => a -> String
fancyFunction x =
  if weAccept x
    then "Do something fancy"
    else "Don't do it!"
    
-- Using fancyFunction
fancyFunction Cardano

Kết quả:
    "Do something fancy"

fancyFunction Card
Kết quả:
    "Do something fancy"

fancyFunction (Country "Mordor")

Kết quả:
    "Don't do it!"
fancyFunction (Has Bitcoin)
Kết quả:
    "Do something fancy"
```

Một loại lớp khác dưới vành đai của chúng tôi! Nó trở nên dễ dàng hơn từng phút!

Chúng ta sẽ làm thêm một ví dụ nữa trước khi tiếp tục sang phần tiếp theo. Cái này khó hơn một chút, nhưng nếu bạn hiểu nó, bạn sẽ có thể hiểu bất kỳ lớp loại nào! Cho dù nó phức tạp đến mức nào!

## Lớp loại `Container`

Đây là tình huống: Chúng tôi đang làm việc trên một phần mềm hậu cần có hai loại gói hàng khác nhau. Một chiếc hộp thông thường có thể chứa hoặc không chứa thứ gì đó, và một món quà, có thể chứa hoặc không chứa thứ gì đó, nhưng nó luôn có bảng tên ghi món quà đó dành cho ai. Vì vậy, chúng tôi có hai loại:

```{.haskell}
data Box a       = Empty          | Has a            deriving (Show)
data Present t a = EmptyPresent t | PresentFor t a   deriving (Show)

:k Box
:k Present
```

Bởi vì chúng tôi đã quyết định rằng thẻ của món quà ( `t` ) có thể là một số, tên hoặc bất kỳ thứ gì khác có thể xác định khách hàng, chúng tôi cũng sẽ tham số hóa loại của nó.

Bây giờ, một số phần của quy trình yêu cầu các chức năng chung cho cả hai loại. Chúng tôi cần:

- Một để kiểm tra xem hộp hoặc quà có trống không.
- Một để kiểm tra xem một giá trị cụ thể có được chứa bên trong hộp hay không.
- Và một để thay thế nội dung của hộp hoặc quà tặng.

Thay vì tự viết các hàm và sau đó chuyển đổi chúng thành một lớp kiểu và các thể hiện như chúng ta đã làm trong hai ví dụ trước, hãy chuyển thẳng sang lớp kiểu.

```{.haskell}
class Container c where
    isEmpty  ::  -- ...
    contains ::  -- ...
    replace  ::  -- ...
```

Lớp type sẽ được gọi là `Container` vì nó cung cấp các hành vi liên quan đến container. Biến loại được gọi là `c` vì nó là một thùng chứa.

Bây giờ, hãy viết ra các chữ ký loại. Chúng ta sẽ bắt đầu với chức năng `replace` . Nguyên nhân tại sao không?

```{.haskell}
class Container c where
    isEmpty  ::  -- ...
    contains ::  -- ...
    replace  ::  c a -> b -> c b
```

`replace` có hai đầu vào:

- Một vùng chứa `c` có một số giá trị thuộc loại---giả sử `a` ---bên trong.
- Và một giá trị khác có thể cùng loại hoặc khác loại với giá trị bên trong vùng chứa. Hãy gọi nó là `b` .

Hàm thay thế giá trị của loại `a` bên trong vùng chứa bằng giá trị của loại `b` . Vì vậy, cuối cùng, chúng tôi nhận được một giá trị loại `cb` vì giá trị mà nó chứa hiện là loại `b` .

Bây giờ, hãy thực hiện chức năng `contains` :

```{.haskell}
class Container c where
    isEmpty  ::  -- ...
    contains ::  (Eq a) => c a -> a -> Bool
    replace  ::  c a -> b -> c b
```

`contains` có hai đầu vào:

- Một thùng chứa `c` có một số giá trị loại `a` bên trong.
- Và một giá trị khác sẽ được so sánh với giá trị bên trong vùng chứa. Vì vậy, nó cần phải cùng loại `a` và một phiên bản của `Eq` vì chúng ta sẽ cần sử dụng `==` để kiểm tra xem nó có cùng giá trị hay không.

Hàm nhận giá trị, kiểm tra xem giá trị đó có giống với giá trị bên trong vùng chứa hay không và trả về `True` nếu đúng và `False` nếu không. Vì vậy, chúng tôi trả về một boolean.

Và cuối cùng, hãy thực hiện chức năng `isEmpty` :

```{.haskell}
class Container c where
    isEmpty  ::  c a -> Bool
    contains ::  (Eq a) => c a -> a -> Bool
    replace  ::  c a -> b -> c b
```

`isEmpty` nhận một đầu vào:

- Một thùng chứa `c` có một số giá trị loại `a` bên trong.

Hàm lấy vùng chứa và trả về `True` nếu nó chứa giá trị và `False` nếu không. Vì vậy, nó trả về một giá trị kiểu `Bool` .

Lớp loại của chúng tôi đã sẵn sàng để đi!

Và bởi vì mỗi `->` (mũi tên) phân tách một giá trị và tất cả các giá trị cần phải có một loại cụ thể, chúng tôi biết rằng cả `a` và `b` đều là các loại cụ thể. Bởi vì họ cô đơn giữa những mũi tên.

Sử dụng cùng một lý do, chúng tôi biết rằng `ca` và `cb` phải là các loại cụ thể. Và bởi vì `a` và `b` là các kiểu cụ thể, điều này có nghĩa là `c` là một hàm tạo kiểu lấy một kiểu cụ thể và trả về một kiểu cụ thể.

Chúng ta có thể thấy điều này nếu chúng ta kiểm tra loại của lớp loại của chúng ta:

```{.haskell}
:k Container
```

Bây giờ chúng ta đã có lớp kiểu của mình, hãy tạo các thể hiện cho kiểu `Box` :

"27"

```{.haskell}
-- class Container c where
--     isEmpty  :: c a -> Bool
--     contains :: (Eq a) => c a -> a -> Bool
--     replace  :: c a -> b -> c b

instance Container Box where

    isEmpty Empty = True
    isEmpty _     = False
    
    contains (Has x) y = x == y
    contains Empty   _ = False
 
    replace _ x = Has x
    

:k Box
:k Container
```

Lưu ý rằng chúng tôi tạo một phiên bản cho `Box` , không phải `Box a` . Đối với lớp loại `Eq` , chúng tôi đã áp dụng `Box` cho biến loại `a` để có được loại cụ thể `Box a` vì lớp loại `Eq` cần một loại cụ thể làm tham số. Nhưng `Container` có một hàm tạo loại `* -> *` , cùng loại với `Box` . Vì vậy, chúng tôi phải vượt qua `Box` mà không áp dụng nó cho bất cứ điều gì.

Việc thực hiện thực tế của các chức năng là khá đơn giản. Bởi vì `Box` có hai hàm tạo nên chúng tôi có hai công thức cho mỗi hàm.

Bây giờ, hãy tạo ví dụ cho loại `Present` :

```{.haskell}
-- class Container c where
--     isEmpty  :: c a -> Bool
--     contains :: (Eq a) => c a -> a -> Bool
--     replace  :: c a -> b -> c b


instance Container (Present t) where
    
    isEmpty (EmptyPresent _) = True
    isEmpty _                = False
    
    contains (PresentFor _ x) y = x == y
    contains (EmptyPresent _) _ = False
    
    replace (PresentFor tag _) x = PresentFor tag x
    replace (EmptyPresent tag) x = PresentFor tag x


:k Present
:k Container
:k Present String
```

Bây giờ, thể hiện dành cho hàm tạo kiểu `Present t` . Điều này là do bản thân `Present` có loại `* -> * -> *` , nhưng vì `Container` nhận một hàm tạo kiểu `* -> *` , nên chúng ta phải áp dụng `Present` cho một loại---như `Present String` --- để có được loại chúng tôi cần. Và bởi vì chúng tôi muốn có thể sử dụng bất kỳ loại nào làm thẻ, nên chúng tôi sử dụng biến loại `t` .

Vì vậy, phần này là quan trọng. Chữ `t` trong `Present t` là thẻ. Và toàn bộ hàm tạo kiểu `Present t` là `c` . Chúng ta có thể coi hàm tạo kiểu `Present t` là `c` vì nó là kiểu không bao giờ thay đổi. Chúng tôi không thay đổi loại thẻ trong bất kỳ chức năng nào. Nhưng chúng tôi sửa đổi loại nội dung trong chức năng `replace` . Khi chúng tôi sử dụng `replace` , loại nội dung có thể thay đổi từ `a` thành `b` , vì vậy chúng tôi không thể coi chúng là loại không đổi như `t` . Đó là lý do tại sao chúng là tham số cho hàm tạo kiểu `c` , vì vậy chúng ta có thể thay đổi kiểu trong hàm `replace` nếu cần.

Giống như trước đây, việc triển khai thực tế các chức năng là đơn giản.

Và để lấy phần thưởng từ công việc của chúng tôi, đây là một vài ví dụ sử dụng các hành vi lớp loại mới của chúng tôi:

```{.haskell}
Has False `contains` False         -- True

isEmpty (Has 'a')                  -- False

PresentFor "Tommy" 5 `contains` 5  -- True

PresentFor "Tommy" 5 `replace` "Arduino"   -- PresentFor "Tommy" "Arduino"


guessWhat'sInside :: (Container a, Eq b) => a b -> b -> String
guessWhat'sInside x y =
  if x `contains` y
    then "You're right!!"
    else "WROOONG!"

guessWhat'sInside (PresentFor "Mary" "A Raspberry Pi!") "A Ponny!"  -- **Mary's Dissapointment increasses**
guessWhat'sInside (Has 1) 15
```

Hiểu lớp loại này và các thể hiện là phần khó nhất của bài học. Có thể mất một lúc để hiểu đầy đủ những gì chúng ta vừa thấy. Nhưng đừng lo lắng, nếu một cái gì đó không nhấp, nó sẽ làm với một số thực hành. Đó là lý do tại sao điều quan trọng là phải làm bài tập về nhà.

Bây giờ, hãy tìm hiểu về phân lớp. Sau tất cả những gì chúng tôi đã trải qua, đây là một miếng bánh.

## Khám phá lớp loại `Ord` (Phân lớp)

Chúng tôi chưa bao giờ nói về phân lớp trước đây, nhưng bạn đã biết nó hoạt động như thế nào.

Chúng ta hãy xem nó trong thực tế khi định nghĩa một thể hiện cho lớp loại `Ord` .

Nếu chúng ta chạy lệnh info trên lớp loại `Ord` ( `:i Ord` ), chúng ta sẽ nhận được kết quả như sau:

```{.haskell}
type Ord :: * -> Constraint         -- Takes a concreate type
class Eq a => Ord a where           -- That "Eq a =>" is new!! 🤔
  compare :: a -> a -> Ordering
  (<) :: a -> a -> Bool             -- A bunch of functions
  (<=) :: a -> a -> Bool
  (>) :: a -> a -> Bool
  (>=) :: a -> a -> Bool
  max :: a -> a -> a
  min :: a -> a -> a
  {-# MINIMAL compare | (<=) #-}    -- We can only implement "compare" or "<=".
```

Tất cả mọi thứ kiểm tra ra. Ngoại trừ `Eq a =>` . Chúng tôi đã thấy điều này trong cả chức năng và trường hợp. Nhưng không bao giờ trên định nghĩa lớp loại.

Điều này ( `Eq a =>` ) có nghĩa là những gì bạn tưởng tượng:

**Để biến một loại `a` một thể hiện của `Ord` , trước tiên chúng ta phải biến nó thành một thể hiện của `Eq` ! Có nghĩa là `Eq` là điều kiện tiên quyết cho `Ord` . Nói cách khác, `Eq` là lớp cha của `Ord` hoặc `Ord` là lớp con của `Eq` .**

Các siêu lớp cho phép suy ra các chữ ký đơn giản hơn. Bằng cách nói rằng một loại là một thể hiện của `Ord` , chúng ta không chỉ biết rằng nó có các hành vi của `Ord` mà còn có các hành vi của `Eq` . Ngoài ra, điều này cho phép chúng ta sử dụng các hành vi của lớp loại `Eq` để xác định các thể hiện của lớp loại `Ord` . Đó thực sự là một cái gì đó xảy ra trong trường hợp này. Lớp loại `Ord` sử dụng các chức năng được cung cấp bởi lớp loại `Eq` .

Chúng tôi không thể nhìn thấy nó vì lệnh thông tin không hiển thị toàn bộ định nghĩa lớp loại. Giống như khi chúng ta chạy lệnh info cho lớp kiểu `Eq` , nó không hiển thị các định nghĩa đệ quy lẫn nhau của `==` và `/=` mà chúng ta vừa viết.

Tuy nhiên, mặc dù chúng ta không thể nhìn thấy chúng, nhưng chúng ta biết rằng có một loạt các định nghĩa hàm được định nghĩa theo thuật ngữ của nhau. Đó là lý do tại sao chúng ta có thể triển khai toàn bộ phiên bản bằng cách chỉ xác định `compare` hoặc `<=` .

Lệnh thông tin không hiển thị tất cả mã đó vì chúng tôi, các nhà phát triển, không quan tâm đến nó. Chúng tôi chỉ muốn biết:

- Những hành vi nào đi kèm với lớp loại. Để xem đó có phải thứ chúng ta cần không.
- Loại của lớp loại và các hành vi tối thiểu chúng ta cần thực hiện. Để chỉ thực hiện những điều đó.
- Nếu nó phụ thuộc vào lớp loại khác. Để thực hiện cái đó trước cái này.
- Và cuối cùng, những kiểu nào đã là một thể hiện của lớp kiểu này. Để xem loại nào đã có thể sử dụng những hành vi đó.

Và đó là những gì lệnh thông tin cho chúng ta thấy.

Vì vậy, để biến một loại thành thể hiện của `Ord` , trước tiên, chúng ta phải biến nó thành một thể hiện của `Eq` . May mắn thay, chúng tôi đã tạo một vài phiên bản cho `Eq` trước đây, vì vậy chúng tôi đã hoàn thành được nửa chặng đường nếu muốn tạo phiên bản `Ord` cho bất kỳ loại nào trong số đó.

Ví dụ: nếu chúng ta muốn tạo một thể hiện của `Box a` cho lớp loại `Ord` , chúng ta phải triển khai một trong các hàm cần thiết cho định nghĩa đầy đủ tối thiểu! Trong trường hợp này, chúng tôi đã chọn chức năng `compare` :

```{.haskell}
-- type Ord :: * -> Constraint
-- class Eq a => Ord a where
--   compare :: a -> a -> Ordering

instance (Ord a) => Ord (Box a) where
  Has x `compare` Has y = x `compare` y
  Empty `compare` Has _ = LT
  Has _ `compare` Empty = GT
  Empty `compare` Empty = EQ
  

Has 9 >= Has 5

Kết quả:
    True

Empty `compare` Has 0

Kết quả:
    LT

Empty < Empty

Kết quả:
    False
```

Đây là những gì đang xảy ra ở đây:

- Nếu cả hai hộp có một số giá trị bên trong, chúng tôi sẽ so sánh các giá trị. Và bởi vì chúng ta đang áp dụng hàm `compare` cho `x` và `y` của loại `a` , nên chúng ta cần thêm ràng buộc rằng loại `a` phải là một thể hiện của `Ord` .
- Nếu một trong các hộp `Empty` và hộp kia thì không, thì bên trong hộp có gì không quan trọng. Nó sẽ luôn lớn hơn cái `Empty` . Bởi vì tôi nói thế.
- Tất nhiên, nếu cả hai đều là `Empty` thì chúng bằng nhau.

Và bùm! đó là nó!

Chúng tôi tạo ra:

- Lớp loại `Eq` với 3 trường hợp khác nhau.
- Lớp loại `WeAccept` với 4 phiên bản.
- Sau đó, lớp loại `Container` với 3 thể hiện.
- Và cuối cùng, chúng ta tạo một kiểu là một thể hiện của lớp kiểu `Ord` .

**Chúc mừng! 🎉 Bạn biết mọi thứ cần thiết để làm việc với các loại lớp!!**

Trong phần cuối cùng của bài học này, chúng ta sẽ tìm hiểu cách thức và thời điểm tự động lấy các phiên bản. Tiết kiệm cho chúng tôi một chút thời gian quý báu và giảm số lượng mã chúng tôi phải duy trì.

## xuất phát

Các thể hiện có nguồn gốc là một cách tự động để biến một kiểu thành một thể hiện thành một lớp kiểu. Điều này là có thể bởi vì nhiều loại lớp phổ biến thường được thực hiện theo cùng một cách. Và một số người thông minh có bằng tiến sĩ đã tìm ra cách tạo mã này dựa trên định nghĩa của loại.

Điều này được giới hạn trong `Eq` , `Ord` , `Enum` , `Show` và các thư viện khác được xác định trong Prelude hoặc thư viện chuẩn---các thư viện đi kèm với Haskell và chúng ta sẽ khám phá trong các bài học sau. Bây giờ, hãy nghĩ rằng tất cả các lớp kiểu mà chúng ta đã sử dụng cho đến bây giờ và chúng ta không tự tạo ra chúng đều có thể được dẫn xuất.

Để sử dụng tính năng này, hãy thêm từ khóa `deriving` sinh vào cuối khai báo kiểu của bạn với tên của tất cả các lớp kiểu mà bạn muốn dẫn xuất. Ví dụ: nếu chúng ta làm điều này:

```{.haskell}
data Choice = No | Idk | Yes deriving (Eq, Ord, Show, Bounded, Enum)
```

```{.haskell}
Yes /= No             -- Are these values different?   (Behavior from Eq)

Kết quả:
    True

Yes > No              -- Is Yes bigger than No?        (Behavior from Ord)

Kết quả:
    True

show Yes              -- Transform Yes to String       (Behavior from Show)

Kết quả:
    "Yes"

(minBound) :: Choice  -- Smallest value of type Choice (Behavior from Bounded)

Kết quả:
    No

succ No               -- Successor of No               (Behavior from Enum)

Kết quả:
    Idk
```

Và thế là xong!! Loại `Choice` của bạn có các hành vi được cung cấp bởi tất cả các lớp loại đó.

Vì vậy, nếu chúng ta có thể làm điều đó ngay từ đầu, thì tại sao bạn lại quan tâm đến việc tạo ra các phiên bản thủ công?

Chà... Một lý do là không phải tất cả các lớp kiểu đều có thể được dẫn xuất. Và một điều nữa là việc bắt nguồn đôi khi có thể sai.

### Bắt nguồn có thể đi sai

Mỗi loại lớp có bộ quy tắc riêng để dẫn xuất các thể hiện. Ví dụ: khi lấy loại `Ord` , các hàm tạo giá trị được xác định trước đó sẽ nhỏ hơn. Vì vậy, trong trường hợp này:

```{.haskell}
data PaymentMethod = Cash | Card | CC deriving (Eq, Ord)

Cash > Card

Kết quả:
    False

Card < CC

Kết quả:
    True

CC `compare` Cash

Kết quả:
    GT

```

`Cash` nhỏ hơn `Card` , nhỏ hơn `CC` .

Và trong trường hợp này:

```{.haskell}
data Box a = Empty | Has a deriving (Eq, Ord)

Has 5 `compare` Has 6

Kết quả:
    LT

Has "Hi" >= Has "Hello!"

Kết quả:
    True
```

Nếu một hàm tạo giá trị có một tham số ( `Has a` ) và hai giá trị được tạo từ cùng một hàm tạo ( `Has 5` và `Has 6` ), thì các tham số sẽ được so sánh (giống như chúng ta đã làm khi tự định nghĩa các thể hiện).

Đó là những quy tắc mà trình biên dịch tuân theo để tự động tạo cá thể `Ord` cho loại của bạn. Các lớp loại khác có các quy tắc khác. Chúng ta sẽ không đi qua các quy tắc của từng loại lớp, nhưng tôi sẽ cung cấp một [liên kết](https://www.haskell.org/onlinereport/haskell2010/haskellch11.html) với một lời giải thích ngắn trong bài học tương tác. Trong trường hợp bạn muốn tìm hiểu thêm.

Bây giờ, giả sử chúng ta muốn sử dụng một loại để quản lý độ dài cho phần mềm Kỹ thuật dân dụng.

Chúng tôi làm việc với cả mét và kilômét, nhưng vì chúng tôi không muốn vô tình trộn lẫn chúng và gặp lỗi nghiêm trọng tiềm ẩn, nên chúng tôi xác định một loại dữ liệu có hai hàm tạo. Một cho mét và một cho km. Cả hai đều chứa giá trị kiểu `Double` . Chúng tôi cũng sẽ dẫn xuất lớp loại `Eq` .

```{.haskell}
data Length = M Double | Km Double deriving (Eq)
```

Tuy nhiên, ngay khi bắt đầu sử dụng kiểu dữ liệu này, chúng tôi phát hiện ra một vấn đề nhỏ. Chúng tôi biết rằng 1000 mét bằng 1 km, nhưng khi chúng tôi kiểm tra điều này trong mã của mình, chúng tôi nhận thấy rằng không phải vậy!:

```{.haskell}
M 1000 == Km 1 -- False
```

Kết quả: Sai

Đó là bởi vì khi chúng tôi bắt nguồn `Eq` , Haskell đã tạo mã này:

```{.haskell}
instance Eq Length where
  (==) (M  x) (M  y) = x == y
  (==) (Km x) (Km y) = x == y
  (==) _      _      = False
```

Điều này rất hiệu quả nếu chúng ta so sánh mét với mét và kilômét với kilômét. Nhưng chúng tôi đã triển khai sai để so sánh giữa các hàm tạo vì Haskell không biết rằng giá trị của các hàm tạo khác nhau có liên quan theo bất kỳ cách nào!! Haskell chỉ giả định rằng nếu các hàm tạo khác nhau, thì các giá trị cũng vậy!

Vì vậy, trong trường hợp này, chúng ta phải tự viết thể hiện để tính đến mối quan hệ giữa các hàm tạo. Như thế này:

```{.haskell}
data Length = M Double | Km Double

instance Eq Length where
  (==) (M  x) (M  y) = x == y
  (==) (Km x) (Km y) = x == y
  (==) (M  x) (Km y) = x == 1000 * y
  (==) (Km x) (M  y) = x * 1000 == y


M 3000 == Km 3   -- True
Km 7   /= M 14   -- True
```

Đó là lý do tại sao nên ý thức về cách mỗi loại lớp được dẫn xuất. Để biết khi nào bạn có thể lấy được chúng và khi nào bạn phải viết ví dụ bằng tay.

Và để kết thúc bài học, đây là một số mẹo để viết mã trong thế giới thực:

### Mẹo viết mã trong thế giới thực

`

- Tất cả mọi thứ tôi giải thích ở đây hôm nay áp dụng cho tất cả các lớp loại.

`

- Chúng tôi không định nghĩa các lớp loại thường xuyên. Thông thường, những thứ đi kèm với Haskell là tất cả những gì chúng ta cần.

`

- Chúng tôi triển khai các phiên bản khá nhiều. Và nó thường (nhưng không phải luôn luôn) là một ý tưởng tốt để lấy chúng. Nếu bạn nghi ngờ, hãy thử tính toán tự động và kiểm tra các giả định của bạn. Bạn luôn có thể quay lại và xác định các phiên bản theo cách thủ công.

`

- Bạn có thể xem qua định nghĩa lớp loại bằng cách sử dụng `:i` trên GHCi để xem các hành vi tối thiểu cần triển khai khi tạo phiên bản của mình. Thực hiện những điều đó, và bạn đã hoàn tất.
