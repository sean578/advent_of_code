"""
"""

if __name__ == '__main__':

    lines = [line.strip() for line in open("1_input.txt", 'r').readlines()]

    total = 0
    biggest = 0
    for line in lines:
        if line == '':
            if total > biggest:
                biggest = total
            total = 0
        else:
            total += int(line)

    print(biggest)
