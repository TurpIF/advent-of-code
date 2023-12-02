import sys

if __name__ == '__main__':
    lines = list(sys.stdin.read().splitlines())

    BLUE = 'blue'
    RED = 'red'
    GREEN = 'green'

    def process(line):
        [game, triage] = line.split(":")
        game_id = int(game[len("Game "):])

        triage_tokens = [[tokens.split() for tokens in part.split(',')]
                         for part in triage.split(';')]

        max_quantity = {BLUE: 0, RED: 0, GREEN: 0}

        for token_per_play in triage_tokens:

            for token in token_per_play:
                for color in [BLUE, RED, GREEN]:
                    if token[1] == color:
                        max_quantity[color] = max(int(token[0]), max_quantity[color])

        power = max_quantity[BLUE] * max_quantity[RED] * max_quantity[GREEN]

        print(game_id, power, max_quantity)
        return power

    result = sum(process(line) for line in lines)
    print(result)
