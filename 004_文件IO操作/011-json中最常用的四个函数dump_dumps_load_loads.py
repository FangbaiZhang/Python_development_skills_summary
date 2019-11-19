import json

# json文件数据，表面看是一个字典，实际类型是一个字符串
# 使用dumps和loads就可以进行字典和json格式字符串相互转换

# json.dumps()函数的使用，将字典类型数据转化为json格式的字符串
# 可以直接使用dump将python字典数据写入到json文件中，读取出来还是一个字典
dict = {"age": "12"}
json_info = json.dumps(dict)
print("dict的类型："+str(type(dict)))
print("通过json.dumps()函数处理之后：")
print("json_info的类型："+str(type(json_info)))
print("*" * 100)


# json.loads()函数的使用，将json格式的字符串转化为字典
# json_info数据是一个字符串，json数据实际是一个字符串
json_info = '{"age": "12"}'
dict1 = json.loads(json_info)
print("json_info的类型："+str(type(json_info)))
print("通过json.loads()函数处理：")
print("dict1的类型："+str(type(dict1)))