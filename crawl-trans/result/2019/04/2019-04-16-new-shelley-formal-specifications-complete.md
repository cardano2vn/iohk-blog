# New Shelley formal specifications complete
### **Formal specifications for delegation and incentives published**
![](img/2019-04-16-new-shelley-formal-specifications-complete.002.png) 16 April 2019![](img/2019-04-16-new-shelley-formal-specifications-complete.002.png)[ Philipp Kant](/en/blog/authors/philipp-kant/page-1/)![](img/2019-04-16-new-shelley-formal-specifications-complete.003.png) 3 mins read

![Philipp Kant](img/2019-04-16-new-shelley-formal-specifications-complete.004.png)[](/en/blog/authors/philipp-kant/page-1/)
### [**Philipp Kant**](/en/blog/authors/philipp-kant/page-1/)
Formal Methods Director

Engineering

- ![](img/2019-04-16-new-shelley-formal-specifications-complete.005.png)[](https://www.linkedin.com/in/dr-philipp-kant-4972b1a3 "LinkedIn")
- ![](img/2019-04-16-new-shelley-formal-specifications-complete.006.png)[](https://twitter.com/philipp_kant "Twitter")
- ![](img/2019-04-16-new-shelley-formal-specifications-complete.007.png)[](https://github.com/kantp "GitHub")

![New Shelley formal specifications complete](img/2019-04-16-new-shelley-formal-specifications-complete.008.jpeg)

The goal of the Cardano [Shelley](https://cardanoroadmap.com/ "cardanoroadmap.com") era is to bring full decentralization to Cardano, moving beyond the federated epoch and handing control of the ledger over to the community via stake pools.Â  As part of the process of delivering Shelley, we create formal specifications which allow us to verify that the final code is in line with what the researchers initially envisaged in their publications. By creating implementation-independent specifications, we can build components of the system using different languages, confident that they will work together. 

We are pleased to announce that we have successfully reached an important milestone in the Shelley journey, with the key specifications now completed. The finished specifications are as follows:

- [Engineering Design Specification For Delegation and Incentives In Cardano-Shelley](https://hydra.iohk.io/build/790053/download/1/delegation_design_spec.pdf "Delegation Design Spec, hydra.iohk.io"): Describes the requirements and design for the delegation and incentive mechanisms to be used in the Shelley release of Cardano.
- [A Formal Specification of the Cardano Ledger](https://hydra.iohk.io/build/789825/download/1/ledger-spec.pdf "Ledger Specification, hydra.iohk.io"): Specifies the ledger rules for Shelley, including delegation and incentives.
- [A Specification of the Non-Integral Calculations in the Ledger](https://hydra.iohk.io/build/779843/download/1/non-integer-calculations.pdf "Non-integer calculations, hydra.iohk.io"): This document defines a way to exactly calculate non-integral calculations in the ledger for Shelley which use elementary mathematical functions. The main objective is to provide an unambiguous specification that gives the same results, independent of the architecture or programming language to prevent chain forks because of slight differences in calculated results.

To provide a smooth transition from the Byron era to the Shelley era, the Shelley code will have to be compatible with the Byron rules. To enable this, we have created specifications for the Byron era as well:

- [A Formal Specification of the Cardano Ledger for the Byron release](https://hydra.iohk.io/build/793054/download/1/ledger-spec.pdf "A Formal Specification of the Cardano Ledger, hydra.iohk.io"): This document defines the rules for extending a ledger with transactions, as implemented in the Byron release of the Cardano Ledger.
- [Specification of the Blockchain Layer (Byron)](https://hydra.iohk.io/build/761704/download/1/blockchain-spec.pdf "Specification of the Blockchain Layer, hydra.iohk.io"): This document defines inference rules for operations on a blockchain as a specification of the blockchain layer of Cardano in the Byron release and in a transition to the Shelley release.

The process of implementing these specifications in production code is well underway, and the specifications will continue to improve with feedback from the mathematics, research, and development communities.

For the most up to date version of the specifications, check the [Formal Models for Ledger Rules GitHub repository](https://github.com/input-output-hk/cardano-ledger-specs "Cardano Ledger Specs, github.com").

Artwork, 

[](https://creativecommons.org/licenses/by/4.0/)

![Creative Commons](img/2019-04-16-new-shelley-formal-specifications-complete.009.png)

[](http://www.beeple-crap.com)

Mike Beeple
