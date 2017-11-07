#!/usr/bin/python
# -*- coding:UTF-8 -*-

#求绝对值的函数
x = abs(-10)
print(x)
#把函数本身赋值给变量呢？
f = abs
print(f(-10))
#既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
def add(x,y,f):
	return f(x) + f(y)

print(add(-5,6,abs))

#偏函数,python的functools模块，其中一个就是偏函数。
#要注意，这里的偏函数和数学意义上的偏函数不一样
print (int('12345',base=8))
print (int('123',16))

import functools
int2 = functools.partial(int , base=2)
print (int2('1010101'))