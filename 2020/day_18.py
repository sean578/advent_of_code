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


def perform_calc(string):
    match = re.search(r'\d+\s+[\+\*]\s+\d+', string)
    if match is None:
        print('bad string', string)
    a = match.group(0)
    x, operator, y = a.split()
    if operator == '+':
        z = int(x) + int(y)
    elif operator == '*':
        z = int(x) * int(y)
    else:
        print('strange operator found')
    return str(z), len(a)


def replace(string, l_bracket, r_bracket, new_string):
    return string[:l_bracket] + new_string + string[r_bracket+1:]


def do_all_calcs(string):
    while '*' in string or '+' in string:
        z, length = perform_calc(string)
        string = z + ' ' + string[length+1:]
    return string


if __name__ == '__main__':
    data = parse_input('day_18.txt')
    answer = []
    for d in data:
        print('Calculating:', d)
        while '(' in d:
            l_bracket, r_bracket = get_expression_index(d)
            # swap this below with do all calcs
            z = do_all_calcs(d[l_bracket+1: r_bracket])
            # z, length = perform_calc(d[l_bracket+1: r_bracket])
            d = replace(d, l_bracket, r_bracket, z)
        d = do_all_calcs(d)
        print('Answer:', d)
        answer.append(d)

    answer = [int(i) for i in answer]
    print(answer)
    print('Answer part 1:', sum(answer))
