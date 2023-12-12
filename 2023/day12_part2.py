import itertools
import sys
from collections import Counter
from functools import cmp_to_key
from itertools import cycle
from itertools import repeat
from itertools import chain
from heapq import *

class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}
    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]

def process_line(line):
    [arrangement, info_raw] = line.split(' ')
    infos = [int(i) for i in info_raw.split(',')]

    arrangement = ''.join(repeat(arrangement + '?', 5))[:-1]
    infos = list(chain(*repeat(infos, 5)))

    print(arrangement)
    print(infos)

    @Memoize
    def process_dp(arrangement, from_arrangement, from_infos):
        def get_arrangement(i):
            return None if i >= len(arrangement) else arrangement[i]

        i = from_arrangement

        def try_consume(remaining_info, i):
            while remaining_info > 0:
                if get_arrangement(i) == '#':
                    remaining_info -= 1
                    i += 1

                elif get_arrangement(i) == '?':
                    remaining_info -= 1
                    i += 1

                else:
                    # not possible
                    return False

            if get_arrangement(i) == '#':
                # We need at least a space
                return False

            return i + 1

        for j, info in enumerate(infos[from_infos:]):
            if get_arrangement(i) == '.':
                while get_arrangement(i) == '.':
                    i += 1

            # Either we skip, either we start consuming
            if get_arrangement(i) == '?':
                result = 0
                # Try consuming
                r = try_consume(info - 1, i + 1)
                if r:
                    '''new_arrangement = list(arrangement)
                    for a in range(i, r - 1):
                        new_arrangement[a] = '#'
                    if r - 1 < len(new_arrangement):
                        new_arrangement[r - 1] = '.'
                    new_arrangement = "".join(new_arrangement)'''
                    new_arrangement = arrangement
                    result += process_dp(new_arrangement, r, from_infos + j + 1)

                # Try skipping
                '''new_arrangement = list(arrangement)
                new_arrangement[i] = '.'
                new_arrangement = "".join(new_arrangement)'''
                new_arrangement = arrangement
                result += process_dp(new_arrangement, i + 1, from_infos + j)
                return result

            r = try_consume(info, i)
            if not r:
                return 0

            i = r

        if get_arrangement(i) in ['.', '?']:
            while get_arrangement(i) in ['.', '?']:
                i += 1

        if i < len(arrangement):
            # Not everything was consumed
            return 0

        # print(arrangement, infos, from_arrangement)
        return 1

    result = process_dp(arrangement, 0, 0)
    print(result)
    return result


def process_all(lines):
    return sum(process_line(line) for line in lines)


input = '''
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
'''

lines = list(input.splitlines()[1:])

if __name__ == '__main__':
    lines = list(sys.stdin.read().splitlines())

    result = process_all(lines)
    print(result)
