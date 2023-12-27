from collections import OrderedDict


def get_hash(string):
    current_value = 0
    for char in string:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    return current_value


if __name__ == '__main__':
    the_line = [line.strip() for line in open("15_input.txt").readlines()]
    assert len(the_line) == 1
    steps = the_line[0].split(",")

    boxes = [OrderedDict() for _ in range(256)]
    for step in steps:
        # Get the input
        if "=" in step:
            label, focal_length = step.split("=")
        else:
            label = step.split("-")[0]
            focal_length = None

        # Do the instruction
        box = get_hash(label)
        if focal_length is None:
            if label in boxes[box]:
                boxes[box].pop(label)
        else:
            boxes[box][label] = focal_length

    # Sum up the powers
    total = 0
    for i, box in enumerate(boxes):
        for j, focal_length in enumerate(box.values(), 1):
            total += (i + 1) * j * int(focal_length)
    print(total)
