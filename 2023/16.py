import copy


move_delta = {
    "u": (-1, 0),
    "d": (1, 0),
    "l": (0, -1),
    "r": (0, 1),
}


def move(direction, location, grid_shape):
    # Return the new location (direction unchanged)
    # Return false if have left the grid

    assert direction in move_delta

    delta = move_delta[direction]

    location[0] += delta[0]
    location[1] += delta[1]

    if location[0] < 0 or location[0] >= grid_shape[0]:
        return False
    if location[1] < 0 or location[1] >= grid_shape[1]:
        return False

    return location


def change_direction(direction, device):

    # Empty space
    if device == ".":
        return direction, None

    # Mirrors
    if device == "\\":
        if direction == "r":
            return "d", None
        if direction == "l":
            return "u", None
        if direction == "d":
            return "r", None
        if direction == "u":
            return "l", None
    if device == "/":
        if direction == "r":
            return "u", None
        if direction == "l":
            return "d", None
        if direction == "d":
            return "l", None
        if direction == "u":
            return "r", None

    # Splitters
    if device == "-":
        if direction in ("l", "r"):
            return direction, None
        if direction == "d":
            return "l", "r"
        if direction == "u":
            return "r", "l"

    if device == "|":
        if direction in ("u", "d"):
            return direction, None
        if direction == "l":
            return "d", "u"
        if direction == "r":
            return "u", "d"

    assert False


def print_grid(grid):
    print()
    for row in grid:
        print("".join(row))
    print()


if __name__ == '__main__':
    grid = [list(line.strip()) for line in open("16_input.txt").readlines()]
    # print_grid(grid)
    grid_shape = (len(grid), len(grid[0]))

    starting_point_queue = [([0, 0], "r")]
    locations_visited = set()
    location_and_direction_visited = set()

    while len(starting_point_queue) > 0:
        location, direction = starting_point_queue.pop()
        if not location:
            break

        # Keep moving until beam has left the grid
        while True:
            # Stop if we have been at the location in this direction before (cycles)
            if (tuple(location), direction) in location_and_direction_visited:
                break

            locations_visited.add(tuple(location))
            location_and_direction_visited.add((tuple(location), direction))

            direction_change = change_direction(direction, grid[location[0]][location[1]])
            direction, starting_point_direction = direction_change
            location_original = copy.deepcopy(location)
            location = move(direction, location, grid_shape)

            if starting_point_direction is not None:
                new_starting_point_location = move(starting_point_direction, location_original, grid_shape)
                starting_point_queue.insert(
                    0, (new_starting_point_location, starting_point_direction)
                )
            if not location:
                break

    print(len(locations_visited))
