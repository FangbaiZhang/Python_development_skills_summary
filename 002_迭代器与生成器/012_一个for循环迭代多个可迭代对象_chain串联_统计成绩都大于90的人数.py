# -*- coding:utf-8 -*-

from random import randint
from itertools import chain

# chain多个可迭代对象串联，依次访问
for x in chain([1, 2, 3], ['a', 'b', 'c']):
    print(x)
print("*" * 50)

# 统计四个班级语文大于90的总人数
# chain串联所有班级的成绩，班级人数不同
c1 = [randint(60, 100) for _ in range(42)]
c2 = [randint(60, 100) for _ in range(44)]
c3 = [randint(60, 100) for _ in range(46)]
c4 = [randint(60, 100) for _ in range(45)]

count = 0
for x in chain(c1, c2, c3, c4):
    if x >= 90:
        count += 1
print(count)
print("*" * 50)
