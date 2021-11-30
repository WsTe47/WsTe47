import pandas as pd
import matplotlib.pyplot as plt

# 解决中文乱码问题
plt.rcParams['font.sans-serif'] = 'SimHei'
# 解决负号无法显示问题
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_excel('香港酒店数据1.xlsx')
print(df.columns)
print(df['评分人数'].value_counts())
df['热门等级'] = pd.cut(df['评分人数'], [0, 500, 1000, 2000, 8000, 50000],
                    labels=['D', 'C', 'B', 'A', 'S'])

print(df['热门等级'].value_counts())
y=df['热门等级'].value_counts().values
x=df['热门等级'].value_counts().index

plt.figure(figsize=(8, 8))
plt.title('各热门等级酒店评分', fontsize=20)
plt.xlabel('热门等级', fontsize=15)
for a, b in zip(x, y):
    # 第一个参数:x轴的位置,第二参数:y轴的位置,第三个参数:显示的内容
    plt.text(a, b + 0.3, b, ha='center', va='bottom', fontsize=12)
plt.bar(x, y, width=0.5, color='r', label='数量')
# 显示图例
plt.legend()
plt.show()