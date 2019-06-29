# -*- coding:utf-8 -*-

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

    # <= 运算符重载
    def __le__(self, other):
        print('in__le__')
        return self.area() <= other.area()



# 创建两个矩形实例
r1 = Rectangle(2, 8)
r2 = Rectangle(4, 4)

print(r1 < r2)
print('*' * 50)

print(r1 <= r2)

# 每个运算符都可以重载，但是都写一个方法太麻烦
# 看006案例

