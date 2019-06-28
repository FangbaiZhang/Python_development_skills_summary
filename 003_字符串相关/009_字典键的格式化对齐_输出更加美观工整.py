# -*- coding:utf-8 -*-

d = {
    'faffa': 254,
    'tha': 12.01,
    'Dicgta': 25854,
    'Thgh': 5878,
    'faattga33': 689
}

# 先找出键中最长的键，使用map函数，传入len和所有的键
# 得到键的可迭代对象，然后取最大值
print(list(map(len, d.keys())))
m = max(map(len, d.keys()))
print(m)

# 调整每个键，进行左对齐，并调整宽度，空格补全
d_new = {}
for k, v in d.items():
    # 键左对齐，调整宽度
    k1 = k.ljust(m)
    print(k1 + ':')
    d1 = {k1: v}
    # 左对齐后的字典添加到新字典中
    d_new.update(d1)

print(d_new)



