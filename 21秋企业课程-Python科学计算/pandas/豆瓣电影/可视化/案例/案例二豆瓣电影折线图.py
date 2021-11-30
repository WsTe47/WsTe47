'''
绘制每年上映的电影数量的曲线图
'''
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 解决中文乱码问题
plt.rcParams['font.sans-serif']='SimHei'
# 解决负号无法显示问题
plt.rcParams['axes.unicode_minus']=False

df = pd.read_excel('movie.xlsx')
data = df['年代'].value_counts()
data = data.sort_index()
print(data)
x = data.index
y = data.values
print(x)
print(y)
plt.plot(x,y,color='b')
plt.title('每年电影数量',fontsize=20)
plt.ylabel('电影数量',fontsize=18)
plt.xlabel('年份',fontsize=18)
#每隔10年
for a,b in zip(x[::10],y[::10]):
    plt.text(a,b+10,b,ha='center',va='bottom',fontsize=10)


plt.show()