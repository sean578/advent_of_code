import copy


def get_input():
    with open("15.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    the_map = []
    moves = ""
    for line in lines:
        if not line:
            continue
        if line[0] == "#":
            the_map.append(list(line))
        elif line[0] in ("<>^v"):
            moves += line

    return the_map, moves


def get_initial_position(the_map):
    rows = len(the_map)
    cols = len(the_map[0])

    robot = None
    for row in range(rows):
        for col in range(cols):
            if the_map[row][col] == "@":
                robot = [row, col]
                break
        else:
            continue
        break
    return robot


def do_move(the_map, robot, move, proposed):

    rows = len(the_map)
    cols = len(the_map[0])

    if the_map[proposed[0]][proposed[1]] == ".":
        the_map[proposed[0]][proposed[1]] = "@"
        the_map[robot[0]][robot[1]] = "."
        robot = proposed
    elif the_map[proposed[0]][proposed[1]] == "#":
        pass
    elif the_map[proposed[0]][proposed[1]] == "O":
        if move == ">":
            for col in range(proposed[1], cols):
                if the_map[proposed[0]][col] == "#":
                    break
                elif the_map[proposed[0]][col] == ".":
                    the_map[proposed[0]][col] = "O"
                    the_map[proposed[0]][proposed[1]] = "@"
                    the_map[robot[0]][robot[1]] = "."
                    robot = proposed
                    break
        elif move == "<":
            for col in range(proposed[1], -1, -1):
                if the_map[proposed[0]][col] == "#":
                    break
                elif the_map[proposed[0]][col] == ".":
                    the_map[proposed[0]][col] = "O"
                    the_map[proposed[0]][proposed[1]] = "@"
                    the_map[robot[0]][robot[1]] = "."
                    robot = proposed
                    break
        elif move == "v":
            for row in range(proposed[0], rows):
                if the_map[row][proposed[1]] == "#":
                    break
                elif the_map[row][proposed[1]] == ".":
                    the_map[row][proposed[1]] = "O"
                    the_map[proposed[0]][proposed[1]] = "@"
                    the_map[robot[0]][robot[1]] = "."
                    robot = proposed
                    break
        elif move == "^":
            for row in range(proposed[0], -1, -1):
                if the_map[row][proposed[1]] == "#":
                    break
                elif the_map[row][proposed[1]] == ".":
                    the_map[row][proposed[1]] = "O"
                    the_map[proposed[0]][proposed[1]] = "@"
                    the_map[robot[0]][robot[1]] = "."
                    robot = proposed
                    break
        else:
            assert False
    else:
        assert False

    return the_map, robot


def part_1(the_map, moves):

    # Get the initial robot position
    robot = get_initial_position(the_map)

    # iterate through the moves
    for i, move in enumerate(moves, 1):
        if move == ">":
            proposed = (robot[0], robot[1] + 1)
        elif move == "<":
            proposed = (robot[0], robot[1] - 1)
        elif move == "v":
            proposed = (robot[0] + 1, robot[1])
        elif move == "^":
            proposed = (robot[0] - 1, robot[1])
        else:
            assert False

        the_map, robot = do_move(the_map, robot, move, proposed)

    rows = len(the_map)
    cols = len(the_map[0])

    solution = 0
    for row in range(rows):
        for col in range(cols):
            if the_map[row][col] == "O":
                solution += 100 * row + col
    return solution


def make_larger_map(the_map):
    rows = len(the_map)
    cols = len(the_map[0])

    updated_map = []
    for row in range(rows):
        new_row = []
        for col in range(cols):
            value = the_map[row][col]
            if value == "#":
                new_row.extend(["#", "#"])
            elif value == "O":
                new_row.extend(["[", "]"])
            elif value == ".":
                new_row.extend([".", "."])
            elif value == "@":
                new_row.extend(["@", "."])
            else:
                assert False
        updated_map.append(new_row)

    return updated_map


def make_move(the_map, move, robot, i):

    rows = len(the_map)
    cols = len(the_map[0])

    deltas = {
        ">": (0, 1),
        "<": (0, -1),
        "v": (1, 0),
        "^": (-1, 0)
    }

    delta = deltas[move]
    proposed_coord = (robot[0] + delta[0], robot[1] + delta[1])
    proposed_value = the_map[proposed_coord[0]][proposed_coord[1]]

    if proposed_value == "#":
        return the_map, robot
    elif proposed_value == ".":
        the_map[proposed_coord[0]][proposed_coord[1]] = "@"
        the_map[robot[0]][robot[1]] = "."
        robot = proposed_coord
        return the_map, robot

    assert proposed_value in ("[]"), f"{proposed_value}"

    # left & right moves are similar (need to look for [] and move both now)
    if move == ">":
        for col in range(proposed_coord[1], cols):
            if the_map[proposed_coord[0]][col] == "#":
                break
            elif the_map[proposed_coord[0]][col] == ".":

                # @[].
                # @[][].

                symbol = "]"
                for c in range(col, proposed_coord[1], -1):
                    the_map[proposed_coord[0]][c] = symbol
                    if symbol == "]":
                        symbol = "["
                    else:
                        symbol = "]"

                the_map[proposed_coord[0]][proposed_coord[1]] = "@"
                the_map[robot[0]][robot[1]] = "."
                robot = proposed_coord
                break
    elif move == "<":
        for col in range(proposed_coord[1], -1, -1):
            if the_map[proposed_coord[0]][col] == "#":
                break
            elif the_map[proposed_coord[0]][col] == ".":

                # .[]@
                # .[][]@

                symbol = "["
                for c in range(col, proposed_coord[1]):
                    the_map[proposed_coord[0]][c] = symbol
                    if symbol == "]":
                        symbol = "["
                    else:
                        symbol = "]"

                the_map[proposed_coord[0]][proposed_coord[1]] = "@"
                the_map[robot[0]][robot[1]] = "."
                robot = proposed_coord
                break

    elif move == "^":

        row = proposed_coord[0]
        pushing_cols = {proposed_coord[1]}
        # todo: use a normal queue for pushing_cols
        ok = True

        # keep track of what move entails.
        pushing = []

        while pushing_cols:

            next_pushing_cols = set()
            pushed_locations = set()
            for c in pushing_cols:
                proposed = the_map[row][c]

                if proposed == "#":
                    # We can never push a box into a wall so we can't do the move
                    ok = False
                    break
                elif proposed == ".":
                    # Pushing this is ok so move on to checking the next pushing column
                    pushed_locations.add(c)
                    continue
                elif proposed == "[":
                    next_pushing_cols.update({c, c + 1})
                    pushed_locations.update({c, c + 1})
                elif proposed == "]":
                    next_pushing_cols.update({c, c - 1})
                    pushed_locations.update({c, c - 1})
                else:
                    assert False
            else:
                # if we reach the end of the for loop then will go to the next iteration of the while loop
                # if we have broken out of the for loop, we will also break out of the while loop
                pushing.append((row, pushing_cols, pushed_locations))
                pushing_cols = next_pushing_cols
                row = row - 1
                continue
            break

        # do the move if was allowed
        if ok:
            old_map = copy.deepcopy(the_map)
            for push in pushing:
                for col_to_update in push[2]:
                    if col_to_update in push[1]:
                        the_map[push[0]][col_to_update] = old_map[push[0]+1][col_to_update]
                    else:
                        the_map[push[0]][col_to_update] = "."
            the_map[robot[0]][robot[1]] = "."
            robot = proposed_coord

    elif move == "v":

        row = proposed_coord[0]
        pushing_cols = {proposed_coord[1]}
        # todo: use a normal queue for pushing_cols
        ok = True

        # keep track of what move entails.
        pushing = []

        while pushing_cols:

            next_pushing_cols = set()
            pushed_locations = set()
            for c in pushing_cols:
                proposed = the_map[row][c]

                if proposed == "#":
                    # We can never push a box into a wall so we can't do the move
                    ok = False
                    break
                elif proposed == ".":
                    # Pushing this is ok so move on to checking the next pushing column
                    pushed_locations.add(c)
                    continue
                elif proposed == "[":
                    next_pushing_cols.update({c, c + 1})
                    pushed_locations.update({c, c + 1})
                elif proposed == "]":
                    next_pushing_cols.update({c, c - 1})
                    pushed_locations.update({c, c - 1})
                else:
                    assert False
            else:
                # if we reach the end of the for loop then will go to the next iteration of the while loop
                # if we have broken out of the for loop, we will also break out of the while loop
                pushing.append((row, pushing_cols, pushed_locations))
                pushing_cols = next_pushing_cols
                row = row + 1
                continue
            break

        # do the move if was allowed
        if ok:
            old_map = copy.deepcopy(the_map)
            for push in pushing:
                for col_to_update in push[2]:
                    if col_to_update in push[1]:
                        the_map[push[0]][col_to_update] = old_map[push[0]-1][col_to_update]
                    else:
                        the_map[push[0]][col_to_update] = "."
            the_map[robot[0]][robot[1]] = "."
            robot = proposed_coord

    return the_map, robot


def part_2(the_map, moves):

    # make the new, larger map
    the_map = make_larger_map(the_map)

    robot = get_initial_position(the_map)

    for i, move in enumerate(moves):
        the_map, robot = make_move(the_map, move, robot, i)

    rows = len(the_map)
    cols = len(the_map[0])

    solution = 0
    for row in range(rows):
        for col in range(cols):
            if the_map[row][col] == "[":
                solution += 100 * row + col
    return solution


if __name__ == '__main__':
    the_map, moves = get_input()
    # print(part_1(the_map, moves))
    print(part_2(the_map, moves))