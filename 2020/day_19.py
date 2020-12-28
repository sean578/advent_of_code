import re
from functools import partial


def load_input(filename):
    rules = {}
    test_strings = []
    for line in open(filename).readlines():
        if ':' in line:
            key, value = line.strip('\n').split(': ')
            v = value.replace('"', '')
            rules[key] = v
        else:
            if len(line.strip()) > 0:
                test_strings.append(line.strip('\n'))
    # New rules for part 2
    rules['8'] = '42 | 42 8'
    rules['11'] = '42 31 | 42 11 31'
    return rules, test_strings


def replace_with_dict_entry(match, dict):
    value = dict[match.group()]
    return '(' + value + ')'


if __name__ == '__main__':
    filename = 'day_19.txt'
    dict, test_strings = load_input(filename)

    instruction = dict['0']
    p = re.compile(r'\d+')
    i = 0
    while p.search(instruction):
        if i == 101:
            break
        instruction = p.sub(partial(replace_with_dict_entry, dict=dict), instruction)
        i += 1

    # get rid of spaces & only match if reach end of string
    instruction = instruction.replace(' ', '') + '$'
    # print('Expanded regular expression:\n', instruction)

    matches = []
    p = re.compile(instruction)
    for string in test_strings:
        if p.match(string):
            matches.append(1)
        else:
            matches.append(0)

    print('Answer part 2:', sum(matches))

