#coding:utf-8

import sqlite3
import redis


DATABASE = r'C:\Users\Administrator\Desktop\ppdai\SpiderResult1.db3'
RDATABASE = {'host':'192.168.1.7', 'port':6379, 'db':0}


class SqliteClass(object):
    def __init__(self, database):
        self.conn = sqlite3.connect(database)
        self.cur = self.conn.cursor()
        table_info = self.cur.execute('PRAGMA table_info(Content)').fetchall()

        self.col_name = {}
        for col in table_info:
        	self.col_name[col[1]] = ""

        del self.col_name["ID"]

        self.place_holder = ",".join(['?' for i in range(len(self.col_name))])

    def __getitem__(self, key):
        return self.col_name[key.decode('utf-8')]

    def __setitem__(self, key, value):
        self.col_name[key.decode('utf-8')] = value

    def insert(self, table="Content"):
        keys = ",".join(self.col_name.keys())
        values = map(unicode, self.col_name.values())
        sql = "INSERT INTO {0} ({1}) VALUES ({2})".format(table, keys, self.place_holder)
        self.cur.execute(sql, values)

    def select(self, field="*", where="", table="Content"):
        if where:
            sql = "SELECT {0} FROM {1} WHERE {2}".format(field, table, where)
        else:
            sql = "SELECT {0} FROM {1}".format(field, table)

        return self.cur.execute(sql)

    def save(self):
        self.conn.commit()

    def close(self):
        self.cur.close()
        self.conn.close()


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
    path = r'C:\Users\Heweitao\Desktop\rongjinsuo\SpiderResult1.db3'
    SqliteClass(path)