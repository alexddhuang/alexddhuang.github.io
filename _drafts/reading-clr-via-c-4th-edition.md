---
title: "Reading CLR via C#, 4th Edition"
categories: IT
tags: csharp dotnet
toc: true
---

[*CLR via C#*, 4th Edition](https://www.oreilly.com/library/view/clr-via-c/9780735668737/) (2012) by [Jeffrey Richter](https://twitter.com/jeffrichter).

## Part I. CLR Basics

### Chapter 1. The CLR’s Execution Model

#### Compiling Source Code into Managed Modules

The CLR runs *managed modules*. A managed module contains these parts:

- PE32 or PE32+ header
- CLR header
- Metadata
- IL code