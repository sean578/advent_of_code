# conversions = [
#     ['e', 'H'],
#     ['e', 'O'],
#     ['H', 'HO'],
#     ['H', 'OH'],
#     ['O', 'HH']
# ]

conversions_as_dict = {
    'e': ['H', 'O'],
    'H': ['HO', 'OH'],
    'O': ['HH']
}


def replace_substring(string, index, replacement, num_to_replace):
    # Works for replacement of a single character

    string_as_list = list(string)
    string_as_list[index] = replacement
    del string_as_list[index+1:index+num_to_replace]
    return ''.join(string_as_list)


def recursive_fn(current_molecule, required_molecule, conversions):
    print('current_molecule', current_molecule)
    if current_molecule == required_molecule:
        return current_molecule
    else:
        for index, letter in enumerate(current_molecule):
            for conv in conversions[letter]:
                print('conv', conv)
                # do the conversion
                current_molecule = replace_substring(current_molecule, index, conv, 1)
                # recursive call
                recursive_fn(current_molecule, required_molecule, conversions)


def normal_fn(initial_molecule, required_molecule, conversions):

    index = 0
    current_molecule = initial_molecule
    while current_molecule != required_molecule:
        for conv in conversions[current_molecule[index]]:
            # replace
            current_molecule = replace_substring(current_molecule, index, conv, 1)
            print(current_molecule)
        index = index + 1



normal_fn('e', 'HH', conversions_as_dict)
