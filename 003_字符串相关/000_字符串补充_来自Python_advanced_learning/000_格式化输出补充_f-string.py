# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2019/11/30 16:29
Desc:
'''

username = 'tom'
action = 'payment'

# %s
message = 'User %s has logged in and did an action %s.' % (username, action)
print(message)

# format
message = 'User {} has logged in and did an action {}.'.format(username, action)
print(message)

# f-string
message = f'User {username} has logged in and did an action {action}.'
print(message)

res= f"{2 * 3}"
print(res)
# 6

comedian = {'name': 'Tom', 'age': 20}
res1 = f"The comedian is {comedian['name']}, aged {comedian['age']}."
print(res1)
# 'The comedian is Tom, aged 20.'