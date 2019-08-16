---
title: "Reading Linear Algebra Done Right, 3rd Edition"
category: Mathematics
tags: linear-algebra
toc: true
---

It's time to pick up the knowledge of linear algebra! My chosen book is Sheldon Axler's [*Reading Linear Algebra Done Right*, 3rd Edition](https://www.amazon.com/dp/3319110799) (2015).

## Chapter 1. Vector Spaces

### 1.B Definition of Vector Space

#### 1.19 Definition vector space

A *vector space* is a set $V$ along with an addition on $V$ and a scalar multiplication on $V$ such that the following properties hold:

- *commutativity*

    $$
    u + v = v + u\text{ }(u,v\in V)
    $$

- *associativity*

    $$
    (u + v) + w = u + (v + w) \text{ and } (ab)c=a(bc) \text{ } (u,v,w\in V \text{ and } a,b,c \in \mathbf{F})
    $$

- *additive identity*

    $$
    \text{there exists an element } 0 \in V \text{ such that } v + 0 = v \text{ for all } v \in V 
    $$

- *additive inverse*

    $$
    \text{ for every } v \in V \text{, there exists } w \in V \text{ such that } v + w = 0
    $$

- *multiplicative identity*

    $$
    1v = v \text{ for all } v \in V
    $$

- *distributive properties*

    $$
    a(u + v) = au + av \text{ and } (a + b)v = av + bv
    $$