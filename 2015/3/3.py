filename = 'input.txt'

input_file = open(filename, 'r')

instructions = input_file.read()
input_file.close()

current_location = [[0, 0], [0, 0]]  # location of santa, robot

visited_houses = [tuple(current_location[0])]         # list of coordinates presents have been delivered to

santa_robot_flag = 0    # 0: Santa, 1: Robot
for instruction in instructions:
    
    if instruction == '>':
        current_location[santa_robot_flag][0] = current_location[santa_robot_flag][0] + 1 
    elif instruction == 'v':
        current_location[santa_robot_flag][1] = current_location[santa_robot_flag][1] - 1
    elif instruction == '<':
        current_location[santa_robot_flag][0] = current_location[santa_robot_flag][0] - 1
    elif instruction == '^':
        current_location[santa_robot_flag][1] = current_location[santa_robot_flag][1] + 1
    else:
        print('Instruction not recognised: {}'.format(instruction))
        
    if tuple(current_location[santa_robot_flag]) not in visited_houses:
        visited_houses.append(tuple(current_location[santa_robot_flag]))
        
    santa_robot_flag = not santa_robot_flag
          
print(len(visited_houses))


