from collections import defaultdict
from shapely.geometry import Polygon, JOIN_STYLE


DIRECTIONS = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1)
}


def create_map(lines, offset=(0, 0)):
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

    pos = offset  # row, col, # Played around with this to get looking even
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


def flood_fill(grid, grid_shape, coord_start=(1, 1)):
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
            if 0 <= new_coord[0] < grid_shape[0] and 0 <= new_coord[1] < grid_shape[1]:
                queue.append(new_coord)

    return grid


def count(grid):
    total = 0
    for row in grid:
        for item in row:
            if item in ("#", "X"):
                total += 1
    return total


def get_instructions_part_2(lines):
    directions = {
        0: "R",
        1: "D",
        2: "L",
        3: "U"
    }
    instructions = []
    for line in lines:
        bit = line[-1][2:-1]
        distance_hex = bit[:-1]
        distance = int(distance_hex, 16)
        direction_int = int(bit[-1])
        direction = directions[direction_int]
        instructions.append((direction, distance))
    return instructions


def get_polygon(instructions, start_coord=(0, 0)):

    pos = start_coord
    polygon = [pos]
    for direction, distance in instructions:
        delta = [distance * unit for unit in DIRECTIONS[direction]]
        pos = (pos[0] + delta[0], pos[1] + delta[1])
        polygon.append(pos)

    return polygon


if __name__ == '__main__':
    lines = [line.strip().split() for line in open("18_input.txt").readlines()]

    # Used for part 1
    # grid = create_map(lines, offset=(0, 0))
    # grid_shape = (len(grid), len(grid[0]))
    # print_grid(grid)
    # grid = flood_fill(grid, grid_shape, coord_start=(100, 100))  # Played with start to get inside
    # total = count(grid)

    # idea for part 2: parse input into list of (x, y) coords (polygon) + then find area
    # (x, y) are start & end of each dig line
    instructions = get_instructions_part_2(lines)
    polygon = Polygon(get_polygon(instructions))
    area = polygon.buffer(0.5, join_style=JOIN_STYLE.mitre).area
    print(int(area))
