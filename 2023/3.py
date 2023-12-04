import re


def is_number_valid(number_span, top, middle, bottom):
    number_span[1] -= 1  # index rather than slice value

    left = number_span[0] - 1
    right = number_span[1] + 1

    valid = False

    if middle[left] != ".":
        valid = True
    if middle[right] != ".":
        valid = True

    if not all(i == "." for i in top[left:right + 1]):
        valid = True
    if not all(i == "." for i in bottom[left:right + 1]):
        valid = True

    return valid


if __name__ == '__main__':
    lines_raw = [line.strip() for line in open("3_input.txt", 'r').readlines()]

    # append lines of . to top and bottom
    all_dots = "." * len(lines_raw[0])
    lines_raw.insert(0, all_dots)
    lines_raw.append(all_dots)

    # append . to start and stop of each line
    lines = []
    for l in lines_raw:
        l = list(l)
        l.insert(0, ".")
        l.append(".")
        l = "".join(l)
        lines.append(l)

    # Skip first/last lines, go through each triplet.
    total = 0
    for i in range(1, len(lines) - 1):
        top = lines[i-1]
        middle = lines[i]
        bottom = lines[i+1]

        # Regex to get value & spans of all numbers in line (no overlap)
        numbers = list(re.finditer(r"\d+", middle))

        # todo: if I use this dict below & sum over keys then sum is too low...why?!
        # numbers_dict = {int(n.group()): n.span() for n in numbers}

        numbers_list = [int(n.group()) for n in numbers]
        spans_list = [n.span() for n in numbers]

        # Check if number is valid before including
        for value, span in zip(numbers_list, spans_list):
            if is_number_valid(list(span), top, middle, bottom):
                total += int(value)

    print(total)
