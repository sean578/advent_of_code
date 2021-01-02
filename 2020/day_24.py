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
            print('Input error', ex_1)

    return instructions


if __name__ == '__main__':
    filename = 'day_24.txt'
    all_instructions = load_input(filename)

    # ex_1 = 'esew'
    # ex_2 = 'nwwswee'
    # flips = ex_2
    # instructions = parse_instruction(flips)
    # print('Instructions', instructions)


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

    num_black = 0
    for color in tile_colors.values():
        if color:
            num_black += 1

    print('Number black:', num_black)
