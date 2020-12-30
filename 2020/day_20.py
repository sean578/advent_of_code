import numpy as np
np.set_printoptions(edgeitems=100, linewidth=100000,
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


def find_match_right(current_side, tiles, tile_ids_remaining):
    for id in tile_ids_remaining:
        for r in range(4):
            for f in range(2):
                tile_adj = rotate(tiles[id], r)
                tile_adj = flip(tile_adj, f)
                sides = get_sides(tile_adj)
                if np.array_equal(current_side, sides['left']):
                    return id, r, f, sides['right']
    return None, None, None, None


def find_match_below(current_side, tiles, tile_ids_remaining):
    for id in tile_ids_remaining:
        for r in range(4):
            for f in range(2):
                tile_adj = rotate(tiles[id], r)
                tile_adj = flip(tile_adj, f)
                sides = get_sides(tile_adj)
                if np.array_equal(current_side, sides['top']):
                    return id, r, f, sides['right'], sides['bottom']
    return None, None, None, None, None


def find_tiles(size, tiles, tile_ids_remaining, top_left):

    pic = {
        'grid': np.zeros((num_tiles, num_tiles), dtype=object),
        'rots': np.zeros((num_tiles, num_tiles), dtype=int),
        'flips': np.zeros((num_tiles, num_tiles), dtype=int)
    }

    pic['grid'][0, 0] = top_left

    sides = get_sides(tiles[top_left])
    current_side = sides['right']
    bottom_side = sides['bottom']

    for pos_y in range(size):
        for pos_x in range(1, size):
            id, r, f, current_side = find_match_right(current_side, tiles, tile_ids_remaining)
            pic['grid'][pos_y, pos_x] = id
            pic['rots'][pos_y, pos_x] = r
            pic['flips'][pos_y, pos_x] = f
            tile_ids_remaining.remove(id)

        # Get 1st one in line
        if pos_y < size - 1:
            id, r, f, current_side, bottom_side = find_match_below(bottom_side, tiles, tile_ids_remaining)
            pic['grid'][pos_y + 1, 0] = id
            pic['rots'][pos_y + 1, 0] = r
            pic['flips'][pos_y + 1, 0] = f
            tile_ids_remaining.remove(id)

    return pic


def create_picture(num_tiles, tile_size, tiles, pic):
    # Now create the picture
    picture = np.zeros((num_tiles * tile_size, num_tiles * tile_size))
    for x in range(num_tiles):
        for y in range(num_tiles):

            tile = tiles[pic['grid'][y, x]]
            tile_flipped = flip(tile, pic['flips'][y, x])
            tile_final = rotate(tile_flipped, pic['rots'][y, x])
            picture[x*tile_size : (x+1)*tile_size, y*tile_size : (y+1)*tile_size] = tile_final

            if pic['grid'][y, x] == '1907':
                print('flips', pic['flips'][y, x])
                print('rots', pic['rots'][y, x])
                print('x, y', x, y)
                print(picture)
    return picture


def create_picture_without_gaps(size, tile_size, tiles, pic):
    # Now create the picture
    picture = np.zeros((size*(tile_size-2), size*(tile_size-2)))
    for x in range(size):
        for y in range(size):
            tile = tiles[pic['grid'][y, x]]
            tile_flipped = flip(tile, pic['flips'][y, x])
            tile_final = rotate(tile_flipped, pic['rots'][y, x])
            picture[y*(tile_size-2):(y+1)*(tile_size-2), x*(tile_size-2):(x+1)*(tile_size-2)] = tile_final[1:tile_size-1, 1:tile_size-1]
    return picture


def load_monster(filename):
    monster = []
    for line in open(filename).readlines():
        for i in line.strip('\n'):
            if i == '#':
                monster.append(1)
            else:
                monster.append(0)
    monster = np.array(monster, dtype=int)
    monster = monster.reshape((3, 20))
    return monster


def find_a_top_left_tile(connected_sides, connected_sides_nums):
    for id, num in connected_sides_nums.items():
        if num == 2:
            if 'right' in connected_sides[id]:
                if 'bottom' in connected_sides[id]:
                    return id


if __name__ == '__main__':
    filename = 'day_20.txt'
    # filename = 'day_20_example_1.txt'
    tiles = load_input(filename)
    num_tiles = int(math.sqrt(len(tiles.items())))  # Assume grid square
    tile_size = len(list(tiles.values())[0])
    print('size', num_tiles)
    print('tile_size', tile_size)

    connected_sides_nums, connected_sides = sides(tiles)

    print(tiles['2833'])
    # print(tiles['1907'])

    print(flip(rotate(tiles['1907'], 3), 1))

    # for id, sides in connected_sides.items():
    #     print(id, sides)

    top_left = find_a_top_left_tile(connected_sides, connected_sides_nums)
    print('top_left', top_left)

    tiles_ids_remaining = list(tiles.keys())
    tiles_ids_remaining.remove(top_left)

    pic = find_tiles(num_tiles, tiles, tiles_ids_remaining, top_left)

    print('grid')
    print(pic['grid'])
    print('rots')
    print(pic['rots'])
    print('flips')
    print(pic['flips'])

    picture = create_picture(num_tiles, tile_size, tiles, pic)
    print(picture)
    picture_without_gaps = create_picture_without_gaps(num_tiles, tile_size, tiles, pic)

    # Find sea monsters
    monster = load_monster('day_20_monster.txt')

    monsters_found = []
    for f in range(2):
        for r in range(4):
            pic = flip(picture_without_gaps, f)
            pic = rotate(pic, r)
            found = generic_filter(pic, lambda x: np.all(x), footprint=monster, mode='constant')
            monsters_found.append(np.count_nonzero(found))

    num_monsters = max(monsters_found)
    print('num monsters', num_monsters)
    answer = np.count_nonzero(picture_without_gaps) - 15*num_monsters
    print('Answer part 2:', answer)

    # 2369 too high
