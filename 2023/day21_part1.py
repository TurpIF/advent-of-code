import itertools
import sys
from collections import Counter
from functools import cmp_to_key
from itertools import cycle
from itertools import repeat
from itertools import chain
from itertools import islice
from heapq import *
from collections import deque
from collections import defaultdict

def process_all(lines):
    def print_grid(traversed, len_x, len_y):
        for y in range(len_y):
            line = ''
            for x in range(len_x):
                if (x, y) in traversed:
                    line += 'O'
                else:
                    line += lines[y][x]

            print(line)

    def is_walkable(x, y):
        if not (0 <= x < len(lines[0]) and 0 <= y < len(lines)):
            return False

        return lines[y][x] == '.' or lines[y][x] == 'S'
    def neighbours(args):
        x, y = args
        candidates = [
            (x - 1, y),
            (x + 1, y),
            (x, y - 1),
            (x, y + 1)
        ]

        return [(1, c) for c in candidates if is_walkable(c[0], c[1])]

    init_point = None
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == 'S':
                init_point = x, y

    traversed = set()
    previous_traversed = set()
    previous_traversed.add(init_point)
    for s in range(64):
        traversed = set()

        for p in previous_traversed:
            for n in neighbours(p):
                traversed.add(n[1])

        previous_traversed = traversed
        #print_grid(traversed, len(lines[0]), len(lines))
        #print()

    # print_grid(traversed, len(lines[0]), len(lines))

    return len(traversed)

input = '''
...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
'''

lines = list(input.splitlines()[1:])

if __name__ == '__main__':
    lines = list(sys.stdin.read().splitlines())

    result = process_all(lines)
    print(result)
