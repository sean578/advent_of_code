import re

input_filename = 'input.txt'

input_file = open(input_filename, 'r')
number_nice_strings = 0

def check_if_good_string(string):
    
    # Match repeats of two letters:
    match_1 = re.search(r'([a-z][a-z]).*\1', string)
    
    # Match repeated letters with one in between:
    match_2 = re.search(r'([a-z]).\1', string)
    
    return match_1 and match_2

number_good_strings = 0
for line in input_file:
    if check_if_good_string(line):
        number_good_strings = number_good_strings + 1
        
print(number_good_strings)