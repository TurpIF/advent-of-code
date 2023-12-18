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

UP = '3'
DOWN = '1'
LEFT = '2'
RIGHT = '0'

def process_all(lines):
    poly = []
    x, y = 0, 0
    poly.append((x, y))
    perim = 0

    for line in lines:
        [_, _, hexa] = line.split()
        length = int(hexa[2:2+5], 16)
        dir = hexa[-2]
        print(hexa, length, dir)

        if dir == UP:
            y -= length
        if dir == DOWN:
            y += length
        if dir == LEFT:
            x -= length
        if dir == RIGHT:
            x += length

        perim += length
        poly.append((x, y))

    print(len(poly), perim)

    result = 0
    for p1, p2 in islice(zip(cycle(poly), cycle(poly[1:])), len(poly) - 1):
        print(p1, p2)
        [x1, y1] = p1
        [x2, y2] = p2
        result += x1 * y2 - x2 * y1
    result = (int(abs(result)) >> 1)
    result += (perim >> 1) + 1  # not sure why perimeter should be halved, neither why there is a +1

    return result


input = '''
R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
'''

lines = list(input.splitlines()[1:])

if __name__ == '__main__':
    lines = list(sys.stdin.read().splitlines())

    result = process_all(lines)
    print(result)
