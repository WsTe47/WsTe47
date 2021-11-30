# 折线图是用直线将各数据连接起来组成的图形
# 通常表示数据随时间变化的趋势
# 例如: 温度变化
import matplotlib.pyplot as plt
import numpy as np

# 生成-10到10，5等分的数字
x = np.linspace(-10, 10, 5)
print(x)
y = x ** 2
print(y)
plt.plot(x, y)
plt.show()
