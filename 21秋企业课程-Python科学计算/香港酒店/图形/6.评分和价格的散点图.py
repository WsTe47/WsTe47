import pandas as pd
import matplotlib.pyplot as plt

# 解决中文乱码问题
plt.rcParams['font.sans-serif'] = 'SimHei'
# 解决负号无法显示问题
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_excel('香港酒店数据1.xlsx')
df = df.sort_values(by=['价格'], ascending=False)
print(df)
df=df.drop([9])
print(df)
y = df['价格'].values[::1]
x = df['评分'].values[::1]
plt.figure(figsize=(10, 8))
plt.scatter(x, y, color='c', marker='p')
plt.title('酒店价格与评分', fontsize=20)
plt.xlabel('价格', fontsize=18)
plt.ylabel('评分', fontsize=18)
plt.show()
