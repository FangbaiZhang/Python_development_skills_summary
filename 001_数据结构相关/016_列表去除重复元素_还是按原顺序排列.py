# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2019/9/17 22:22
Desc:
'''

l = ['1', '5', '1', '3', '3',]
def list_new(l):
    # 先使用set生成一个集合，会自动删除掉重复的元素
    # 使用sorted排序，排序还是按照以前的索引值
    list_new = sorted(set(l), key=l.index)
    print(list_new)

list_new(l)