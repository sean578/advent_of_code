"""
"""

if __name__ == '__main__':

    lines = [l.strip('\n') for l in open("5_input.txt").readlines()]

    # Store dictionary of piles, each as a list with the objects to be moved at the end
    from collections import defaultdict
    piles = defaultdict(list)

    # Store instructions as a list of tuples
    import re
    instructions = []

    inst_flag = False
    for line in lines:
        if not line:
            inst_flag = True
            continue
        if not inst_flag:
            if '[' in line:
                for i, index in enumerate(range(1, len(line), 4)):
                    if line[index] != " ":
                        piles[i+1].insert(0, line[index])
        if inst_flag:
            op = [int(i) for i in re.findall(r'\d+', line)]
            assert len(op) == 3, op
            instructions.append(op)

    print("Start:")
    for pile, boxes in piles.items():
        print(pile, boxes)

    # print("Instructions:")
    # for i in instructions:
    #     print(i)

    # When moving pop and append from end of list 1 item at a time
    for i in instructions:
        num, a, b = i
        for _ in range(num):
            t = piles[a].pop()
            piles[b].append(t)

    print("Finish:")
    for pile, boxes in piles.items():
        print(pile, boxes)

    answer = []
    for i in range(1, 10, 1):
        answer.append(piles[i].pop())
    print("Answer part 1", "".join(answer))