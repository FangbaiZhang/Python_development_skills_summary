# -*- coding:utf-8 -*-

s = 'abc'

# 使用format方法
# 左对齐
s1 = format(s, '<20')
print(s1)
print(len(s1))
print("*" * 50)

# 右对齐
s2 = format(s, '>20')
print(s2)
print(len(s2))
print("*" * 50)

# 居中对齐
s3 = format(s, '^20')
print(s3)
print(len(s3))
print("*" * 50)