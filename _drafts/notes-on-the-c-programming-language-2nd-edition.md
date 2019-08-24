---
title: "Notes on \"The C Programming Language, 2nd Edition\""
categories: IT
tags: c
toc: true
---

Here are some notes on [*The C Programming Language*](https://en.wikipedia.org/wiki/The_C_Programming_Language), 2nd Edition (1988) by [Brian Kernighan](https://en.wikipedia.org/wiki/Brian_Kernighan) and [Dennis Ritchie](https://en.wikipedia.org/wiki/Dennis_Ritchie). Source code are [here](https://github.com/alexddhuang/knrc2e).

## Preface

> C is not a big language, and it is not well served by a big book.

## Preface to the First Edition

> This book is meant to help the reader learn how to program in C. It contains a tutorial introduction to get new users started as soon as possible, separate chapters on each major feature, and a reference manual. Most of the treatment is based on reading, writing and revising examples, rather than on mere statements of rules. For the most part, the examples are complete, real programs, rather than isolated fragments. All examples have been tested directly from the text, which is in machine-readable form. Besides showing how to make effective use of the language, we have also tried where possibleto illustrate useful algorithms and principles of good style and sound design.

Why aren't all books on programming language written in this way?

## Introduction

> C is a relatively "low level" language. This characterization is not pejorative; it simply means that C deals with the same sort of objects that most computers do, namely characters, numbers, and addresses. These may be combined and moved about with the arithmetic and logical operators implemented by real machines.
> 
> C provides no operations to deal directly with composite objects such as character strings, sets, lists, or arrays. There are no operations that manipulate an entire array or string, although structures may be copied as a unit. The language does not define any storage allocation facility other than static definition and the stack discipline provided by the local variables of functions; there is no heap or garbage collection. Finally, C itself provides no input/output facilities; there are no `READ` or `WRITE` statements, and no built-in file access methods. All of these higher-level mechanisms must be provided by explicitly-called functions. Most C implementations have included a reasonably standard collection of such functions.
> 
> Similarly, C offers only straightforward, single-thread control flow: tests, loops, grouping, and subprograms, but not multiprogramming, parallel operations, synchronization, or coroutines.

>  Since C is relatively small, it can be described in a small space, and learned quickly. A programmer can reasonably expect to know and understand and indeed regularly use the entire language.

In fact, [C is not easy to master](https://www.quora.com/How-easy-is-it-to-learn-C).

> C retains the basic philosophy that programmers know what they are doing; it only requires that they state their intentions explicitly.

## Chapter 1. A Tutorial Introduction

### 1.1 Getting Started

> The only way to learn a new programming language is by writing programs in it.

> Normally you are at liberty to give functions whatever names you like, but "main" is special -- your program begins executing at the beginning of `main`. This means that every program must have a `main` somewhere.

[Kiran Kedilaya](https://www.quora.com/profile/Kiran-Kedilaya-1) had provided a [simple explaination](https://www.quora.com/Why-is-the-Main-Function-required-in-C-programming) of why `main` is required:

> For any program to execute, the OS must transfer control to the program. In order to do so, the OS is designed in such a way that it transfers control to the “main” function in any program. This is done in order to maintain uniformity across various programming languages (e.g. C, C++, C#, Java, etc.).

> Exercise 1-2. Experiment to find out what happens when `printf`'s argument string contains `\c`, where `c` is some character not listed above.

Escape `\` and directly print `c`.

### 1.5 Character Input and Output

> The model of input and output supported by the standard library is very simple. Text input or output, regardless of where it originates or where it goes to, is dealt with as streams of characters, A text stream is a sequence of characters divided into lines; each line consists of zero or more characters followed by a new line character. It is the responsibility of the library to make each input or output stream conform to this model; the C programmer using the library need not worry about how lines are represented outside the program.

#### 1.5.1 File Copying

```c
#include <stdio.h>

main()
{
    int c;

    while ((c = getchar()) != EOF)
        putchar(c);
}
```

#### 1.5.2 Character Counting

```c
#include <stdio.h>

main()
{
    double nc;

    for (nc = 0; getchar() != EOF; nc++)
        ;
    printf("%.0f\n", nc);
}
```

#### 1.5.3 Line Counting

```c
#include <stdio.h>

main()
{
    int c, nl = 0;

    while ((c = getchar()) != EOF)
        if (c == '\n')
            nl++;
    printf("%d\n", nl);
}
```

> Exercise 1-8. Write a program to count blanks, tabs, and newlines.

```c
#include <stdio.h>

main()
{
    int c, nb, nt, nl;

    nb = nt = nl = 0;
    while ((c = getchar()) != EOF)
        if (c == ' ')
            nb++;
        else if (c == '\t')
            nt++;
        else if (c == '\n')
            nl++;
    printf("%d %d %d\n", nb, nt, nl);
}
```

> Exercise 1-9. Write a program to copy its input to its output, replacing each string of one or more blanks by a single blank.

```c
#include <stdio.h>

int main()
{
    int inblank = 0;
    int c;

    while ((c = getchar()) != EOF) {
        if (c == ' ') {
            if (!inblank)
                putchar(c);
            inblank = 1;
        } else {
            putchar(c);
            inblank = 0;
        }
    }
}
```

> Exercise 1-10. Write a program to copy its input to its output, replacing each tab by `\t` each backspace by `\b`, and each back slash by `\\`. This makes tabs and backspaces visible in an unambiguous way.

```c
#include <stdio.h>

int main()
{
    int c;

    while ((c = getchar()) != EOF) {
        if (c == '\\')
            printf("\\\\");
        else if (c == '\b')
            printf("\\b");
        else if (c == '\t')
            printf("\\t");
        else 
            putchar(c);
    }
}
```
