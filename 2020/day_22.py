from collections import deque


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

    return list(deck1), list(deck2)


def answer_part1(w1, w2):
    mults1 = list(range(len(w1), 0, -1))
    mults2 = list(range(len(w2), 0, -1))

    answer_a = 0
    for a, b in zip(w1, mults1):
        answer_a += a*b
    answer_b = 0
    for a, b in zip(w2, mults2):
        answer_a += a*b

    return max(answer_a, answer_b)


if __name__ == '__main__':
    filename = 'day_22.txt'
    deck1, deck2 = load_input(filename)

    w1, w2 = play_game(deck1, deck2)
    answer_part1 = answer_part1(w1, w2)
    print('Answer part 1', answer_part1)