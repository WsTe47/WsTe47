import matplotlib.pyplot as plt
import pandas as pd

# 解决中文乱码问题
plt.rcParams['font.sans-serif'] = 'SimHei'
# 解决负号无法显示问题
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_excel('香港酒店数据1.xlsx')

df['价格等级'] = pd.cut(df['价格'], [0, 500, 1000, 2000, 4000, 20000],
                    labels=['0-499', '500-999', '1000-1999', '2000-3999', '4000-19999'])

group = df.groupby('价格等级')

x=df['价格等级'].value_counts().values
x=x/sum(x)
plt.figure(figsize=(7, 7))
plt.title('各价格等级占比', fontsize=15)
plt.pie(x, labels=df['价格等级'].value_counts().index, autopct='%.1f %%', startangle=90)
plt.legend()
plt.show()
