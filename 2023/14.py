import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


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


def move_rock(grid, y, x, direction):
    assert grid[y][x] == "O"

    can_move = True
    while can_move:
        if direction == "north":
            if grid[y - 1][x] == ".":
                grid[y - 1][x] = "O"
                grid[y][x] = "."
                y -= 1
            else:
                can_move = False
        elif direction == "south":
            if grid[y + 1][x] == ".":
                grid[y + 1][x] = "O"
                grid[y][x] = "."
                y += 1
            else:
                can_move = False
        elif direction == "west":
            if grid[y][x - 1] == ".":
                grid[y][x - 1] = "O"
                grid[y][x] = "."
                x -= 1
            else:
                can_move = False
        elif direction == "east":
            if grid[y][x + 1] == ".":
                grid[y][x + 1] = "O"
                grid[y][x] = "."
                x += 1
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
    grid = add_border(grid)

    y_max = len(grid)
    x_max = len(grid[0])

    cycles, loads = [], []
    for cycle in range(300):

        # Move north
        for y in range(y_max):
            for x in range(x_max):
                if grid[y][x] == "O":
                    grid = move_rock(grid, y, x, "north")

        # Move west
        for x in range(x_max):
            for y in range(y_max):
                if grid[y][x] == "O":
                    grid = move_rock(grid, y, x, "west")

        # Move south
        for y in range(y_max-1, -1, -1):
            for x in range(x_max):
                if grid[y][x] == "O":
                    grid = move_rock(grid, y, x, "south")

        # Move east
        for x in range(x_max-1, -1, -1):
            for y in range(y_max):
                if grid[y][x] == "O":
                    grid = move_rock(grid, y, x, "east")

        load = get_load(grid)
        cycles.append(cycle)
        loads.append(load)

    plt.scatter(cycles, loads, s=2)
    plt.show()

    # debug:
    # offset = 10
    # time_period = 7

    # input:
    # Found by looking at plot (offset is arb as long as larger than time for oscillation to begin)
    offset = 150
    time_period = 42

    index = (1000000000 - offset) % time_period
    print(index-1, loads[offset + index - 1])
