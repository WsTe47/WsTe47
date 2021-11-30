import pandas as pd
import numpy as np

# 读取excel
df = pd.read_excel('./movie.xlsx')
# print(df.head)
# 行操作
# 查看第一行数据
print(df.iloc[0])
# 查看前五行 iloc[start,end]取start开始到end-1
print(df.iloc[0:5])
# 查看前五行 loc[start:end]取start到end
print(df.loc[0:4])
# 删除名字是Unnamed: 0列
df1 = df.drop('Unnamed: 0', axis=1)
df1 = df1.drop('Unnamed: 0.1', axis=1)
print(df1.head())
# 添加一行
# 名字	投票人数	类型	产地	上映时间	时长	年代	评分	首映地点
dic = {'名字': '大话西游', '投票人数': 350000, '类型': '喜剧', '产地': '中国大陆',
       '上映时间': '1996-10-01 00:00:00', '时长': 116, '年代': 1996, '评分': 9.8, '首映地点': '中国大陆'}
# 一行电影的字典数据构造成Series
s = pd.Series(dic)
print(s)
print(df1.tail(1))
# 设置行标签
s.name = 38730
# 添加一行数据
df1 = df1.append(s)
print(df1.tail(1))
# 删除一行
df1 = df1.drop(38730)
print(df1.tail())
# 列操作
# 查看所有列
print(df1.columns)
# 查看前五行电影名称
print(df1['名字'][:5])
# 查看多列
print(df1[['名字', '类型']][:5])
# 添加一列
df1['序号'] = range(1, len(df) + 1)
# 删除一列
df1 = df1.drop('序号', axis=1)
print(df1)
# 通过标签选择数据
# df.loc[[index][column]]
print(df1.loc[[1, 3, 5, 7, 9], ['名字', '首映地点']])
# 条件选择
# 选择产地是美国的电影
print(df1[df1['产地'] == '美国'])
# 选择产地是美国电影并且评分大于9分
print(df1[(df1['产地'] == '美国') & (df1['评分'] > 9)])
# 选择产地是美国或中国大陆的电影并且评分大于9分
print(df1[((df1['产地'] == '美国') | (df1['产地'] == '中国大陆')) & (df1['评分'] > 9)])
# 缺失值处理
# 查找评分缺失值的数据
print(df1[df1['评分'].isnull()])
# 填充缺失值(平均分)
df1['评分'].fillna(np.mean(df['评分']), inplace=True)
print(df1[df1['评分'].isnull()])
# 删除缺失值
# dataframe存入excel
# df1.to_excel('./movie1.xlsx')
df2 = pd.read_excel('./movie1.xlsx')
print(len(df2))
# 删除有缺失值的行
df2 = df2.dropna()
print(len(df2))
# 异常值处理: 对于异常值,一般数量很少,在影响整理的情况下，直接删除
# 找到时长>1000的数据的行标签,删除对应的行
df2.drop(df2[df2['时长'] > 1000].index, inplace=True)
# 重置索引
df2.index = range(len(df2))
print(df2[df2['投票人数'] < 0])
df2 = df2[df2.投票人数 > 0]
print(df2)
