from collections import Counter


def get_input():
    with open("1.txt") as f:
        a = [[int(i) for i in line.split()] for line in f.readlines()]

    list_1 = []
    list_2 = []
    for row in a:
        list_1.append(row[0])
        list_2.append(row[1])

    return list_1, list_2


def part_1(list_1, list_2):
    list_1_sorted = sorted(list_1)
    list_2_sorted = sorted(list_2)

    total_difference = 0
    for x, y in zip(list_1_sorted, list_2_sorted):
        total_difference += abs(x - y)

    return total_difference


def part_2(list_1, list_2):

    counts = Counter(list_2)

    total = 0
    for i in list_1:
        if i in counts:
            total += i * counts[i]

    return total


if __name__ == '__main__':
    list_1, list_2 = get_input()

    print(part_1(list_1, list_2))
    print(part_2(list_1, list_2))
