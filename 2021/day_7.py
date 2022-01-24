def read_data(filename):
    return [int(i) for i in open(filename).readline().strip().split(',')]


if __name__ == '__main__':
    pos_list = read_data('day_7.txt')
    # print(pos_list)

    # Get counts of each value
    pos_counts = [0] * (max(pos_list) + 1)
    for pos in pos_list:
        pos_counts[pos] += 1
    # print(pos_counts)

    # Brute force - find cost for each possible pos
    min_fuel_cost = 999999
    min_alignment_pos = -1
    for alignment_pos in range(max(pos_list)):
        fuel_cost = 0
        for pos, count in enumerate(pos_counts):
            fuel_cost += abs(pos - alignment_pos) * count
        if fuel_cost < min_fuel_cost:
            min_fuel_cost = fuel_cost
            min_alignment_pos = alignment_pos

    print('best position', min_alignment_pos)
    print('fuel required', min_fuel_cost)
