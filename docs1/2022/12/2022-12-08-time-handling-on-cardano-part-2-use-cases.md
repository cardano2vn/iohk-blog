# Time handling on Cardano, part 2: use cases
### **How Plutus, Marlowe, and Hydra address timekeeping on Cardano**
![](img/2022-12-08-time-handling-on-cardano-part-2-use-cases.002.png) 8 December 2022![](img/2022-12-08-time-handling-on-cardano-part-2-use-cases.002.png)[ Arnaud Bailly](/en/blog/authors/arnaud-bailly/page-1/)![](img/2022-12-08-time-handling-on-cardano-part-2-use-cases.003.png) 6 mins read

![Arnaud Bailly](img/2022-12-08-time-handling-on-cardano-part-2-use-cases.004.png)[](/en/blog/authors/arnaud-bailly/page-1/)
### [**Arnaud Bailly**](/en/blog/authors/arnaud-bailly/page-1/)
Technical Lead

Engineering

- ![](img/2022-12-08-time-handling-on-cardano-part-2-use-cases.005.png)[](mailto:arnaud.bailly@iohk.io "Email")
- ![](img/2022-12-08-time-handling-on-cardano-part-2-use-cases.006.png)[](https://linkedin.com/in/arnaudbailly "LinkedIn")
- ![](img/2022-12-08-time-handling-on-cardano-part-2-use-cases.007.png)[](https://twitter.com/dr_c0d3 "Twitter")
- ![](img/2022-12-08-time-handling-on-cardano-part-2-use-cases.008.png)[](https://github.com/abailly "GitHub")

![Time handling on Cardano, part 2: use cases](img/2022-12-08-time-handling-on-cardano-part-2-use-cases.009.jpeg)

*This blog post has been written by Arnaud Bailly, Michael Peyton Jones, Sebastian Nagel, Polina Vinogradova, and Brian Bush.*

The [previous post](https://iohk.io/en/blog/posts/2022/12/07/time-handling-on-cardano-part-1-about-ouroboros-and-the-importance-of-determinism/) discussed how Ouroboros handles time on Cardano and explained the importance of determinism. Here is more about specific use cases for time on Cardano.
## **How do Plutus scripts handle time?**
Plutus scripts get access to the transaction validity range, defined by its creator. When defining the validity range, a creator can decide that a transaction is valid from slot X to slot Y, or leave one or both of the bounds undefined. This imposes constraints into which slot a transaction can be included, which is very useful on-chain to define various 'contracts'.

The script can assume that the actual time of validation is in this range. Otherwise, the transaction will fail in [phase 1](https://iohk.io/en/blog/posts/2021/09/07/no-surprises-transaction-validation-part-2/) before script execution. This ensures determinism since the script will *always* see the same piece of information (the validity range) regardless of when the script is validated, so the behavior will be the same.

The limits of the validity interval are expressed in real time (POSIXTime), rather than slots, and the conversion from slots to real time is done by consensus, as discussed in the previous post. Using real time rather than slots is important because slot lengths can change at a hard fork, so assumptions based on counting slots are generally unreliable. The fact that scripts see the validity range allows the scripts to make assertions like 'the current time is before/after some given time', but it does not enable a script to make any other kind of assertion ('the second in which this transaction is validated is even', for example.)

In Alonzo's original design, the validity range covered all known uses of time, while also fitting neatly with the existing time-to-live (TTL) field. In theory, it is possible to apply the same principles to other kinds of assertions, for example â€“ let the script rely on assertions checked in phase 1. However, this would not be easy as it implies deep structural changes to various parts of the Cardano network. And because phase 1 checks need to be valid for every node across the network, this precludes any kind of assertion that depends on some local condition, like 'Current Time'.
## **Use cases for time**
Time has different applications in the Cardano ecosystem.
### **Hydra**
The Hydra protocol is dependent on time to compute and enforce the contestation deadline, which is a critical part of the protocol's safety mechanism. The Hydra Head state machine tracks the passage of time using UTCTime but the tick comes from the chain, based on the slot number observed from blocks produced by the chain. The reason for using UTCTime addresses the limitations inherent in the slot-to-time conversion the validity window imposes. One cannot convert a slot too far in the future, which means that it is simpler to use UTCTime off-chain and only do conversions when submitting/receiving transactions to or from the chain.

This implies that the tick's granularity is roughly 20s, as this is the expected frequency at which blocks are produced. Using this measure of time, Hydra is available to react to the protocol-relevant crossing of the contestation deadline.

What's important is that local time in the Hydra Head (and nodes) is tied to the on-chain time handled by Ouroboros (see [part 1](https://iohk.io/en/blog/posts/2022/12/07/time-handling-on-cardano-part-1-about-ouroboros-and-the-importance-of-determinism/) for more details). As Hydra is an isomorphic protocol, it is desirable to process 'timed transactions' also on layer 2 (see [issue #196](https://github.com/input-output-hk/hydra-poc/issues/196)). However, Hydra does not produce blocks, so the consensus itself does not need a notion of time (yet).

This requires an understanding of the precision and process of discretizing time on a layer 2 ledger. Although the complexities of handling time on-chain also apply to layer 2, layer 2 can provide better solutions since such networks are much smaller, have a shorter lifespan, and do not need to scale globally.

If you're interested in getting involved in discussions and sharing the types of applications you have and the resolution time they'd require, join this [Hydra Discord channel](https://discord.com/channels/826816523368005654/890903732462710836/890951034099335178).
### **Marlowe**
Marlowe is a domain-specific language (DSL) for writing financial and transactional contracts, nearly all of which involve time. A wide variety of standard financial contracts have been written in Marlowe, including most of the [ACTUS](https://www.actusfrf.org/) standard contracts (eg, loans, swaps, options, and derivatives). Furthermore, Marlowe supports a variety of non-financial contract types such as auctions, token swaps, and even games. Cardano's existing mechanisms for working with time dovetail nicely with Marlowe's semantics and provide Marlowe transactions with locality and determinism inherited from Plutus.

In Marlowe, contract's time typically appears in the deadlines and timeouts that constrain how the execution of the contract evolves, and this works perfectly with Cardano's validity intervals. The timeout logic is needed in a loan contract, for example, to handle the situation where a loan payment is missed: then different logic needs to be executed in order to impose a penalty, adjust the schedule of future payments, etc. Contracts may also directly use the time endpoints of the validity interval in numerical computations, perhaps to adjust future payment amounts based on when an early payment was received. The fact that time appears as an interval has little practical impact on Marlowe because the interval can be as short as the time taken from submitting a transaction to its appearing in a block on the Cardano network â€“ just a few minutes.
## **Solutions**
Cardano could potentially provide more accurate time-related data during transaction validation, such as the timestamp from the block producer at which the block was minted, converted from its slot, or even the actual timestamp in UTC with milliseconds precision. However, this would *break prospective determinism* (see [part 1](https://iohk.io/en/blog/posts/2022/12/07/time-handling-on-cardano-part-1-about-ouroboros-and-the-importance-of-determinism/)) as it does on protocols which do not include this feature: a user could no longer tell if a transaction can definitely apply to the ledger or not, because that would depend on the exact timestamp that the block producer used when creating the block.

Another option is adding various assertion kinds to transaction bodies beyond the validity interval. This is possible, but difficult as already outlined before, hence there needs to be a use case for these assertion kinds to be useful.

Finally, layer 2 networks such as Hydra, can provide increased accuracy through shorter 'slot length' and shorter validity range, alongside decreased latency in transactions finality. Note that the current Hydra Head implementation does not *yet* provide that level of flexibility.
## **Conclusion**
Time *is* a complex topic, especially in a decentralized blockchain setting. These blog posts show that there is a clear notion of on-chain time on Cardano with specific constraints and available improvement options in the longer term.

On-chain time behaves in a somewhat different way from the time in traditional software. This divergence is defined in a consistent way to address system constraints while ensuring security and usability for end-users and stake pool operators. Moreover, Cardano's measure of time appears to be good enough to cover multiple use cases, even when compared to traditional finance uses.

Join [Discord community channels](https://discord.com/channels/826816523368005654/826816523964383263) for further discussions of time handling on Cardano and potential use cases that were not mentioned in these posts.
