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

def reverse(l):
    return list(map(lambda x: x[::-1], l))

def apply_gravity(lines):
    new_lines = []
    for line in lines:
        ground = 0
        new_line = ['.' for _ in range(len(line))]

        for i, c in enumerate(line):
            if c == 'O':
                new_line[ground] = 'O'
                ground += 1
            if c == '#':
                new_line[i] = '#'
                ground = i + 1
        new_lines.append(new_line)
    return new_lines

def print_grid(lines):
    for line in lines:
        print(''.join(line))
    print()

class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}
    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]

@Memoize
def tilt_sequence(lines):
    # north, west, source, east
    lines = transpose(transpose(lines.split('\n')))

    #north
    for x in range(len(lines[0])):
        ground = 0
        for y in range(len(lines)):
            c = lines[y][x]
            if c == 'O':
                lines[ground][x] = 'O'
                if y != ground:
                    lines[y][x] = '.'
                ground += 1
            if c == '#':
                ground = y + 1

    # lines = transpose(lines)
    # lines = apply_gravity(lines)

    #print('after north')
    #print_grid(lines)

    # west
    for y in range(len(lines)):
        ground = 0
        for x in range(len(lines[0])):
            c = lines[y][x]
            if c == 'O':
                lines[y][ground] = 'O'
                if x != ground:
                    lines[y][x] = '.'
                ground += 1
            if c == '#':
                ground = x + 1

    #lines = transpose(lines)
    #lines = apply_gravity(lines)

    #print('after west')
    #print_grid(lines)

    # south
    for x in range(len(lines[0])):
        ground = len(lines[0]) - 1
        for y in reversed(range(len(lines))):
            c = lines[y][x]
            if c == 'O':
                lines[ground][x] = 'O'
                if y != ground:
                    lines[y][x] = '.'
                ground -= 1
            if c == '#':
                ground = y - 1

    #lines = reverse(transpose(lines))
    #lines = apply_gravity(lines)

    #print('after south')
    #print_grid(lines)

    # east
    for y in range(len(lines)):
        ground = len(lines) - 1
        for x in reversed(range(len(lines[0]))):
            c = lines[y][x]
            if c == 'O':
                lines[y][ground] = 'O'
                if x != ground:
                    lines[y][x] = '.'
                ground -= 1
            if c == '#':
                ground = x - 1
    # lines = reverse(transpose(reverse(lines)))
    # lines = apply_gravity(lines)

    #print('after east')
    #print_grid(lines)

    # lines = lines

    #print('after all')
    #print_grid(lines)
    return '\n'.join(''.join(c for c in line) for line in lines)

def process_all(lines):
    # Computing the prepared lines below
    lines = '\n'.join(line for line in lines)
    # lines = transpose(transpose(lines))
    for i in range(1000000000):
        if i % 100000000 == 0:
            print(i)
            print(lines)
            print()
            # print_grid(lines)
        lines = tilt_sequence(lines)

    print(lines)
    # print_grid(lines)

    lines = transpose(lines.split('\n'))

    # return 0
    # lines = transpose(lines)

    result = 0
    for line in lines:
        load = 0

        for i, c in enumerate(line):
            if c == 'O':
                load += len(lines) - i

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

prepared_input = '''
.....#....
....#...O#
.....##...
...#......
.....OOO#.
.O#...O#.#
....O#...O
......OOOO
#....###.O
#.OOO#..OO
'''

