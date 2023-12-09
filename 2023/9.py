import copy


if __name__ == '__main__':
    lines = [line.strip() for line in open("9_input.txt", 'r').readlines()]
    lines = [[int(i) for i in l.split()] for l in lines]

    total = 0
    for line in lines:

        diffs = []
        diff = copy.deepcopy(line)

        while True:
            diff_new = []
            for i in range(len(diff)-1):
                diff_new.append(diff[i+1] - diff[i])
            diffs.append(diff_new)
            diff = diff_new
            if len(set(diff_new)) == 1:
                break

        # part 1
        # num = diffs[-1][-1]
        # for i in range(len(diffs) - 1, 0, -1):
        #     num += diffs[i-1][-1]
        # total += line[-1] + num

        # part 2
        num = diffs[-1][0]
        for i in range(len(diffs) - 1, 0, -1):
            num = diffs[i-1][0] - num
        num = line[0] - num
        total += num
    print(total)
