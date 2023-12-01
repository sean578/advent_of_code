import json


# def is_num(character):
#     if 48 <= ord(character) <= 57:
#         return True
#     else:
#         return False
#
#
# def get_num(full_string, initial_index):
#     int_string = ""
#     while is_num(full_string[initial_index]):
#         int_string += left[initial_index]
#         initial_index += 1
#     return int(int_string), initial_index
#
#
# def get_list(full_string, initial_index):
#     # todo: don't just find closing bracket - find the one at the correct level
#     inside_list = ""
#     level = -1
#     while not (full_string[initial_index] == ']' and level == 0):
#         inside_list += full_string[initial_index]
#         if full_string[initial_index] == '[':
#             level += 1
#         elif full_string[initial_index] == ']':
#             level -= 1
#         initial_index += 1
#     inside_list += full_string[initial_index]
#     inside_list = inside_list[1:-1]
#     return inside_list, initial_index
#
#
# def get_value(full_string, index):
#
#     # Closing bracket
#     if full_string[index] == ']':
#         return None, None, True
#     # int
#     if is_num(full_string[index]):
#         num, index = get_num(full_string, index)
#         return num, index, False
#     # list
#     if full_string[index] == '[':
#         inside_list, index = get_list(full_string, index)
#         return index, inside_list, False


def compare(left, right, index):
    # todo: sort out using the index - not the value (left, right full value now)
    winner = None
    while winner is None:
        # Compare
        # todo: first check if have run out of elements

        if type(l) == int and type(r) == int:
            if l < r:
                winner = left
                break
            elif r < l:
                winner = right
                break
            else:
                winner = None
                i += 1
                l = left[i]
                r = right[i]
                continue
        elif type(l) == int and type(r) == list:
            l = [l]
            # Now need to compare again
            continue
        elif type(l) == list and type(r) == int:
            r = [r]
            # Now need to compare again
            continue
        elif type(l) == list and type(r) == list:
            # todo: recursively call this on the element
            pass
    return winner


if __name__ == '__main__':
    # left = [1, 1, 3, 1, 1]
    # right = [1, 1, 5, 1, 1]

    # left = [[1], [2, 3, 4]]
    # right = [[1], 4]

    left = json.loads("[9]")
    right = json.loads("[[8, 7, 6]]")

    winner = None
    i = 0
    l = left[i]
    r = right[i]
    winner = compare(l, r)

    print("Winner:", winner)



    # done = False
    # i = 0
    # j = 0
    # assert left[i] == '['
    # assert right[j] == '['
    # while not done:
    #     # Now could be a list or an int or closing bracket
    #     i, value_left, left_done = get_value(left, i)
    #     j, value_right, right_done = get_value(right, j)
    #
    #     print('value left', value_left)
    #     print('value right', value_right)











    # for l, r in zip(left, right):
    #     if l == r:
    #         continue
    #     elif l < r:
    #         print('correct')
    #     else:
    #         print('incorrect')