import copy
from collections import defaultdict


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


def get_possible_fields(field_rules, tickets):
    # If at least 1 rule is obeyed for all tickets then add possible location of field
    # tickets: [ticket][field]

    possible_fields = defaultdict(set)  # key = field name, value = set of possible locations

    # loop over fields & corresponding rules
    for field, rules in field_rules.items():
        # loop over position - which positions work for the field
        for pos in range(len(tickets[0])):
            # loop over tickets - do all tickets meet rule
            num_ok = 0
            for t in tickets:
                # check if ok for either range
                if (rules[0][0] <= t[pos] <= rules[0][1]) or (rules[1][0] <= t[pos] <= rules[1][1]):
                    num_ok += 1
            if num_ok == len(tickets):
                possible_fields[field].add(pos)

    return possible_fields


def get_fields(possible_fields):
    # keys: field names
    # values: possible indicies for the field names
    possible_fields = copy.deepcopy(possible_fields)

    # if len set = 1 then we know the field -> remove from other sets
    all_done = False
    while not all_done:
        all_done = True
        done = set()
        for field, value in possible_fields.items():
            if len(value) == 1:
                done.add(list(value)[0])
        # discard found indices from the lists of possible indices for other fields
        for d in done:
            for field, value in possible_fields.items():
                if len(value) > 1:
                    possible_fields[field].discard(d)  # discard if d in set
                    all_done = False
    return possible_fields


def remove_bad_tickets(tickets):
    good_tickets = []
    for t in range(len(tickets)):
        fields_ok = []
        for f in range(len(tickets[1])):
            field_ok = False
            for minimum, maximum in zip(range_minimums, range_maximums):
                if minimum <= tickets[t][f] <= maximum:
                    field_ok = True
            fields_ok.append(field_ok)
        # If all fields ok
        if all(fields_ok):
            good_tickets.append(tickets[t])
    return good_tickets


def convert_ticket_to_dict(ticket, a):
    yours = {}
    for field, index in a.items():
        yours[field] = ticket[list(index)[0]]
    return yours


def get_answer(yours, string):
    answer = 1
    for field, value in yours.items():
        if field[:len(string)] == string:
            answer *= value
    if answer == 1:
        return 0
    else:
        return answer


def print_dict(title, dict):
    print()
    print(title)
    for key, value in dict.items():
        print(key, value)


if __name__ == '__main__':
    filename = 'day_16.txt'
    ranges_lines = 20

    # Read in fields, allowable ranges and tickets
    fields, range_minimums, range_maximums, your_ticket, other_tickets = load_input(filename, ranges_lines)
    # other ticket indicies: [ticket][field]

    # Remove bad tickets
    good_tickets = remove_bad_tickets(other_tickets)

    # rearrange range mins/max by field
    field_rules = defaultdict(list)
    for index, (i, j) in enumerate(zip(range_minimums, range_maximums)):
        field_rules[fields[index // 2]].append((i, j))

    # First pass of possible locations of fields
    possible_fields = get_possible_fields(field_rules, good_tickets)

    # Algorithm to find actual positions
    actual_fields = get_fields(possible_fields)

    # convert your ticket
    yours = convert_ticket_to_dict(your_ticket, actual_fields)

    # Get the answer
    answer = get_answer(yours, 'departure')
    print('\nAnswer part 2:', answer)
