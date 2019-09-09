---
title: "Reading Concrete Mathematics, 2nd ED"
categories: IT
tags: computer-science math
toc: true
---

Here are some notes on the book [*Concrete Mathematics*, 2nd Edition](https://en.wikipedia.org/wiki/Concrete_Mathematics) (1994) by [Ronald Graham](http://www.math.ucsd.edu/~fan/ron/), [Donald Knuth](https://www-cs-faculty.stanford.edu/~knuth/), and [Oren Patashnik](https://dblp.uni-trier.de/pers/hd/p/Patashnik:Oren). 

Is it a word game? The "Concrete" on the title of this book is a blend of CONtinuous and disCRETE. 

> More concretely, it is the controlled manipulation of mathematical formulas, using a collection of techniques for solving problems.

> The major topics treated in this book include sums, recurrences, elementary number theory, binomial coefficients, generating functions, discrete probability, and asymptotic methods.

## 1. Recurrent Problems

### 1.1 The Tower of Hanoi

We are given a tower of $n$ disks, initially stacked in decreasing size on one of three pegs. The objective is to transfer the entire tower to one of the other pegs, moving only one disk at a time and never moving a larger one onto a smaller. The question is **how many moves are necessary and sufficient to perform the task**?

Let $T_n$ be the minimum number of moves that will transfer $n$ disks from one peg to another under [Lucas](https://en.wikipedia.org/wiki/%C3%89douard_Lucas)'s rule. For transfering $n$ disks from peg A to peg B, we have to transfer the first $n-1$ disks from A to C, and then move the last disk from A to B, and finally move the $n-1$ disks from C to B. So the sum moves are

$$
T_n = 2T_{n-1} + 1
$$

Combining this formula with the case $T_0=0$, we finally have

$$
T_n = 2^{n} - 1
$$

