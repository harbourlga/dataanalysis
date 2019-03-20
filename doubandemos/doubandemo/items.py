# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

# from scrapy import Item,Field
import scrapy



class DoubanBookItem(scrapy.Item):
    title = scrapy.Field()
    title2=scrapy.Field()
    info=scrapy.Field()
    rate =scrapy.Field()
    hot = scrapy.Field()
    img_url = scrapy.Field()
    images = scrapy.Field()


