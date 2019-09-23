---
title: "Notes on The C Programming Language, 2nd Edition"
categories: IT
tags: c
toc: true
---

[*The C Programming Language*](https://en.wikipedia.org/wiki/The_C_Programming_Language) by [Brian Kernighan](https://www.cs.princeton.edu/~bwk/) and [Dennis Ritchie](https://www.bell-labs.com/usr/dmr/www/), the first edition was published in 1978, and the second edition was published in 1988.

> C is not a big language, and it is not well served by a big book.
> 
> -- Preface

> Most of the treatment is based on reading, writing and revising examples, rather than on mere statements of rules.
> 
> -- Preface to the First Edition

## Solutions to Exercises

### Exercise 1-2

> Experiment to find out what happens when `printf`'s argument string contains `\c`, where `c` is some character not listed above.

It will ignore `\` and print `c`.
