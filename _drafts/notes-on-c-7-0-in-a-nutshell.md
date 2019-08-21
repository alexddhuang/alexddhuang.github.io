---
title: "Notes on \"C# 7.0 in a Nutshell\""
category: IT
tags: csharp
toc: true
---

[Joseph Albahari](http://www.albahari.com/) and Ben Albahari's book [*C# 7.0 in a Nutshell*](http://www.albahari.com/nutshell/) (2018) is the 4th edition of this book series. Only the first three chapters after the introduction concentrate purely on C#. The remaining chapters cover the core .NET Framework

## Chater 2. C# Language Basics

### Type Basics

#### Conversions

> Implicit conversions are allowed when both of the following are true:
> - The compiler can guarantee they will always succeed.
> - No information is lost in conversion.

#### Value Types Versus Reference Types

> Value types comprise most built-in types (specifically, all numeric types, the `char` type, and the `bool` type) as well as custom `struct` and `enum` types.
>
> Reference types comprise all `class`, `array`, `delegate`, and `interface` types. (This includes the predefined `string` type.) 

### Numeric Types

> The [`decimal`](https://docs.microsoft.com/en-us/dotnet/api/system.decimal) type is typically used for financial calculations, where base-10-accurate arithmetic and high preci‐ sion are required.

#### Specialized Operations on Integral Types

> The `checked` operator tells the runtime to generate an `OverflowException` rather than overflowing silently when an integral-type expression or statement exceeds the arithmetic limits of that type. The checked operator affects expressions with the `++`, `−−`, `+`, `−` (binary and unary), `*`, `/`, and explicit conversion operators between integral types.

### Boolean Type and Operators

#### Bool Conversions

> No casting conversions can be made from the bool type to numeric types or vice versa.

For type safety?

### Variables and Parameters

#### Definite Assignment

> C# enforces a definite assignment policy. In practice, this means that outside of an `unsafe` context, it’s impossible to access uninitialized memory. Definite assignment has three implications:
> - Local variables must be assigned a value before they can be read.
> - Function arguments must be supplied when a method is called (unless marked as optional).
> - All other variables (such as fields and array elements) are automatically initialized by the runtime.

#### Parameters

> To pass by reference, C# provides the `ref` parameter modifier.

> An `out` argument is like a `ref` argument, except it:
> - Need not be assigned before going into the function
> - Must be assigned before it comes out of the function
>
> The `out` modifier is most commonly used to get multiple return values back from a method.

It seems a little bit redundant.

### Null Operators

#### Null Coalescing Operator

> The `??` operator is the null coalescing operator. It says “If the operand is non-null, give it to me; otherwise, give me a default value.” For example:
> 
> ```c#
> string s1 = null;
> string s2 = s1 ?? "nothing";   // s2 evaluates to "nothing"
> ```

It is a syntax sugar of `string s2 = s1 == null ? "nothing" : null`.

#### Null-conditional Operator (C# 6)

> It allows you to call methods and access members just like the standard dot operator, except that if the operand on the left is null, the expression evaluates to `null` instead of throwing a `NullReferenceException`:
> 
> ```c#
> System.Text.StringBuilder sb = null;
> string s = sb?.ToString(); // No error; s instead evaluates to null
> ```

It is a syntax sugar of `string s = sb == null ? null : sb.ToString()`.
