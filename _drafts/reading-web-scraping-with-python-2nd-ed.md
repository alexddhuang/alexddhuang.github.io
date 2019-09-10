---
title: "Reading Web Scraping with Python, 2nd ED"
categories: IT
tags: web scraper python
toc: true
---

Here are some notes on the book [*Web Scraping with Python*, 2nd Edition](https://www.oreilly.com/library/view/web-scraping-with/9781491985564/) (2018) by [Ryan Mitchell](http://ryanemitchell.com/).

## Part I. Building Scrapers

### Chapter 1. Your First Web Scraper

#### An Introduction to [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)

A simple example:

```python
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page1.html")
bs = BeautifulSoup(html, "html.parser")
print(bs.h1)
```

### Chapter 3. Writing Web Crawlers

#### Traversing a Single Domain

In this section, the author wrote a [Six Degrees of Wikipedia](https://en.wikipedia.org/wiki/Wikipedia:Six_degrees_of_Wikipedia) solution finder. But when I tried to access `https://en.wikipedia.org` through `urlopen`, I got an error report:

```
ConnectionResetError: [Errno 54] Connection reset by peer
```

I didn't know how to solve it. Maybe it was caused by the network environment. Alternatively, I wrote a Python script to find a path of Six Degrees of GitHub:

```python
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random

random.seed(datetime.datetime.now())
def getLinks(username):
    html = urlopen('https://github.com{}?tab=followers'.format(username))
    bs = BeautifulSoup(html, 'html.parser')
    return bs.select('a[data-hovercard-type="user"]')

links = getLinks('/alexddhuang')
while len(links) > 0:
    newUser = links[random.randint(0, len(links) - 1)].attrs['href']
    print(newUser)
    links = getLinks(newUser)
```