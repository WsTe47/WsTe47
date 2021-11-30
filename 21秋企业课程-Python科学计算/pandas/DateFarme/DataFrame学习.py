import pandas as pd
import numpy as np

df = pd.read_excel(r'豆瓣电影数据.xlsx')
print(df.head())
# 行操作
# 查看第一行的数据
print(df.iloc[0])
# 查看前五行的数据:左开右闭
print(df.iloc[0:5])
# loc[start:end] end也包含也内
print(df.loc[0:5])
print(df.tail(1))
# 添加一行
dit = {'名字': '唐伯虎点秋香', '投票人数': 34000, '类型': '喜剧', '产地': '中国', '上映时间': '1998-12-11 00:00:00', '时长': 112, '年代': 1998,
       '评分': 9.6, '首映地点': '中国'}
s = pd.Series(dit)
# 指定索引名称
s.name = 38738
print(s)
# 添加数据
df = df.append(s)
# 查看最后5行
print(df[-5:])
# 删除一行
df = df.drop(38738)
print(df[-5:])
# 列操作
# 查看所有的列
print(df.columns)
# 查看前五行的名字数据
print(df['名字'][:5])
# 查看多列
print(df[['名字', '类型']][:5])
# 增加一列
df['序号'] = range(1, len(df) + 1)
print(df.head())
# 删除一列
df = df.drop('序号', axis=1)
print(df)
# 通过标签选择数据
# df.loc[[index],[column]]
print(df.loc[1, '名字'])
print(df.loc[[1, 3, 5, 7, 9], ['名字', '评分']])
# 条件选择
# 选取产地为美国的所有电影
print(df[df['产地'] == '美国'].head())
# 选取产地为美国的所有电影,并且评分地对地导弹于9
print(df[(df['产地'] == '美国') & (df.评分 > 9)].head())
# 选取产地是美国或中国大陆所有电影,并且评分大于9
print(df[((df.产地 == '美国') | (df.产地 == '中国大陆')) & (df.评分 > 9)])
# 缺失值及异常处理
# 判断缺失值
print(df[df['名字'].isnull()][:10])
dit = {'名字': '唐伯虎点秋香', '投票人数': 34000, '类型': '喜剧', '产地': '中国', '上映时间': '1998-12-11 00:00:00', '时长': 112, '年代': 1998,
       '评分': np.nan, '首映地点': '中国'}
s = pd.Series(dit)
# 指定索引名称
s.name = 38738
print(s)
# 添加数据
df = df.append(s)
# 填充缺失值
print(df[df['评分'].isnull()])
df['评分'].fillna(np.mean(df['评分']), inplace=True)
print(df[['名字', '评分']][-5:])
# 填充所有缺失值
df1 = df.fillna('未知电影')
print(df1)
# 删除缺失值
# how=all 删除全为空值的行或列
# inplace=True: 覆盖之前的数据
# axis=0或1,删除行或列
print(len(df))
df1 = df.dropna()
print(len(df1))
# 处理异常值: 对于异常值,一般来说数量都会很少，在不影响整 体数据分布的情况下，我们直接删除就可以
print(df[df.投票人数 < 0])
df = df[df.投票人数 > 0]
print(df)

df.to_excel('./movie_data.xlsx')

