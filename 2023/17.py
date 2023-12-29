import heapq
import math


def adjacent(current_node, grid_shape, directions, forward_moves, visited):
    direction = directions[current_node[0]][current_node[1]]
    forward_moves = forward_moves[current_node[0]][current_node[1]]

    assert direction in ("u", "d", "l", "r", "s"), f"{direction}"
    assert forward_moves <= 3

    opposites = {
        "u": "d",
        "d": "u",
        "l": "r",
        "r": "l",
        "s": None
    }

    deltas = {
        "d": (1, 0),
        "u": (-1, 0),
        "r": (0, 1),
        "l": (0, -1)
    }

    # Can't go in opposite direction
    if direction != "s":
        del deltas[opposites[direction]]
    # If have moved forward 3 times, can't go forward again
    if forward_moves == 3:
        del deltas[direction]

    new_nodes = []
    new_directions = []
    new_num_forwards = []
    for new_direction, delta in deltas.items():
        new_node = (current_node[0] + delta[0], current_node[1] + delta[1])

        if new_node[0] < 0 or new_node[0] >= grid_shape[0]:
            continue
        if new_node[1] < 0 or new_node[1] >= grid_shape[1]:
            continue
        if visited[new_node[0]][new_node[1]]:
            continue
        new_nodes.append(new_node)
        new_directions.append(new_direction)

        if direction == "s":
            new_num_forwards.append(1)
        elif new_direction == direction:
            new_num_forwards.append(forward_moves + 1)
        else:
            new_num_forwards.append(1)

        # DEBUG
        # if current_node == (0, 5):
        #     print(new_node, direction, new_direction, num_forwards)
        #     print(forward_moves)

    # List of neighboring nodes, the direction they will be reached, the number of forward moves to get there
    return zip(new_nodes, new_directions, new_num_forwards)


def print_grid(grid):
    print()
    for row in grid:
        print("".join([str(i) for i in row]))
    print()


def get_path(previous, start=(-1, -1)):
    path = [start]
    p = previous[start[0]][start[1]]
    while p is not None:
        path.append(p)
        p = previous[p[0]][p[1]]
    path.reverse()
    return path


def print_path(path, grid, directions):

    symbols = {
        "u": "^",
        "d": "v",
        "l": "<",
        "r": ">",
        "s": "o"
    }

    for p in path:
        grid[p[0]][p[1]] = symbols[directions[p[0]][p[1]]]
    for row in grid:
        print("".join([str(i) for i in row]))


if __name__ == '__main__':
    grid = [[int(i) for i in row.strip()] for row in open("17_debug.txt").readlines()]

    grid_shape = (len(grid), len(grid[0]))

    # print(adjacent((0, 0), grid, "r", 0))

    # dijksta's algorithm
    # Queue of nodes to visit - hold the shortest distance to the start node
    # queue = [(100000, (i, j)) for i in range(grid_shape[1]) for j in range(grid_shape[0])]
    # queue[0] = (0, (0, 0))
    queue = [(0, (0, 0))]
    heapq.heapify(queue)
    # current_node = heapq.heappop(queue)  # To pop the shortest distance element from the queue

    # Grid of nodes not visited so can quickly check if still in queue
    visited = [[False for _ in range(grid_shape[1])] for _ in range(grid_shape[0])]

    # Grid of current shortest distances from source mode
    distances = [[math.inf for _ in range(grid_shape[1])] for _ in range(grid_shape[0])]
    distances[0][0] = 0

    # Grid of directions when visiting the node (by the shortest path yet found)
    directions = [[None for _ in range(grid_shape[1])] for _ in range(grid_shape[0])]
    directions[0][0] = "s"  # arb between right/down, START flag below makes sure this count starts correct

    # Keep a grid of num of previous forward moves used when visiting the node (by the shortest path yet found)
    forward_moves = [[0 for _ in range(grid_shape[1])] for _ in range(grid_shape[0])]

    # Keep a grid of previous nodes so can get paths (for debugging)
    previous = [[None for _ in range(grid_shape[1])] for _ in range(grid_shape[0])]

    while queue:
        # Remove the node with the shortest distance to the start node
        current_node = heapq.heappop(queue)
        current_node_distance, current_node_coord = current_node
        # print("Current node", current_node)

        # Iterate through neighbours of current node
        for neighbour in adjacent(current_node_coord, grid_shape, directions, forward_moves, visited):
            # print("neighbour", neighbour)
            node, direction, num_forwards = neighbour
            proposed_distance = grid[node[0]][node[1]] + current_node_distance
            if proposed_distance < distances[node[0]][node[1]]:
                distances[node[0]][node[1]] = proposed_distance
                directions[node[0]][node[1]] = direction
                forward_moves[node[0]][node[1]] = num_forwards
                previous[node[0]][node[1]] = current_node_coord
                # todo: This assumes only pushing to heap when found...ok? Assumes only updated once...
                heapq.heappush(queue, (proposed_distance, tuple(node)))

        visited[current_node_coord[0]][current_node_coord[1]] = True

        # print("QUEUE", queue)

    print("distances")
    for row in distances:
        print(row)

    print()
    print("forward moves")
    for row in forward_moves:
        print("".join([str(i) for i in row]))

    print()
    print("directions")
    for row in directions:
        print("".join(row))

    # print("visited")
    # for row in visited:
    #     print(row)

    # print("previous")
    # for row in previous:
    #     print(row)

    print()
    print("Shortest path")
    shortest_path = get_path(previous)
    print_path(shortest_path, grid, directions)
