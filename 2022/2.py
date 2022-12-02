"""
"""

if __name__ == '__main__':

    convert = {
        'X': 'A',
        'Y': 'B',
        'Z': 'C'
    }

    score = {
        'A': 1,
        'B': 2,
        'C': 3
    }

    lose = {
        'A': 'B',
        'B': 'C',
        'C': 'A'
    }

    win = {value:key for key, value in lose.items()}

    # part 1
    lines = [line.strip() for line in open("2_input.txt", 'r').readlines()]

    total = 0
    for line in lines:
        opponent, me = line.split()
        me = convert[me]
        total += score[me]
        if me == opponent:
            total += 3
        elif opponent == lose[me]:
            pass
        elif opponent == win[me]:
            total += 6
        else:
            raise "Error"

    print(total)