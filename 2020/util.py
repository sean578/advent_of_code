def load_input(filename, parse_line):
    input = []
    for line in open(filename).readlines():
        input.append(parse_line(line))
    return input