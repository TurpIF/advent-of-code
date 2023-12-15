import itertools
import sys
from collections import Counter
from functools import cmp_to_key
from itertools import cycle
from itertools import repeat
from itertools import chain
from heapq import *

def process_all(lines):
    line = lines[0]
    steps = line.split(',')
    lens = {}
    result = 0
    for step in steps:
        key = ''
        value = -1
        is_removed = False
        if step[-1] == '-':
            key = step[:-1]
            is_removed = True
        else:
            [key, value] = step.split('=')
            value = int(value)

        hash = 0
        for c in key:
            hash += ord(c)
            hash = (hash * 17) % 256

        if hash not in lens:
            lens[hash] = ([], {})

        if is_removed:
            if key in lens[hash][0]:
                lens[hash][0].remove(key)
                del lens[hash][1][key]
        else:
            if key in lens[hash][0]:
                lens[hash][1][key] = value
            else:
                lens[hash][0].append(key)
                lens[hash][1][key] = value

        # print(key, hash, value, is_removed, lens)

    print(lens)

    for l in lens.keys():
        for pos, key in enumerate(lens[l][0]):
            result += (l + 1) * (pos + 1) * lens[l][1][key]
    return result


input = '''
rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
'''

lines = list(input.splitlines()[1:])

if __name__ == '__main__':
    lines = list(sys.stdin.read().splitlines())

    result = process_all(lines)
    print(result)
