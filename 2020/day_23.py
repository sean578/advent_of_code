def find_destination_cup(current_cup, cups):
    # current_cup -> min -> max --> min

    for i in range(current_cup-1, min(cups) - 1, -1):
        if i in cups:
            return i
    for i in range(max(cups), current_cup - 1, -1):
        if i in cups:
            return i

    return False


if __name__ == '__main__':
    cups = [int(i) for i in '952316487']
    # cups = [int(i) for i in '389125467']  # example

    num_moves = 100
    current_index = 0
    # destination_index = None
    length = len(cups)

    for i in range(num_moves):

        # Get current cup
        current_cup = cups[current_index]

        # Do pick-up
        pick_up_index = []
        pick_up = []
        for p in range(3):
            pick_up_index.append((current_index + 1 + p) % length)
        for p in range(3):
            pick_up.append(cups[pick_up_index[p]])
        for p in range(3):
            cups.remove(pick_up[p])

        # Find destination cup
        destination_cup = find_destination_cup(current_cup, cups)

        # Put the pick-up cups back in
        for p in range(3):
            index = (cups.index(destination_cup) + 1 + p) % length
            cups.insert(index, pick_up[p])

        # Current cup may have moved - find where it is by value and increment index for new current cup
        current_index = (cups.index(current_cup) + 1) % length

    # Get in answer format
    cups_in_order = []
    for i in range(len(cups)):
        index = (cups.index(1) + i) % length
        cups_in_order.append(cups[index])

    cups_in_order = [str(i) for i in cups_in_order]
    cups_in_order = cups_in_order[1:]
    print('Answer part 1:', ''.join(cups_in_order))
