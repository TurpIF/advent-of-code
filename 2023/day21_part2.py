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

def process_all(lines, expected_distance):
    def print_grid(traversed, len_x, len_y, min_x=0, min_y=0):
        for y in range(min_x, len_y):
            line = ''
            for x in range(min_y, len_x):
                px = x % len(lines[0])
                py = y % len(lines)
                if lines[py][px] == 'S':
                    line += 'S'
                elif (x, y) in traversed:
                    line += 'O'
                else:
                    line += lines[py][px]

            print(line)

    def is_walkable(x, y):
        #if not (0 <= x < len(lines[0]) and 0 <= y < len(lines)):
        #    return False

        x = x % len(lines[0])
        y = y % len(lines)

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
    for s in range(expected_distance):
        traversed = set()

        for p in previous_traversed:
            for n in neighbours(p):
                traversed.add(n[1])

        previous_traversed = traversed

    # print_grid(boundaries, 2 * expected_distance, 2 * expected_distance, min_x=-expected_distance, min_y=-expected_distance)

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

    # I tried first with dijkstra to reduce the complexity, and then I tried to transform to
    # expectation by counting cells with distance = expected and the even cells where
    # distance < expected. This was working on the sample input perfectly. So I tried on the big
    # one, with the big expected steps. Surely it was still too big for dijkstra.
    # .
    # But it helped me to draw the (step -> reachable_pots(step)), which looks like a quadratic
    # polynome. But not exactly :/
    # The not exactly made me think that I have an issue in my code. And indeed, when running the
    # part1 implem (without dijkstra), I found differences -> removing dijkstra.
    # Even with the fix, the polynomial was still not exact :(
    # .
    # Here I tried observing the input and output for small step values:
    # the input is a square of 131 x 131
    # there is a diamond form inside (not sure what to do with that)
    # there is no rock on the row/column where the S is located
    # there is no rock on the bordering rows/columns
    # The output is a diamond composed of inner boards and boundary boards
    # -> it is possible to use a manhattan distance to at least reach the boundary boards
    # -> inner boards are filled (but there is even/odd boards)
    # -> boundary boards on the edge seems to be similar (but with the same even/odd distinction)
    # -> in boundary boards, the corners parts (I didn't observe if it was composed of many boards)
    # are edge cases to handle (+ potentially handling even/odd)
    # -> depending of the number of boundary boards, previous strategy from part 1 could do the job
    # for counting the remaining point in such.
    # ==> It seems complicated
    # .
    # Before trying this, I first came back to the polynome.
    # I assumed that there should be some recurrence every square, and there was a closed form:
    # step 1 * 131 -> 14797
    # step 2 * 131 -> 58819
    # step 3 * 131 -> 132067
    # step 4 * 131 -> 234541
    # https://www.wolframalpha.com/input?i=14797%2C+58819%2C+132067%2C+234541
    # f(step) = a(n = step / 131) = polynome
    # The step 5 * 131 was correctly found
    # .
    # Testing with the step = k * 131 + 1 worked too:
    # https://www.wolframalpha.com/input?i=15018%2C+59258%2C+132724%2C+235416
    #
    # Finally, 26501365 = 202300 * 131 + 65
    # So I applied again: https://www.wolframalpha.com/input?i=33086%2C+91672%2C+179484%2C+296522
    # It worked :)


    # Get process_all values from this, and update the polynome from it
    for n in range(6):
        x = len(lines) * n + 65
        print('(', n, ',', process_all(lines, x), '),')

    expected_step = 26501365
    n = expected_step // len(lines)

    a0 = 3726
    a1 = 14747
    a2 = 14613
    print(a2 * n ** 2 + a1 * n + a0)
