import numpy as np

l = [1, 2, 3, 4]
arr = np.array(l)
print(arr)
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr1)
i = arr[0]
print(i)
i = arr1[1][2]
print(i)
a = np.arange(1, 10)
print(type(a))
print(a)
print(arr1.ndim)  # 查看维度
print(arr1.shape)  # 查看形状
print(arr1.dtype)  # 查看数据类型
# 数据类型转换
arr2 = arr1.astype(np.float32)
print(arr2)
print(arr2.dtype)
# 数组运算
a = np.arange(10)
print(a)
a = a + 2
print(a)
print(a > 5)
# 索引和切片
arr1 = np.array([[1, 2, 3,11], [4, 5, 6,7], [7, 8, 9,10]])
print(arr1)
print(arr1[1][2])
print(arr1[1:, 1:])
# 布尔索引:通过布尔值进行索引的方式,可以类比于开关,用于确定数据位的显示于关闭
a2 = np.array([1, 2, 3, 4])
b2 = np.array([True, False, True, False])
# True的过滤出来
print(a2[b2])
c = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
c1 = np.array([
    [True, False, True],
    [True, False, False],
    [True, True, False]
])
print(c[c1])
