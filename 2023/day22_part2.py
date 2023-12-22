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


def process_all(lines):
    bricks = []
    bricks_by_id = {}
    for id, line in enumerate(lines):
        left, right = line.split('~')

        x1, y1, z1 = left.split(',')
        x1 = int(x1)
        y1 = int(y1)
        z1 = int(z1)

        x2, y2, z2 = right.split(',')
        x2 = int(x2)
        y2 = int(y2)
        z2 = int(z2)

        if z1 <= z2:
            p = x1, y1, z1
            l = x2 - x1 + 1, y2 - y1 + 1, z2 - z1 + 1
        else:
            p = x2, y2, z2
            l = x1 - x2 + 1, y1 - y2 + 1, z1 - z2 + 1

        brick = (p, l)
        bricks.append(brick)
        bricks_by_id[id] = brick

    bricks = sorted(bricks, key=lambda b: b[0][2])
    new_bricks = []
    print(bricks)
    # print(bricks_by_id)
    floor = defaultdict(lambda: 0)
    bricks_by_pos = defaultdict(list)
    for brick in bricks:
        min_floor = 1
        for x in range(brick[0][0], brick[0][0] + brick[1][0]):
            for y in range(brick[0][1], brick[0][1] + brick[1][1]):
                min_floor = max(min_floor, floor[(x, y)])

        new_brick = ((brick[0][0], brick[0][1], min_floor), brick[1])
        new_bricks.append(new_brick)

        for x in range(brick[0][0], brick[0][0] + brick[1][0]):
            for y in range(brick[0][1], brick[0][1] + brick[1][1]):
                z_below = min_floor
                z_above = z_below + brick[1][2]
                floor[(x, y)] = z_above
                bricks_by_pos[(x, y, z_above)].append(new_brick)

    bricks_by_support = defaultdict(set)
    supported_bricks_by_brick = defaultdict(set)
    for brick in new_bricks:
        supporting_bricks = set()
        for x in range(brick[0][0], brick[0][0] + brick[1][0]):
            for y in range(brick[0][1], brick[0][1] + brick[1][1]):
                for b in bricks_by_pos[(x, y, brick[0][2])]:
                    supporting_bricks.add(b)

        print(brick, supporting_bricks)
        for b in supporting_bricks:
            bricks_by_support[brick].add(b)
            supported_bricks_by_brick[b].add(brick)

    print()
    important_bricks = set()
    falling_bricks_by_important_brick = defaultdict(set)
    not_supporting_bricks = set(new_bricks)

    for brick in new_bricks:
        # print(brick, bricks_by_support[brick])

        for b in bricks_by_support[brick]:
            if b in not_supporting_bricks:
                not_supporting_bricks.remove(b)

        if len(bricks_by_support[brick]) == 1:
            for b in bricks_by_support[brick]:
                important_bricks.add(b)
                falling_bricks_by_important_brick[b].add(brick)

    print(new_bricks)
    print(floor)
    print(bricks_by_pos)
    print('important', important_bricks)
    print('bricks_by_support', bricks_by_support)
    print('supported_bricks_by_brick', supported_bricks_by_brick)
    #print('not supporting', not_supporting_bricks)
    #print(falling_bricks_by_important_brick)

    print()
    print()
    print()

    result = 0
    for important_brick in important_bricks:
        removed = set()
        removed.add(important_brick)

        open_set = [important_brick]
        while open_set:
            brick = open_set.pop(0)
            for child in supported_bricks_by_brick[brick]:
                supporting_count = sum(1 for b in bricks_by_support[child] if b not in removed)
                if supporting_count == 0:
                    removed.add(child)
                    open_set.append(child)

        print(important_brick, removed)
        result += len(removed) - 1

    return result


input = '''
1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9
'''

lines = list(input.splitlines()[1:])

if __name__ == '__main__':
    lines = list(sys.stdin.read().splitlines())

    result = process_all(lines)
    print(result)
