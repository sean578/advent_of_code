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
        j = 1
        while i + j < len(data) and data[i + j] <= value + 3:
            adjacency_dict[value].append(data[i + j])
            j += 1
    adjacency_dict[data[-1]] = []
    return adjacency_dict


def dfs_dp(adjacency_dict, start, cache):
    # If arrive at final mode then have found a path
    if not adjacency_dict[start]:
        return 1  # found a path
    else:
        # Only do dfs if we haven't already stored the number of paths from this start node to the final node
        if start not in cache.keys():
            # The number of paths to a node is the sum of number of paths to parent nodes
            cache[start] = sum(dfs_dp(adjacency_dict, c, cache) for c in adjacency_dict[start])
        return cache[start]


if __name__ == '__main__':
    filename = 'day_10.txt'
    data = load_input(filename, parse_line)

    data.sort()
    data.append(data[-1] + 3)
    data.insert(0, 0)

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

    # Find number of paths between vertex 0 and final node
    # Note final node is only element without a child in the adjacency list
    number_paths = dfs_dp(adjacency_dict, 0, {})
    print('Answer part 2:', number_paths)