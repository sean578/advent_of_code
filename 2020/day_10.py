from util import load_input


def parse_line(line):
    return int(line.strip('\n'))


if __name__ == '__main__':
    filename = 'day_10.txt'
    data = load_input(filename, parse_line)

    data.sort()
    data.append(data[-1] + 3)
    data.insert(0, 0)

    print(data)
    diffs = []
    for x, y in zip(data, data[1:]):
        diffs.append(y-x)

    counts = {}
    for value in set(diffs):
        count = diffs.count(value)
        counts[value] = count

    print(counts)

    answer = counts[1] * counts[3]
    print(answer)
