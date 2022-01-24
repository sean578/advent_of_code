def read_data(filename):
    return [line.strip().split(' | ') for line in open(filename).readlines()]


if __name__ == '__main__':
    data = read_data('day_8.txt')

    num_segments = {
        0: 6,
        1: 2,
        2: 5,
        3: 5,
        4: 4,
        5: 5,
        6: 6,
        7: 3,
        8: 7,
        9: 6
    }

    answer = 0
    for line in data:
        for output_value in line[1].split():
            if len(output_value) in [2, 4, 3, 7]:
                answer += 1

    print('answer part 1:', answer)