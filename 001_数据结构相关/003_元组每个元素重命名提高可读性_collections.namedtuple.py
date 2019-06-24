# -*- coding:utf-8 -*-

# 普通元组：
student1 = ('Jim', 20, 'male', '4557922@qq.com')
student2 = ('Alex', 22, 'male', '5548822@qq.com')
# 访问每个学生的属性不方便

# 可以使用namedtuple函数给每个元组的元素添加一个关键字作为属性
from collections import namedtuple
Student = namedtuple('Student', ['name', 'age', 'sex', 'email'])
student3 = Student('Jim', 20, 'male', '4557922@qq.com')
print(student3)
# 访问元素可以直接使用句点法，.属性
print(student3.name)
print(student3.age)

