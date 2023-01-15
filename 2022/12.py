import copy
import numpy as np


def get_start_index(elevation_map):
    start = 'S'
    start_index = np.argwhere(elevation_map == start)
    assert start_index.shape == (1, 2)
    start_index = tuple(start_index[0, :])
    return start_index


def numeric_elevation(character):
    if character == 'S':
        e = 0
    elif character == 'E':
        e = 25
    else:
        e = ord(character) - 97
    return e


def possible_moves(start_index, elevation_map, visited):
    size_y, size_x = elevation_map.shape
    start_elevation = elevation_map[start_index]

    end_indices = []
    steps = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for step in steps:
        proposal = tuple([sum(x) for x in zip(start_index, step)])
        # check if inside the map
        if proposal[0] < 0 or proposal[0] >= size_y:
            continue
        if proposal[1] < 0 or proposal[1] >= size_x:
            continue
        # check if not too steep
        finish_elevation = elevation_map[proposal]
        if numeric_elevation(finish_elevation) - numeric_elevation(start_elevation) > 1:
            continue
        # check not already visited
        if proposal in visited:
            continue
        end_indices.append(proposal)

    return end_indices


def bfs(start_index, elevation_map):

    layer = -1
    finished = False
    boundary = [start_index]
    visited = [start_index]

    while not finished:
        layer += 1
        print(f"Layer: {layer}")
        print(f"Boundary size = {len(boundary)}")
        print(f"Boundary = {boundary}")
        # If the end index is in the list of possible moves then we are done
        new_boundary = []
        for pos in boundary:
            visited.append(pos)
            if elevation_map[pos] == 'E':
                finished = True
                break
            else:
                new_positions = possible_moves(pos, elevation_map, visited)
                for p in new_positions:
                    new_boundary.append(p)
        boundary = set(new_boundary)

    return layer


if __name__ == '__main__':
    elevation_map = [list(line.strip()) for line in open("12_input.txt").readlines()]
    elevation_map = np.array(elevation_map)
    print(f"Map shape: {elevation_map.shape}")

    # Each step is worth 1.
    # Directed graph, no weights
    # Could have cycles...don't want to visit the same location twice
    # Don't need the path, just the number of steps

    start_index = get_start_index(elevation_map)
    print(bfs(start_index, elevation_map))
