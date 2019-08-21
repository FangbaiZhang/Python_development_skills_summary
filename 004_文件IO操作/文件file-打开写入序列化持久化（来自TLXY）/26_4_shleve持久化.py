# 持久化shelve
# shv相当于一个字典
import shelve

shv = shelve.open(r'shv.db')
shv['one'] = 1
shv['two'] = 2
shv['three'] = 3
shv.close()

# 查看项目文件夹创建了三个shv文件，实际是个数据库

# 读取shelve案例
shv = shelve.open(r'shv.db')
try:
    print(shv['one'])
    print(shv['two'])
    print(shv['five'])
except Exception as e:
    print("没有这个元素")
finally:
    shv.close()