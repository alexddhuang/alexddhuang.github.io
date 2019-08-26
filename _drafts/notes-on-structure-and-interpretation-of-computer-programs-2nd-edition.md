---
title: "Notes on \"Structure and Interpretation of Computer Programs, 2nd Edition\""
categories: IT
tags: programming
toc: true
---

[*Structure and Interpretation of Computer Programs*, 2nd Edition](https://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book.html) by [Harold Abelson](https://en.wikipedia.org/wiki/Hal_Abelson) and [Gerald Jay Sussman](https://en.wikipedia.org/wiki/Gerald_Jay_Sussman) with Julie Sussman.

## Chapter 1. Building Abstractions with Procedures
### The Elements of Programming

Every powerful language has three mechanisms for accomplishing combining simple ideas to form more complex ideas:

1. *primitive expressions*, which represent the simplest entities the language is concerned with,
2. *means of combination*, by which compound elements are built from simpler ones, and
3. *means of abstraction*, by which compound elements can be named and manipulated as units.

#### Expressions

> You type an expression, and the interpreter responds by displaying the result of its evaluating that expression.

Lisp uses the *prefix notation* for combinations, one of the benefits is that there never arise any questions like *operator precedence*.

#### Naming and the Environment

The general form of defining names:

```scheme
(define <name> <object>)
```

The interpreter must maintain some sort of memory that keeps track of the name-object pairs. These memories are called *environments*.

#### Evaluating Combinations

To evaluate a combination, the interpreter first evaluates subexpressions of the combination, then applies values of subexpressions to the arguments of the leftmost operator. Thus, the evaluation rule is **recursive** in nature.

#### Compound Procedures

The general form of a procedure definition:

```scheme
(define (<name> <formal parameters>) <body>)
```

#### The Substitution Model for Procedure Application

> To apply a compound procedure to arguments, evaluate the body of the procedure with each formal parameter replaced by the corresponding argument.

There are two orders:

1. Normal order: fully expand and then reduce.
2. Applicative order: evaluate the arguments and then apply.

#### Conditional Expressions and Predicates

The general form of a conditional expression:

```scheme
(cond (<p1> <e1>)
      (<p2> <e2>)
      
      (<pn> <en>))
```

The general form of an `if` expression:

```scheme
(if <predicate> <consequent> <alternative>)
```

#### Example: Square Roots by Newton's Method

The equation of the *tangent line* to the curve $y = f(x)$ at $x = x_n$ is

$$
y = f'(x_n)(x - x_n) + f(x_n)
$$

Then we take the intersection of this line with the x-axis as the next approximation solution $x_{n+1}$.

$$
x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}
$$

Solving square roots $\sqrt{a}$ equals to solving the root of equation $y = x^2 - a$, so we have

$$
x_{n+1} = x_{n} - \frac{x^2_n - a}{2x_n} = \frac{x_n + a/x_n}{2}
$$

```scheme
(define (sqrt-iter guess x)
  (if (good-enough? guess x)
      guess
      (sqrt-iter (improve guess x)
                 x)))

(define (improve guess x)
  (average guess (/ x guess)))

(define (average x y)
  (/ (+ x y) 2))

(define (good-enough? guess x)
  (< (abs (- (square guess) x)) 0.001))

(define (abs x) (if (< x 0) (- 0 x) x))
(define (square x) (* x x))

(define (sqrt x)
  (sqrt-iter 1.0 x))
```

