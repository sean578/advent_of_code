from intcode_day_13 import IntCode
import numpy as np
np.set_printoptions(linewidth=400)

intcode = IntCode('day_13_part_2.txt')  # Initialise the program


def setup_screen(y, x):
    return np.zeros((y, x), dtype=np.int32)


def get_screen_data(data, screen):
    i = 0
    data_as_list = []
    while i < len(data):
        if data[i] == -1 and data[i + 1] == 0:
            print('score', data[i + 2])
        else:
            data_as_list.append(data[i:i + 3])
        i = i + 3

    # Create the screen array
    for thing in data_as_list:
        screen[thing[1], thing[0]] = thing[2]

    return screen


# Set up the screen
screen = setup_screen(24, 41)

# Run program until an input is required - input it based on the paddle & ball locations
done = False
while not done:
    intcode.output_values = []
    return_value = intcode.command()
    if 99 in intcode.output_values:
        intcode.output_values.pop(-1)
        done = True
        print('Final score:')
        get_screen_data(intcode.output_values, screen)
    else:
        screen = get_screen_data(intcode.output_values, screen)
        if int(np.where(screen == 4)[1]) < int(np.where(screen == 3)[1]):
            user = -1
        elif int(np.where(screen == 4)[1]) > int(np.where(screen == 3)[1]):
            user = 1
        else:
            user = 0
        intcode.input_values.append(int(user))

