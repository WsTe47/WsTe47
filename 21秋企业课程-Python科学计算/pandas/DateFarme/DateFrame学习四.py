import pandas as pd
import numpy as np

df = pd.read_excel('movie.xlsx')

# 分组
group = df.groupby(df['产地'])
# 可以计算分组后的各个统计值
print(group.mean())
# 计算每年的评均评分
print(df['评分'].groupby(df['年代']).mean())
# 也可以传入多个分组变量
print(df.groupby([df['产地'], df['年代']]).mean())
# 获得每个地区，每一年的电影评分的均值
means = df['评分'].groupby([df['产地'], df['年代']]).mean()
print(means)
# series通过unstack方法转化为dataframe
means_df = means.unstack()
print(means_df)
# 离散化处理:在实际项目中，对有的数据属性，我们往往并不关注数据的绝对值，只关注它所处的区间或等级
# 比如我们可以把评分9分及以上的电影定义为A,7-9为B,5到7为C,3-5为D,小于3为E
# pd.cut(x,bins,labels) x:需要离散化的数组,Series,DataFrame对象 bins:分组依据(左开右闭) labels:显示区间化分结果
# 0-3 3-5 5-7 7-9 9-10
df['评分等级'] = pd.cut(df['评分'], [0, 3, 5, 7, 9, 10], labels=['E', 'D', 'C', 'B', 'A'])
print(df)
# 可以根据投票人数来刻画电影的热门程度
bins = np.percentile(df['投票人数'], [0, 20, 40, 60, 80, 100])
df['热门程度'] = pd.cut(df['投票人数'], bins, labels=['E', 'D', 'C', 'B', 'A'])
print(df)
# 查看投票人数很多，评分很低
print(df[(df['热门程度'] == 'A') & (df['评分等级'] == 'E')])
