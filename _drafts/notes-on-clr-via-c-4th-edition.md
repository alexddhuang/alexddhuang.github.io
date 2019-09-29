---
title: "Notes on CLR via C#, 4th Edition"
categories: IT
tags: csharp dotnet
toc: true
---

[*CLR via C#*, 4th Edition](https://www.amazon.com/CLR-via-4th-Developer-Reference/dp/0735667454). [Jeffrey Richter](https://twitter.com/jeffrichter). 2012.

## Part I. CLR Basics

### Chapter 1. The CLR’s Execution Model

#### Compiling Source Code into Managed Modules

> A *managed module* is a standard 32-bit Windows portable executable (PE32) file or a standard 64-bit Windows portable executable (PE32+) file that requires the CLR to execute.

There are four parts in a managed module:

- PE32 or PE32+ header
- CLR header
- Metadata
- IL code

#### Combining Managed Modules into Assemblies

An *assembly* is a logical grouping of one or more managed modules or resource files. An assembly is the smallest unit of reuse, security, and versioning.

#### Loading the Common Language Runtime
