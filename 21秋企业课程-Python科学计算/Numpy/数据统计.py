import numpy as np

arr = np.random.randint(1, 20, size=10)
print(arr)
# 排序
a = np.sort(arr)
print(a)
arr = np.random.randint(0, 50, size=25).reshape(5, 5)
print(arr)
# axis排序的轴索引，默认是-1
a = np.sort(arr, axis=1)
print(a)
# 按竖向排序
a = np.sort(arr, axis=0)
print(a)
name = np.array(['小敏', '小米', '校长', '小米', '小米', '小米', '小王', '小张', '小王'])
# 去重
n = np.unique(name)
print(n)
# 数据统计
arr = np.arange(20).reshape(4, 5)
print(arr)
# 所有元素求和
print(np.sum(arr))
# 按0轴求和
print(np.sum(arr, axis=0))
# 按1轴求和
print(np.sum(arr, axis=1))
# 求所有元素平均数
print(np.mean(arr))

print(np.min(arr))
print(np.max(arr))
