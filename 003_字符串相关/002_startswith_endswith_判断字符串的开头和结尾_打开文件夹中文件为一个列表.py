# -*- coding:utf-8 -*-


# 如何判断字符串a是否以字符串b开头或者结尾
# 比如判断一个文件夹下所有文件的后缀名，即文件的类型

import os, stat

# 将文件夹中文件名打开为一个列表
l = os.listdir('./002_案例测试文件夹')
print(l)

# endswith判断字符串的结尾和开头
s= 'g.sh'
print(s.endswith('.sh'))
print(s.startswith('p'))


# 也可以传入元组，只要一个满足即可
print(s.endswith(('.sh', '.py')))

# 过滤歘上面列表中py和sh的列表
l = [name for name in os.listdir('./002_案例测试文件夹') if name.endswith(('.sh', '.py'))]
print(l)