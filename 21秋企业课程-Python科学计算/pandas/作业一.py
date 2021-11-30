"""
（1）用字典数据类型创建DataFrame。 data={'state':['a','b','c','d'], 'year':[1991,1992,1993,1994], 'pop':[6,7,8,9]}
（2）将创建的Dataframe的索引设置为，ABCD。并且命名为“索引”。
（3）在下面新增一行。然后删除。
（4）增加新的属性列，列名设置为‘port’，值均为1。
（5）取出1991和1994年的数据。
（6）获取列‘state’和‘year’的数据。
（7）查看每一列数据的数据格式，并且将‘pop’每个数据乘2。
"""
import pandas as pd
import numpy as np

# （1）用字典数据类型创建DataFrame。 data={'state':['a','b','c','d'], 'year':[1991,1992,1993,1994], 'pop':[6,7,8,9]}
data = {'state': ['a', 'b', 'c', 'd'], 'year': [1991, 1992, 1993, 1994], 'pop': [6, 7, 8, 9]}
df = pd.DataFrame(data)

# （2）将创建的Dataframe的索引设置为，ABCD。并且命名为“索引”。
df.index = (['A', 'B', 'C', 'D'])
df.index.name = "索引"
print(df)
print(df.tail(2))

# （3）在下面新增一行。然后删除。
data1 = {'state': ['Guo'], 'year': ['Hai'], 'pop': ['Dong']}
df = df.append(data1, ignore_index=True)
df.index = (['A', 'B', 'C', 'D', 'E'])
print(df.tail(2))
df = df.drop('E')
print(df.tail(2))

# （4）增加新的属性列，列名设置为‘port’，值均为1。
df['port'] = 1
print(df)

# （5）取出1991和1994年的数据。
print(df[(df['year'] == 1991) | (df['year'] == 1994)])

# （6）获取列‘state’和‘year’的数据。
print(df[['state', 'year']])

# （7）查看每一列数据的数据格式，并且将‘pop’每个数据乘2。
print(df.dtypes)
print(df['pop'])
df['pop']=df['pop']*2
print(df['pop'])

