# -*- coding:utf-8 -*-

from random import randint

# 可迭代对象可以使用sorted进行排序
l1 = sorted([2, 5, 7, 4, 9])
print(l1)
print("*" * 100)

# 生成一个字典
dic = {x: randint(60, 100) for x in 'xyzabc'}
print(dic)
print("*" * 100)
# 字典直接使用sorted排序，会按照键进行排序
# 查看字典的可迭代对象，实际是字典的键
print(iter(dic))
print(list(iter(dic)))
print(sorted(dic))
print("*" * 100)


# 初级方法：
# 元组元素比较，先比较第0个元素，如果第一个相等，则再依次向后比较
# 可以将上面的字典转换为元组，然后进行比较
# zip将两个可迭代对象生成一一对应的元组
dic1 = zip(dic.values(), dic.keys())
dic2 = list(dic1)
print(dic2)
# 按照键由小到大排序
print(sorted(dic2))
# 按照键由大到小排序，元组第一个元素，即键相同，则会去比较第二个元素
print(sorted(dic2, reverse=True))
print("*" * 100)


# 高级方法：
# 上面使用zip函数转变了字典
# sorted函数可以传入一个key作为比较的值
dic3 = sorted(dic.items(), key=lambda x: x[1])
print(dic3)
