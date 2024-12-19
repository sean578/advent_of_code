def get_input():
    with open("7.txt") as f:
        rows = [line.strip().split(": ") for line in f.readlines()]

    the_input = []
    for row in rows:
        the_input.append((int(row[0]), [int(i) for i in row[1].split(" ")]))
    return the_input


def possible(target, values):

    if len(values) == 1:
        if values[0] == target:
            return True
        else:
            return False

    if len(values) == 2:
        return possible(target, [values[0] + values[1]]) or possible(target, [values[0] * values[1]])
    else:
        return possible(target, [values[0] + values[1]] + values[2:]) or possible(target, [values[0] * values[1]] + values[2:])


def part_1(the_input):
    calibration = 0
    for row in the_input:
        valid = possible(*row)
        if valid:
            calibration += row[0]

    return calibration


def possible_part_2(target, values):

    if len(values) == 2:
        if target == values[0] + values[1] or target == values[0] * values[1] or target == int(str(values[0]) + str(values[1])):
            return True
        else:
            return False

    return possible_part_2(target, [values[0] + values[1]] + values[2:]) or possible_part_2(target, [values[0] * values[1]] + values[2:]) or possible_part_2(target, [int(str(values[0]) + str(values[1]))] + values[2:])


def part_2(the_input):
    calibration = 0
    for row in the_input:
        valid = possible_part_2(*row)
        if valid:
            calibration += row[0]
    return calibration


if __name__ == '__main__':
    the_input = get_input()
    print(part_1(the_input))
    print(part_2(the_input))
