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

    positions = [node for node in network.keys() if node[-1] == 'A']
    print(positions)

    cycles = {}
    for position in positions:
        orig_position = position
        visited = set()
        path = []
        final_positions = []
        for index, instruction in cycle(enumerate(instructions)):
            if (position, index) in visited:
                path.append((position, index))
                break

            visited.add((position, index))
            path.append((position, index))

            i = 0 if instruction == 'L' else 1
            position = network[position][i]

            if position[-1] == 'Z':
                final_positions.append(len(path))

        cycle_init = 0
        cycle_length = 0
        for i, node in enumerate(path[:-1]):
            if node == path[-1]:
                cycle_init = i
                cycle_length = len(path) - i - 1
                break

        # with the input, there is only a single final position per cycle which its distance equals
        # to the length of the cycle.
        # So we have printed lines like: XXA [N] I N
        # Then we try to find the smallest number f = k1 * N1 = k2 * N2 = ... for all ki
        # -> this looks like the LCM, which was the good answer
        print(orig_position, final_positions, cycle_init, cycle_length)

        cycles[orig_position] = (cycle_init, cycle_length, final_positions)

    from math import lcm
    return lcm(*[cycle[1] for cycle in cycles.values()])

input = '''
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
'''

lines = list(input.splitlines()[1:])

if __name__ == '__main__':
    lines = list(sys.stdin.read().splitlines())

    result = process_all(lines)
    print(result)
