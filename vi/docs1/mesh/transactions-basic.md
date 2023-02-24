---
id: giao dịch cơ bản
sidebar_position: '4'
title: Giao dịch cơ bản   - SDK lưới (Thư viện nguồn mở để xây dựng ứng dụng Web3 trên Chuỗi khối Cardano)
sidebar_label: Giao dịch cơ bản
description: Tạo giao dịch để gửi tài sản.
image: "../img/og/og-getstarted-mesh.png"
---

Khi viết, có 4 loại giao dịch chính:

-  [Gửi lovelace và tài sản](transactions-basic) (cái này)
- [Tương tác với hợp đồng thông minh](transactions-smart-contract)
- [Đúc và đốt tài sản](transactions-minting)
- [Tương tác với các stakepool](transactions-staking)

Trong phần này, chúng ta sẽ khám phá những điều sau đây:

- [Gửi ADA đến Địa chỉ](#send-ada-to-addresses)
- [Gửi nhiều tài sản đến địa chỉ](#send-multiple-assets-to-addresses)
- [Gửi tài sản cho Hendler](#send-assets-to-handler)

## Gửi ADA đến một Địa chỉ

Bạn có thể xâu chuỗi `tx.sendLovelace()` để gửi cho nhiều người nhận. Ví dụ:

```javascript
import { Transaction } from "@meshsdk/core";

const tx = new Transaction({ initiator: wallet })
  .sendLovelace(
    "addr_test1vpvx0sacufuypa2k4sngk7q40zc5c4npl337uusdh64kv0c7e4cxr",
    "1000000"
  )
  .sendLovelace("ANOTHER ADDRESS HERE", "1500000");
const unsignedTx = await tx.build();
const signedTx = await wallet.signTx(unsignedTx);
const txHash = await wallet.submitTx(signedTx);
```

[thử bản trình diễn](https://meshjs.dev/apis/transaction#sendAda)

## Gửi nhiều tài sản đến địa chỉ

Chúng ta có thể xâu chuỗi một loạt `tx.sendAssets()` và `tx.sendLovelace()` để gửi nhiều nội dung cho nhiều người nhận. Ví dụ:

```javascript
import { Transaction, Asset } from "@meshsdk/core";

const tx = new Transaction({ initiator: wallet })
  .sendLovelace(
    "addr_test1vpvx0sacufuypa2k4sngk7q40zc5c4npl337uusdh64kv0c7e4cxr",
    "1000000"
  )
  .sendAssets(
    "addr_test1vpvx0sacufuypa2k4sngk7q40zc5c4npl337uusdh64kv0c7e4cxr",
    [
      {
        unit: "64af286e2ad0df4de2e7de15f8ff5b3d27faecf4ab2757056d860a424d657368546f6b656e",
        quantity: "1",
      },
    ]
  )
  .sendLovelace("ANOTHER ADDRESS HERE", "1500000");

const unsignedTx = await tx.build();
const signedTx = await wallet.signTx(unsignedTx);
const txHash = await wallet.submitTx(signedTx);
```

[thử bản trình diễn](https://meshjs.dev/apis/transaction#sendAssets)

## Gửi tài sản cho Handler

Chúng tôi có thể lấy địa chỉ của Tay cầm ADA với bất kỳ nhà cung cấp chuỗi khối nào và gọi hàm `fetchHandleAddress()` .

Chẳng hạn, hãy gửi một số dây buộc tình yêu tới `$jingles` :

```javascript
import { KoiosProvider, Transaction } from "@meshsdk/core";

const koios = new KoiosProvider("api");

const tx = new Transaction({ initiator: wallet }).sendLovelace(
  await koios.fetchHandleAddress("jingles"),
  "1000000"
);

const unsignedTx = await tx.build();
const signedTx = await wallet.signTx(unsignedTx);
const txHash = await wallet.submitTx(signedTx);
```

Kiểm tra [Sân chơi lưới](https://meshjs.dev/apis/transaction) để xem bản trình diễn trực tiếp và giải thích đầy đủ.
