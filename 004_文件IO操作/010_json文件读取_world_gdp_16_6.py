# -*- coding: cp936 -*-
# ��ϸ��P325
# ����JSON�ļ�

import json
import pygal_maps_world.maps
from country_codes import get_country_code
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS


# �����ݼ��ص�һ���б���
filename = '010_world_gdp.json'
with open(filename) as f:
    # ��ȡ�ļ��е����ݣ���ȡ�Ľ��Ϊһ���б��б���ÿһ��Ԫ�ض���һ���ֵ�
    pop_data = json.load(f)
    

# ����һ������ÿ������GDPֵ���ֵ�
world_gdp = {}
for pop_dict in pop_data:
    # ����ݶ�Ӧ��ֵ�Ƿ�Ϊ2016
    if pop_dict['Year'] == 2016:
        country_name = pop_dict['Country Name']
        # ����ԭʼ�����д���С�����Ƚ�����ת��Ϊ��������Ȼ��ת��������
        gdp = int(float(pop_dict['Value']))
        # pygalֻ��ʹ��������ĸ�Ĺ����룬JSON���ṩ����3λ�ģ�����һ���������2λ�Ĺ�����
        code = get_country_code(country_name)
        if code:
            # �����������ڣ�����������Ϊ�����˿�������Ϊֵ���洢���ֵ���
            world_gdp[code] = gdp

# �����˿����������еĹ��ҷ���
cc_pops_1, cc_pops_2, cc_pops_3, cc_pops_4 = {}, {}, {}, {}
for cc, pop in world_gdp.items():
    if pop < 100*100000000:
        cc_pops_1[cc] = pop
    elif pop < 1000*100000000:
        cc_pops_2[cc] = pop
    elif pop < 10000*100000000:
        cc_pops_3[cc] = pop
    else:
        cc_pops_4[cc] = pop

# ����ÿ������������ٸ�����
print(cc_pops_1)
print(cc_pops_2)
print(cc_pops_3)
print(cc_pops_4)
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3), len(cc_pops_4))



wm_style = RS('#336699', base_style=LCS)
wm = pygal_maps_world.maps.World(style=wm_style)

wm.title = 'World Population in 2010, by Country'
wm.add('0-10m', cc_pops_1)
wm.add('10m-100m', cc_pops_2)
wm.add('100m-1bn', cc_pops_3)
wm.add('>1bn', cc_pops_4)

wm.render_to_file('World_GDP.svg')
 

