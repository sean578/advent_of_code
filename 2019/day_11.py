import numpy as np
import matplotlib.pyplot as plt
from intcode_day_11 import IntCode


class Painter:

    def __init__(self, array_size):
        self.array_size = array_size
        self.current_dir = 0
        self.coords_visited = []
        self.current_pos = [self.array_size // 2, self.array_size // 2]
        self.painting = np.zeros((self.array_size, self.array_size), dtype=np.int64)
        self.painting_to_view = 2*np.ones((self.array_size, self.array_size), dtype=np.int64)
        self.painting[self.current_pos[0], self.current_pos[1]] = 1  # Start on a white tile for the second part
        self.painting_to_view[self.current_pos[0], self.current_pos[1]] = 1  # Start on a white tile for the second part
        self.current_color = self.painting[self.current_pos[0], self.current_pos[1]]  # Check this indexing works

        print('Initial position\t', self.current_pos)
        print('Initial color\t\t', self.current_color)

    def append_to_locations(self):
        coords_around_zero = (self.current_pos[0] - self.array_size // 2,
                              self.current_pos[1] - self.array_size // 2)
        if coords_around_zero not in self.coords_visited:
            self.coords_visited.append(coords_around_zero)

    def move(self, dir_to_turn):
        # Get the new robot direction
        if dir_to_turn == 1:
            self.current_dir += 1
        elif dir_to_turn == 0:
            self.current_dir -= 1
        else:
            raise Exception('Incorrect robot direction receieved')

        self.current_dir %= 4

        # Move in that direction
        if self.current_dir == 0:
            self.current_pos[0] += 1
        elif self.current_dir == 1:
            self.current_pos[1] += 1
        elif self.current_dir == 2:
            self.current_pos[0] -= 1
        elif self.current_dir == 3:
            self.current_pos[1] -= 1
        else:
            raise Exception('Incorrect direction')

        if self.current_pos[0] <= 0 or self.current_pos[1] <= 0:
            raise Exception('Position outside of array')

    def paint(self, color_to_paint):
        if color_to_paint not in (0, 1):
            raise Exception('Incorrect color to paint')
        self.painting[self.current_pos[0], self.current_pos[1]] = color_to_paint
        self.painting_to_view[self.current_pos[0], self.current_pos[1]] = color_to_paint

    def get_current_color(self):
        color = self.painting[self.current_pos[0], self.current_pos[1]]
        if color not in (0, 1):
            raise Exception('Current color incorrect')
        self.current_color = color


try:
    intcode = IntCode('day_11.txt')  # Initialise the program
except:
    raise Exception('Cannot read program file')

painter = Painter(array_size=200)  # Painting robot

while True:
    # Get current tile color - provide copies to intcode intput queue

    if len(intcode.input_values) > 0:
        raise Exception('Not all input values used')

    painter.get_current_color()
    intcode.input_values.append(painter.current_color)

    # Ask for instruction on how to paint current tile and how to move
    intcode.command()
    intcode.command()
    if 99 in intcode.output_values:
        break
    print('output vals', intcode.output_values)
    new_color = intcode.output_values.pop(0)
    new_dir = intcode.output_values.pop(0)

    if len(intcode.output_values) > 0:
        raise Exception('Too many output values produced')

    painter.paint(new_color)  # Use the new color to paint the current tile
    painter.move(new_dir)  # Use the new direction to move the robot
    painter.append_to_locations()  # If this is a new location, add to list

# print(painter.coords_visited)
# print(len(painter.coords_visited))

plt.imshow(painter.painting, cmap='gray', origin='lower')
plt.show()
