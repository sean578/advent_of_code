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
    ymax = 7
    xmax = 13

    grid = [['#' for _ in range(xmax)] for _ in range(ymax)]

    for x in range(1, xmax-1):
        grid[1][x] = '.'
    for x in (3, 5, 7, 9):
        for y in range(2, 6):
            grid[y][x] = '.'
    for i, s in enumerate(state):
        for e in s:

            grid[ymax-e[1]-2][e[0]+1] = state_order[i]

    print('-')
    for l in grid:
        print(' '.join(l))


def get_blocks(state):
    # Get a list of amphipods which are blocking the hall and homes
    blocks_home = {
        2: 0,
        4: 0,
        6: 0,
        8: 0
    }
    blocks_home_types = {
        2: set(),
        4: set(),
        6: set(),
        8: set()
    }

    blocks_hallway = set()
    for i, color in enumerate(state):
        for a in color:
            x, y = a
            if y == 4:
                blocks_hallway.add(x)
            else:
                blocks_home[x] += 1
                blocks_home_types[x].add(2*i + 2)
    return blocks_hallway, blocks_home, blocks_home_types


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
    # Get list of number blocking
    blocks_hallway, blocks_home, blocks_home_types = get_blocks(state)

    # For each amphipod get its neighbour states
    for i, color in enumerate(state):
        e = energy_lookup[state_order[i]]
        home_x = allowed_room_x[state_order[i]]
        lc = list(color)

        # Find the possible neighbour states for each occurance of color
        for k, a in enumerate(lc):
            x, y = a

            lb, sb = find_blocking_pos(blocks_hallway, a)

            # If in the hallway, can move to home?
            if y == 4:
                # IN HALLWAY -> MOVE TO HOME
                #todo: simplify this!
                if blocks_home[home_x] <= 3:
                    if (blocks_home[home_x] == 0) or ((len(blocks_home_types[home_x]) == 1) and (home_x in blocks_home_types[home_x])):
                        if home_x in range(lb+1, sb):
                            ns = create_new_state(state, lc, i, k, (home_x, blocks_home[home_x]))
                            neighbours[ns] = e * number_moves(x, y, home_x, blocks_home[home_x])
            # If in a borrow, if the highest block can move
            elif blocks_home[x] - 1 <= y:
                # IN HOME -> MOVE TO HALLWAY
                for xi in range(lb+1, sb):
                    if xi in (0, 1, 3, 5, 7, 9, 10):
                        ns = create_new_state(state, lc, i, k, (xi, 4))
                        neighbours[ns] = e * number_moves(x, y, xi, 4)

    return neighbours


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
                old_energy = energy_dict[neighbour]
            else:
                old_energy = math.inf
            if new_energy < old_energy:
                heapq.heappush(queue, (new_energy, neighbour))
                parent_dict[neighbour] = state
                energy_dict[neighbour] = new_energy

            if len(energy_dict) % 10000 == 0:
                print('Number of new states:', len(energy_dict), 'Length of queue:', len(queue))
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

    initial_state_dict = {
        'A': ((4, 3), (8, 0), (6, 1), (8, 2)),
        'B': ((2, 0), (6, 0), (4, 1), (6, 2)),
        'C': ((4, 0), (8, 3), (4, 2), (8, 1)),
        'D': ((2, 3), (6, 3), (2, 1), (2, 2)),
    }

    final_state_dict = {
        'A': ((2, 0), (2, 1), (2, 2), (2, 3)),
        'B': ((4, 0), (4, 1), (4, 2), (4, 3)),
        'C': ((6, 0), (6, 1), (6, 2), (6, 3)),
        'D': ((8, 0), (8, 1), (8, 2), (8, 3)),
    }

    state = create_state(initial_state_dict, state_order)
    print('Initial state:')
    print(state)
    print_state(state, state_order)
    final_state = create_state(final_state_dict, state_order)

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