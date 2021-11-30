import numpy as np
import pandas as pd

# 读取数据
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 300)
df = pd.read_excel('./香港酒店数据1.xlsx')
df = df.drop('Unnamed: 0', axis=1)
print(df)

# 查看评分的格式
print('*' * 30, '查看评分的格式', '*' * 30)
print(df['评分'].dtype)
# df['评分']=df['评分'].astype(int)
# print(df['评分'].dtype)

# 降序排序
print('*' * 30, '降序排序', '*' * 30)
print(df.sort_values(by='评分', ascending=False))

# 升序排序
print('*' * 30, '升序排序', '*' * 30)
print(df.sort_values(by='评分', ascending=True))

# 价格排名
print('*' * 30, '价格排名', '*' * 30)
print(df.sort_values(by='价格', ascending=False))

# 地区均价  (两种表示，第二种时候一定一定记得mean后加（）
print('*' * 30, '地区均价', '*' * 30)
print(np.mean(df['价格'].iloc[df[df.地区 == '油尖旺'].index]))
print(df['价格'].iloc[df[df.地区 == '油尖旺'].index].mean())

# 描述性统计
print('*' * 30, '描述性统计', '*' * 30)
print(df.describe())

# 求所有价格的均值方差，最大最小值，中值
# print(np.mean(df['价格']))
print()
print('*' * 30, '求所有价格的均值方差，最大最小值，中值', '*' * 30)

print('0平均值：', df['价格'].mean())
print('G方差：', df['价格'].var())
print('H最大值：', df['价格'].max())
print('D最小值：', df['价格'].min())
print('0中值：', df['价格'].median())

# 计算评分和价格之间的的相关系数，协方差
print('*' * 30, '关系系数', '*' * 30)
print(df[['评分', '价格']].corr())
print()
print('*' * 30, '协方差', '*' * 30)
print(df[['评分', '价格']].cov())

# 按照评分降序排序，评分相同时按价格升序排序
print(df.sort_values(by=['评分', '价格'], ascending=[False, True]))

# 计算出，评分小于3分的酒店数量和占比
print('*' * 30, '评分小于3分的酒店数量', '*' * 30)
print(len(df[df['评分'] < 3]))

print('*' * 30, '评分小于3分的酒店占比', '*' * 30)
print(len(df[df['评分'] < 3]) / len(df['评分']) * 100, '%')

# 统计出酒店评分大于等于4分的酒店的价格均值
print('*' * 30, '评分大于等于4分的酒店的价格均值', '*' * 30)
print(df['价格'].iloc[df[df.评分 >= 4].index].mean())
print(np.mean(df['价格'].iloc[df[df['评分'] >= 4].index]))

# 计算出每个地区的酒店占总酒店数量的比例
print('*' * 30, '每个地区的酒店占总酒店数量的比例', '*' * 30)
area = (df['地区'].drop_duplicates())
for i in area:
    print(i, ':', end=' ')
    print(len(df[df['地区'] == i]) / len(df['地区']) * 100, '%')

# 找出酒店评分人数排名前20的酒店，并计算他们的价格均值
aa = df.sort_values(by='评分人数', ascending=False)[:20]
print('*' * 30, '找出酒店评分人数排名前20的酒店', '*' * 30)
print(aa['名字'])
print('*' * 30, '计算他们的价格均值', '*' * 30)
print(aa['价格'].mean())

# 查看酒店分布的类型数量和地区数量
print('酒店分布的类型数量为Ghd：')
print(len(df['类型'].value_counts()))
print('酒店分布的地区数量为Ghd：')
print(len(df['地区'].value_counts()))
# 统计各个类型和地区包含的酒店数量
print('各个地区包含的酒店数量：')
print(df['类型'].value_counts())
print('各个类型包含的酒店数量：')
print(df['地区'].value_counts())
