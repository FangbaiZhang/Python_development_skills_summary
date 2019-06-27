# -*- coding:utf-8 -*-

# 含有多种分隔符分割

# 方法1：未成功呵呵
# 定义一个分割函数
def mySplit(s, ds):
    res = [s]

    # ds是要分割的符号，for循环依次分割每一种符号
    # 每分割一次都加入到t列表中，使用的extend扩展列表，列表最后还是一维的列表
    for d in ds:
        t = []
        map(lambda x: t.extend(x.split(d)), res)
        res = t

    # 如果有两个符号在一起，分割后会产生空字符，需要排除空字符，加入if判断
    return  [x for x in res if x]

s = 'ab;cd%e\tfg,,jklioha;hp,vrww\tyz'
a = mySplit(s, ';%,')
print(a)


# 方法2：
# 正则表达式分割,推荐使用
import re
# 将多个分隔符直接写在正则表达式中，使用中括号，后面的+号表示前面的符号可以出现多次
t = re.split(r'[;%,\t]+', s)
print(t)
