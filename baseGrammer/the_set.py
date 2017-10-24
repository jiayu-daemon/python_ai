#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s1 = set([1, 1, 2, 2, 3, 3])
#s1.add(4)
s1.remove(1)
print(s1)
s2 = set([2, 3, 4])
print(s2)
print(s1 & s2)
print(s1 | s2)