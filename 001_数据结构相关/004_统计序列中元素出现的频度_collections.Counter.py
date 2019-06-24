# -*- coding:utf-8 -*-

from numpy import random
from random import randint

# 生成一个随机序列,两种方法
print("*" * 100)
data = [randint(0, 20) for _ in range(20)]
print(data)
data = list(random.randint(0, 20, 20))
print(data)
print("*" * 100)

# 统计随机序列中元素出现的次数
# 初级方法：
# 以上面序列中的元素作为键生成一个字典
c = dict.fromkeys(data, 0)
print("空字典：")
print(c)
print("*" * 100)
# 循环data中的每一个元素，元素在里面一次，该元素对应字典中的值就加1
for x in data:
    c[x] += 1
print("统计后的字典：")
print(c)
print("*" * 100)


# 高级方法：
from collections import Counter
c2 = Counter(data)
print(c2)
print("*" * 100)
# 上面已经统计频度的结果，可以直接找出出现频度最高的n个元素
c3 = c2.most_common(3)
print("频度最高三个元素及出现次数：")
print(c3)
print("*" * 100)
