import numpy as np
import matplotlib.pyplot as plt


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
    if value == 1:
        the_array[start_indices[0]:stop_indices[0]+1, start_indices[1]:stop_indices[1]+1] = the_array[start_indices[0]:stop_indices[0]+1, start_indices[1]:stop_indices[1]+1] + 1
    else:
        the_array[start_indices[0]:stop_indices[0]+1, start_indices[1]:stop_indices[1]+1] = the_array[start_indices[0]:stop_indices[0]+1, start_indices[1]:stop_indices[1]+1] - 1
        the_array = np.clip(the_array, 0, 2147483647)
        print(the_array)
    return the_array

def toggle_sub_array(start_indices, stop_indices, the_array):
    the_array[start_indices[0]:stop_indices[0]+1, start_indices[1]:stop_indices[1]+1] = the_array[start_indices[0]:stop_indices[0]+1, start_indices[1]:stop_indices[1]+1] + 2
    return the_array

    
the_lights = np.zeros((1000, 1000), dtype = np.int)
input_data = open(input_filename)

for line in input_data:
    instruction_array = line.split(' ')
    code = get_instruction(instruction_array)
    start, stop = get_indices(instruction_array)
    
    if code == 2:
        the_lights = toggle_sub_array(start, stop, the_lights)
    else:
        the_lights = set_sub_array(start, stop, the_lights, code)

print( 'Number of lights on = {}'.format(np.sum(the_lights)))
print('Number of lights less than zero: {}'.format(np.sum(the_lights < 0)))

plt.imshow(the_lights, interpolation='none')
plt.colorbar()