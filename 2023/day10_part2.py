import sys
from collections import Counter
from functools import cmp_to_key
from itertools import cycle
from heapq import *

def process_all(lines):
    def get_cell(x, y):
        print(x, y)
        if -1 <= x < 0 and -1 <= y <= len(lines):
            return '.'
        if -1 <= y < 0 and -1 <= x <= len(lines[0]):
            return '.'
        if len(lines[0]) - 1 < x <= len(lines[0]) and -1 <= y <= len(lines):
            return '.'
        if len(lines) - 1 < y <= len(lines) and -1 <= x <= len(lines[0]):
            return '.'
        if x < 0 or x >= len(lines[0]):
            return '#'
        if y < 0 or y >= len(lines):
            return '#'
        if x != int(x) or y != int(y):
            return '~'

        return lines[int(y)][int(x)]

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
    parents = {}
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
                    parents[neighbour] = item
            else:
                distances[neighbour] = neighbour_distance
                heappush(queue, (neighbour_distance, neighbour))
                parents[neighbour] = item

            if distances[neighbour] > 1 and neighbour == start_position:
                break

    path = []
    max_position = start_position
    max_distance = max(distances.values())
    for position, distance in distances.items():
        if distance == max_distance:
            path.append(position)
            x = position
            max_position = position
            while x != start_position:
                x = parents[x]
                path.insert(0, x)
            break

    for position in get_neighbours(*max_position):
        if position not in path:
            path.append(position)
            x = position
            while x != start_position:
                x = parents[x]
                path.insert(0, x)

    print(path)
    print(distances)
    print(parents)

    def is_horizontally_connected(left, right):
        if left in ['-', 'L', 'F', 'S'] and right in ['-', 'J', '7', 'S']:
            return True
        return False

    def is_vertically_connected(top, down):
        if top in ['|', '7', 'F', 'S'] and down in ['|', 'L', 'J', 'S']:
            return True
        return False

    def get_other_neighbours(x, y):
        candidates = []

        if x != int(x) and y != int(y):
            cell_ul = get_cell(x - 0.5, y - 0.5)
            cell_ur = get_cell(x + 0.5, y - 0.5)
            cell_dl = get_cell(x - 0.5, y + 0.5)
            cell_dr = get_cell(x + 0.5, y + 0.5)

            if cell_ul == '.' or cell_ur == '.' or not is_horizontally_connected(cell_ul, cell_ur):
                candidates.append((x, y - 0.5))
            if cell_dl == '.' or cell_dr == '.' or not is_horizontally_connected(cell_dl, cell_dr):
                candidates.append((x, y + 0.5))
            if cell_ul == '.' or cell_dl == '.' or not is_vertically_connected(cell_ul, cell_dl):
                candidates.append((x - 0.5, y))
            if cell_ur == '.' or cell_dr == '.' or not is_vertically_connected(cell_ur, cell_dr):
                candidates.append((x + 0.5, y))

        if x == int(x) and y != int(y):
            if get_cell(x, y - 0.5) == '.' or not (x, int(y - 0.5)) in path:
                candidates.append((x, y - 0.5))
            if get_cell(x, y + 0.5) == '.' or not (x, int(y + 0.5)) in path:
                candidates.append((x, y + 0.5))

            candidates.append((x - 0.5, y))
            candidates.append((x + 0.5, y))

        if x != int(x) and y == int(y):
            if get_cell(x - 0.5, y) == '.' or not (int(x - 0.5), y) in path:
                candidates.append((x - 0.5, y))
            if get_cell(x + 0.5, y) == '.' or not (int(x + 0.5), y) in path:
                candidates.append((x + 0.5, y))

            candidates.append((x, y - 0.5))
            candidates.append((x, y + 0.5))

        if x == int(x) and y == int(y):
            candidates.append((x - 0.5, y))
            candidates.append((x + 0.5, y))
            candidates.append((x, y - 0.5))
            candidates.append((x, y + 0.5))

        return [c for c in candidates if get_cell(*c) != '#']

    visited = set()
    start_position = (0.0, 0.0)
    visited.add(start_position)
    queue = []
    queue.append(start_position)
    parents = {}
    while queue:
        item = queue.pop()
        neighbours = get_other_neighbours(*item)

        for neighbour in neighbours:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
                parents[neighbour] = item

    outside_positions = list(visited)
    print()
    print('outside_positions', outside_positions)
    print()

    result = max(distances.values())
    OKGREEN = '\033[92m'
    OKBLUE = '\033[94m'
    OKRED = '\033[91m'
    ENDC = '\033[0m'

    result = 0
    for y, line in enumerate(lines):
        s = ''
        for x, c in enumerate(line):
            if c == 'S':
                s += OKGREEN + c + ENDC
            elif (x, y) in path:
                s += OKBLUE + c + ENDC
            elif (x, y) in outside_positions:
                s += OKRED + c + ENDC
            elif c == '.':
                s += c
                result += 1
            else:
                s += c
                result += 1

        print(s)

    return result

input = '''
.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...
'''

lines = list(input.splitlines()[1:])

if __name__ == '__main__':
    lines = list(sys.stdin.read().splitlines())

    result = process_all(lines)
    print(result)
