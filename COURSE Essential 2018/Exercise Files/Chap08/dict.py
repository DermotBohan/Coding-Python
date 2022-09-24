#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    animals = dict(kitten='meow', puppy='ruff!', lion='grrr',
                   giraffe='I am a giraffe!', dragon='rawr')
    for k, v in animal.items():
        print(f'{k}: {v}')

    for k in animals.keys():
        print(k)
    for v in animals.values():
        print(v)
    print_dict(animals)


def print_dict(o):
    for x in o:
        print(f'{x}: {o[x]}')


if __name__ == '__main__':
    main()
