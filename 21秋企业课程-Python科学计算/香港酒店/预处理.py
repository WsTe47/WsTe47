import pandas as pd
import numpy as np

df = pd.read_excel('./香港酒店数据.xlsx')
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 300)
print(df)
# 读取香港酒店数据,按照数据的内容，重新设置数据的索引，重新设置列名称
df = df.drop(1, axis=0)
df.reset_index(drop=True)
df = df.drop('Unnamed: 0', axis=1)
df.columns = '名字', '类型', '城市', '地区', '地点', '评分', '评分人数', '价格'
print('*' * 55, '读取香港酒店数据,按照数据的内容，重新设置数据的索引，重新设置列名称', '*' * 55)
print(df)

# 查找出所有类型为“休闲度假”并且在湾仔地区的酒店
print('*' * 55, '查找出所有类型为“休闲度假”并且在湾仔地区的酒店', '*' * 55)
print(df[(df['类型'] == '休闲度假') & (df['地区'] == '湾仔')])

# 查找出所有地址在观塘或者油尖旺，评分大于4的酒店
print('*' * 55, '查找出所有地址在观塘或者油尖旺，评分大于4的酒店', '*' * 55)
print(df[((df['地区'] == '油尖旺') | (df['地区'] == '观塘')) & (df['评分'] > 4)])
# 用“其他”填充类型和地区,用评分均值填充评分缺失值,删除价格和评分人数的缺失值

# 用“其他”填充类型和地区
df['类型'].fillna('其他', inplace=True)
df['地区'].fillna('其他', inplace=True)

# 用评分均值填充评分缺失值
df['评分'].fillna(np.mean(df['评分']), inplace=True)

# 删除价格和评分人数的缺失值
df = df.dropna(subset=['价格', '评分人数'])

# 做到第二题倒数第二问，排前20酒店时候发现出现了重复。重审题没有发现之前有去重要求，但还是加上了。
df = df.drop_duplicates(['名字'])

df.to_excel('香港酒店数据1.xlsx')
