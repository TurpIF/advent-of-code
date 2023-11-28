import sys

if __name__ == '__main__':
    candidates = []
    current_candidate = 0

    for line in sys.stdin.read().splitlines():
        if line:
            current_candidate += int(line)
        else:
            candidates.append(current_candidate)
            current_candidate = 0

    if current_candidate > 0:
        candidates.append(current_candidate)

    top3 = sum(sorted(candidates, reverse=True)[:3])

    print(top3)
