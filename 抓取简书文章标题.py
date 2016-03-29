#!/usr/bin/env python
# -*- coding:utf-8 -*-

import scrapy

class JianshuSpider(scrapy.Spider):

    """docstring for JianshuSpider"""

    # spider 的名字
    name = "jianshu"
    # 爬虫的起始 url
    start_urls = ["http://www.jianshu.com/collections/16/notes?order_by=added_at"]

    # 爬虫开始，收到响应回调 parse 函数
    def parse(self, response):
        for item in response.css('.article-list li'):
            # 文章标题
            print item.css('h4 a::text').extract()[0].encode('utf-8')
            # 文章链接
            print item.css('h4 a::attr(href)').extract()
