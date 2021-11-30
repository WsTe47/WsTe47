'''
根据电影时长和电影评分绘制散点图
用两组数据构成多个坐标点，考察坐标点的分布上，判断两变量之间是否存在某种关联或总结坐点的分布模式。
散点图将序列显示为一组点，值由点在图表中的位置表示。类别由图表中的不同标记表示。散点图通常用于比较跨类别的聚合数据
'''
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 解决中文乱码问题
plt.rcParams['font.sans-serif']='SimHei'
# 解决负号无法显示问题
plt.rcParams['axes.unicode_minus']=False

df = pd.read_excel('movie.xlsx')
#只取百分之一的数据
x = df['时长'][::100]
y = df['评分'][::100]

plt.figure(figsize=(10,8))
plt.scatter(x,y,color='c',marker='p')
plt.title('电影时长与评分',fontsize=20)
plt.xlabel('时长',fontsize=18)
plt.ylabel('评分',fontsize=18)
plt.show()