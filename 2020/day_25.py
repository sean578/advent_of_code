def transform(value, subject_number):
    value *= subject_number
    value %= 20201227
    return value


if __name__ == '__main__':
    public_keys = (14082811, 5249543)

    subject_number = 7
    value = 1
    done = [False, False]
    loop_sizes = [None, None]
    loop = 1
    while not all(done):
        value = transform(value, subject_number)
        if value == public_keys[0]:
            done[0] = True
            loop_sizes[0] = loop
        elif value == public_keys[1]:
            done[1] = True
            loop_sizes[1] = loop
        loop += 1
    print('loop sizes', loop_sizes)

    # Now calculate encryption keys
    value_1, value_2 = 1, 1
    subject_number_1 = public_keys[0]
    subject_number_2 = public_keys[1]

    for i in range(loop_sizes[1]):
        value_1 = transform(value_1, subject_number_1)
    for i in range(loop_sizes[0]):
        value_2 = transform(value_2, subject_number_2)

    print('Answer 1', value_1)
    print('Answer 2', value_2)
