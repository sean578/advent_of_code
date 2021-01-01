from collections import deque
import copy


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


def answer(w1, w2):
    mults1 = list(range(len(list(w1)), 0, -1))
    mults2 = list(range(len(list(w2)), 0, -1))

    answer_a = 0
    for a, b in zip(w1, mults1):
        answer_a += a*b
    answer_b = 0
    for a, b in zip(w2, mults2):
        answer_a += a*b

    return max(answer_a, answer_b)


def play_recursive_ok(deck1, deck2):
    """ Determine whether to play a recursive game """
    if len(deck1) > deck1[0] and len(deck2) > deck2[0]:
        return True
    else:
        return False


def in_infinite_loop(deck1, deck2, states):
    """ Check if stuck in an infinite loop """
    pass


def play_recursive_game(deck1, deck2):

    # if a deck is empty - finish
    if len(list(deck1)) == 0:
        winner = '2'
        return deck1, deck2, winner
    elif len(list(deck2)) == 0:
        winner = '1'
        return deck1, deck2, winner
    # else if already been in this state - finish
    # todo
    # Check if enough cards left to play recursive game
    elif play_recursive_ok(deck1, deck2):
        d1 = copy.deepcopy(deck1)
        d2 = copy.deepcopy(deck2)
        num_cards_d1 = d1.popleft()
        num_cards_d2 = d2.popleft()
        d1 = deque(list(d1)[:num_cards_d1])
        d2 = deque(list(d2)[:num_cards_d2])

        d1, d2, winner = play_recursive_game(d1, d2)
        deck1, deck2 = play_hand(deck1, deck2, winner)
        return play_recursive_game(deck1, deck2)
    else:
        deck1, deck2 = play_hand(deck1, deck2, False)
        return play_recursive_game(deck1, deck2)


if __name__ == '__main__':
    filename = 'day_22_example_1.txt'
    deck1, deck2 = load_input(filename)

    w1, w2 = play_game(deck1, deck2)
    answer_part1 = answer(w1, w2)
    print('Answer part 1', answer_part1)

    # Part 2
    deck1, deck2 = load_input(filename)
    deck1, deck2, w = play_recursive_game(deck1, deck2)

    answer_part2 = answer(deck1, deck2)
    print('Answer part 2', answer_part2)


