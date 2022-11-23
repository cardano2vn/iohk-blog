# What is SECP and how it drives cross-chain development on Cardano
### **New cryptographic primitives are coming to Cardano to enable secure, cross-chain DApp development**
![](img/2022-11-03-what-is-secp-and-how-it-drives-cross-chain-development-on-cardano.002.png) 3 November 2022![](img/2022-11-03-what-is-secp-and-how-it-drives-cross-chain-development-on-cardano.002.png)[ Olga Hryniuk](/en/blog/authors/olga-hryniuk/page-1/)![](img/2022-11-03-what-is-secp-and-how-it-drives-cross-chain-development-on-cardano.003.png) 3 mins read

![Olga Hryniuk](img/2022-11-03-what-is-secp-and-how-it-drives-cross-chain-development-on-cardano.004.png)[](/en/blog/authors/olga-hryniuk/page-1/)
### [**Olga Hryniuk**](/en/blog/authors/olga-hryniuk/page-1/)
Senior Technical Writer

Marketing & Communications

- ![](img/2022-11-03-what-is-secp-and-how-it-drives-cross-chain-development-on-cardano.005.png)[](https://www.linkedin.com/in/olga-hryniuk-1094a3160/ "LinkedIn")
- ![](img/2022-11-03-what-is-secp-and-how-it-drives-cross-chain-development-on-cardano.006.png)[](https://github.com/olgahryniuk "GitHub")

![What is SECP and how it drives cross-chain development on Cardano](img/2022-11-03-what-is-secp-and-how-it-drives-cross-chain-development-on-cardano.007.png)

Cryptography plays an integral role in the blockchain space, ensuring trust and security between network participants. 

DApp developers can use *cryptographic primitives* as the building blocks to create secure transactions containing sensitive data, develop custom encryption and decryption algorithms, and validate such by using digital signatures. 

In recent decades, Elliptic Curve Cryptography (ECC) has become the de facto primitive for developing cryptographic protocols and secure applications. ECC provides the same level of security as other mechanisms while using shorter keys and signatures.

**What is SECP?**

SECP, or SECP256k1 in particular, is the name of the elliptic curve. Many blockchains (including Bitcoin, Ethereum, and Binance Coin) use this curve to implement public key cryptography, which uses a key pair (public and private keys) to validate transaction signatures. 

Examples of SECP include the Elliptic Curve Digital Signature Algorithm (ECDSA) and Schnorr signatures. These allow users to verify the integrity of specific signed hashed data. ECDSA and Schnorr signature algorithms work with the SECP256k1 curve in many blockchains.
## **Cryptography on Cardano**
Cardano uses the Edwards-curve Digital Signature Algorithm (EdDSA) with elliptic curve25519 as its native signature algorithm.

This means that Plutus DApp developers who want to work with other blockchains and need to validate ECDSA and Schnorr signatures would have to spend time, effort, and funds to implement such SECP elliptic curves in Plutus. Additionally, this considerably increases potential security risks. Since ECDSA and Schnorr arenâ€™t native to Cardano, such operations would be more expensive and time-consuming *unless provided as built-in functions*.

**Adding new built-in functions to Plutus**

To enable building cross-chain applications efficiently, Input Output Global (IOG) is adding new built-in functions to support ECDSA and Schnorr signatures along with Cardanoâ€™s native signature.

These built-in functions will become native to Cardano, and since they will be implemented and audited by experts, they will provide the highest level of security. This will allow any Plutus DApp developer to widen the choice of multi-signature or threshold signature design to use. In particular, Schnorr-based designs are well understood and widely used by the DApp community.

[CIP-49](https://github.com/mlabs-haskell/CIPs/blob/c5bdd66fe49c19c341499f86cebaa2eef9e90b74/CIP-0049/README.md) provides a more in-depth oversight of the motivation and specification for the new implementation of built-in functions. These changes affect the Plutus interpreter, so implementation will require a hard fork combinator event. To find out more about this requirement, read [CIP implementation specifics](https://github.com/cardano-foundation/CIPs/tree/master/CIP-0035#types-of-release).
## **How will new cryptographic primitives work?**
![SECP on Cardano](img/2022-11-03-what-is-secp-and-how-it-drives-cross-chain-development-on-cardano.008.png)

Fï»¿igure 1. How SECP cryptographic primitives will work on Cardano

After the new cryptographic primitives implementation, Plutus will be able to easily verify transactions from other blockchains using ECDSA and Schnorr standards. For example, Plutus will be able to natively verify signatures generated in EVM sidechains, which will improve the developer experience in terms of process simplicity, cost, and advanced security.

Community feedback indicated how the addition of new cryptographic primitives would improve the process of secure and efficient cross-chain DApp development on Cardano. Learning from the Vasil upgrade, IOG teams have [done a lot of work](https://youtu.be/hZRwLWKNNfQ?t=257) refining the release process and are utilizing this for the SECP release. The community is already helping to test this new functionality, which will initially be deployed on the Cardano devnet. From that point, the functionality will undergo continuous testing on preview and pre-production environments. Once the community is comfortable that test benchmarks have been achieved and critical indicators have been met, IOG will propose a date of mainnet deployment via a hard fork combinator event.

To stay abreast of developments, please join IOGâ€™s developer [Discord channels](https://discord.com/channels/826816523368005654/826816523964383263).

Iâ€™d like to thank Inigo Querejeta Azurmendi, Nigel Hemsley, and Mark Irwin for their input and support in preparing this blog post.
