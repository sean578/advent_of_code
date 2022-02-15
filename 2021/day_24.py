def read_data(filename):
    commands = [i.strip().split(' ') for i in open(filename).readlines()]

    return commands


def perform_commands(commands, entry, variables):

    # Each time an input command found use digit from entry
    entry_index = 0
    for c in commands:

        if c[0] == 'inp':
            variables[c[1]] = entry[entry_index]
            entry_index += 1
        else:

            # Get operands
            v = [0, 0]
            for i in range(2):
                if c[i+1] in variables:
                    v[i] = int(variables[c[i+1]])
                else:
                    v[i] = int(c[i+1])

            if c[0] == 'add':
                variables[c[1]] = str(v[0] + v[1])
            elif c[0] == 'mul':
                variables[c[1]] = str(v[0] * v[1])
            elif c[0] == 'div':
                if v[1] == 0:
                    return None
                variables[c[1]] = str(v[0] // v[1])
            elif c[0] == 'mod':
                if v[0] < 0 or v[1] <= 0:
                    return None
                variables[c[1]] = str(v[0] % v[1])
            elif c[0] == 'eql':
                if v[0] == v[1]:
                    variables[c[1]] = 1
                else:
                    variables[c[1]] = 0
            else:
                print('Incorrect command', c)

    return variables


if __name__ == '__main__':
    commands = read_data('day_24.txt')

    # entry = '92915979999498'  # Highest
    entry = '21611513911181'  # Smallest

    variables = {
        'w': '0',
        'x': '0',
        'y': '0',
        'z': '0'
    }

    print('doing:', entry)

    variables = perform_commands(commands, entry, variables)

    if variables:
        if variables['z'] == '0':
            print('We are good')
        else:
            print('Not zero')
    else:
        print('Broken')
