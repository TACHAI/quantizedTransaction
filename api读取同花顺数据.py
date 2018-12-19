#__*_ encoding: utf-8 --*-

import os
import numpy as np
import pandas as pd
import pandas_datareader.data as web
import datetime

''' pd.read_csv test '''
# # ss(上海证券) sz(深圳证券)
# df_csvave = web.DataReader('601233.ss',"yahoo",datetime.datetime(2018,1,1))
# print(df_csvave)
# print(df_csvave.index)
# print(df_csvave.columns)
#
# # 存数据
# path=os.getcwd()
# df_csvave.to_csv(path+'/yahoo.csv',columns=df_csvave.columns,index=True)

# 读数据
path=os.getcwd()
df_csvload=pd.read_csv(path+'/yahoo.csv',parse_dates=True,index_col=0,encoding='gb2312')

# 股票数据内容概况查看：head(),tail(),shape,describe(),info()
# 前3行
print(df_csvload.head(3))
# 倒数3行
print(df_csvload.tail(3))


print(df_csvload.index)
print(df_csvload.columns)

print(df_csvload.shape)
print(df_csvload.describe())
print(df_csvload.info())

# 缺失值处理方法：isnull(),notnull(),dropna(),fillna()

print(df_csvload.isnull())
print(df_csvload[df_csvload.isnull().T.any()])

# 数据精度处理：round(),astype(),applymap(),lambda()
# '%0.2f%'x  (保留2位小数浮点型)
df_csvload=df_csvload.applymap(lambda x:'%0.2f'%x)
df_csvload.Volume=df_csvload.loc[:,['Volume']].apply(lambda x:'%0.0f'%x,axis=1)

df_csvload.Volume=df_csvload.Volume.astype(int)
print(df_csvload.head(4))

