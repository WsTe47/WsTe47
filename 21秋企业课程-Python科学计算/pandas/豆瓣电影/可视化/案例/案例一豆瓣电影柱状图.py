'''
绘制每个国家或地区的电影数量的柱状图
'''
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 解决中文乱码问题
plt.rcParams['font.sans-serif'] = 'SimHei'
# 解决负号无法显示问题
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_excel('movie.xlsx')
print(df[:5])
data = df['产地'].value_counts()
print(data)
x = data.index
y = data.values
plt.figure(figsize=(10, 6))
plt.bar(x, y, color='g')
plt.title('各国家或地区电影数量', fontsize=20)
plt.xlabel('国家或地区', fontsize=16)
plt.ylabel('电影数量', fontsize=16)
# 坐标轴的字体调整
plt.tick_params(labelsize=14)
# 调整x轴竖着显示
plt.xticks(rotation=90)
# 显示每个轴的数字
for a, b in zip(x, y):
    # 第一个参数x轴位置,第二个参数y轴位置,第三个参数显示的文本内容
    plt.text(a, b + 50, b, ha='center', va='bottom', fontsize=10)
plt.show()
