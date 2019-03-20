#coding:utf-8

import sqlite3
import redis

from items import SqliteClass


DATABASE = r'C:\Users\Administrator\Desktop\ppdai\SpiderResult1.db3'
RDATABASE = {'host':'192.168.1.7', 'port':6379, 'db':0}


class Redis(object):
    def __init__(self, host, port, db):
        try:
            self.r = redis.StrictRedis(host=host, port=port, db=db)
        except Exception, e:
            print e.message

    def _set(self, key, value):
        self.r.set(key, value)

    def _get(self, key):
        return self.r.get(key)

    def __setitem__(self, key, value):
        self._set(key, value)

    def __getitem__(self, key):
        return self._get(key)

def get_redis(r):
    return Redis(r['host'], r['port'], r['db'])


def set_max(database, rdb):
    db = SqliteClass(database)
    max_id = db.select(field='max(编号)').fetchall()[0][0]
    rdb['max'] = int(max_id)
    db.close()


def get_max(rdb):
    return rdb['max']


def set():
    r = get_redis(RDATABASE)
    set_max(DATABASE, r)

def get():
    r = get_redis(RDATABASE)
    return r['max']

if __name__ == "__main__":
    set()
    print get()
