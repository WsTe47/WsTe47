import pandas as pd
import matplotlib.pyplot as plt

# 解决中文乱码问题
plt.rcParams['font.sans-serif']='SimHei'
# 解决负号无法显示问题
plt.rcParams['axes.unicode_minus']=False

df = pd.read_excel('data.xlsx')

data = df['date'].value_counts()
data = data.sort_index()
print(data)
x = data.index
y = data.values
plt.plot(x,y)
plt.title('月就业数量',fontsize=20)
plt.xlabel('日期',fontsize=16)
plt.ylabel('就业数量',fontsize=16)
#调整x轴竖着显示
plt.xticks(rotation=90)
#每隔10年
for a,b in zip(x,y):
    plt.text(a,b,b,ha='center',va='bottom',fontsize=10)
plt.show()