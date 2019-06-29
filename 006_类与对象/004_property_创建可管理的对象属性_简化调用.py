# -*- coding:utf-8 -*-

from math import pi

# 定义一个圆的类
class Circle(object):

    def __init__(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius

    def setRadius(self, value):
        if not isinstance(value, (int, float)):
            return ValueError('wrong type.')
        self.radius = float(value)

    def getArea(self):
        return self.radius ** 2 * pi

    R = property(getRadius, setRadius)

# 创建一个实例
c = Circle(2)
# 通过方法访问属性
print(c.getRadius())
print(c.getArea())
print('*' * 50)


# 上面访问属性比较繁琐，不够简洁，
# property可以创建可管理的对象属性
# 类最后加上一个属性
# 访问属性R
c = Circle(5.2)
print(c.R)
# 设置属性R
c.R = 6.8
print(c.R)
print('*' * 50)

