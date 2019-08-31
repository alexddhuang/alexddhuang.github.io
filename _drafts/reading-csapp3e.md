---
title: "Reading CSAPP3e"
categories: IT
tags: computer-systems
toc: true
---

[*Computer Systems: A Programmer's Perspective*](https://csapp.cs.cmu.edu/) by [Randal E. Bryant](http://www.cs.cmu.edu/~bryant) and [David R. O'Hallaron](http://www.cs.cmu.edu/~droh) is a book to teach computer systems from a programmer's perspective, that means readers will learn about computer systems in terms of how they affect the behavior and performance of their programs, instead of learning how to design and build a system at first. I am reading the 3rd edition (2015) of this book.

## Chapter 2. Representing and Manipulating Information

### 2.1 Information Storage

#### 2.1.3 Addressing and Byte Ordering

There are two conventions of ordering the bytes of an object:

- Little-endian: the least significant byte comes first.
- Big-endian: the most significant byte comes first.

In what cases, byte ordering should be considered by programmers?

- When binary data are communicated over a network between different machines. For example, in the .Net platform, before the client sending an integer to the server, it needs to invoke [`System.Net.IPAddress.HostToNetworkOrder`](https://docs.microsoft.com/en-us/dotnet/api/system.net.ipaddress.hosttonetworkorder) to convert the integer from host byte order to network byte order; Similarly, after the server receiving the integer, it needs to invoke [`System.Net.IPAddress.NetworkToHostOrder`](https://docs.microsoft.com/en-us/dotnet/api/system.net.ipaddress.networktohostorder).
- When inspecting machine-level programs.
- When programs are written that circumvent the normal type system. An example: [`show-bytes.c`](https://github.com/alexddhuang/csapp3e/blob/master/ch02/show-bytes.c).

### 2.2 Integer Representations

#### 2.2.2 Unsigned Encodings

$$
B2U_w(\vec{x}) \doteq \sum^{w-1}_{i=0} x_i 2^i
$$

Let each $x_i$ be one, we get the maximum $UMax_w = 2^w - 1$, and let each $x_i$ be zero, we get the minimum $UMin_w=0$.

#### 2.2.3 Two’s-Complement Encodings

$$
B2T_w(\vec{x}) \doteq -x_{w-1}2^{w-1} + \sum^{w-2}_{i=0} x_i 2^i
$$

Let $x_{w-1}=0$ and each rest $x_i=1$, we get the maximum $TMax_w=2^{w-1}-1$, and let $x_{w-1}=1$ and each rest $x_i=0$, we get the minimum $TMin_w=-2^{w-1}$.

#### 2.2.4 Conversions between Signed and Unsigned

A general rule of C implementations handling conversions between signed and unsigned numbers at the same word size: *Keep the bit patterns unchanged*.

$$
B2U_w(\vec{x}) - B2T_w(\vec{x}) = x_{w-1}2^{w}
$$

According to this formula, we can easily get the rules of conversions between unsigned and two's-complement.

$$
T2U_w(x) = 
\begin{cases}
x + 2^w, &x < 0 \\
x, &x \geq 0
\end{cases}
$$

$$
U2T_w(x) = 
\begin{cases}
x, &x \leq TMax_w  \\
x - 2^{w}, &x > TMax_w
\end{cases}
$$