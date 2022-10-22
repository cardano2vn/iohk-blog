# Backwards-incompatible changes in Cardano 1.4 Wallet API
### **Matthias Benkort and Jacob Mitchell cover what's new**
![](img/2018-12-18-backwards-incompatible-changes-in-cardano-1-4-wallet-api.002.png) 18 December 2018![](img/2018-12-18-backwards-incompatible-changes-in-cardano-1-4-wallet-api.002.png)[ Matthias Benkort](/en/blog/authors/matthias-benkort/page-1/)![](img/2018-12-18-backwards-incompatible-changes-in-cardano-1-4-wallet-api.003.png) 4 mins read

![](img/2018-12-18-backwards-incompatible-changes-in-cardano-1-4-wallet-api.004.png)[ Simplicity and Michelson - Input Output](https://ucarecdn.com/cb0054f1-4e81-4617-82c2-6a6a363270c7/-/inline/yes/ "Simplicity and Michelson - Input Output")

![Matthias Benkort](img/2018-12-18-backwards-incompatible-changes-in-cardano-1-4-wallet-api.005.png)[](/en/blog/authors/matthias-benkort/page-1/)
### [**Matthias Benkort**](/en/blog/authors/matthias-benkort/page-1/)
Software Engineering Lead

Engineering

- ![](img/2018-12-18-backwards-incompatible-changes-in-cardano-1-4-wallet-api.006.png)[](https://www.linkedin.com/in/matthias-benkort-47186a57/ "LinkedIn")
- ![](img/2018-12-18-backwards-incompatible-changes-in-cardano-1-4-wallet-api.007.png)[](https://twitter.com/MBenkort "Twitter")
- ![](img/2018-12-18-backwards-incompatible-changes-in-cardano-1-4-wallet-api.008.png)[](https://github.com/KtorZ "GitHub")

![Backwards-incompatible changes in Cardano 1.4 Wallet API](img/2018-12-18-backwards-incompatible-changes-in-cardano-1-4-wallet-api.009.jpeg)

In this blog, [wallet API lead Matthias Benkort](/en/team/matthias-benkort "Matthias Benkort's profile") explains backwards-incompatible Cardano wallet API changes that are coming in Cardano 1.4, and [devOps lead Jacob Mitchell](/en/team/jacob-mitchell/ "Jacob Mitchell's profile") shows how to build a Cardano client with both the old V0 wallet API and the new V1 wallet API, instead of the default option providing only the new API. This blog post is mainly intended for current users of the Cardano wallet API; in particular, those who have already integrated with the beta release of the V1 API prior to Cardano 1.4.

The Cardano wallet API has its own versioning. As of Cardano 1.4 the previous V0 wallet API will become obsolete. All V0 API REST endpoints have been ported to [V1 API](https://cardanodocs.com/technical/wallet/api/v1/), and the wallet rewrite gave the wallet team an opportunity to correct and improve the Cardano wallet semantics. As a result, there have been four breaking changes as described below. The V1 wallet API will become the default wallet API in Cardano 1.4.

1. The diagnostic structure of the **NotEnoughMoney** error has been changed to accommodate more cases.
1. The diagnostic structure of the **WalletAlreadyExists** error has been modified to provide the extra field **walletId** for the ID of the pre-existing wallet.
1. The behavior of **/api/v1/addresses/{address}** has been adjusted to more accurately reflect the semantics of ownership regarding addresses. The previous version of this endpoint failed with an HTTP error when the given address was unknown to the wallet. This was misleading, since an address that is unknown to the wallet could still belong to it. To reflect this, the V1 endpoint no longer fails, and instead when an address is not recognised it returns a new field **isOurs**, which indicates either that the address is ours, or that it is not recognised.
1. A DELETE request to **/api/v1/wallets/{wallet}** now correctly fails with a 404 HTTP response code if the wallet doesn't exist. Previously, it incorrectly responded with 204.

Regardless of whether the old or new data layer runs, the V1 API will have the changes described above. The first two changes are mostly intended so that developers can understand what's going on. If exchanges or other parties were using it to build a specific error message for their API or front end, then it may break.

The third change is more subtle and is actually a bug fix. The old behavior of the GET address endpoint was sending wrong information to nodes, so we have fixed it to improve its accuracy. In doing so, we had to introduce a new **isOurs** field and review what HTTP statuses were being sent - should exchanges have been relying on this for any business logic, they will need to update it.

The default installation of Cardano 1.4 will come with the V1 wallet API only. 

Generally, exchanges and other integrators use stable releases to build a Cardano client using a shell script that launches a Cardano wallet against mainnet:

**nix-build -A connectScripts.mainnet.wallet**

In this case there is no roll back - Cardano wallet is upgraded to V1.

In order to have both V0 and V1 functionality developers should use **useLegacyDataLayer** in the **custom-wallet-config.nix** file as described in our [documentation for exchanges](https://github.com/input-output-hk/cardano-sl/blob/master/docs/exchange-onboarding.md#generate-custom-configuration). **Caution!** In this mode, despite making V1 endpoints available, the API won't utilize the newly developed data layer. As a consequence, developers may experience limitations known of the legacy data layer. This mode is therefore deprecated and we strongly recommend users to run nodes without it.

We have described backwards-incompatible changes coming with the wallet API in Cardano 1.4. Should anyone have trouble upgrading to 1.4, seek help through either an already established communication channel, or our [support portal](https://iohk.zendesk.com).

Artwork, 

[](https://creativecommons.org/licenses/by/4.0/ "Creative Commons")

![Creative Commons](img/2018-12-18-backwards-incompatible-changes-in-cardano-1-4-wallet-api.010.png)

[](http://www.beeple-crap.com)

Mike Beeple
## **Attachments**
![](img/2018-12-18-backwards-incompatible-changes-in-cardano-1-4-wallet-api.004.png)[ Simplicity and Michelson - Input Output](https://ucarecdn.com/cb0054f1-4e81-4617-82c2-6a6a363270c7/-/inline/yes/ "Simplicity and Michelson - Input Output")
