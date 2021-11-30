'''
根据电影的评分绘制频率分布直方图
直方图: 又称质量分布图，是一种统计报告图，由一系列高度不等的纵向条纹或线段表示数据的分布情况，
一般用横轴表示数据类型，纵轴表示分布情况
'''
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 解决中文乱码问题
plt.rcParams['font.sans-serif']='SimHei'
# 解决负号无法显示问题
plt.rcParams['axes.unicode_minus']=False

df = pd.read_excel('movie.xlsx')

plt.figure(figsize=(10,6))
#bins柱子数量,edgecolor:柱子加边框,alpha:透明度
plt.hist(df['评分'],bins=20,edgecolor='k',alpha=0.5)
plt.title('电影的评分频率')
plt.show()