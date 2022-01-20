if __name__ == '__main__':
    commands = [line.strip().split() for line in open('day_2.txt').readlines()]

    hor = 0
    depth = 0
    aim = 0

    for dir, amount in commands:
        amount = int(amount)
        if dir == 'up':
            aim -= amount
        elif dir == 'down':
            aim += amount
        elif dir == 'forward':
            hor += amount
            depth += aim*amount
        else:
            print('Incorrect command found.')

    result = hor * depth
    print(result)