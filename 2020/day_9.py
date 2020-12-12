from util import load_input


def parse_line(line):
    return int(line.strip('\n'))


def check_ok(value, buffer):
    for i in buffer:
        need = value - i
        if need == i:
            pass
        elif need in buffer:
            return True

    return False


if __name__ == '__main__':
    filename = 'day_9.txt'
    preamble = 25

    data = load_input(filename, parse_line)
    buffer = data[:preamble]

    for i in range(preamble, len(data)):
        d = data[i]
        if not check_ok(d, buffer):
            print(d)

        if i < len(data) - 1:
            buffer.pop(0)  # remove oldest from buffer
            buffer.append(data[i])  # add new to buffer (if not the last value)
