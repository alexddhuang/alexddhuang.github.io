---
title: "Reading Hands-On Programming with R"
categories: IT
tags: r
toc: true
---

[*Hands-On Programming with R*](https://rstudio-education.github.io/hopr/) was written by [Garrett Grolemund](https://twitter.com/statgarrett).

## I Part 1

### 1 Project 1: Weighted Dice

> Your first mission is simple: assemble R code that will simulate rolling a pair of dice, like at a craps table. Once you have done that, we’ll weight the dice a bit in your favor, just to keep things interesting.

### 2 The Very Basics

#### 2.2 Objects

Creating an object:

```r
die <- 1:6

die
## 1 2 3 4 5 6
```

`<-` is an assignment operator of R. The `:` operator returns a vector.

R vectors support *element-wise execution*:

```r
die - 1
## 0 1 2 3 4 5

die / 2
## 0.5 1.0 1.5 2.0 2.5 3.0

die * die
## 1  4  9 16 25 36
```

If you give R two vectors of unequal lengths, R will repeat the shorter vector until it is as long as the longer vector, and then do the math. If the length of the short vector does not divide evenly into the length of the long vector, R will return a warning message. This behavior is known as *vector recycling*.

```r
die + 1:2
## 2 4 4 6 6 8

die + 1:4
## Warning message:
## In die + 1:4 : 长的对象长度不是短的对象长度的整倍数
```

Of course, R also supports normal matrix operations:

```r
die %*% die # Inner product
## 91

die %o% die # Outer product
##      [,1] [,2] [,3] [,4] [,5] [,6]
## [1,]    1    2    3    4    5    6
## [2,]    2    4    6    8   10   12
## [3,]    3    6    9   12   15   18
## [4,]    4    8   12   16   20   24
## [5,]    5   10   15   20   25   30
## [6,]    6   12   18   24   30   36

t(die) # Transposition
##      [,1] [,2] [,3] [,4] [,5] [,6]
## [1,]    1    2    3    4    5    6
```

#### 2.3 Functions

We can simulate a roll of the die with R’s `sample` function:

```r
sample(die, size = 1)
## 5

sample(die, size = 2)
## 3 5

sample(die, size = 6)
## 6 3 5 4 1 2

sample(die, size = 7)
## Error in sample.int(length(x), size, replace, prob) : 
##   'replace = FALSE'，因此不能取比总体要大的样本

sample(die, size = 7, replace = TRUE)
## 3 5 5 2 3 4 5
```

If you don't know the arguments of a function, you can call `args`:

```r
args(sample)
## function (x, size, replace = FALSE, prob = NULL) 
## NULL
```

#### 2.4 Writing Your Own Functions

```r
roll <- function() {
    die <- 1:6
    dice <- sample(die, size = 2, replace = TRUE)
    sum(dice)
}

roll()
## 10
roll()
## 8
```

#### 2.5 Arguments

```r
roll <- function(bones = 1:6) {
    dice <- sample(bones, size = 2, replace = TRUE)
    sum(dice)
}
```

### 3 Packages and Help Pages

#### 3.1 Packages

Run `install.packages("ggplot2")` to install the [`ggplot2`](https://ggplot2.tidyverse.org/) package, which is a system for declaratively creating graphics.

Run `library("ggplot2")` to load it.

```r
x <- c(-1, -0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1)
qplot(x, x^3)
```

{% include image.html name="xxx.png" width="50%" %}

If you pass only one vector to `qplot(x, binwidth = w)`, it will draw a histogram.
