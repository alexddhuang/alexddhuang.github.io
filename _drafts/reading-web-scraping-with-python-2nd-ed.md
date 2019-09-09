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