import sys
from collections import Counter
from functools import cmp_to_key
from itertools import cycle
from heapq import *

def process_all(lines):
    def get_cell(x, y):
        if x < 0 or x >= len(lines[0]):
            return '.'
        if y < 0 or y >= len(lines):
            return '.'

        return lines[y][x]

    def get_neighbours(x, y):
        cell = lines[y][x]
        candidates = []
        if cell == 'S':
            if get_cell(x, y - 1) in ['S', '|', '7', 'F']:
                candidates.append((x, y - 1))
            if get_cell(x, y + 1) in ['S', '|', 'L', 'J']:
                candidates.append((x, y + 1))
            if get_cell(x - 1, y) in ['S', '-', 'L', 'F']:
                candidates.append((x - 1, y))
            if get_cell(x + 1, y) in ['S', '-', 'J', '7']:
                candidates.append((x + 1, y))
        elif cell == '|':
            if get_cell(x, y - 1) in ['S', '|', '7', 'F']:
                candidates.append((x, y - 1))
            if get_cell(x, y + 1) in ['S', '|', 'L', 'J']:
                candidates.append((x, y + 1))
        elif cell == '-':
            if get_cell(x - 1, y) in ['S', '-', 'L', 'F']:
                candidates.append((x - 1, y))
            if get_cell(x + 1, y) in ['S', '-', 'J', '7']:
                candidates.append((x + 1, y))
        elif cell == 'L':
            if get_cell(x, y - 1) in ['S', '|', '7', 'F']:
                candidates.append((x, y - 1))
            if get_cell(x + 1, y) in ['S', '-', 'J', '7']:
                candidates.append((x + 1, y))
        elif cell == 'J':
            if get_cell(x, y - 1) in ['S', '|', '7', 'F']:
                candidates.append((x, y - 1))
            if get_cell(x - 1, y) in ['S', '-', 'L', 'F']:
                candidates.append((x - 1, y))
        elif cell == '7':
            if get_cell(x, y + 1) in ['S', '|', 'L', 'J']:
                candidates.append((x, y + 1))
            if get_cell(x - 1, y) in ['S', '-', 'L', 'F']:
                candidates.append((x - 1, y))
        elif cell == 'F':
            if get_cell(x, y + 1) in ['S', '|', 'L', 'J']:
                candidates.append((x, y + 1))
            if get_cell(x + 1, y) in ['S', '-', 'J', '7']:
                candidates.append((x + 1, y))

        return candidates

    start_position = (0, 0)

    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == 'S':
                start_position = (x, y)

    print(start_position)

    queue = []
    visited = set()
    distances = {}
    queue.append((0, start_position))
    distances[start_position] = 0
    while queue:
        distance, item = heappop(queue)
        neighbours = get_neighbours(*item)
        print(neighbours)

        for neighbour in neighbours:
            neighbour_distance = distance + 1
            if neighbour in distances:
                current_distance = distances[neighbour]
                if neighbour_distance < current_distance:
                    distances[neighbour] = neighbour_distance
                    heappush(queue, (neighbour_distance, neighbour))
                    # potentially update a parent link
            else:
                distances[neighbour] = neighbour_distance
                heappush(queue, (neighbour_distance, neighbour))

            if distances[neighbour] > 1 and get_cell(*neighbour) == 'S':
                break

    print(distances)
    result = max(distances.values())
    return result

input = '''
-L|F7
7S-7|
L|7||
-L-J|
L|-JF
'''

lines = list(input.splitlines()[1:])

if __name__ == '__main__':
    lines = list(sys.stdin.read().splitlines())

    result = process_all(lines)
    print(result)
