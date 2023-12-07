from functools import reduce


def part_1(times, best_distances):
    ways_to_win_all = []
    for time, best_distance in zip(times, best_distances):
        ways_to_win = 0
        for t in range(1, time):
            distance = t * (time - t)
            if distance > best_distance:
                ways_to_win += 1
        ways_to_win_all.append(ways_to_win)
    return reduce(lambda x, y: x * y, ways_to_win_all)


if __name__ == '__main__':
    lines = [line.strip() for line in open("6_input.txt", 'r').readlines()]

    times = [int(i) for i in lines[0].split(":")[1].split()]
    best_distances = [int(i) for i in lines[1].split(":")[1].split()]

    print(part_1(times, best_distances))

