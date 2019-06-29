# -*- coding:utf-8 -*-

# python中默认的缓冲区(全缓冲)是4096字节
# buffering可以设置缓冲字节大小，当写入的数据超过设置值，才会写入到文件中
f = open('001_测试缓冲案例文件.txt', 'w', buffering=2048)
# 写入3个字节，打开txt文件为空
f.write('abc')
# 写入2045个字节，总共2048个，还是为空
f.write('+' * 2044)
# 在写入一个字节，就由缓冲存储到磁盘了


# 行缓冲： buffering=1
# f = open('001_测试缓冲案例文件.txt', 'w', buffering=1)
# f.write('abc')
# 只要遇到换行符，就将缓存存到磁盘
# f.write('\n')

# 无缓冲：buffering=0
# 写入数据就直接存储到磁盘