def get_input():
    with open("10.txt") as f:
        contour_map = [[int(i) for i in line.strip()] for line in f.readlines()]
    return contour_map


def get_possible_moves(contour_map, position):
    candidates = [
        (position[0], position[1] + 1),
        (position[0], position[1] - 1),
        (position[0] + 1, position[1]),
        (position[0] - 1, position[1]),
    ]

    current_value = contour_map[position[0]][position[1]]

    possible_moves = []
    for candidate in candidates:
        if candidate[0] < 0 or candidate[0] >= len(contour_map):
            continue
        if candidate[1] < 0 or candidate[1] >= len(contour_map):
            continue
        if contour_map[candidate[0]][candidate[1]] != current_value + 1:
            continue

        possible_moves.append(candidate)

    return possible_moves


def get_routes(contour_map, position):
    # do dfs with backtracking to get a set of all the peaks that can be reached (include repeats)

    peaks = []
    lifo = [position]
    while lifo:
        # print(lifo)
        # print("----")
        current_position = lifo.pop()
        if contour_map[current_position[0]][current_position[1]] == 9:
            peaks.append(current_position)
            continue
        moves = get_possible_moves(contour_map, current_position)
        # print("moves", moves)
        lifo.extend(moves)

    return peaks


def part_1(contour_map):

    # for each trailhead (zero) dfs (LIFO) (using incrementing by 1 as condition for children)
        # when a 9 is reached, add it to the set of peaks for the trailhead & then get size of the set

    # todo: this will count all of the ways to get to the same peak - not ideal (but needed for part 2!)
    # todo: no memory of previously found routes from a certain location - will recalculate

    scores = []
    for row in range(len(contour_map)):
        for col in range(len(contour_map[0])):
            if contour_map[row][col] == 0:
                peaks = get_routes(contour_map, (row, col))
                scores.append(len(set(peaks)))

    return sum(scores)


def part_2(contour_map):
    scores = []
    for row in range(len(contour_map)):
        for col in range(len(contour_map[0])):
            if contour_map[row][col] == 0:
                peaks = get_routes(contour_map, (row, col))
                scores.append(len(peaks))

    return sum(scores)


if __name__ == '__main__':
    contour_map = get_input()
    print(part_1(contour_map))
    print(part_2(contour_map))
