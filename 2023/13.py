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


def get_reflections(grid):
    num_rows = grid.shape[0]
    valid = []

    # Get indices of repeating consecutive lines
    matching_rows = np.where(np.all(grid[:-1, :] == grid[1:, :], axis=1))
    if matching_rows[0].shape == (0,):
        return valid
    matching_rows = matching_rows[0]

    # Check if reflections
    for matching_row in matching_rows:
        if matching_row >= num_rows // 2:
            grid = grid[::-1][:]
            matching_row_reversed = num_rows - matching_row - 2
        else:
            matching_row_reversed = matching_row
        if np.all(
                grid[:matching_row_reversed+1, :][::-1] ==
                grid[matching_row_reversed+1:matching_row_reversed + matching_row_reversed+2, :]
        ):
            valid.append(matching_row)

    assert len(valid) <= 1
    return valid


if __name__ == '__main__':

    lines = [line.strip() for line in open("13_input.txt").readlines()]
    grids = read_grids(lines)

    all_row_reflections = []
    all_column_reflections = []
    for i, grid in enumerate(grids):
        reflection = get_reflections(np.array(grid))
        all_row_reflections.extend(reflection)
        if len(reflection) > 0:
            continue
        reflection = get_reflections(np.array(grid).T)
        all_column_reflections.extend(reflection)
        if len(reflection) == 0:
            print(np.array(grid))
            assert False,  f"{i}"

    answer = sum([i+1 for i in all_column_reflections]) + 100 * sum(i+1 for i in all_row_reflections)
    print(answer)
