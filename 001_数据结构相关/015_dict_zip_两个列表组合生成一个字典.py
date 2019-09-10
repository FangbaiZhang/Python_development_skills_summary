# zip函数用于打包元素
# >>>a = [1,2,3]
# >>> b = [4,5,6]
# >>> zipped = zip(a,b)  打包为元组的列表
# [(1, 4), (2, 5), (3, 6)]


# 1 构建字典的 2 个列表相同
a = [1, 2, 3, 4]
b = ['ab', 'ac', 'ad']
d1 = dict(zip(a, b))
print(d1)
# {1: 'ab', 2: 'ac', 3: 'ad'}


# 2 构建字典的 2 个列表不同（key比value多）
#

a = [1, 2, 3, 4]
c = ['aa', 'ss']
d2 = dict(zip(a, c))
print(d2)
# {1: 'aa', 2: 'ss'}


# 3 构建字典的 2 个列表不同（key比value少）
a = [1, 2, 3, 4]
d = ['fa', 'fb', 'fc', 'fd', 'fe']
d3 = dict(zip(a, d))
print(d3)
# {1: 'fa', 2: 'fb', 3: 'fc', 4: 'fd'}
