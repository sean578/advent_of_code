def load_input(filename, rnage_lines):
    range_minimums, range_maximums = [], []
    other_tickets = []
    for i, line in enumerate(open(filename).readlines()):
        if i < ranges_lines:
            # get the range min, max
            _, r = line.strip('\n').split(': ')
            rs = r.split(' or ')
            for t in rs:
                range_min, range_max = t.split('-')
                range_minimums.append(int(range_min))
                range_maximums.append(int(range_max))
        elif i < ranges_lines + 2:
            pass
        elif i < ranges_lines + 3:
            your_ticket = [int(i) for i in line.split(',')]
        elif i >= ranges_lines + 5:
            other_ticket = [int(i) for i in line.split(',')]
            other_tickets.append(other_ticket)
    return range_minimums, range_maximums, your_ticket, other_tickets


if __name__ == '__main__':
    filename = 'day_16.txt'
    ranges_lines = 20

    range_minimums, range_maximums, your_ticket, other_tickets = load_input(filename, ranges_lines)

    print('range_minimums', range_minimums)
    print('range_maximums', range_maximums)
    # print('your_ticket', your_ticket)
    # print('other_tickets', other_tickets)

    ticket_values = []
    for i in your_ticket:
        ticket_values.append(i)
    for ticket in other_tickets:
        for i in ticket:
            ticket_values.append(i)

    print('ticket values', ticket_values)

    bad = 0
    for v in ticket_values:
        ok = False
        for minimum, maximum in zip(range_minimums, range_maximums):
            if v >= minimum:
                if v <= maximum:
                    ok = True  # ticket value is ok
        if not ok:
            bad += v

    print('Answer part 1:', bad)
