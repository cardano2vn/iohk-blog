---
id: bắt đầu
sidebar_position: '2'
title: Bắt đầu   - SDK lưới (Thư viện nguồn mở để xây dựng ứng dụng Web3 trên Chuỗi khối Cardano)
sidebar_label: Bắt đầu
description: Bắt đầu với Lưới
image: "../img/og/og-getstarted-mesh.png"
---

Có nhiều cách để bắt đầu với Lưới:

- [Bộ công cụ dành cho người mới bắt đầu](#starter-kits)
- [hướng dẫn](#guides)
- [Di chuyển hoặc cài đặt thủ công](#migration-manual-installation)

## Bộ công cụ dành cho người mới bắt đầu

Cách dễ nhất để bắt đầu với Lưới là sử dụng một trong [các Bộ công cụ dành cho người mới bắt đầu](https://meshjs.dev/starter-templates) .

Ví dụ: nếu bạn là một dự án NFT và muốn bắt đầu trang web đúc tiền đa chữ ký của riêng mình, bạn có thể sử dụng [Bộ khởi động đúc tiền đa chữ ký](https://minting-template.meshjs.dev/) .

Hoặc, nếu bạn là nhà điều hành nhóm cổ phần, [Bộ khởi động cổng thông tin nhà điều hành nhóm](https://staking-template.meshjs.dev/) này cho phép người được ủy quyền kết nối ví và cổ phần của họ với nhóm của bạn.

Khám phá và chọn từ bộ sưu tập [Bộ công cụ dành cho người mới bắt](https://meshjs.dev/starter-templates) đầu mã nguồn mở.

### Cài đặt với CLI

Để bắt đầu cài đặt, hãy mở Terminal của bạn và chạy lệnh CLI sau:

```shell
npx create-mesh-app your-app name
```

Bạn sẽ được nhắc với một số câu hỏi, bạn có thể chọn một trong các mẫu, chọn một khung và chọn ngôn ngữ bạn chọn. Toàn bộ quá trình sẽ mất ít hơn 1 phút.

### Demeter

Bắt đầu dự án của bạn trên [Demeter](https://demeter.run) , chỉ với một nút bấm:

1. Truy cập [Bộ công cụ dành cho người mới bắt đầu](https://meshjs.dev/starter-templates)
2. Chọn một trong các mẫu
3. Nhấp vào *Demeter* để bắt đầu một phiên bản dự án

### Sao chép repo GitHub

Mọi mẫu khởi động đều là mã nguồn mở, bạn có thể sao chép chúng từ [GitHub](https://github.com/MeshJS) :

1. Truy cập [Bộ công cụ dành cho người mới bắt đầu](https://meshjs.dev/starter-templates)
2. Chọn một trong các mẫu
3. Nhấp vào *GitHub Repo* để chuyển đến kho lưu trữ GitHub
4. Sao chép kho lưu trữ

## hướng dẫn

Cho dù bạn là người mới trong lĩnh vực phát triển web hay nhà phát triển full-stack blockchain dày dạn kinh nghiệm, những hướng dẫn này sẽ giúp bạn bắt đầu.

[Duyệt qua tất cả các hướng dẫn](https://meshjs.dev/guides) |
--- | ---
[Bắt đầu một ứng dụng Web3 trên Next.js](https://meshjs.dev/guides/nextjs) | Hướng dẫn từng bước để thiết lập ứng dụng web Next.js, kết nối ví và duyệt nội dung của ví.
[Đúc tiền trên Node.js](https://meshjs.dev/guides/minting-on-nodejs) | Tải khóa do CLI tạo và tài sản đúc trên Node.js
[Giao dịch đa chữ ký (đúc tiền)](https://meshjs.dev/guides/multisig-minting) | Tạo giao dịch multi-sig và đúc NFT
[Sử dụng Hợp đồng thông minh với Lưới](https://meshjs.dev/guides/smart-contract) | Hướng dẫn từng bước để tích hợp Hợp đồng thông minh Cardano của bạn với ứng dụng web.
[Chứng minh quyền sở hữu ví bằng mật mã](https://meshjs.dev/guides/prove-wallet-ownership) | Chứng minh bằng mật mã quyền sở hữu của ví bằng cách ký một phần dữ liệu bằng ký hiệu dữ liệu.

## Cài đặt thủ công di chuyển

Nếu bạn đang muốn sử dụng Lưới vào dự án hiện tại của mình, bạn có thể chọn ngăn xếp và định cấu hình chúng.

[Duyệt qua tất cả các ngăn xếp](https://meshjs.dev/migration-manual-installation) |
--- | ---
[Tiếp theo.js](https://meshjs.dev/migration-manual-installation#nextjs) | Khung phát triển web do Vercel tạo cho phép các ứng dụng web dựa trên React với kết xuất phía máy chủ
[NestJS](https://meshjs.dev/migration-manual-installation#nestjs) | Khung cho các ứng dụng phía máy chủ
[Gatsby](https://meshjs.dev/migration-manual-installation#gatsby) | Trình tạo trang tĩnh được xây dựng trên Node.js bằng React và GraphQL
[gói web](https://meshjs.dev/migration-manual-installation#webpack) | Một gói mô-đun cho JavaScript.

## Guides

Whether you are new to web development or a seasoned blockchain full-stack developer, these guides will help you get started.

| [Browse all guides](https://meshjs.dev/guides) | |
|--|--|
| [Start a Web3 app on Next.js](https://meshjs.dev/guides/nextjs) | A step-by-step guide to setup a Next.js web application, connect wallet and browse wallet's assets. |
| [Minting on Node.js](https://meshjs.dev/guides/minting-on-nodejs) | Load a CLI generated key and mint assets on Node.js |
| [Multi-Signatures Transaction (Minting)](https://meshjs.dev/guides/multisig-minting) | Create a multi-sig transaction and mint NFTs|
| [Use Smart Contract with Mesh](https://meshjs.dev/guides/smart-contract) | A step-by-step guide to integrate your Cardano Smart Contract to a web application. |
| [Cryptographically Prove Wallet Ownership](https://meshjs.dev/guides/prove-wallet-ownership) | Cryptographically prove the ownership of a wallet by signing a piece of data using data sign. |

## Migration Manual Installation

If you are looking to use Mesh into your existing project, you can choose the stack and configure them.

| [Browse all stacks](https://meshjs.dev/migration-manual-installation) | |
|--|--|
| [Next.js](https://meshjs.dev/migration-manual-installation#nextjs) | Web development framework created by Vercel enabling React-based web applications with server-side rendering |
| [NestJS](https://meshjs.dev/migration-manual-installation#nestjs) | Framework for server-side applications |
| [Gatsby](https://meshjs.dev/migration-manual-installation#gatsby) | Static site generator built on top of Node.js using React and GraphQL |
| [Webpack](https://meshjs.dev/migration-manual-installation#webpack) | A module bundler for JavaScript. |
