input_file_name = 'input.txt'

input_file = open(input_file_name, "r")
data = input_file.read()

floor = 0   
for position, transition in enumerate(data):
    if transition == '(':
        floor = floor + 1
    elif transition == ')':
        floor = floor - 1
    else:
        print('incorrect character: {}'.format(transition))
        
    if floor == -1:
        print(position + 1)
            
