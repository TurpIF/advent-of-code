import itertools
import sys
from collections import Counter
from functools import cmp_to_key
from itertools import cycle
from itertools import repeat
from itertools import chain
from heapq import *

UP = 'U'
DOWN = 'D'
LEFT = 'L'
RIGHT = 'R'

def print_grid(traversed, len_x, len_y):
    for y in range(len_y):
        line = ''
        for x in range(len_x):
            if (x, y) in traversed:
                line += '#'
            else:
                line += '.'

        print(line)

def process_all(lines):
    result = 0
    beams = []
    beams.append(((0, 0), RIGHT))
    visited_beams = set()
    traversed = set()

    def add_beam(pos, direction):
        beam_x, beam_y = pos
        if not (0 <= beam_x < len(lines[0]) and 0 <= beam_y < len(lines)):
            return

        if (pos, direction) in visited_beams:
            return

        visited_beams.add((pos, direction))
        beams.append((pos, direction))

    while beams:
        (beam_x, beam_y), beam_dir = beams.pop()
        # print_grid(traversed, len(lines[0]), len(lines))
        # print('Next', (beam_x, beam_y), beam_dir)
        if not (0 <= beam_x < len(lines[0]) and 0 <= beam_y < len(lines)):
            continue

        if beam_dir == RIGHT:
            for x in range(beam_x, len(lines[0])):
                traversed.add((x, beam_y))
                if lines[beam_y][x] == '|':
                    add_beam((x, beam_y - 1), UP)
                    add_beam((x, beam_y + 1), DOWN)
                    break
                if lines[beam_y][x] == '/':
                    add_beam((x, beam_y - 1), UP)
                    break
                if lines[beam_y][x] == '\\':
                    add_beam((x, beam_y + 1), DOWN)
                    break
        elif beam_dir == LEFT:
            for x in range(beam_x, -1, -1):
                traversed.add((x, beam_y))
                if lines[beam_y][x] == '|':
                    add_beam((x, beam_y - 1), UP)
                    add_beam((x, beam_y + 1), DOWN)
                    break
                if lines[beam_y][x] == '/':
                    add_beam((x, beam_y + 1), DOWN)
                    break
                if lines[beam_y][x] == '\\':
                    add_beam((x, beam_y - 1), UP)
                    break
        elif beam_dir == DOWN:
            for y in range(beam_y, len(lines)):
                traversed.add((beam_x, y))
                if lines[y][beam_x] == '-':
                    add_beam((beam_x - 1, y), LEFT)
                    add_beam((beam_x + 1, y), RIGHT)
                    break
                if lines[y][beam_x] == '/':
                    add_beam((beam_x - 1, y), LEFT)
                    break
                if lines[y][beam_x] == '\\':
                    add_beam((beam_x + 1, y), RIGHT)
                    break
        elif beam_dir == UP:
            for y in range(beam_y, -1, -1):
                traversed.add((beam_x, y))
                if lines[y][beam_x] == '-':
                    add_beam((beam_x - 1, y), LEFT)
                    add_beam((beam_x + 1, y), RIGHT)
                    break
                if lines[y][beam_x] == '/':
                    add_beam((beam_x + 1, y), RIGHT)
                    break
                if lines[y][beam_x] == '\\':
                    add_beam((beam_x - 1, y), LEFT)
                    break

    return len(traversed)


input = '''
.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|....
'''

lines = list(input.splitlines()[1:])

if __name__ == '__main__':
    lines = list(sys.stdin.read().splitlines())

    result = process_all(lines)
    print(result)
