# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2019/9/16 21:53
Desc:
'''

# 网址只有某个页码不同，直接生成大量网址的列表
url_list = ["https://www.renren.com/videos?page=" + str(i) + "&size=12" for i in range(1, 21)]
print(type(url_list))
print(url_list)