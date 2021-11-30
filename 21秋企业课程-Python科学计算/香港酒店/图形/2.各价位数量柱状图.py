import pandas as pd
import matplotlib.pyplot as plt

# 解决中文乱码问题
plt.rcParams['font.sans-serif'] = 'SimHei'
# 解决负号无法显示问题
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_excel('香港酒店数据1.xlsx')
# 离散化处理: 在实际的项目中，对有的属性，往往不关心数据的绝对值，只关注他所处的区间或等级
# 比如我们可以评分9分及以上定义为A,7-9为B,5-7为C,3-5为D,小于3为E
# pd.cut(x,bins,labels) x:需要离散化处理的数据(数组,Series,DataFrame) bins:分组的依据 labels: 区间划分的结果
# 0-3 3-5 5-7 7-9 9-10
df['价格等级'] = pd.cut(df['价格'], [0, 500, 1000, 2000, 4000, 20000],
                    labels=['0-499', '500-999', '1000-1999', '2000-3999', '4000-19999'])

print(df['价格等级'].value_counts())
y = df['价格等级'].value_counts().values
x = df['价格等级'].value_counts().index

plt.figure(figsize=(8, 8))
plt.title('各价格酒店数量', fontsize=20)
plt.xlabel('价格', fontsize=15)
for a, b in zip(x, y):
    # 第一个参数:x轴的位置,第二参数:y轴的位置,第三个参数:显示的内容
    plt.text(a, b + 0.3, b, ha='center', va='bottom', fontsize=12)
plt.bar(x, y, width=0.5, color='r', label='数量')
# 显示图例
plt.legend()
plt.show()
