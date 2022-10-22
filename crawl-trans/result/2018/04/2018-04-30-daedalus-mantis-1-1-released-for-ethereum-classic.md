# Daedalus Mantis 1.1 Released for Ethereum Classic
### **Software update delivers performance improvements**
![](img/2018-04-30-daedalus-mantis-1-1-released-for-ethereum-classic.002.png) 30 April 2018![](img/2018-04-30-daedalus-mantis-1-1-released-for-ethereum-classic.002.png)[ Jeremy Wood](/en/blog/authors/jeremy-wood/page-1/)![](img/2018-04-30-daedalus-mantis-1-1-released-for-ethereum-classic.003.png) 5 mins read

![Jeremy Wood](img/2018-04-30-daedalus-mantis-1-1-released-for-ethereum-classic.004.png)[](/en/blog/authors/jeremy-wood/page-1/)
### [**Jeremy Wood**](/en/blog/authors/jeremy-wood/page-1/)
Founder

- ![](img/2018-04-30-daedalus-mantis-1-1-released-for-ethereum-classic.005.png)[](tmp///www.youtube.com/watch?v=E2G9xLYpR1c "YouTube")
- ![](img/2018-04-30-daedalus-mantis-1-1-released-for-ethereum-classic.006.png)[](tmp///jp.linkedin.com/in/jeremykwood "LinkedIn")
- ![](img/2018-04-30-daedalus-mantis-1-1-released-for-ethereum-classic.007.png)[](tmp///twitter.com/iohk_jeremy "Twitter")

![Daedalus Mantis 1.1 Released for Ethereum Classic](img/2018-04-30-daedalus-mantis-1-1-released-for-ethereum-classic.008.jpeg)

It's the end of April and it already feels like a long time since February, when we announced version 1.0 of Mantis, our Ethereum Classic client built in Scala. After the success of [Mantis 1.0](/en/blog/mantis-ethereum-classic-beta-release/ "Mantis release") some of the Grothendieck team got temporarily drafted onto other projects. That, coupled with the two-month full-time Haskell training course some of the team were on earlier this year, meant that Team Grothendieck has been short-handed recently. In fact, internally this release is sometimes called "The Konrad Release" as it was developer [Konrad Staniec](/en/team/konrad-staniec/ "Konrad Staniec, IOHK") who kept the 1.1 candle burning and the performance pull requests (PRs) coming. 

For review of the PRs we did of course leverage the expertise of the whole team, and special mention to [Alan Verbner](/en/blog/iohk-spotlight-alan-verbner/ "IOHK Spotlight - Alan Verbner") and [Nico Taller](/en/team/nicolas-tallar/ "Nicolas Tallar, IOHK") for their efforts in review and testing of the performance improvements to the complex pruning functionality. 

While I'm listing contributors, many thanks to [Lukasz Gasior](/en/team/lukasz-gasior/ "Lukasz Gasior, IOHK") and [Radek Tkaczyk](/en/team/radek-tkaczyk/ "Radek Tkaczyk, IOHK") for taking time to review PRs early on and especially to Carlos Montero and Jeremy Townsend, two new IOHK developers who jumped head first into the Mantis code just as the test cycle was starting and were invaluable in reviewing PRs and testing the JSON RPC API. Also the testing team's Alan McNicholas for giving the release candidate a whirl and finding an installer bug! That's quite a lot of shoulders to the wheel. 

The objective of the 1.0 release was to create a working product, while the 1.1 release aimed to take the working code and find and remove the performance bottlenecks. The most painful bottleneck identified was in synchronizing the blockchain. This was complicated by the fact that tuning that performance depends on quite a few factors, the speed of the network, the type of hard disk on the machine and the number and type of peers at the time of synchronizing. 

For example on MacOs with an SSD and 8Gb of RAM Konrad was consistently getting about 17 hours for a full synchronization, whereas on an "small" EC2 instance this could take over a week! One of the reasons for this is AWS t2.small instances can be "limited" or "unlimited" referring to their CPU credits per hour. Once the limit of CPU credits has been reached, the synchronization slows down considerably. Our developer Jeremy Townsend wrote this up and it turns out this can be improved by using a "compute optimised" EC2 instance because the software now spends most of its time actually verifying blocks of transactions and those crypto functions are compute expensive!

Apart from performance, the "difficulty bomb" ECIP 1041 has been disabled â€“ just in time too as the block where this becomes important rolls around in early May. 

There have been no changes to the wallet interface in this release. A couple of fairly minor changes were considered but the Daedalus team is flat out and while they are on the teamâ€™s backlog list they did not rise sufficiently in priority for inclusion in this release. The only real implication of that in this release is how the block download progress is reported. It was quite confusing for users to see a 0.0% progress bar for such a long time. The reason is the synchronization for ETC is different to the synchronization for ADA, in that ETC implements 'fast sync' and ADA does not. 

Fast sync downloads the state trie and the blocks in the blockchain. Ada has no fast sync and downloads only the blocks. In 1.0 the state trie was downloaded *before* the blockchain and when the state trie was fully downloaded the blocks began to download. The progress bar is only aware of the blocks and so continued to show "0.0%" while the state trie was being downloaded. In 1.1 the situation is better but not perfect. In 1.1, as a result of performance testing and improvements the block downloading begins straight away and the state trie downloads towards the end of the synchronization. The user will see the progress bar update as expected, however towards the end of the synchronization the progress will appear to stall. This happens while the state trie downloads. While this is not perfect and needs to be fixed, on the plus side the whole process is faster and so the frustration should be less. Thank you in advance for your patience with this.

![Ethereum Classic Roadmap](img/2018-04-30-daedalus-mantis-1-1-released-for-ethereum-classic.009.png)

The next release will be Mantis 2.0, currently slated for the end of the year, around Q4. This will be a significant release with significant new functionality. The Project Manager for this release, Ravi Patel, and a full-strength team will be introducing this functionality as it is prioritized.

On a general note, I feel the progress in ETC is picking up pace. Observing the external ETC community it seems there has been a lot of good organisational work done and dedicated people involved. I'm more optimistic than ever about the future!
