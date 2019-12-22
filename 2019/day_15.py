from intcode_day_15 import IntCode
import numpy as np


def initialise_maze(size):
    maze = np.zeros((size, size), dtype=np.int8)
    current_loc = [size // 2, size // 2]  # y, x
    maze[current_loc[0], current_loc[1]] = 3  # 3 is current location
    return maze, current_loc


def update_map(maze, current_loc, direction, direction_dict, status, status_codes):
    """
    Current location: y, x
    """
    new_loc = [None, None]

    if status_codes[status] == 'finished':
        print('Program complete')
        return maze, current_loc

    if direction_dict[direction] == 'north':
        new_loc[0] = current_loc[0] - 1
        new_loc[1] = current_loc[1]
    elif direction_dict[direction] == 'south':
        new_loc[0] = current_loc[0] + 1
        new_loc[1] = current_loc[1]
    elif direction_dict[direction] == 'west':
        new_loc[1] = current_loc[1] - 1
        new_loc[0] = current_loc[0]
    elif direction_dict[direction] == 'east':
        new_loc[1] = current_loc[1] + 1
        new_loc[0] = current_loc[0]

    # Update the map
    # If moving then change droid location
    if status_codes[status] != 'hit_wall':
        maze[current_loc[0], current_loc[1]] = 2  # droid has been here
        maze[new_loc[0], new_loc[1]] = 3  # Location of the droid
    else:
        maze[new_loc[0], new_loc[1]] = status + 1

    if status_codes[status] == 'hit_wall':
        print('hit wall')
        return maze, current_loc
    else:
        return maze, new_loc


direction_dict = {
    0: 'north',
    1: 'south',
    2: 'west',
    3: 'east'
}

status_codes = {
    0: 'hit_wall',  # Not moved
    1: 'moved_step',
    2: 'found_oxygen',  # Moved step prior to this
    99: 'finished'
}

# Instance of an incode machine
program = IntCode('day_15.txt')

# Initialise a map of the maze
maze, current_loc = initialise_maze(15)

direction = 0  # intitial direction
status = 0
# while status_codes[status] != 'finished':
# for _ in range(15):
while True:
    direction = int(input('Direction...'))
    program.input_values.append(direction+1)  # Provide an input instruction
    print(direction_dict[direction])
    program.command()  # Get program to move droid
    # if len(program.input_values) > 0:
    #     raise Exception('Not used all input values')
    # print('output', program.output_values)
    status = program.output_values.pop(0)  # Get the status of the repair droid
    # if len(program.output_values) > 0:
    #     if program.output_values.pop(0) == 99:
    #         break
    #     else:
    #         raise Exception('Not used all output values')
    maze, current_loc = update_map(maze,
                                   current_loc,
                                   direction,
                                   direction_dict,
                                   status,
                                   status_codes)
    # print(status_codes[status])


    print(maze)

