import sys
from collections import Counter
from functools import cmp_to_key
from itertools import cycle

def process_all(lines):
    instructions = lines[0]

    network = {}
    for line in lines[2:]:
        origin = line[:3]
        left = line[7:10]
        right = line[12:-1]
        network[origin] = (left, right)

    print(network)

    step = 0
    position = 'AAA'
    for instruction in cycle(instructions):
        i = 0 if instruction == 'L' else 1
        position = network[position][i]
        step += 1

        if position == 'ZZZ':
            return step

    return 0

input = '''
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
'''

lines = list(input.splitlines()[1:])

if __name__ == '__main__':
    lines = list(sys.stdin.read().splitlines())

    result = process_all(lines)
    print(result)
