import numpy as np
import copy


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


def flip(array, f):
    flipped_array = None
    if f == 0:
        flipped_array = array
    elif f == 1:
        flipped_array = np.flip(array, 0)
    elif f == 2:
        flipped_array = np.flip(array, 1)
    elif f == 3:
        flipped_array = np.flip(array, (0, 1))
    else:
        print('Incorrect number of flips')
    return flipped_array


def rotate(array, r):
    return np.rot90(array, r, axes=(0, 1))


def find_connecting_tile_right(tile, tiles, right_edge):
    # find any that fit on the right of the tile until none do
    for id, t in tiles.items():
        for f in range(4):
            t_flipped = flip(t, f)
            for r in range(4):
                t_rotated = rotate(t_flipped, r)
                t_left = t_rotated[:, 0][::-1]
                if np.array_equal(right_edge, t_left):
                    tile = np.hstack((tile, t_rotated))
                    right_edge = tile[:, -1]
                    del tiles[id]
                    return tile, tiles, right_edge, True
    return tile, tiles, right_edge, False


def find_connecting_tile_left(tile, tiles, left_edge):
    # find any that fit on the left of the tile until none do
    for id, t in tiles.items():
        for f in range(4):
            t_flipped = flip(t, f)
            for r in range(4):
                t_rotated = rotate(t_flipped, r)
                t_right = t_rotated[:, -1]
                if np.array_equal(left_edge, t_right):
                    tile = np.hstack((t_rotated, tile))
                    left_edge = tile[:, 0]
                    del tiles[id]
                    return tile, tiles, right_edge, True
    return tile, tiles, right_edge, False


if __name__ == '__main__':
    filename = 'day_20_example_1.txt'
    tiles = load_input(filename)
    tiles_original = copy.deepcopy(tiles)

    lines = []

    # while tiles left -> choose any tile
    while len(list(tiles.keys())) > 0:
        id = list(tiles.keys())[0]
        tile = tiles[id]
        del tiles[id]

        left_edge = tile[:, 0]
        right_edge = tile[:, -1][::-1]

        found = True
        while found:
            tile, tiles, right_edge, found = find_connecting_tile_right(tile, tiles, right_edge)
        found = True
        while found:
            tile, tiles, left_edge, found = find_connecting_tile_left(tile, tiles, left_edge)

        # todo: if tile is not of the correct size then need to repeat with the initial tile rotated
        lines.append(tile)

    for line in lines:
        print(line)

    print(tiles.keys())
