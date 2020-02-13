# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
WeiXin: AXiaShuBai
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2020/2/13 14:46
Desc:
'''

# pycharm文件夹有个mark down as ---> sources root
# 标记后为深蓝色，意思为标记为系统路径

# 未标记的普通文件夹，不同文件夹之间导入模块
# 需要使用from 文件夹名 import py文件名，即使同一个文件夹中导入另外一个py文件，也要写上文件夹名称
# 文件路径也都要写上比如：
# from nCov_data_analysis.china_data_analysis import ChinaData
# from nCov_data_analysis import a_get_html
# src="../echarts/dist/echarts.min.js"

# 如果标记为系统路径，所有模块都加入到系统路径，可以直接导入模块py文件
# import a_get_html

# 具体参考wuhan_2019-nCoV项目文件夹中的
# nCov_basemap_visualization、nCov_data_analysis、nCov_ECharts_map_visualization
# 三个文件夹中的导入，一般不要标记，使用完整写法，方便查找查看引用的模块