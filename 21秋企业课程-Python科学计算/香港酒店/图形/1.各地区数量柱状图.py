import pandas as pd
import matplotlib.pyplot as plt

# 解决中文乱码问题
plt.rcParams['font.sans-serif'] = 'SimHei'
# 解决负号无法显示问题
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_excel('香港酒店数据1.xlsx')
data = df['地区'].value_counts()
# print(data)
print(data.values)
print(data.index)

y = data.values
x = data.index
plt.figure(figsize=(10, 10))
plt.title('各地区酒店数量——GHD', fontsize=25)
plt.xlabel('地区', fontsize=20)
plt.ylabel('酒店数量', fontsize=20)
plt.bar(x, y, color='r', width=0.8)
# 调整x轴竖着显示
plt.xticks(rotation=90)
plt.tick_params(labelsize=11)
for a, b in zip(x, y):
    # 第一参数x轴的位置,第二个参数就是y轴的位置,第三个参数显示的文本内容
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
plt.show()
