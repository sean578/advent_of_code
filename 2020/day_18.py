import re


def parse_input(filename):
    data = []
    for line in open(filename).readlines():
        data.append(line.strip('\n'))
    return data


def get_expression_index(string):
    l_bracket = max([pos for pos, c in enumerate(string) if c == '('])
    r_bracket = string[l_bracket:].find(')') + l_bracket
    return l_bracket, r_bracket


def replace(string, l_bracket, r_bracket, new_string):
    return string[:l_bracket] + new_string + string[r_bracket+1:]


def do_all_calcs(string):
    while '+' in string:
        match = re.search(r'\d+\s+\+\s+\d+', string)
        string = string.replace(match.group(0), str(eval(match.group(0))), 1)
    while '*' in string:
        match = re.search(r'\d+\s+\*\s+\d+', string)
        string = string.replace(match.group(0), str(eval(match.group(0))), 1)
    return string


if __name__ == '__main__':

    data = parse_input('day_18.txt')
    answer = []
    for i, d in enumerate(data):
        while '(' in d:
            l_bracket, r_bracket = get_expression_index(d)
            z = do_all_calcs(d[l_bracket+1: r_bracket])
            d = replace(d, l_bracket, r_bracket, z)
        d = do_all_calcs(d)
        answer.append(d)

    answer = [int(i) for i in answer]
    print('Answer part 2:', sum(answer))
