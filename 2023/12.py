def num_combs(spring, group, num, memory, total=0):
    mem = memory.get((spring, group, num))
    if mem is not None:
        # print("USING MEMORY")
        return mem

    if len(spring) > 0:
        symbol = spring[0]
    else:
        if len(group) != 0:
            memory[(spring, group, num)] = total
            return total
        else:
            # found a valid combination
            memory[(spring, group, num)] = total + 1
            return total + 1

    if symbol == "?":
        # Call again with ? replaced (string length the same)
        return num_combs(tuple(["#"] + list(spring[1:])), group, num, memory, total) + \
               num_combs(tuple(["."] + list(spring[1:])), group, num, memory, total)
    if symbol == ".":
        if num != 0:
            if len(group) == 0:
                memory[(spring, group, num)] = total
                return total
            if group[0] == num:
                # Have the group we need - continue calling on rest
                return num_combs(spring[1:], group[1:], 0, memory, total)
            else:
                # Not valid - return no combinations
                memory[(spring, group, num)] = total
                return total
        else:
            # Still outside of group - call on rest
            return num_combs(spring[1:], group, num, memory, total)
    if symbol == "#":
        # either starting a new group or continuing - just note length and call on rest
        return num_combs(spring[1:], group, num + 1, memory, total)


if __name__ == '__main__':
    lines = [line.strip() for line in open("12_debug.txt").readlines()]
    springs, groups = [], []
    for line in lines:
        spring, group = line.split(" ")
        initial_spring = list(spring) + ["?"]
        springs.append((initial_spring*5)[:-1])
        groups.append(5*[int(i) for i in group.split(",")])

    # Damaged = #, groups are sizes of contiguous damaged springs (in order)
    answer = 0
    for spring, group in zip(springs, groups):
        print("".join(spring), group)
        total = 0
        total = num_combs(tuple(["."] + spring + ["."]), tuple(group), 0, {}, total)
        print(total)
        answer += total
    print(answer)
