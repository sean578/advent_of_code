def load_input(filename):
    commands, amounts = [], []
    for line in open(filename).readlines():
        line = line.strip('\n')
        command, amount = line[0], int(line[1:])
        commands.append(command)
        amounts.append(amount)
    return commands, amounts


def move(x_0, y_0, x_ship_0, y_ship_0, command, amount):
    """
    Args:
        x_0: x position of waypoint (rel. to ship)
        y_0: y position of waypoint (rel. to ship)
        x_ship_0: x postion of ship
        y_ship_0: y position of ship
    """

    x_ship = x_ship_0
    y_ship = y_ship_0
    x = x_0
    y = y_0

    if command == 'N':
        x = x_0
        y = y_0 + amount
    elif command == 'S':
        x = x_0
        y = y_0 - amount
    elif command == 'E':
        x = x_0 + amount
        y = y_0
    elif command == 'W':
        x = x_0 - amount
        y = y_0
    elif command == 'L':
        for _ in range(amount // 90):
            x = -y_0
            y = x_0
            x_0 = x
            y_0 = y
    elif command == 'R':
        for _ in range(amount // 90):
            x = y_0
            y = -x_0
            x_0 = x
            y_0 = y
    elif command == 'F':
        x_ship = x_ship_0 + x_0 * amount
        y_ship = y_ship_0 + y_0 * amount
    else:
        print('Unknown command encountered')

    return x, y, x_ship, y_ship


if __name__ == '__main__':
    filename = 'day_12.txt'
    commands, amounts = load_input(filename)

    x, y = 10, 1
    x_ship, y_ship = 0, 0
    print('Initial position', x, y, x_ship, y_ship)

    for c, a in zip(commands, amounts):
        print('Command', c, a)
        x, y, x_ship, y_ship = move(x, y, x_ship, y_ship, c, a)
        print('New position', x, y, x_ship, y_ship)

    print('Answer part 2:', abs(x_ship) + abs(y_ship))
