# -*- coding: utf-8 -*-
import sys

from lxml import etree

import scrapy
from scrapy.http import Request
from paipaidai.items import PaipaidaiItem

reload(sys)
sys.setdefaultencoding('utf-8')


class FirstSpider(scrapy.Spider):
    name = 'first'
    allowed_domains = ['ppdai.com']
    url = r'http://invest.ppdai.com/loan/info?id={}'

    def start_requests(self):
        for i in xrange(98606313, 98606314):
            yield Request(url=self.url.format(i),
                          callback=self.parse, meta={'id': i})

    def parse(self, response):
        meta = response.meta
        html = etree.HTML(response.text)

        detail_group = html.xpath("//div[@class='newLendDetailbox']")
        title = detail_group[0].xpath("h3/span")
        author = detail_group[0].xpath("//span[@class='username']")

        detail_money_group = detail_group[0].xpath(
            "//div[@class='newLendDetailMoneyLeft']")
        amount = detail_money_group[0].xpath("dl[1]/dd/em")
        rate = detail_money_group[0].xpath("dl[2]/dd")
        period = detail_money_group[0].xpath("dl[3]/dd")

        detail_refund_group = detail_group[0].xpath(
            "//div[@class='newLendDetailRefundLeft']//div[@class='item w260']"
        )
        repayment = detail_refund_group[0]
        complement = detail_refund_group[1].xpath("span")
        response_group = html.xpath("//div[@class='scroll-area']/ol")
        time = response_group[0].xpath("li[5]")[0].text
        begin_time = response_group[-1].xpath("li[5]")[0].text

        item = PaipaidaiItem() 
        item['title'] = title[0].text
        item['author'] = author[0].text
        item['amount'] = amount[0].tail
        item['rate'] = rate[0].text
        item['period'] = "".join(
            map(lambda x: x.strip(), period[0].itertext()))
        item['repayment'] = repayment.text.strip()
        item['complement'] = complement[0].tail.strip().strip("%")
        item['webid'] = meta['id']
        item['begin_time'] = begin_time
        item['time'] = time
        item['response'] = []

        for each_ol in response_group:
            username = each_ol.xpath("li/span[@class='listname']")[0].text
            user_rate = each_ol.xpath("li[2]")[0].text.strip("%")
            user_amount = each_ol.xpath("li[4]")[0].text.strip("&#165;")
            user_time = each_ol.xpath("li[5]")[0].text

            item['response'].append(
                '{username=%s|rate=%s|postmoney=%s|money=%s|postdate=%s|status=全部通过}' % (
                    username, user_rate, user_amount, user_amount, user_time
                ))

        yield item
