'''
根据电影的时长绘制饼图
'''
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 解决中文乱码问题
plt.rcParams['font.sans-serif'] = 'SimHei'
# 解决负号无法显示问题
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_excel('movie.xlsx')

# 根据电影的长度绘制
data = pd.cut(df['时长'], [0, 60, 90, 110, 1000]).value_counts()
print(data)
y = data.values
y = y / sum(y)
print(y)

plt.figure(figsize=(7, 7))
plt.title('电影时长占比', fontsize=15)
plt.pie(y, labels=data.index, autopct='%.1f %%', startangle=90)
plt.legend()
plt.show()
