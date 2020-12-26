import numpy as np
import itertools


def load_input(filename):
    data = []
    for line in open(filename).readlines():
        l = [1 if x is '#' else 0 for x in line.strip('\n')]
        data.append(l)

    d = np.array(data)
    return d


def initialise_grid(data, num_cycles):
    grid = np.zeros((len(data[0]) + 2*num_cycles, len(data[1]) + 2*num_cycles, 1 + 2*num_cycles))
    grid_shape = grid.shape
    layer_0 = grid_shape[-1] // 2
    # Put the initial data in the middle of the array
    grid[grid_shape[0]//2 : grid_shape[0]//2 + len(data[0]), grid_shape[1]//2 : grid_shape[1]//2 + len(data[1]), layer_0] = data
    return grid, grid_shape


if __name__ == '__main__':
    filename = 'day_17_example_1.txt'
    num_cycles = 6

    data = load_input(filename)
    print('Input layer:')
    for l in data:
        print(l)
    # indexes: [vert][hor]

    grid, grid_shape = initialise_grid(data, num_cycles)

    for cycle in range(num_cycles):
        # use grid_old to check and then update grid
        grid_old = grid[:]
        deltas = list(itertools.product([-1, 0, 1], repeat=3))
        for x in range(grid_shape[0]):
            for y in range(grid_shape[1]):
                for z in range(grid_shape[2]):
                    num_active = 0
                    active = grid_old[x, y, z]
                    for delta in deltas:
                        if 0 <= x + delta[0] < grid_shape[0]:
                            if 0 <= y + delta[1] < grid_shape[1]:
                                if 0 <= z + delta[2] < grid_shape[2]:
                                    if grid_old[x + delta[0], y + delta[1], z + delta[2]]:
                                        num_active += 1
                    if active:
                        if num_active == 2 or num_active == 3:
                            grid[x, y, z] = 1
                        else:
                            grid[x, y, z] = 0
                    else:
                        if num_active == 3:
                            grid[x, y, z] = 1
                        else:
                            grid[x, y, z] = 0

        print(grid[:, :, grid_shape[-1] // 2])
        print(cycle, np.count_nonzero(grid))