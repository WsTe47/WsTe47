import pandas as pd

pd.set_option('max_columns', 10)
df = pd.read_json('data.json')
print(df['student'])

# 把学生数据封装成list
list = []
for i in df['student']:
    print(i)
    list.append(i)

# 使用list生成dataframe
data = pd.DataFrame(list)
print(data)
print(data.info())
print(data.describe())
# 去重
data.drop_duplicates(inplace=True)
print(data)
# 查找缺失值数量
print(data.isnull().sum())
data['education'] = data['education'].fillna('高中')
print(data.isnull().sum())
data['profession'] = data['profession'].fillna('非计算机专业')
print(data.isnull().sum())
data.to_excel('data.xlsx', index=False)
