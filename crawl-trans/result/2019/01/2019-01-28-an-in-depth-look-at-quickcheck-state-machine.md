# An in-depth look at quickcheck-state-machine
![](img/2019-01-28-an-in-depth-look-at-quickcheck-state-machine.002.png) 28 January 2019![](img/2019-01-28-an-in-depth-look-at-quickcheck-state-machine.002.png)[ Edsko de Vries](/en/blog/authors/edsko-de-vries/page-1/)![](img/2019-01-28-an-in-depth-look-at-quickcheck-state-machine.003.png) 46 mins read

![Edsko de Vries](img/2019-01-28-an-in-depth-look-at-quickcheck-state-machine.004.png)[](/en/blog/authors/edsko-de-vries/page-1/)
### [**Edsko de Vries**](/en/blog/authors/edsko-de-vries/page-1/)
Software Engineer

Well-Typed

- ![](img/2019-01-28-an-in-depth-look-at-quickcheck-state-machine.005.png)[](http://www.linkedin.com/in/edsko-de-vries-04126b31 "LinkedIn")
- ![](img/2019-01-28-an-in-depth-look-at-quickcheck-state-machine.006.png)[](https://twitter.com/EdskoDeVries "Twitter")
- ![](img/2019-01-28-an-in-depth-look-at-quickcheck-state-machine.007.png)[](https://github.com/edsko "GitHub")

![An in-depth look at quickcheck-state-machine](img/2019-01-28-an-in-depth-look-at-quickcheck-state-machine.008.jpeg)

*Please note: this post originally appeared on the [Well-Typed blog](http://www.well-typed.com/blog/2019/01/qsm-in-depth/ "An in-depth look at quickcheck-state-machine, well-typed.com").* Stateful APIs are everywhere: file systems, databases, widget libraries, the list goes on. Automated testing of such APIs requires generating sequences of API calls, and when we find a failing test, ideally *shrinking* such a sequence to a minimal test case. Neither the generation nor the shrinking of such sequences is trivial. After all, it is the very nature of stateful systems that later calls may depend on earlier calls: we can only add rows to a database table after we create it, we can only write to a file after we open it, etc. Such dependencies need to be tracked carefully. Moreover, in order to verify the responses we get back from the system, the test needs to maintain some kind of internal representation of what it thinks the internal state of the system is: when we read from a file, we need to know what was in the file in order to be able to verify if the response was correct or not.

In this blog post we will take an in-depth look at [quickcheck-state-machine](http://hackage.haskell.org/package/quickcheck-state-machine "quickcheck-state-machine, hackage.haskell.org"), a library for testing stateful code. Our running example will be the development of a simple mock file system that should behave identically to a real file system. Although simple, the example will be large enough to give us an opportunity to discuss how we can verify that our generator is producing all test cases we need, and how we can inspect whether the shrinker is doing a good job; in both cases, test case labelling will turn out to be essential. Throughout we will also discuss design patterns for quickcheck-state-machine tests which improve separation of concerns and reduce duplication. It should probably be pointed out that this is an opinionated piece: there are other ways to set things up than we present here.

We will not show the full development in this blog post, and instead focus on explaining the underlying concepts. If you want to follow along, the code is [available for download](https://github.com/well-typed/qsm-in-depth "qsm-in-depth, github.com"). We will assume [version 0.6 of quickcheck-state-machine](http://hackage.haskell.org/package/quickcheck-state-machine-0.6.0 "0.6 quickcheck-state-machine, hackage.haskell.org"), which was recently released. If you are using an older version, it is recommended to upgrade, since the newer version includes some important bug fixes, especially in the shrinker.
## **Introducing the running example**
Our running example will be the development of a simple mock file system; the intention is that its behaviour is identical to the real file system, within the confines of what it needs to support. We will represent the state of the file system as

data Mock = M {

`    `dirs  :: Set Dir

`  `, files :: Map File String

`  `, open  :: Map MHandle File

`  `, next  :: MHandle

`  `}

type MHandle = Int

emptyMock :: Mock

emptyMock = M (Set.singleton (Dir [])) Map.empty Map.empty 0

We record which directories (folders) exist, the contents of all files on the system, the currently open handles (where mock handles are just integers), and the next available mock handle. To avoid confusion between files and directories we do not use FilePath but instead use

data Dir  = Dir [String]

data File = File {dir :: Dir, name :: String}

As one example, here is the mock equivalent of readFile:

type MockOp a = Mock -> (Either Err a, Mock)

mRead :: File -> MockOp String

mRead f m@(M \_ fs hs \_)

`  `| alreadyOpen               = (Left Busy         , m)

`  `| Just s <- Map.lookup f fs = (Right s           , m)

`  `| otherwise                 = (Left DoesNotExist , m)

`  `where

`    `alreadyOpen = f `List.elem` Map.elems hs

We first check if there is an open handle to the file; if so, we disallow reading this file (â€œresource busyâ€); if the file exists, we return its content; otherwise we report a â€œdoes not existâ€ error. The implementation of the other mock functions is similar; the full API is

mMkDir :: Dir               -> MockOp ()

mOpen  :: File              -> MockOp MHandle

mWrite :: MHandle -> String -> MockOp ()

mClose :: MHandle           -> MockOp ()

mRead  :: File              -> MockOp String

Finally, we should briefly talk about errors; the errors that the mock file system can report are given by

data Err = AlreadyExists | DoesNotExist | HandleClosed | Busy

and they capture a subset of the IO exceptions

[](#1)

1

fromIOError :: IOError -> Maybe Err

fromIOError e =

`    `case ioeGetErrorType e of

`      `GHC.AlreadyExists    -> Just AlreadyExists

`      `GHC.NoSuchThing      -> Just DoesNotExist

`      `GHC.ResourceBusy     -> Just Busy

`      `GHC.IllegalOperation -> Just HandleClosed

`      `\_otherwise           -> Nothing
## **Testing**
Typically we are developing some stateful code, and then write a pure (mock) implementation of the same thing to test it, making sure that the stateful implementation and the simpler pure model compute the same things. Here we are doing the opposite: we are adjusting the model (the mock file system) to match what the real file system does. Either way, the process is the same: we write tests, execute them both in the real thing and in the model, and compare results.

If we were writing unit tests, we might write tests such as

- Write to two different files
- Write to a file and then read it
- etc.

However, as John Hughes of QuviQ â€“ and one of the original authors of QuickCheck â€“ [likes to point out](http://www.quviq.com/more-thorough-testing/ "quviq.com"), as systems grow, it becomes impossible to write unit tests that test the interaction between all the features of the system. So, *donâ€™t write unit tests*. Instead, *generate* tests, and verify *properties*.

To generate tests for our mock file system, we have to generate sequences of calls into the API; *â€œopen this file, open that file, write to the first file we opened, â€¦â€*. We then execute this sequence both against the mock file system and against the real thing, and compare results. If something goes wrong, we end up with a test case that we can inspect. Ideally, we should then try to reduce this test to try and construct a *minimal* test case that illustrates the bug. We have to be careful when shrinking: for example, when we remove a call to open from a test case, then any subsequent writes that used that file handle must also be removed. A library such as quickcheck-state-machine can be used both to help with generating such sequences and, importantly, with shrinking them.
## **Reifying the API**
It is important that we generate the test *before* executing it. In other words, the test generation should not depend on any values that we only get when we run the test. Such a dependency makes it impossible to re-run the same test multiple times (no reproducible test cases) or shrink tests to obtain minimal examples. In order to do this, we need to *reify* the API: we need to define a data type whose constructors correspond to the API calls:

data Cmd h =

`    `MkDir Dir

`  `| Open File

`  `| Write h String

`  `| Close h

`  `| Read File

Cmd is polymorphic in the type of handles h; this is important, because we should be able to execute commands both against the mock file system and against the real file system:

runMock ::       Cmd MHandle -> Mock -> (.. Mock)

runIO   :: .. -> Cmd IO.Handle -> IO ..

What should the return type of these functions be? After all, different functions return different things: Open returns a new handle, Read returns a string, the other functions return unit. To solve this problem we will simply introduce a union type

[](#2)

2

for successful responses

data Success h = Unit () | Handle h | String String

A response is then either a succesful response or an error:

newtype Resp h = Resp (Either Err (Success h))

It is now easy to implement runMock: we just map all the constructors in Cmd to the corresponding API calls, and wrap the result in the appropriate constructor of Success:

runMock :: Cmd MHandle -> Mock -> (Resp MHandle, Mock)

runMock (MkDir d)   = first (Resp . fmap Unit)   . mMkDir d

runMock (Open  f)   = first (Resp . fmap Handle) . mOpen  f

runMock (Write h s) = first (Resp . fmap Unit)   . mWrite h s

runMock (Close h)   = first (Resp . fmap Unit)   . mClose h

runMock (Read  f)   = first (Resp . fmap String) . mRead  f

where first :: (a -> b) -> (a, x) -> (b, x) comes from Data.Bifunctor.

We can write a similar interpreter for IO; it will take a FilePath as an additional argument that it will use as a prefix for all paths; we will use this to run the IO test in some temporary directory.

runIO :: FilePath -> Cmd IO.Handle -> IO (Resp IO.Handle)
## **References**
Our interpreter for IO takes real IO handles as argument; but will not have any real handles until we actually run the test. We need a way to generate commands that run in IO but donâ€™t use real handles (yet). Here is where we see the first bit of infrastructure provided by quickcheck-state-machine, *references*:

data Reference a r = Reference (r a)

where we will instantiate that r parameter to either Symbolic or Concrete:

[](#3)

3

data Symbolic a = Symbolic Var

data Concrete a = Concrete a

In other words, a Reference a Concrete is really just a wrapper around an a; indeed, quickcheck-state-machine provides

reference :: a -> Reference a Concrete

concrete  :: Reference a Concrete -> a

However, a Reference a Symbolic is a *variable*:

newtype Var = Var Int

An example of a program using symbolic references is

openThenWrite :: [Cmd (Reference IO.Handle Symbolic)]

openThenWrite = [

`      `Open (File (Dir []) "a")

`    `, Open (File (Dir []) "b")

`    `, Write (Reference (Symbolic (Var 0))) "Hi"

`    `]

This program corresponds precisely to our example from earlier: â€œopen this file, open that file, then write to the first file we openedâ€. Commands can return as many symbolic references in their result values as they want

[](#4)

4

; in our simple example, only Open creates a new reference, and so Var 0 returns to the handle returned by the first call to Open.

When we *execute* the test, those variables will be instantiated to their real values, turning symbolic references into concrete references. We will of course not write programs with symbolic references in them by hand; as we will see later, quickcheck-state-machine provides infrastructure for doing so.

Since we will frequently need to instantiate Cmd and Resp with references to handles, we will introduce some special syntax for this:

newtype At f r = At (f (Reference IO.Handle r))

type    f :@ r = At f r

For example, here is a wrapper around runIO that we will need that executes a command with concrete references:

semantics :: FilePath -> Cmd :@ Concrete -> IO (Resp :@ Concrete)

semantics root (At c) = (At . fmap reference) <$>

`                          `runIO root (concrete <$> c)

This is really just a call to runIO, with some type wrapping and unwrapping.
## **Relating the two implementations**
When we run our tests, we will execute the same set of commands against the mock implementation and in real IO, and compare the responses we get after each command. In order to compare, say, a command â€œwrite to this MHandleâ€ against the mock file system to a command â€œwrite to this IOHandleâ€ in IO, we need to know the relation between the mock handles and the IO handles. As it turns out, the most convenient way to store this mapping is as a mapping from *references* to the IO handles (either concrete or symbolic) to the corresponding mock handles.

type HandleRefs r = [(Reference IO.Handle r, MHandle)]

(!) :: Eq k => [(k, a)] -> k -> a

env ! r = fromJust (lookup r env)

Then to compare the responses from the mock file system to the responses from IO we need to keep track of the state of the mock file system and this mapping; we will refer to this as the *model* for our test:

data Model r = Model Mock (HandleRefs r)

initModel :: Model r

initModel = Model emptyMock []

The model must be polymorphic in r: during test *generation* we will instantiate r to Symbolic, and during test *execution* we will instantiate r to Concrete.
## **Stepping the model**
We want to work towards a function

transition :: Eq1 r => Model r -> Cmd :@ r -> Resp :@ r -> Model r

to step the model; we will gradually build up towards this. First, we can use the model to translate from commands or responses in terms of references to the corresponding commands or responses against the mock file system:

toMock :: (Functor f, Eq1 r) => Model r -> f :@ r -> f MHandle

toMock (Model \_ hs) (At fr) = (hs !) <$> fr

Specifically, this can be instantiated to

toMock :: Eq1 r => Model r -> Cmd :@ r -> Cmd MHandle

which means that if we have a command in terms of references, we can translate that command to the corresponding command for the mock file system and execute it:

step :: Eq1 r => Model r -> Cmd :@ r -> (Resp MHandle, Mock)

step m@(Model mock \_) c = runMock (toMock m c) mock

In order to construct the full new model however we also need to know how to extend the handle mapping. We can compute this by comparing the response we get from the â€œrealâ€ semantics (Resp :@ r) to the response we get from the mock semantics (from step), and simply zip the handles from both responses together to obtain the new mapping. We wrap all this up into an *event*:

data Event r = Event {

`    `before   :: Model  r

`  `, cmd      :: Cmd :@ r

`  `, after    :: Model  r

`  `, mockResp :: Resp MHandle

`  `}

and we construct an event from a model, the command we executed, and the response we got from the real implementation:

lockstep :: Eq1 r

`         `=> Model   r

`         `-> Cmd  :@ r

`         `-> Resp :@ r

`         `-> Event   r

lockstep m@(Model \_ hs) c (At resp) = Event {

`      `before   = m

`    `, cmd      = c

`    `, after    = Model mock' (hs <> hs')

`    `, mockResp = resp'

`    `}

`  `where

`    `(resp', mock') = step m c

`    `hs' = zip (toList resp) (toList resp')

The function we mentioned at the start of this section is now easily derived:

transition :: Eq1 r => Model r -> Cmd :@ r -> Resp :@ r -> Model r

transition m c = after . lockstep m c

as well as a function that compares the mock response and the response from the real file system and checks that they are the same:

postcondition :: Model   Concrete

`              `-> Cmd  :@ Concrete

`              `-> Resp :@ Concrete

`              `-> Logic

postcondition m c r = toMock (after e) r .== mockResp e

`  `where

`    `e = lockstep m c r

We will pass this function to quickcheck-state-machine to be run after every command it executes to make sure that the model and the real system do indeed return the same responses; it therefore does not need to be polymorphic in r. (Logic is a type introduced by quickcheck-state-machine; think of it as a boolean with some additional information, somewhat similar to QuickCheckâ€™s Property type.)

Events will also be very useful when we label our tests; more on that later.
## **Constructing symbolic responses**
We mentioned above that we will not write programs with symbolic references in it by hand. Instead what will happen is that we execute commands in the mock file system, and then replace any of the generated handles by new variables. Most of this happens behind the scenes by quickcheck-state-machine, but we do need to give it this function to construct symbolic responses:

symbolicResp :: Model Symbolic

`             `-> Cmd :@ Symbolic

`             `-> GenSym (Resp :@ Symbolic)

symbolicResp m c = At <$> traverse (const genSym) resp

`  `where

`    `(resp, \_mock') = step m c

This function does what we just described: we use step to execute the command in the mock model, and then traverse the response, constructing a new (fresh) variable for each handle. GenSym is a monad defined in quickcheck-state-machine for the sole purpose of generating variables; we wonâ€™t use it anywhere else except in this function.
## **Generating commands**
To generate commands, quickcheck-state-machine requires a function that produces the next command given the current model; this function will be a standard QuickCheck generator. For our running example, the generator is easy to write:

generator :: Model Symbolic -> Maybe (Gen (Cmd :@ Symbolic))

generator (Model \_ hs) = Just $ QC.oneof $ concat [

**This document was truncated here because it was created in the Evaluation Mode.**
