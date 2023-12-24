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
from copy import deepcopy

class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}
    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]

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

        path = [t]
        x = t
        while x != s:
            x = p[x]
            path.insert(0, x)

        return path, d

    def is_walkable(x, y):
        if not (0 <= x < len(lines[0]) and 0 <= y < len(lines)):
            return False

        return lines[y][x] in ['.', '<', '>', 'v', '^']
    def neighbours(node):
        (x, y) = node

        candidates = []
        candidates.append((x - 1, y))
        candidates.append((x + 1, y))
        candidates.append((x, y - 1))
        candidates.append((x, y + 1))

        ns = [c for c in candidates if is_walkable(*c)]
        return ns

    reduce_neighbours = defaultdict(list)
    cache = {}

    def dfs(start, target, visited, path ='-'):
        if len(path) < 11:
            print(path)
        #key = (start, frozenset(visited))
        # print(cache)
        #if key in cache:
            #pass
            # print('HIT !!!!')
            #return cache[key]
        node = start
        visited.add(start)
        dmax = 0
        for i, (next_node, d) in enumerate(reduce_neighbours[start]):
            if next_node in visited:
                continue
            if next_node == target:
                # cache[key] = d
                return d
            dd = dfs(next_node, target, deepcopy(visited), path + str(i))
            # print(path, node, next_node, str(d) + ' + ' + str(dd) + ' = ' + str(d + dd))
            dmax = max(dmax, d + dd)
        # cache[key] = dmax
        return dmax
        # return distance + 1 + max(dfs(n, target, deepcopy(visited)) for n in ns)

    start = (1, 0)
    target = (len(lines[0]) - 2, len(lines) - 1)
    traversed = set()
    print_grid(traversed, len(lines[0]), len(lines))

    open_set = [(start, start)]
    close_set = set()
    while open_set:
        node, previous = open_set.pop(0)
        if node in close_set:
            continue
        close_set.add(node)

        first_node = node
        visited = set()
        visited.add(previous)
        distance = 0

        while True:
            visited.add(node)
            if node == target:
                reduce_neighbours[previous].append((node, distance + 1))
                break
            ns = set(neighbours(node)) - visited
            if not ns:
                break
            elif len(ns) == 1:
                node = list(ns)[0]
                distance += 1
            else:
                reduce_neighbours[previous].append((node, distance + (1 if previous != start else 0)))
                for n in ns:
                    open_set.append((n, node))
                break

    for k, v in reduce_neighbours.items():
        print(k, ' -> ', v)

    return dfs(start, target, set())


input = '''
#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#
'''

lines = list(input.splitlines()[1:])

if __name__ == '__main__':
    lines = list(sys.stdin.read().splitlines())

    result = process_all(lines)
    print(result)
