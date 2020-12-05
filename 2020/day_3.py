"""
Advent of code - 2020 - Day 3
"""

from functools import reduce


def parse_line(line):
    array = []
    for char in line.strip():
        array.append(char)
    return array


def load_input(filename):
    input = []
    for line in open(filename).readlines():
        input.append(parse_line(line))
    return input


def print_grid(grid):
    for row in grid:
        print(row)


def find_num_trees(grid, num_rows, num_cols, increment):
    num_trees = 0
    i, row, col = 0, 0, 0
    while row < num_rows:
        tree = grid[row][col] == '#'
        if tree:
            num_trees += 1
        i += 1
        row = i*increment[0]
        col = i*increment[1] % num_cols

    return num_trees


if __name__ == '__main__':
    # filename = 'day_3_example_1.txt'
    filename = 'day_3.txt'

    grid = load_input(filename)
    print_grid(grid)

    num_rows = len(grid)
    num_cols = len(grid[0])
    print('num_rows', num_rows)
    print('num_cols', num_cols)

    inc_row_col = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    print('Inc, num_trees')
    num_trees_all = []
    for inc in inc_row_col:
        num_trees = find_num_trees(grid, num_rows, num_cols, inc)
        num_trees_all.append(num_trees)
        print(inc, num_trees)

    print('Answer:', reduce(lambda x, y: x * y, num_trees_all))


