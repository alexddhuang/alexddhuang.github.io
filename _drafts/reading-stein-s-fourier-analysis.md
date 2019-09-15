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

How to prove these are the only (twice differentiable) solutions? First, suppose $f(t)$ is a solution to this equation, then we write it in a form of

$$
f(t) = a(t)\cos{ct} + b(t)\sin{ct}
$$

So our job becomes to prove that $a(t)$ and $b(t)$ are constants. If they are constants, we have

$$
f'(t) = -ca\sin{ct} + cb\cos{ct} \\
-c^{-1}f'(t) = a\sin{ct} - b\cos{ct} \\
f(t)\cos{ct} - c^{-1}f'(t)\sin{ct} = a \\
f(t)\sin{ct} + c^{-1}f'(t)\cos{ct} = b
$$

So we get an inspiration that we may can prove that $g(t)=f(t)\cos{ct} - c^{-1}f'(t)\sin{ct}$ and $h(t)=f(t)\sin{ct} + c^{-1}f'(t)\cos{ct}$ are constants. Let's do it.

$$
\begin{aligned}
g'(t) &= f'(t) \cos{ct} - cf(t) \sin{ct} - c^{-1}f''(t)\sin{ct} - f'(t)\cos{ct} \\
&= - cf(t) \sin{ct} - c^{-1}f''(t)\sin{ct} \\
&= - cf(t) \sin{ct} - c^{-1}(-c^2f(t))\sin{ct} \\
&= 0
\end{aligned}
$$

Similarly, we can get that

$$
h'(t) = 0
$$

Now we know that both $g(t)$ and $h(t)$ are constants, we respectively set them to $a$ and $b$.

$$
g(t)=f(t)\cos{ct} - c^{-1}f'(t)\sin{ct} = a \\
h(t)=f(t)\sin{ct} + c^{-1}f'(t)\cos{ct} = b
$$

Finally, we have

$$
\begin{aligned}
a\cos{ct} + b\sin{ct} &= f(t)\cos^2{ct} - c^{-1}f'(t)\sin{ct}\cos{ct} + f(t)\sin^2{ct} + c^{-1}f'(t)\sin{ct}\cos{ct} \\
&= f(t)
\end{aligned}
$$
