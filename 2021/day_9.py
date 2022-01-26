import numpy as np


def read_data(filename):

    data_list = [[int(i) for i in list(line.strip())] for line in open(filename).readlines()]
    return np.array(data_list, int)


def get_neighbours(data, y, x, size_y, size_x):

    neighbour_vals = []
    neighbour_coords = []
    for delta_x, delta_y in (0, 1), (0, -1), (1, 0), (-1, 0):
        y_new = y + delta_y
        x_new = x + delta_x
        if y_new < size_y and x_new < size_x and y_new >= 0 and x_new >= 0:
            neighbour_vals.append(data[y_new, x_new])
            neighbour_coords.append((y_new, x_new))
    return neighbour_vals, neighbour_coords


def dfs(data, coord, basin_size, size_y, size_x, seen):
    basin_size += 1
    seen.add(coord)

    neighbour_vals, neighbour_coords = get_neighbours(data, coord[0], coord[1], size_y, size_x)
    for nv, nc in zip(neighbour_vals, neighbour_coords):
        if nv != 9 and nc not in seen:
            basin_size = dfs(data, nc, basin_size, size_y, size_x, seen)

    return basin_size


if __name__ == '__main__':
    data = read_data('day_9.txt')
    size_y, size_x = data.shape

    mins = []
    low_points = []
    for y in range(size_y):
        for x in range(size_x):
            neighbours, _ = get_neighbours(data, y, x, size_y, size_x)
            if all(i > data[y, x] for i in neighbours):
                mins.append(data[y, x])
                low_points.append((y, x))
    print('answer part 1:', sum([i+1 for i in mins]))

    # Part 2 plan
    # 1. Keep list of all low point coords from part 1
    # 2. Do DFS starting at each low point.
    #    Valid neighbours are those which are not 9.
    # Assumes there are not multiple low points inside a basin - seems to be true

    basin_sizes = []
    for lp in low_points:
        basin_sizes.append(dfs(data, lp, 0, size_y, size_x, set()))

    basin_sizes.sort(reverse=True)
    print('Answer part 2:', basin_sizes[0] * basin_sizes[1] * basin_sizes[2])
