# -*- coding:utf-8 -*-
#
# 集合支持一系列标准操作，包括并集、交集、差集和对称差集，例如：
# a = t | s          # t 和 s的并集
# b = t & s          # t 和 s的交集
# c = t – s          # 求差集（项在t中，但不在s中）
# d = t ^ s          # 对称差集（项在t或s中，但不会同时出现在二者中）

a = [1, 5, 10, 15, 10]
b = [1, 5, 10, 9, 12]

# 集合会去掉重复元素
print(set(a))
print("*" * 50)

# 并集
c1 = set(a) | set(b)
print(c1)

# 交集
c2 = set(a) & set(b)
print(c2)

# 交集
c3 = set(a) - set(b)
print(c3)
c3 = set(b) - set(a)
print(c3)


# 对称差集
c4 = set(a) ^ set(b)
print(c4)