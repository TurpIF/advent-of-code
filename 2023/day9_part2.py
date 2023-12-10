import sys
from collections import Counter
from functools import cmp_to_key
from itertools import cycle

def process_all(lines):
    def compute_diff_sequence(ls):
        return [b - a for a, b in zip(ls[:-1], ls[1:])]

    result = 0

    for line in lines:
        line = [int(c) for c in line.split()]
        current_diff = line
        diff_sequences = []
        diff_sequences.append(line)
        while True:
            diff_sequence = compute_diff_sequence(current_diff)
            diff_sequences.append(diff_sequence)
            current_diff = diff_sequence

            if all(x == 0 for x in diff_sequence):
                break

        print(line)
        for diff_sequence in diff_sequences:
            print(diff_sequence)
        print()

        diff_sequences[-1].append(0)
        for below, current in zip(diff_sequences[::-1][:-1], diff_sequences[::-1][1:]):
            current.append(current[-1] + below[-1])
            current.insert(0, current[0] - below[0])

        for diff_sequence in diff_sequences:
            print(diff_sequence)
        print()

        result += line[0]
    return result

input = '''
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
'''

lines = list(input.splitlines()[1:])

if __name__ == '__main__':
    lines = list(sys.stdin.read().splitlines())

    result = process_all(lines)
    print(result)
