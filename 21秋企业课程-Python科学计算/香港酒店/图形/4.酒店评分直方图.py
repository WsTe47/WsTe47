import pandas as pd
import matplotlib.pyplot as plt

# 解决中文乱码问题
plt.rcParams['font.sans-serif'] = 'SimHei'
# 解决负号无法显示问题
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_excel('香港酒店数据1.xlsx')

plt.figure(figsize=(10, 6))
# bins柱子数量,edgecolor:柱子加边框,alpha:透明度
plt.hist(df['评分'], bins=20, edgecolor='k', alpha=0.5)
plt.title('酒店评分的直方图-ghd')
plt.show()
