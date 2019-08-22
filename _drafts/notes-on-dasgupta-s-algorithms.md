---
title: "Notes on Dasgupta's \"Algorithms\""
category: IT
tags: algorithms
toc: true
---

[Sanjoy Dasgupta](https://cseweb.ucsd.edu/~dasgupta/)'s [*Algorithms*](https://www.amazon.com/dp/0073523402) is a book developed from a set of lecture notes at Berkeley and U. C. San Diego.

## Chapter 1 Algorithms with numbers

The heart of the technology that enables secure communication in today’s global information environment: **Factoring a number is very hard, while testing the primarity of a number is easy**.

### 1.1 Basic arithmetic 

#### 1.1.1 Addition

A simple law: In any base b ≥ 2, the sum of any three single-digit numbers is at most two digits long.

Proof: We just need to proove that least number with three digits $(100)_b$ minus the biggest number of sum of three single-digit numbers $3(b-1)$ will produce a result bigger than zero:

$$
(100)_b - 3(b-1) = b^2 - 3b + 3
$$

It is easy to see that for all $b \geq 2$, this value is greater than 0.

Now let us see the algorithm of addition of two positioning numbers. Since each of individual sum is a two-digit number, *the carry is always a single digit*. Then we can know that the time complexity of addition is $O(n)$, where $n$ is the length of digits.

#### 1.1.2 Multiplication and division

$\underbrace{O(n)+O(n)+\cdots+O(n)}_{n-1}=O(n^2)$
