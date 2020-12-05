"""
Advent of code - 2020 - Day 3
"""


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


if __name__ == '__main__':
    # filename = 'day_3_example_1.txt'
    filename = 'day_3.txt'

    grid = load_input(filename)
    print_grid(grid)

    num_rows = len(grid)
    num_cols = len(grid[0])
    print('num_rows', num_rows)
    print('num_cols', num_cols)

    num_trees = 0
    i, row, col = 0, 0, 0
    while row < num_rows:
        tree = grid[row][col] == '#'
        if tree:
            num_trees += 1
        i += 1
        row = i
        col = 3*i % num_cols

    print('num_trees', num_trees)
