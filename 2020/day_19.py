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
    return rules, test_strings


def replace_with_dict_entry(match, dict):
    value = dict[match.group()]
    return '(' + value + ')'


if __name__ == '__main__':
    filename = 'day_19.txt'
    dict, test_strings = load_input(filename)

    instruction = dict['0']
    p = re.compile(r'\d+')
    while p.search(instruction):
        instruction = p.sub(partial(replace_with_dict_entry, dict=dict), instruction)

    # get rid of spaces & only match if reach end of string
    instruction = instruction.replace(' ', '') + '$'
    print('Expanded regular expression:\n', instruction)

    matches = []
    p = re.compile(instruction)
    for string in test_strings:
        if p.match(string):
            matches.append(1)
        else:
            matches.append(0)

    print('Answer part 1:', sum(matches))
