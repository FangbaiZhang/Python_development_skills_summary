# -*- coding:utf-8 -*-

import os

# os.path很多内置函数，可以直接查看文件状态
# 相对于003/004案例中的os.stat更快捷
print(dir(os.path))
print('*' * 50)

# 是否是文件夹
print(os.path.isdir('001_测试缓冲案例文件.txt'))
print('*' * 50)

# 是否是普通文件
print(os.path.isfile('001_测试缓冲案例文件.txt'))
print('*' * 50)

# 创建时间，最后访问时间
print(os.path.getctime('001_测试缓冲案例文件.txt'))
print(os.path.getatime('001_测试缓冲案例文件.txt'))
print('*' * 50)

# 文件大小
print(os.path.getsize('001_测试缓冲案例文件.txt'))
print('*' * 50)