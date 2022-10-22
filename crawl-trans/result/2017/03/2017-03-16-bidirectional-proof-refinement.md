# Bidirectional proof refinement
![](img/2017-03-16-bidirectional-proof-refinement.002.png) 16 March 2017![](img/2017-03-16-bidirectional-proof-refinement.002.png)[ Rebecca Valentine](/en/blog/authors/rebecca-valentine/page-1/)![](img/2017-03-16-bidirectional-proof-refinement.003.png) 18 mins read

![](img/2017-03-16-bidirectional-proof-refinement.004.png)[ Bidirectional proof refinement - Input Output](https://ucarecdn.com/9c520277-15b2-4ef1-81c7-8b671e87219e/-/inline/yes/ "Bidirectional proof refinement - Input Output")

![Rebecca Valentine](img/2017-03-16-bidirectional-proof-refinement.005.png)[](/en/blog/authors/rebecca-valentine/page-1/)
### [**Rebecca Valentine**](/en/blog/authors/rebecca-valentine/page-1/)
Cardano SL Developer Team

Plutus Manager

- ![](img/2017-03-16-bidirectional-proof-refinement.006.png)[](https://github.com/psygnisfive "GitHub")

In [my last blog post](/en/blog/proof-refinement-basics/ "Proof refinement basics, IOHK blog"), we looked at the very basics of proof refinement systems. I noted at the end that there was a big drawback of the systems as shown, namely that information flows only in one direction: from the root of a proof tree to the leaves. In this post, we'll see how to get information to flow in the opposite direction as well. The code for this blog post can be found on GitHub [here](https://github.com/psygnisfive/bidirectional-proof-refinement "GitHub; Psygnisfive, Bidirectional proof refinement").
### **Addition Again**
The addition judgment Plus which we defined last time was a three-argument judgment. The judgment Plus L M N was a claim that N is the sum of L and M. But we might want to instead think about specifying only some of the arguments to this judgment. In a language like Prolog, this is implemented by the use of metavariables which get valued in the course of computation. In the proof refinement setting, however, we take a different approach. Instead, we make use of a notion called bidirectionality, where we specify that a judgment's arguments can come in two modes: input and output. This is somewhat related to viewing thing from a functional perspective, but in a more non-deterministic or relational fashion.

Let's start by deciding that the mode of the first two arguments to Plus is that of input, and the third is output. This way we'll think about actually computing the sum of two numbers. Instead of three Nat inputs, we'll instead use only two. We'll use a judgment name that reflects which two:

-- Haskell

data Judgment = Plus12 Nat Nat

`  `deriving (Show)

// JavaScript

function Plus12(x,y) {

`    `return { tag: "Plus12", args: [x,y] };

}

The behavior of the decomposer for Plus12 will have to be slightly different now, though, because there are only two arguments. But additionally, we want to not only expand a goal into subgoals, but also somehow synthesize a result from the results of the subgoals. So where before we had only to map from a goal to some new goals, now we must also provide something that maps from some subresults to a result.

Rather than giving two separate functions, we'll give a single function that returns both the new subgoals, and the function that composes a value from the values synthesized for those subgoals.

-- Haskell

decomposePlus12 :: Nat -> Nat -> Maybe ([Judgment], [Nat] -> Nat)

decomposePlus12 Zero y = Just ([], \zs -> y)

decomposePlus12 (Suc x) y = Just ([Plus12 x y], \[z] -> Suc z)

decompose :: Judgment -> Maybe ([Judgment], [Nat] -> Nat)

decompose (Plus12 x y) = decomposePlus12 x y

// JavaScript

function decomposePlus12(x,y) {

`    `if (x.tag === "Zero") {

`        `return Just([[], zs => y]);

`    `} else if (x.tag === "Suc") {

`        `return Just([[Plus12(x.arg,y)], zs => Suc(zs[0])]);

`    `}

}

function decompose(j) {

`    `if (j.tag === "Plus12") {

`        `return decomposePlus12(j.args[0], j.args[1]);

`    `}

}

The decompose function is somewhat redundant in this example, but the shape of the problem is preserved by having this redundancy. The same is true of the Maybe in the types. We can always decompose now, so the Nothing option is never used, but I'm keeping it here to maintain parallelism with the general framework.

Building a proof tree in this setting proceeds very similarly to how it did before, except now we need to make use of the synthesis functions in parallel with building a proof tree:

-- Haskell

findProof :: Judgment -> Maybe (ProofTree, Nat)

findProof j =

`  `case decompose j of

`    `Nothing -> Nothing

`    `Just (js, f) -> case sequence (map findProof js) of

`      `Nothing -> Nothing

`      `Just tns -> let (ts, ns) = unzip tns

`                  `in Just (ProofTree j ts, f ns)

// JavaScript

function unzip(xys) {

`    `var xs = [];

`    `var ys = [];

`    `for (var i = 0; i < xys.length; i++) {

`        `xs.push(xys[i][0]);

`        `ys.push(xys[i][1]);

`    `}

`    `return [xs,ys]

}

function findProof(j) {

`    `var mjs = decompose(j);

`    `if (mjs.tag === "Nothing") {

`        `return Nothing;

`    `} else if (mjs.tag === "Just") {

`        `var js = mjs.arg[0]

`        `var f = mjs.arg[1]

`        `var mtns = sequence(js.map(j => findProof(j)));

`        `if (mtns.tag === "Nothing") {

`            `return Nothing;

`        `} else if (mtns.tag === "Just") {

`            `var tsns = unzip(mtns.arg);

`            `return Just([ProofTree(j, tsns[0]), f(tsns[1])]);

`        `}

`    `}

}

Now when we run this on some inputs, we get back not only a proof tree, but also the resulting value, which is the Nat that would have been the third argument of Plus in the previous version of the system.

Let's now add another judgment, Plus13, which will synthesize the second argument of the original Plus judgment from the other two. Therefore, the judgment Plus13 L N means L subtracted from N. We'll add this judgment to the existing Judgment declarations.

-- Haskell

data Judgment = Plus12 Nat Nat | Plus13 Nat Nat

`  `deriving (Show)

// JavaScript

function Plus13(x,z) {

`    `return { tag: "Plus13", args: [x,z] };

}

We can now define a decomposition function for this judgment. Notice that this one is partial, in that, for some inputs, there's no decomposition because the first argument is larger than the second. We'll also extend the decompose function appropriately.

-- Haskell

decomposePlus13 :: Nat -> Nat -> Maybe ([Judgment], [Nat] -> Nat)

decomposePlus13 Zero z = Just ([], \xs -> z)

decomposePlus13 (Suc x) (Suc z) = Just ([Plus13 x z], \[x] -> x)

decomposePlus13 \_ \_ = Nothing

decompose :: Judgment -> Maybe ([Judgment], [Nat] -> Nat)

decompose (Plus12 x y) = decomposePlus12 x y

decompose (Plus13 x z) = decomposePlus13 x z

// JavaScript

function decomposePlus13(x,z) {

`    `if (x.tag === "Zero") {

`        `return Just([[], xs => z]);

`    `} else if (x.tag === "Suc" && z.tag === "Suc") {

`        `return Just([[Plus13(x.arg, z.arg)], xs => xs[0]]);

`    `} else {

`        `return Nothing;

`    `}

}

function decompose(j) {

`    `if (j.tag === "Plus12") {

`        `return decomposePlus12(j.args[0], j.args[1]);

`    `} else if (j.tag === "Plus13") {

`        `return decomposePlus13(j.args[0], j.args[1]);

`    `}

}

If we now try to find a proof for Plus13 (Suc Zero) (Suc (Suc (Suc Zero))), we get back Suc (Suc Zero), as expected, because 1 subtracted from 3 is 2. Similarly, if we try to find a proof for Plus13 (Suc (Suc Zero)) (Suc Zero), we find that we get no proof, because we can't subtract a number from something smaller than it.
### **Type Checking Again**
We'll aim to do the same thing with the type checker as we did with addition. We'll split the HasType judgment into two judgments, Check and Synth. The Check judgment will be used precisely in those cases where a type must be provided for the proof to go through, while the Synth judgment will be used for cases where the structure of the program is enough to tell us its type.

-- Haskell

data Judgment = Check [(String,Type)] Program Type

`              `| Synth [(String,Type)] Program

`  `deriving (Show)

// JavaScript

function Check(g,m,a) {

`    `return { tag: "Check", args: [g,m,a] };

}

function Synth(g,m) {

`    `return { tag: "Synth", args: [g,m] };

}

Additionally, because of these changes in information flow, we'll remove some type annotations from the various program forms, and instead introduce a general type annotation form that will be used to shift between judgments explicitly.

-- Haskell

data Program = Var String | Ann Program Type

`             `| Pair Program Program | Fst Program | Snd Program

`             `| Lam String Program | App Program Program

`  `deriving (Show)

// JavaScript

function Var(x) {

`    `return { tag: "Var", arg: x };

}

function Ann(m,a) {

`    `return { tag: "Ann", args: [m,a] };

}

function Pair(m,n) {

`    `return { tag: "Pair", args: [m,n] };

}

function Fst(m) {

`    `return { tag: "Fst", arg: m };

}

function Snd(m) {

`    `return { tag: "Snd", arg: m };

}

function Lam(x,m) {

`    `return { tag: "Lam", args: [x,m] };

}

function App(m,n) {

`    `return { tag: "App", args: [m,n] };

}

The last change that we'll make will be to change the notion of synthesis a little bit from what we had before. In the addition section, we said merely that we needed a function that synthesized a new value from some subvalues. More generally, though, we need that process to be able to fail, because we wish to place constraints on the synthesized values. To capture this, we'll wrap the return type in Maybe.

-- Haskell

decomposeCheck

`  `:: [(String,Type)]

`  `-> Program

`  `-> Type

`  `-> Maybe ([Judgment], [Type] -> Maybe Type)

decomposeCheck g (Pair m n) (Prod a b) =

`  `Just ([Check g m a, Check g n b], \as -> Just undefined)

decomposeCheck g (Lam x m) (Arr a b) =

`  `Just ([Check ((x,a):g) m b], \as -> Just undefined)

decomposeCheck g m a =

`  `Just ( [Synth g m]

`       `, \[a2] -> if a == a2 then Just undefined else Nothing

**This document was truncated here because it was created in the Evaluation Mode.**
