#__*_ encoding: utf-8 --*-

import numpy as np
import pandas as pd


# series组成的字典形式创建
data = {'one':pd.Series([1.,2.,3.],index=['a','b','c']),
        'two':pd.Series([1.,2.,3.,4.],index=['a','b','c','d'])}

df=pd.DataFrame(data)
print(df)

# # 访问行索引
# print(df.index)
# # 访问列索引
# print(df.columns)
# # 访问值
# print(df.values)


# # 访问列
# print(df['one'])
#
# print(df.one)
# # 访问行
# print(df[0:1])

# # 访问所有的行，one和two列  （第一个行标签，第二个列标签）
# print(df.loc[:,['one','two']])
#
# print(df.loc['a',['one','two']])


# # 访问前两行，第一列
# print(df.iloc[0:2,0:1])

# 第一个是行标签，第二个是列标签  ix已经不推荐使用
print(df.ix['a',[0,1]])
print(df.ix[['a','b'],[0,1]])
