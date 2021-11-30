import pandas as pd
import numpy as np

df = pd.read_excel('./movie.xlsx')
print(df.head())
# 删除名字是Unnamed: 0列
df = df.drop('Unnamed: 0', axis=1)
df = df.drop('Unnamed: 0.1', axis=1)
print(df.info())
# 数据类型转换
df['年代'] = df['年代'].astype(np.int64)
# 排序
# 按投票人数排序
print(df.sort_values(by='投票人数', ascending=False)[:10])
# 取出年代最早的五部电影
print(df.sort_values(by='年代')[:5])
# 按多个值排序,先按评分再按投票人数
print(df.sort_values(by=['评分', '投票人数'], ascending=False)[:10])
# 基本统计分析
print(df.describe())
print(len(df[df['年代'] > 2010]))
print('*' * 30)
print(df[df['时长'] > 300])
# 最值
print(df['投票人数'].max())
print(df['投票人数'].min())
print(df['评分'].min())
print(df['年代'].min())
# 均值和中值
print(df['投票人数'].mean())
print(df['投票人数'].median())
# 求和
print(df['投票人数'].sum())
# 相关系数
print(df[['投票人数', '评分']].corr())
# 协方差
print(df[['投票人数', '评分']].cov)
# 计数
# 一共有多少电影
print(len(df))
# 影片来自多少国家
print(df['产地'].unique())
# df['产地'].replace(['中国大陆','中国香港','中国台湾'],['中国','中国','中国'],inplace=True)
df['产地'].replace('中国', '中国大陆', inplace=True)
print(df['产地'].unique())
# 电影来自哪些年份
print(df['年代'].unique())
# 计算每一年的电影数量 value_counts: 按值计数,每个值出现的次数
print(df['年代'].value_counts())
# 电影出产前5的国家
print(df['产地'].value_counts()[:5])
df.to_excel('./movie2.xlsx', index=False)
