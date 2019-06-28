# -*- coding:utf-8 -*-

s1 = '   abcde    '
s2 = '---fatg++++++'

# 删除左边或者右边字符,不传参数就是删除空格，传入参数就是删除传入的符号
print(s1.lstrip())
print(s2.rstrip('g+'))

# 删除两端字符，只能从两端连续删除
print(s2.strip('-+'))
# 删除中间的不可以
print(s2.strip('a+'))

