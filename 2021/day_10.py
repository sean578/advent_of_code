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
    uncorrupted = []
    for line in data:
        ok = True
        lifo = deque([])
        for bracket in line:
            if bracket in bracket_mapping:
                lifo.append(bracket)
            else:
                b = lifo.pop()
                if bracket_mapping[b] != bracket:
                    score += bracket_scores[bracket]
                    ok = False
                    break
        if ok:
            uncorrupted.append(line)

    print('Answer part 1:', score)

    incomplete_scores = {
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4
    }

    line_scores = []
    for line in uncorrupted:
        line_score = 0
        lifo = deque([])
        for bracket in line:
            if bracket in bracket_mapping:
                lifo.append(bracket)
            else:
                b = lifo.pop()

        while lifo:
            b = lifo.pop()
            line_score *= 5
            line_score += incomplete_scores[b]
        line_scores.append(line_score)

    line_scores.sort()
    print('Answer part 2:', line_scores[len(line_scores) // 2])
