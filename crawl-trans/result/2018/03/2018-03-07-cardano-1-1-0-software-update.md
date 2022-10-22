# Cardano 1.1.0 software update
### **A major package of improvements and fixes is ready for users**
![](img/2018-03-07-cardano-1-1-0-software-update.002.png) 7 March 2018![](img/2018-03-07-cardano-1-1-0-software-update.002.png)[ Duncan Coutts](/en/blog/authors/duncan-coutts/page-1/)![](img/2018-03-07-cardano-1-1-0-software-update.003.png) 4 mins read

![](img/2018-03-07-cardano-1-1-0-software-update.004.png)[ Cardano 1](https://ucarecdn.com/81358a2c-cff8-449d-b2ad-2c4bb3ef2a1c/-/inline/yes/ "Cardano 1")

![Duncan Coutts](img/2018-03-07-cardano-1-1-0-software-update.005.png)[](/en/blog/authors/duncan-coutts/page-1/)
### [**Duncan Coutts**](/en/blog/authors/duncan-coutts/page-1/)
Technical Architect

Well-Typed

- ![](img/2018-03-07-cardano-1-1-0-software-update.006.png)[](mailto:duncan.coutts@iohk.io "Email")
- ![](img/2018-03-07-cardano-1-1-0-software-update.007.png)[](https://www.youtube.com/watch?v=TZGVgNsJSnA "YouTube")
- ![](img/2018-03-07-cardano-1-1-0-software-update.008.png)[](http://www.linkedin.com/in/duncancoutts "LinkedIn")
- ![](img/2018-03-07-cardano-1-1-0-software-update.009.png)[](https://github.com/dcoutts "GitHub")

![Cardano 1.1.0 software update](img/2018-03-07-cardano-1-1-0-software-update.010.jpeg)

The software update today is the first major release for Cardano since the mainnet was launched at the end of September and it consists of a great deal of work from the development team. The release contains a few new features that are aimed at improving the user experience. And it also contains a set of important fixes for many of the bugs that were identified since the last release, Cardano SL 1.0.3. Here is [Charles Hoskinson, CEO of IOHK](https://www.pscp.tv/w/1dRJZeyZOagGB "Update on the Update from IOHK_Charles, pscp.tv"), with a video update about this release, and below we outline the most significant changes delivered. Users will notice the changes take effect tomorrow.

The team has been working hard to address the issues some users have experienced with Daedalus and this update contains fixes for some of the problems.

With this release, Daedalus will detect when the time on a user's machine is out of sync with the global time and will display an error message asking the user to fix the issue. Before this feature was added when there was a time difference of 20 seconds or more, the Cardano node was unable to connect to the network and validate the blockchain, and Daedalus would be held on the loading screen with the "Connecting to network" message. This feature will eliminate the problem of users being held on the loading screen because of the time difference issue.

Several other instances of the user being stuck on the "Connecting to network" screen were fixed. Many issues that can lead to this have been partially or completely fixed. Problem areas include node shutdown, networking and block retrieval mechanisms.

A new "Support request" feature enables users to report a problem directly from Daedalus. This will automatically include log files along with the problem report. By always including log files, this feature will help the development team to investigate and solve the problems that users are experiencing. This feature is accessible from the main user interface and from the loading screen when there is a delay while connecting to the network or when blockchain syncing stops.

Blockchain retrieval performance and reliability has been gradually improved, in particular bugs have been fixed that caused significant slowdown in syncing to the network after reaching 99.9%, and caused occasional network disconnections. Handling of whether Daedalus is connected or disconnected is improved, and a lost internet connection is now detected and brings the user to the loading screen to indicate that wallet is not currently operational.

In addition to individual fixes, importantly, this major release is the first time-based release containing significant new code, and represents an improvement in our development process. All previous releases of Cardano were scope-based, i.e. the goal was to deliver a particular scope and often the release was repeatedly postponed because of inaccurate estimations on having the scope ready for release.

There is much debate among software developers on which release process is preferable. As was outlined in our [previous blog post](/en/blog/what-is-our-release-strategy-for-cardano/ "Cardano release strategy"), the Cardano team has chosen time-based releases. We had a significant backlog of work to resolve to be able to release our development branch to the mainnet â€“ a substantial amount of testing had to be performed because of large amount of new code. But with the release of 1.1.0, we have made a major step forward.

There will be two more time-based releases in the next couple of months containing more improvements, fixes and new features for Cardano. New features for the Shelley phase of development will begin to be released in Q2 and continue through Q3. For more information see the [Cardano Roadmap](https://cardanoroadmap.com "Cardano roadmap").

Artwork, [](https://creativecommons.org/licenses/by/4.0/ "Creative Commons")

![Creative Commons](img/2018-03-07-cardano-1-1-0-software-update.011.png)[](https://creativecommons.org/licenses/by/4.0/ "Creative Commons")[](http://www.beeple-crap.com)

[Mike Beeple](http://www.beeple-crap.com)
## **Attachments**
![](img/2018-03-07-cardano-1-1-0-software-update.004.png)[ Cardano 1](https://ucarecdn.com/81358a2c-cff8-449d-b2ad-2c4bb3ef2a1c/-/inline/yes/ "Cardano 1")
