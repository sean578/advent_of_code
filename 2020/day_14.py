import itertools
from copy import deepcopy


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
    xs = []

    for i, x in enumerate(mask[::-1]):
        if x == '0':
            zeros.append(i)
        elif x == '1':
            ones.append(i)
        elif x == 'X':
            xs.append(i)
        else:
            print('Incorrect mask bit found')
    return zeros, ones, xs


def perform_mask(value, mask_zeros, mask_ones):
    for i in mask_zeros:
        value = int(value) & ~(1 << i)
    for i in mask_ones:
        value = int(value) | (1 << i)
    return value


def perform_mask_part_2(mem_addr, mask_ones, mask_x):

    # First set all bits to one where required
    for i in mask_ones:
        mem_addr = int(mem_addr) | (1 << i)

    # Get all combinations of on/off for the floating bits
    combinations = itertools.product([0, 1], repeat=len(mask_x))

    addresses = []
    for comb in combinations:
        a = deepcopy(mem_addr)
        for i, v in zip(mask_x, comb):
            if v == 0:
                a = a & ~(1 << i)
            elif v == 1:
                a = a | (1 << i)
        addresses.append(a)
    return addresses


if __name__ == '__main__':
    filename = 'day_14.txt'
    commands, addresses, values = load_input(filename)

    mask_zeros, mask_ones, mask_xs = None, None, None
    mem = {}
    for c, a, v in zip(commands, addresses, values):
        if c == 'mask':
            mask_zeros, mask_ones, mask_xs = get_mask_bits(v)
        elif c == 'mem':
            addresses = perform_mask_part_2(int(a), mask_ones, mask_xs)
            for addr in addresses:
                mem[addr] = int(v)
    print('Answer part 2:', sum(mem.values()))
