"""
Advent of code - 2020 - Day 4
"""

from util import load_input


def parse_line(line):
        return line.strip()


def parse_input(input, buffer_size):
    parsed_input = [ [] for _ in range(buffer_size) ]
    entry_num = 0
    for line in input:
        if line == '':
            entry_num += 1
        else:
            parsed_input[entry_num] += line.split(' ')
    return parsed_input


if __name__ == '__main__':
    # filename = 'day_4_example_1.txt'
    filename = 'day_4.txt'
    buffer_size = 1000

    valid_entries = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'] #, 'cid']

    input = load_input(filename, parse_line)
    passports = parse_input(input, buffer_size)
    # print(passports)

    num_valid = 0
    for p in passports:
        v = valid_entries[:]
        # print(p)
        for entry in p:
            e = entry.split(':')[0]
            if e in v:
                v.remove(e)
        if len(v) == 0:
            num_valid += 1

    print('Num valid', num_valid)
