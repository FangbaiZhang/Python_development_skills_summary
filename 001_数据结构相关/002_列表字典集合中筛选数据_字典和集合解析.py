# -*- coding:utf-8 -*-

# 字典筛选数据
from random import randint

# 生成一个随机字典
dict = {x: randint(60, 100) for x in range(1, 21)}
print(dict)
print("*" * 100)

# 筛选出值大于90的键值
res = {k: v for k, v in dict.items() if v > 90}
print(res)
print("*" * 100)

# 集合筛选数据
data = list(randint(-10, 20) for x in range(1, 21))
print(data)
# 列表转换为集合，去掉重复元素
s = set(data)
print(s)
print("*" * 100)

# 集合解析，筛选出能被3整除的数
res = {x for x in s if x % 3 == 0}
print(res)