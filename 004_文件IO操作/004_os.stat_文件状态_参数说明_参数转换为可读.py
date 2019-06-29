# -*- coding:utf-8 -*-

import os
import stat
import time

# 查看文件状态
s1 = os.stat('001_测试缓冲案例文件.txt')
print(s1)
s = s1.st_mode
print(s)
print('*' * 50)

# 使用stat标准查看判断文件的权限类型等
# 查看stat里面的一些方法函数
# print(dir(stat))

# 判断是否是文件夹,False不是文件夹
print(stat.S_ISDIR(s1.st_mode))

# 是否是普通文件，True是一个普通文件
print(stat.S_ISREG(s))
print('*' * 50)

# 文件权限，还是在st_mode中
# RUSR用户USR有读R的权限
# 结果只要是大于0数就是True，有读的权限
print(s & stat.S_IRUSR)

# 执行权限,只读打开的，没有执行权限，结果为0
print(s & stat.S_IXUSR)
print('*' * 50)

# 最后访问时间
# 可以修改下文件，重新运行，发现最后时间就更新了
t = s1.st_atime
print(t)
# 时间是秒,要转换为当前时间
t_now = time.localtime(t)
print(t_now)
print('*' * 50)

# 文件大小,大小是字节数
print(s1.st_size)
print('*' * 50)