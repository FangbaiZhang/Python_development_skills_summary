# -*- coding:utf-8 -*-

# 筛选数据
# 初级做法，使用迭代，筛选出符合条件的数据
data = [1, 3, -21, 5, -8, 6]
res = []
for x in data:
    if x >= 0:
        res.append(x)
print(res)
print("*" * 50)


# 高级解决方案：filter函数，列表解析，字典解析，集合解析
# 列表筛选：
# 方法1：使用过滤函数filter
from random import randint
import time
data = [randint(-10, 10) for _ in range(10)]
print(data)
print("*" * 100)
# 过滤函数：符合条件的就留下，使用list生成一个列表
res = list(filter(lambda x: x >= 0, data))
print(res)
print("*" * 100)


# 方法2：列表解析,速度更快，推荐使用
start =time.time()
res = [x for x in data if x >= 0]
end = time.time()
print('Running time: %s Seconds'%(end-start))
print(res)

