import pandas as pd
import numpy as np

# Series对象计算
s1 = pd.Series([1, 2, 3, 4, 5], index=['A', 'B', 'C', 'D', 'E'])
print(s1)
s2 = pd.Series([6, 7, 8, 9], index=['A', 'C', 'G', 'E'])
print(s2)
print(s1 + s2)
# DataFrame对象计算
s1 = pd.DataFrame(np.arange(9).reshape(3, 3), columns=['A', 'B', 'C'], index=['a', 'b', 'c'])
print(s1)
s2 = pd.DataFrame(np.arange(16).reshape(4, 4), columns=['A', 'B', 'C', 'D'], index=['a', 'b', 'c', 'd'])
print(s2)
print(s1 + s2)
# 排序
# 1.series排序
ser1 = pd.Series(np.random.randint(0, 50, 4), index=['a', 'd', 'c', 'b'])
print(ser1)
print(ser1.sort_index())
print(ser1.sort_values())
# 2.datarame排序
frame = pd.DataFrame(np.arange(8).reshape(2, 4), index=['B', 'A'], columns=['a', 'c', 'd', 'b'])
print(frame)
print(frame.sort_index())
print(frame.sort_index(axis=0))
print(frame.sort_index(axis=1, ascending=False))
