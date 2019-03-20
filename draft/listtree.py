# -*- coding: utf-8 -*-
import uuid
import requests
import tools
import json
headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Connection': 'keep-alive',
    'Host': 'wenshu.court.gov.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; W…) Gecko/20100101 Firefox/57.0',
}

response = requests.get('http://wenshu.court.gov.cn/list/list/?sorttype=1&number=A344PWJH&guid=59c9589f-b085-3f92aacf-c083810a07ba', headers=headers)
print(response.cookies)
Cookies = response.cookies
# cookie_str = Cookies[0]
vjkl5 = str(Cookies).split('vjkl5=')[1]
vjkl5 = vjkl5.split(' ')[0]
print(vjkl5)
vl5x = tools.create_vl5x(vjkl5)
print(vl5x)
print(str(vl5x))
headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Connection': 'keep-alive',
    'Host': 'wenshu.court.gov.cn',
    'Referer':'http://wenshu.court.gov.cn/list/list/?sorttype=1&number=&guid=986d0259-c1e9-44ea9824-2b3b9fbead4b&conditions=searchWord+QWJS+++%E5%85%A8%E6%96%87%E6%A3%80%E7%B4%A2:%E6%B7%B1%E5%9C%B3%20%E9%95%BF%E6%98%A5%E9%95%BF%E7%94%9F',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Length': '222',
    'Cache-Control': 'max-age=0',
    'Cookie':str('_gscu_125736681=23411255r26gs182; Hm_lvt_9e03c161142422698f5b0d82bf699727=1530776352; _gscu_2116842793=234111808ot84931; Hm_lvt_3f1a54c5a86d62407544d433f6418ef5=1530776414; Hm_lvt_d2caefee2de09b8a6ea438d74fd98db2=1532081595,1532306860,1532337560,1532505883; XDEBUG_SESSION=XDEBUG_ECLIPSE; _gscbrs_2116842793=1; Hm_lpvt_d2caefee2de09b8a6ea438d74fd98db2=1532511246; vjkl5='+vjkl5),
}
guid = uuid.uuid4()
print(guid)
print(str(tools.create_number(guid)))
post_data = {'Param': '全文检索:深圳',
             'Index': 50,
             'Page': 5,
             'Order': '法院层级',
             'Direction': 'asc',
             'vl5x': str(vl5x),
             'number': str(tools.create_number(guid)),
             'guid': guid,
             }
r = requests.post('http://wenshu.court.gov.cn/List/ListContent', data = post_data, headers=headers)
print(r.text)
response_next = r.content
print(response_next)
print(type(response_next))
response_next=r.json()
print(response_next)
print(type(response_next))
print(response_next[0])
response_next = json.loads(response_next)
print(type(response_next[1]))
print(response_next[1][u'\u6848\u4ef6\u540d\u79f0'])