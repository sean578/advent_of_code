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
            assert self.y is None

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
        grid[2][x] = ' '
        grid[3][x] = ' '
    for s in state:
        if s.room:
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
    """
    If room=True & y=1 can move into hallway (if not blocked)
        (0, 1, 3, 5, 7, 9, 10) are possible.
        Check positions of room=False. Can only move from current x to next blocking on x in both directions.
    If room=False can move into their own room if it is empty or occupied by the same type.
        If empty goes to y=0, if occupied goes to y=1
        Also have to check for blocking between the hallway position and the
    """

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
            if a.y == 1:
                # Can move into hallway
                lb, sb = find_blocking_pos(hallway_pos, a)
                for x in range(lb, sb+1):
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
                if home_x in range(lb, sb+1):
                    if y0_occ:
                        neighbours[i].append((home_x, 1))
                    else:
                        neighbours[i].append((home_x, 0))

    return neighbours


def make_move(state, neighbours, index, move_number):
    # Return updated state of new position after move made
    # move:

    if neighbours[index][1] == 2:
        state[index].y = None
    else:
        state[index].y = neighbours[index][move_number][1]

    state[index].x = neighbours[index][move_number][0]

    return state


if __name__ == '__main__':
    """
    How to define the state:
        - Position of each amphipod
        - Set of occupied positions
        
    How to generate possible neighbours - what is a move:
        - Move a single amphipod
        - Move into a hall position or into a room (don't include in between as more steps)
        - Cost depends on which room / which room pos / which hall pos / which amphipod type
        
    How to deal with not stopping outside rooms:
        - Normal state, if in this state then only 2 possible neighbours
        - 
    
    
    Hall has only max 7 positions (not outside rooms)
    28 initial moves
    Hall, room by x coord. Then to check possible moves, use hall positions
    """

    colors = ['A', 'B', 'D', 'C', 'C', 'B', 'A', 'D']
    state = initial_state(colors)
    for a in state:
        print(a)

    print_state(state)

    # Get neighbours of state
    neighbours = get_neighbours(state)
    for key, value in neighbours.items():
        print(key, state[key])
        print(value)

    # Make a move
    for key in neighbours:
        for i in range(len(neighbours[1])):
            state = initial_state(colors)
            state = make_move(state, neighbours, key, i)
            print_state(state)