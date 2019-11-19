import json

data = {"name": "Felix", "age": 20}

# 以写的方式打开，如果没有则新建一个
# 写入的时候写入的是字典文件，不能是字符串
with open('009_json写入读取.json', 'w') as f:
    # 将data的内容写入到json文件中
    # 将字典数据写入到json文件中，写入到json文件中后，就变成字符串了
    json.dump(data, f)


# 以读的方式打开文件
with open('009_json写入读取.json', 'r') as f:
    # 读取json文件中的内容读取为python格式保存在d中
    d = json.load(f)
    print(d)
    print(type(d)) # 读取结果是一个字典，上面写进去之前就是一个字典
