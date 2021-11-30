# 饼状图: 显示一个数据系列中各项大小和占总的比例
# 例如: 十大品牌市场占有率

import numpy as np
import matplotlib.pyplot as plt

labels = ['A', 'B', 'C', 'D']
values = [15, 30, 45, 10]
plt.pie(x=values, labels=labels, autopct='%.0f%%', shadow=True)
plt.show()
