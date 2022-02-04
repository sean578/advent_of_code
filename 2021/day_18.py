import copy
import math


def read_data(filename):
    return [line.strip() for line in open(filename).readlines()]


def create_depth_list(data):
    # Assumes input is all single digits which seems to be the case (all valid snailfish numbers)
    depth_list = []  # depth, value

    l = 0
    for d in data:
        if d == '[':
            l += 1
        elif d == ']':
            l -= 1
        elif d == ',':
            pass
        else:
            # We have a number
            depth_list.append([l, int(d)])

    if l != 0:
        print('Brackets not closed correctly')
        return None
    else:
        return depth_list


def explode(depth_list):
    # return true if have done an explosion
    depth_list_new = copy.deepcopy(depth_list)

    exploded = False
    for i, leaf in enumerate(depth_list):
        if leaf[0] >= 5:
            exploded = True
            # If there is a number to the left
            if i > 0:
                depth_list_new[i-1][1] += depth_list[i][1]
            if i < len(depth_list)-2:
                depth_list_new[i+2][1] += depth_list[i+1][1]

            del depth_list_new[i]
            depth_list_new[i][0] -= 1
            depth_list_new[i][1] = 0
            break

    return exploded, depth_list_new


def split(depth_list):

    depth_list_new = copy.deepcopy(depth_list)

    splitted = False
    for i, leaf in enumerate(depth_list):
        if leaf[1] > 9:
            splitted = True
            # Replace the single number with two numbers one level deeper
            a = math.floor(leaf[1] / 2)
            b = math.ceil(leaf[1] / 2)
            depth = leaf[0] + 1
            depth_list_new.insert(i, [depth, a])
            depth_list_new.insert(i+1, [depth, b])
            del depth_list_new[i+2]
            break

    return splitted, depth_list_new


def add(depth_list_a, depth_list_b):

    depth_list_a_new = copy.deepcopy(depth_list_a)
    depth_list_b_new = copy.deepcopy(depth_list_b)

    # All values go one level deeper
    for i, val in enumerate(depth_list_a):
        depth_list_a_new[i][0] += 1

    for i, val in enumerate(depth_list_b):
        depth_list_b_new[i][0] += 1

    return depth_list_a_new + depth_list_b_new


def find_mag(depth_list):
    depth_list_new = copy.deepcopy(depth_list)

    while depth_list_new[0][0] != 0:
        i = 0
        while depth_list_new[i][0] != depth_list_new[i+1][0]:
            i += 1
        level, a = depth_list_new.pop(i)
        _, b = depth_list_new.pop(i)
        mag = 3*a + 2*b
        depth_list_new.insert(i, [level - 1, mag])

    return depth_list_new[0][1]


if __name__ == '__main__':
    data = read_data('day_18.txt')
    data = list(map(create_depth_list, data))

    part_1 = False

    # Part 1 : Add the numbers up in sequence...
    if part_1:
        depth_list = data[0]
        for line in data[1:]:

            # add the numbers
            depth_list = add(depth_list, line)

            # do the reduction
            while True:
                exploded, depth_list = explode(depth_list)
                if exploded:
                    continue
                splitted, depth_list = split(depth_list)
                if splitted:
                    continue
                break


        mag = find_mag(depth_list)
        print('mag', mag)

    # Part 2 : Add all combinations of numbers

    n = len(data)
    biggest_mag = 0
    for i in range(n):
        for j in range(n):
            if i != j:

                # add the numbers
                depth_list = add(data[i], data[j])

                # do the reduction
                while True:
                    exploded, depth_list = explode(depth_list)
                    if exploded:
                        continue
                    splitted, depth_list = split(depth_list)
                    if splitted:
                        continue
                    break

                mag = find_mag(depth_list)
                if mag > biggest_mag:
                    biggest_mag = mag

    print('Biggest mag', biggest_mag)