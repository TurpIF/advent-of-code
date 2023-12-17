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
def process_all(lines):
    def get_score(x, y):
        if not (0 <= x < len(lines[0]) and 0 <= y < len(lines)):
            return None
        return int(lines[y][x])

    def neighbours(args):
        (position, current_dir, remaining_count) = args
        x, y = position
        if get_score(x, y) is None:
            return

        candidates = []
        if remaining_count > 0:
            if current_dir == LEFT:
                candidates.append(((position[0] - 1, position[1]), current_dir, remaining_count - 1))
            elif current_dir == RIGHT:
                candidates.append(((position[0] + 1, position[1]), current_dir, remaining_count - 1))
            elif current_dir == UP:
                candidates.append(((position[0], position[1] - 1), current_dir, remaining_count - 1))
            elif current_dir == DOWN:
                candidates.append(((position[0], position[1] + 1), current_dir, remaining_count - 1))

        if current_dir == LEFT:
            candidates.append(((position[0], position[1] - 1), UP, 2))
            candidates.append(((position[0], position[1] + 1), DOWN, 2))
        elif current_dir == RIGHT:
            candidates.append(((position[0], position[1] - 1), UP, 2))
            candidates.append(((position[0], position[1] + 1), DOWN, 2))
        elif current_dir == UP:
            candidates.append(((position[0] - 1, position[1]), LEFT, 2))
            candidates.append(((position[0] + 1, position[1]), RIGHT, 2))
        elif current_dir == DOWN:
            candidates.append(((position[0] - 1, position[1]), LEFT, 2))
            candidates.append(((position[0] + 1, position[1]), RIGHT, 2))

        return ((get_score(c[0][0], c[0][1]), c) for c in candidates if get_score(c[0][0], c[0][1]) is not None)

    def print_grid(traversed, len_x, len_y):
        for y in range(len_y):
            line = ''
            for x in range(len_x):
                if (x, y) in traversed:
                    line += '#'
                else:
                    line += '.'

            print(line)

    def dijkstra(s, t, voisins):
        M = set()
        d = {s: 0}
        p = {}
        suivants = [(0, s)] #Â tas de couples (d[x],x)

        while suivants != []:

            dx, x = heappop(suivants)
            if x in M:
                continue

            M.add(x)

            for w, y in voisins(x):
                if y in M:
                    continue
                dy = dx + w
                if y not in d or d[y] > dy:
                    d[y] = dy
                    heappush(suivants, (dy, y))
                    p[y] = x

        print(d)

        key_min = min((key for key in d.keys() if key[0] == t), key=lambda k: d[k])
        path = [key_min]
        x = key_min
        while x != s:
            x = p[x]
            path.insert(0, x)

        print(path)
        print_grid({p[0] for p in path}, t[0] + 1, t[1] + 1)
        return d[key_min]

    s1 = ((0, 0), RIGHT, 3)
    s2 = ((0, 0), DOWN, 3)
    t = (len(lines[0]) - 1, len(lines) - 1)

    score1 = dijkstra(s1, t, neighbours)
    print(score1)

    score2 = dijkstra(s2, t, neighbours)
    print(score2)

    return min(score1, score2)


input = '''
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
'''

lines = list(input.splitlines()[1:])

if __name__ == '__main__':
    lines = list(sys.stdin.read().splitlines())

    result = process_all(lines)
    print(result)
