import copy
import math


def left_right_iter(lr):
    i = -1
    while True:
        if i < len(lr) - 2:
            i += 1
        else:
            i = -1
        if lr[i] == "L":
            yield 0
        else:
            yield 1


def part_1(left_right, graph):
    node = "AAA"
    for i, instruction in enumerate(left_right_iter(left_right), 1):
        node = graph[node][instruction]
        if node == "ZZZ":
            break
    print("part 1", i)


def get_graph(lines):

    graph = {}
    for l in lines[2:]:
        node, lr_string = l.split(" = ")
        left, right = lr_string[1:-1].split(", ")
        graph[node] = (left, right)

    return graph


if __name__ == '__main__':
    lines = [line.strip() for line in open("8_input.txt", 'r').readlines()]
    left_right = lines[0]
    graph = get_graph(lines)

    # part_1(left_right, graph)

    # get all starting nodes
    starting_nodes = [node for node in graph.keys() if node[-1] == "A"]
    print(starting_nodes)

    nodes = copy.deepcopy(starting_nodes)
    when_finished = [None] * len(starting_nodes)
    for i, instruction in enumerate(left_right_iter(left_right), 1):
        nodes = [graph[node][instruction] for node in nodes]
        for j, node in enumerate(nodes):
            if node[-1] == "Z":
                when_finished[j] = i

        if all([f is not None for f in when_finished]):
            print(i, when_finished)
            break

    # The map takes the Z back to the original mode in the next step.
    # So will keep getting to z every n*when first finished.
    # LCM will give first time they all were in Z at the same time.
    print(math.lcm(*when_finished))
