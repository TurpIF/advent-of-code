import itertools
import sys
from collections import Counter
from functools import cmp_to_key
from itertools import cycle
from itertools import repeat
from itertools import chain
from heapq import *

def process_pattern(lines):
    print(lines)

    x_len = len(lines[0])
    y_len = len(lines)

    for x in range(1, x_len):
        x_pivot = min(x, abs(x - x_len))
        # print(x_pivot, x)

        is_symmetric = True
        for y in range(y_len):
            x_left = lines[y][x - x_pivot:x]
            x_right = lines[y][x: x + x_pivot]

            if x_left != x_right[::-1]:
                is_symmetric = False
                break

        if is_symmetric:
            return x

    for y in range(1, y_len):
        y_pivot = min(y, abs(y - y_len))
        # print(y_pivot, y)

        is_symmetric = True
        for x in range(x_len):
            y_above = ''.join(lines[new_y][x] for new_y in range(y - y_pivot, y))
            y_below = ''.join(lines[new_y][x] for new_y in range(y, y + y_pivot))

            if y_above != y_below[::-1]:
                is_symmetric = False
                break

        if is_symmetric:
            return 100 * y

    return 0

def process_all(lines):
    result = 0
    last_i = 0
    for i, line in enumerate(lines):
        if not line:
            result += process_pattern(lines[last_i:i])
            last_i = i + 1

    result += process_pattern(lines[last_i:])
    return result


input = '''
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
'''

lines = list(input.splitlines()[1:])

if __name__ == '__main__':
    lines = list(sys.stdin.read().splitlines())

    result = process_all(lines)
    print(result)
