# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from JInfomation.items import JinfomationItem


class BaisiSpider(scrapy.Spider):
    name = 'Baisi'
    allowed_domains = ['budejie.com/']
    base_url = 'http://www.budejie.com/'

    def start_requests(self):
        for i in range(1, 11):
            url = self.base_url + str(i)
            print('开始爬取百思不得姐：' + url)
            yield Request(url, callback=self.parse)

    def parse(self, response):
        bsC = BeautifulSoup(response.text, 'lxml')
        contentData = bsC.find('div', class_='j-r-c')
        list_contents = contentData.find_all('div', class_='j-r-list')

        for list_content_bs in list_contents:
            list_content = list_content_bs.find('ul')
            content_list = list_content.find_all('li', recursive=False)
            for data_bs in content_list:
                item = JinfomationItem()
                user_img = data_bs.find('div', class_='u-img')
                item['user_img'] = user_img.find('img')['src']

                user_name = data_bs.find('div', class_='u-txt')
                item['user_name'] = user_name.find('a', class_='u-user-name').get_text()
                item['publish_time'] = user_name.find('span').get_text()

                item['title'] = data_bs.find('div', class_='j-r-list-c-desc').find('a').get_text()
                content_img_bs = data_bs.find('div', class_='j-r-list-c-img')
                content_img = content_img_bs.find('img', class_='lazy')['data-original']
                item['content_imgs'] = content_img
                item['thumbnail_img'] = content_img

                item['info_id'] = 'baisi_' + data_bs.find('div', class_='j-r-list-tool')['data-id']
                yield item