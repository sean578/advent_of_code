"""
Advent of code - 2020 - Day 4
"""

import re
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


def valid_rules(field, value):
    valid = False
    if field == 'byr':
        if len(value) == 4 and 1920 <= int(value) <= 2002:
            valid = True
    elif field == 'iyr':
        if len(value) == 4 and 2010 <= int(value) <= 2020:
            valid = True
    elif field == 'eyr':
        if len(value) == 4 and 2020 <= int(value) <= 2030:
            valid = True
    elif field == 'hgt':
        print(value)
        # get the numbers from the string
        p = re.compile(r"\d+")
        num = int(p.match(value).group())
        if value[-2:] == 'in':
            if 59 <= num <= 76:
                valid = True
        elif value[-2:] == 'cm':
            if 150 <= num <= 193:
                valid = True
        else:
            print('wierd hgt field found')
    elif field == 'hcl':
        p = re.compile(r"\#[a-z0-9]{6}")
        if p:
            valid = True
    elif field == 'ecl':
        if value in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
            valid = True
    elif field == 'pid':
        pass ###### a nine-digit number, including leading zeroes
    # elif field == 'cid':
    #     pass

    return valid


if __name__ == '__main__':
    filename = 'day_4_example_1.txt'
    # filename = 'day_4.txt'
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
            field, value = entry.split(':')
            if field in v:
                # todo: add check if value is valid
                if valid_rules(field, value):
                    v.remove(field)
        if len(v) == 0:
            num_valid += 1

    print('Num valid', num_valid)
