```
1、目前一共三个爬虫，分别为：
    1) 皮皮虾 ： PiPiXia.py
    2) 百思不得姐：Baisi.py
    3) 糗事百科：QiuShi.py
```

```
2、后续内容：
    1）三个爬虫最终存储到同一个 Item 对象，Item 对象会经过 pipelines.py 类进行处理，使用者需要在 pipelines.py 类中将视频图片转存，并把内容进行上传处理
    2）爬取的站点中存在动态数据刷新， info_id 为当前内容唯一标识，需要服务端做内容重复校验
    3）皮皮虾包含 video_low 、 video_mid 、 video_high 三种视频清晰度，目前为video_mid，需要调整，替换代码中的取值字段
```

```
3、执行(二选一)：
    1) 打开entryPoint.py内相应注释，运行 entryPoint.py 即可
    2) cd 至爬虫项目根目录下执行 （ scrapy crawl 爬虫名称(如：PiPiXia、Baisi、QiuShi) ）
```

```
4、结果示例：
```
![aaa](https://github.com/Jiang-Fallen/source/blob/master/image/img_info_spider_01.jpg)
