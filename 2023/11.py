def get_expanded(lines):
    expanded_rows = set()
    for i, r in enumerate(lines):
        if all([c == "." for c in r]):
            expanded_rows.add(i)
    return expanded_rows


def get_distance(x, y, expanded_rows, expanded_cols, expansion_amount=1.):
    row_max = max(y[0], x[0])
    row_min = min(y[0], x[0])
    row_diff = row_max - row_min
    row_extra = (expansion_amount - 1) * len(expanded_rows.intersection(set(range(row_min+1, row_max))))
    row_diff += row_extra

    col_max = max(y[1], x[1])
    col_min = min(y[1], x[1])
    col_diff = col_max - col_min
    col_extra = (expansion_amount - 1) * len(expanded_cols.intersection(set(range(col_min+1, col_max))))
    col_diff += col_extra

    return row_diff + col_diff


if __name__ == '__main__':
    lines = [line.strip() for line in open("11_input.txt").readlines()]

    expanded_rows = get_expanded(lines)
    expanded_cols = get_expanded(zip(*lines))

    # Get set of (y, x) coordinates of galaxies before expansion
    galaxies = set()
    for r, line in enumerate(lines):
        for c, point in enumerate(line):
            if point == "#":
                galaxies.add((r, c))

    # Get shortest paths
    d = 0
    while len(galaxies) > 1:
        galaxy = galaxies.pop()
        for g in galaxies:
            d += get_distance(galaxy, g, expanded_rows, expanded_cols, expansion_amount=1e6)

    print(int(d))
