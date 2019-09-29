---
title: "Notes on Operating System Concepts, 10th Edition"
categories: IT
tags: operating-system
toc: true
---

*[Operating System Concepts, 10th Edition](https://os-book.com/OS10/index.html)*. [Avi Silberschatz](http://www.cs.yale.edu/homes/avi), [Peter Baer Galvin](http://www.galvin.info/), and [Greg Gagne](http://people.westminstercollege.edu/faculty/ggagne). 2018.

## Part 1. Overview

### Chapter 1. Introduction

#### 1.2 Computer-System Organization

> A modern general-purpose computer system consists of one or more CPUs and a number of device controllers connected through a common bus that provides access between components and shared memory

{% include image.html name="computer-organization.png" %}

> Typically, operating systems have a *device driver* for each device controller. This device driver understands the device controller and provides the rest of the operating system with a uniform interface to the device. The CPU and the device controllers can execute in parallel, competing for memory cycles. To ensure orderly access to the shared memory, a memory controller synchronizes access to the memory.

Interrupts are a key part of how operating systems and hardware interact.
