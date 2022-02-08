import numpy as np


def read_data(filename):
    lines = [line.strip().split(' ') for line in open(filename).readlines()]

    instruct = []
    xs = []
    ys = []
    zs = []
    for line in lines:
        instruct.append(line[0])
        x, y, z = line[1].split(',')
        x = x[2:]
        y = y[2:]
        z = z[2:]

        x = tuple([int(i) for i in x.split('..')])
        y = tuple([int(i) for i in y.split('..')])
        z = tuple([int(i) for i in z.split('..')])
        xs.append(x)
        ys.append(y)
        zs.append(z)

    return list(zip(instruct, xs, ys, zs))


def do_instruction(grid, instruction):

    on_off, (x_min, x_max), (y_min, y_max), (z_min, z_max) = instruction

    # Part 1:
    if (x_min < -50) or (x_max > 50) or (y_min < -50) or (y_max > 50) or (z_min < -50) or (z_max > 50):
        print('Skip')
        return grid
    else:
        if on_off == 'on':
            val = 1
        elif on_off == 'off':
            val = 0
        else:
            print('Incorrect on_off:', on_off)

        grid[50+x_min:50+x_max+1, 50+y_min:50+y_max+1, 50+z_min:50+z_max+1] = val
        return grid


if __name__ == '__main__':
    instructions = read_data('day_22.txt')
    for i in instructions:
        print(i)

    size = 101
    grid = np.zeros((size, size, size), np.uint8)
    for i in instructions:
        grid = do_instruction(grid, i)

    answer = np.count_nonzero(grid)
    print('Answer:', answer)
