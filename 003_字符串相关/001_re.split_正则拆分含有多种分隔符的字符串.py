# -*- coding:utf-8 -*-

# 含有多种分隔符分割

s = 'ab;cd%e\tfg,,jklioha;hp,vrww\tyz'

# 方法1，使用中括号：
# 正则表达式分割,推荐使用
import re
# 将多个分隔符直接写在正则表达式中，使用中括号，后面的+号表示前面的符号可以出现多次
t = re.split(r'[;%,\t]+', s)
print(t)

# 方法2：使用|表示或
s="info：xiaoZhang 33 shandong"
res = re.split(r'：| ', s)
print(res)

