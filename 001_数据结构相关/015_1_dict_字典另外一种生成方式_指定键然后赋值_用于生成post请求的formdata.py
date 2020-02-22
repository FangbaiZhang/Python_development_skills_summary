# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
WeiXin: AXiaShuBai
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2020/2/22 22:51
Desc:
'''
a = 10
b = 20
c = 30

d = dict(a=a, b=b, c=c)
print(d)

# 常用于post请求生成formdata
# rsp = requests.post(url, data=data) 传入的data就是FormData需要是字典格式
formdata = dict(commit="sign_in", user_name="10086@qq.com", password="123456")
print(formdata)