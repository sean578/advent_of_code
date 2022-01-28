import numpy as np
np.set_printoptions(edgeitems=30, linewidth=100000,
    formatter=dict(float=lambda x: "%.3g" % x))
import matplotlib.pyplot as plt

def read_data(filename):
    data = [line.strip() for line in open(filename).readlines()]
    dots = []
    folds = []
    for line in data:
        if ',' in line:
            i, j = line.split(',')
            dots.append((int(i), int(j))) # x, y

        elif 'fold' in line:
            i, j = line.split('=')
            folds.append((i[-1], int(j)))

    return dots, folds


def create_initial_array(dots):
    # dots: x, y

    size_x = max([i[0] for i in dots]) + 1
    size_y = max([i[1] for i in dots]) + 1

    array = np.zeros((size_y, size_x), np.uint8)

    for dot in dots:
        array[dot[1], dot[0]] = 1

    return array


def apply_fold(fold, paper):
    dir, index = fold
    # dir = 'y' means 'up
    # dir = 'x' means left

    if dir == 'y':
        # Separate out the two sections
        a = paper[:index, :]
        b = paper[index+1:, :]

        # Reverse one section
        b = np.flipud(b)

    elif dir == 'x':
        # Separate out the two sections
        a = paper[:, :index]
        b = paper[:, index+1:]

        # Reverse one section
        b = np.fliplr(b)

    # Or the sections
    paper = np.logical_or(a, b)
    paper = paper.astype(np.uint8)

    return paper


if __name__ == '__main__':
    dots, folds = read_data('day_13.txt')
    paper = create_initial_array(dots)
    print('Initial paper:\n', paper)

    for i, fold in enumerate(folds):
        print('Fold', i, fold)
        paper = apply_fold(fold, paper)
        num_dots = np.count_nonzero(paper)
        print('Num dots:', num_dots)

    plt.imshow(paper)
    plt.show()