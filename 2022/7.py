"""
"""


class Node:

    def __init__(self, directory, name, size=None):
        self.directory = directory
        self.name = name
        self.size = size
        self.children = []


def create_graph(lines):

    nodes = {}

    i = 0
    while i < len(lines):
        if lines[i][:4] == "$ cd":
            name = lines[i][5:]
            if name == "..":
                i += 1
                continue
            i += 1

            # print("Exploring:", name)
            # Create new node
            new_node = Node(directory=True, name=name)
            nodes[name] = new_node

            i += 1
            while lines[i][0] != '$':
                q, name = lines[i].split()
                # Create new node if required
                if name not in nodes:
                    if q == "dir":
                        child_node = Node(directory=True, name=name)
                    else:
                        child_node = Node(directory=False, name=name, size=int(q))
                    nodes[name] = child_node
                else:
                    child_node = nodes[name]
                new_node.children.append(child_node)

                i += 1
                if i >= len(lines):
                    break
            continue

        i += 1

    return nodes


if __name__ == '__main__':

    lines = [line.strip() for line in open("7_input.txt").readlines()]
    nodes = create_graph(lines)

    print("node list:")
    for key, value in nodes.items():
        print(key, value.directory, value.size, [i.name for i in value.children])

