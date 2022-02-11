from dataclasses import dataclass
from collections import defaultdict


@dataclass(frozen=False)
class AmphipodState:
    """ State for a single amphipod """

    color: str
    # 0 = Hall, 1 = Room
    room: bool
    # If room == False then must be in [0, 1, 3, 5, 7, 9, 10]
    # If room == True then must be in [2, 4, 6, 8]
    x: int
    # 0 = lower part of room, 1 = upper part of room
    y: int = None

    def __post_init__(self):
        if self.room:
            assert self.x in (2, 4, 6, 8)
            assert self.y in (0, 1)
        else:
            assert self.x in (0, 1, 3, 5, 7, 9, 10)
            assert self.y == 2

        assert self.color in ('A', 'B', 'C', 'D')


def initial_state(colors):
    state = []
    xi = (2, 2, 4, 4, 6, 6, 8, 8)
    yi = (0, 1, 0, 1, 0, 1, 0, 1)
    for i, c in enumerate(colors):
        state.append(AmphipodState(
            color=c,
            room=True,
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
        if not a.room:
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


def get_neighbours(state):
    # Todo: have to get weight for each of these movements too

    neighbours = defaultdict(list)  # index: (x, y) tuples. Index is index in state list

    allowed_room_x = {
        'A': 2,
        'B': 4,
        'C': 6,
        'D': 8
    }

    hallway_pos = get_hallway_positions(state)

    for i, a in enumerate(state):
        if a.room:
            # Can move into hallway
            lb, sb = find_blocking_pos(hallway_pos, a)
            for x in range(lb+1, sb):
                if x in (0, 1, 3, 5, 7, 9, 10):
                    neighbours[i].append((x, 2))
        elif not a.room:
            home_x = allowed_room_x[a.color]
            y0_occ = False
            y1_occ = False
            for b in state:
                if b.room and b.x == home_x:
                    y0_occ = True
                    if b.color != a.color or b.y == 1:
                        y1_occ = True  # May not actually be occupied but using to say it is blocked

            if y0_occ and y1_occ:
                # No options
                pass
            else:
                lb, sb = find_blocking_pos(hallway_pos, a)
                if home_x in range(lb+1, sb):
                    if y0_occ:
                        neighbours[i].append((home_x, 1))
                    else:
                        neighbours[i].append((home_x, 0))

    return neighbours


def make_move(state, neighbours, index, move_number):
    # Return updated state of new position after move made

    if neighbours[index][move_number][1] == 2:
        state[index].y = 2
        state[index].room = False
    else:
        state[index].y = neighbours[index][move_number][1]
        state[index].room = True

    state[index].x = neighbours[index][move_number][0]

    return state


if __name__ == '__main__':

    # initial state
    colors = ['A', 'B', 'D', 'C', 'C', 'B', 'A', 'D']
    state = initial_state(colors)
    for a in state:
        print(a)
    print_state(state)

    # Try to do the correct path manually
    moves = [(5, 2), (3, 0), (3, 0), (2, 0), (5, 0), (1, 2), (1, 0), (7, 0), (6, 0), (7, 0), (2, 0), (6, 0)]  # index, move number
    printit = False
    for move in moves:
        neighbours = get_neighbours(state)
        if printit:
            for key, value in neighbours.items():
                print(key, state[key])
                print(value)
        state = make_move(state, neighbours, *move)
        print_state(state)
