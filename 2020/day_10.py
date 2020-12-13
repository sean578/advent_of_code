"""
Using dynamic programming to make dfs more efficient:
[dfs dp](https://cs.stackexchange.com/questions/3078/algorithm-that-finds-the-number-of-simple-paths-from-s-to-t-in-g)
"""

from collections import defaultdict
from util import load_input


def parse_line(line):
    return int(line.strip('\n'))


def create_adjacency_dict(data):
    adjacency_dict = defaultdict(list)
    for i, value in enumerate(data):
        # print('i, value', i, value)
        j = 1
        while i + j < len(data) and data[i + j] <= value + 3:
            # print('j, value', j, data[i + j])
            adjacency_dict[value].append(data[i + j])
            j += 1
    adjacency_dict[data[-1]] = []
    return adjacency_dict


def dfs(adjacency_dict, start, count):
    print(count)
    if not adjacency_dict[start]:
        return count + 1
    else:
        for node in adjacency_dict[start]:
            count = dfs(adjacency_dict, node, count)

    return count


def dfs_dp(adjacency_dict, start, cache):
    if not adjacency_dict[start]:
        return 1  # found a path
    else:
        if start not in cache.keys():
            cache[start] = sum(dfs_dp(adjacency_dict, c, cache) for c in adjacency_dict[start])
        return cache[start]


if __name__ == '__main__':
    filename = 'day_10.txt'
    data = load_input(filename, parse_line)

    data.sort()
    data.append(data[-1] + 3)
    data.insert(0, 0)

    print('Sorted input', data)
    diffs = []
    for x, y in zip(data, data[1:]):
        diffs.append(y-x)

    counts = {}
    for value in set(diffs):
        count = diffs.count(value)
        counts[value] = count

    print('Part 1')
    print(counts)
    answer = counts[1] * counts[3]
    print('Answer', answer)

    print('Part 2')

    # Create a graph (adjacency dict)
    adjacency_dict = create_adjacency_dict(data)
    print(adjacency_dict)
    # for key, value in adjacency_dict.items():
    #     print(key, value)

    # Find number of paths between vertex 0 and 22
    number_paths = dfs_dp(adjacency_dict, 0, {})
    # number_paths = dfs(adjacency_dict, 0, 0)
    print('Answer part 2:', number_paths)