#!/usr/bin/python3
# attr.py


def fun(): 
    pass


print(hasattr(object, '__doc__'))
print(hasattr(fun, '__doc__'))
print(hasattr(fun, '__call__'))

print(getattr(object, '__doc__'))
print(getattr(fun, '__doc__'))

