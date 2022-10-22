# A Brief Note on Provable Security in Cryptocurrencies
![](img/2016-09-22-a-brief-note-on-provable-security-in-cryptocurrencies.002.png) 22 September 2016![](img/2016-09-22-a-brief-note-on-provable-security-in-cryptocurrencies.002.png)[ Mario Larangeira](/en/blog/authors/mario-larangeira/page-1/)![](img/2016-09-22-a-brief-note-on-provable-security-in-cryptocurrencies.003.png) 5 mins read

![](img/2016-09-22-a-brief-note-on-provable-security-in-cryptocurrencies.004.png)[ A Brief Note on Provable Security in Cryptocurrencies - Input Output - HongKong](https://ucarecdn.com/b0b08864-d4e2-40ed-9ea6-21f9ff33b560/-/inline/yes/ "A Brief Note on Provable Security in Cryptocurrencies - Input Output - HongKong")

![Mario Larangeira](img/2016-09-22-a-brief-note-on-provable-security-in-cryptocurrencies.005.png)[](/en/blog/authors/mario-larangeira/page-1/)
### [**Mario Larangeira**](/en/blog/authors/mario-larangeira/page-1/)
Research Fellow

Academic Research

- ![](img/2016-09-22-a-brief-note-on-provable-security-in-cryptocurrencies.006.png)[](mailto:mario.larangeira@iohk.io "Email")
- ![](img/2016-09-22-a-brief-note-on-provable-security-in-cryptocurrencies.007.png)[](https://www.youtube.com/watch?v=LUUFbGB-vyg "YouTube")
- ![](img/2016-09-22-a-brief-note-on-provable-security-in-cryptocurrencies.008.png)[](https://jp.linkedin.com/in/larangeira "LinkedIn")

![A Brief Note on Provable Security in Cryptocurrencies](img/2016-09-22-a-brief-note-on-provable-security-in-cryptocurrencies.009.jpeg)

This post tries to give a short overview of provable security in cryptocurrencies.
### **Provable Security**
Provable security is a relatively new area within the cryptography discipline. The first papers in the modern cryptography (the one that starts from the seventies until now) do not have a rigorous security analysis. That is, with the exception of citation of concrete attacks, there is no attempt to meticulously formalize the adversary power and capabilities.

For example, the paper "New Directions in Cryptography" by Whitfield Diffie and Martin Hellman, which is considered by most the beginning of modern cryptography (at least the public and civilian one), does not provide such rigorous analysis.

The publications from the cryptographic research community of today illustrate a startling difference from that era. In almost every relevant conference or journal, it is required from the authors a security analysis. With special care when the work proposes a new cryptographic scheme or claim improvements. Today, a new scheme or protocol without a proof of security in its original publication will hardly be accepted.

In the context of cryptocurrencies such evolution can be observed too. However, before going to that topic, it is convenient to review briefly what we mean by "adversary power and capabilities" mentioned earlier.
### **Class of Attacks**
A somewhat naive approach is to rely on the observation of the impossibility of a concrete attack. Unfortunately, provable security is a subtle topic. Such approach would just be true for that particular concrete attack. In other words, it does not necessarily tell us anything about small variants or maybe different parameter values involved in the attack.

A more systematic, and therefore more preferable, approach is to design a formal model of the adversary capabilities. The goal of such a design is to construct a model attack as inclusive as possible. That is, a model which would capture as much concrete attacks as possible. Thereby giving us, in fact, a class of attacks.

The construction of such a model is not the end. What we actually want is to show (and prove) an upper bound in the probability of success of the adversary in that class of attacks. Needless to say, that the proof should show that such bound is small (more theoretical people should argue about what "small" means, but let skip this discussion in this post).

The way of computing such a bound is in fact what has been developed for the past decades for numerous cryptographic schemes and it involves computation assumptions, primitive models information theory and etc (and it is better drop it here, because it deserves a post on its own right). Needless to say that in this process some degree of generalization and simplification takes place. In the end the result is often called "the model."

The model is what ultimately is going to be analyzed not the system. Therefore, the construction of the model and the assurance that it is reasonable, i.e., is based as close as possible on reality, is of prime importance in provable security.

As an example, in the case of the public-key encryption schemes, one classic attack model is named CPA, which stands for Chosen-Plaintext Attack. This class of attacks embraces all the attacks that the adversary can obtain, somehow, ciphertexts from any plaintexts of its (finite) choices. By the end of that interaction, the adversary is assumed to output some value under a certain probability. For example, the correct secret-key or a valid ciphertext.

The reader should keep in mind that CPA is only one class. Other models can be devised and indeed have been proposed already, i.e., when the adversary has access to encrypted texts (instead of the plaintexts) given its choice of plaintext, as happens in the CCA (Chosen-Ciphertext Attack) a more powerful class of attacks. And there are several others.
### **Adversary Model in Cryptocurrency**
While the public-key encryption scheme is a cryptographic primitive, a cryptocurrency is a protocol. Furthermore, a ledger based cryptocurrency imposes to the participants that they agree on the ledger state in order to validate transactions. Here, once again, to give a proper treatment in the study the security of the protocol means to explicitly model the adversary power and capabilities.

The comparison between protocols and primitives brings us a couple of differences, which should be taken into account. For example, a protocol requires the participants to exchange messages over the network, hence it is necessary to take a closer look on how the adversary behaves in the presence of these messages. The adversary can see the contents of the message? Can it block them for some time or indefinitely? All these particular cases translate into different constrained scenarios which ultimately gives us different capabilities of the protocol.

Good examples of these research variants are [The Bitcoin Backbone Protocol: Analysis and Applications](/en/research/library#IPQHNW2R) and [Analysis of the Blockchain Protocol in Asynchronous Networks](/en/research/library#8WP4QF65). They respectively study proof-of-work in the synchronous (the messages cannot be blocked) and asynchronous (can be blocked for some time) settings. A more recent work is about the formalization of the proof-of-stake based protocol [A Provably Secure Proof-of-Stake Blockchain Protocol](/en/research/library#9BKRHCSI) in synchronous.

For further reading on models and provable security, we refer the reader to a few more papers with a heavy load of cryptography theory.

[Random Oracles in Constantinople: Pratical Asynchronous Byzantine Agreement Using Cryptography](/en/research/library#7A537TWI)

[Zero Knowledge in the Random Oracle model, Revisited](/en/research/library#XTGGH9TQ)
## **Attachments**
![](img/2016-09-22-a-brief-note-on-provable-security-in-cryptocurrencies.004.png)[ A Brief Note on Provable Security in Cryptocurrencies - Input Output - HongKong](https://ucarecdn.com/b0b08864-d4e2-40ed-9ea6-21f9ff33b560/-/inline/yes/ "A Brief Note on Provable Security in Cryptocurrencies - Input Output - HongKong")
