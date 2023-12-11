import sys
from collections import Counter
from functools import cmp_to_key
from itertools import cycle
from heapq import *

def process_all(lines):
    ys_without_galaxy = set()
    xs_without_galaxy = set()
    for y, line in enumerate(lines):
        is_row_without_galaxy = True
        for x, c in enumerate(line):
            if c == '#':
                is_row_without_galaxy = False
                break

        if is_row_without_galaxy:
            ys_without_galaxy.add(y)

    for x in range(len(lines[0])):
        is_col_without_galaxy = True
        for y in range(len(lines)):
            c = lines[y][x]
            if c == '#':
                is_col_without_galaxy = False
                break

        if is_col_without_galaxy:
            xs_without_galaxy.add(x)

    galaxies = []
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == '#':
                galaxies.append((x, y))

    def compute_distance(g1, g2):
        d = abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
        for x in range(min(g1[0], g2[0]) + 1, max(g1[0], g2[0])):
            if x in xs_without_galaxy:
                d += 1

        for y in range(min(g1[1], g2[1]) + 1, max(g1[1], g2[1])):
            if y in ys_without_galaxy:
                d += 1
        return d

    print(xs_without_galaxy)
    print(ys_without_galaxy)
    print(galaxies)

    result = 0
    for i, g1 in enumerate(galaxies):
        for g2 in galaxies[i + 1:]:
            distance = compute_distance(g1, g2)
            print(g1, g2, distance)
            result += distance

    result = int(result)
    return result

input = '''
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
'''

lines = list(input.splitlines()[1:])

if __name__ == '__main__':
    lines = list(sys.stdin.read().splitlines())

    result = process_all(lines)
    print(result)
