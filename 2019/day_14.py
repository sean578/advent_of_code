import math


def get_data_into_dict(filename):
    f = open(filename)

    the_inputs = []
    the_outputs = []

    # Get the equations from file into inputs and output elements & amounts
    for line in f.readlines():
        react_ins, react_out = line.strip().split(' => ')
        react_ints_list = react_ins.split(', ')
        the_inputs.append([i.split(' ') for i in react_ints_list])
        react_out_num, react_out_substance = react_out.split(' ')
        the_outputs.append([int(react_out_num), react_out_substance])

    # Convert input amounts to ints
    for i, equation in enumerate(the_inputs):
        for j, pair in enumerate(equation):
            the_inputs[i][j][0] = int(pair[0])

    # Put the equations into dictionary form
    equations = {}
    for key, value in zip(the_outputs, the_inputs):
        equations[key[1]] = tuple([value, key[0]])

    return equations


def print_dict(dict):
    for key, value in dict.items():
        print(key, value)
    print('\n')


def substitute_reaction(to_replace, reaction_dict, convert_to_ore=False):
    element = to_replace
    to_insert = reaction_dict[element[1]]
    # multiply compounds by amount required:
    to_insert_correct_ammount = []
    for pair in to_insert[0]:
        if pair[1] != 'ORE' or convert_to_ore:
            multiplier = math.ceil(element[0] / to_insert[1])
            # print('amounts...', element[0], to_insert[1])
            # print('multiplier', multiplier)
            pair[0] *= multiplier
            to_insert_correct_ammount.append(pair)
        else:
            to_insert_correct_ammount.append(element)

    return to_insert_correct_ammount


def combine_elements(a_reaction_list):
    combined_list = []
    names = set([sublist[1] for sublist in a_reaction_list])
    reaction_list_dict = dict.fromkeys(names, 0)
    for element in a_reaction_list:
        reaction_list_dict[element[1]] += element[0]
    for key, value in reaction_list_dict.items():
        combined_list.append([value, key])

    return combined_list

"""
Rections: 
key: element to make
value[0]: list of amount, element pairs required
value[1]: amount of element made
"""

reactions = get_data_into_dict('day_14.txt')
print('Initial reaction equations:\n')
print_dict(reactions)

index = 0
reaction_list = [[1, 'FUEL']]

for x in range(10):

    print('########################')
    # print('reaction_list', reaction_list)

    reaction_list_next = []
    index=0
    for i in reaction_list:
        # print('\ni', i)
        if i[1] != 'ORE':
            reaction_list_next.extend(substitute_reaction(i, reactions))
        else:
            reaction_list_next.extend(i)
        elements_combined = combine_elements(reaction_list_next)
        # if len(elements_combined) != len(reaction_list_next):
        #     break
        reaction_list_next = elements_combined
    reaction_list = reaction_list_next

print('\nreaction_list_before conversion to ore\n', reaction_list_next)

reaction_list_final = []
for i in reaction_list_next:
    reaction_list_final.extend(substitute_reaction(i, reactions, convert_to_ore=True))
reaction_list_final = combine_elements(reaction_list_final)
print('\nreaction_list_final\n', reaction_list_final)

