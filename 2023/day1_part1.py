import sys

if __name__ == '__main__':
    lines = list(sys.stdin.read().splitlines())

    def process(line):
        digits = [c for c in line if c.isdigit()]
        return int(digits[0]) * 10 + int(digits[-1])

    result = sum(process(line) for line in lines)

    print(result)
