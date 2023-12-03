import sys

def process(lines):
    def search_number(x, y):
        if x < 0 or y < 0 or y > len(lines) - 1 or x > len(lines[0]) - 1:
            return None

        if not lines[y][x].isdigit():
            return None

        line = lines[y]
        x_min = x
        while x_min - 1 >= 0 and line[x_min - 1].isdigit():
            x_min -= 1

        x_max = x
        while x_max + 1 <= len(line) - 1 and line[x_max + 1].isdigit():
            x_max += 1

        print((x_min, y), (x, y), line[x_min:x_max + 1])

        number = int(line[x_min:x_max + 1])
        return (x_min, y), number

    gears = 0

    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == '*':
                print (x, y, c)

                gear_parts = {}

                for candidate_x, candidate_y in [
                    (x - 1, y),
                    (x + 1, y),
                    (x, y - 1),
                    (x, y + 1),
                    (x - 1, y - 1),
                    (x + 1, y - 1),
                    (x - 1, y + 1),
                    (x + 1, y + 1)]:
                    candidate_number = search_number(candidate_x, candidate_y)
                    if candidate_number:
                        gear_parts[(candidate_number[0])] = candidate_number[1]

                if len(gear_parts) == 2:
                    values = list(gear_parts.values())
                    gear_value = values[0] * values[1]
                    gears += gear_value
                    print(gear_parts, gear_value)

    return gears


if __name__ == '__main__':
    lines = list(sys.stdin.read().splitlines())

    result = process(lines)
    print(result)
