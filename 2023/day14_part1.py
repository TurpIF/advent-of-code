import itertools
import sys
from collections import Counter
from functools import cmp_to_key
from itertools import cycle
from itertools import repeat
from itertools import chain
from heapq import *

def transpose(l):
    return list(map(list, zip(*l)))
def process_all(lines):
    lines = transpose(lines)

    result = 0
    for line in lines:
        load = 0
        potential_load = len(line)
        print(''.join(line))

        for i, c in enumerate(line):
            if c == 'O':
                load += potential_load
                potential_load -= 1
            if c == '#':
                potential_load = len(line) - i -1

        print(load)
        result += load

    return result


input = '''
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
'''

lines = list(input.splitlines()[1:])

if __name__ == '__main__':
    lines = list(sys.stdin.read().splitlines())

    result = process_all(lines)
    print(result)
