---
title: "Notes on Eloquent JavaScript, 3rd Edition"
categories: IT
tags: javascript
toc: true
---

Here are my notes on [Marijn Haverbeke](https://twitter.com/MarijnJH)'s [*Eloquent JavaScript*, 3rd Edition](https://eloquentjavascript.net/).

## Part I. Language 

### Chapter 3. Functions

#### Bindings and Scopes

> Each binding has a scope, which is the part of the program in which the binding is visible.

> The set of bindings visible inside a block is determined by the place of that block in the program text. Each local scope can also see all the local scopes that contain it, and all scopes can see the global scope. This approach to binding visibility is called lexical scoping.

#### Declaration Notation

> Function declarations are not part of the regular top-to-bottom flow of control. They are conceptually moved to the top of their scope and can be used by all the code in that scope. This is sometimes useful because it offers the freedom to order code in a way that seems meaningful, without worrying about having to define all functions before they are used.

#### Arrow Functions

> There’s no deep reason to have both arrow functions and `function` expressions in the language.

#### Optional Arguments

- Downside: You’ll accidentally pass the wrong number of arguments to functions, and no one will tell you about it.
- Upside: A function is allowed to be called with different numbers of arguments.

#### Closure

> This feature -- being able to reference a specific instance of a local binding in an enclosing scope -- is called closure. A function that references bindings from local scopes around it is called a closure. 
