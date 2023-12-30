from collections import defaultdict

DIRECTIONS = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1)
}


def create_map(lines):
    instructions = []
    for line in lines:
        direction, steps, color = line
        instructions.append(
            {
                "direction": direction,
                "steps": int(steps),
                "color": color
            }
        )

    pos = (0, 0)  # row, col
    rows = defaultdict(list)
    rows[pos[0]].append(pos[1])

    for instruction in instructions:
        direction, steps = instruction["direction"], instruction["steps"]
        move = DIRECTIONS[direction]
        for step in range(steps):
            pos = (pos[0] + move[0], pos[1] + move[1])
            rows[pos[0]].append(pos[1])

    max_cols = 0
    for row, cols in rows.items():
        if max(cols) >= max_cols:
            max_cols = max(cols) + 1

    grid = [["." for _ in range(max_cols)] for _ in range(len(rows))]
    for row, cols in rows.items():
        for col in cols:
            grid[row][col] = "#"
    return grid


def print_grid(grid):

    for row in grid:
        print("".join(row))


def flood_fill(grid, coord_start=(1, 1)):
    queue = [coord_start]
    while len(queue) > 0:
        coord = queue.pop(0)

        if grid[coord[0]][coord[1]] in ("#", "X"):
            # Reached border or filled already
            continue

        # Fill the current coord
        grid[coord[0]][coord[1]] = "X"

        # Call function all all valid neighbours
        for delta in DIRECTIONS.values():
            new_coord = (coord[0] + delta[0], coord[1] + delta[1])
            # circular so don't worry about edges
            # if 0 <= new_coord[0] < grid_shape[0] and 0 <= new_coord[1] < grid_shape[1]:
            queue.append(new_coord)

    return grid


def count(grid):
    total = 0
    for row in grid:
        for item in row:
            if item in ("#", "X"):
                total += 1
    return total


if __name__ == '__main__':
    lines = [line.strip().split() for line in open("18_input.txt").readlines()]

    grid = create_map(lines)
    grid = flood_fill(grid, coord_start=(1, 1))
    # print()
    # print_grid(grid)

    total = count(grid)
    print(total)
