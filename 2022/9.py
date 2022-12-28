"""
"""


def update_tail(h, t):

    if max(abs(h[0] - t[0]), abs(h[1] - t[1])) <= 1:
        return t

    # If same row
    if h[0] == t[0]:
        if h[1] > t[1]:
            t[1] += 1
        else:
            t[1] -= 1
        return t
    # If same col
    if h[1] == t[1]:
        if h[0] > t[0]:
            t[0] += 1
        else:
            t[0] -= 1
        return t
    # Else diagonal
    if h[0] - t[0] > 0:
        t[0] += 1
    else:
        t[0] -= 1
    if h[1] - t[1] > 0:
        t[1] += 1
    else:
        t[1] -= 1
    return t


if __name__ == '__main__':

    ms = [line.strip().split(" ") for line in open("9_input.txt").readlines()]
    moves = [[m[0], int(m[1])] for m in ms]

    h, t = [0, 0], [0, 0]

    tails_pos_history = set()
    tails_pos_history.add(tuple(t))

    for m in moves:
        direction, steps = m
        for _ in range(steps):
            if direction == 'U':
                h[0] += 1
            elif direction == 'D':
                h[0] -= 1
            elif direction == 'L':
                h[1] -= 1
            elif direction == 'R':
                h[1] += 1
            else:
                raise "Incorrect direction"

            t = update_tail(h, t)
            tails_pos_history.add(tuple(t))

    print(len(tails_pos_history))
