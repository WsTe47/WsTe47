import pandas as pd
import numpy as np

df = pd.read_excel('movie_data.xlsx')
print(df[:5])
# 查看格式
print(df['投票人数'].dtype)
df['投票人数'] = df['投票人数'].astype('int')
print(df[:5])
print(df.info())
# df['年代'] = df['年代'].astype('int')
print(df[df.年代 == '2008\u200e'])
# 查看值
print(df[df.年代 == '2008\u200e']['年代'].values)
# 修改行标签是 15205列是年代的值
df.loc[15205, '年代'] = 2008
df['年代'] = df['年代'].astype('int')
print(df['年代'][:5])
# df['时长'] = df['时长'].astype('int')
print(df[df['时长'] == '8U'])
# 按列名来删除此行
df.drop([31641], inplace=True)
print(df[df['时长'] == '12J'])
df.drop([32946], inplace=True)
df['时长'] = df['时长'].astype('int')
df.info()
# 排序
# 按投票人数进行排序
print(df.sort_values(by='投票人数', ascending=False)[:5])
# 按年代进行排序
print(df.sort_values(by='年代')[:5])
# 多个值排序，先按照评分，再按照投票人数
print(df.sort_values(by=['评分', '投票人数'], ascending=False)[:5])
# 基本统计分析
# describe(0对dataframe中的数值型数据进行描述性统计,可以发现异常值
print(df.describe())
print(df[df['年代'] > 2021])
print('*' * 10)
print(df[df['时长'] > 1000])
# 通过index删除上述记录
df.drop(df[df['年代'] > 2021].index, inplace=True)
print(df[df['年代'] > 2021])
df.drop(df[df['时长'] > 1000].index, inplace=True)
print(df[df['时长'] > 1000])
# 重置index
df.index = range(len(df))
# 最值
print(df['投票人数'].max())
print(df['投票人数'].min())
print(df['评分'].min())
print(df['年代'].min())
# 均值和中值
print(df['投票人数'].mean())
print(df['投票人数'].median())
# 方差和标准差
print(df['评分'].var())
print(df['评分'].std())
# 求和
print(df['投票人数'].sum())
# 相关系统、协方差
# 评分和投票人数是正相关0.122955
print(df[['投票人数', '评分']].corr())
print(df[['投票人数', '评分']].cov())
# 计数
# 一共有多少电影
print(len(df))
# 影片来自多少国家
print(df['产地'].unique())
print(len(df['产地'].unique()))
# 产地中包含一些重的数据,比如美国和USA,德国和西德,俄罗斯和苏联
df['产地'].replace('USA', '美国', inplace=True)
print(df['产地'].unique())
df['产地'].replace(['西德', '苏联', '中国'], ['德国', '俄罗斯', '中国大陆'], inplace=True)
print(df['产地'].unique())
print(len(df['产地'].unique()))
# 电影来自多少年份
print(len(df['年代'].unique()))
# 计算每一年的电影数量 value_counts:按值计数: 每个值出现的次数
print(df['年代'].value_counts())
# 电影产出前5的国家
print(df['产地'].value_counts()[:5])
# 保存数据
df.to_excel('movie.xlsx')
# 透视图:pandas提拱了一个pivot_table
# 基础形式
# 1.默认对索引进行均值计算，这里对每个年份进行分类，对各个数值型变量计算均值
print(pd.pivot_table(df, index=['年代']))
# 也可以有多个索引
pd.set_option('max_columns', 100)
pd.set_option('max_rows', 5000)
print(pd.pivot_table(df, index=['年代', '产地']))
# 也可以指定需要统计的汇总的数据
print(pd.pivot_table(df, index=['年代', '产地'], values=['评分']))
# 也可以指定函数，来统计不同的统计值
print(pd.pivot_table(df, index=['年代', '产地'], values=['投票人数'], aggfunc=np.sum))
# 通过将投票人数和评分进行对应分组，对产地实现数据聚合和总结
print(pd.pivot_table(df, index=['产地'], values=['投票人数', '评分'], aggfunc=[np.sum, np.mean]))
# 排数值(NaN)难以处理，如果想移除它们，可以使用fill_value,这里会把非数值替换为0,margins显示总和数据
print(pd.pivot_table(df, index=['产地'], aggfunc=[np.sum, np.mean], fill_value=0, margins=True))
# 对不同值执行不同的函数,可以向aggfunc传递一个字典
print(pd.pivot_table(df, index=['产地'], values=['投票人数', '评分'], aggfunc={'投票人数': np.sum, '评分': np.mean}, fill_value=0,
                     margins=True))
# 对各个的年份的投票人数求和，对评分求均值
print(pd.pivot_table(df, index=['年代'], values=['投票人数', '评分'], aggfunc={'投票人数': np.sum, '评分': np.mean}, fill_value=0,
                     margins=True))
# 透视表过滤
table = pd.pivot_table(df, index=['年代'], values=['投票人数', '评分'], aggfunc={'投票人数': np.sum, '评分': np.mean}, fill_value=0)
print(type(table))
print(table[:5])
# 查看1994年平均评分
print(table[table.index == 1994])
# 查看评分
print(table.sort_values(by='评分', ascending=False)[:10])
# 多个索引汇总
