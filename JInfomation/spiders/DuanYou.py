# -*- coding: utf-8 -*-
import scrapy


class DuanyouSpider(scrapy.Spider):
    name = 'DuanYou'
    allowed_domains = ['duanyou.com']
    start_urls = ['http://duanyou.com/']

    def parse(self, response):
        pass
