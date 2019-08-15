---
title: "Reading Mathematics for 3D Game Programming and Computer Graphics, 3rd Edition"
categories: IT
tags: mathematics game-development computer-graphics
toc: true
---

Here are my notes on [*Mathematics for 3D Game Programming and Computer Graphics*, 3rd Edition](http://mathfor3dgameprogramming.com/) (2011) by [Eric Lengyel](https://twitter.com/EricLengyel).

## Chapter 4 Transforms

### 4.1 Linear Transformations

A linear transformation can be represented by a $n \times n$ matrix $\mathbf{M}$ and an n-dimensional vector $\mathbf{T}$. If a point $\mathbf{P}$ was transformed to a new coordinate framework, the new point $\mathbf{P}'$ can be calculated by

$$
\mathbf{P}' = \mathbf{M}\mathbf{P} + \mathbf{T}
$$

#### 4.1.1 Orthogonal Matrices

Some linear transformations have some eye-catching properties, for example, they **preserve lengths and angles**. This property can be expressed by the following mathematical equation: For every two vectors $\mathbf{P}_1$ and $\mathbf{P}_2$, we have

$$
\mathbf{P}_1 \cdot \mathbf{P}_2 = \mathbf{P}'_1 \cdot \mathbf{P}'_2
$$

Let temporarily ignore the translation vector $\mathbf{T}$, and only pay attention to the matrix $\mathbf{M}$:

$$
\begin{align}
\mathbf{P}_1 \cdot \mathbf{P}_2 &= \mathbf{M}\mathbf{P}_1 \cdot \mathbf{M}\mathbf{P}_2 \\ 
&= (\mathbf{M}\mathbf{P}_1)^T \mathbf{M}\mathbf{P}_2 \\
&= {\mathbf{P}_1}^T \mathbf{M}^T \mathbf{M} \mathbf{P}_2 \\
\end{align}
$$

Now we get a sufficient condition: $\mathbf{M}^T = \mathbf{M}^{-1}$. Is it a necessary condition?

### 4.3 Rotation Transforms
