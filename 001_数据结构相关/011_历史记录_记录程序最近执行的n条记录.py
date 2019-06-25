# -*- coding:utf-8 -*-

from random import randint
from collections import deque
import pickle


# 创建一个随机整数
N = randint(0, 100)
print(N)
# 创建一个空队列，容量为5
history = deque([], 5)

# 创建一个猜数字判断条件
def guess(k):
    if k == N:
        print("Right")
        return True
    if k < N:
        print("%s is less than N" % k)
    else:
        print("%s is greater than N" % k)
    return False

while True:
    line = input("Please input a number between 0 - 100:")
    if line.isdigit():
        k = int(line)
        history.append(k)
        if guess(k):
            break
    elif line == 'history' or line == 'h':
        print(history)

print("你猜对了！！！")