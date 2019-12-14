import numpy as np
import matplotlib.pyplot as plt
from intcode_day_11 import IntCode


class Painter:

    def __init__(self, array_size):
        self.array_size = array_size
        self.current_dir = 0
        self.coords_visited = []
        # self.current_pos = [self.array_size // 2, self.array_size // 2]
        self.current_pos = [10, 10]
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

        if self.current_dir > 3 or self.current_dir < 0:
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

    def paint(self, color_to_paint):
        self.painting[self.current_pos[0], self.current_pos[1]] = color_to_paint
        self.painting_to_view[self.current_pos[0], self.current_pos[1]] = color_to_paint

    def get_current_color(self):
        self.current_color = self.painting[self.current_pos[0], self.current_pos[1]]


intcode = IntCode('day_11.txt')  # Initialise the program
painter = Painter(array_size=100)  # Painting robot

loop = 0
while True:
    # Get current tile color - provide copies to intcode intput queue
    painter.get_current_color()
    intcode.input_values.append(painter.current_color)

    # Ask for instruction on how to paint current tile and how to move
    while len(intcode.output_values) < 2:
        intcode.command()
    if 99 in intcode.output_values:
        break
    new_color = intcode.output_values.pop(0)
    new_dir = intcode.output_values.pop(0)

    painter.paint(new_color)  # Use the new color to paint the current tile
    painter.move(new_dir)  # Use the new direction to move the robot

    # painter.append_to_locations()  # If this is a new location, add to list

    # Reset intocode input/output queues
    intcode.input_values = []
    intcode.output_values = []

    loop += 1

# print(painter.coords_visited)
# print(len(painter.coords_visited))
print(loop)
plt.imshow(painter.painting_to_view, cmap='gray', origin='lower')
plt.show()
