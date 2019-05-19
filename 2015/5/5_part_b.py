input_filename = 'input.txt'

input_file = open(input_filename, 'r')
number_nice_strings = 0

test_string = 'ieodomkazucvgmuy'

for line in input_file:
    good_string_nn = False
    good_string_n2 = False
    nn_pairs = []
    n2_pairs = []
    line = line.strip()  
    #line = test_string
        
    # Get the nearest neighbour pairs into a list
    for i in range(len(line) - 1):
        nn_pairs.append(line[i:i+2])
        
    # Get the nearest by 2 neighbour pairs into a list
    for i in range(len(line) - 2):
        n2_pairs.append(line[i:i+3:2])
    
    # Find any duplicates in the nn pair list
    # !!! Don't want repeats which are next to each other in list
    # print(nn_pairs)
    for i in nn_pairs:
        if nn_pairs.count(i) > 1:
            if nn_pairs[nn_pairs.index(i) + 1] != i:
                good_string_nn = True
            
    # Find any repeating characters in each element of the n2 pair list
    for i in n2_pairs:
        # print(n2_pairs.count(i))
        if i[0] == i[1]:
            good_string_n2 = True
            # print('Bad n2 found')
    
    if good_string_nn and good_string_n2:
        print('Good string:\t {}'.format(line))
        number_nice_strings = number_nice_strings + 1
    else:
        print('Bad string:\t {}'.format(line))
            
print('Found {} nice strings'.format(number_nice_strings))
