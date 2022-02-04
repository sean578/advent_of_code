def read_data(filename):
    pass

class BinaryTree:

    def __init__(self, max_size):
        self.binary_tree = [(-1, -1)]*max_size
        self.node_index = 0
        self.level = 0
        self.default = -1
        self.binary_tree[self.node_index] = (self.level, self.default)

    def __repr__(self):
        leaves = [x for x in self.binary_tree if x[1] != -1]
        return f"Leaves of binary tree:\n{str(leaves)}"

    def print_current_node(self):
        print(self.binary_tree[self.node_index])

    def move_to_left_child(self):
        self.node_index = 2*self.node_index + 1
        self.level += 1

    def move_to_right_child(self):
        self.node_index = 2*self.node_index + 2
        self.level += 1

    def set_node(self, value):
        try:
            self.binary_tree[self.node_index] = (self.level, value)
        except:
            print('Index out of range:', self.node_index)

    def move_to_parent(self):
        self.node_index = self.node_index // 2
        self.level -= 1

    def go_to_root(self):
        self.node_index = 0
        self.level = 0


if __name__ == '__main__':
    read_data('filename')
