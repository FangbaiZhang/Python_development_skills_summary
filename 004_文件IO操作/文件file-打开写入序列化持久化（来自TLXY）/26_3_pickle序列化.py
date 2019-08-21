# pickle序列化实例

import pickle

age = 19

with open('test02.txt', 'wb') as f:
    pickle.dump(age, f)

# 反序列化，读取文件
with open('test02.txt', 'rb') as f:
    age = pickle.load(f)
    print(age)


# 序列化写入一个列表
a = [20, 'Felix', 'Zhang']

with open('test03.txt', 'wb') as f:
    pickle.dump(a, f)

# 反序列化，读取文件
with open('test03.txt', 'rb') as f:
    a = pickle.load(f)
    print(a)


