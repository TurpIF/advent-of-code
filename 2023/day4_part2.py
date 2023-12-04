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

    return nb_match

def process_all(lines):
    nb_cards = {}

    def add_cards(card_id, n):
        if card_id not in nb_cards:
            nb_cards[card_id] = n
        else:
            nb_cards[card_id] += n

    for i, line in enumerate(lines):
        card_id = i + 1
        nb_match = process(line)

        add_cards(card_id, 1)
        nb_current_card = nb_cards[card_id]

        print(card_id, nb_current_card, nb_match, list(range(card_id + 1, card_id + nb_match + 1)))
        for new_card_id in range(card_id + 1, card_id + nb_match + 1):
            add_cards(new_card_id, nb_current_card)

    print(nb_cards)
    return sum(nb_cards.values())


if __name__ == '__main__':
    lines = list(sys.stdin.read().splitlines())

    result = process_all(lines)
    print(result)
