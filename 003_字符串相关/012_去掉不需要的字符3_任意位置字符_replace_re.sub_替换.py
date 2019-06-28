# -*- coding:utf-8 -*-
import re

s = r'\tafa\t13d\t8773\rfafa\r323'

# replace替换方法，但是每次只能替换一个
# 删除所有\t,替换为空格，也可以替换为其它字符
s1 = s.replace(r'\t', '')
print(s1)
print('*' * 50)

# re.sub正则替换一次可以替换多个
s = '\tafa\t13d\t8773\rfafa\r323'
s2 = re.sub(r'[\t\r]', '', s)
print(s2)
print('*' * 50)