---
title: "Start Blog"
date: 2019-08-13 19:54:51 +0800
date_modified: 2019-09-02 00:00:23 +0800
category: IT
tags: blog
---

The reason I start a blog is personal. I want to take notes and record something I did. I like to write in plain text, and building a personal website gives me the freedom to control all contents. [GitHub Pages](https://pages.github.com/) + [Jekyll](https://jekyllrb.com/) is my first choice, since I'm a fan of GitHub, and the service of GitHub Pages is free.

Choosing which Jekyll theme has bothered me for a while. Finally, I choose the default one: [Minima](https://github.com/jekyll/minima). It's very simple, tiny, and elegant. Although it is lack of some powerful features, I can implement them by myself.

The normal way to import a Jekyll theme is adding the below line into `_config.yml`.

```yml
theme: JEKYLL_THEME_NAME
```

However, this way is not convenient for customization. Yes, you can copy a template file into your repo and modify it, but what if this file in the original repo were updated? You have to copy it again and compare the difference carefully, and then merge them.

My method is forking the target theme (in my case, the Minima theme), then create a branch (in my case, named `alexddhuang`). In this branch, I can do any customization I want to do. Then, I use the [`jekyll-remote-theme`](https://github.com/benbalter/jekyll-remote-theme) plugin to import this branch:

```yml
plugins:
  - jekyll-remote-theme

remote_theme: alexddhuang/minima@alexddhuang
```

Now, if the original repo of Minima updates, I can fetch all those changes and merge them into the `alexddhuang` branch by using Git:

```bash
$ git checkout alexddhuang
$ git merge master
```