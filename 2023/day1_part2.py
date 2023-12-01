import sys

if __name__ == '__main__':
    lines = list(sys.stdin.read().splitlines())

    def process(line):
        # Add back the lettered digits to allow reusing them. For instance eightwo should produce
        # 8 and 2 as they share the same "t". Adding back non digits characters is fine as they are
        # filtered then.

        line = line.replace("one", "one1one")\
            .replace("two", "two2two")\
            .replace("three", "three3three")\
            .replace("four", "four4four")\
            .replace("five", "five5five")\
            .replace("six", "six6six")\
            .replace("seven", "seven7seven")\
            .replace("eight", "eight8eight")\
            .replace("nine", "nine9nine")

        print(line)
        digits = [c for c in line if c.isdigit()]
        return int(digits[0]) * 10 + int(digits[-1])

    result = sum(process(line) for line in lines)

    print(result)
