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

    a = []
    if len(cols) > 0:
        a += [c[0] for c in cols]
    if len(rows) > 0:
        a += [r[0] for r in rows]
    return a


def final_calc(boards, winning_board, number):
    board_sum = np.sum(boards[winning_board, ...])
    return board_sum * number


def print_boards(num_boards, boards):
    for i in range(num_boards):
        print('Board', i)
        print(boards[i, ...])


if __name__ == '__main__':

    numbers, boards, num_boards = read_numbers_and_boards('day_4.txt')

    winning_boards = set()
    done = False
    last_num = -1
    for n in numbers:
        if done:
            break

        boards = apply_number_to_boards(n, boards)
        winning_board = check_if_board_has_won(boards)
        if winning_board:
            for board in winning_board:
                winning_boards.add(board)
                if len(winning_boards) == num_boards:
                    worst = board
                    last_num = n
                    done = True
                    break
                boards[board, ...] = -1

    answer = final_calc(boards, worst, last_num)
    print('last board', worst)
    print('last num', last_num)
    print('answer', answer)
