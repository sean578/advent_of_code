def load_input(filename):
    data = None
    commands, values = [], []
    for line in open(filename).readlines():
        line = line.strip('\n')
        command, value = line.split(' = ')
        commands.append(command)
        values.append(value)

    return commands, values


if __name__ == '__main__':
    filename = 'day_14_example_1.txt'
    commands_raw, values = load_input(filename)

    commands = []
    addresses = []
    for c in commands_raw:
        if c != 'mask':
            c, a = c[:-1].split('[')
        else:
            c, a = 'mask', -1
        commands.append(c)
        addresses.append(a)

    for c, a, v in zip(commands, addresses, values):
        print(c, a, v)
