#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    game = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
    print_list(game)
    print(game[1:3])
    i = game.index('Paper')
    print(game[i])
    print(f"i is equal to: {i}")
    game.append('Computer')
    game.insert(0, 'Computer')
    game.remove('Paper')

    game.pop()
    x = game.pop(3)

    del game[1:3]

    del game[1:5:2]

    print(', '.join(game))
    print(x)
    print(len(game))
    print_list(game)


def print_list(o):
    for i in o:
        print(i, end=' ', flush=True)
    print()


if __name__ == '__main__':
    main()
