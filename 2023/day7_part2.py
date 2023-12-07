import sys
from collections import Counter
from functools import cmp_to_key
from functools import cache

def process_all(lines):
    @cache
    def compute_type(hand):
        counter = Counter(hand)
        joker = 1
        joker_count = counter[joker]
        counter[joker] = 0
        most_common = counter.most_common(1)[0]
        counter[most_common[0]] = most_common[1] + joker_count

        most_commons = sorted(map(lambda x: x[1], counter.most_common(2)), reverse=True)
        print('most_commons', most_commons, counter, joker_count)
        if most_commons[0] == 5:
            return 5
        elif most_commons[0] == 4:
            return 4
        elif most_commons[0] == 3:
            if most_commons[1] == 2:
                return 3
            else:
                return 2
        elif most_commons[0] == 2:
            if most_commons[1] == 2:
                return 1
            else:
                return 0
        elif most_commons[0] == 1:
            return -1
        raise IOError()

    def compare_hands(hand1, hand2):
        type1 = compute_type(tuple(hand1))
        type2 = compute_type(tuple(hand2))

        if type1 > type2:
            return 1
        elif type1 < type2:
            return -1
        else:
            for c1, c2 in zip(hand1, hand2):
                if c1 > c2:
                    return 1
                if c1 < c2:
                    return -1

        raise IOError()

    def compare_input(x1, x2):
        return compare_hands(x1[0], x2[0])

    def parse_hand(hand):
        ls = []
        for c in hand:
            if c == 'A':
                ls.append(14)
            elif c == 'K':
                ls.append(13)
            elif c == 'Q':
                ls.append(12)
            elif c == 'J':
                ls.append(1)
            elif c == 'T':
                ls.append(10)
            else:
                ls.append(int(c))
        return ls

    all_hands = [(parse_hand(line.split()[0]), int(line.split()[1])) for line in lines]
    sorted_hands = sorted(all_hands, key=cmp_to_key(compare_input), reverse=True)
    print(sorted_hands)

    result = 0
    length = len(all_hands)
    for (i, (_, bid)) in enumerate(sorted_hands):
        rank = length - i
        # print('rank', i, rank)
        result += bid * rank
    return result

input = '''
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
'''

lines = list(input.splitlines()[1:])

if __name__ == '__main__':
    lines = list(sys.stdin.read().splitlines())

    result = process_all(lines)
    print(result)
