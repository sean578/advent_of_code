import numpy as np
import copy


def read_data(filename):
    data = []
    lines = [l.strip() for l in open(filename).readlines()]
    for line in lines:
        data.append(list(line))
    return np.array(data)


def move_east(data):

    data_copy = copy.deepcopy(data)

    move_done = False
    for y in range(data.shape[0]):
        for x in range(data.shape[1]):
            if data[y, x] == '>':
                if data[y, ((x+1) % data.shape[1])] == '.':
                    move_done = True
                    data_copy[y, x] = '.'
                    data_copy[y, ((x+1) % data.shape[1])] = '>'

    return data_copy, move_done


def move_south(data):

    data_copy = copy.deepcopy(data)

    move_done = False
    for y in range(data.shape[0]):
        for x in range(data.shape[1]):
            if data[y, x] == 'v':
                if data[((y+1) % data.shape[0]), x] == '.':
                    move_done = True
                    data_copy[y, x] = '.'
                    data_copy[((y+1) % data.shape[0]), x] = 'v'

    return data_copy, move_done


if __name__ == '__main__':
    data = read_data('day_25.txt')
    print(data)

    move_done = True
    moves = 0
    while move_done:
        data, md1 = move_east(data)
        data, md2 = move_south(data)
        move_done = md1 or md2
        moves += 1

    print('Number of moves:', moves)