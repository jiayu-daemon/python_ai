#!/usr/bin/python3

dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])


dict['Age'] = 8;               # 更新 Age
dict['School'] = "菜鸟教程"    # 添加信息

print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])

"""
字典是另一种可变容器模型，且可存储任意类型对象。
字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中 ,格式如下所示
"""