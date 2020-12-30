import numpy as np
np.set_printoptions(edgeitems=30, linewidth=100000,
    formatter=dict(float=lambda x: "%.3g" % x))
from collections import defaultdict
import math
from scipy.ndimage import generic_filter


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


def get_sides(tile):
    sides = {}
    sides['top'] = tile[0, :]
    sides['bottom'] = tile[-1, :]
    sides['left'] = tile[:, 0]
    sides['right'] = tile[:, -1]
    return sides


def sides(tiles):
    # Get the corner tiles, also which sides are connected
    connected_sides_nums = {}
    connected_sides = defaultdict(list)

    for id_1, our_tile in tiles.items():
        our_sides = get_sides(our_tile)
        side_count = 0
        for id_2, other_tile in tiles.items():
            if id_1 != id_2:
                their_sides = get_sides(other_tile)
                for side_1, s1 in our_sides.items():
                    for s2 in their_sides.values():
                        if np.array_equal(s1, s2):
                            side_count += 1
                            connected_sides[id_1].append(side_1)
                their_sides = get_sides(flip(other_tile, 3))
                for side_1, s1 in our_sides.items():
                    for s2 in their_sides.values():
                        if np.array_equal(s1, s2):
                            side_count += 1
                            connected_sides[id_1].append(side_1)
        connected_sides_nums[id_1] = side_count

    return connected_sides_nums, connected_sides


def find_match_right(current_side, tiles, tiles_left):
    id, r, f = None, None, None
    for id in tiles_left:
        for r in range(4):
            for f in range(2):
                tile_adj = rotate(tiles[id], r)
                tile_adj = flip(tile_adj, f)
                sides = get_sides(tile_adj)
                if np.array_equal(current_side, sides['left']):
                    return id, r, f, sides['right']
    return None, None, None, None


def find_match_below(current_side, tiles, tiles_left):
    id, r, f = None, None, None
    for id in tiles_left:
        for r in range(4):
            for f in range(2):
                tile_adj = rotate(tiles[id], r)
                tile_adj = flip(tile_adj, f)
                sides = get_sides(tile_adj)
                if np.array_equal(current_side, sides['top']):
                    return id, r, f, sides['right']
    return None, None, None, None


def find_tiles(size, current_side, below_side, tiles, tiles_left):
    for pos_y in range(size):
        for pos_x in range(1, size):
            id, r, f, side = find_match_right(current_side, tiles, tiles_left)
            grid[pos_y, pos_x] = id
            rots[pos_y, pos_x] = r
            flips[pos_y, pos_x] = f
            tiles_left.remove(id)
            current_side = side

        # Get 1st one in line
        if pos_y < size - 1:
            id, r, f, _ = find_match_below(below_side, tiles, tiles_left)
            grid[pos_y + 1, 0] = id
            rots[pos_y + 1, 0] = r
            flips[pos_y + 1, 0] = f
            sides = get_sides(tiles[id])
            current_side = sides['right']
            below_side = sides['bottom']
            tiles_left.remove(id)
    return grid, rots, flips


def create_picture(size, tile_size, tiles, grid, flips, rots):
    # Now create the picture
    picture = np.zeros((size*tile_size, size*tile_size))
    for x in range(size):
        for y in range(size):
            tile = tiles[grid[y, x]]
            tile_flipped = flip(tile, flips[y, x])
            tile_final = rotate(tile_flipped, rots[y, x])
            picture[y*tile_size:(y+1)*tile_size, x*tile_size:(x+1)*tile_size] = tile_final
    return picture


def create_picture_without_gaps(size, tile_size, tiles, grid, flips, rots):
    # Now create the picture
    picture = np.zeros((size*(tile_size-2), size*(tile_size-2)))
    for x in range(size):
        for y in range(size):
            tile = tiles[grid[y, x]]
            tile_flipped = flip(tile, flips[y, x])
            tile_final = rotate(tile_flipped, rots[y, x])
            picture[y*(tile_size-2):(y+1)*(tile_size-2), x*(tile_size-2):(x+1)*(tile_size-2)] = tile_final[1:tile_size-1, 1:tile_size-1]
    return picture


def load_monster(filename):
    monster = []
    for line in open(filename).readlines():
        # l = line.strip('\n')
        for i in line.strip('\n'):
            if i == '#':
                monster.append(1)
            else:
                monster.append(0)
    monster = np.array(monster, dtype=int)
    monster = monster.reshape((3, 20))
    return monster


def find_monster(buffer):
    # print('buffer', buffer)
    if np.all(buffer):
        return 1
    else:
        return 0


if __name__ == '__main__':
    filename = 'day_20_example_1.txt'
    tiles = load_input(filename)
    size = int(math.sqrt(len(tiles.items())))  # Assume grid square
    tile_size = len(list(tiles.values())[0])
    print('size', size)
    print('tile_size', tile_size)

    connected_sides_nums, connected_sides = sides(tiles)

    top_left = '2971'  # todo: find this automatically from above dicts
    tiles_left = list(tiles.keys())
    tiles_left.remove(top_left)

    grid = np.zeros((size, size), dtype=object)
    rots = np.zeros((size, size), dtype=int)
    flips = np.zeros((size, size), dtype=int)
    grid[0, 0] = top_left
    sides = get_sides(tiles[top_left])
    current_side = sides['right']
    below_side = sides['bottom']

    grid, rots, flips = find_tiles(size, current_side, below_side, tiles, tiles_left)
    picture = create_picture(size, tile_size, tiles, grid, flips, rots)
    picture_without_gaps = create_picture_without_gaps(size, tile_size, tiles, grid, flips, rots)

    # Do any rotations/flips of the final picture
    picture = flip(picture, 1)
    picture_without_gaps = flip(picture_without_gaps, 1)
    print(picture_without_gaps)

    # Find sea monsters
    monster = load_monster('day_20_monster.txt')
    print(np.array(monster, dtype=int))

    monsters_found = []
    for f in range(2):
        for r in range(4):
            pic = flip(picture_without_gaps, f)
            pic = rotate(pic, r)
            found = generic_filter(pic, find_monster, footprint=monster, mode='constant')
            monsters_found.append(np.count_nonzero(found))

    num_monsters = max(monsters_found)
    print('num monsters', num_monsters)
    answer = np.count_nonzero(picture_without_gaps) - 15*num_monsters
    print('Answer part 2:', answer)