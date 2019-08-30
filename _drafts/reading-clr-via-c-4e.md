---
title: "Reading CLR via C#, 4e"
categories: IT
tags: csharp
toc: true
---

[*CLR via C#*](https://www.amazon.com/dp/0735667454) by Jeffrey Richter is a book to explain how to develop applications and reusable classes for the [.NET Framework](https://dotnet.microsoft.com/).

## Part I. CLR Basics

### Chapter 1. The CLR’s Execution Model

#### Compiling Source Code into Managed Modules

A *managed module* is a standard Windows portable executable file that requires the CLR to execute.

> In addition to emitting IL, every compiler targeting the CLR is required to emit full metadata into every managed module.

Uses of metadata:

- Metadata removes the need for native C/C++ header and library files.
- Microsoft Visual Studio uses metadata to help you write code.
- The CLR’s code verification process uses metadata to ensure that your code performs only “type-safe” operations.
- Metadata allows an object’s fields to be serialized into a memory block, sent to another ma- chine, and then deserialized, re-creating the object’s state on the remote machine. (Wow! Born for the internet programming.)
- Metadata allows the garbage collector to track the lifetime of objects. 

#### Combining Managed Modules into Assemblies

What is an assembly?

1. It is a logical grouping of one or more modules or resource files.
2. It is the smallest unit of reuse, security, and versioning.

#### Loading the Common Language Runtime

