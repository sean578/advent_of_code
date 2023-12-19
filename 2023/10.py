"""
"""

if __name__ == '__main__':
    grid_raw = [list(line.strip()) for line in open("10_input.txt", 'r').readlines()]
    grid_raw.insert(0, ["."]*len(grid_raw[0]))
    grid_raw.append(["."]*len(grid_raw[0]))

    # Add a border of dots so don't have to deal with edge cases
    grid = []
    for l in grid_raw:
        l.insert(0, ".")
        l.append(".")
        grid.append(l)

    # get coords of starting position
    for i, r in enumerate(grid):
        for j, c in enumerate(r):
            if c == "S":
                start = (i, j)
    print(start)

    # Store direction came from as going through maze
    # Then only need to know current symbol to make the move

    symbol_to_dirs = {
        "|": {"n", "s"},
        "-": {"e", "w"},
        "L": {"n", "e"},
        "J": {"n", "w"},
        "7": {"s", "w"},
        "F": {"s", "e"}
    }

    moves = {
        "n": (-1, 0),
        "s": (1, 0),
        "w": (0, -1),
        "e": (0, 1)
    }

    opposites = {
        "n": "s",
        "s": "n",
        "e": "w",
        "w": "e"
    }

    # todo: no manual finding of start!
    node = (51, 41)  # current location
    direction = "e"  # direction have previously moved
    num_moves = 0
    locations = []
    while True:
        locations.append(node)
        # make a move
        pipe_type = grid[node[0]][node[1]]
        num_moves += 1
        if pipe_type == "S":
            break
        (direction,) = symbol_to_dirs[pipe_type] - set(opposites[direction])
        node = (node[0] + moves[direction][0], node[1] + moves[direction][1])

    print("part 1", num_moves / 2)

    # part 2
    visited = [["." for _ in range(len(grid[0]))] for _ in range(len(grid[1]))]
    for location in locations:
        visited[location[0]][location[1]] = "*"
    for v in visited:
        print(" ".join(v))
