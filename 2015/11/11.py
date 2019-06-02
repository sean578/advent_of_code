import re

def increment_string(string):
    bytes_as_a_list = list(bytes(string, 'ascii'))
    
    incremented = False
    i = -1
    while incremented == False:
        if bytes_as_a_list[i] < 122:
            bytes_as_a_list[i] = bytes_as_a_list[i] + 1
            incremented = True
        else:
            bytes_as_a_list[i] = 97
            i = i - 1
    
    return bytes(bytes_as_a_list).decode("ascii") 

def check_for_3_increasing_letters(string):
    bytes_string = bytes(string, 'ascii')
    matched = False
    for i in range(len(string) - 2):
        if bytes_string[i] == bytes_string[i+1] - 1:
            if bytes_string[i] == bytes_string[i+2] - 2:
                matched = True
    return matched

def check_no_disallowed_letters(string):
    if re.search(r'[iol]', string):
        return False
    else:
        return True

def check_for_two_nonoverlapping_pairs(string):
    if re.search(r'([a-z])\1[a-z]*([a-z])\2', string):
        return True
    else:
        return False
    
#################################################################
#################################################################
#################################################################
        
string_old = 'cqjxjnds'
string = increment_string('cqjxxyzz')

#for i in range(3):
#    print(string)
#    string = increment_string(string)

found_good_string = False
while found_good_string == False:
    # print(string)
    if check_no_disallowed_letters(string) and check_for_two_nonoverlapping_pairs(string) and check_for_3_increasing_letters(string):
        found_good_string = True  
        print(string)          
    else:
        string = increment_string(string)
        


