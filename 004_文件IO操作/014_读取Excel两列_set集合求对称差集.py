# -*- coding:utf-8 -*-
import xlrd

# 读取Excel文件，然后添加一列
book = xlrd.open_workbook('014_test.xlsx')
# 读取第一张表,index从0开始
sheet1 = book.sheet_by_index(0)
# 读取总行数
rows = sheet1.nrows
print(rows)

col_1 = []
col_2 = []

for i in range(0, rows):#第0行为表头
    # 循环输出excel表中每一行，即所有数据
    all_data = sheet1.row_values(i)
    # 每一行数据，都放在一个列表，可以切片取出每一列
    # 把第一列和第二列数据分别提取到两个列表中
    col_1.append(all_data[0])
    col_2.append(all_data[1])

# 找出两列中不同且唯一的元素
# 集合求对称差集
a = set(col_1)
b = set(col_2)

c = a ^  b
print(c)









