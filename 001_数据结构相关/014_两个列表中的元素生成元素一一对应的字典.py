ret1 = ["link1", "link2", "link3"]
ret2 = ["name1", "name2", "name3"]

for link in ret1:
    item = dict()
    item["link"] = link
    # ret1.index(link)表示当前link在ret1列表中索引的位置
    print(ret1.index(link))
    item["name"] = ret2[ret1.index(link)]
    print(item)


