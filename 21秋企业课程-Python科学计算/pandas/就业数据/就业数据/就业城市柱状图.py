import pandas as pd
import matplotlib.pyplot as plt

# 解决中文乱码问题
plt.rcParams['font.sans-serif'] = 'SimHei'
# 解决负号无法显示问题
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_excel('data.xlsx')
data = df['city'].value_counts()
print(data)
x = data.index
y = data.values

plt.figure(figsize=(10, 6))
plt.bar(x, y, color='g', width=0.8)
plt.title('各个城市就业分布', fontsize=20)
plt.xlabel('城市', fontsize=16)
plt.ylabel('就业数量', fontsize=16)
# 调整x轴竖着显示
plt.xticks(rotation=90)
# 显示每个轴的数字
for a, b in zip(x, y):
    # 第一参数x轴的位置,第二个参数就是y轴的位置,第三个参数显示的文本内容
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
plt.show()
