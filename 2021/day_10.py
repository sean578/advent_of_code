from collections import deque


def read_data(filename):
    return [list(line.strip()) for line in open(filename).readlines()]


if __name__ == '__main__':
    data = read_data('day_10.txt')

    # Push opening brackets into a LIFO
    # When finding a closing bracket, pop from LIFO
    # If bracket type popped is not equal to bracket met then signal error

    # LIFO: deque, push = append(), pop = pop()

    bracket_mapping = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }

    bracket_scores = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }

    score = 0
    for line in data:
        fifo = deque([])
        for bracket in line:
            if bracket in bracket_mapping:
                fifo.append(bracket)
            else:
                b = fifo.pop()
                if bracket_mapping[b] != bracket:
                    score += bracket_scores[bracket]
                    break

    print('Answer part 1:', score)