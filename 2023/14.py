def print_grid(grid):
    print()
    for line in grid:
        print("".join(line))
    print()


def add_border(grid):
    y_length = len(grid)
    x_length = len(grid[0])
    grid.insert(0, ["#"] * x_length)
    grid.append(["#"] * x_length)
    for row in grid:
        row.insert(0, "#")
        row.append("#")
    return grid


def move_rock(grid, y, x):
    # todo: sort out boundaries
    assert grid[y][x] == "O"

    can_move = True
    while can_move:
        if grid[y - 1][x] == ".":
            grid[y - 1][x] = "O"
            grid[y][x] = "."
            y -= 1
        else:
            can_move = False

    return grid


def get_load(grid):
    load = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "O":
                delta_load = len(grid) - y - 1
                load += delta_load
    return load


if __name__ == '__main__':
    grid = [list(line.strip("\n")) for line in open("14_input.txt").readlines()]
    # print_grid(grid)
    grid = add_border(grid)
    # print_grid(grid)

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "O":
                grid = move_rock(grid, y, x)

    # print_grid(grid)
    load = get_load(grid)
    print(load)
