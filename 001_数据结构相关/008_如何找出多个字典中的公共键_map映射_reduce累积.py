# -*- coding:utf-8 -*-

from random import randint, sample
from functools import reduce

# 每一节比赛：进球人员及对应的进球个数
s1 = {x: randint(1, 2) for x in sample('abcdefg', randint(1, 5))}
print(s1)
s2 = {x: randint(1, 2) for x in sample('abcdefg', randint(1, 5))}
print(s2)
s3 = {x: randint(1, 2) for x in sample('abcdefg', randint(1, 5))}
print(s3)
print("*" * 100)


# 高级方法2：
# 定义一个函数，然后使用map映射函数生成一个由每个字典的keys组成的列表
def fun(s):
    return s.keys()
l1 = list(map(fun, [s1, s2, s3]))
print(l1)
print("*" * 100)

# reduce函数：reduce() 函数会对参数序列中元素进行累积。
# 函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：
# 用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，
# 得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。
res = reduce(lambda a, b: a & b, map(fun, [s1, s2, s3]))
print(res)
print("*" * 100)