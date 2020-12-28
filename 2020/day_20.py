import numpy as np
from collections import defaultdict


def load_input(filename):
    tiles = {}
    tile, tile_num = None, None
    for line in open(filename).readlines():
        if line[:4] == 'Tile':
            tile = []
            _, tile_num = line.strip(':\n').split()
        else:
            l_stripped = line.strip()
            if l_stripped:
                tile.append([1 if x == '#' else 0 for x in l_stripped])
            else:
                tiles[tile_num] = np.array(tile)
        tiles[tile_num] = np.array(tile)
    return tiles


def get_outer(array):
    outer = [
        array[:, 0],
        array[:, -1],
        array[0, :],
        array[-1, :]
    ]
    return outer


if __name__ == '__main__':
    filename = 'day_20.txt'
    tiles = load_input(filename)

    # Get possible outers
    outers = defaultdict(list)
    all_outers = []
    for num, tile in tiles.items():
        outer = get_outer(tile)
        for i in outer:
            outers[num].append(i)
            all_outers.append(i)

    # Get number matches per tile
    matches = {}

    for id, edges in outers.items():
        m = 0
        for e in edges:
            for a in all_outers:
                if list(e) == list(a):
                    m += 1
                if list(e[::-1]) == list(a):
                    m += 1
        matches[id] = m - 4

    for key, value in matches.items():
        print(key, value)

    minimum = min(matches.values())

    corner_tiles = []
    for key, value in matches.items():
        if value == minimum:
            corner_tiles.append(key)

    print(corner_tiles)

    answer = 1
    for a in [int(i) for i in corner_tiles]:
        answer *= a
    print('Answer part 1:', answer)