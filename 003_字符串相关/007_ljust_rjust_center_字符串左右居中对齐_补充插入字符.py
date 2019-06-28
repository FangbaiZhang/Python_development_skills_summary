# -*- coding:utf-8 -*-

s = 'abc'

# 左对齐，传入数字是对齐后字符串的长度
s1 = s.ljust(20)
print(s1)
print(len(s1))
print("*" * 50)

# 右对齐，总共占位20个字符，前面空格填充
s2 = s.rjust(20)
print(s2)
print(len(s2))
print("*" * 50)

# 居中对齐
s3 = s.center(20)
print(s3)
print(len(s3))
print("*" * 50)

# 空字符可以添加填充字符,字符只能是一个
s4 = s.center(20, '=')
s5 = s.upper().center(20, 'X')
print(s4)
print(s5)
print(len(s4))
print("*" * 50)