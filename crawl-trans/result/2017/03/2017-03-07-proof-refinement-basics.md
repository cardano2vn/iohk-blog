# Proof refinement basics
![](img/2017-03-07-proof-refinement-basics.002.png) 7 March 2017![](img/2017-03-07-proof-refinement-basics.002.png)[ Rebecca Valentine](/en/blog/authors/rebecca-valentine/page-1/)![](img/2017-03-07-proof-refinement-basics.003.png) 19 mins read

![](img/2017-03-07-proof-refinement-basics.004.png)[ Proof Refinement Basics - Input Output](https://ucarecdn.com/acd33d70-27c0-4e24-b150-0be8c5721402/-/inline/yes/ "Proof Refinement Basics - Input Output")

![Rebecca Valentine](img/2017-03-07-proof-refinement-basics.005.png)[](/en/blog/authors/rebecca-valentine/page-1/)
### [**Rebecca Valentine**](/en/blog/authors/rebecca-valentine/page-1/)
Cardano SL Developer Team

Plutus Manager

- ![](img/2017-03-07-proof-refinement-basics.006.png)[](https://github.com/psygnisfive "GitHub")

![Proof refinement basics](img/2017-03-07-proof-refinement-basics.007.jpeg)

In this blog post, I'm going to discuss the overall structure of a proof refinement system. Such systems can be used for implementing automatic theorem provers, proof assistants, and type checkers for programming languages. The proof refinement literature is either old or hard to understand, so this post, and subsequent ones on the same topic, will present it in a more casual and current way. Work on proof refinement as a methodology for building type checkers and interactive proof systems has a long history, going back to LCF, HOL, Nuprl, and Coq. These techniques never really penetrated into the mainstream of programming language implementation, but perhaps this may change.

The GitHub repo for this project can be found [here](https://github.com/psygnisfive/proof-refinement-basics).
## **Prologue**
As part of my work for IOHK, I've been designing and implementing a programming language called Plutus, which we use as the scripting language for our blockchains. Because IOHK cares deeply about the correctness of its systems, Plutus needs to be held to a very high standard, and needs to enable easy reasoning about its behavior. For that reason, I chose to make Plutus a pure, functional language with a static type system. Importantly, the language has a formal type theoretic specification.

To implement the type checker for the language, I used a fairly standard technique. However, recently I built a new framework for implementing programming languages which, while different from the usual way, has a more direct connection to the formal specification. This greater similarity makes it easier to check that the implementation is correct.

The framework also makes a number of bugs easier to eliminate. One class of bugs that arose a number of times in the first implementation was that of metavariables and unification. Because the language supports a certain about of unification-driven type inference, it's necessary to propagate updates to the information state of the type checking algorithm, so that everything is maximally informative and the algorithm can run correctly. Propagating this information by hand is error prone, and the new framework makes it possible to do it once and for all, in a bug-free way.

The framework additionally makes some features easier to program. For example, good error reporting is extremely important. But good error messages need to have certain information about where the error occurs. Not just where in the source code, but where in the logical structure of the program. All sorts of important information about the nature of the error, and the possible solutions, depend on that. The framework I developed also makes this incredibly easy to implement, so much so that it's build right into the system, and any language implemented using it can take advantage of it.
### **Proofs and Proof Systems**
In the context of modern proof theory and type theory, a proof can be seen as a tree structure with labeled nodes and the class of proof trees which are valid is defined by a set of rules that specify how a node in a tree may relate to its child nodes. The labels, in the context of proofs, are usually hypothetical judgments, and the rules are inference rules, but you can also use the same conceptual framework for many other things.

An example of a rule is for any choice of A and B, if you can show that A is true and that B is true, then it's permissible to conclude Aâˆ§B is true. This is usually written with the notation

![Maths](img/2017-03-07-proof-refinement-basics.008.png)

This rule explains one way that it's ok to have a node labeled 

Aâˆ§B is true
