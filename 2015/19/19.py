import re

input_file = open('input.txt')


def replacements_into_dict(file):

    convert_one_letter = []
    convert_two_letter = []

    for line in input_file:
        conversion = line.strip('\n').split(' => ')
        if len(conversion[0]) == 1:
            convert_one_letter.append([conversion[0], conversion[1]])
        elif len(conversion[0]) == 2:
            convert_two_letter.append([conversion[0], conversion[1]])
        else:
            if len(line) > 1:
                print('Reached last line of file')
                input_molecule = line.strip('\n')

    return convert_one_letter, convert_two_letter, input_molecule


def find_indices_of_match(string, substring):

    index_list = []
    for match in re.finditer(string, substring):
        index_list.append(match.start())

    return index_list


def replace_substring(string, index, replacement, num_to_replace):
    # Works for replacement of a single character

    string_as_list = list(string)
    string_as_list[index] = replacement
    del string_as_list[index+1:index+num_to_replace]
    return ''.join(string_as_list)


convert_1, convert_2, molecule = replacements_into_dict(input_file)

print('\nConvert 1 letter:')
for key, value in convert_1:
    print(key, value)

print('\nConvert 2 letter:')
for key, value in convert_2:
    print(key, value)

print('\nInput molecule:\n')
print(molecule)

# All the new molecules
molecules_out = []

# Do the replacements of 1 letter:
for to_replace, replacement in convert_1:
    for index in find_indices_of_match(to_replace, molecule):
        new_molecule = replace_substring(molecule, index, replacement, len(to_replace))
        molecules_out.append(new_molecule)

# Do the replacements of 2 letters:
for to_replace, replacement in convert_2:
    for index in find_indices_of_match(to_replace, molecule):
        new_molecule = replace_substring(molecule, index, replacement, len(to_replace))
        molecules_out.append(new_molecule)

print(len(molecules_out))
print(len(set(molecules_out)))





# print('testing find function')
# string = 'hello'
# substring = 'll'
# replacement = 'pop'
#
# for index in find_indices_of_match(substring, string):
#     print(replace_substring(string, index, replacement, len(substring)))



