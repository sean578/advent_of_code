import numpy as np


def read_grids(lines):

    grids = []
    a_grid = []
    for line in lines:
        if line == "":
            grids.append(a_grid)
            a_grid = []
            continue
        a_grid.append(list(line))
    grids.append(a_grid)

    return grids


def find_smudge(grid):
    # part 2

    # Find consecutive matching rows that match or are off by one
    matching_rows = grid[:-1, :] == grid[1:, :]
    close_rows = np.where(np.count_nonzero(matching_rows == 0, axis=1) <= 1)
    if close_rows[0].shape == (0,):
        return False
    # indices of row before possible reflection line
    close_rows = close_rows[0]

    # Check if a reflection line that requires one change is found from above
    for close_row in close_rows:
        top = grid[:close_row + 1]
        bottom = grid[close_row + 1:]
        top_reversed = top[::-1]
        min_length = min(top.shape[0], bottom.shape[0])
        same = top_reversed[:min_length, :] == bottom[:min_length, :]
        if np.count_nonzero(same == 0) == 1:
            return close_row
    return False


def get_reflection(grid):
    # part 1
    valid = []
    matching_rows = np.where(np.all(grid[:-1, :] == grid[1:, :], axis=1))
    if matching_rows[0].shape == (0,):
        return valid
    # indices of row before possible reflection line
    matching_rows = matching_rows[0]

    # Check if reflections
    for matching_row in matching_rows:
        top = grid[:matching_row + 1]
        bottom = grid[matching_row + 1:]

        top_reversed = top[::-1]
        min_length = min(top.shape[0], bottom.shape[0])
        same = top_reversed[:min_length, :] == bottom[:min_length, :]
        if np.all(same):
            valid.append(matching_row)
    return valid


def print_numpy(grid):
    for row in grid.tolist():
        print("".join(row))


if __name__ == '__main__':

    lines = [line.strip() for line in open("13_input.txt").readlines()]
    grids = read_grids(lines)

    all_row_reflections = []
    all_column_reflections = []
    for i, grid in enumerate(grids):
        grid = np.array(grid)
        close_rows = find_smudge(grid)
        if close_rows is not False:
            all_row_reflections.append(close_rows)
        else:
            close_col = find_smudge(grid.T)
            if close_col is not False:
                all_column_reflections.append(close_col)

    answer = sum([i+1 for i in all_column_reflections]) + 100 * sum(i+1 for i in all_row_reflections)
    print("answer", answer)
