from util import load_input


def parse_line(line):
    return line.strip()


def seat_id(row, col):
    return row * 8 + col


def update_range(lower, upper, code):
    if code == 'F' or code == 'L':
        upper = upper - (upper - lower) // 2 - 1
    elif code == 'B' or code == 'R':
        lower = lower + (upper - lower) // 2 + 1
    return lower, upper


def get_row_or_col(codes, l, u):
    for c in codes:
        l, u = update_range(l, u, c)
    return l


if __name__ == '__main__':
    ex_0 = 'FBFBBFFRLR'
    ex_1 = 'BFFFBBFRRR'
    ex_2 = 'FFFBBBFRRR'
    ex_3 = 'BBFFBBFRLL'

    filename = 'day_5.txt'

    data = load_input(filename, parse_line)
    id_max = 0
    for d in data:
        # get row
        row = get_row_or_col(d[:7], 0, 127)
        col = get_row_or_col(d[7:], 0, 7)

        id = seat_id(row, col)
        if id > id_max:
            id_max = id
    print(id_max)