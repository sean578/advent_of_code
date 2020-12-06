from util import load_input


def parse_line(line):
    return line.strip('\n')


def parse_input(input, buffer_size):
    parsed_input = ['' for _ in range(buffer_size)]
    num_ppl = [0] * buffer_size
    entry_num = 0
    for line in input:
        if line == '':
            entry_num += 1
        else:
            parsed_input[entry_num] += line
            num_ppl[entry_num] += 1
    return parsed_input, num_ppl


if __name__ == '__main__':
    filename = 'day_6.txt'
    data = load_input(filename, parse_line)

    answers, num = parse_input(data, 1000)

    sum_all_correct = 0
    for a, n in zip(answers, num):
        num_all_correct = 0
        for c in set(a):
            if a.count(c) == n:
                num_all_correct += 1
        sum_all_correct += num_all_correct
    print(sum_all_correct)
