import heapq
import math
import copy


def create_state(state_dict, state_order):

    state = []
    for color in state_order:
        state.append(frozenset(state_dict[color]))
    state = tuple(state)

    return state


def print_state(state, state_order):
    ymax = 5
    xmax = 13

    grid = [['#' for _ in range(xmax)] for _ in range(ymax)]

    for x in range(1, xmax-1):
        grid[1][x] = '.'
    for x in (3, 5, 7, 9):
        grid[2][x] = '.'
        grid[3][x] = '.'
    for i, s in enumerate(state):
        for e in s:

            grid[ymax-e[1]-2][e[0]+1] = state_order[i]

    print('-')
    for l in grid:
        print(' '.join(l))


def get_blocks(state):
    # Get a list of x coords that are blocking
    blocks_y1 = set()
    blocks_y2 = set()
    for color in state:
        for a in color:
            x, y = a
            if y == 2:
                blocks_y2.add(x)
            elif y == 1:
                blocks_y1.add(x)
    return blocks_y1, blocks_y2


def find_blocking_pos(hallway_pos, amphipod):
    x, _ = amphipod
    sb = 11  # Smallest blocking above room x
    lb = -1  # Largest blocking below room x
    for hp in hallway_pos:
        if x < hp < sb:
            sb = hp
        elif lb < hp < x:
            lb = hp

    return lb, sb


def number_moves(x_initial, y_initial, x_final, y_final):
    return abs(y_final - y_initial) + abs(x_final - x_initial)


def create_new_state(old_state, lc, i, j, new_coords):
    # From old_state (list of frozen sets) create a full new state (list of frozen sets)
    # access old coords via i, j
    # They should be converted into x, y of new_coords

    state = copy.deepcopy(old_state)
    state = [i for i in state]  # Need to be mutible
    list_coords = copy.deepcopy(lc)
    list_coords[j] = new_coords
    state[i] = frozenset(list_coords)
    return tuple(state)


def get_neighbours(state, state_order, allowed_room_x, energy_lookup):
    neighbours = {}  # new state: (x, y, delta energy) tuples
    home_blocks, hallway_pos = get_blocks(state)

    # For each amphipod get its neighbour states
    for i, color in enumerate(state):
        e = energy_lookup[state_order[i]]
        home_x = allowed_room_x[state_order[i]]
        lc = list(color)

        # Find if home of color is occupied
        y0_occ = False
        y1_occ = False
        for j, c in enumerate(state):
            for b in c:
                bx, by = b
                if by == 0 and bx == home_x:
                    y0_occ = True
                    if state_order[j] != state_order[i]:
                        y1_occ = True
                if by == 1 and bx == home_x:
                    y1_occ = True

        # Find the possible neighbour states for each occurance of color
        for k, a in enumerate(lc):
            x, y = a
            lb, sb = find_blocking_pos(hallway_pos, a)

            if y == 1 or (y == 0 and x not in home_blocks):
                for xi in range(lb+1, sb):
                    if xi in (0, 1, 3, 5, 7, 9, 10):
                        ns = create_new_state(state, lc, i, k, (xi, 2))
                        neighbours[ns] = e * number_moves(x, y, xi, 2)
            elif y == 2:
                if not (y0_occ and y1_occ):
                    if home_x in range(lb+1, sb):
                        if y0_occ:
                            ns = create_new_state(state, lc, i, k, (home_x, 1))
                            neighbours[ns] = e * number_moves(x, y, home_x, 1)
                        else:
                            ns = create_new_state(state, lc, i, k, (home_x, 0))
                            neighbours[ns] = e * number_moves(x, y, home_x, 0)
    return neighbours


def make_move(state, neighbours, index, move_number):
    # Return updated state of new position after move made

    state[index].x = neighbours[index][move_number][0]
    state[index].y = neighbours[index][move_number][1]
    energy = neighbours[index][move_number][2]

    return state, energy


