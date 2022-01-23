import copy


def read_data(filename):
    start = open(filename).readline().strip().split(',')
    return [int(i) for i in start]


if __name__ == '__main__':
    num_days = 256
    fish = read_data('day_6.txt')

    # Create a list of counts
    fish_counts = [0]*9
    for f in fish:
        fish_counts[f] += 1

    for t in range(num_days):
        num_zeros_temp = fish_counts[0]
        for i in range(8):
            fish_counts[i] = fish_counts[i + 1]
        fish_counts[6] += num_zeros_temp
        fish_counts[8] = num_zeros_temp

    print('number of fish', sum(fish_counts))
