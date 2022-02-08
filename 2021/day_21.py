from itertools import product
import copy


def next_pos(current_pos, move):
    pos = current_pos + move
    pos = 1 + (pos - 1) % 10
    return pos


def create_game_states(starting_pos):

    game_state_counts = {}
    game_state_counts[starting_pos] = 1

    return game_state_counts


def do_move(game_state_counts, player, possible_moves):
    if player == '1':
        p = 0
    elif player == '2':
        p = 1
    else:
        print('Incorrect player:', player)

    gsc = copy.deepcopy(game_state_counts)
    for state, count in game_state_counts.items():
        for move in possible_moves:
            new_pos = next_pos(state[p], move)
            new_score = state[p + 2] + new_pos
            if p == 0:
                key = (new_pos, state[1], new_score, state[3])
            else:
                key = (state[0], new_pos, state[2], new_score)
            if key in gsc:
                gsc[key] += count
            else:
                gsc[key] = count
        gsc[state] -= count
        if gsc[state] == 0:
            del gsc[state]

    return copy.deepcopy(gsc)


def count_wins(wins, game_state_counts):

    gsc = copy.deepcopy(game_state_counts)
    for state, count in game_state_counts.items():
        # Player 1 has won
        if state[2] >= 21:
            wins['1'] += count
            del gsc[state]
        # Player 2 has won
        if state[3] >= 21:
            wins['2'] += count
            del gsc[state]

    return copy.deepcopy(gsc), wins


if __name__ == '__main__':

    # Part 2 ideas:

    # Keep counts of current board position (p1, p2 ~ 100 unique positions)
    # Keep difference between scores rather than both scores? : 21 unique positions

    # Create and initialise game states
    starting_pos = (1, 6, 0, 0)  # p1_pos, p2_pos, p1_score, p2_score
    game_state_counts = create_game_states(starting_pos)

    print('Initial state: (p1_pos, p2_pos, p1_score, p2_score)')
    for state, count in game_state_counts.items():
        print(state, count)

    # Roll die 3 times, move is sum. Possibilities are:
    a = list(product(range(1, 4), repeat=3))  # 27 possibilities -> need to create 27 universes
    possible_moves = list(map(lambda x: sum(x), a))
    print('Possible moves:')
    print(possible_moves)

    # Keep track of number of wins
    wins = {
        '1': 0,
        '2': 0
    }

    round = 1
    while True:
        print('round:', round)
        round += 1
        if not round % 10:
            print(f'Length of dict: {len(game_state_counts)}')

        # Do move of p1:
        game_state_counts = do_move(game_state_counts, '1', possible_moves)
        game_state_counts, wins = count_wins(wins, game_state_counts)
        if len(game_state_counts) == 0:
            break
        # Do move of p2:
        game_state_counts = do_move(game_state_counts, '2', possible_moves)
        game_state_counts, wins = count_wins(wins, game_state_counts)
        if len(game_state_counts) == 0:
            break

    print(f'After {round} rounds: (p1_pos, p2_pos, p1_score, p2_score)')
    for state, count in game_state_counts.items():
        print(state, count)

    print(f'Number of wins:')
    for key, value in wins.items():
        print(key, value)