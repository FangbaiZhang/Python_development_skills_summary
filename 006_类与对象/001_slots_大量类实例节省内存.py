# -*- coding:utf-8 -*-

from player import Player1, Player2
import sys

# 创建两个实例
p1 = Player1('0001', 'Jim')
p2 = Player2('0001', 'Jim')

# p1使用的内存比p2多
# Player2类使用了__slots__可以节省内存
# 比较p1和p2属性的差异，集合取差集
s = set(dir(p1)) - set(dir(p2))
print(s)
print('*' * 50)

# 占用内存的主要是'__dict__'属性，需要占用大量内存
print(p1.__dict__)
print(sys.getsizeof(p1.__dict__))
# 打印结果显示字典占用了112个字节

# __dict__是一个动态字典属性，可以向里面添加属性
p1.__dict__['gender'] = 'girl'
print(p1.__dict__)
print(sys.getsizeof(p1.__dict__))
# 添加属性后，字节变的更大了，占用内存更大

# 因此，为了节约内存，Player2类我们使用slots，去掉__dict__属性
# slots声明了类的属性，相当于将属性提前固定了，后面不能动态添加属性了
