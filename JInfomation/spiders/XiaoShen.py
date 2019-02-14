# -*- coding: utf-8 -*-
import scrapy


class XiaoshenSpider(scrapy.Spider):
    name = 'XiaoShen'
    allowed_domains = ['xiaoshen.com']
    start_urls = ['http://xiaoshen.com/']

    def parse(self, response):
        pass
