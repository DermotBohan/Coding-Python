#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

print('Hello, World.'.upper())              # HELLO, WORLD.
print('Hello, World.'.swapcase())           # hELLO, wORLD.
print('Hello, World. {}'.format(42 * 7))    # Hello, World. 294

s = 'Hello, World. {}'
print(s.format(42*7))
print('Hello, World.')


class MyString(str):
    def __str__(self):
        return self[::-1]


s = MyString('Hello, World')
print(s)


print('Hello, World.'.upper())
print('Hello, World.'.lower())
print('Hello, World.'.capitalize())
print('Hello, World.'.title())
print('Hello, World.'.swapcase())
print('Hello, World.'.casefold())
print('Hello, World.')
