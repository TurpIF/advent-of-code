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
    result = 0
    for step in steps:
        hash = 0
        for c in step:
            hash += ord(c)
            hash = (hash * 17) % 256
        result += hash

    return result


input = '''
rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
'''

lines = list(input.splitlines()[1:])

if __name__ == '__main__':
    lines = list(sys.stdin.read().splitlines())

    result = process_all(lines)
    print(result)
