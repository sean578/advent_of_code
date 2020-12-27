import numpy as np
import itertools
import copy


def load_input(filename):
    data = []
    for line in open(filename).readlines():
        l = [1 if x is '#' else 0 for x in line.strip('\n')]
        data.append(l)

    d = np.array(data)
    return d


def initialise_grid(data, num_cycles):
    grid_size = {
        'x': len(data[0]) + 2*num_cycles + 1,
        'y': len(data[1]) + 2*num_cycles + 1,
        'z': len(data[2]) + 2*num_cycles + 1
    }

    print('grid sizes:', grid_size)

    grid = np.zeros((grid_size['x'], grid_size['y'], grid_size['z']))

    # Put the initial data in the middle of the array
    grid[
        (grid_size['x'] - len(data[1])) // 2 : (grid_size['x'] - len(data[1])) // 2 + len(data[0]),
        (grid_size['y'] - len(data[1])) // 2 : (grid_size['y'] - len(data[1])) // 2 + len(data[1]),
        grid_size['z'] // 2,
    ] = data

    return grid, grid_size


def print_grid(grid):
    for z in range(grid.shape[-1]):
        print('z =', z - (len(grid[-1]) // 2))
        print(grid[:, :, z])


if __name__ == '__main__':
    filename = 'day_17.txt'
    num_cycles = 6

    data = load_input(filename)
    # indexes: [vert][hor]

    grid, grid_shape = initialise_grid(data, num_cycles)

    print_grid(grid)
    for cycle in range(num_cycles):
        print('---------------------------------------------------')
        print('cycle', cycle + 1)
        # use grid_old to check and then update grid
        grid_old = copy.deepcopy(grid)
        deltas = list(itertools.product([-1, 0, 1], repeat=3))
        deltas.remove((0, 0, 0))
        for x in range(grid_shape['x']):
            for y in range(grid_shape['y']):
                for z in range(grid_shape['z']):
                    num_active = 0
                    for delta in deltas:
                        x_delta, y_delta, z_delta = x + delta[0], y + delta[1], z + delta[2]
                        if 0 <= x_delta < grid_shape['x'] and \
                           0 <= y_delta < grid_shape['y'] and \
                           0 <= z_delta < grid_shape['z']:
                            if grid_old[x_delta, y_delta, z_delta]:
                                num_active += 1
                    if grid_old[x, y, z]:
                        if num_active < 2 or num_active > 3:
                            grid[x, y, z] = 0
                    else:
                        if num_active == 3:
                            grid[x, y, z] = 1

        print_grid(grid)
    print('Answer:', np.count_nonzero(grid))