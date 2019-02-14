# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from JInfomation.items import JinfomationItem
from urllib.parse import urlencode
import requests
import json


'''https://is.snssdk.com/bds/feed/stream/?iid=60098419220&resolution=1242*2688&os_version=12.1.2&app_name=super&channel=App%20Store&idfa=0EA5AE11-4F23-4ED8-A06C-DB7AB9F24ED1&device_platform=iphone&vid=432B1874-E09C-485C-8CDA-7BD006A86163&openudid=0c7a8d334449a1af809dd2cc83ae71710ebd58cd&device_type=iPhone11,6&idfv=432B1874-E09C-485C-8CDA-7BD006A86163&version_code=1.5.5&ac=WIFI&device_id=58287653281&aid=1319&update_version_code=1551&direction=1&cursor=1549849931742&api_version=2&feed_count=1&list_type=1&mas=00fb71866958a370f99e174e65b7210311bcc8b1d06da2f2dba387&as=a2f5dd2608165cc5803591&ts=1549849960'''


_base_url = 'https://is.snssdk.com/bds/feed/stream/'
_params = {'iid': '60098419220',
           'resolution': '1242*2688',
           'os_version': '12.1.2',
           'app_name': 'super',
           'channel': 'App%20Store',
           'idfa': '0EA5AE11-4F23-4ED8-A06C-DB7AB9F24ED1',
           'device_platform': 'iphone',
           'vid': '432B1874-E09C-485C-8CDA-7BD006A86163',
           'openudid': '0c7a8d334449a1af809dd2cc83ae71710ebd58cd',
           'device_type': 'iPhone11,6',
           'idfv': '432B1874-E09C-485C-8CDA-7BD006A86163',
           'version_code': '1.5.5',
           'ac': 'WIFI',
           'device_id': '58287653281',
           'aid': '1319',
           'update_version_code': '1551',
           'direction': '1',
           'cursor': '1549849931742',
           'api_version': '2',
           'feed_count': '1',
           'list_type': '1',
           'mas': '00fb71866958a370f99e174e65b7210311bcc8b1d06da2f2dba387',
           'as': 'a2f5dd2608165cc5803591',
           'ts': '1549849960'
           }
_headers = {
    'Host': 'is.snssdk.com',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1',
    'Cookie': 'odin_tt=bdec917e6706affe2324cd407c389347e1d8d47cfba60521354bf6dc5c14746de17637fb91ae537442d5ae1ea352877511ffcbb58274d8ba487a04ac29b24aae'
}

class PipixiaSpider(scrapy.Spider):
    name = 'PiPiXia'
    allowed_domains = ['snssdk.com']

    def start_requests(self):
        data = urlencode(_params)
        url = _base_url + "?" + data
        print('开始爬取皮皮虾：' + url)
        for i in range(10):
            yield Request(url, headers=_headers, callback=self.parse)

    def parse(self, response):
        dict = json.loads(response.text)

        data_array = dict['data']['data']
        for data_dict in data_array:
            if data_dict['cell_type'] != 1:
                continue

            item = JinfomationItem()
            item_dict = data_dict['item']
            item['info_id'] = item_dict['item_id_str']
            item['publish_time'] = item_dict['create_time']

            item['title'] = item_dict['share']['title']

            video_data = item_dict['video']
            if video_data != None:
                item['video_id'] = video_data['video_id']
                # 三个画质 video_low 、 video_mid 、 video_high
                video_info = video_data['video_mid']
                item['thumbnail_img'] = video_info['cover_image']['url_list'][0]['url']
                item['video_url'] = video_info['url_list'][0]['url']

            user_dict = item_dict['author']
            item['user_name'] = user_dict['name']
            item['user_img'] = user_dict['avatar']['url_list'][0]['url']

            yield item





