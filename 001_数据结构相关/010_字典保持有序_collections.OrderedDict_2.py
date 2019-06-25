# -*- coding:utf-8 -*-

from collections import OrderedDict
from random import randint
import time

d = OrderedDict()
players = list('ABCDEFGH')
start = time.time()

for i in range(8):
    # 使用一个input函数作为阻塞函数，等待输入
    input("依次输入1-8的数字：")
    p = players.pop(randint(0, 7-i))
    # 开始时间相同，结束时间不同
    end = time.time()
    print(i+1, p, end - start)
    d[p] = (i+1, end - start)
print(d)

