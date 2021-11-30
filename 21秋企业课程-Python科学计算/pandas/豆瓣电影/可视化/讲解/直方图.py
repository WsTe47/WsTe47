# 直方图: 同一系列的数据高度不等的纵向的条形组成,表示数据分布情况
# 例如: 薪水分布情况

import numpy as np
import matplotlib.pyplot as plt

x = 100 + 20 * np.random.randn(2000)
print(x)
plt.hist(x, bins=10)
plt.show()
