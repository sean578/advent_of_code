def create_next_cups(cups):
    next_cups = {}
    for i, cup in enumerate(cups):
        next_cups[cup] = cups[(i + 1) % len(cups)]

    return next_cups


def get_destination_cup(current_cup, length):
    found = False
    destination_cup = current_cup - 1
    while not found:
        if (destination_cup in (p1, p2, p3)) or (destination_cup < 1):
            if destination_cup < 1:
                destination_cup = length
            else:
                destination_cup -= 1
        else:
            found = True
    return destination_cup


def get_answer_part_1(next_cups):
    answer = []
    a = 1
    for _ in range(length - 1):
        a = next_cups[a]
        answer.append(a)

    answer = [str(i) for i in answer]
    answer = ''.join(answer)
    return answer


def get_answer_part_2(next_cups):
    a = next_cups[1]
    b = next_cups[a]
    return a*b


if __name__ == '__main__':
    cups_initial = [int(i) for i in '952316487']  # real input
    # cups_initial = [int(i) for i in '389125467']  # example

    cups = cups_initial + list(range(max(cups_initial) + 1, 1000000 + 1))
    # cups = cups_initial

    num_moves = 10000000  # int(10e6)
    current_index = 0
    # destination_index = None
    length = len(cups)

    # Create a dictionary to hold next cups
    next_cups = create_next_cups(cups)

    # Initial position
    current_cup = cups[0]
    destination_cup = None

    for move in range(num_moves):
        # Find pick-up cups
        p1 = next_cups[current_cup]
        p2 = next_cups[p1]
        p3 = next_cups[p2]
        # Remove pick-up cups
        next_cups[current_cup] = next_cups[p3]

        # Calculate destination cup label
        destination_cup = get_destination_cup(current_cup, length)

        # Update pick-up cup positions
        next_cups[p3] = next_cups[destination_cup]
        next_cups[destination_cup] = p1
        next_cups[p1] = p2
        next_cups[p2] = p3

        # Update current cup position
        current_cup = next_cups[current_cup]

    # Get the answer (part 1):
    # answer_part_1 = get_answer_part_1(next_cups)
    # print('Answer part 1:', answer_part_1)

    # Get the answer (part 2):
    answer_part_2 = get_answer_part_2(next_cups)
    print('Answer part 2:', answer_part_2)