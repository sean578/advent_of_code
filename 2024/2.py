import copy


def get_input():
    with open("2.txt") as f:
        a = [[int(i) for i in line.split()] for line in f.readlines()]
    return a


def part_1(rows):
    num_safe = 0
    for row in rows:
        diff = [i - j for i, j in zip(row[1:], row[:-1])]
        if not (all(i > 0 for i in diff) or all(i < 0 for i in diff)):
            continue
        if all(abs(i) <= 3 for i in diff):
            num_safe += 1

    return num_safe


def check_if_ok(row):
    diff = [i - j for i, j in zip(row[1:], row[:-1])]
    if not (all(i > 0 for i in diff) or all(i < 0 for i in diff)):
        return False
    if all(abs(i) <= 3 for i in diff):
        return True
    return False


def part_2(rows):
    num_safe = 0
    for row in rows:
        if check_if_ok(row):
            num_safe += 1
            continue

        # try removals
        for x in range(len(row)):
            r = copy.deepcopy(row)
            r.pop(x)
            if check_if_ok(r):
                num_safe += 1
                break

    return num_safe


if __name__ == '__main__':
    rows = get_input()
    print(part_1(rows))
    print(part_2(rows))
