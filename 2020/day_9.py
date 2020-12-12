from util import load_input


def parse_line(line):
    return line.strip('\n')


if __name__ == '__main__':
    filename = '.txt'
    data = load_input(filename, parse_line)

    for l in data:
        print(l)
