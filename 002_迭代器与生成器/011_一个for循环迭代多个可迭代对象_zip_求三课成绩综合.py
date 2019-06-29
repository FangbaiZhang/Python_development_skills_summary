# -*- coding:utf-8 -*-

from random import randint

# 创建3个数字列表
# 分别代表语文，数学，英语成绩
# 求和，求出总成绩
chinese = [randint(60, 100) for _ in range(10)]
math = [randint(60, 100) for _ in range(10)]
english = [randint(60, 100) for _ in range(10)]

# 联锁操作
for i in range(len(math)):
    res = chinese[i] + math[i] + english[i]
    print(res, [chinese[i], math[i], english[i]])
print("*" * 50)

# 上面是并行访问，可以使用zip函数，适用于长度相同
# 将可迭代对象一一对应，生成一个元组，然后所有元组生成一个列表
# 如果长度不一致，则只会取较短的为基准，长度不同就会少统计
for c, m, e in zip(chinese, math, english):
    res = c + m + e
    print(res, [c, m, e])
print("*" * 50)

# 长度不同，使用串联，参考012案例