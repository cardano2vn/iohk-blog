# Valentine upgrade FAQ
### **A set of frequently asked questions about the recent Valentine upgrade.**
![](img/2023-02-27-valentine-upgrade-faq.002.png) 27 February 2023![](img/2023-02-27-valentine-upgrade-faq.002.png)[ Fernando Sanchez](/en/blog/authors/fernando-sanchez/page-1/)![](img/2023-02-27-valentine-upgrade-faq.003.png) 3 mins read

![Fernando Sanchez](img/2023-02-27-valentine-upgrade-faq.004.png)[](/en/blog/authors/fernando-sanchez/page-1/)
### [**Fernando Sanchez**](/en/blog/authors/fernando-sanchez/page-1/)
Senior Technical Writer

Marketing and Communications

- ![](img/2023-02-27-valentine-upgrade-faq.005.png)[](mailto:fernando.sanchez@iohk.io "Email")
- ![](img/2023-02-27-valentine-upgrade-faq.006.png)[](https://www.linkedin.com/in/linkedinsanchezf/ "LinkedIn")

![Valentine upgrade FAQ](img/2023-02-27-valentine-upgrade-faq.007.png)

**Q** - **What does the Valentine intra-era hard fork achieve?**

**A** - To enable building efficient cross-chain applications, new built-in functions have been added to support ECDSA and Schnorr signatures along with Cardanoâ€™s native signature. Once implemented, these functions will become native to Cardano. An added advantage is that security audits by experts will ensure the highest possible level of security.

**Q** - **What is an intra-era hard fork?**

**A** - A small and focused semantic change to the ledger requiring a hard fork. It doesn't change the ledger era (eg, Babbage) though.

**Q** - **How do DApp developers benefit from the implementation of native ECDSA and Schnorr signatures on Cardano?**

**A** - These signatures are commonly used in other chains and are well understood, which means that DApp developers will enjoy a wider choice of multi-signature or threshold signature design and thus enhanced usability of Cardano. 

**Q** - **Why is a hard fork needed to add new built-in functions for Schnorr and ECDSA signatures with the SECP256k1 curve for Plutus scripts?**

**A** - This update requires a hard fork because of the changes needed for the Plutus interpreter. Because this is an intra-era hard fork, it does not change the ledger era, which means that this is an upgrade to the Babbage era (Vasil functionality).

**Q** - **What are cryptographic primitives?**

**A** - They are the underlying building blocks that DApp developers use to, for example, secure transactions/data, develop custom encryption and decryption algorithms, and validate messages through digital signatures.

**Q** - **Why has Elliptic Curve Cryptography (ECC) become so popular in the last few years?**

**A** - This technology is now the mainstream for developing cryptographic protocols and secure applications. ECC uses smaller keys and signatures for the same level of security and provides very fast key generation and agreement, and fast signatures.

**Q** - **Which cryptographic algorithm and elliptic curve do the Ethereum and Bitcoin chains use?**

**A** - Both chains use the ECDSA algorithm with the SECP256k1 elliptic curve.

**Q** - **Which elliptic curve does Cardano use with its signature algorithm?**

**A** - Cardano uses the Edwards-curve Digital Signature Algorithm (EdDSA) with elliptic curve Curve25519 as its base curve. It is thus referred to as Ed25519.

**Q** - **What is the advantage of adding built-in functions for Schnorr and ECDSA signatures with the SECP256k1 curve for Plutus scripts?**

**A** - Because Cardano uses EdDSA (unlike Ethereum and Bitcoin), DApp developers would need to spend time and resources to implement Schnorr and ECDSA signatures over the SECP elliptic curves in Plutus. Adding built-in functions to support Schnorr and ECDSA signatures with the SECP256k1 curve in Plutus scripts eliminates that burden, and also removes any potential security risks, since these curves are not native to Cardano.

**Q** - **Post-implementation, what can Plutus do better?**

**A** - Plutus can easily verify transactions from other blockchains using ECDSA and Schnorr standards. For example, Plutus can natively verify signatures generated in EVM sidechains, which will improve the developer experience in terms of process simplicity, cost, and advanced security.
