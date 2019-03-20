#test PyV8


# import random
import PyV8

# ctxt = PyV8.JSContext()
# ctxt.enter()
# func = ctxt.eval("""
#     (function(){
#         function hello(){
#             return "Hello world.";
#         }
#         return hello();
#     })
# """)
# print func()


def test_create_vl5x(param):
    ctxt = PyV8.JSContext()
    ctxt.enter()
    js_file = open('E:\lga\dataanalysis\draft\getKey.js', 'r')
    js_data = js_file.read()
    js_file.close()
    ctxt.eval(js_data.decode('GBK', 'ignore'))
    create_key = ctxt.locals.getKey
    key1 = create_key(param)
    return key1

vjkl5 = 'ee12b046a9bff0eb73e01ed1887f270879a86298'
print(test_create_vl5x(	vjkl5))




import uuid
guid = uuid.uuid4()
# print('guid:{}'.format(str(guid)))

import requests
param = {'guid':str(guid)}
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'}
r1 = requests.post('http://wenshu.court.gov.cn/ValiCode/GetCode', data=param, headers=headers)
print(r1.text)


url = 'http://wenshu.court.gov.cn/list/list/?sorttype=1&number=A344PWJH&guid=59c9589f-b085-3f92aacf-c083810a07ba'


import scrapy
from scrapy.http import Request,FormRequest

# class Request_cookies(Request):
#     def start(self, url):


