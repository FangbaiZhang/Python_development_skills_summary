# -*- coding:utf-8 -*-

import os, stat

# 查看文件
f = os.stat('./002_案例测试文件夹/test1.py')
print(f)

# 查看文件权限
print(os.stat('./002_案例测试文件夹/test1.py').st_mode)

# 修改文件权限
os.chmod('./002_案例测试文件夹/test1.py', os.stat('./002_案例测试文件夹/test1.py').st_mode | stat.S_IXUSR)

print(os.stat('./002_案例测试文件夹/test1.py').st_mode)