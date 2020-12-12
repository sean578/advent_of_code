from collections import defaultdict
import re


def parse_line(line):
    line = line.strip('.\n')
    # line = line.strip('.\n').strip(' bags').strip(' bag')
    line = re.sub(' bags$', '', line)
    line = re.sub(' bag$', '', line)
    a, b = line.split(' bags contain ')
    b_split = b.split(', ')
    b_bit_stripped = [a.strip(' bag') for a in b_split]
    b_stripped = [a.strip(' bags') for a in b_bit_stripped]

    # Assume numbers only ever 1 digit
    nums = [a[0] for a in b_stripped]
    colors = [a[2:] for a in b_stripped]

    return a, colors, nums


def build_adjacency_dict(filename, parse_line):
    # Note doesn't take into account no other bags correctly

    adj_list = defaultdict(set)
    for line in open(filename).readlines():
        a, colors, nums = parse_line(line)
        for color in colors:
            adj_list[color].add(a)
    return adj_list


if __name__ == '__main__':
    filename = 'day_7_example_1.txt'
    adj_list = build_adjacency_dict(filename, parse_line)

    for a, b in adj_list.items():
        print(a, b)
