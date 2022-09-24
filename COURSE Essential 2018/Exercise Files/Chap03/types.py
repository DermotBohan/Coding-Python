#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = (1, 'two', 3.0, [4, 'four'], 5)
y = (1, 'two', 3.0, [4, 'four'], 5)
# print('x is {}'.format(x))
print(type(x))
print(type(y))

print(id(x))
print(id(y))

if x[0] is y[0]:
    print("same")
else:
    print("Not the same")
