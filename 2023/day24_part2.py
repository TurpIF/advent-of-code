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

    print()
    print('''
(declare-const px Real)
(declare-const py Real)
(declare-const pz Real)

(declare-const vx Real)
(declare-const vy Real)
(declare-const vz Real)

(declare-const t1 Real)
(declare-const t2 Real)
(declare-const t3 Real)''')

    for i, (p, v) in enumerate(islice(zip(positions, velocities), 3)):
        tvar = 't' + str(i + 1)
        print('(assert (= (+ px (* vx ', tvar, ')) (+ ', p[0], ' (* ', v[0], ' ', tvar, '))))')
        print('(assert (= (+ py (* vy ', tvar, ')) (+ ', p[1], ' (* ', v[1], ' ', tvar, '))))')
        print('(assert (= (+ pz (* vz ', tvar, ')) (+ ', p[2],  ' (* ', v[2], ' ', tvar, '))))')

    print('''
(apply (then simplify solve-eqs))
(check-sat)
(get-model)''')

    print('')
    print('Copy this in https://microsoft.github.io/z3guide/playground/Freeform%20Editing/')
    print('Then sum the 3 px, py, pz')

    return 0


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
