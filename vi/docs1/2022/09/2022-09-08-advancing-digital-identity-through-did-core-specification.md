# Cải tiến định danh kỹ thuật số thông qua đặc tả cốt lõi của DID

### **The recent DID core specification approval at the World Wide Web Consortium (W3C) provided clearer and stronger foundations for identity platforms building decentralized identifiers.**

![](img/2022-09-08-advancing-digital-identity-through-did-core-specification.002.png) 8 tháng 9 năm 2022 ![](img/2022-09-08-advancing-digital-identity-through-did-core-specification.002.png) [Ivan Irakoze](/en/blog/authors/ivan-irakoze/page-1/) ![](img/2022-09-08-advancing-digital-identity-through-did-core-specification.003.png) 4 phút đọc

![Ivan Irakoze](img/2022-09-08-advancing-digital-identity-through-did-core-specification.004.png)[](/en/blog/authors/ivan-irakoze/page-1/)

### [**Ivan Irakoze**](/en/blog/authors/ivan-irakoze/page-1/)

Blog/Feature Writer

Marketing &amp; Communication

- ![](img/2022-09-08-advancing-digital-identity-through-did-core-specification.005.png)[](mailto:ivan.irakoze@iohk.io "Email")
- ![](img/2022-09-08-advancing-digital-identity-through-did-core-specification.006.png)[](https://twitter.com/The_ADA_Poet "Twitter")

![Cải tiến nhận dạng kỹ thuật số thông qua đặc điểm kỹ thuật cốt lõi của DID](img/2022-09-08-advancing-digital-identity-through-did-core-specification.007.jpeg)

In June 2022, the World Wide Web Consortium (W3C) approved theÂ [Decentralized Identifier (DID) Working Group](https://www.w3.org/2020/12/did-wg-charter.html)â€™s DID core specification to move to the W3C Recommendation stage. This milestone reaffirms the rising relevance ofÂ **digital identity**Â and provides clearer and stronger foundations for identity platforms such asÂ [Atala PRISM](https://www.atalaprism.io/#why).

Here, we look at:

- what digital identity and DIDs are.
- what DID core specification approval means for digital identity.

## **What is digital identity?**

To define digital identity, we must first understand all that identity entails.

[Danh tính](https://atala.mymidnight.blog/ssi-fundamentals-i-identity/) bao gồm tất cả các đặc điểm không thay đổi mô tả chúng ta là ai, chẳng hạn như dân tộc, ngày sinh, dòng dõi, v.v. và các đặc điểm có thể thay đổi như nghề nghiệp, danh tính trực tuyến của chúng ta, v.v.

Typically we only consider individuals as having an identity, but other entities like organizations, businesses, and digital and physical things can also have unique identifying characteristics.

[Digital identity](https://www.essentialcardano.io/article/digital-identity)Â is an online representation of entities and the claims about who or what they are.Â **Verifiable Credentials (VCs)**Â represent these claims in the digital world, similar to the physical documents we use today.

Entities, whether individuals or organizations, use these VCs to share information with other entities. This exchange of information presents two important questions regarding security:

- How safe is it to share identifying information with other entities?
- Who controls the data?

Trong thời đại internet, các công ty khác nhau thu thập một lượng lớn thông tin (thường là thông tin cá nhân) cho những mục đích ngoài tầm kiểm soát của chúng ta, điều đó khiến việc bảo mật danh tính của chính chúng ta trở nên quan trọng. Do đó  "Định danh tự chủ" (Self-sovereign Identity - SSI) và "Danh tính phi tập trung" (Decentralized Identifiers - DIDs) ra đời.

## **What are self-sovereign identities and decentralized identifiers?**

SSI [ là một tập hợp các nguyên tắc](https://github.com/WebOfTrustInfo/self-sovereign-identity/blob/master/self-sovereign-identity-principles.md) đòi hỏi phải có đặc quyền không thể chối cãi để kiểm soát thông tin cá nhân mà bạn chia sẻ với người khác.

[DIDs](https://atala.mymidnight.blog/ssi-fundamentals-iii-dids/)Â are an important aspect of aÂ [decentralized identity](https://www.essentialcardano.io/glossary/decentralized-identity)Â platform. Algorithms produce unique, random strings of characters. When exchanged with a peer, DIDs create a secure channel that enables bidirectional communication. Every DID is effectively a pseudonym, and the user has complete control of their data, and with whom they share it.

The Working Groupâ€™s DID core specification defines a DID, its components, and its functional methods. According to the DID Working Group, DIDs:

- Are controlled by the entities that hold them.
- Enable cryptographic authentication of the DID holder.
- Describe the discovery of information needed to launch secure and privacy-preserving communication methods.
- Give access to service-independent data portability.

## **What does DID core specification approval mean for digital identity?**

DID core specification approval by the W3C Director standardizes DIDs, ensuring that DID technology is accepted by all invested parties and can begin moving towards wider adoption.

Mặc dù [Google, Apple và Mozilla chính thức phản đối việc cải tiến thông số kỹ thuật DID](https://www.w3.org/2019/did-wg/faqs/2021-formal-objections/) , [Giám đốc W3C tuyên bố rằng](https://www.w3.org/2022/06/DIDRecommendationDecision.html) :

*Nếu đặc tả cốt lõi về DID không chuyển sang giai đoạn Khuyến nghị, điều này sẽ làm giảm động lực cho các nhà thiết kế hệ thống định danh phi tập trung khác, dẫn tới họ có thể tuân theo sự thống nhất của một nhóm người được thuê để tạo ra một sản phẩm trong lĩnh vực này. Người ta có thể dễ dàng thấy trước không cần thiết phải triển khai các kế hoạch [URI](https://www.techtarget.com/whatis/definition/URI-Uniform-Resource-Identifier) khác làm phức tạp hóa khả năng tương tác mà cộng đồng đã và đang làm việc để giải quyết. Và kết luận rằng sự cân bằng nằm ở lợi ích của cộng đồng các nhà phát triển DID, khuyến khích họ tiếp tục công việc của mình và tìm kiếm sự đồng thuận về các phương pháp DID tiêu chuẩn. Các phản đối đã bị bác bỏ. Đặc tả cốt lõi của DID được chấp thuận để chuyển sang giai đoạn Khuyến nghị W3C.*

This decision enablesÂ **the standardization of a universal template**Â that allowsÂ **interoperability**Â andÂ **portability**. Without standardization, DIDs and VCs created by different DID methods might not be readable by verifiers or storable in a single identity wallet.

W3C Recommendation status of the DID core specification, therefore, codifies the work of hundreds of people diligently working on improving the digital identity framework.

The next step in the process outlined by the W3C Director is for the Working Group toÂ *â€œaddress and deliver proposed standard DID method(s) and demonstrate interoperable implementations.â€*

## **Tìm hiểu thêm về Atala PRISM**

Input Output Global, Inc. (IOG) liên tục nghiên cứu và xây dựng các sản phẩm và dịch vụ thông qua công nghệ blockchain. Một trong những sản phẩm này là **Atala PRISM** - một nền tảng định danh kỹ thuật số được xây dựng trên các nguyên tắc SSI và một bộ dịch vụ dành cho dữ liệu có thể xác minh và danh tính kỹ thuật số, được xây dựng trên blockchain Cardano.

Xem video giải thích bên dưới để tìm hiểu thêm về Atala PRISM.

*Tôi muốn gửi lời cảm ơn [Peter Vielhaber](https://iohk.io/en/team/pete-vielhaber) đã đóng góp ý kiến và hỗ trợ cho bài đăng trên blog cộng tác này. Bài này được dịch bởi Vũ Đình Quân, Review bởi Quang Pham, Biên tập bởi .... Bài viết nguồn [tại đây](https://iohk.io/en/blog/posts/2022/09/08/advancing-digital-identity-through-did-core-specification). *Dự án này được tài trợ bởi Catalyst**
