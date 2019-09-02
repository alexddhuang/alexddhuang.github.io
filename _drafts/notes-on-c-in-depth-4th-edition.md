---
title: "Notes on C# in Depth, 4th Edition"
categories: IT
tags: csharp
toc: true
---

[*C# in Depth*](https://csharpindepth.com/), 4th Edition (2019) by [Jon Skeet](https://stackoverflow.com/users/22656/jon-skeet).

## Part 2. C# 2–5

### 2. C# 2

#### 2.1 Generics

Where to use *generics*?

- Collections
- Delegates, particularly in [LINQ](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/linq/)
- Asynchronous code, where a `Task<T>` is a promise of a future value of type `T`
- Nullable value types