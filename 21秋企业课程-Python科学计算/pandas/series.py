import pandas as pd

# Series这种数据结构类似于python列表的值(value)+标签(index),是一维的数据结构
# index可以是任意的值，必须保证每一个value对应一个index标签
# 1.通过列表创建 2.通过字典创建
s = pd.Series([1, 3, 5, 22, 40])
print(s)
# 自定义标签
s = pd.Series([1, 3, 5, 22, 40], index=['a', 'b', 'c', 'd', 'e'])
print(s)
# 取值(数组)
print(s.values)
# 取行标签
print(s.index)
# 根据索引取单个的值
print(s[2])
# 切片
print(s[2:5])
# 索引名称
s.index.name = '索引'
print(s)
# 根据行标签取值
print(s['d'])
# 如果是字符串行标签切片,右边是取值的
print(s['c':'e'])
# 通过字典创建
d = {'name': '可乐', 'price': 4.5, 'count': 1, 'volume': 450}
s1 = pd.Series(d)
print(s1)
