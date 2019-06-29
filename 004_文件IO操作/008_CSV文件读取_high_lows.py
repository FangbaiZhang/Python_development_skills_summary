# -*- coding: cp936 -*-
# ��ϸ��P313
# ����CSV�ļ�

import csv
from datetime import datetime
from matplotlib import pyplot as plt


filename = '008_sitka_weather_07-2014.csv'
with open(filename) as f:
    
    # ��ȡ�����ļ�������
    reader = csv.reader(f)
    
    # ��ȡ�ļ��ĵ�һ������
    header_row = next(reader)
    print(header_row)
    print("\n")
    
    # ��ӡ�ļ�ͷ����λ�ã������ǵڼ��У������Ӧ������
    for index, column_header in enumerate(header_row):
        print(index, column_header)
    print("\n")
    
    # ���������ʾ��ȡ�ļ��е�������£����������ʾ����0��Ϊ���ڣ���һ��Ϊ�������    
    highs = []
    for row in reader: # �ӵ�2�п�ʼ����ÿһ�У���Ϊ��һ��ǰ���Ѿ�����next��ȡ��
        high = int(row[1])
        highs.append(high)  # ��ÿ�е�����1�������ݣ�ʵ��Ϊ���ĵڶ������������ӵ��б���
    print(highs)
    print("\n")

# ��������������ݻ���ͼ��
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(highs, c='red')

# ����ͼ�εĸ�ʽ
plt.title("Daily high temperature, July 2014")
plt.xlabel("Date", fontsize=16)
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis='both', which='which', labelsize=8)

plt.show()
            

