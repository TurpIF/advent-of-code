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
    positions = []
    velocities = []
    for line in lines:
        t1, t2 = line.split('@')
        positions.append(list(map(int, t1.split(','))))
        velocities.append(list(map(int, t2.split(','))))

    print(positions)
    print(velocities)

    result = 0
    for (p1, v1), (p2, v2) in itertools.combinations(zip(positions, velocities), 2):
        # https://web.archive.org/web/20091003070719/http://local.wasp.uwa.edu.au/~pbourke/geometry/lineline2d/

        denominator = v1[0] * v2[1] - v2[0] * v1[1]
        if denominator == 0:
            print(p1, v1, p2, v2, 'skip')
            continue

        t1 = (v2[0] * (p1[1] - p2[1]) - v2[1] * (p1[0] - p2[0])) / denominator
        t2 = (v1[0] * (p1[1] - p2[1]) - v1[1] * (p1[0] - p2[0])) / denominator

        x = v1[0] * t1 + p1[0]
        y = v1[1] * t1 + p1[1]

        print(p1, v1, p2, v2, x, y, t1, t2)

        low_bound = 200000000000000
        high_bound = 400000000000000
        if t1 > 0 \
                and t2 > 0 \
                and low_bound <= x <= high_bound \
                and low_bound <= y <= high_bound:
            result += 1

    return result


input = '''
19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3
'''

lines = list(input.splitlines()[1:])

if __name__ == '__main__':
    lines = list(sys.stdin.read().splitlines())

    result = process_all(lines)
    print(result)
