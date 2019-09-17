---
title: "Reading Pro Git, 2nd Edition"
categories: IT
tags: git
toc: true
---

Here are some notes on [*Pro Git*, 2nd Edition](https://git-scm.com/book/en/v2) (2014) by [Scott Chacon](http://scottchacon.com/about.html) and [Ben Straub](https://github.com/ben).

## 1. Getting Started

### 1.3 What is Git?

#### Snapshots, Not Differences

Many other VCSs think their data as a list of file-based changes, while Git thinks its data as a stream of snapshots.

> This makes Git more like a mini filesystem with some incredibly powerful tools built on top of it, rather than simply a VCS.

#### Git Has Integrity

> Everything in Git is checksummed before it is stored and is then referred to by that checksum.

The checksum is a [SHA-1](https://en.wikipedia.org/wiki/SHA-1) hash, which is a 40-character string.

### 1.6 First-Time Git Setup

There are three places to store the configuration of Git.

1. `/etc/gitconfig`

    > Contains values applied to every user on the system and all their repositories. If you pass the option `--system` to `git config`, it reads and writes from this file specifically.

2. `~/.gitconfig` or `~/.config/git/config`

    > Values specific personally to you, the user. You can make Git read and write to this file specifically by passing the `--global` option, ...

3. `.git/config`

    > Specific to that single repository. You can force Git to read from and write to this file with the `--local` option, but that is in fact the default.

> You can view all of your settings and where they are coming from using:
> 
> ```bash
> $ git config --list --show-origin
> ```

#### Your Editor

> If you want to use a different text editor, such as Emacs, you can do the following:
> 
> ```bash
> $ git config --global core.editor emacs
> ```

