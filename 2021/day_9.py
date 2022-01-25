import numpy as np


def read_data(filename):

    data_list = [[int(i) for i in list(line.strip())] for line in open(filename).readlines()]
    return np.array(data_list, int)


def get_neighbours(data, y, x, size_y, size_x):

    neighbours = []
    for delta_x, delta_y in (0, 1), (0, -1), (1, 0), (-1, 0):
        y_new = y + delta_y
        x_new = x + delta_x
        if y_new < size_y and x_new < size_x and y_new >= 0 and x_new >= 0:
            neighbours.append(data[y_new, x_new])
    return neighbours


if __name__ == '__main__':
    data = read_data('day_9.txt')
    size_y, size_x = data.shape

    mins = []
    for y in range(size_y):
        for x in range(size_x):
            neighbours = get_neighbours(data, y, x, size_y, size_x)
            if all(i > data[y, x] for i in neighbours):
                mins.append(data[y, x])

    print('answer part 1:', sum([i+1 for i in mins]))
