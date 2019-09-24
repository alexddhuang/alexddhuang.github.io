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

## Character Input and Output

> The model of input and output supported by the standard library is very simple. Text input or output, regardless of where it originates or where it goes to, is dealt with as streams of characters. A *text stream* is a sequence of characters divided into lines; each line consists of zero and more characters followed by a newline character. It is the responsibility of the library to make each input or output stream conform to this model; the C programmer using the library need not worry about how lines are represented outside the program.

### File Copying

```c
#include <stdio.h>

main()
{
    int c;

    while ((c = getchar()) != EOF)
        putchar(c);
}
```

## Solutions to Exercises

### Exercise 1-2

> Experiment to find out what happens when `printf`'s argument string contains `\c`, where `c` is some character not listed above.

It will ignore `\` and print `c`.
