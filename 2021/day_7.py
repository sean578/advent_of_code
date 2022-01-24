import math


def read_data(filename):
    return [int(i) for i in open(filename).readline().strip().split(',')]


if __name__ == '__main__':
    pos_list = read_data('day_7.txt')

    # Get counts of each value
    pos_counts = [0] * (max(pos_list) + 1)
    for pos in pos_list:
        pos_counts[pos] += 1

    # Brute force - find cost for each possible pos
    min_fuel_cost = math.inf
    min_alignment_pos = -1
    for alignment_pos in range(max(pos_list)):
        fuel_cost = 0
        for pos, count in enumerate(pos_counts):
            n = abs(pos - alignment_pos)
            fuel_cost += count * ((n + 1) * n / 2)
            # Part 1
            # fuel_cost += abs(pos - alignment_pos) * count
        if fuel_cost < min_fuel_cost:
            min_fuel_cost = fuel_cost
            min_alignment_pos = alignment_pos

    print('best position', min_alignment_pos)
    print('fuel required', int(min_fuel_cost))
