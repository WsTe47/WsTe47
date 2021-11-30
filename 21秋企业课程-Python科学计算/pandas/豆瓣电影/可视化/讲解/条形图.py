# 以长方形的长度为变量的统计图表
# 通常用于比较小的数据集分析
# 例如: 不同季度销量，不同国家的人口

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(5)
print(x)
y = [20, 10, 30, 25, 55]

# 解决中文问题
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.title('月销量')
plt.xlabel('月')
plt.ylabel('销量')
for a, b in zip(x, y):
    # 第一个参数:x轴的位置,第二参数:y轴的位置,第三个参数:显示的内容
    plt.text(a, b + 0.2, b, ha='center', va='bottom', fontsize=12)
plt.bar(x, y, width=0.5, color='r', label='销量')
# 显示图例
plt.legend()
plt.show()
