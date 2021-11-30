# 散点图: 研究两个变量的相关性: 正相关、负相关、不想关

import matplotlib.pyplot as plt
import numpy as np

# 随机生成x,y数据 不相关
x = np.random.randn(1000)
y = np.random.randn(1000)
plt.scatter(x, y)
plt.show()

# y是通过x生成的,图形是向右上方倾斜的，正相关
y1 = x + np.random.randn(1000) * 0.5
plt.scatter(x, y1)
plt.show()
# 向右下方倾斜的,负相关
y2 = -x + np.random.randn(1000) * 0.5
plt.scatter(x, y2)
plt.show()
