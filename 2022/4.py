"""
"""

if __name__ == '__main__':
    lines = [line.strip() for line in open("4_input.txt", 'r').readlines()]

    num_pairs = 0
    num_pairs_part2 = 0
    for line in lines:
        a, b = line.split(',')
        a_low, a_high = [int(i) for i in a.split('-')]
        b_low, b_high = [int(i) for i in b.split('-')]

        a_set = set(range(a_low, a_high + 1))
        b_set = set(range(b_low, b_high + 1))

        if a_set.issubset(b_set) or b_set.issubset(a_set):
            num_pairs += 1

        # part 2
        if not a_set.isdisjoint(b_set):
            num_pairs_part2 += 1

    print(num_pairs)
    print(num_pairs_part2)