import numpy as np


def read_numbers_and_boards(filename):
    # Read in the numbers that are called and the player boards
    # List of numbers
    # 3d numpy array of boards

    lines = [line.strip() for line in open(filename).readlines()]
    num_lines = len(lines)
    num_boards = (num_lines - 1) // 6
    print('Number of boards', num_boards)

    numbers = [int(i) for i in lines[0].split(',')]

    boards_as_string = ' '.join(lines[2:])
    boards_as_string = ' '.join(boards_as_string.split())
    boards = np.fromstring(boards_as_string, dtype=int, sep=' ').reshape(num_boards, 5, 5)

    return numbers, boards, num_boards


def apply_number_to_boards(number, boards):
    # Replace places where number appears to zero in board
    boards[boards == number] = 0
    return boards


def check_if_board_has_won(boards):
    # Return index of winning board if has won
    # Sum over x - check
    # sum over y - check

    cols = np.argwhere(np.sum(boards, axis=1) == 0)
    rows = np.argwhere(np.sum(boards, axis=2) == 0)

    if len(cols) == 1:
        return cols[0][0]
    if len(rows) == 1:
        return rows[0][0]

    return None


def final_calc(boards, winning_board, number):
    board_sum = np.sum(boards[winning_board, ...])
    return board_sum * number

def print_boards(num_boards, boards):
    for i in range(num_boards):
        print('Board', i)
        print(boards[i, ...])


if __name__ == '__main__':

    numbers, boards, num_boards = read_numbers_and_boards('day_4.txt')

    for n in numbers:
        boards = apply_number_to_boards(n, boards)
        check_if_board_has_won(boards)
        winning_board = check_if_board_has_won(boards)
        if winning_board:
            print('winning board number', winning_board)
            break

    print('result', final_calc(boards, winning_board, n))




