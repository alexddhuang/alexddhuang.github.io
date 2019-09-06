---
title: "豆瓣书籍排行榜：JavaScript 版"
date: 2019-09-04 20:10:25 +0800
date_modified: 2019-09-07 02:21:23 +0800
categories: IT
tags: douban books bayesian-average javascript
---

之前我写过一个 Python 脚本，它通过豆瓣开放的 API 获取书籍信息，然后根据[贝叶斯平均](/2019/08/30/ji-yu-bei-xie-si-ping-jun-zhi-zuo-dou-ban-shu-ji-pai-xing-bang.html)算出每一本书的综合评分，再根据此评分制作一个排行榜。这一次，我用 JavaScript 重写了这个脚本，这样，我可以把这个脚本挂到网上，服务大家。网址：[https://alexddhuang.github.io/douban-books-rank/](https://alexddhuang.github.io/douban-books-rank/)。

使用 JavaScript 访问豆瓣 API，第一个要解决的就是[跨域访问](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Access_control_CORS)的问题。使用 [`XMLHttpRequest`](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest) 是不行的，但是我们可以用 [JSONP](https://www.w3schools.com/js/js_json_jsonp.asp)。

```javascript
function jsonp(url) {
    const script = document.createElement("script");
    script.type = "text/javascript";
    script.src = url + "&callback=callback";
    document.body.append(script)
}
```

这个函数借用了 `<script>` 元素去访问某个 `url`，服务器返回的 JSON 会传递给一个名叫 `callback` 的全局函数。

具体的代码可以在这里找到：[douban-books-rank](https://github.com/alexddhuang/douban-books-rank)。

-------

**2019-09-07 更新：更快！更强！**

我发现之前的代码做了一些很愚蠢的事情，使得搜索速度不是特别快。豆瓣的搜索 API 是这样的：

```
https://api.douban.com/v2/book/search?q=[q]&start=[start]
```

其中 `q` 是需要搜索的文本，`start` 为每页数据的书籍条目的起始下标。如果不传入 `start` 参数，则该 API 返回第一页数据。每页数据都有字段 `count`，表示该页的书籍条目数量，字段 `start` 表示该页书籍条目的起始下标，字段 `total` 表示书籍条目总数。

我之前是用递归的方式获取所有条目的：

```javascript
function callback(page) {
    const count = page['count'];
    const start = page['start'];
    const total = page['total'];

    // Parse data ...

    if (start + count >= total) {
        // Finish, show results ...
        return;
    }

    jsonp(url + `&start=${start + count}`);
}
```

这样写的缺点是：你必须等待上一页的数据解析完成后，再去访问下一页数据，从而造成了阻塞。

避免阻塞的一个方式就是，在解析数据之前先迭代遍历每一页数据：

```javascript
let readbooks = 0;

function callback(page) {
    const count = page['count'];
    const start = page['start'];
    const total = page['total'];

    if (start == 0) {
        readbooks = 0;

        for (let s = start + count; s < total; s += count) {
            jsonp(url + `&start=${s}`);
        }
    }

    // Parse data ...

    readbooks += count;
    
    if (readbooks >= total) {
        // Finish, show results ...
    }
}
```
