# -*- coding:utf-8 -*-
import re
from collections import Counter

# 读取整个文件为一个字符串
txt = open('009_filetest.txt').read()
# print(txt)

# 使用非字母对上面的字符串进行分割
res = re.split(r'\W+', txt)
# print(res)
# 统计每个单词出现的次数
c = Counter(res)
print(c)
print("*" * 100)
print(c.most_common(5))
print("*" * 100)