# -*- coding:utf-8 -*-

import xlrd

# 读取Excel文件，然后添加一列
book = xlrd.open_workbook('012_学生成绩表.xlsx')

# 返回里面的sheets表,表中只有2个表，返回两个对象
sheets = book.sheets()
print(sheets)
print('*' * 50)

# 读取第一张表,index从0开始
sheet1 = book.sheet_by_index(0)
# 读取行列数
rows = sheet1.nrows
print(rows)
columns = sheet1.ncols
print(columns)
print('*' * 50)

# 访问某行某列
print(sheet1.cell(0,0))
print(sheet1.cell(0,1))
print(sheet1.cell(1,0))
print(sheet1.cell(1,1))
print('*' * 50)

# 访问某行, 某列
print(sheet1.row(1))
print(sheet1.col(1))
print('*' * 50)