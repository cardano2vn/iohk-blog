# The Daedalus Mantis integration 1.0 is released
### **Highly secure wallet now available for Ethereum Classic**
![](img/2018-02-02-daedalus-mantis-integration-1-0-is-released.002.png) 2 February 2018![](img/2018-02-02-daedalus-mantis-integration-1-0-is-released.002.png)[ Jeremy Wood](/en/blog/authors/jeremy-wood/page-1/)![](img/2018-02-02-daedalus-mantis-integration-1-0-is-released.003.png) 2 mins read

![](img/2018-02-02-daedalus-mantis-integration-1-0-is-released.004.png)[ The Daedalus Mantis integration 1](https://ucarecdn.com/22405380-54da-4605-a392-f87944e6efb2/-/inline/yes/ "The Daedalus Mantis integration 1")

![Jeremy Wood](img/2018-02-02-daedalus-mantis-integration-1-0-is-released.005.png)[](/en/blog/authors/jeremy-wood/page-1/)
### [**Jeremy Wood**](/en/blog/authors/jeremy-wood/page-1/)
Founder

- ![](img/2018-02-02-daedalus-mantis-integration-1-0-is-released.006.png)[](tmp///www.youtube.com/watch?v=E2G9xLYpR1c "YouTube")
- ![](img/2018-02-02-daedalus-mantis-integration-1-0-is-released.007.png)[](tmp///jp.linkedin.com/in/jeremykwood "LinkedIn")
- ![](img/2018-02-02-daedalus-mantis-integration-1-0-is-released.008.png)[](tmp///twitter.com/iohk_jeremy "Twitter")

![The Daedalus Mantis integration 1.0 is released](img/2018-02-02-daedalus-mantis-integration-1-0-is-released.009.jpeg)

There has been a lot of change in the short time since Release Candidate 1 went out on December 22. Some of the team have swapped the short, dark days of winter for life in the Caribbean, as IOHK have sponsored an eight-week intense and high quality Haskell course in the University of the West Indies in Barbados. Meanwhile work *has* been getting done on the [Daedalus Mantis integration 1.0 release](https://www.banklesstimes.com/2018/02/01/iohks-secure-daedalus-wallet-now-supports-ethereum-classic/ "IOHK Secure Daedalus Wallet Now Supports Ethereum Classic, Bankless Times"). 

The [security audit report](https://twitter.com/veorq/status/956931637857660932 "Security audit report") came in and was digested and published, and a close eye was kept on the bug reporting in Github and the [Ethereum Classic forum](https://forum.ethereumclassic.org/ "Ethereum Classic Forum").

Happily there were very few reported problems. There is a known issue with installing the Daedalus Mantis integration over an existing Daedalus wallet install and this will be fixed in a future version. For now the workaround is to uninstall the Daedalus wallet before installing the Daedalus Mantis integration. Unfortunately it is not possible to install both simultaneously, support for multiple wallet types is something the Daedalus team are working feverishly on. 

The most visible impact of the security report was the dropping of support for the automatic download of the bootstrap database. This feature was based on MD5 checksum, which is more broken than we realized. 

It is still possible to download a bootstrap database and install it by hand to reduce the amount of time spent syncing the network and it is recommended. Although a small bug fix to the discovery process and some tuning have also reduced the sync wait time, so both are good options now.

And so we can finally after a huge effort from the team and without further ado announce the release of the [Daedalus Mantis Integration 1.0](https://github.com/input-output-hk/mantis/releases "Daedalus Mantis Integration 1.0")!

Planning for next release, 1.1, has already begun, focused on performance improvements and refactors and while we have no dates yet we expect it to be in the first half of this year.

Sincere thanks to those who supported the team, the project and Ethereum Classic over the past months, it is greatly appreciated.
## **Attachments**
![](img/2018-02-02-daedalus-mantis-integration-1-0-is-released.004.png)[ The Daedalus Mantis integration 1](https://ucarecdn.com/22405380-54da-4605-a392-f87944e6efb2/-/inline/yes/ "The Daedalus Mantis integration 1")
