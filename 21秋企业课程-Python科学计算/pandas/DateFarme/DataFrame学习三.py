import pandas as pd
import numpy as np

#层次化索引
s = pd.Series(np.arange(1,10),index=[['a','a','a','b','b','c','c','d','d'],[1,2,3,1,2,3,1,2,3]])
print(s)
print(s.index)
#取外层索引
print(s['a'])
#取值
print(s['a':'c'])
#取内层,第一个参数是外层，第二个参数是内层
print(s[:,1])
#取值
print(s['a',1])
#转换成dataframe
print(s.unstack())
#DataFrame层次化索引
data = pd.DataFrame(np.arange(12).reshape(4,3),index=[['a','a','b','b'],[1,2,1,2]],columns=[['A','A','B'],['Z','X','C']])
print(data)
#选限列
print(data['A'])
#设置名称
data.index.names = ['row1','row2']
print(data)
data.columns.names= ['col1','col2']
print(data)
#调整顺序
print(data.swaplevel('row2','row1'))

df = pd.read_excel('movie.xlsx')
print(df[:5])
#把产地和年代同时设成索引，产地是外层索引，年代为内层索引
#set_index可以把列变成索引
#reset_index是把索引变成列
df = df.set_index(['产地','年代'])
print(df[:5])
#每一个索引都是一个元组
print(df.index)
#获取所有美国电影，通过行标签选取数据
print(df.loc['美国'])
print(df.loc['中国大陆'])
df = df.swaplevel('产地','年代')
print(df)
print(df.loc[1994])
df = df.reset_index()
print(df)
#数据旋转
data = df[:5]
#行和列交换
print(data.T)
print(data.stack())
