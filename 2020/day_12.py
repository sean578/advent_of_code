

def load_input(filename):
    commands, amounts = [], []
    for line in open(filename).readlines():
        line = line.strip('\n')
        command, amount = line[0], int(line[1:])
        commands.append(command)
        amounts.append(amount)
    return commands, amounts


def move(x_0, y_0, angle_0, command, amount):
    angles = ('N', 'E', 'S', 'W')
    if command == 'N':
        x = x_0
        y = y_0 + amount
        angle = angle_0
    elif command == 'S':
        x = x_0
        y = y_0 - amount
        angle = angle_0
    elif command == 'E':
        x = x_0 + amount
        y = y_0
        angle = angle_0
    elif command == 'W':
        x = x_0 - amount
        y = y_0
        angle = angle_0
    elif command == 'L':
        x = x_0
        y = y_0
        angle = (angle_0 - amount // 90) % 4
    elif command == 'R':
        x = x_0
        y = y_0
        angle = (angle_0 + amount // 90) % 4
    elif command == 'F':
        if angle_0 == 0:
            x = x_0
            y = y_0 + amount
        elif angle_0 == 1:
            x = x_0 + amount
            y = y_0
        elif angle_0 == 2:
            x = x_0
            y = y_0 - amount
        elif angle_0 == 3:
            x = x_0 - amount
            y = y_0
        else:
            'Incorrect angle encountered'
        angle = angle_0
    else:
        print('Unknown command encountered')

    return x, y, angle


if __name__ == '__main__':
    filename = 'day_12.txt'
    commands, amounts = load_input(filename)

    x, y, angle = 0, 0, 1  # angle is an index to LUT
    print('Initial position', x, y, angle)
    for c, a in zip(commands, amounts):
        print('Command', c, a)
        x, y, angle = move(x, y, angle, c, a)
        print('New position', x, y, angle)

    print(x, y, angle)
    print('Answer part 1:', abs(x) + abs(y))