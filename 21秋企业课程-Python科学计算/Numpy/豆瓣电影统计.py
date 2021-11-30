import json
import numpy as np

'''
要求: 
1.读取json文件,分别创建电影名称、评分、评分人数、电影时长四个数组
2.对评分人数进行排序
3.打印出评分人数最少的电影名称和最多的电影名称
4.打印出所有的评分人数总和
5.打印出电影最长时长
6.打印出最小评分
7.打印平均电影时长
'''
movie_list = []
name = []
rate = []
rate_count = []
movie_len = []
with open('top250.json', 'r', encoding='utf-8') as f:
    movie_list = json.load(f)

print(movie_list)
for item in movie_list:
    # print(item)
    name.append(item['title'])
    rate.append(item['rating'])
    rate_count.append(item['count'])
    movie_len.append(item['length'])

title_arr = np.array(name)
rate_arr = np.array(rate)
count_arr = np.array(rate_count)
len_arr = np.array(movie_len)

print(title_arr)
print(rate_arr)
print(count_arr)
print(len_arr)

# 对评分人数进行排序
new_arr = np.sort(count_arr)
print(new_arr)
# 打印出所有的评分人数总和
print(f'评分人数总和：{np.sum(count_arr)}')
# 打印出电影最长时长
print(f'电影最长时长{np.max(len_arr)}')
# 打印出最小评分
print(f'最小评分{np.min(rate)}')
# 打印平均电影时长
print(f'平均电影时长{np.mean(len_arr)}')
# 打印出评分人数最少的电影名称和最多的电影名称
# 取出排序的值对应的索引
order = np.argsort(count_arr)
print(order)
print(f'评分人数最少的电影:{title_arr[order[0]]}')
print(f'评分人数最多的电影:{title_arr[order[-1]]}')
