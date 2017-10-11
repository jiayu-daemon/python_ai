#!/usr/bin/python3
# callable.py

class Car(object):
    def setName(self, name):
        self.name = name    


def fun():
    pass


c = Car()
print(callable(fun))
print(callable(c.setName))
print(callable([]))
print(callable(1))