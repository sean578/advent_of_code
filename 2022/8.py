import numpy as np


if __name__ == '__main__':
    a = [[int(l) for l in line.strip()] for line in open("8_input.txt").readlines()]
    b = np.array(a, dtype=int)

    c = np.zeros_like(b)
    h, w = b.shape

    num_visible = 0
    for row in range(h):
        for col in range(w):
            # looking down
            v = b[row, col]
            y = False
            if row == 0 or col == 0 or row == h-1 or col == w-1:
                y = True
            elif np.all(b[:row, col] < v):
                y = True
            elif np.all(b[row+1:, col] < v):
                y = True
            elif np.all(b[row, :col] < v):
                y = True
            elif np.all(b[row, col+1:] < v):
                y = True
            if y == True:
                num_visible += 1

    print(num_visible)
