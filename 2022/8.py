import numpy as np


def part1(b):

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

    return num_visible


if __name__ == '__main__':
    a = [[int(l) for l in line.strip()] for line in open("8_input.txt").readlines()]
    b = np.array(a, dtype=int)

    num_visible = part1(b)
    print("part 1:", num_visible)

    # hold the scenic score of each tree
    c = np.zeros_like(b)
    h, w = b.shape

    # row, col is tree getting score for
    for row in range(h):
        for col in range(w):
            score_down, score_up, score_right, score_left = 0, 0, 0, 0
            current = b[row, col]
            # look down
            for i in range(row + 1, h, 1):
                score_down += 1
                if b[i, col] >= current:
                    break
            # look up
            for i in range(row - 1, -1, -1):
                score_up += 1
                if b[i, col] >= current:
                    break
            # look right
            for i in range(col + 1, w, 1):
                score_right += 1
                if b[row, i] >= current:
                    break
            # look left
            for i in range(col - 1, -1, -1):
                score_left += 1
                if b[row, i] >= current:
                    break

            c[row, col] = score_down * score_up * score_right * score_left

    print("Part 2:", np.max(c))
