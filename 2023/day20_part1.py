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

BROADCASTER = 'broadcaster'
FLIP_FLOP = '%'
CONJUNCTION = '&'
LOW = 'low'
HIGH = 'high'
ON = True
OFF = False

def process_all(lines):
    workflows = {}
    flip_flops = {}
    conjunctions = {}
    links = {}

    for n, line in enumerate(lines):
        key, rule = line.split('->')
        key = key[:-1]
        tokens = [c[1:] for c in rule.split(',')]

        if key == BROADCASTER:
            workflows[key] = (BROADCASTER, tokens)
        elif key[0] == FLIP_FLOP:
            key = key[1:]
            flip_flops[key] = OFF
            workflows[key] = (FLIP_FLOP, tokens)
        elif key[0] == CONJUNCTION:
            key = key[1:]
            conjunctions[key] = {}
            workflows[key] = (CONJUNCTION, tokens)

        for token in tokens:
            if token not in links:
                links[token] = []
            links[token].append(key)

    for key, conjunction in conjunctions.items():
        linked = links[key]
        for link in linked:
            conjunction[link] = LOW

    print(workflows)
    print(flip_flops)
    print(conjunctions)
    print(links)
    print()

    def click_once():
        nb_low = 0
        nb_high = 0
        for _ in range(1000):
            print()
            open_set = [('broadcaster', 'init', LOW, 0)]
            while open_set:
                state = open_set.pop(0)
                button, previous_button, signal, depth = state
                print(previous_button + ' -' + signal + '->', button)

                nb_low += 1 if signal == LOW else 0
                nb_high += 1 if signal == HIGH else 0

                if button in workflows:
                    workflow = workflows[button]
                    if workflow[0] == BROADCASTER:
                        for token in workflow[1]:
                            open_set.append((token, button, signal, depth + 1))
                    elif workflow[0] == FLIP_FLOP:
                        if signal == LOW:
                            previous_state = flip_flops[button]
                            flip_flops[button] = not previous_state
                            new_signal = HIGH if previous_state == OFF else LOW

                            for token in workflow[1]:
                                open_set.append((token, button, new_signal, depth + 1))
                    elif workflow[0] == CONJUNCTION:
                        conjunctions[button][previous_button] = signal

                        new_signal = LOW if all(s is None or s == HIGH for s in conjunctions[button].values()) else HIGH
                        for token in workflow[1]:
                            open_set.append((token, button, new_signal, depth + 1))

        return nb_low * nb_high

    return click_once()


input = '''
%gv -> lq, pm
%rv -> jd, nh
%nh -> rs, jd
&vt -> tj
%zv -> pm, gv
%gh -> jd, vd
%hh -> bf, qm
%kx -> nf
%st -> pm, zc
%bh -> qm, pv
&sk -> tj
%hl -> nf, pn
%mt -> st, pm
&jd -> ts, gh, vd, dc, xc
%zm -> hm
%pv -> vv
%zf -> nf, cz
&xc -> tj
%bf -> qm
%ts -> sg
%ht -> ch, nf
%pb -> rv, jd
%nx -> fc
%mb -> mt
%mh -> jd, pb
%lc -> bh
%xg -> mb, pm
%vd -> dc
broadcaster -> gh, dl, xg, fb
%sg -> mh, jd
%qq -> ts, jd
%dl -> nf, sv
%vv -> sm, qm
%zc -> tb
%sr -> zv, pm
%dc -> gb
%cz -> nf, zm
%rs -> jd
%hm -> nf, hl
%gd -> sr
&qm -> lc, pv, nx, fb, kk
&tj -> rx
%gb -> qq, jd
%xf -> zf
%tb -> lg
%sm -> qm, hh
%fb -> dr, qm
%lq -> pm
&nf -> zm, dl, ch, xf, vt
&pm -> sk, zc, tb, gd, mb, xg
%pn -> nf, kx
%fc -> xb, qm
%ch -> xf
&kk -> tj
%lg -> pm, gd
%sv -> nf, ht
%xb -> qm, lc
%dr -> nx, qm
'''

lines = list(input.splitlines()[1:])

if __name__ == '__main__':
    # lines = list(sys.stdin.read().splitlines())

    result = process_all(lines)
    print(result)
