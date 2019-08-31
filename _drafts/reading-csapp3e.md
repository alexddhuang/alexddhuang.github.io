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
