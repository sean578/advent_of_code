from collections import defaultdict
import re


def parse_line(line):
    line = line.strip('.\n')
    line = re.sub(' bags$', '', line)
    line = re.sub(' bag$', '', line)
    a, b = line.split(' bags contain ')
    b_split = b.split(', ')
    b_bit_stripped = [re.sub(' bag$', '', a) for a in b_split]
    b_stripped = [re.sub(' bags$', '', a) for a in b_bit_stripped]
    # Assume numbers only ever 1 digit
    nums = [a[0] for a in b_stripped]
    colors = [a[2:] for a in b_stripped]
    return a, colors, nums


def build_adjacency_dict(filename, parse_line):
    # Note doesn't take into account no other bags

    adj_list = defaultdict(set)
    for line in open(filename).readlines():
        a, colors, nums = parse_line(line)
        for color in colors:
            if color != ' other':
                adj_list[color].add(a)
    return adj_list


def dfs(key, adj_list, possible_bags):
    possible_bags.add(key)

    # if no more parent bags return
    if key not in adj_list.keys():
        return possible_bags
    # Else do dfs on all parent bags
    else:
        for color in adj_list[key]:
            dfs(color, adj_list, possible_bags)

    return possible_bags


if __name__ == '__main__':
    # filename = 'day_7_example_1.txt'
    filename = 'day_7.txt'

    adj_list = build_adjacency_dict(filename, parse_line)

    print('Adjacency list:')
    for a, b in adj_list.items():
        print(a, b)
    print('')

    possible_bags = set()
    dfs('shiny gold', adj_list, possible_bags)

    # print('Possible bags', possible_bags)
    print('Answer', len(possible_bags) - 1)
