---
title: "Reading Programming C# 5.0"
categories: IT
tags: csharp dotnet
toc: true
---

Here are my notes on the book [*Programming C# 5.0*](http://shop.oreilly.com/product/0636920024064.do) (2012) by Ian Griffiths. The source code is [here](https://github.com/alexddhuang/programming-csharp5).

## Chapter 1. Introducing C#

### Why C#?

Powerful features supported by C#:

- Object-oriented programming
- Generics
- Functional programming
- Both dynamic and static typing
- List- and set-oriented programming, thanks to [Language Integrated Query (LINQ)](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/linq/)
- Asynchronous programming

C# has a powerful runtime ([CLR](https://docs.microsoft.com/en-us/dotnet/standard/clr)) which supports:

- Security sandboxing
- Runtime type checking
- Exception handling
- Thread management
- Automated memory manage­ment

## Chapter 3. Types

### Classes

#### Static Classes

If you want to prevent users to create any instance of your class, you can declare your class as `static`. A static class only has static fields and methods.

#### Reference Types

Types defined by `class` are all *reference types*. A variable of the reference type does not hold the value, but a reference to the value. If you assign this variable to another one, you are copying the reference, but not the value.