#### Procedures as Black-Box Abstractions
### Procedures and the Processes They Generate
#### Linear Recursion and Iteration
#### Tree Recursion
#### Orders of Growth
#### Exponentiation
#### Greatest Common Divisors
#### Example: Testing for Primality
### Formulating Abstractions with Higher-Order Procedures
#### Procedures as Arguments
#### Constructing Procedures Using Lambda
#### Procedures as General Methods
#### Procedures as Returned Values
## Chapter 2. Building Abstractions with Data
### Introduction to Data Abstraction
#### Example: Arithmetic Operations for Rational Numbers
#### Abstraction Barriers
#### What Is Meant by Data?
#### Extended Exercise: Interval Arithmetic
### Hierarchical Data and the Closure Property
#### Representing Sequences
#### Hierarchical Structures
#### Sequences as Conventional Interfaces
#### Example: A Picture Language
### Symbolic Data
#### Quotation
#### Example: Symbolic Differentiation
#### Example: Representing Sets
#### Example: Huffman Encoding Trees
### Multiple Representations for Abstract Data
#### Representations for Complex Numbers
#### Tagged data
#### Data-Directed Programming and Additivity
### Systems with Generic Operations
#### Generic Arithmetic Operations
#### Combining Data of Different Types
#### Example: Symbolic Algebra
## Chapter 3. Modularity, Objects, and State
### Assignment and Local State
#### Local State Variables
#### The Benefits of Introducing Assignment
#### The Costs of Introducing Assignment
### The Environment Model of Evaluation
#### The Rules for Evaluation
#### Applying Simple Procedures
#### Frames as the Repository of Local State
#### Internal Definitions
### Modeling with Mutable Data
#### Mutable List Structure
#### Representing Queues
#### Representing Tables
#### A Simulator for Digital Circuits
#### Propagation of Constraints
### Concurrency: Time Is of the Essence
#### The Nature of Time in Concurrent Systems
#### Mechanisms for Controlling Concurrency
### Streams
#### Streams Are Delayed Lists
#### Infinite Streams
#### Exploiting the Stream Paradigm
#### Streams and Delayed Evaluation
#### Modularity of Functional Programs and Modularity of Objects
## Chapter 4. Metalinguistic Abstraction
### The Metacircular Evaluator
#### The Core of the Evaluator
#### Representing Expressions
#### Evaluator Data Structures
#### Running the Evaluator as a Program
#### Data as Programs
#### Internal Definitions
#### Separating Syntactic Analysis from Execution
### Variations on a Scheme -- Lazy Evaluation
#### Normal Order and Applicative Order
#### An Interpreter with Lazy Evaluation
#### Streams as Lazy Lists
### Variations on a Scheme -- Nondeterministic Computing
#### Amb and Search
#### Examples of Nondeterministic Programs
#### Implementing the Amb Evaluator
### Logic Programming
#### Deductive Information Retrieval
#### How the Query System Works
#### Is Logic Programming Mathematical Logic?
#### Implementing the Query System
## Chapter 5. Computing with Register Machines
### Designing Register Machines
#### A Language for Describing Register Machines
#### Abstraction in Machine Design
#### Subroutines
#### Using a Stack to Implement Recursion
#### Instruction Summary
### A Register-Machine Simulator
#### The Machine Model
#### The Assembler
#### Generating Execution Procedures for Instructions
#### Monitoring Machine Performance
### Storage Allocation and Garbage Collection
#### Memory as Vectors
#### Maintaining the Illusion of Infinite Memory
### The Explicit-Control Evaluator
#### The Core of the Explicit-Control Evaluator
#### Sequence Evaluation and Tail Recursion
#### Conditionals, Assignments, and Definitions
#### Running the Evaluator
### Compilation
#### Structure of the Compiler
#### Compiling Expressions
#### Compiling Combinations
#### Combining Instruction Sequences
#### An Example of Compiled Code
#### Lexical Addressing
#### Interfacing Compiled Code to the Evaluator

## Exercises

### Exercise 1.7

> The `good-enough?` test used in computing square roots will not be very effective for finding the square roots of very small numbers. Also, in real computers, arithmetic operations are almost always performed with limited precision. This makes our test inadequate for very large numbers. Explain these statements, with examples showing how the test fails for small and large numbers. An alternative strategy for implementing `good-enough?` is to watch how guess changes from one iteration to the next and to stop when the change is a very small fraction of the guess. Design a square-root procedure that uses this kind of end test. Does this work better for small and large numbers?

- Small numbers

    Suppose $g$ is a guess for the square root of $x$, and $e$ is an error, then `good-enough?` is equivalent to

    $$
    \left \| g^2 - x \right \| < e \\
    \Rightarrow -e + x < g^2 < e + x
    $$

    If $x$ is a very small number relative to $e$, the fit of $g$ is relatively large, which results in inaccurate results. For example,

    ```scheme
    (sqrt 0.001)
    ; 0.04124542607499115
    (sqrt 0.0001)
    ; 0.03230844833048122
    (sqrt 0.00001)
    ; 0.03135649010771716
    (sqrt 0.000001)
    ; 0.031260655525445276
    (sqrt 0.0000001)
    ; 0.03125106561775382
    ```

- Large numbers

    For some very large numbers, the distance between two floating-point numbers may be larger than the error, so that the computation of `sqrt` will never end.

    For example, suppose the length of the significand of floating-point numbers is 7, then 

    $$
    1.234567\times 10^5 - 1.234566\times 10^5 = 0.1 > 0.001
    $$

    In this case, smaller error would makes the situation worse.