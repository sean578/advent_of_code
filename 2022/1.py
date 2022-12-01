"""
"""

if __name__ == '__main__':


    # part 1
    lines = [line.strip() for line in open("1_input.txt", 'r').readlines()]

    total = 0
    biggest = 0
    for line in lines:
        if line == '':
            if total > biggest:
                biggest = total
            total = 0
        else:
            total += int(line)

    print(biggest)

    # part 2

    cals = []
    total = 0
    for line in lines:
        if line == '':
            cals.append(total)
            total = 0
        else:
            total += int(line)

    cals.sort(reverse=True)
    print(sum(cals[:3]))
