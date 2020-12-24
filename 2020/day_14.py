def load_input(filename):
    data = None
    commands_raw, values = [], []
    for line in open(filename).readlines():
        line = line.strip('\n')
        command, value = line.split(' = ')
        commands_raw.append(command)
        values.append(value)

    commands = []
    addresses = []
    for c in commands_raw:
        if c != 'mask':
            c, a = c[:-1].split('[')
        else:
            c, a = 'mask', -1
        commands.append(c)
        addresses.append(a)

    return commands, addresses, values


def get_mask_bits(mask):
    zeros = []
    ones = []

    for i, x in enumerate(mask[::-1]):
        if x == '0':
            zeros.append(i)
        elif x == '1':
            ones.append(i)
    return zeros, ones


def perform_mask(value, mask_zeros, mask_ones):
    for i in mask_zeros:
        value = int(value) & ~(1 << i)
    for i in mask_ones:
        value = int(value) | (1 << i)
    return value


if __name__ == '__main__':
    filename = 'day_14.txt'
    commands, addresses, values = load_input(filename)

    mask_zeros, mask_ones = None, None
    mem = [0]*100000
    for c, a, v in zip(commands, addresses, values):
        if c == 'mask':
            mask_zeros, mask_ones = get_mask_bits(v)
        elif c == 'mem':
            value = perform_mask(v, mask_zeros, mask_ones)
            mem[int(a)] = value

    print('Answer part 1:', sum(mem))