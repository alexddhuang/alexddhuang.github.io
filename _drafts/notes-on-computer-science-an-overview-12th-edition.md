---
title: "Notes on \"Computer Science: An Overview, 12th Edition\""
categories: IT
tags: computer-science
toc: true
---

[*Computer Science: An Overview*, 12th Edition](https://www.amazon.com/dp/0133760065) (2014) by Glenn Brookshear and Dennis Brylow.

## Chapter 1. Data Storage

### Bits and Their Storage

*Bits* are *binary digits*. Their meanings depend on how we interpret them.

#### Gates and Flip-­Flops

> A device that produces the output of a Boolean operation when given the operation’s input values is called a gate. 

A pictorial representation of AND, OR, XOR, and NOT gates:

{% include image.html name="and.png" width="30%" %}
{% include image.html name="or.png" width="30%" %}
{% include image.html name="xor.png" width="30%" %}
{% include image.html name="not.png" width="30%" %}

> A flip-flop is a fundamental unit of computer memory. It is a circuit that produces an output value of 0 or 1, which remains constant until a pulse (a temporary change to a 1 that returns to 0) from another circuit causes it to shift to the other value. In other words, the output can be set to “remember” a zero or a one under control of external stimuli.

A simple implementation of flip-flop:

{% include image.html name="flip-flop.png" width="50%" %}

In the normal state, both inputs are set to zeros, and the output can be either 0 or 1. When the upper input receives a pulse, the output value shifts to 1 and then keeps stable; When the lower input receives a pulse, the output value shifts to 0 and then keeps stable.

The flip-flop circuit shows that

1. How devices can be constructed from gates;
2. How abstractions are used;
3. How a bit is stored in computers.

### Main Memory

A computer’s main memory is organized as individual, addressable cells. A cell is typically 8 bits.

### Mass Storage

> Due to the volatility and limited size of a computer’s main memory, most comput- ers have additional memory devices called mass storage (or secondary storage) systems, including magnetic disks, CDs, DVDs, magnetic tapes, flash drives, and solid-state disks.

#### Magnetic Systems

A *magnetic disk* or *hard disk drive (HDD)*:

{% include image.html name="disk.png" width="50%" %}
