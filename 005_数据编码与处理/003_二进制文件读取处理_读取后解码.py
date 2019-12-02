# -*- coding:utf-8 -*-
import struct

# 文件读取为字节
f = open('003_二进制编码文件测试.txt', 'rb')
info = f.read()
print(type(info))
print(info)

# 上面讀取的字节转换为字符串
s2 = bytes.decode(info,'utf-8')
print(type(s2))
print(s2)

# 字节编码为字符串
s3 = bytes(s2, 'utf-8')
print(s3)

s4= s2.encode('utf-8')
print(s4)


