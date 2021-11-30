import pandas as pd
import numpy as np

pd.set_option('max_columns', 10)
df = pd.read_json('./data.json')
# print(df['student'])
data = []
for i in df['student']:
    # print(i)
    data.append(i)
print(data)
print('*' * 30)
# 通过列表生成dataframe
df1 = pd.DataFrame(data)
print(df1)
print(df1.info())
print(df1.describe())
# 去重
df1.drop_duplicates(inplace=True)
print('*' * 30)
print(df1.isnull().sum())
# 填充缺失值
df1['education'] = df1['education'].fillna('小学')
df1['profession'] = df1['profession'].fillna('非计算机专业')
print(df1.isnull().sum())
df1['salary'] = df1['salary'].astype(np.int64)
df1.to_excel('data.xlsx', index=False)
# 画就业薪水直方图
# 每个城市就业数量柱状图
