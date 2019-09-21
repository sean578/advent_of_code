import numpy as np

the_aunt = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

input_data = open('input.txt')

#########################################################################
# Get the data in as array
#########################################################################

sues = []
for line in input_data:
    temp = line.strip('\n').split(', ')
    temp[0] = temp[0].split(': ')[1] + ': ' + temp[0].split(': ')[2]
    sues.append(temp)

#########################################################################
# Get the elements as dictionaries
#########################################################################

sues_as_dict = []
for sue in sues:
    temp_dict = {}
    for param in sue:
        temp_array = param.split(': ')
        temp_dict[temp_array[0]] = temp_array[1]
    sues_as_dict.append(temp_dict)

#########################################################################
# Test each sue for a match
#########################################################################

aunt_number = 0
for sue in sues_as_dict:
    aunt_number = aunt_number + 1
    match = True
    for key, value in sue.items():
        # print(value)
        if key == 'cats' or key == 'trees':
            if the_aunt[key] < int(value):
                pass
            else:
                match = False
        elif key == 'pomeranians' or key == 'goldfish':
            if the_aunt[key] > int(value):
                pass
            else:
                match = False
        else:
            if the_aunt[key] == int(value):
                pass
            else:
                match = False
    if match:
        print('aunt_number', aunt_number)
        print(sue.items())
