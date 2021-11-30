import pandas as pd
import numpy as np

ser = pd.Series(np.random.randint(0, 20, size=3), index=['A', 'B', 'C'])
print(ser)
print(ser.index)
print(ser[1:])
# 重建索引
ser = ser.reindex(['A', 'C', 'B'])
print(ser)
# 根据索引删除
ser = ser.drop('A')
print(ser)
ser = pd.Series(np.random.randint(0, 20, size=5), index=['A', 'B', 'C', 'D', 'E'])
print(ser)
ser = ser.drop(['A', 'C', 'E'])
print(ser)

df = pd.DataFrame(np.arange(10).reshape(2, 5), index=['a', 'b'], columns=['A', 'B', 'C', 'D', 'E'])
print(df)
df1 = df.drop('A', axis=1)
print(df1)
df1 = df.drop('a')
print(df1)
df = pd.DataFrame(np.random.randint(0, 100, size=15).reshape(3, 5), index=['a', 'b', 'C'],
                  columns=['A', 'B', 'C', 'D', 'E'])
print(df)
print(df['A'])
print(df[['A', 'B', 'C']])
print(df[df['B'] > 30])
print(df[(df['B'] > 30) & (df['C'] > 50)])
