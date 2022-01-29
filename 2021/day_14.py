from collections import Counter
import copy


def read_data(filename):
    data = [line.strip() for line in open(filename).readlines()]
    template = data[0]
    insertions = [line.split(' -> ') for line in data[2:]]

    insertion_dict = {key: value for key, value in insertions}
    return template, insertion_dict


def create_pair_counts(template, insertion_dict):
    pairs = []
    for i in range(len(template) - 1):
        pairs.append(template[i:i+2])

    pair_counts = {key: 0 for key in insertion_dict}
    for pair in pairs:
        pair_counts[pair] += 1
    return pair_counts


def create_new_pair_dict(insertion_dict):
    # What are the 2 new pairs created when an insertion is performed?

    pair_dict = {key: None for key in insertion_dict}
    for pair, insertion_char in insertion_dict.items():
        pair_dict[pair] = (pair[0] + insertion_char, insertion_char + pair[1])

    return pair_dict


def do_insertions(pair_counts, pair_dict):

    # The initial pair counts
    pc = copy.deepcopy(pair_counts)

    for pair, count in pc.items():

        for p in pair_dict[pair]:
            pair_counts[p] += count
        pair_counts[pair] -= count

    return pair_counts


def get_answer(pair_counts, template):

    letter_set = set()
    for pair in pair_counts:
        for p in pair:
            letter_set.add(p)

    letter_counts = {key: 0 for key in letter_set}
    for pair, count in pair_counts.items():
        for l in pair:
            letter_counts[l] += count

    # If count letters then overcount by 2
    # Except for start and finish letters - first add one to these, then divide all by 2
    letter_counts[template[0]] += 1
    letter_counts[template[-1]] += 1

    for letter in letter_counts:
        letter_counts[letter] //= 2

    return max(letter_counts.values()) - min(letter_counts.values())


def print_nonzero_counts(pair_counts):

    for key, value in pair_counts.items():
        if value > 0:
            print(key, value)


if __name__ == '__main__':
    template, insertion_dict = read_data('day_14.txt')

    # 1. Create dict of pairs, counts
    # 2. For each insertion, update the pair counts correctly
        # Lose pair, add the 2 new pairs
    # 3. Convert the pair counts to letter counts (take care of double counting except at start/finish)

    pair_dict = create_new_pair_dict(insertion_dict)
    pair_counts = create_pair_counts(template, pair_dict)

    for step in range(40):
        pair_counts = do_insertions(pair_counts, pair_dict)

    answer = get_answer(pair_counts, template)
    print('Answer:', answer)