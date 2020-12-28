import numpy as np


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
    return tiles


if __name__ == '__main__':
    filename = 'day_20_example_1.txt'
    tiles = load_input(filename)

    for num, tile in tiles.items():
        print(num)
        print(tile)