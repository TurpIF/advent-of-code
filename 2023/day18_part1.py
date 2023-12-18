import itertools
import sys
from collections import Counter
from functools import cmp_to_key
from itertools import cycle
from itertools import repeat
from itertools import chain
from heapq import *
from collections import deque

UP = 'U'
DOWN = 'D'
LEFT = 'L'
RIGHT = 'R'

def print_grid(traversed, len_x, len_y, min_x=0, min_y=0):
    for y in range(min_x, len_y):
        line = ''
        for x in range(min_y, len_x):
            if (x, y) in traversed:
                line += '#'
            else:
                line += '.'

        print(line)

def process_all(lines):
    path = set()
    x, y = 0, 0
    path.add((x, y))
    fill = set()

    for line in lines:
        [dir, length, _ ] = line.split()
        length = int(length)
        if dir == UP:
            for dy in range(0, length):
                path.add((x, y - dy - 1))
            y -= length
        if dir == DOWN:
            for dy in range(0, length):
                path.add((x, y + dy + 1))
            y += length
        if dir == LEFT:
            for dx in range(0, length):
                path.add((x - dx - 1, y))
            x -= length
        if dir == RIGHT:
            for dx in range(0, length):
                path.add((x + dx + 1, y))
            x += length

    min_x = min(p[0] for p in path)
    min_y = min(p[1] for p in path)
    len_x = max(p[0] for p in path) + 1
    len_y = max(p[1] for p in path) + 1

    fill = set(path)

    def bfs(neighbours, start, visit):
        visited = set()
        queue = deque([start])

        while queue:
            vertex = queue.popleft()
            visit(vertex)
            if vertex not in visited:
                visited.add(vertex)
                queue.extend(neighbours(vertex))

    def neighbours(vertex):
        x, y = vertex
        candidates = []
        if (x - 1, y) not in path:
            candidates.append((x - 1, y))
        if (x + 1, y) not in path:
            candidates.append((x + 1, y))
        if (x, y - 1) not in path:
            candidates.append((x, y - 1))
        if (x, y + 1) not in path:
            candidates.append((x, y + 1))
        return candidates

    bfs(neighbours, (1, 1), lambda vertex: fill.add(vertex))

    '''for y in range(min_x, len_y):
        is_inside = (min_y, y) in path
        was_empty = False
        for x in range(min_y, len_x):
            if (x, y) in path:
                if is_inside and was_empty:
                    is_inside = False
                else:
                    is_inside = True
            else:
                was_empty = True

            if is_inside:
                fill.add((x, y))'''

    print(path)
    print_grid(path, len_x, len_y, min_x, min_y)
    print()
    print_grid(fill, len_x, len_y, min_x, min_y)

    return len(fill)


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
