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

    # When moving pop and append from end of list 1 item at a time
    for i in instructions:
        num, a, b = i
        # part 1
        # for _ in range(num):
        #     t = piles[a].pop()
        #     piles[b].append(t)
        # part 2
        t = piles[a][-num:]
        for _ in range(num):
            piles[a].pop()
        piles[b].extend(t)

    print("Finish:")
    for pile, boxes in piles.items():
        print(pile, boxes)

    answer = []
    for i in range(1, 10, 1):
        answer.append(piles[i].pop())
    print("Answer", "".join(answer))