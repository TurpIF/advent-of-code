import sys

if __name__ == '__main__':
    lines = list(sys.stdin.read().splitlines())

    max_red = 12
    max_green = 13
    max_blue = 14

    BLUE = 'blue'
    RED = 'red'
    GREEN = 'green'

    def process(line):
        [game, triage] = line.split(":")
        game_id = int(game[len("Game "):])

        triage_tokens = [[tokens.split() for tokens in part.split(',')]
                         for part in triage.split(';')]

        is_valid = True
        for token_per_play in triage_tokens:
            remaining = {BLUE: max_blue, RED: max_red, GREEN: max_green}

            for token in token_per_play:
                for color in [BLUE, RED, GREEN]:
                    if token[1] == color:
                        remaining[color] -= int(token[0])

                        if remaining[color] < 0:
                            is_valid = False

        # print(game_id, is_valid)
        return game_id if is_valid else 0

    result = sum(process(line) for line in lines)
    print(result)
