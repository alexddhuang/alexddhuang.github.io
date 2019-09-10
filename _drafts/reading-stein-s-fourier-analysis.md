---
title: "Reading Stein's Fourier Analysis"
categories: Mathematics
tags: fourier-analysis
toc: true
---

Here are some noets on [Elias M. Stein](https://en.wikipedia.org/wiki/Elias_M._Stein)'s textbook [*Fourier Analysis: An Introduction*](https://press.princeton.edu/titles/7562.html) (2003).

## Chapter 1. The Genesis of Fourier Analysis

The problems of the vibrating string and the heat flow led to the development of Fourier Analysis.

### 1 The vibrating string

The motion of a vibrating string is governed by [Hooke's Law](https://en.wikipedia.org/wiki/Hooke's_law): $F=-ky(t)$. Combining this law with [Newton's Second Law](https://en.wikipedia.org/wiki/Newton%27s_laws_of_motion#Newton's_second_law), $F=m\ddot{y}(t)$, we get a differential equation:

$$
m\ddot{y}(t)=-ky(t)
$$

With $c=\sqrt{k/m}$, this equation becomes

$$
\ddot{y}(t) + c^2 y(t) = 0
$$

It is easy to check that the below form of function is a solution of this equation.

$$
y(t) = a \cos{ct} + b \sin{ct}
$$

where $a$ and $b$ are constants.

How to proove these are the only (twice differentiable) solutions?
