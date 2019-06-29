# -*- coding:utf-8 -*-

# 字符串前加r：去除反斜杠的\的转义含义，表示后面的一个符号\

# 字符串前加u：我是含有中文字符组成的字符串,后面字符串以 Unicode 格式 进行编码，
# 一般用在中文字符串前面，防止因为源码储存格式问题，导致再次使用时出现乱码

# 字符串前加b：后面字符串是bytes 类型，网络编程中，服务器和浏览器只认bytes 类型数据。
# 如：send 函数的参数和 recv 函数的返回值都是 bytes 类型


# bytes 和 str 的互相转换方式
# 一个汉字在utf-8编码下为3个字节
# 用什么编码，就要用什么解码，编码解码要一致，不然就会出错或者乱码
# 同一个汉字，不同编码格式的字节不同，字节数也不同
# 字符串编码为字节
s = u'汉字'
s1 = str.encode(s, 'utf-8')
print(type(s))
print(type(s1))
print(s1)
print("*" * 50)

# 字节解码为字符串
s2 = bytes.decode(s1,'utf-8')
print(type(s2))
print(s2)
print("*" * 50)


# 使用gbk936编码
# 一个汉字占2个字节
s = u'汉字'
s1 = str.encode(s, 'gbk')
print(type(s))
print(type(s1))
print(s1)
print("*" * 50)

#
s = '好好学习，天天向上。\n好好学习，天天向上。\n好好学习，天天向上。'
print(s)
s1 = str.encode(s, 'utf-8')
print(s1)


