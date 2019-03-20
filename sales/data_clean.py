import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pylab as plt
from pandas import Series, DataFrame

train = pd.read_csv('E:\lga\\time\sales_train_v2.csv', encoding='utf-8')
df_items = pd.read_csv('E:\lga\\time\items.csv', encoding='utf-8')
train_1 = pd.merge(train ,df_items ,how='left')
train_1.set_index(["shop_id"], inplace=True)
for i in range(0,60):
    df_x = train_1.loc[i,:]
    df_x.to_csv('E:\\lga\\time\\shop\\shop_{shop_id}.csv'.format(shop_id=i), encoding='utf-8')
    print('succeed')


#对第一家商店进行分析
shop_0 = pd.read_csv("E:\lga\\time\\shop\shop_0.csv", encoding='utf-8')
shop_0.head()
del shop_0['item_name'] #删除一列
shop_0.describe()
group1 = shop_0.groupby('item_cnt_day')
group1.size() #求出item_cnt_day的分布情况
group2 = shop_0.groupby(['item_cnt_day','item_category_id'])
group2.size()


#对每个商店2年内每月内的每日总销量进行可视化展示
shop_0_series = shop_0.loc[:,['date','item_cnt_day']]
shop_0_series.index = shop_0_series['date']
del shop_0_series['date']
shop_0_series.index = pd.to_datetime(shop_0_series.index, format='%d.%m.%Y')
shop_0_series['item_cnt_day'] = shop_0_series['item_cnt_day'].astype(int) #将item_cnt_day转换为整数类型
group3 = shop_0_series.groupby(shop_0_series.index)
timelist = group3.size()
timelist = list(timelist.index) #将时间段放入列表
timelist_0 = []
for x in range(0, len(timelist)):
    str_1 = str(timelist[x])[0:10]
    timelist_0.append(str_1)
    print('succeed') #将timelist内每一项的时间类型转换为str

def shop_item_cnt_sum(timelist, shop):
    #组成一个新的df,shop必须为一列item_cnt_day其index为date
    df = DataFrame(columns=('date', 'item_cnt_day'))

    for i in timelist:
       A = sum(shop[i]['item_cnt_day'])
       row = DataFrame({'date':[i], 'item_cnt_day':[A]})
       df = df.append(row, ignore_index=True)

    df.index = df['date']
    df.index = pd.to_datetime(df.index, format='%Y-%m-%d')
    return df


#取出所有的shop,对每个shop求sum最后做成一张折线表
for i in range(0,60):
    shop_series = pd.read_csv("E:\lga\\time\\shop\shop_{0}.csv".format(i), encoding='utf-8')
    del shop_series['item_name']
    shop_series = shop_series.loc[:, ['date', 'item_cnt_day']]
    shop_series.index = shop_series['date']
    del shop_series['date']
    shop_series.index = pd.to_datetime(shop_series.index, format='%d.%m.%Y')
    A = shop_item_cnt_sum(timelist_0, shop_series)
    A['item_cnt_day'].plot()
plt.show()


#对训练集内的总成交量按月进行汇总
train = pd.read_csv('E:\lga\\time\sales_train_v2.csv', encoding='utf-8')
train_0 = train.loc[:,['date_block_num','item_cnt_day']]
train_0.index = train_0['date_block_num']
def shop_item_cnt_sum(train_0):
    #组成一个新的df,shop必须为一列item_cnt_day其index为date
    df = DataFrame(columns=('date_block_num_all', 'item_cnt_day'))
    for i in range(0,34):
         A =sum(train_0[train_0.loc[:,'date_block_num']==i]['item_cnt_day'])
         row = DataFrame({'date_block_num_all': [i], 'item_cnt_day': [A]})
         df = df.append(row, ignore_index=True)
    return df

train_0_0 = shop_item_cnt_sum(train_0)
train_0_0.index = train_0_0['date_block_num_all']
del train_0_0['date_block_num_all']
train_0_0['item_cnt_day'].plot()



