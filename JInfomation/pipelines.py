# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class JinfomationPipeline(object):
    def process_item(self, item, spider):

        #爬取结果处理
        print(item)

        return item
