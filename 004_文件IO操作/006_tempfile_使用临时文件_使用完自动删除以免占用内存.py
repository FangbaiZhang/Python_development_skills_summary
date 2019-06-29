# -*- coding:utf-8 -*-

from tempfile import TemporaryFile, NamedTemporaryFile

# 临时文件，程序关闭后临时文件会自动删除
# 如果不想删除，可以传入delete=False

# 创建一个实例
f = TemporaryFile(mode='w+b')
# 查看临时文件在系统磁盘中存储位置
print(f.name)
print('*' * 50)

# 临时文件中写入内容，以字节写入
f.write(b'Hello world!' * 10000)

# 读取文件之前，先将指针调到文件开头
f.seek(0)

# 每次读取100个字节
r1 = f.read(100)
print(r1)
print('*' * 50)
r2 = f.read(100)
print(r2)
print('*' * 50)


# NamedTemporaryFile与上面功能类似
f = NamedTemporaryFile()
print(f.name)
