string = str(3113322113)
print('Input string: ', string)

# get the first character
# look how many characters in a row there are
# append to the new string

def create_new_string(string):
    
    new_string = ''
    done = False
    z = 0 # index in input string
    i = 0 # num of same characters
    while z < len(string):
        # print(z, i)
        num_char = 0
        i = 0
        current_char = string[z]
        
        if(z == len(string) - 1):
            new_string = new_string + str(1)
            new_string = new_string + str(current_char)
            z = z + 1
        else:
        
            while string[z+i] == current_char and done == False:
                num_char = num_char + 1
                if i + z < len(string)-1:
                    i = i + 1
                    # z = z + 1
                else:
                    done = True
            z = z + i
            
           #  if done == False:
            # print('num_char, char', num_char, current_char)
            new_string = new_string + str(num_char)
            new_string = new_string + str(current_char)
                
    return new_string


for _ in range(50):
    string = create_new_string(string)
    # print(string)
    
print('Length of output string: ', len(string))
    