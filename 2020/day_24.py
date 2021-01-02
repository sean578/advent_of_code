import copy

def load_input(filename):
    all_instructions = []
    for line in open(filename).readlines():
        instructions = parse_instruction(line.strip())
        all_instructions.append(instructions)
    return all_instructions


def parse_instruction(flips):
    # Get list of instructions from command
    instructions = []
    index = 0
    while index < len(flips):
        if flips[index:index+2] == 'se':
            instructions.append('se')
            index += 2
        elif flips[index:index+2] == 'sw':
            instructions.append('sw')
            index += 2
        elif flips[index:index+2] == 'ne':
            instructions.append('ne')
            index += 2
        elif flips[index:index+2] == 'nw':
            instructions.append('nw')
            index += 2
        elif flips[index] == 'e':
            instructions.append('e')
            index += 1
        elif flips[index] == 'w':
            instructions.append('w')
            index += 1
        else:
            print('Input error', flips)

    return instructions


def num_black_tiles(tile_colors):
    num_black = 0
    for color in tile_colors.values():
        if color:
            num_black += 1
    return num_black


def print_tiles(tile_colors):
    for tile, color in tile_colors.items():
        print(tile, color)


if __name__ == '__main__':
    filename = 'day_24.txt'
    all_instructions = load_input(filename)
    reference_tile = (0, 0)

    moves = {
        'e': (1, 0),
        'w': (-1, 0),
        'ne': (0, 1),
        'nw': (-1, 1),
        'se': (1, -1),
        'sw': (0, -1)
    }

    tile_colors = {}
    for instructions in all_instructions:
        # Do moves
        tile = list(reference_tile)
        for move in instructions:
            x, y = moves[move]
            tile[0] += x
            tile[1] += y
        key = tuple(tile)
        if key in tile_colors.keys():
            tile_colors[key] = not tile_colors[key]  # Flip
        else:
            tile_colors[key] = True  # True = black

    num_black_tiles(tile_colors)

    # Part 2

    for i in range(100):

        # Extend dictionary to include tiles next to 1 black tile
        temp = copy.deepcopy(tile_colors)
        for tile in tile_colors.keys():
            if tile_colors[tile]:
                for x, y in moves.values():
                    if (x + tile[0], y + tile[1]) not in tile_colors.keys():
                        temp[(x + tile[0], y + tile[1])] = False
        tile_colors = temp

        # Go through and do the flipping
        temp = copy.deepcopy(tile_colors)
        for tile in tile_colors.keys():
            count_black = 0
            for x, y in moves.values():
                if (x + tile[0], y + tile[1]) in tile_colors.keys():
                    if tile_colors[(x + tile[0], y + tile[1])]:
                        count_black += 1
            # black
            if tile_colors[tile]:
                if (count_black == 0) or (count_black > 2):
                    temp[tile] = False
            # white
            else:
                if count_black == 2:
                    temp[tile] = True

        tile_colors = temp

    num_black_tiles = num_black_tiles(tile_colors)
    print('Answer part 2:', num_black_tiles)