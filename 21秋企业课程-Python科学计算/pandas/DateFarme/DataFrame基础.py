import pandas as pd

# 创建字典
data = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9], 'd': [10, 11, 12]}
print(data)
df = pd.DataFrame(data)
print(df)
# 查看某一列数据
print(df['a'])
# 添加列
df['e'] = [13, 14, 15]
# 修改列数据
df['c'] = [71, 81, 91]
# 删除列
del df['e']
print(df)
