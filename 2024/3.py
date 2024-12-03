import re


def get_input():
    with open("3.txt") as f:
        a = f.read()
    return a


def part_1(string):
    matches = re.findall(r"mul\((\d\d?\d?),(\d\d?\d?)\)", string)

    total = 0
    for match in matches:
        total += int(match[0]) * int(match[1])

    return total


def part_2(string):
    matches = re.findall(r"(mul\((\d\d?\d?),(\d\d?\d?)\))|(do\(\))|(don't\(\))", string)

    on = True
    total = 0
    for match in matches:
        if match[-2]:
            on = True
        elif match[-1]:
            on = False
        else:
            if on:
                total += int(match[1]) * int(match[2])

    return total


if __name__ == '__main__':

    string = get_input()
    print(part_1(string))
    print(part_2(string))
