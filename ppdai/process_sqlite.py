# coding:utf-8

import json
import sys
import re

import redis
from get_max_id import set_max, SqliteClass

reload(sys)
sys.setdefaultencoding('utf-8')

RONGJINSUO = {
    'sqlite': {
        'path': r'C:\Users\Heweitao\Desktop\rongjinsuo\SpiderResult1.db3',
    },
    'redis': {
        'host': 'localhost',
        'port': '6379',
        'db': '1',
    }
}

PPDAI = {
    'sqlite': {
        'path': r'C:\Users\Administrator\Desktop\ppdai\SpiderResult1.db3',
    },
    'redis': {
        'host': 'localhost',
        'port': '6379',
        'db': '0',
    }
}


class SavingInDisk(object):

    def __init__(self, parms):
        self.redis_parms = parms['redis']
        self.sqlite_parms = parms['sqlite']

    def connect(self):
        self.rediscli = redis.StrictRedis(
            host=self.redis_parms['host'],
            port=self.redis_parms['port'],
            db=self.redis_parms['db']
        )
        self.row = SqliteClass(self.sqlite_parms['path'])

    def saving(self):
        key = self.rediscli.keys("*items")
        while True:
            try:
                source, data = self.rediscli.blpop(key, timeout=5)
            except TypeError:
                print "done."
                break

            self.save_in_row(data)
            self.row.insert()
            self.row.save()
            print 'process complete:', self.row["网址"]

        self.row.close()
        self.rediscli.flushdb()
        set_max(self.sqlite_parms['path'], self.redis_parms)

    def save_in_row(self, data):
        item = json.loads(data)
        self.row["标题"] = item['title']
        self.row['作者'] = item.get('author')
        self.row["时间"] = item['time']
        self.row["编号"] = item['webid']
        self.row["借款金额"] = item['amount']
        self.row["年利率"] = item['rate']
        self.row["借款期限"] = item['period']
        self.row["发标时间"] = item['begin_time']
        self.row["还款方式"] = item['repayment']
        self.row["回复内容"] = item['response']
        self.row["完成度"] = item['complement']
        self.row['类型图片'] = item['image']
        self.row['采集时间'] = item['crawled']
        self.row["网站编号"] = 297
        self.row["已发"] = 0
        self.row["已采"] = 1
        self.row["网址"] = r'https://www.rjs.com/invest/{}.html'.format(item['webid'])


def process(database):
    test = SavingInDisk(database)
    test.connect()
    test.saving()


if __name__ == "__main__":
    process(RONGJINSUO)