prepared_long_input = '''
.......O#...........OOO#...#...OO#...........O#......O#.##..#....O#........OO#..........#........OOO
.....OO#..#..O#.#...........##...........OOOO#...............OO#...OO#O#...........OOO#..O#.......OO
....OO#.OO#.OO#......O#.......#...##..#...O##..........OOOOO#...OO##.O#..#.......##......#.O#.....O#
...O#...##..O#....#.........#..........OOO#..OOOO#.......O#....OOO#...........OOO##..#....#..#..O#.#
#.........O#........OO#...O#......O#.#.O#..O#........OOOOOO#.##....#....................OO#.O#.#...#
...##...#...O##.#.......#.#..#.......O#..OO#..OOO#...........OOOOO##...O#..#................#..#....
..........#.......................OOOOOO#...O#.#..O#O##........OO##.......................OOO#...#..
...#......#...OO#.#..O#.......#..O#..........OOO#..#..O#..#.......O##.......O#.#..#.........#....#..
...##.##.....OOO#..#..........##..#.#............OOOOOO#.......#..#.......................OOOOOO#..#
....#......#......................OOO#.OO#O#..O#...................OOOOO#....O##....####.#..#......O
..........O##..OOO#.....##..........#...OO#....................OOOOOOOO#...#...OO##..........#......
....#.O#..O#..........................OOOOOOOOOOOOO###...OOO#......#..OO#...#.#.##.................O
......O#O##.O#...OOO#...#.......O#.#..#O#..#.#.......OOOOOO#.....#.O#.....OO#............O#.......OO
.....#....O#...O##...#........#.#......OOO#...#.....OO##.........O#..#....#..#.###.....O#..O#.....#.
....##..#...........OO#..........#....O#.............OO#...OO#.#.#.O#.......#.#.....#..............O
..........#....#.#.O##.....OO#....#....#....OOO#.....O##........OO#.......................O##....O#.
.....OOO#.##.......#..OO#.....................OOOOOOO#..#.......................OO#........OO#..##..
OOO#.......OO#..##.#..OOO#.#............##.#.#...O##......OOOO#...........OO#.#....O#....#.#.....#..
.OOO#..O#.......#...O#.#.........OOO#............OOOO##.##O####....O#.O#..................O#........
OO#.#.........O#....#...#.....O#..#O#.OO#....OOOOO###.....#...#....##.O#.........................OOO
....OOOO#................O##....O##O#O#.#...OOO####.#...#....#...O#..#.....O#........OOO#.......OOOO
.OO#..##...............OO#.#......O#.#....OO#..O#..#...####.#...........OOOO#.....O##.O#...O#...O##O
O##...........OOOO#..#...#......O#...#..#..OO#.....#....#.....#...O#......O#...#...#.O#.#........OO#
..O#.....O##..O#.#.........OO#..........O##....#......#.....OO#......OOOO#O#...#..#........OO##..O#.
..............OOOOO##..#...#.....O#......................OO#.#.O#..O#..#.O#.#......#..........O#.#.#
...OOOO#....##...O#......#.................OOOO#.....#..#.O#.............................OOOOOO#..OO
O#.#...........OOOO#................O####..O#............#.....OO#..#..O##.#.....#.....OOOO#...##..O
.......OOOO#..#.O#.......#...........O#.#......O#.O#.........O#.........OOO#........O##...O#.....#.#
...OO#.....O##..#...................OOOOO#.##.O#.#.....#.#.#...........OOOO#....O#......O#.....#....
.OO#.........OOOO#..........OOOOOO#.........O#......##.......OO#.......OO#......#...#...............
OOO#O#....OOO##.#.###...#..O#.#...................OO#.#......#..#.....O#...O#......................#
O##..OOOOOO#.##..........O#..........OO#.............OO#.......#....OO####.....O#...#........O#.....
O#.#.OO#OO#...OO#........#.......O#.....OO#...OOO#..............OOO#.#..#.#...#.................O#..
.O#.#...OOO#..#......OO#.....#........OOO#..OO##...OO#.#......#....O#..#.............OO#.#......#..O
.....O#.#.....OOO#.....................OOOO##..####...#..........#.#....#..........#........O#....OO
#...#....#..................OOOOOO#........OOO#...#......#....................O##.....#.........O##.
#.........#..#..O#..##.#.##...O#......OOOO#......O#............O#........#.##O#.......O#.#.......O#.
......O#..#...##...............OOOOO#..........OO##.......OOO#......#O##......OO#..O#..........OO#..
.....O#...#..............OOO#...O#...O#.#.....#....O#.....O##...#..#..OO#....#.O#..O#.#...O#......OO
..O#....#.#.......OOO#...O##......O#............OO#...#..###....#...##..#......#.........O#.#.#..#O#
#...........OOOOO#...OOO##....O#..........O#....#.#.....#.#.....#..............OO#....#...#..#..#.#.
##.....OO#.....#....OOOOOOO#.........OOOO#....#...................O#.....O#.............O#..#...#...
##O#.#.........O##O##.#...#....OOOOO#................O#...O##..#......O#..O###.....#..#..OOO##......
....O#........O#.#......OO###..O#....OO#...#......OOO#.#.#...#.....OO#...##..#.........#...OO#.....O
..#...O#..#....#....OOO#....OO#..O#....#.....#..#............O#..#...................OOO#........OOO
..####.........#.O#O#OO#.#....OO#..O#.#..##..##.............OO#................OO#.......O#......OOO
..#...........OO#.##......OOO#..#...........O#.OO#..........O#...#..#......#....#...O#......O###..OO
..#.#.......OO#...#.OO#..#......O#...OO#.....O#.O#........#........O#.....#.............OO#......OO#
....O#......O#....O#.............OOO#..............OOOO#...........#......O#.#...#..O#.....O#......O
.O#..........OOOOOO#....O##......#.......OOO#...........O##........OOOOO#........O#..#..###...O#...O
........OO#..O#O#...O#...#.............OOOOO#.O#.......#.#....OO#..O#....#....OO#....##.......#..#..
OO#......O#..O##................OOOOOO#...OO#.#.........OOO#...#..O#....#..O#......O#....O#...O#...#
##.#........OO##..............OOOOOOOOOOO#............OO#....................OOOOO#.#...#..OOO##....
......OOOO#.....O#..O#...OOOO#.#..#.......OOOO#....O#.###.#...O#..#.......O##OOO#.........#.......OO
.#..O#.....OOOO#....OOO#.#.......OOO#O##......O#............#....OO#..#....#.##...........OOO#.....O
....OOO#..O#.#..OOO#.OO#..#OO#.....OOO#.#..................OO#.#O#....#.#...#..#.OO#.....O#.......OO
....OO#........OO##..O#....OO#....OOO#.....O#...........O#.#....#...........#O#...OO#....O#......OO#
.O#....O#............OOOO#.O#....OOOO#.#...........OOO#............O#.......O#..#.O#O#....#......OOO
...O##.........OOOOOO#.....OOOOO##........OOOO#..........O#.#......#......O#.....OOO#...........OOOO
OO#.......OOOO#.#...##..OO#.....OOOOO#...OOO#.....OOO#....O#.#........OOOO#.#..OO#...#.....OO##.#...
......................OOOOOOOOOOOOOOOOO#O#....OOO#.O#......OOOO##....OO#....OOO#..O#........OOOO#...
.OOO#.O#.#...OO#......#.O#O#.#O#...............OOOOOOO#.OO##.O#...#...OOO#..O###....O#.......OO#...#
###....OO#.#.O##....#...OO#..O#....OO#OO#..#.........OOOOOO#....OO##.#.##.#.....#....#O##...O#......
...OO#.......OOO#....#..#..#...#...#..O#.....#OOO#OO#.#..OO##..#...#....#.........O#..........OOOOOO
.......OOOOOO#...#..#...#..........OO#.......O#O#.#O#..O#..#..............O#..#...#...O#.#.#..#..OOO
O#.OO##.......OOOO#.O##..O#................OOOO#......O##........O#....##.....O##.........O#.#.#..OO
.......OOOO##.#..##.O#.....OOO##....O##.....O#......OOO#........O#......O#.........#..##.......O#..O
....OOO#.......OO##O#..............OOOOO#......#..........OOOO#..#..#...#.............O#..#......O#.
#..O#.........O###.#..........OOOOO##.O#.....#..OOO#...................OO#...#..#.##.........OO#....
.............OO##....O#O#....OO#.....#.......O#..##..##..........O#.....#.........##......#.#.....OO
.......OOOO#.........O#...OO#.....O##......##.#............#.......O#..#......................#.#..O
.OO#...........OOOOOO#....OOO##...................OOO#...OO#...O#........OOO#.##...#..#........O#..#
....OOOOOOO#....OOO##.O#.O#............OOOOOOOO#....OO###........OOO##....O#.................OO##...
...OOOOOOO#........OOO#....O##....O#..OOO#...#.....O#..O#..#.#................OO#........#.#..#.....
...OO#.....OOOOOOOO#..........OOOOO#..O#...O##.....OO#...........OO#.#..O#.#......#.................
#....OO#OO#.###......OOOO#......OOOOO#......O#.O#....................OOOOOO#....#.................OO
................OOOOOOOOOOOOO#.....OOOOO#..#...#....OO#.#.....#.....O##..#..........O####...........
.OOOOO#.O#.....#....OO#....OOOO#.O#...OO#......#.OO#.......OO#.#...............OOO#.......#......O#.
O#O#..OOO#.......OOOOOO#...OO#.....OOOO#...#...#...........OOOOOOOO#.#.......OOO#O#..#..#.......OO#.
..OO#..O##.O#O#..#.O#...O#O#..#..####.......##....OOO##.........OOOOOO##.......OO#...........O#..OOO
.......OOOOOO#.........................OOOO#...OO#.......OOOOO#.##............OOOOO#...........#..OO
.....OOOOO#.....OO#....O#.................OOOOOOOO#.....OOOO##...#......OOO#O##..............OOO#O#.
..OOO#.....OO#....OOOOOO##.OO#...#..##.....#.#O#.....OOOOO##.......##.....#....O#O#...##.....#....O#
......OOOO#....OOOOO#OO##..O#...............OOOOOOOO#...OO##.......##........O#O#..............O#..O
#.........OOOOOOO#.#.O#.......O#..........OOOO#.#.#.....OOOO##.....#.O#..O#..OO#.#.......O#......OOO
.#...O#.#.OO#.OOOO#....OOO#........OOOOO#..........OOOOOO#...#..#........OOO#...#........OO#..#.O#.#
....OO#...O#....OOOOOOO#..#....OOOO###O#.......OO#.......OOOOO#.#...O#..#..#.....#....OO##.....#.#..
#......OO#..OOOO#...###.....#..OOO#.#.#.........OOOOO#.#....#........OO#.......O#.....OO##..........
#..OO#...#.#.............OOOO#.........OOOO#O#...#.##........#...#.........O#....O#.O#.............O
..........OOO#OO#............#.................OOOOO#............OOO#............OOOOO#......OO##...
..#........OO##............OOO#.......OOOOO#.......O#..OOO#.........O#.O#..#......OO#..#.##..##....#
........OOOOOO#..OOO#.....OO#.................OOOOOOOOO##.#.#.......O#.#..#..#..#.#.OO#.#........OO#
......OOOOOOOOO#........OOOOO#.#.O#.....OO#....OO#.#.................OOOOO#........OO#...##.....#.OO
..OOOOOOOO#..O#..O#O#........OOO#....#.#..OO#.........OOOOOO#..............OOOO#.#.#...#.......OO#.O
OO#OO#..OO#.O#.#..O#.....OO#..O##........OOOOOOOOO#..#..O#.....O#............OOOO#......#......#...O
O#.OO#..OO#.#..O#....OO##.#....OOO#.O#...OOO###...OOOO#..........OOOOOOO#...OO#....OOO#......#....#.
..O#.O#...OO##.#...O#......OO#....OOO##......OOO##..#..OO#..OOO#...OO#...OOO#..#..##..#......OO#.#..
..O#......OOO#...OOOO#.....OOOOO#...OOOO#............OO#.....OOOOOO#....O#............OOOO##......O#
#...#....OO#.#.....OOOOOOOOOO##.OOOO#....OOOOOO####..OOO#..OOOO#...OOO#.##.OOO#.....OOO#O#.#.....OOO
.....OOOOOOO#.O#...OOO#O#OO#...OOO#.....OOOOOOOOOOO#.#..OOO#.....OOOOOOO#.....OOOOOOOOOO#...OOOO##.O
'''

lines = list(input.splitlines()[1:])
prepared_lines = list(prepared_input.splitlines()[1:])
prepared_long_lines = list(prepared_long_input.splitlines()[1:])

if __name__ == '__main__':
    # lines = list(sys.stdin.read().splitlines())

    result = process_all(lines)
    print(result)
