from collections import defaultdict


def read_data(filename):
    return [line.strip().split('-') for line in open(filename).readlines()]


def create_adjacency_dict(data):
    adj_dict = defaultdict(list)
    for edge in data:
        if edge[1] != 'start':
            adj_dict[edge[0]].append(edge[1])
        if edge[0] != 'start':
            adj_dict[edge[1]].append(edge[0])
    return adj_dict


def print_dict(dict):
    print('The dict:')
    for key, value in dict.items():
        print(key, value)


def dfs(node, adj_dict, visited_small, num_paths):

    # print(node)

    if node == 'end':
        num_paths += 1
        # print('---------------PATH----------------')
    else:
        for neighbour in adj_dict[node]:
            if neighbour == 'end' and visited_small['end'] != 0:
                continue
            if neighbour.islower():
                if visited_small[neighbour] >= 1 and 2 in visited_small.values():
                    continue
                else:
                    visited_small[neighbour] += 1
            num_paths = dfs(neighbour, adj_dict, visited_small, num_paths)

    if node.islower():
        visited_small[node] -= 1

    return num_paths


if __name__ == '__main__':
    data = read_data('day_12.txt')
    adj_dict = create_adjacency_dict(data)
    print_dict(adj_dict)

    # Idea: do DFS recording number of times destination is reached.
    # Have a dictionary of lower case nodes that have already been visited on the current path

    visited_small = {key: 0 for key in adj_dict}
    num_paths = 0
    num_paths = dfs('start', adj_dict, visited_small, num_paths)
    print('Num paths:', num_paths)