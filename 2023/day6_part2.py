import sys

def process_all(lines):
    times = [int(lines[0].split(':')[1].replace(' ', ''))]
    distances = [int(lines[1].split(':')[1].replace(' ', ''))]

    nb_wins = []
    for time, distance in zip(times, distances):
        nb_win = 0
        for holding_time in range(time):
            travel_distance = (time - holding_time) * holding_time

            if travel_distance > distance:
                # print(time, distance, holding_time, travel_distance)
                nb_win += 1
        nb_wins.append(nb_win)

    result = 1
    for nb_win in nb_wins:
        result *= nb_win

    print(result)
    return result

input = '''
Time:        53     71     78     80
Distance:   275   1181   1215   1524
'''

lines = list(input.splitlines()[1:])

if __name__ == '__main__':
    #lines = list(sys.stdin.read().splitlines())

    result = process_all(lines)
    print(result)
