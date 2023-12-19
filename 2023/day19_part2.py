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

ACCEPTED = 'A'
REJECTED = 'R'
GT = '>'
LT = '<'
JUMP = 'J'

def process_all(lines):
    result = 0

    workflows = {}
    states = []
    is_parsing_workflow = True
    for line in lines:
        if not line:
            is_parsing_workflow = False

        if is_parsing_workflow:
            part_key, conditions = line.split('{')
            conditions = conditions[:-1]
            tokens = conditions.split(',')
            commands = []
            for token in tokens:
                if '<' in token:
                    compare_key, compared_value = token.split('<')
                    compared_value, jump_key = compared_value.split(':')
                    compared_value = int(compared_value)
                    commands.append((LT, compare_key, compared_value, jump_key))
                elif '>' in token:
                    compare_key, compared_value = token.split('>')
                    compared_value, jump_key = compared_value.split(':')
                    compared_value = int(compared_value)
                    commands.append((GT, compare_key, compared_value, jump_key))
                elif token == 'R':
                    commands.append((JUMP, REJECTED))
                elif token == 'A':
                    commands.append((JUMP, ACCEPTED))
                else:
                    commands.append((JUMP, token))

            workflows[part_key] = commands

        elif line:
            line = line[1:-1]
            tokens = line.split(',')
            state = {}
            for token in tokens:
                var_name, var_value = token.split('=')
                var_value = int(var_value)
                state[var_name] = var_value
            states.append(state)

    print(workflows)
    print(states)

    def execute_state():
        result = 0
        open_set = [('in', {'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)})]
        while open_set:
            part_key, state = open_set.pop()
            print(part_key, state)

            if part_key == REJECTED:
                print('REJECTED')
                print()
                continue
            if part_key == ACCEPTED:
                r = 1
                for v in state.values():
                    r *= v[1] - v[0] + 1
                print(state, r)
                print('ACCEPTED')
                print()
                result += r
                continue

            workflow = workflows[part_key]
            for command in workflow:
                if command[0] == GT:
                    _, key, value, jump = command
                    state_min, state_max = state[key]
                    if state_min > value:
                        open_set.append((jump, state))
                        break
                    elif value < state_max:
                        new_state = state.copy()
                        new_state[key] = (value + 1, state_max)
                        remaining_state = state.copy()
                        remaining_state[key] = (state_min, value)
                        state = remaining_state
                        open_set.append((jump, new_state))
                elif command[0] == LT:
                    _, key, value, jump = command
                    state_min, state_max = state[key]
                    if state_max < value:
                        open_set.append((jump, state))
                        break
                    elif value > state_min:
                        new_state = state.copy()
                        new_state[key] = (state_min, value - 1)
                        remaining_state = state.copy()
                        remaining_state[key] = (value, state_max)
                        state = remaining_state
                        open_set.append((jump, new_state))
                if command[0] == JUMP:
                    _, jump = command
                    open_set.append((jump, state))
                    break

        return result

    return execute_state()


input = '''
px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}
'''

lines = list(input.splitlines()[1:])

if __name__ == '__main__':
    # lines = list(sys.stdin.read().splitlines())

    result = process_all(lines)
    print(result)
