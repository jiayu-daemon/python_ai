#!/usr/bin/env python3
# -*- coding: utf-8 -*-

d = {
    'Michael': 95,
    'Bob': 75,
    'Tracy': 85
}
print('d[\'Michael\'] =', d['Michael'])
print('d[\'Bob\'] =', d['Bob'])
print('d[\'Tracy\'] =', d['Tracy'])
print('d.get(\'Thomas\', -1) =', d.get('Thomas', -1))
d.pop('Bob')
print(d)

"""
由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉
dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value
"""