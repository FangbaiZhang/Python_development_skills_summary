# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
WeiXin: AXiaShuBai
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2020/2/27 14:54
Desc:
'''

# 序列化的两个模块：
# • json: 用于字符串和python数据类型间进行转换
# • pickle： 用于python特有的类型和python的数据类型间进行转换
# Json模块提供了四个功能：dumps、dump、loads、load
# pickle模块提供了四个功能：dumps、dump、loads、load

# 带s的是用来处理数据，不带的是处理文件：load读取文件，dump写入文件

# pickle中：
# dumps可以将数据类型转换成序列化（只有python才认识）的字符串
# loads将已经序列化的数据反序列化为正常的对象，字符串，函数，类等


# 那pickle和json有什么区别呢？
# json是可以在不同语言之间交换数据的，而pickle只在python之间使用。
# json只能序列化最基本的数据类型，而pickle可以序列化所有的数据类型，包括类，函数都可以序列化。
# json序列化后的数据看起来好像是个字典，但要注意了，实际上这是个字符串，因为json只能是字符串格式，只是看起来像字典而已。
