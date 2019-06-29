# -*- coding:utf-8 -*-
from functools import total_ordering

@total_ordering
class Rectangle(object):

    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    # < 运算符重载
    def __lt__(self, other):
        print('in__lt__')
        return self.area() < other.area()

    # == 运算符重载
    def __eq__(self, other):
        print('in__eq__')
        return self.area() == other.area()



# 创建两个矩形实例
r1 = Rectangle(2, 8)
r2 = Rectangle(4, 4)

print(r1 < r2)
print('*' * 50)

print(r1 <= r2)
print('*' * 50)

print(r1 > r2)

# 每个运算符都可以重载，但是都写一个方法太麻烦
# @total_ordering类方法可以根据类中定义的
# 小于方法和等于方法自己进行推测


