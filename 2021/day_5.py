import numpy as np


def read_data(filename):

    d = [line.strip().split(' -> ') for line in open(filename).readlines()]

    e = []
    for i in d:
        e.append([[int(j) for j in i[0].split(',')], [int(j) for j in i[1].split(',')]])

    return e


def get_coord_list(coord):

    x1 = coord[0][0]
    y1 = coord[0][1]
    x2 = coord[1][0]
    y2 = coord[1][1]

    if x2 > x1:
        x = list(range(x1, x2 + 1))
    else:
        x = list(range(x1, x2 - 1, -1))

    if y2 > y1:
        y = list(range(y1, y2 + 1))
    else:
        y = list(range(y1, y2 - 1, -1))

    # If x1 = x2 or y1 = y2 then need to extend so have correct number elements
    if x2 == x1:
        x = len(y) * x
    if y2 == y1:
        y = len(x) * y

    return x, y


if __name__ == '__main__':

    data = read_data('day_5.txt')
    grid_size = 1000

    # For part 1, filter out diagonal lines
    # data_hor = list(filter(lambda d: (d[0][0] == d[1][0]) or (d[0][1] == d[1][1]), data))

    all_coords_x = []
    all_coords_y = []
    for coord in data:
        x, y = get_coord_list(coord)
        all_coords_x += x
        all_coords_y += y

    counts = np.zeros((grid_size, grid_size))
    for x, y in zip(all_coords_x, all_coords_y):
        counts[x, y] += 1

    answer = np.count_nonzero(counts > 1)
    print(answer)
