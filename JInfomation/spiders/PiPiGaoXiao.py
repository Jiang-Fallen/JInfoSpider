# -*- coding: utf-8 -*-
import scrapy


class PipigaoxiaoSpider(scrapy.Spider):
    name = 'PiPiGaoXiao'
    allowed_domains = ['pipigaoxiao.com']
    start_urls = ['http://pipigaoxiao.com/']

    def parse(self, response):

        pass
