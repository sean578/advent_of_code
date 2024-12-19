from collections import defaultdict


def get_input():
    with open("5.txt") as f:
        a = [line.strip() for line in f.readlines()]

    rules = defaultdict(set)
    to_produce = []
    for row in a:
        if "|" in row:
            before, after = row.split("|")
            rules[int(before)].add(int(after))
        elif row != "":
            to_produce.append([int(i) for i in row.split(",")])

    return rules, to_produce


def part_1(rules, to_produce):
    answer = 0
    for p in to_produce:
        already_come = set()
        for item in p:
            if rules[item].intersection(already_come):
                break
            already_come.add(item)
        else:
            answer += p[len(p)//2]
    return answer


def part_2(rules, to_produce):

    # print(sorted([len(r) for r in rules.values()]))
    # for key, value in rules.items():
    #     print(key, value)
    #
    # print()
    answer = 0
    for p in to_produce:
        # print()
        # print(p)

        reordered = False
        already_come = set()
        i = 0
        while i < len(p):
            item = p[i]
            rule = rules[item]

            if rule.intersection(already_come):
                reordered = True
                # print("intersection:", item, rule, rule.intersection(already_come).pop(), p)
                a, b = p.index(item), p.index(rule.intersection(already_come).pop())
                p[b], p[a] = p[a], p[b]
                i = 0
                already_come = set()
            else:
                already_come.add(item)
                i += 1
        if reordered:
            # print("Updated p:", p)
            answer += p[len(p) // 2]

    return answer


if __name__ == '__main__':
    rules, to_produce = get_input()
    # print(part_1(rules, to_produce))
    print(part_2(rules, to_produce))
