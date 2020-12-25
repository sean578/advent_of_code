def load_input(filename, range_lines):
    range_minimums, range_maximums, fields = [], [], []
    other_tickets = []
    for i, line in enumerate(open(filename).readlines()):
        if i < ranges_lines:
            # get the range min, max
            field, r = line.strip('\n').split(': ')
            fields.append(field)
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
    return fields, range_minimums, range_maximums, your_ticket, other_tickets


def get_possible_fields(fields, num_fields, num_tickets, range_minimums, range_maximums, tickets):
    # for each field create a set of possible fields

    a = {}
    for f in range(num_fields):
        possible_field_indicies_all = []
        for t in range(num_tickets):
            # check which ranges it could fit in (use indicies) & append to possible field indices
            possible_field_indicies = []
            for i, (lower, upper) in enumerate(zip(range_minimums, range_maximums)):
                if lower <= tickets[t][f] <= upper:
                    possible_field_indicies.append(i // 2)
            possible_field_indicies_all.append(possible_field_indicies)

        # Now find the intersection of the possible field indices
        possible = set(possible_field_indicies_all[0]).intersection(*possible_field_indicies_all)
        a[fields[f]] = possible

    return a


def get_fields(a):
    # if len set = 1 then we know the field -> remove from other sets
    all_done = False
    while not all_done:
        all_done = True
        done = []
        for field, value in a.items():
            if len(value) == 1:
                done.append(list(value)[0])
        for d in done:
            for field, value in a.items():
                if len(value) > 1:
                    a[field].discard(d)  # discard if d in set
                    all_done = False
    return a


def remove_bad_tickets(num_tickets, num_fields, tickets):
    good_tickets = []
    for t in range(num_tickets):
        fields_ok = []
        for f in range(num_fields):
            field_ok = False
            for minimum, maximum in zip(range_minimums, range_maximums):
                if minimum <= tickets[t][f] <= maximum:
                    field_ok = True
            fields_ok.append(field_ok)
        # If all fields ok
        if all(fields_ok):
            good_tickets.append(tickets[t])
    return good_tickets


if __name__ == '__main__':
    filename = 'day_16.txt'
    ranges_lines = 20

    fields, range_minimums, range_maximums, your_ticket, other_tickets = load_input(filename, ranges_lines)
    print('fields', fields)

    print('range_minimums', range_minimums)
    print('range_maximums', range_maximums)

    num_tickets = len(other_tickets)
    num_fields = len(other_tickets[0])
    # other ticket indicies: [ticket][field]

    # Remove bad tickets
    good_tickets = remove_bad_tickets(num_tickets, num_fields, other_tickets)

    print('num tickets', len(other_tickets))
    print('num good tickets', len(good_tickets))

    a = get_possible_fields(fields, num_fields, len(good_tickets), range_minimums, range_maximums, good_tickets)
    print('Possibilities after first pass', a)

    a = get_fields(a)
    print('Actual', a)

    # convert your ticket
    print('Your ticket', your_ticket)
    yours = {}
    for field, index in a.items():
        yours[field] = your_ticket[list(index)[0]]
    print('Your ticket', yours)

    # Get the answer
    answer = 1
    for field, value in yours.items():
        if field[:9] == 'departure':
            answer *= value

    print('Answer part 2:', answer)