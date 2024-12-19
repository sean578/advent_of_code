import copy
from collections import namedtuple


def get_input():
    with open("6.txt") as f:
        a = [list(line.strip()) for line in f.readlines()]
    return a


Current = namedtuple('Current', 'location direction')

directions = {
    "right": (0, 1),
    "down": (1, 0),
    "left": (0, -1),
    "up": (-1, 0)
}

direction_order = ["right", "down", "left", "up"]


def get_initial(map):
    rows = len(map)
    cols = len(map[0])

    for row in range(rows):
        for col in range(cols):
            if map[row][col] == ">":
                current = Current((row, col), "right")
                break
            elif map[row][col] == "v":
                current = Current((row, col), "down")
                break
            elif map[row][col] == "<":
                current = Current((row, col), "left")
                break
            elif map[row][col] == "^":
                current = Current((row, col), "up")
                break
        else:
            continue
        map[row][col] = "."
        break

    return current, map


def part_1(map):

    # set of positions visited
    visited = set()

    # get initial position & location
    current, map = get_initial(map)

    done = False
    while not done:
        visited.add(current.location)

        # loop over possible directions to make a move
        dir_index = direction_order.index(current.direction)
        for _ in range(4):

            # make a move
            delta = directions[current.direction]
            proposed = (current.location[0] + delta[0], current.location[1] + delta[1])

            # if we would leave the map, then we are done
            if proposed[0] < 0 or proposed[1] < 0 or proposed[0] >= len(map) or proposed[1] >= len(map[0]):
                done = True
                break
            # if we can move in this direction, do so
            if map[proposed[0]][proposed[1]] == ".":
                current = Current(proposed, current.direction)
                break
            # if not, try the next direction
            else:
                dir_index += 1
                dir_index = dir_index % 4
                current = Current(current.location, direction_order[dir_index])

    return len(visited)


def part_2(map):

    current_initial, map = get_initial(map)

    loops = 0
    for row_index in range(len(map)):
        print(f"{row_index} / {len(map)}")
        for col_index in range(len(map[0])):

            # row, col, direction
            states = set()
            if map[row_index][col_index] == "." and (row_index, col_index) != current_initial.location:
                map[row_index][col_index] = "#"
            else:
                continue

            current = current_initial
            done = False
            while not done:
                current_state = (current.location[0], current.location[1], current.direction)
                if current_state in states:
                    loops += 1
                    map[row_index][col_index] = "."
                    break
                states.add(current_state)

                # loop over possible directions to make a move
                dir_index = direction_order.index(current.direction)
                for _ in range(4):

                    # make a move
                    delta = directions[current.direction]
                    proposed = (current.location[0] + delta[0], current.location[1] + delta[1])

                    # if we would leave the map, then we are done
                    if proposed[0] < 0 or proposed[1] < 0 or proposed[0] >= len(map) or proposed[1] >= len(map[0]):
                        done = True
                        map[row_index][col_index] = "."
                        break
                    # if we can move in this direction, do so
                    if map[proposed[0]][proposed[1]] == ".":
                        current = Current(proposed, current.direction)
                        break
                    # if not, try the next direction
                    else:
                        dir_index += 1
                        dir_index = dir_index % 4
                        current = Current(current.location, direction_order[dir_index])

    return loops


if __name__ == '__main__':
    map = get_input()

    # print(part_1(map))
    print(part_2(map))
