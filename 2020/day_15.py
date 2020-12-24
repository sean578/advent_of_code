from collections import defaultdict


if __name__ == '__main__':
    # start = [0, 3, 6]
    start = [6,13,1,15,2,0]

    turn_numbers = defaultdict(list)
    # initialise
    for i, s in enumerate(start):
        print(i, s)
        turn_numbers[s].append(i+1)

    prev_num = start[-1]
    for turn in range(len(start) + 1, 30000000 + 1):
        # if has been spoken before
        if len(turn_numbers[prev_num]) >= 2:
            next_num = turn_numbers[next_num][-1] - turn_numbers[next_num][-2]
        else:
            next_num = 0
        turn_numbers[next_num].append(turn)
        prev_num = next_num

    print(turn, next_num)