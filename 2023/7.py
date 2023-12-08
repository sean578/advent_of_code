from collections import Counter, defaultdict


def hand_type(hand):
    joker_states = {
        0: 1,
        1: 3,
        2: 4,
        3: 5,
        4: 5,
        5: 6,
        6: 6
    }

    c = Counter(hand)
    jokers = c.get("J", 0)
    if jokers > 0:
        del c["J"]

    hand_num = 0
    if 5 in c.values():
        hand_num = 6
    elif 4 in c.values():
        hand_num = 5
    elif 3 in c.values():
        if 2 in c.values():
            hand_num = 4
        else:
            hand_num = 3
    elif 2 in c.values():
        if Counter(c.values())[2] == 2:
            hand_num = 2
        else:
            hand_num = 1

    # include jokers
    for _ in range(jokers):
        hand_num = joker_states[hand_num]

    return hand_num


if __name__ == '__main__':
    lines = [line.strip() for line in open("7_input.txt", 'r').readlines()]

    hands = [l.split()[0] for l in lines]
    bids = [int(l.split()[1]) for l in lines]

    hand_types = defaultdict(list)
    for h, b in zip(hands, bids):
        hand_types[hand_type(h)].append([h, b])

    m = {
        "T": 10,
        "J": 1,
        "Q": 12,
        "K": 13,
        "A": 14
    }

    # sort within each hand type
    rank = len(hands)
    total = 0
    for ht in range(6, -1, -1):
        if hand_types.get(ht) is not None:
            ordered = []
            # map t, j, q, k, a
            for h in hand_types.get(ht):
                new_list = []
                for c in h[0]:
                    if c in m:
                        new_list.append(m[c])
                    else:
                        new_list.append(int(c))
                ordered.append((new_list, h[1]))
            for i in sorted(ordered, key=lambda x: x[0], reverse=True):
                # print(rank, i[1])
                total += rank * i[1]
                rank -= 1

    print(total)

