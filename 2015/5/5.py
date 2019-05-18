input_filename = 'input.txt'

input_file = open(input_filename, 'r')

bad_strings = ('ab', 'cd', 'pq', 'xy')    # Need to check none of these combinations exist
vowels = ('a', 'e', 'i', 'o', 'u')  # Need atleast three of these

number_nice_strings = 0

for line in input_file:
    
    count_vowels = 0
    prev_letter = None
    contains_repeat = False
    contains_bad_string = False
    
    for bad_string in bad_strings:
        if bad_string in line:
            contains_bad_string = True
    
    for letter in line:
        if letter in vowels:
            count_vowels = count_vowels + 1
        if letter == prev_letter:
            contains_repeat = True
        prev_letter = letter
    
    if count_vowels >= 3:
            if contains_repeat:
                if contains_bad_string == False:
                    number_nice_strings = number_nice_strings + 1
                    # print(line)
    
print('Found {} nice strings'.format(number_nice_strings))
