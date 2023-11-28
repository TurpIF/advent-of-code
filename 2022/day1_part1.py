import sys

if __name__ == '__main__':
    max_candidate = 0
    current_candidate = 0

    for line in sys.stdin.read().splitlines():
        if line:
            current_candidate += int(line)
        else:
            if current_candidate > max_candidate:
                max_candidate = current_candidate

            current_candidate = 0

    if current_candidate > max_candidate:
        max_candidate = current_candidate

    print(max_candidate)
