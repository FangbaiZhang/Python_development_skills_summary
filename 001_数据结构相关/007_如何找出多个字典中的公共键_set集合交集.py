# -*- coding:utf-8 -*-

from random import randint, sample

# sample用于随机取样,取出随机个数的元素
# abcdefg七个个字母代表七个个球员，取出随机的到1到3个表示有进球
l1 = sample('abcdefg', randint(1, 3))
print(l1)
print("*" * 100)

# 每一节比赛：进球人员及对应的进球个数
s1 = {x: randint(1, 2) for x in sample('abcdefg', randint(1, 5))}
print(s1)
s2 = {x: randint(1, 2) for x in sample('abcdefg', randint(1, 5))}
print(s2)
s3 = {x: randint(1, 2) for x in sample('abcdefg', randint(1, 5))}
print(s3)
print("*" * 100)

# 找出s1\s2\s3都出现过的键,也有可能一个都没有，可以多运行代码几次
# 初级方法,for循环遍历查找：
res = []
for k in s1:
    if k in s2 and k in s3:
        res.append(k)
print(res)
print("*" * 100)

# 高级方法1:
# set集合交集：
# 每个字典的键可以取出，类型是一个集合，可以直接去交集
print(type(s1.keys()))
res = s1.keys() & s2.keys() & s3.keys()
print(res)
print("*" * 100)


