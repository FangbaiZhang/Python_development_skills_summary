# -*- coding:utf-8 -*-

from collections import OrderedDict

# python内置dict是无序的
# 创建一个空字典，然后添加元素进去
# Python2中是无序的，Python3中已经有序的
dict1 = {}
dict1['a'] = 10
dict1['b'] = 20
dict1['c'] = 30
dict1['d'] = 40
print(dict1)
for k in dict1:
    print(k)
print("*" * 100)


# 使用有序字典OrderedDict
# 可以按顺序写入读取
dict1 = OrderedDict()
dict1['a'] = 10
dict1['b'] = 20
dict1['c'] = 30
dict1['d'] = 40
print(dict1)
for k in dict1:
    print(k)
print("*" * 100)


