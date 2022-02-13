from dataclasses import dataclass
from collections import defaultdict
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


def get_neighbours(state, state_order, allowed_room_x, energy_dict):
    neighbours = {}  # new state: (x, y, delta energy) tuples
    home_blocks, hallway_pos = get_blocks(state)

    # For each amphipod get its neighbour states
    for i, color in enumerate(state):
        e = energy_dict[state_order[i]]
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


# def same_state(state_a, state_b):
#     # Return true if states are the same
#
#     # 8 amphipod state instances in each state
#     for a in state_a:
#         if a not in state_b:
#             return False
#
#     return True
#
#
# def initialise(initial_state):
#     # Priority queue, results, visited
#
#     # DATA STRUCTURES
#     # Priority queue to quickly get min energy state (min heap)
#     queue = [(0, initial_state)]  # 0 energy to start state
#
#     # Visited (set)
#     visited = set()  # (state, energy, parent)
#     visited.add((initial_state, 0, None))
#
#     return queue, visited
#
#
# def dijkstra(matrix, moves, queue, visited, allowed_room_x, energy_dict):
#     # todo: see comments in initialse for what needs to change
#
#     while queue:
#         # Pop min element, add to visited, results
#         # Keep popping till find element not visited
#         found = False
#         energy, state = None, None
#         while not found:
#             energy, state = heapq.heappop(queue)
#             if state not in visited:
#                 found = True
#
#         # For neighbours
#         # todo: neighbour is a dict - need to iterate through keys & lists
#         for neighbour in get_neighbours(state, allowed_room_x, energy_dict):
#             # If new energy less than results energy then update results & push to queue
#             new_energy = energy + neighbour[key][-1]
#             old_energy = # todo need a quick lookup for the last energy of this state
#             if new_energy < old_energy:
#                 heapq.heappush(queue, (new_energy, neighbour))
#                 parents[neighbour[0]][neighbour[1]] = n
#                 distances[neighbour[0]][neighbour[1]] = new_energy
#
#     return distances, parents


if __name__ == '__main__':

    """
    Data structures:
    state : Tuple of frozensets for 'A', 'B', ... (frozenset((x1, y1), (x2, y2)), frozenset((x1, y1), (x2, y2)), ...)
    visited : set of states
    energy : dictionary state : energy
    parents : dictionary state : state
    heap : tuples of (energy, state)
    neighbours : List of (state, delta energy)
    """

    state_order = ('A', 'B', 'C', 'D')

    allowed_room_x = {
        'A': 2,
        'B': 4,
        'C': 6,
        'D': 8
    }

    energy_dict = {
        'A': 1,
        'B': 10,
        'C': 100,
        'D': 1000,
    }

    # initial & final states
    # ((x1, y1), (x2, y2))
    initial_state_dict = {
        'A': ((2, 0), (8, 0)),
        'B': ((2, 1), (6, 1)),
        'C': ((4, 1), (6, 0)),
        'D': ((4, 0), (8, 1)),
    }

    final_state_dict = {
        'A': ((2, 0), (2, 1)),
        'B': ((4, 0), (4, 1)),
        'C': ((6, 0), (6, 1)),
        'D': ((8, 0), (8, 1)),
    }

    state = create_state(initial_state_dict, state_order)
    print(state)
    print_state(state, state_order)

    final_state = create_state(final_state_dict, state_order)

    # # Do the known correct path manually
    # moves = [(5, 2), (3, 0), (3, 0), (2, 0), (5, 0), (1, 2), (1, 0), (7, 0), (6, 0), (7, 0), (2, 0), (6, 0)]  # index, move number
    neighbours = get_neighbours(state, state_order, allowed_room_x, energy_dict)

    print('Neighbours:')
    for state, energy in neighbours.items():
        print(state)
        print('Energy:', energy)
        print_state(state, state_order)

    # state, energy = make_move(state, neighbours, *move)
    # total_energy += energy
    # print_state(state)
    #
    # print('Total energy:', total_energy)
    #
    # # Test checking state the same:
    # print('Same state?', same_state(state, final_state))