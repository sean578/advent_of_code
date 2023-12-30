import heapq


def adjacent(current_node, grid_shape, direction, forward_moves, NUM_ALLOWED_FORWARD=10, MINIMUM_NUM_FORWARD=4):

    assert direction in ("u", "d", "l", "r"), f"{direction}"
    assert forward_moves <= NUM_ALLOWED_FORWARD

    opposites = {
        "u": "d",
        "d": "u",
        "l": "r",
        "r": "l"
    }

    deltas = {
        "d": (1, 0),
        "u": (-1, 0),
        "r": (0, 1),
        "l": (0, -1)
    }

    # Can't go in opposite direction
    del deltas[opposites[direction]]
    # If haven't moved forward MINIMUM_NUM_FORWARD times, have to go forward
    if forward_moves < MINIMUM_NUM_FORWARD:
        deltas = {direction: deltas[direction]}
    # If have moved forward NUM_ALLOWED_FORWARD times, can't go forward again
    if forward_moves == NUM_ALLOWED_FORWARD:
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

        new_nodes.append(new_node)
        new_directions.append(new_direction)

        if new_direction == direction:
            new_num_forwards.append(forward_moves + 1)
        else:
            new_num_forwards.append(1)

    # List of neighboring nodes, the direction they will be reached, the number of forward moves to get there
    return zip(new_nodes, new_directions, new_num_forwards)


if __name__ == '__main__':
    NUM_ALLOWED_FORWARD = 10
    MINIMUM_NUM_FORWARD = 4

    grid = [[int(i) for i in row.strip()] for row in open("17_input.txt").readlines()]
    grid_shape = (len(grid), len(grid[0]))

    # Queue of nodes to visit - hold the shortest distance to the start node
    # distance, coords, num_forwards, last_direction
    queue = [(0, (0, 0), 0, 'r'), (0, (0, 0), 0, 'd')]
    heapq.heapify(queue)

    # Grid of nodes not visited so can quickly check if still in queue
    # (coords, num_forward, direction)
    visited = set()

    while queue:
        # Remove the node with the shortest distance to the start node
        current_node = heapq.heappop(queue)
        current_node_distance, current_node_coord, current_node_num_forwards, current_node_direction = current_node

        # If this is the final node then we are done
        if current_node_coord == (grid_shape[0] - 1, grid_shape[1] - 1):
            if current_node_num_forwards >= 4:
                print(current_node_distance)
                break

        # If we have already visited then we need to pop again
        if (current_node_coord, current_node_num_forwards, current_node_direction) in visited:
            continue
        visited.add((current_node_coord, current_node_num_forwards, current_node_direction))

        # Iterate through neighbours of current node
        for neighbour in adjacent(
                current_node_coord,
                grid_shape,
                current_node_direction,
                current_node_num_forwards,
                NUM_ALLOWED_FORWARD,
                MINIMUM_NUM_FORWARD
        ):
            node, direction, num_forwards = neighbour
            proposed_distance = grid[node[0]][node[1]] + current_node_distance
            # Always add to the queue - if a greater distance than won't be popped (could keep a grid of the best distances so far to keep queue shorter)
            heapq.heappush(queue, (proposed_distance, tuple(node), num_forwards, direction))
