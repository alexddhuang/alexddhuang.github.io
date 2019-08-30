---
title: "基于贝叶斯平均制作豆瓣书籍排行榜"
date: 2019-08-30 13:33:18 +0800
categories: IT
tags: bayesian-average books python douban
---

当你在[豆瓣](https://book.douban.com/)上搜索书籍时，你会发现得到的搜索结果的排序是完全让人摸不着头脑的，所以我打算写一个 Python 脚本通过访问豆瓣 API 获取书籍信息，然后利用[贝叶斯平均](https://en.wikipedia.org/wiki/Bayesian_average)计算出每本书的综合评分，再根据此评分作出一个排行榜。

贝叶斯平均的公式如下：

$$
\bar{x} = \frac{Cm + \sum^{n}_{i=1} x_i}{C + n}
$$

其中 $n$ 为该项目的票数，$x_i$ 为该项目各张投票的票面值（分数），那么 $\sum^{n}_{i=1} x_i$ 即为该项目的总分数了。$C$ 是一个与数据集大小相关的数，$m$ 是一个预设平均值。该公式的意义就是，假设先给每个项目投 $C$ 张票，每张票的分数为 $m$，然后再加上实际的投票情况算出一个算术平均值。这样做的目的是尽量抹平各个项目之间票数的差异。

具体到我们要实现的这个脚本，我们令 $C$ 为每本书的平均票数，$m$ 为所有票面值的算术平均值。

代码：[`top-books.py`](https://github.com/alexddhuang/douban-rank/blob/master/top-books.py)。
