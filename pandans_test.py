#!/usr/bin/env python
#__*_ encoding: utf-8 --*-
#author tachai

import numpy as np
import pandas as pd


s= pd.Series([-1.5599,-1.34534,-1.4442,-1.9837],index=["a","b","c","d"])

# print(s.values)
# print(s.index)
# print(s[['a','b']])
print(s[:2])

# df = pd.DataFrame({'one':[1,2,3,4],'two':[1.,2.,3.,4.]})
# print(df)
# 以嵌套列形式创建
# df = pd.DataFrame([[1,2,3,5],[1.,2.,3.,4.]],index=['a','b'],columns=['one','two','three','four'])
# print(df)


# 二维ndarray创建
# data=np.zeros((2,),dtype=[('A','i4'),('B','f4'),('C','a10')])
# print(data)
#
# df=pd.DataFrame(data)
# print(df)

data ={'one':pd.Series([1.,2.,3.],index=['a','b','c']),'two':pd.Series([1.,2.,3.,4.],index=['a','b','c','d'])}

df = pd.DataFrame(data,index=['d','b','a'],columns=['two','one'])
print(df)