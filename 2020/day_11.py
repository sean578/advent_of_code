from itertools import product
from copy import deepcopy


def load_input(filename):

    with open(filename) as f:
        array = []
        lut = ('.', 'L', '#')
        for line in f.readlines():
            array.append([lut.index(i) for i in line.strip('\n')])

    return array


def do_a_step(data, row, cols):
    # take a deep copy here, create a new array
    next_pattern = deepcopy(data)
    for r in range(rows):
        for c in range(cols):
            # if is a seat we need to check if it changes
            if data[r][c] != 0:
                num_occupied = 0
                for inc in adjacent:
                    row = r + inc[0]
                    col = c + inc[1]
                    # if not outside the edge of the board
                    if 0 <= row < rows and 0 <= col < cols:
                        if data[row][col] == 2:
                            num_occupied += 1

                # if seat empty
                if data[r][c] == 1:
                    if num_occupied == 0:
                        next_pattern[r][c] = 2
                    else:
                        next_pattern[r][c] = 1
                # if seat occupied
                elif data[r][c] == 2:
                    if num_occupied >= 4:
                        next_pattern[r][c] = 1
                    else:
                        next_pattern[r][c] = 2
                else:
                    print('error')

    return next_pattern, data == next_pattern


if __name__ == '__main__':
    filename = 'day_11.txt'
    data = load_input(filename)

    adjacent = list(product([-1, 0, 1], [-1, 0, 1]))
    adjacent.remove((0, 0))

    rows, cols = len(data), len(data[0])

    same = False
    while not same:
        data, same = do_a_step(data, rows, cols)

    total_occupied = 0
    for row in range(rows):
        for col in range(cols):
            if data[row][col] == 2:
                total_occupied += 1

    print('Part 1 answer', total_occupied)