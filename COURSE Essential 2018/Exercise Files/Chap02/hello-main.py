#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import platform


def main():     # function declaration
    message()   # function definition


def message():
    print('This is python version {}'.format(platform.python_version()))
    if True:
        print('This is true')
    else:
        print('This is not true')


if __name__ == '__main__':
    main()
