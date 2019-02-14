# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from bs4 import BeautifulSoup
from JInfomation.items import JinfomationItem

class QiushiSpider(scrapy.Spider):
    name = 'QiuShi'
    allowed_domains = ['qiushibaike.com']
    base_url = 'https://www.qiushibaike.com'

    # topic_list = ['8hr', 'hot', 'imgrank']
    #hot imgrank 页面排版不同，需要重新写规则
    topic_list = ['8hr']

    def start_requests(self):
        for topic in self.topic_list:
            for i in range(1, 11):
                url = self.base_url + '/' + topic + '/page/' + str(i) + '/'
                print('开始爬取糗事百科：' + url)
                yield Request(url, callback=self.parse)

    def parse(self, response):
        bsc = BeautifulSoup(response.text, 'lxml')
        content_data = bsc.find('div', class_='recommend-article')
        list_content = content_data.find('ul')
        content_list = list_content.find_all('li', recursive=False)

        for item_data in content_list:
            if item_data.find('a') == None:
                continue
            url_path = item_data.find('a')['href']
            url = self.base_url + url_path

            item_id = item_data['id']

            content_right = item_data.find('div', class_='recmd-right')
            user_info = content_right.find('a', class_='recmd-user')
            user_img = 'https:' + user_info.find('img')['src']
            user_name = user_info.find('span').get_text()

            content_left = item_data.find('a')
            video_duration = None
            if content_left['class'][1] == 'video':
                video_duration = content_left.find('div').get_text()

            if content_left['class'][1] != 'word':
                thumbnail_img = 'https:' + content_left.find('img')['src']


            yield Request(url, callback=self.content_parse, meta={'item_id': item_id,
                                                                  'user_img': user_img,
                                                                  'user_name': user_name,
                                                                  'thumbnail_img': thumbnail_img,
                                                                  'video_duration': video_duration
                                                                  })

    def content_parse(self, response):
        item = JinfomationItem()
        item['info_id'] = response.meta['item_id']
        item['user_name'] = response.meta['user_name']
        item['user_img'] = response.meta['user_img']
        item['thumbnail_img'] = response.meta['thumbnail_img']
        item['video_duration'] = response.meta['video_duration']

        bsc = BeautifulSoup(response.text, 'lxml')
        content_data = bsc.find('div', class_='col1 new-style-col1')

        item['title'] = content_data.find('h1', class_='article-title').get_text()
        publish_time = content_data.find('div', class_='stats').find('span', class_='stats-time').get_text()
        item['publish_time'] = publish_time.replace('\n', '')

        item['content_desc'] = content_data.find('div', class_='content').get_text()

        img_content = content_data.find('div', class_='thumb')
        if img_content != None:
            content_img_datas = img_content.find_all('img')
            img_urls = []
            for img_data in content_img_datas:
                img_url = 'https:' + img_data['src']
                img_urls.append(img_url)
            item['content_imgs'] = img_urls

        video_data = content_data.find('video')
        if video_data != None:
            item['video_url'] = video_data.find('source')['src']

        yield item