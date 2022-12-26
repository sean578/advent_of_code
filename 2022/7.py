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

    # Stack that holds each directory that contains the current file/directory
    dir_stack = []

    # Dictionary holding the size of each directory
    sizes = {}

    # Directories defined by cd <dir-name>
    # Pop the stack if cd .. found (no longer looking at items in that directory)
    # If a file (with a size) then add to sizes of all directories in stack
    # Use the index to define the directory rather than the name as can have the same name in different locations
    for i, line in enumerate(lines):
        if line == "$ cd ..":
            dir_stack.pop()
        elif line == "$ ls" or line[0:3] == "dir":
            continue
        elif line[0:4] == "$ cd":
            _, n = line.split("cd ")
            dir_stack.append(i)
            if i not in sizes:
                sizes[i] = 0
        else:
            # file found
            s, _ = line.split()
            for d in dir_stack:
                sizes[d] += int(s)

    result = 0
    for v in sizes.values():
        if v <= 100000:
            result += v

    print(f"Part 1: {result}")

    ROOT = 0

    total_space = 70000000
    required_space = 30000000

    unused_space = total_space - sizes[ROOT]
    required_room = required_space - unused_space
    assert required_room > 0, required_room

    min_deletion_size = total_space
    for s in sizes.values():
        if s >= required_room and s <= min_deletion_size:
            min_deletion_size = s

    print(f"Part 2: {min_deletion_size}")
