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
        if leaf[0] == 5:
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

    # All values go one level deeper
    for i, val in enumerate(depth_list_a):
        depth_list_a[i][0] += 1

    for i, val in enumerate(depth_list_b):
        depth_list_b[i][0] += 1

    return depth_list_a + depth_list_b


if __name__ == '__main__':
    data = read_data('day_18.txt')

    # data = '[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]'
    # data = '[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]'
    #
    # data_a = '[[[[4,3],4],4],[7,[[8,4],9]]]'
    # data_b = '[1,1]'

    # depth_list_a = create_depth_list(data_a)
    # depth_list_b = create_depth_list(data_b)

    data = list(map(create_depth_list, data))

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

    print(depth_list)
    print([[i[1]] for i in depth_list])