# 爬取的字符串存储到json文件中时候，里面会有Unicode编码，\ue768这样子
#
# 查阅资料发现，json.dumps有一个默认参数。ensure_ascii =true,  它会将不是ascii字符的转义为json字符串。
#
# 如果是false ,不是ascii字符的会包含在里面，即如果是中文就会保存中文。
#
# 参考TZKT项目中P09_requests_xml_xpath_json.dumps_糗事百科爬虫

#         with open("./糗事百科.json", "a", encoding="utf-8") as f:
#             for content in content_list:
#                 # ensure_ascii是false,不是ascii字符的会包含在里面，即如果是中文就会保存中文
#                 f.write(json.dumps(content, ensure_ascii=False) + "\n")
#             print("第%s页保存成功" % page_num)
