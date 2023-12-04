import sys


def process(line):
    _, info = line.split(":")
    [winning_part, owning_part] = info.split("|")
    winning_numbers = [int(s) for s in winning_part.split()]
    owning_numbers = {int(s) for s in owning_part.split()}

    nb_match = 0

    for winning_number in winning_numbers:
        if winning_number in owning_numbers:
            nb_match += 1

    if nb_match == 0:
        return 0

    return 2 ** (nb_match - 1)


if __name__ == '__main__':
    lines = list(sys.stdin.read().splitlines())

    result = sum(process(line) for line in lines)
    print(result)
