from collections import deque
import copy
import sys


def load_input(filename):
    deck1, deck2 = [], []
    on_deck_2 = False
    for line in open(filename).readlines():
        if len(line.strip()) == 0:
            on_deck_2 = True
        elif line.strip()[0] == 'P':
            pass
        else:
            if on_deck_2:
                deck2.append(int(line.strip()))
            else:
                deck1.append(int(line.strip()))
    return deque(deck1), deque(deck2)


def play_game(deck1, deck2):
    while deck1 and deck2:

        c1 = deck1.popleft()
        c2 = deck2.popleft()

        if c1 > c2:
            deck1.append(c1)
            deck1.append(c2)
        elif c2 > c1:
            deck2.append(c2)
            deck2.append(c1)
        else:
            print('We have a match - what to do?')

    return deck1, deck2


def play_hand(deck1, deck2, winner):
    """ If winner then use this instead of checking cards """

    c1 = deck1.popleft()
    c2 = deck2.popleft()

    if winner == '1':
        deck1.append(c1)
        deck1.append(c2)
    elif winner == '2':
        deck2.append(c2)
        deck2.append(c1)
    elif c1 > c2:
        deck1.append(c1)
        deck1.append(c2)
    elif c2 > c1:
        deck2.append(c2)
        deck2.append(c1)
    else:
        print('We have a match - what to do?')

    return deck1, deck2


def answer(w):
    mults = list(range(len(list(w)), 0, -1))

    answer = 0
    for a, b in zip(w, mults):
        answer += a*b

    return answer


def play_recursive_ok(deck1, deck2):
    """ Determine whether to play a recursive game """
    if len(deck1) > deck1[0] and len(deck2) > deck2[0]:
        return True
    else:
        return False


def in_infinite_loop(deck1, deck2, states):
    """ Check if stuck in an infinite loop """
    for s in states:
        if tuple(deck1) == s[0] and tuple(deck2) == s[1]:
            return True
    return False


def copy_cards_for_subgame(deck1, deck2):
    d1 = copy.deepcopy(deck1)
    d2 = copy.deepcopy(deck2)
    num_cards_d1 = d1.popleft()
    num_cards_d2 = d2.popleft()
    d1 = deque(list(d1)[:num_cards_d1])
    d2 = deque(list(d2)[:num_cards_d2])
    return d1, d2


def play_recursive_game(deck1, deck2, states, num_games):

    num_games += 1
    # print(num_games)

    # if a deck is empty - finish
    if len(list(deck1)) == 0:
        winner = '2'
        return deck1, deck2, winner, num_games
    elif len(list(deck2)) == 0:
        winner = '1'
        return deck1, deck2, winner, num_games

    if in_infinite_loop(deck1, deck2, states):
        winner = '1'
        return deck1, deck2, winner, num_games
    else:
        states.add((tuple(deck1), tuple(deck2)))

    # Check if enough cards left to play recursive game
    if play_recursive_ok(deck1, deck2):
        d1, d2 = copy_cards_for_subgame(deck1, deck2)
        d1, d2, winner, num_games = play_recursive_game(d1, d2, set(), num_games)
        deck1, deck2 = play_hand(deck1, deck2, winner)
    else:
        deck1, deck2 = play_hand(deck1, deck2, False)

    return play_recursive_game(deck1, deck2, states, num_games)


if __name__ == '__main__':
    sys.setrecursionlimit(22000)

    filename = 'day_22.txt'
    states = set()
    deck1, deck2 = load_input(filename)
    deck1, deck2, w, num_games = play_recursive_game(deck1, deck2, states, 0)

    if w == '1':
        answer_part2 = answer(deck1)
    else:
        answer_part2 = answer(deck2)
    print('Answer part 2', answer_part2)
    print('It took', num_games, 'calls')

