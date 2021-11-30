import pandas as pd
import matplotlib.pyplot as plt

# 解决中文乱码问题
plt.rcParams['font.sans-serif']='SimHei'
# 解决负号无法显示问题
plt.rcParams['axes.unicode_minus']=False

df = pd.read_excel('data.xlsx')
data = df['status'].value_counts()
print(data)
x = data.values
y = x/sum(x)
print(x)
print(y)
plt.figure(figsize=(15,10))
plt.pie(y,labels=data.index,autopct='%.1f %%')
plt.title('就业人员状态占比')
#显示图例
plt.legend()
plt.show()