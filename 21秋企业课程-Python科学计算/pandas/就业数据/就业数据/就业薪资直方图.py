import pandas as pd
import matplotlib.pyplot as plt

# 解决中文乱码问题
plt.rcParams['font.sans-serif']='SimHei'
# 解决负号无法显示问题
plt.rcParams['axes.unicode_minus']=False

df = pd.read_excel('data.xlsx')
plt.figure(figsize=(10,6))
plt.hist(df['salary'],bins=10,edgecolor='k')
plt.title('就业薪资')
plt.xlabel('薪资')
plt.ylabel('数量')
plt.show()