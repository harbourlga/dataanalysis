#!/usr/bin/python
# encoding: utf-8

# from scrapy.spiders import BaseSpider
from scrapy.http import Request
from scrapy.selector import Selector
import scrapy
from douban.items import DoubanBookItem

class Books(BaseSpider):
    name ='DoubanBooks'
    start_urls = ['http://book.douban.com/top250']


    def parse(self,response):

        selector = Selector(response)
        books = selector.xpath('//tr[@class="item"]')

        for eachbook in books:
            item = DoubanBookItem()

            title=eachbook.xpath('td[@valign="top"  and not(@width)]/div[@class="pl2"]/a/text()').extract()
            title = title[0]

            title2=eachbook.xpath('td[@valign="top"  and not(@width)]/div[@class="pl2"]/span/text()').extract()
            title2=title2[0] if len(title2)>0 else ''

            info =eachbook.xpath('td[@valign="top"  and not(@width)]/p[@class="pl"]/text()').extract()
            info = info[0]
            rate=eachbook.xpath('td[@valign="top"  and not(@width)]/div[@class="star clearfix"]/span[@class="rating_nums"]/text()').extract()
            rate= rate[0]
            hot=eachbook.xpath('td[@valign="top"  and not(@width)]/div[@class="star clearfix"]/span[@class="pl"]/text()').extract()
            hot = hot[0]

            img_url= eachbook.xpath('td[@valign="top"  and @width]/a[@class="nbg"]/img/@src').extract()
            item['title']=title
            item['title2']=title2
            item['info']=info
            item['rate']=rate
            item['hot']=hot
            item['img_url'] = img_url

            yield item

        nextlink=selector.xpath('//span[@class="next"]/a/@href').extract()
        if nextlink:
            nextlink=nextlink[0]
            yield Request(nextlink,callback=self.parse)


