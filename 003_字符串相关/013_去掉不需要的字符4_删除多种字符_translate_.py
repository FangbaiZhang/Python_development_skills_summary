# -*- coding:utf-8 -*-
import string


s = 'abc12334243xyz'

# 字符串映射表，对应替换，传入的长度相同
s1 = str.maketrans('abcxyz', 'xyzabc')
print(s1)

# 翻译替换，传入每个字符要翻译成对象，使用str.maketrans传入
s2 = s.translate(str.maketrans('abcxyz', 'xyzabc'))
print(s2)

# 删除多种字符，也可以使用
s = 'abc\tfafa\rfae\tfat'
s3 = s.translate(str.maketrans('\t\r', '  '))
print(s3)