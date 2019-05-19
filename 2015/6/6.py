import numpy as np

input_filename = 'input.txt'

# example input line:
# turn on 489,959 through 759,964
# toggle

def get_instruction(instruction_array):
    
    if instruction_array[0] == 'toggle':
        return 2
    elif instruction_array[1] == 'on':
        return 1
    else:
        return 0
    
def get_indices(instruction_array):
    if len(instruction_array) == 5:
        start = instruction_array[2].strip().split(',')
        start = list(map(int, start))
        stop = instruction_array[4].strip().split(',')
        stop = list(map(int, stop))
    else:
        start = instruction_array[1].strip().split(',')
        start = list(map(int, start))
        stop = instruction_array[3].strip().split(',')
        stop = list(map(int, stop))
        
    return start, stop
        
def set_sub_array(start_indices, stop_indices, the_array, value):
    the_array[start_indices[0]:stop_indices[0]+1, start_indices[1]:stop_indices[1]+1] = value
    return the_array

def toggle_sub_array(start_indices, stop_indices, the_array):
    the_array[start_indices[0]:stop_indices[0]+1, start_indices[1]:stop_indices[1]+1] = np.invert(the_array[start_indices[0]:stop_indices[0]+1, start_indices[1]:stop_indices[1]+1])
    return the_array

    
the_lights = np.zeros((1000, 1000), dtype = np.bool)
input_data = open(input_filename)

for line in input_data:
    instruction_array = line.split(' ')
    code = get_instruction(instruction_array)
    start, stop = get_indices(instruction_array)
    
    if code == 2:
        the_lights = toggle_sub_array(start, stop, the_lights)
    else:
        the_lights = set_sub_array(start, stop, the_lights, code)

print( 'Number of lights on = {}'.format(np.count_nonzero(the_lights)))