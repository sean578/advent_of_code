from dataclasses import dataclass
from collections import defaultdict
import heapq
import math


@dataclass(frozen=False)
class AmphipodState:
    """ State for a single amphipod """
    color: str
    x: int
    y: int


def create_state(colors):
    state = []
    xi = (2, 2, 4, 4, 6, 6, 8, 8)
    yi = (0, 1, 0, 1, 0, 1, 0, 1)
    for i, c in enumerate(colors):
        state.append(AmphipodState(
            color=c,
            x=xi[i],
            y=yi[i]
        ))
    return state


def print_state(state):
    ymax = 5
    xmax = 13

    grid = [['#' for _ in range(xmax)] for _ in range(ymax)]

    for x in range(1, xmax-1):
        grid[1][x] = '.'
    for x in (3, 5, 7, 9):
        grid[2][x] = '.'
        grid[3][x] = '.'
    for s in state:
        grid[ymax-s.y-2][s.x+1] = s.color

    print('State:')
    for l in grid:
        print(' '.join(l))


def get_hallway_positions(state):
    # Get a list of x coords that are blocking
    blocks = set()
    for a in state:
        if a.y == 2:
            blocks.add(a.x)

    return blocks


def find_blocking_pos(hallway_pos, amphipod):
    sb = 11  # Smallest blocking above room x
    lb = -1  # Largest blocking below room x
    for hp in hallway_pos:
        if amphipod.x < hp < sb:
            sb = hp
        elif lb < hp < amphipod.x:
            lb = hp

    return lb, sb


def number_moves(x_initial, y_initial, x_final, y_final):
    return abs(y_final - y_initial) + abs(x_final - x_initial)


def get_neighbours(state, allowed_room_x, energy_dict):
    neighbours = defaultdict(list)  # index: (x, y, energy) tuples. Index is index in state list
    hallway_pos = get_hallway_positions(state)

    for i, a in enumerate(state):
        e = energy_dict[a.color]
        home_x = allowed_room_x[a.color]
        lb, sb = find_blocking_pos(hallway_pos, a)

        if a.y != 2:
            for x in range(lb+1, sb):
                if x in (0, 1, 3, 5, 7, 9, 10):
                    neighbours[i].append((x, 2, e * number_moves(a.x, a.y, x, 2)))
        else:
            y0_occ = False
            y1_occ = False
            for b in state:
                if b.y == 0 and b.x == home_x:
                    y0_occ = True
                    if b.color != a.color:
                        y1_occ = True
            if not (y0_occ and y1_occ):
                if home_x in range(lb+1, sb):
                    if y0_occ:
                        neighbours[i].append((home_x, 1, e * number_moves(a.x, a.y, home_x, 1)))
                    else:
                        neighbours[i].append((home_x, 0, e * number_moves(a.x, a.y, home_x, 0)))

    return neighbours


def make_move(state, neighbours, index, move_number):
    # Return updated state of new position after move made

    state[index].x = neighbours[index][move_number][0]
    state[index].y = neighbours[index][move_number][1]
    energy = neighbours[index][move_number][2]

    return state, energy


def same_state(state_a, state_b):
    # Return true if states are the same

    # 8 amphipod state instances in each state
    for a in state_a:
        if a not in state_b:
            return False

    return True


def initialise(matrix, start_node):
    # Priority queue, results, visited

    # DATA STRUCTURES
    # Priority queue to quickly get min distance mode (min heap)
    # todo: change names node -> state, distance -> energy
    queue = [(0, start_node)]  # 0 distance to start node
    heapq.heapify(queue)  # Not required

    # Visited (set)
    # todo: this should be a set ideally, or a list
    r, c = len(matrix), len(matrix[0])
    visited = [[0 for _ in range(c)] for _ in range(r)]

    # Results dict (parent & distance)
    # todo: how to do this - can't list all the possible states before hand
    distances = [[math.inf for _ in range(c)] for _ in range(r)]
    distances[start_node[0]][start_node[1]] = 0
    parents = [[None for _ in range(c)] for _ in range(r)]

    return queue, visited, distances, parents


def dijkstra(matrix, moves, queue, visited, distances, parents):
    # todo: see comments in initialse for what needs to change

    while queue:
        # Pop min element, add to visited, results
        # Keep popping till find element not visited
        found = False
        dist, n = None, None
        while not found:
            dist, n = heapq.heappop(queue)
            if not visited[n[0]][n[1]]:
                found = True

        # For neighbours
        for neighbour in get_neighbours(matrix, n, moves):
            # If new distance less than results distance then update results & push to queue
            new_dist = dist + matrix[neighbour[0]][neighbour[1]]
            old_dist = distances[neighbour[0]][neighbour[1]]
            if new_dist < old_dist:
                heapq.heappush(queue, (new_dist, neighbour))
                parents[neighbour[0]][neighbour[1]] = n
                distances[neighbour[0]][neighbour[1]] = new_dist

    return distances, parents


if __name__ == '__main__':

    """
    Needed for Dijkstra:
    
    Structures:
    - Priority queue for nodes (states) and energy
    - List of visited states
    - Energies to each stated in visited
    - Parent state for each state in visited
    
    Functions:
    - Compare 2 states
    - Get neighbour states
    """

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

    # initial state
    colors = ['A', 'B', 'D', 'C', 'C', 'B', 'A', 'D']
    state = create_state(colors)
    print('Initial state:')
    for a in state:
        print(a)
    print_state(state)

    # Define final state
    colors = ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D']
    final_state = create_state(colors)
    print('Final state:')
    for a in state:
        print(a)
    print_state(final_state)

    # Try to do the correct path manually
    moves = [(5, 2), (3, 0), (3, 0), (2, 0), (5, 0), (1, 2), (1, 0), (7, 0), (6, 0), (7, 0), (2, 0), (6, 0)]  # index, move number
    total_energy = 0
    printit = False
    for move in moves:
        neighbours = get_neighbours(state, allowed_room_x, energy_dict)
        if printit:
            for key, value in neighbours.items():
                print(key, state[key])
                print(value)
        state, energy = make_move(state, neighbours, *move)
        total_energy += energy
        print('Energy used:', energy)
        print_state(state)

    print('Total energy:', total_energy)

    # Test checking state the same:
    print('Same state?', same_state(state, final_state))