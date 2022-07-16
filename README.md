# 豆瓣top250电影爬取demo

试听B站IT私塾视频后的一个实现。老师讲的很清楚，非常适合我这样的蒟蒻。

地址：[https://www.bilibili.com/video/BV12E411A7ZQ?p=1&vd_source=1059275620bd0ed824dec12d68d5a48d](https://www.bilibili.com/video/BV12E411A7ZQ?p=1&vd_source=1059275620bd0ed824dec12d68d5a48d)

还是必须要亲自实现一遍，才能成为自己的东西。

这个工作其实早就该做了，拖到现在还没看完确实该好好反省了。

## 使用到的库包括以下

| 库     | 功能 |
| ------- | -------- |
| bs4     | 文本分析 |
| re      | 正则解析 |
| urllib  | 服务器访问 |
| xlwt    | Excel存储 |
| sqlite3 | 数据库存储 |

## Echarts可视化图表和Wordcloud词云

使用方法参考官网

我的笔记：https://xuanyuangoudan.cyou/2022/07/16/2022_07_16/#more

## 静态页面站点

https://xuanyuangoudan.cyou/Douban_flask/templates/index

这里由于page只支持静态网页，所以从数据库读出的数据在HTML中无法通过Jinja2赋值

如果是本地搭建的服务器应该就不会出现显示不出数据的问题

## 学习笔记

[https://xuanyuangoudan.cyou/categories/%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0/%E7%88%AC%E8%99%AB/](https://xuanyuangoudan.cyou/categories/%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0/%E7%88%AC%E8%99%AB/)
