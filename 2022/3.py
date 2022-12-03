"""
"""

if __name__ == '__main__':

    lines = [line.strip() for line in open("3_input.txt", 'r').readlines()]

    total_priority = 0
    for line in lines:
        l = len(line) //2
        a, b = line[:l], line[l:]
        a = set(a)
        b = set(b)
        both = a.intersection(b).pop()
        if both.isupper():
            priority = ord(both) - 65 + 27
        else:
            priority = ord(both) - 97 + 1

        total_priority += priority

    print(total_priority)

    # part 2
    total_priority = 0
    for i in range(0, len(lines), 3):
        a = set(lines[i+0])
        b = set(lines[i+1])
        c = set(lines[i+2])

        both = a.intersection(b).intersection(c)
        assert len(both) == 1
        both = both.pop()
        if both.isupper():
            priority = ord(both) - 65 + 27
        elif both.islower():
            priority = ord(both) - 97 + 1
        else:
            print('ERROR')

        total_priority += priority

    print(total_priority)
