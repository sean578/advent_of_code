import re
import math


def read_data(filename):
    return [line.strip() for line in open(filename).readlines()]


def do_addition(a, b):
    # Add without any reducing
    return '[' + a + ',' + b + ']'


def do_reduction():
    # Keep doing explodes & splits until reduced
    pass


def check_for_explode(data):
    # Are any pairs nested 4 deep?
    # Return index of open bracket of first pair that needs exploding

    nest_level = 0
    for i, char in enumerate(data):
        if char == '[':
            nest_level += 1
            if nest_level == 5:
                return i
        elif char == ']':
            nest_level -= 1

    if nest_level != 0:
        print('Bracket error')
    return None


def check_for_split(data):
    # Are any numbers 10 or greater?
    # Return start & end index of first digit of number which is 10 or greater

    return re.search('\d\d+', data)


def do_explode(data, index):

    # Get the indicies and number that are to be replaced
    left_number = re.search("\[\d+", data[index:])
    right_number = re.search("\d+\]", data[index:])
    print('left_number, right_number:', left_number.group(0)[1:], right_number.group(0)[:-1])

    if left_number and right_number:
        # Replace the number to the right
        right_number_to_update = re.search("\d+", data[index:][right_number.end():])
        if right_number_to_update:
            new_number = str(int(right_number_to_update.group(0)) + int(right_number.group(0)[:-1]))
            new_data_part = re.sub("\d+", new_number, data[index:][right_number.end():], count=1)
            data = data[:index + right_number.end()] + new_data_part

        # Replace the number to the left
        l = len(data[:index][right_number.end():])
        left_number_to_update = re.search("\d+", data[:index][right_number.end():][::-1])  # Look in reverse direction
        if left_number_to_update:
            new_number = str(int(left_number_to_update.group(0)) + int(left_number.group(0)[1:]))
            new_data_part = re.sub("\d+", new_number, data[:index][::-1], count=1)
            data = new_data_part[::-1] + data[index + left_number.start():]

        # Replace the exploded pair with zero
        data = data[:index] + '0' + data[index + right_number.end():]
    return data


def do_split(data, split_match):

    i, j = split_match.start(), split_match.end()
    d = split_match.group(0)

    a = str(math.floor(int(d) / 2))
    b = str(math.ceil(int(d) / 2))

    return data[:i] + '[' + a + ',' + b + ']' + data[j:]


if __name__ == '__main__':
    data = read_data('day_18.txt')

    # Test data
    a = '[[[[4,3],4],4],[7,[[8,4],9]]]'
    b = '[1,1]'

    explode_1 = '[[[[[9,8],1],2],3],4]'
    explode_2 = '[7,[6,[5,[4,[3,2]]]]]'
    explode_3 = '[[6,[5,[4,[3,2]]]],1]'
    explode_4 = '[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]'
    explode_5 = '[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]'

    split_1 = '[[[[0,7],4],[15,[0,13]]],[1,1]]'
    split_2 = '[[[[0,7],4],[[7,8],[0,13]]],[1,1]]'

    # Test addition
    """
    a_plus_b = do_addition(a, b)
    print('a + b = ', a_plus_b)
    """

    # Check for explode
    """
    index_to_explode = check_for_explode(explode_1)
    print('Index to explode = ', index_to_explode)
    """

    # Do explode
    """
    print('-------------------------------------')
    d = explode_1
    print('Tring exploding on:', d)
    index = check_for_explode(d)
    if index:
        data = do_explode(d, index)
        print('Data after exploding:', data)
    """

    # Check for split
    split_match = check_for_split(split_2)
    if split_match:
        start, end = split_match.start(), split_match.end()
        split = split_match.group(0)
        print('Indicies of number to split:', start, end)
        print('Number to split:', split)
    else:
        print('Nothing to split')

    # Do split
    data = do_split(split_2, split_match)
    print('Data after split:', data)
