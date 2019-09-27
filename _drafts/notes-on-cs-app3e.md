---
title: "Notes on CS:APP3e"
categories: IT
tags: computer-systems
toc: true
---

[*Computer Systems: A Programmer's Perspective*, 3rd Edition](https://csapp.cs.cmu.edu/) by [Randal E. Bryant](http://www.cs.cmu.edu/~bryant) and [David R. O'Hallaron](http://www.cs.cmu.edu/~droh) was published in 2015.

## Preface

> This book (known as CS:APP) is for computer scientists, computer engineers, and others who want to be able to write better programs by learning what is going on “under the hood” of a computer system.

> Many systems books are written from a *builder’s perspective*, describing how to implement the hardware or the systems software, including the operating system, compiler, and network interface. This book is written from a *programmer’s perspective*, describing how application programmers can use their knowledge of a system to write better programs.

I am thinking whether any person can make a computer from scratch at an acceptable cost these days.

## Chapter 1. A Tour of Computer Systems

### 1.3 It Pays to Understand How Compilation Systems Work

Why programmers need to understand how compilation systems work:

- *Optimizing program performance*.

    - Is a `switch` statement always more efficient than a sequence of `if-else` statements? 
    - How much overhead is incurred by a function call? 
    - Is a `while` loop more efficient than a `for` loop? 
    - Are pointer references more efficient than array indexes? 
    - Why does our loop run so much faster if we sum into a local variable instead of an argument that is passed by reference? 
    - How can a function run faster when we simply rearrange the parentheses in an arithmetic expression?

- *Understanding link-time errors*.

    - What does it mean when the linker reports that it cannot resolve a reference?
    - What is the difference between a static variable and a global variable? 
    - What happens if you define two global variables in different C files with the same name? 
    - What is the difference between a static library and a dynamic library? 
    - Why does it matter what order we list libraries on the command line? 
    - And **scariest of all**, why do some linker-related errors not appear until run time?

- *Avoiding security holes*.

### 1.4 Processors Read and Interpret Instructions Stored in Memory

#### 1.4.1 Hardware Organization of a System

{% include image.html name="hardware-org.png" width="60%" %}

- Buses

    > Buses are typically designed to transfer fixed-size chunks of bytes known as *words*. The number of bytes in a word (the *word size*) is a fundamental system parameter that varies across systems.

- I/O Devices

    > Each I/O device is connected to the I/O bus by either a *controller* or an *adapter*. The distinction between the two is mainly one of packaging. Controllers are chip sets in the device itself or on the system’s main printed circuit board (often called the *motherboard*). An adapter is a card that plugs into a slot on the motherboard.

- Main Memory

    > Physically, main memory consists of a collection of *dynamic random access memory* (DRAM) chips. Logically, memory is organized as a linear array of bytes, each with its own unique address (array index) starting at zero.

- Processor

    > The *central processing unit* (CPU), or simply *processor*, is the engine that interprets (or *executes*) instructions stored in main memory. At its core is a word-size storage device (or *register*) called the *program counter* (PC). At any point in time, the PC points at (contains the address of) some machine-language instruction in main memory.

### 1.7 The Operating System Manages the Hardware

The operating system has two primary purposes: 

1. To protect the hardware from misuse by runaway applications.
2. To provide applications with simple and uniform mechanisms for manipulating complicated and often wildly different low-level hardware devices.

For achieving these goals, operating systems provide three layers of abstraction:

{% include image.html name="operating-system-abstractions.png" width="50%" %}

- Processes

    A *process* is the operating system's abstraction for a running program. The operating system keeps track of all the state information which is called the *context*. At any point in time, a *uniprocessor system* can only execute the code for a single process. When the operating system decides to run another process, it performs a *context switch* by saving the context of the current process.

- Threads

    A process can consist of multiple execution units, called *threads*. Comparing with processes, threads have some benefits on concurrent programming:

    - It's easier to share data between multiple threads than between multiple processes.
    - Threads are typically more efficient than processes.
    - Multi-threading is a way to make programs run faster when multiple processors are available.

- Virtual Memory

    > *Virtual memory* is an abstraction that provides each process with the illusion that it has exclusive use of the main memory.

- Files

    > A *file* is a sequence of bytes, nothing more and nothing less.

### 1.9 Important Themes

#### 1.9.1 Amdahl’s Law

> [Gene Amdahl](https://en.wikipedia.org/wiki/Gene_Amdahl), one of the early pioneers in computing, made a simple but insightful observation about the effectiveness of improving the performance of one part of a system. This observation has come to be known as *Amdahl’s law*. The main idea is that when we speed up one part of a system, the effect on the overall system performance depends on both how significant this part was and how much it sped up.

Consider a system in which executing some application requires time $T_{old}$. Suppose some part of the system requires a fraction $\alpha$ of this time. After improving the performance of this part by a factor $k$, the overall execution time is

$$
\begin{aligned}
T_{new} &= \frac{\alpha}{k}T_{old} + (1-\alpha)T_{old} \\
&= (\frac{\alpha}{k} + (1-\alpha))T_{old} 
\end{aligned}
$$

So the speedup $S=T_{old}/T_{new}$ equals

$$
\frac{1}{1-\alpha+\alpha / k}
$$

Let $\alpha=80\%$ and $k=10$, we get that $S\approx3.57$. 

> Even though we made a substantial improvement to a major part of the system, our net speedup was significantly less than the speedup for the one part.

#### 1.9.2 Concurrency and Parallelism

- *Concurrency*: the general concept of a system with multiple, simultaneous activities.
- *Parallelism*: the use of concurrency to make a system run faster.
