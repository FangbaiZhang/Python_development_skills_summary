# -*- coding:utf-8 -*-

import os

# 查看文件状态
# 方式1：stat传入path路径
s1 = os.stat('001_测试缓冲案例文件.txt')
print(s1)
print('*' * 50)

# 方式2：fstat传入文件描述符
f = open('001_测试缓冲案例文件.txt', 'r')
# 获取打开文件后的描述符
s2 = f.fileno()
print(s2)
# 传入描述符，获取文件状态
s3 = os.fstat(s2)
print(s3)
print('*' * 50)

