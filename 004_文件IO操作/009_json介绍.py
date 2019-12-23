# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2019/11/19 16:05
Desc:
'''

# json是 JavaScript Object Notation 的首字母缩写，
# 单词的意思是javascript对象表示法，
# 这里说的json指的是类似于javascript对象的一种数据格式，
# 目前这种数据格式比较流行，逐渐替换掉了传统的xml数据格式。

# json格式的数据主要有两种形式：
# 类似python字典的形式，实际类型是一个字符串，python使用load读取出来以后已经转换为字典类型了
# {"name":"tom", "age":18}

# json数据格式的属性名称(键)和字符串值(值)需要用双引号引起来，用单引号或者不用引号会导致读取数据错误

# json的另外一个数据格式是数组，和javascript中的数组字面量相同，python读取出来后就转变为列表类型了
# ["tom",18,"programmer"]  010json文件就是数组，不过数组内部元素是字典，读取出来就是一个列表

# 如果是字典形式，load读取出来就是python字典类型
# 如果是数组形式，load读取出来就是python列表类型
# 读取出来以后直接当做字典或者列表操作即可