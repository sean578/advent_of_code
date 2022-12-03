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
