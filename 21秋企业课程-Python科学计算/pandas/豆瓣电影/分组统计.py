import pandas as pd

df = pd.read_excel('./movie2.xlsx')
print(df.head())
# 按产地分组
group = df.groupby(df['产地'])
# 统计分组后每一个数值列的平均值
print(group,'**********')
print(group.mean())
# 计算每年的平均评分
print(df['评分'].groupby(df['年代']).mean())
# 每一个地区，每一年的电影评分平均值
print(df['评分'].groupby([df['产地'], df['年代']]).mean())
# 离散化处理: 在实际的项目中，对有的属性，往往不关心数据的绝对值，只关注他所处的区间或等级
# 比如我们可以评分9分及以上定义为A,7-9为B,5-7为C,3-5为D,小于3为E
# pd.cut(x,bins,labels) x:需要离散化处理的数据(数组,Series,DataFrame) bins:分组的依据 labels: 区间划分的结果
# 0-3 3-5 5-7 7-9 9-10
df['评分等级'] = pd.cut(df['评分'], [0, 3, 5, 7, 9, 10], labels=['E', 'D', 'C', 'B', 'A'])
print(df)
pd.set_option('max_columns', 10)
print(df[df['评分等级'] == 'E'])
