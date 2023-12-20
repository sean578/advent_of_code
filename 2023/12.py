def num_combs(spring, group, num, total=0):

    if len(spring) > 0:
        symbol = spring.pop(0)
    else:
        if len(group) != 0:
            return total
        else:
            # found a valid combination
            return total + 1

    if symbol == "?":
        # Call again with ? replaced (string length the same)
        return num_combs(["#"] + spring, group, num, total) + num_combs(["."] + spring, group, num, total)
    if symbol == ".":
        if num != 0:
            if len(group) == 0:
                return 0
            if group[0] == num:
                # Have the group we need - continue calling on rest
                return num_combs(spring, group[1:], 0, total)
            else:
                # Not valid - return no combinations
                return total
        else:
            # Still outside of group - call on rest
            return num_combs(spring, group, num, total)
    if symbol == "#":
        # either starting a new group or continuing - just note length and call on rest
        num += 1
        return num_combs(spring, group, num, total)


if __name__ == '__main__':
    lines = [line.strip() for line in open("12_input.txt").readlines()]
    springs, groups = [], []
    for line in lines:
        spring, group = line.split(" ")
        springs.append(list(spring))
        groups.append([int(i) for i in group.split(",")])

    # Damaged = #, groups are sizes of contiguous damaged springs (in order)
    answer = 0
    for spring, group in zip(springs, groups):
        # print("".join(spring), group)
        total = 0
        total = num_combs(["."] + spring + ["."], group, 0, total)
        answer += total
        # break

    print(answer)