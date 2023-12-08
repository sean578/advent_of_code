from functools import reduce
import math


def part_1(times, best_distances):
    distances = []
    ways_to_win_all = []
    for time, best_distance in zip(times, best_distances):
        ways_to_win = 0
        for t in range(1, time):
            distance = t * (time - t)
            distances.append(distance)
            if distance > best_distance:
                ways_to_win += 1
        ways_to_win_all.append(ways_to_win)
    return reduce(lambda x, y: x * y, ways_to_win_all), distances


if __name__ == '__main__':
    lines = [line.strip() for line in open("6_input.txt", 'r').readlines()]

    times = [int(i) for i in lines[0].split(":")[1].split()]
    best_distances = [int(i) for i in lines[1].split(":")[1].split()]

    answer, _ = part_1(times, best_distances)

    time = int("".join(lines[0].split(":")[1].split()))
    best_distance = int("".join(lines[1].split(":")[1].split()))

    # Brute force part 2...
    # answer, distances = part_1([time], [best_distance])

    # Part 2 efficient
    # distance = v*t
    # distance = hold_time(total_time - hold_time)
    crossing_point_1 = math.ceil((time - math.sqrt(time ** 2 - 4 * best_distance)) / 2)
    crossing_point_2 = math.floor((time + math.sqrt(time ** 2 - 4 * best_distance)) / 2)

    print(crossing_point_2 - crossing_point_1 + 1)
