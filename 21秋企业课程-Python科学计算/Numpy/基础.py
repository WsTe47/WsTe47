# 列表
a = [1, 2, 3, 4]
b = ['a', 'b', 'c', 'd']
# 取列表长度
l = len(a)
print(l)
# 切片
# c[i:j] 从位置i开始取到j-1位置，返回列表
c = ['黄瓜', '西瓜', '苹果', '香蕉', '草莓', '柚子']
c1 = c[1:3]
print(c1)
c2 = c[2:5]
print(c2)
c3 = c[1:]
print(c3)
c4 = c[2:-1]
print(c4)
# 追加元素
c.append('哈密瓜')
print(c)
s = '/'.join(c)
print(s)
for i in c:
    print(i)
# 字典 json
d = {}
print(type(d))
import json

d = {'name': '可乐', 'price': 4.5, 'count': 1, 'volume': 450}
d1 = {'name': '橙汁', 'price': 5.0, 'count': 2, 'volume': 500}
l = []
l.append(d)
l.append(d1)
print(l)
print(d['name'])
for k, v in d.items():
    print(k, v)
with open('../pandas/就业数据/data.json', 'wb') as f:
    f.write(json.dumps(d, ensure_ascii=False).encode('utf-8'))
