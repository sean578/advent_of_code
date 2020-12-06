from util import load_input


def parse_line(line):
    return line.strip('\n')


def parse_input(input, buffer_size):
    parsed_input = ['' for _ in range(buffer_size)]
    print(parsed_input)
    entry_num = 0
    for line in input:
        if line == '':
            entry_num += 1
        else:
            parsed_input[entry_num] += line
    return parsed_input


if __name__ == '__main__':
    filename = 'day_6.txt'
    data = load_input(filename, parse_line)

    for l in data:
        print(l)

    data_parsed = parse_input(data, 1000)

    counts = 0
    for d in data_parsed:
        counts += len(set(d))
    print(counts)
