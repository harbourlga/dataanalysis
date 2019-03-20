#coding:utf-8

import sys

import requests
from lxml import etree

reload(sys)
sys.setdefaultencoding('utf-8')


url = r'http://invest.ppdai.com/loan/info?id=98606313'
headers = {
	"Host":"invest.ppdai.com",
	"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
	"Referer": "http://invest.ppdai.com/loan/listnew"
}

html = etree.HTML(requests.get(url=url, headers=headers).content)

detail_group = html.xpath("//div[@class='newLendDetailbox']")
title = detail_group[0].xpath("h3/span")
author = detail_group[0].xpath("//span[@class='username']")

detail_money_group = detail_group[0].xpath("//div[@class='newLendDetailMoneyLeft']")
amount = detail_money_group[0].xpath("dl[1]/dd/em")
rate = detail_money_group[0].xpath("dl[2]/dd")
period = detail_money_group[0].xpath("dl[3]/dd")

detail_refund_group = detail_group[0].xpath("//div[@class='newLendDetailRefundLeft']//div[@class='item w260']")
repayment = detail_refund_group[0]
complement = detail_refund_group[1].xpath("span")

response_group = html.xpath("//div[@class='scroll-area']/ol")
time = response_group[0].xpath("li[5]")[0].text
begin_time = response_group[-1].xpath("li[5]")[0].text

print title[0].text
print author[0].text
print amount[0].tail
print rate[0].text
print "".join(period[0].itertext())
print repayment.text.strip()
print complement[0].tail.strip().strip("%")
print time
print begin_time

for each_ol in response_group:
	username = each_ol.xpath("li/span[@class='listname']")[0].text
	user_rate = each_ol.xpath("li[2]")[0].text.strip("%")
	user_amount = each_ol.xpath("li[4]")[0].text.strip("&#165;")
	user_time = each_ol.xpath("li[5]")[0].text

	print '{username=%s|rate=%s|postmoney=%s|money=%s|postdate=%s|status=全部通过}' %(
		   username, user_rate, user_amount, user_amount, user_time)



















