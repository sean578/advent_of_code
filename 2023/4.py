def part_1(winning, ours):

    total = 0
    for w, o in zip(winning, ours):

        winning_set = set(w)
        ours_set = set(o)

        answer = int(2**(len(ours_set.intersection(winning_set)) - 1))
        total += answer

    return total


def part_2(winning, ours):
    num_cards = [1] * len(ours)
    for i, (w, o) in enumerate(zip(winning, ours)):

        # get number of wins
        winning_set = set(w)
        ours_set = set(o)
        num_wins = len(ours_set.intersection(winning_set))

        # update the number of cards we have
        for j in range(i+1, i+num_wins+1):
            num_cards[j] += num_cards[i]

    return sum(num_cards)


if __name__ == '__main__':
    lines = [line.strip() for line in open("4_input.txt", 'r').readlines()]
    nums = [l.split(": ")[1].split(" | ") for l in lines]

    winning = []
    ours = []
    for n in nums:
        w = n[0].split()
        o = n[1].split()
        winning.append(w)
        ours.append(o)

    print(part_1(winning, ours))
    print(part_2(winning, ours))