def initialise(initial_state):

    # Priority queue to quickly get min energy state (min heap)
    queue = [(0, initial_state)]  # 0 energy to start state

    # Visited (set)
    visited = set(initial_state)  # the state

    # Energy (dict)
    energy_dict = {
        initial_state: 0
    }

    # Parents (dict)
    parent_dict = {
        initial_state: None
    }

    return queue, visited, energy_dict, parent_dict


def dijkstra(queue, visited, energy_dict, parent_dict, allowed_room_x, energy_lookup, state_order, final_state):

    while queue:
        # Pop min element, add to visited, results
        # Keep popping till find element not visited
        found = False
        energy, state = None, None
        while not found:
            energy, state = heapq.heappop(queue)
            if state not in visited:
                found = True

        # For neighbours
        for neighbour, energy_delta in get_neighbours(state, state_order, allowed_room_x, energy_lookup).items():
            # If new energy less than results energy then update results & push to queue
            new_energy = energy + energy_delta
            if neighbour in energy_dict:
                old_energy = energy_dict[neighbour]  # todo need to check if state exists
            else:
                old_energy = math.inf
            if new_energy < old_energy:
                heapq.heappush(queue, (new_energy, neighbour))
                parent_dict[neighbour] = state
                energy_dict[neighbour] = new_energy

            if len(energy_dict) % 10000 == 0:
                print('Number of new states:', len(energy_dict))
                if final_state in energy_dict:
                    print('Final state energy:', energy_dict[final_state])

    return energy_dict, parent_dict


def get_shortest_path(parent_dict, final_state):
    path = []  # List of states
    n = final_state
    while n:
        path.append(n)
        n = parent_dict[n]

    path.reverse()
    return path


if __name__ == '__main__':
    SEARCH = True

    state_order = ('A', 'B', 'C', 'D')

    allowed_room_x = {
        'A': 2,
        'B': 4,
        'C': 6,
        'D': 8
    }

    energy_lookup = {
        'A': 1,
        'B': 10,
        'C': 100,
        'D': 1000,
    }

    # initial & final states
    # ((x1, y1), (x2, y2))
    # initial_state_dict = {
    #     'A': ((2, 0), (8, 0)),
    #     'B': ((2, 1), (6, 1)),
    #     'C': ((4, 1), (6, 0)),
    #     'D': ((4, 0), (8, 1)),
    # }

    initial_state_dict = {
        'A': ((4, 1), (8, 0)),
        'B': ((2, 0), (6, 0)),
        'C': ((4, 0), (8, 1)),
        'D': ((2, 1), (6, 1)),
    }

    final_state_dict = {
        'A': ((2, 0), (2, 1)),
        'B': ((4, 0), (4, 1)),
        'C': ((6, 0), (6, 1)),
        'D': ((8, 0), (8, 1)),
    }

    state = create_state(initial_state_dict, state_order)
    print('Initial state:')
    print(state)
    print_state(state, state_order)
    final_state = create_state(final_state_dict, state_order)

    # print('INITIAL STATE:')
    # state = frozenset({(2, 0), (7, 2)}), frozenset({(6, 1), (2, 1)}), frozenset({(4, 1), (6, 0)}), frozenset({(9, 2), (4, 0)})
    # print(state)
    # print_state(state, state_order)
    #
    #
    # print('NEIGHBOUR STATES:')
    # for neighbour, energy_delta in get_neighbours(state, state_order, allowed_room_x, energy_lookup).items():
    #     print(neighbour)
    #     print_state(neighbour, state_order)

    if SEARCH:
        # Do the search algorithm
        queue, visited, energy_dict, parent_dict = initialise(state)
        energy_dict, parent_dict = dijkstra(queue, visited, energy_dict, parent_dict, allowed_room_x, energy_lookup, state_order, final_state)

        print('Minimum energy to get to final state:')
        print(energy_dict[final_state])

        # Get the path taken
        shortest_path = get_shortest_path(parent_dict, final_state)
        for state in shortest_path:
            print(state)
            print_state(state, state_order)