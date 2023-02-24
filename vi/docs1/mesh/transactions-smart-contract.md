---
id: transactions-smart-contract
sidebar_position: '5'
title: Giao dịch hợp đồng thông minh   - SDK lưới (Thư viện nguồn mở để xây dựng ứng dụng Web3 trên chuỗi khối Cardano)
sidebar_label: Giao dịch hợp đồng thông minh
description: Tạo giao dịch để làm việc với hợp đồng thông minh.
image: "../img/og/og-getstarted-mesh.png"
---

Trong phần này, chúng ta sẽ xem xét cách tạo giao dịch để làm việc với hợp đồng thông minh. Nếu bạn chưa quen với giao dịch, hãy nhớ xem cách tạo giao dịch để [gửi lovelace và tài sản](transactions-basic) .

Trong phần này, chúng ta sẽ khám phá những điều sau đây:

- [Khóa tài sản trong hợp đồng thông minh](#lock-assets-in-smart-contract)
- [Mở khóa tài sản từ Hợp đồng thông minh](#unlock-assets-from-smart-contract)
- [Đúc tài sản với hợp đồng thông minh](#minting-assets-with-smart-contract)

## Khóa tài sản trong hợp đồng thông minh

Token locking is a feature where certain assets are reserved on the smart contract. The assets can only be unlocked when certain conditions are met, for example, when making a purchase.

Để khóa tài sản trong hợp đồng luôn thành công:

```javascript
import { Transaction } from "@meshsdk/core";

// this is the script address of always succeed contract
const scriptAddress = "addr_test1wpnlxv2xv9a9ucvnvzqakwepzl9ltx7jzgm53av2e9ncv4sysemm8";

const tx = new Transaction({ initiator: wallet }).sendAssets(
  {
    address: scriptAddress,
    datum: {
      value: "supersecret",
    },
  },
  [
    {
      unit: "64af286e2ad0df4de2e7de15f8ff5b3d27faecf4ab2757056d860a424d657368546f6b656e",
      quantity: "1",
    },
  ]
);

const unsignedTx = await tx.build();
const signedTx = await wallet.signTx(unsignedTx);
const txHash = await wallet.submitTx(signedTx);
```

[thử bản trình diễn](https://meshjs.dev/apis/transaction/smart-contract#lockAssets)

## Mở khóa tài sản từ Hợp đồng thông minh

As we may have locked assets in the contract, you can create transactions to unlock the assets with a redeemer that corresponds to the datum. Define the corresponding code to create the datum, only a transaction with the corrent datum hash is able to unlock the asset. Define the unit of the locked asset to search for the UTXO in the smart contract, which is required for the transaction's input.

```javascript
async function _getAssetUtxo({ scriptAddress, asset, datum }) {
  const koios = new KoiosProvider("preprod");

  const utxos = await koios.fetchAddressUTxOs(scriptAddress, asset);

  const dataHash = resolveDataHash(datum);

  let utxo = utxos.find((utxo: any) => {
    return utxo.output.dataHash == dataHash;
  });

  return utxo;
}

// fetch input UTXO
const assetUtxo = await _getAssetUtxo({
  scriptAddress: "addr_test1wpnlxv2xv9a9ucvnvzqakwepzl9ltx7jzgm53av2e9ncv4sysemm8",
  asset: "64af286e2ad0df4de2e7de15f8ff5b3d27faecf4ab2757056d860a424d657368546f6b656e",
  datum: "supersecret",
});

// get wallet change address
const address = await wallet.getChangeAddress();

// create the unlock asset transaction
const tx = new Transaction({ initiator: wallet })
  .redeemValue({
    value: assetUtxo,
    script: {
      version: "V1",
      code: "4e4d01000033222220051200120011",
    },
    datum: "supersecret",
  })
  .sendValue(address, assetUtxo) // address is recipient address
  .setRequiredSigners([address]);

const unsignedTx = await tx.build();
// note that the partial sign is set to true
const signedTx = await wallet.signTx(unsignedTx, true);
const txHash = await wallet.submitTx(signedTx);
```

[thử bản trình diễn](https://meshjs.dev/apis/transaction/smart-contract#unlockAssets)

## Đúc tài sản với hợp đồng thông minh

We can use a Plutus Script to mint tokens. This script is designed to always succeed, meaning that anyone can sign and mint tokens with it, as there are no validation on this script.

```javascript
import {
  Transaction,
  AssetMetadata,
  Mint,
  Action,
  PlutusScript,
} from "@meshsdk/core";

const script: PlutusScript = {
  code: plutusMintingScriptCbor,
  version: "V2",
};

const redeemer: Partial<Action> = {
  tag: "MINT",
};

const tx = new Transaction({ initiator: wallet });

const assetMetadata1: AssetMetadata = {
  name: "Mesh Token",
  image: "ipfs://QmRzicpReutwCkM6aotuKjErFCUD213DpwPq6ByuzMJaua",
  mediaType: "image/jpg",
  description: "This NFT is minted by Mesh (https://meshjs.dev/).",
};
const asset1: Mint = {
  assetName: "MeshToken",
  assetQuantity: "1",
  metadata: assetMetadata1,
  label: "721",
  recipient: "addr_test1vpvx0sacufuypa2k4sngk7q40zc5c4npl337uusdh64kv0c7e4cxr",
};
tx.mintAsset(script, asset1, redeemer);

const unsignedTx = await tx.build();
const signedTx = await wallet.signTx(unsignedTx);
const txHash = await wallet.submitTx(signedTx);
```

Kiểm tra [Sân chơi lưới](https://meshjs.dev/apis/transaction/smart-contract) để xem bản trình diễn trực tiếp và giải thích đầy đủ.
