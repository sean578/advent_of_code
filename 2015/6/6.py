input_filename = 'input.txt'

# example input line:
# turn on 489,959 through 759,964
# toggle

def get_instruction(instruction_array):
    
    if instruction_array[0] == 'toggle':
        return 0
    elif instruction_array[1] == 'on':
        return 1
    else:
        return 2
    
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
        
    print(start)
    print(stop)

input_data = open(input_filename)

for line in input_data:
    instruction_array = line.split(' ')
    code = get_instruction(instruction_array)
    get_indices(instruction_array)
